def on_button_pressed_b():
    global x
    led.unplot(0, 0)
    led.plot(x - 2, 0)
    x += 2
input.on_button_pressed(Button.B, on_button_pressed_b)

x = 0
x = 0
y = 0

def on_forever():
    pass
basic.forever(on_forever)
