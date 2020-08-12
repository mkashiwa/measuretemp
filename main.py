temp = 0

#def on_gettemp():
#    global temp
#    temp = input.temperature()
#    basic.show_string("" + str((temp)))
#basic.forever(on_forever)


def on_button_pressed_a():
    global temp
    temp = input.temperature()
    radio.send_string(""+str((temp)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_string("I got it!")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    radio.send_string("One more!")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)