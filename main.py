from e_drone.drone import *
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import numpy as np
import cv2

# -----------------------------
# HSV thresholds 
# -----------------------------
HSV_BLUE_L = (95, 0, 50)
HSV_BLUE_U = (110, 255, 250)

HSV_RED_L = (0, 0, 5)
HSV_RED_U = (17, 255, 240)

HSV_PUR_L = (110, 0, 5)
HSV_PUR_U = (140, 255, 50)

# -----------------------------
# Sate
# -----------------------------
ST_APPROACH_RING = 0   # 링 탐색 + 접근
ST_CENTERING     = 1   # 링 중심 정렬
ST_INSIDE_CHECK  = 2   # 링 내부에서 표식 확인/행동

# -----------------------------
# 마스크 + bbox/center
# -----------------------------
def mask_inrange(hsv, low, high, blur_ksize=0):
    m = cv2.inRange(hsv, low, high)
    if blur_ksize and blur_ksize >= 3:
        m = cv2.medianBlur(m, blur_ksize)
    return m

def bbox_center_from_mask(mask, min_pixels=250):
    ys, xs = np.where(mask == 255)
    pix = xs.size
    if pix < min_pixels:
        return None
    minx = int(xs.min()); maxx = int(xs.max())
    miny = int(ys.min()); maxy = int(ys.max())
    cx = (minx + maxx) // 2
    cy = (miny + maxy) // 2
    return (minx, maxx, miny, maxy, cx, cy, int(pix))

# -----------------------------
# 제어: 중심 오차 -> 이동 명령 (Deadband 기반)
# sendControlPosition16(x, y, z, v, yaw, a) 사용
# -----------------------------
def step_centering(drone, cx, cy, w, h, band_x=35, band_y=35):
    tx, ty = w // 2, h // 2
    err_x = cx - tx
    err_y = cy - ty

    # 좌우(y) 보정
    if err_x > band_x:
        drone.sendControlPosition16(0, -1, 0, 2, 0, 0)  # 오른쪽이면 왼쪽으로
        sleep(0.25)
        return False
    if err_x < -band_x:
        drone.sendControlPosition16(0, 1, 0, 2, 0, 0)   # 왼쪽이면 오른쪽으로
        sleep(0.25)
        return False

    # 상하(z) 보정 (부호는 환경 따라 반대일 수 있음)
    if err_y > band_y:
        drone.sendControlPosition16(0, 0, -1, 2, 0, 0)
        sleep(0.25)
        return False
    if err_y < -band_y:
        drone.sendControlPosition16(0, 0, 1, 2, 0, 0)
        sleep(0.25)
        return False

    return True

def step_forward(drone, dist_level="mid"):
    # 전진량을 3단계 사용
    if dist_level == "far":
        drone.sendControlPosition16(10, 0, 0, 6, 0, 0)
        sleep(3.5)
    elif dist_level == "mid":
        drone.sendControlPosition16(7, 0, 0, 5, 0, 0)
        sleep(3.0)
    else:  # "near"
        drone.sendControlPosition16(4, 0, 0, 4, 0, 0)
        sleep(2.2)

# -----------------------------
# 링 크기 기반 거리/내부 판단
# -----------------------------
def ring_distance_level(bbox, w, h):
    minx, maxx, miny, maxy, cx, cy, pix = bbox
    bw = maxx - minx
    bh = maxy - miny
    # 화면 대비 링 크기
    scale = max(bw / float(w), bh / float(h))

    if scale < 0.18:
        return "far"
    elif scale < 0.35:
        return "mid"
    else:
        return "near"

def is_inside_ring(bbox, w, h):
    minx, maxx, miny, maxy, cx, cy, pix = bbox
    bw = maxx - minx
    bh = maxy - miny

    # 링 테두리가 거의 안 보이면 bbox가 갑자기 작아지는 경향
    if bw < 60 or bh < 60:
        return True
    # 또는 중심이 거의 화면 중앙이고 크기가 near였다가 급감하는 경우 등을 추가 가능
    return False

# -----------------------------
# 표식 처리
# -----------------------------
def do_turn_and_pass(drone):
    # 회전 + 전진 + 약간 상승(기존과 달리 수치/순서 약간 변경)
    drone.sendControlPosition16(0, 0, 0, 0, 90, 20)
    sleep(5.5)
    drone.sendControlPosition16(9, 0, 0, 5, 0, 0)
    sleep(4.0)
    drone.sendControlPosition16(0, 0, 1, 3, 0, 0)
    sleep(1.5)

# -----------------------------
# main
# -----------------------------
def main():
    drone = Drone()
    drone.open()

    level = 1
    state = ST_APPROACH_RING

    # 안정화 카운터
    center_ok_cnt = 0
    inside_cnt = 0
    mark_ok_cnt = 0

    try:
        drone.sendTakeOff()
        sleep(5)

        # 초기 탐색용 전진
        drone.sendControlPosition16(8, 0, 0, 5, 0, 0)
        sleep(4)

        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        raw = PiRGBArray(camera, size=(640, 480))
        sleep(1)

        for frame in camera.capture_continuous(raw, format='bgr', use_video_port=True):
            img = frame.array
            raw.truncate(0)

            img = cv2.flip(img, 0)
            img = cv2.flip(img, 1)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h, w = img.shape[:2]

            # 파란 링 마스크 + 블러
            m_blue = mask_inrange(hsv, HSV_BLUE_L, HSV_BLUE_U, blur_ksize=17)
            blue_bbox = bbox_center_from_mask(m_blue, min_pixels=400)

            # 링이 안 보일 경우
                if pur_bbox is not None:
                    mark_ok_cnt += 1
                    if mark_ok_cnt >= 2 or level >= 3:
                        drone.sendLanding()
                        break
                    continue

                # 빨강이 보이면 회전 후 다음 레벨
                if red_bbox is not None and level < 3:
                    mark_ok_cnt += 1
                    if mark_ok_cnt >= 2:
                        do_turn_and_pass(drone)
                        level += 1
                        state = ST_APPROACH_RING
                        mark_ok_cnt = 0
                    continue

                # 아무 표식도 안 보이면: 짧게 전진하며 재탐색
                mark_ok_cnt = 0
                drone.sendControlPosition16(2, 0, 0, 3, 0, 0)
                sleep(0.25)
                continue

    except Exception as e:
        print("exception:", e)
        try:
            drone.sendLanding()
            sleep(2)
        except:
            pass
    finally:
        drone.close()

if __name__ == "__main__":
    main()
