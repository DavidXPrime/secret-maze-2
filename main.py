def on_button_pressed_a():
    global X
    led.unplot(X, Y)
    X = X + 1
    led.plot(X, Y)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Y
    led.unplot(X, Y)
    Y = Y + 1
    led.plot(X, Y)
input.on_button_pressed(Button.B, on_button_pressed_b)

Y = 0
X = 0
X = 0
Y = 0
led.plot(X, Y)
solution = [[0,0],[1,0],[2,0],[2,1],[3,1],[3,2],[4,2],[4,3],[4,4]]

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
