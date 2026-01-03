# Mini Drone
<!--
https://www.youtube.com/watch?v=yMJ3bWivwfw&list=PLZlJypPEW-QmJ8V-05h_3_saUJU8ye0pW&index=6
-->
# 드론
<img width="500" height="300" alt="드론2" src="https://github.com/user-attachments/assets/029de597-e55e-49f7-8d34-b61ba6f78355" />
<img width="400" height="400" alt="드론" src="https://github.com/user-attachments/assets/c31b2793-6abc-4de4-87a1-39afa682adac" />



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
  12. 공유기 접속 -> 내부 네트워크에서 현재 Raspberri Pi의 IP 확인
  13. PuTTY 켠 후 Raspberri Pi의 IP 입력 후 접속
  14. 최초로그인 (ID: pi, PW: raspberry)

 ## serial 통신으로 드론 제어 환경 구축
   <!--
  PuTTY에 접속해 로그인 성공한 후의 과정
  
  ![7](https://user-images.githubusercontent.com/76850241/194638347-bd06715b-91f4-4ca7-871b-7a09efb13504.PNG)
  
  ![8](https://user-images.githubusercontent.com/76850241/194638540-3f4dccc5-ba38-441e-b6c5-b55bb45a5559.PNG)
  -->
  15. 다음 명령어 입력해 업데이트 진행
  ```conf    
    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo reboot
 ```
  16. 다시 Raspberri에 접속해 다음 입력
 ```conf
    $ sudo raspi-config
 ```
  17. Interfacing Option을 선택해 P3 VNC를 enable로 바꿈
  18. 컴퓨터에 VNC viewer를 설치해 PuTTY와 같이 접속
  19. VNC viewer -> Raspberri 아이콘
  20. Serial Port Enable, Serial Console을 Disable
  21. Terminal을 켠 후 config.txt 수정
  22. 다음 입력
  ```conf
  # disable Bluetooth
  dtoverlay=pic-disable-bt
  ```

  <!--
  VNC viewer(Virtual Network Computing. 인터넷으로 연결된 컴퓨터에 원격으로 접근)프로그램으로 접속해 Raspberry OS를 이용해 serial 통신으로 드론을 제어하기 위한 환경을 만들어줌
  -->



  ## 카메라를 통해 이미지를 받아올 수 있도록 이미지를 허용해 주는 과정

  라즈베리의 카메라와 허밍버드 드론 연결과정
  <!--
  ![10](https://user-images.githubusercontent.com/76850241/194640758-1e3ca7cf-4db3-4db3-9f0c-5c8c7ff125c1.PNG)
   -->
 23. VNC viewer -> Raspberri 아이콘
 24. Camera Enable
 ```conf
 Preferences > Raspberri Pi Configuration > interfaces
 ```
  25. Terminal을 켠 후 카메라 장착 확인
  ```conf
  $ vcgencmd get_camera ---> supported = 1 detected = 1
  ```


## 드론을 제어하기 위한 Python 개발환경 구축과정
<!--
![9](https://user-images.githubusercontent.com/76850241/194639393-c9a82a56-03dc-4b9e-bcf4-f066571e723e.PNG)
-->
1. PuTTY / VNC의 Terminal을 이용해 다음 입력
 ```conf
  $ sudo apt-get install libatlas-base-dev
  $ pip3 install e_drone 
  $ pip3 install --upgrade e_drone
 ```  
2. PuTTY / VNC의 Terminal을 이용해 다음 입력
 ```conf
  $ echo 'deb [trusted=yes] http://dl.bintray.com/yoursunny/PiZero stretch-backports main' |\
    sudo tee /etc/apt/sources.list.d/bintray-yoursunny-PiZero.list
  $ sudo apt update
  $ sudo apt install python3-opencv
  $ python3 -c 'import cv2; print(cv2.__version__)' --> 3.2.0
 ``` 

# 대회 환경

<img width="600" height="600" alt="대회맵" src="https://github.com/user-attachments/assets/b63bec0b-3151-486d-b47b-35f0c19fc804" />
<br><br>
<img width="800" height="600" alt="대회맵" src="https://github.com/user-attachments/assets/24971796-90cd-4bca-aa9d-7cc614419eee" />


