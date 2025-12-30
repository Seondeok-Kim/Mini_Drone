# Mini Drone

https://www.youtube.com/watch?v=yMJ3bWivwfw&list=PLZlJypPEW-QmJ8V-05h_3_saUJU8ye0pW&index=6
# 드론
<img width="700" height="500" alt="드론2" src="https://github.com/user-attachments/assets/029de597-e55e-49f7-8d34-b61ba6f78355" />
모델명: 코드론 DIY

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


# Raspberry Pi Zero W 스펙
<!--
![3](https://user-images.githubusercontent.com/76850241/194636345-5931b677-5547-47f3-bf41-9ee8ea09fad3.PNG)
-->
<img width="1000" height="900" alt="Raspberri Pi Zero W" src="https://github.com/user-attachments/assets/cc616ff6-5b95-4a75-b4b9-1bb21f41a418" />

1GHz single-core CPU
512MB RAM
Mini HDMI port
Micro USB OTG port
Micro USB power
HAT-compatible 4-pin header
Composite video and reset headers
CSI camera connector (v1.3 only)
<!--
USB포트와 Power포트가 비슷하게 생김. power포트에 충전기를 연결해야 함. USB포트에 연결하게 되면 라즈베리 파이의 손상 우려가 있음. 
USB 포트에 컴퓨터와 연결을 하면 자동으로 전원이 인가되고 데이터를 주고받을 수 있음
-->

# Raspberry Pi Zero 환경구축

  4-1.OS설치
  
  ![4](https://user-images.githubusercontent.com/76850241/194636895-9e2759d7-00fb-4a2e-b639-dddbcaba2174.PNG)
  
  ![5](https://user-images.githubusercontent.com/76850241/194637184-7fb67d2c-ad98-4000-a1ac-35e23c79b7e0.PNG)
  
  ![6](https://user-images.githubusercontent.com/76850241/194637457-791d748b-d678-473c-abe6-9d0b0d0e44fb.PNG)
  
  PuTTY : 윈도우에서 ssh연결을 쉽게 하도록 도와주는 프로그램
  
  공유기가 연결된 노트북과 라즈베리 파이에 IP주소를 할당하므로, 라즈베리파이와 컴퓨터가 같은 공유기의 인터넷 주소를 가지고 있어야 함
  
  라즈베리 홈페이지에서 balena etcher를 설치해서 SD 카드에 라즈베리파이 OS 설치
  
  $ :컴퓨터에 입력하는 명령어



  4-2.serial 통신으로 드론을 제어하는 환경 구축축
  
  PuTTY에 접속해 로그인 성공한 후의 과정
  
  ![7](https://user-images.githubusercontent.com/76850241/194638347-bd06715b-91f4-4ca7-871b-7a09efb13504.PNG)
  
  ![8](https://user-images.githubusercontent.com/76850241/194638540-3f4dccc5-ba38-441e-b6c5-b55bb45a5559.PNG)
  
  
  
  VNC viewer(Virtual Network Computing. 인터넷으로 연결된 컴퓨터에 원격으로 접근)프로그램으로 접속해 Raspberry OS를 이용해 serial 통신으로 드론을 제어하기 위한 환경을 만들어줌




  4-3.카메라를 통해 이미지를 받아올 수 있도록 이미지를 허용해 주는 과정
  
  라즈베리의 카메라와 허밍버드 드론 연결과정
  
  ![10](https://user-images.githubusercontent.com/76850241/194640758-1e3ca7cf-4db3-4db3-9f0c-5c8c7ff125c1.PNG)
  



# 드론을 제어하기 위한 Python 개발환경 구축과정

![9](https://user-images.githubusercontent.com/76850241/194639393-c9a82a56-03dc-4b9e-bcf4-f066571e723e.PNG)



# 최종 허밍버드 드론 모습 & 대회 맵

 ![KakaoTalk_20220727_212523070](https://user-images.githubusercontent.com/76850241/181916277-6ed485a6-9fb8-4041-a126-9c0b05dbd8cd.jpg)<img width="1394" height="692" alt="미니드론_자율비행경진대회_대회맵" src="https://github.com/user-attachments/assets/50add4b4-e962-4c9d-915c-c13b45fbf1fc" />


![KakaoTalk_20220727_212523070_01](https://user-images.githubusercontent.com/76850241/181916281-1da62a58-b4b0-4410-9022-565e19598268.jpg)

![Uploading 미니드론_자율비행경진대회_대회맵.png…]()

