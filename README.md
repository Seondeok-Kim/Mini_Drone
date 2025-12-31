# Mini Drone
<!--
https://www.youtube.com/watch?v=yMJ3bWivwfw&list=PLZlJypPEW-QmJ8V-05h_3_saUJU8ye0pW&index=6
-->
# 드론
<img width="700" height="500" alt="드론2" src="https://github.com/user-attachments/assets/029de597-e55e-49f7-8d34-b61ba6f78355" />
<img width="600" height="800" alt="드론" src="https://github.com/user-attachments/assets/f3736eaf-a411-43ec-8c2f-78d684dcbcfb" />

- 모델명: 코드론 DIY

# 부속품
![2](https://user-images.githubusercontent.com/76850241/194635996-befd44cd-61ba-45d0-82b2-569eb74162ae.PNG)


# 드론 펌웨어 업데이트 
<!--
![1](https://user-images.githubusercontent.com/76850241/194636011-ac5da568-4fd7-42c5-aa80-25c7db9b6957.PNG)
-->
1. 로보링크 홈페이지 접속
2. 홈페이지 상단 오른쪽 'Download'-> 한글
3. 허밍버드 선택 -> '펌웨어 Download'
4. 다운받은 파일 압축 해제 -> 'Drone4AutoUpdaterLight' 파일 실행
5. Drone 버튼 누르면서 컴퓨터와 연결
6. 펌웨어 업데이트 진행


# Raspberry Pi Zero W
<!--
![3](https://user-images.githubusercontent.com/76850241/194636345-5931b677-5547-47f3-bf41-9ee8ea09fad3.PNG)
-->
<img width="600" height="600" alt="Raspberri Pi Zero W" src="https://github.com/user-attachments/assets/cc616ff6-5b95-4a75-b4b9-1bb21f41a418" />

- 1GHz single-core CPU
- 512MB RAM
- Mini HDMI port
- Micro USB OTG port
- Micro USB power
- HAT-compatible 4-pin header
- Composite video and reset headers
- CSI camera connector (v1.3 only)

<!--
USB포트와 Power포트가 비슷하게 생김. power포트에 충전기를 연결해야 함. USB포트에 연결하게 되면 라즈베리 파이의 손상 우려가 있음. 
USB 포트에 컴퓨터와 연결을 하면 자동으로 전원이 인가되고 데이터를 주고받을 수 있음
-->

# Raspberry Pi Zero W 환경 구축

  ## OS설치
 <!-- 
  ![4](https://user-images.githubusercontent.com/76850241/194636895-9e2759d7-00fb-4a2e-b639-dddbcaba2174.PNG)
  
  ![5](https://user-images.githubusercontent.com/76850241/194637184-7fb67d2c-ad98-4000-a1ac-35e23c79b7e0.PNG)
  
  ![6](https://user-images.githubusercontent.com/76850241/194637457-791d748b-d678-473c-abe6-9d0b0d0e44fb.PNG)
  -->
  
  1. SD 카드 포맷
  2. Raspberri Pi 홈페이지 접속
  3. 'Downloads' -> Raspbian
  4. 'Raspbian OS and recommended software' 다운
  5. 다운받은 압축파일 해제 -> 이미지를 SD 카드에 설치
  6. SD 카드의 boot -> cmdline.txt 파일 수정 -> 'rootwait'과 'quiet' 사이 'modules-load=dwc2, g_ether' 입력
  7. 'config.txt' 파일 열고 'detoverlay=dwc2' 맨 아래 입력
  8. SD카드의 boot에 'ssh'파일 생성 (확장자 없음)
  9. SD카드의 boot에 'wpa_supplicant.conf'파일을 생성
  ```conf
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1
  
  network={
      ssid="your_wifiname"
      psk="wifi_password"
      key_mgmt=WPA-PSK
  }
  ```
  10. 'PuTTY'설치
  11. SD카드를 Raspberri Pi에 삽입하고 5pin 전원 연결
  12. 공유기 접속 -> 내부 네트워크에현
<img width="800" height="600" alt="대회맵" src="https://github.com/user-attachments/assets/b63bec0b-3151-486d-b47b-35f0c19fc804" />
<img width="1600" height="800" alt="대회맵" src="https://github.com/user-attachments/assets/aad7d638-db43-41b3-bc76-563aab6a57eb" />








