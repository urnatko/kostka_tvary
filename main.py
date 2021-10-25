def on_button_pressed_a():
    basic.show_number(pocetTresu)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global pocetTresu, cislo
    pocetTresu += 1
    cislo = randint(1, 6)
    if cislo == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    else:
        if cislo == 2:
            basic.show_leds("""
                . . . . .
                                . . . # .
                                . . . . .
                                . # . . .
                                . . . . .
            """)
        else:
            if cislo == 3:
                basic.show_leds("""
                    . . . . #
                                        . . . . .
                                        . . # . .
                                        . . . . .
                                        # . . . .
                """)
            else:
                if cislo == 4:
                    basic.show_leds("""
                        # . . . #
                                                . . . . .
                                                . . . . .
                                                . . . . .
                                                # . . . #
                    """)
                else:
                    if cislo == 5:
                        basic.show_leds("""
                            # . . . #
                                                        . . . . .
                                                        . . # . .
                                                        . . . . .
                                                        # . . . #
                        """)
                    else:
                        basic.show_leds("""
                            # . . . #
                                                        . . . . .
                                                        # . . . #
                                                        . . . . .
                                                        # . . . #
                        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

cislo = 0
pocetTresu = 0
pocetTresu = 0

def on_forever():
    pass
basic.forever(on_forever)
