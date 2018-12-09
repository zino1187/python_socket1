""" 파이썬은 이게 멀티라인 주석이다, #싱글라인 주석 
    그리고 문장의 끝에 세미콜론을 쓰지 않고, {브레이스} 대신 들여쓰기로 표현

gui 프로그래밍은 생각보다 복잡한데, 이렇게 복잡한  gui 프로그래밍을 쉽게 도와주는 도구가 툴킷이다. 

[ 언어별 자주 사용되는 툴킷 ]
 - c/c++ : Qt, wxWidget 
 - tcl 스크립트 언어: tcl/tk
 
 특히 tcl/tk 툴킷을 파이썬 언어에서 사용할 수 있도록,. 바인딩 시켜 제공되는 모듈을 tkinter 라 한다
 from 모듈명 import 함수명
 """
from socket import * 
import threading # 쓰레드 모듈 
from tkinter import *  #2.x 버전 Tkinter ,  3.x 버전 tkinter 

win=Tk() #윈도우 객체 생성

#네트워크 관련 정보 
ip="localhost"
port=9999
address=(ip, port) # 튜플로 묶기 

#제어변수 선언 
receive_msg=StringVar(win)
send_msg=StringVar(win)

#끝없이 청취해야 하므로, 무한루프로 돌려야 하고, 무한루프는 메인
#실행부를 이용해서는 안된다. 왜?? 메인 실행부는 프로그램을 운영
#하고, 각종 이벤트도 감지해야 하는데, 무한루프로 빠지게 하면, 
#프로그램은 멈추게 된다...
def receive():
    print("Im listening now...")
    while True:
        data=client.recv(1024)  
        print("서버의 메세지: ", data.decode("UTF-8"))      
        receive_msg.set(data.decode("UTF-8")) #값을 넣을때는 set()
    client.close() #while 문을 빠져나오면 소켓 닫기

def send():
    print("do you want to send", send_msg.get())
    client.send(bytes(send_msg.get(),"UTF-8"))    

#함수 정의
def makeConnection():
    global thread, client #다른 함수에서 사용할 수 있도록 전역변수로 선언
    print("do you want to connect?")
    client =socket(AF_INET, SOCK_STREAM) # AF_INET : 어디에?? IPV4 주소 체계 사용함, SOCK_STREAM : 어떤 방식으로 통신(프로토콜) TCP
    client.connect(address)
    thread=threading.Thread(target=receive, args=())
    thread.start()


#  제목 컴포넌트 생성
la_from=Label(win, text="전송된 메시지")
la_to=Label(win, text="전송할 메시지")

#  입력 컴포넌트 생성
input_from=Entry(win,textvariable=receive_msg)
input_to=Entry(win, textvariable=send_msg)

#  버튼 컴포넌트 생성
bt_container=Frame(win)
bt_connect = Button(bt_container, text="접속", command=makeConnection)
bt_send = Button(bt_container, text="전송", command=send)

#레이아웃 설정 
la_from.grid(row=0, column=0)
la_to.grid(row=1,column=0)
input_from.grid(row=0, column=1)
input_to.grid(row=1, column=1)

bt_connect.grid(row=0, column=0)
bt_send.grid(row=0, column=1)
bt_container.grid(row=2,columnspan=2)

win.mainloop() #윈도우 루프 (루프가 없으면 윈도우가 잠깐 실행되고 종료)