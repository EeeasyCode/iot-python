from tkinter import *


class WidgetDemo:
    def __init__(self):
        window = Tk()
        window.title("위젯 데모")

        frame1 = Frame(window)
        frame1.pack()
        self.v2 = IntVar()
        led_on = Radiobutton(frame1, text="LED ON", variable=self.v2, value=1, command=self.process_radio_button)
        led_off = Radiobutton(frame1, text="LED OFF", variable=self.v2, value=2, command=self.process_radio_button)

        led_on.grid(row=1, column=1)
        led_off.grid(row=1, column=2)

        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="LED 색을 입력하세요(R/G/B): ")
        self.ledColor = StringVar()
        entry_name = Entry(frame2, textvariable=self.ledColor)
        btn_get_name = Button(frame2, text="실행", command=self.process_button)
        self.message = Message(frame2, text="위젯 데모입니다.")
        label.grid(row=1, column=1)
        entry_name.grid(row=1, column=2)
        btn_get_name.grid(row=1, column=3)
        self.message.grid(row=1, column=4)

        text = Text(window)
        text.pack()
        window.mainloop()

    def process_radio_button(self):
        print("LED ON" if self.v2.get() == 1 else "LED OFF")

    def process_button(self):
        print(self.ledColor.get() + " LED")
        if self.v2.get() == 1:
            self.message.configure(text="LED ON")
        else:
            self.message.configure(text="LED OFF")


WidgetDemo()
