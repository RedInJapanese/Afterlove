# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define anubis = Character("Anubis")
define m = Character(_("Me"), color="#ffa500")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg duat
    with fade

    "As you slowly open your eyes, a wave of confusion hits you as you try to ascertain where you are."

    "You see a lot of sand and archaic architecture, which makes you even more confused."

    "You look into the distance and you see a tall figure, but somethings off about its head... You can't quite put your finger on it..."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show anubis placeholder
    with dissolve

    # These display lines of dialogue.

    anubis "Welcome to the duat, lost soul. Here you will face judgement for the events that transpired in your life."

    menu: 
        "You are incredibly confused, you don't know how you got here, where this place is, or who he is..."

        "Ask who he is":

            jump who

        "Ask where you are":

            jump where

        "Ask how you got here":

            jump how

label who:

    show anubis placeholder
    with dissolve

    anubis "I am anubis, egyptian god of funerary rights, protector of graves, and guide to the underworld"

    anubis "I am here to judge you."

    return 

label where: 

    show anubis placeholder
    with dissolve

    anubis "where did i ask"

    return 

label how:
    show anubis placeholder
    with dissolve

    anubis "how did i ask"
    # This ends the game.
    return
