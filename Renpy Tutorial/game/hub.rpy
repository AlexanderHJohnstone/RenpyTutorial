## hub.rpy

label start:

    scene bg tavern

    narrator "The smell of stale ale and clamor of drunken adventurers hits you as you step into Karlach's tavern."
    narrator "If you're going to find any information Briarly's missing sister you're going to have to find the ranger."
    narrator "Briarly thinks he was somehow involved, so any information is good, but by gaining his trust I might be able to to ask him directly."
    show ranger neutral with dissolve
    player "I think he's the one I'm looking for. Here goes nothing!"
    
    call yourName_storylet

    #call secondStudent_scene
    #call thirdStudent_scene

    if ranger_trust >= 2:
        narrator "You can tell he's beginning to open up."
    else:
        narrator "You're going to have to turn this conversation around if you want to gain his trust."
    
    #call fourthStudent_scene
    #call fifthStudent_scene

    if ranger_trust >= 4:
        narrator "Keep this going and he might tell you everything you need to know."
    else:
        narrator "This coversation has been a waste of time, you decide to cut your losses and leave."
        return

    #call sixthStudent_scene
    #call seventhStudent_scene

    jump ending


label ending:
    show ranger neutral
    narrator "Time to piece together what you've learned."

    if ranger_secrets:
        python:
            for i, secret in enumerate(ranger_secrets, 1):
                renpy.say(narrator, f"{i}. {secret}")       # one click per secret

        narrator "Trust: [ranger_trust]"
    else:
        narrator "We learned nothing certain tonight."

    if ranger_trust >= 6:
        narrator "You have gained his trust, he may now help you on your quest."
    else:
        narrator "This conversation did not well, looks like you're on your own again."

    return
