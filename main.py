import time
import tkinter
import tkinter.font
from tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led_red_pin = 16
led_green_pin = 20
led_blue_pin = 21

led_red_pwm_pin = 26
led_green_pwm_pin = 19
led_blue_pwm_pin = 13

buzzer_pin = 18

buzzer_control = False

GPIO.setup(buzzer_pin, GPIO.OUT)
pwmBuzzer = GPIO.PWM(buzzer_pin, 1.0)

scale = [ 262, 294, 330, 349, 392, 440, 494]
twinkle = [1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1, \
           5, 5, 4, 4, 3, 3, 2, 5, 5, 4, 4, 3, 3, 2, \
           1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1]
GPIO.setup(led_red_pin, GPIO.OUT)
GPIO.setup(led_green_pin, GPIO.OUT)
GPIO.setup(led_blue_pin, GPIO.OUT)
GPIO.setup(led_red_pwm_pin, GPIO.OUT)
GPIO.setup(led_green_pwm_pin, GPIO.OUT)
GPIO.setup(led_blue_pwm_pin, GPIO.OUT)

pwmRed = GPIO.PWM(led_red_pwm_pin, 500)
pwmGreen = GPIO.PWM(led_green_pwm_pin, 500)
pwmBlue = GPIO.PWM(led_blue_pwm_pin, 500)


class WidgetDemo:
    def __init__(self):
        def led_pwm_window():
            def set_pwm():
                print("set")
                pwmRed.start(0)
                pwmGreen.start(0)
                pwmBlue.start(0)

            def updateRed(duty):
                pwmRed.ChangeDutyCycle(float(duty))
                print(float(duty))

            def updateGreen(duty):
                pwmGreen.ChangeDutyCycle(float(duty))
                print(float(duty))

            def updateBlue(duty):
                pwmBlue.ChangeDutyCycle(float(duty))
                print(float(duty))

            if self.ledControl.get() == "M":
                newWindow = Toplevel(window)
                frame1 = Frame(newWindow)
                frame1.pack()
                set_pwm()
                Label(frame1, text='Red').grid(row=0, column=0)
                Label(frame1, text='Green').grid(row=1, column=0)
                Label(frame1, text='Blue').grid(row=2, column=0)
                scaleRed = Scale(frame1, from_=0, to=100,
                                 orient=HORIZONTAL, command=updateRed)
                scaleRed.grid(row=0, column=1)
                scaleGreen = Scale(frame1, from_=0, to=100,
                                   orient=HORIZONTAL, command=updateGreen)
                scaleGreen.grid(row=1, column=1)
                scaleBlue = Scale(frame1, from_=0, to=100,
                                  orient=HORIZONTAL, command=updateBlue)
                scaleBlue.grid(row=2, column=1)

            elif self.ledControl.get() == "X":
                print("X")
                GPIO.output(led_red_pin, False)
                GPIO.output(led_green_pin, False)
                GPIO.output(led_blue_pin, False)
                self.red_led_state.set("OFF")
                self.green_led_state.set("OFF")
                self.blue_led_state.set("OFF")

            elif self.ledControl.get() == "I":
                GPIO.output(led_red_pin, True)
                time.sleep(1)
                GPIO.output(led_red_pin, False)
                time.sleep(1)
                GPIO.output(led_green_pin, True)
                time.sleep(1)
                GPIO.output(led_green_pin, False)
                time.sleep(1)
                GPIO.output(led_blue_pin, True)
                time.sleep(1)
                GPIO.output(led_blue_pin, False)
                time.sleep(1)
                print("I")

        def led_control_window():
            newWindow = Toplevel(window)
            frame1 = Frame(newWindow)
            frame1.pack()

            self.led_state = IntVar()
            self.led_state.set(1)
            print("state init")
            self.red_led_state = StringVar()
            self.red_led_state.set("OFF")
            self.green_led_state = StringVar()
            self.green_led_state.set("OFF")
            self.blue_led_state = StringVar()
            self.blue_led_state.set("OFF")

            led_on = Radiobutton(frame1, text="LED ON", variable=self.led_state, value=0,
                                 command=self.process_radio_button)
            led_off = Radiobutton(frame1, text="LED OFF", variable=self.led_state, value=1,
                                  command=self.process_radio_button)

            led_on.grid(row=1, column=1)
            led_off.grid(row=1, column=2)

            frame2 = Frame(newWindow)
            frame2.pack()
            label = Label(frame2, text="LED 색을 입력하세요(R/G/B): ")
            self.ledColor = StringVar()
            entry_name = Entry(frame2, textvariable=self.ledColor)
            btn_get_name = Button(frame2, text="실행", command=self.process_button)

            label.grid(row=1, column=1)
            entry_name.grid(row=1, column=2)
            btn_get_name.grid(row=1, column=3)

            frame3 = Frame(newWindow)
            frame3.pack()
            label = Label(frame3, text="LED 동작을 입력해주세요(M, X, I): ")
            self.ledControl = StringVar()
            entry_name = Entry(frame3, textvariable=self.ledControl)
            btn_get_name = Button(frame3, text="실행", command=led_pwm_window)
            label.grid(row=1, column=1)
            entry_name.grid(row=1, column=2)
            btn_get_name.grid(row=1, column=3)

            frame4 = Frame(newWindow)
            frame4.pack()

            label_font = tkinter.font.Font(weight="bold")
            label1 = Label(frame4, text="LED ON/OFF 상태", font=label_font)
            label2 = Label(frame4, text="RED LED")
            label3 = Label(frame4, textvariable=self.red_led_state)
            label4 = Label(frame4, text="GREEN LED")
            label5 = Label(frame4, textvariable=self.green_led_state)
            label6 = Label(frame4, text="BLUE LED")
            label7 = Label(frame4, textvariable=self.blue_led_state)

            label1.grid(row=3, column=0)
            label2.grid(row=4, column=0)
            label3.grid(row=4, column=1)
            label4.grid(row=5, column=0)
            label5.grid(row=5, column=1)
            label6.grid(row=6, column=0)
            label7.grid(row=6, column=1)

        def btn_control_window():
            newWindow = Toplevel(window)
            frame1 = Frame(newWindow)
            frame1.pack()
            # button을 누르면, 라벨에 On/Off 변경값 표시함
            label1 = Label(frame1, text='구성한 버튼을 누르면 Buzzer가 켜집니다.')
            label1.pack()
            b1 = Button(frame1, text="ON", command=self.buzzer_on_button)
            b2 = Button(frame1, text="OFF", command=self.buzzer_off_button)

            b1.pack(side=LEFT, padx=10)
            b2.pack(side=RIGHT, padx=10)

        def buzzer_song_window():
            newWindow = Toplevel(window)
            frame1 = Frame(newWindow)
            frame1.pack()
            label1 = Label(frame1, text='buzzer로 연주할 곡을 선택해주세요')
            label1.pack()
            b1 = Button(frame1, text="작은별", command=self.buzzer_twinkle_button)
            b2 = Button(frame1, text="곰 세 마리", command=self.buzzer_off_button)

            b1.pack()
            b2.pack()

        def security_window():
            newWindow = Toplevel(window)
            frame1 = Frame(newWindow)
            frame1.pack()
            label1 = Label(frame1, text='custom 시큐리티 프로젝트')
            label1.grid(row=0, column=0)
            # 활성화 버튼을 통해, 도난 방지 모드 ON이면 PIR 작동 -> 움직임 감지 시 부저, 카메라, LED, LCD 컨트롤 -> GUI 프로그램 상에도 경고 메시지 출력

        window = Tk()
        led_control_button = Button(window, text="LED Control", command=led_control_window)
        btn_control_button = Button(window, text="Button Control", command=btn_control_window)
        security_project_button = Button(window, text="Security Project", command=security_window)
        buzzer_song_button = Button(window, text="Buzzer Song", command=buzzer_song_window)

        led_control_button.pack()
        btn_control_button.pack()
        security_project_button.pack()
        buzzer_song_button.pack()
        window.title("위젯 데모")

        window.mainloop()

    def buzzer_twinkle_button(self):
        pwm.start(90.0)
        for i in range(0, 42):
            pwmBuzzer.CahngeFrequency(scale[twinkle[i]])
            if i==6 or i==13 or i==20 or i==27 or i==34 or i==41:
                time.sleep(1.0)
            else:
                time.sleep(0.5)
        print("buzzer_twinkle_button")

    def buzzer_on_button(self):
        GPIO.output(buzzer_pin, True)
        print("buzzer on")

    def buzzer_off_button(self):
        GPIO.output(buzzer_pin, False)
        print("buzzer off")

    def process_radio_button(self):
        # print("LED ON" if self.led_state.get() == 0 else "LED OFF")
        print("")

    def process_button(self):
        if self.led_state.get() == 0:
            if self.ledColor.get() == "R":
                GPIO.output(led_red_pin, True)
                self.red_led_state.set("ON")
            elif self.ledColor.get() == "G":
                GPIO.output(led_green_pin, True)
                self.green_led_state.set("ON")
            elif self.ledColor.get() == "B":
                GPIO.output(led_blue_pin, True)
                self.blue_led_state.set("ON")

        else:
            if self.ledColor.get() == "R":
                self.red_led_state.set("OFF")
                GPIO.output(led_red_pin, False)
            elif self.ledColor.get() == "G":
                self.green_led_state.set("OFF")
                GPIO.output(led_green_pin, False)
            elif self.ledColor.get() == "B":
                self.blue_led_state.set("OFF")
                GPIO.output(led_blue_pin, False)


WidgetDemo()

try:
    WidgetDemo()
except KeyboradInterrupt:
    pass
finally:
    GPIO.cleanup()
