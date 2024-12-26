basic.show_leds("""
    . . # . .
    . . # . .
    . # . # .
    # # # # #
    # . . . #
    """)

def on_forever():
    if cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        cuteBot.motors(50, 10)
    if cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        cuteBot.motors(10, 50)
    if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        cuteBot.motors(50, 50)
    if cuteBot.tracking(cuteBot.TrackingState.L_R_UNLINE):
        cuteBot.motors(5, 5)
basic.forever(on_forever)
