# 키보드로 조종하기
import turtle as t


def turn_right():
    t.setheading(0)  # 거북이의 머리 0도
    t.forward(10)


def turn_up():
    t.setheading(90)
    t.forward(10)


def turn_left():
    t.setheading(180)
    t.forward(10)


def turn_down():
    t.setheading(270)
    t.forward(10)


def clear():
    t.clear()


t.shape('turtle')
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(clear, "Escape")     # 선 모두 지우기
t.listen()                          # 실행 대기

t.mainloop()
