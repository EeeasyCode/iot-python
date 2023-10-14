from tkinter import *

class WidgetDemo:
    def __init__(self):
        window = Tk()
        window.title("위젯 데모")

        frame1 = Frame(window)
        frame1.pack()
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text="굵게",
            variable=self.v1, command=self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text="빨간색", bg="red",
            variable=self.v2, value=1,
            command=self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text="노란색", bg="yellow",
                            variable=self.v2, value=2,
                            command=self.processRadiobutton)
        cbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)

        frame2 = Frame(window)
        frame2.pack()
        label=Label(frame2, text="입력하세요: ")
        self.name = StringVar()
        entryName=Entry(frame2, textvariable=self.name)
        btGetName=Button(frame2, text="가져오기", command=self.processButton)
        message = Message(frame2, text="위젯 데모입니다.")
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)
        message.grid(row=1, column=4)

        text = Text(window)
        text.pack()
        text.insert(END, "ㅁㄴㅇㄹㄴㅁㅇㄹ")
        text.insert(END, "ㅁㄴㅇㄹㄴㅁㅇㄹ")
        text.insert(END, "ㅁㄴㅇㄹㄴㅁㅇㄹ")
        window.mainloop()

    def processCheckbutton(self):
        print("체크 버튼이" + ("선택") if self.v1.get() == 1 else "해제")

    def processRadiobutton(self):
        print("빨간색" if self.v1.get() == 1 else "노란색")

    def processButton(self):
        print("이름은 " + self.name.get() + "입니다.")

WidgetDemo()