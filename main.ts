let cislo = 0
input.onGesture(Gesture.Shake, function () {
    cislo = randint(1, 6)
    if (cislo == 1) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    } else {
        if (cislo == 2) {
            basic.showLeds(`
                . . . . .
                . . . # .
                . . . . .
                . # . . .
                . . . . .
                `)
        } else {
            if (cislo == 3) {
                basic.showLeds(`
                    . . . . #
                    . . . . .
                    . . # . .
                    . . . . .
                    # . . . .
                    `)
            } else {
                if (cislo == 4) {
                    basic.showLeds(`
                        # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
                        `)
                } else {
                    if (cislo == 5) {
                        basic.showLeds(`
                            # . . . #
                            . . . . .
                            . . # . .
                            . . . . .
                            # . . . #
                            `)
                    } else {
                        basic.showLeds(`
                            # . . . #
                            . . . . .
                            # . . . #
                            . . . . .
                            # . . . #
                            `)
                    }
                }
            }
        }
    }
})
basic.forever(function () {
	
})
