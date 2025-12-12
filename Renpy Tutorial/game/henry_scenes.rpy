
label Henry_storylet:

    player "I study the ranger."

    menu:
        "Ask kindly about their past":
            show ranger jovial
            $ change_trust(+1)
            ranger "I once lived by the sea."
            $ add_secret("Grew up by the sea")
            player "I nod. That explains the seashell bracelet."
        "Press for a secret":
            show ranger angry
            $ change_trust(-1)
            ranger "Some secrets wash away with the tide."

    return