# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define anubis = Character("Anubis")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg duat

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    anubis "You've created a new Ren'Py game."

    anubis "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
