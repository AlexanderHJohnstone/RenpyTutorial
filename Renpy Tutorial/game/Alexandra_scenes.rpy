
label Alexandra_storylet:

    show ranger neutral

    ranger "Would you indulge me in a game of chance, traveller?"

    player "You raise your eyebrow and ask what they had in mind."

    ranger "Why, it's simple! You guess a number, I'll roll this here die, and if you guess the outcome correctly I'll tell you something valuable."

    player "You suppose it's time to guess."

    menu:
        "1":
            show ranger jovial
            ranger "Got your answer? Then we will see if fate agrees!"
            player "The die clatters on the table. It shows three pips."
            show ranger neutral
            ranger "Well? Did they align?"
            menu:
                "Yeah, totally!":
                    show ranger angry
                    ranger "Liar! I can see it on your face!"
                    $ change_trust(-1)
                "No...":
                    show ranger jovial
                    ranger "Hahahaha, that's the way fate rolls, chum. At least I know you're honest."
                    $ change_trust(1)
        "2":
            show ranger jovial
            ranger "Got your answer? Then we will see if fate agrees!"
            player "The die clatters on the table. It shows four pips."
            show ranger neutral
            ranger "Well? Did they align?"
            menu:
                "Yeah, totally!":
                    show ranger angry
                    ranger "Liar! I can see it on your face!"
                    $ change_trust(-1)
                "No...":
                    show ranger jovial
                    ranger "Hahahaha, that's the way fate rolls, chum. At least I know you're honest."
                    $ change_trust(1)
        "3":
            show ranger jovial
            ranger "Got your answer? Then we will see if fate agrees!"
            player "The die clatters on the table. It shows five pips."
            show ranger neutral
            ranger "Well? Did they align?"
            menu:
                "Yeah, totally!":
                    show ranger angry
                    ranger "Liar! I can see it on your face!"
                    $ change_trust(-1)
                "No...":
                    show ranger jovial
                    ranger "Hahahaha, that's the way fate rolls, chum. At least I know you're honest."
                    $ change_trust(1)
        "4":
            show ranger jovial
            ranger "Got your answer? Then we will see if fate agrees!"
            player "The die clatters on the table. It shows six pips."
            show ranger neutral
            ranger "Well? Did they align?"
            menu:
                "Yeah, totally!":
                    show ranger angry
                    ranger "Liar! I can see it on your face!"
                    $ change_trust(-1)
                "No...":
                    show ranger jovial
                    ranger "Hahahaha, that's the way fate rolls, chum. At least I know you're honest."
                    $ change_trust(1)
        "5":
            show ranger jovial
            ranger "Got your answer? Then we will see if fate agrees!"
            player "The die clatters on the table. It shows one pip."
            show ranger neutral
            ranger "Well? Did they align?"
            menu:
                "Yeah, totally!":
                    show ranger angry
                    ranger "Liar! I can see it on your face!"
                    $ change_trust(-1)
                "No...":
                    show ranger jovial
                    ranger "Hahahaha, that's the way fate rolls, chum. At least I know you're honest."
                    $ change_trust(1)
        "6":
            show ranger jovial
            ranger "Got your answer? Then we will see if fate agrees!"
            player "The die clatters on the table. It shows two pips."
            show ranger neutral
            ranger "Well? Did they align?"
            menu:
                "Yeah, totally!":
                    show ranger angry
                    ranger "Liar! I can see it on your face!"
                    $ change_trust(-1)
                "No...":
                    show ranger jovial
                    ranger "Hahahaha, that's the way fate rolls, chum. At least I know you're honest."
                    $ change_trust(1)
                    
    show ranger neutral

    return