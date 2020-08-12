let temp = 0
// def on_gettemp():
//     global temp
//     temp = input.temperature()
//     basic.show_string("" + str((temp)))
// basic.forever(on_forever)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    temp = input.temperature()
    radio.sendString("" + ("" + temp))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("I got it!")
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendString("One more!")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
