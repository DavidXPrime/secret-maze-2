input.onButtonPressed(Button.A, function () {
    led.unplot(X, Y)
    X = X + 1
    led.plot(X, Y)
})
input.onButtonPressed(Button.B, function () {
    led.unplot(X, Y)
    Y = Y + 1
    led.plot(X, Y)
})
let Y = 0
let X = 0
X = 0
Y = 0
led.plot(X, Y)
basic.forever(function () {
	
})
