# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define anubis = Character("Anubis")
define m = Character(_("Me"), color="#ffa500")
# The game starts here.
default who = False
default where = False
default how = False
default jackal = False
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene city
    with fade

    "As you stir from your slumber you notice that you’re in the back of a truck with a group of misfits, scoundrels, and other vagabonds."

    "One calls out to you"

    "???: Heh, finally awake?"

    "You shrug and try to collect your thoughts and try to recall why you’re here"

    "Right, you’re here because you’ve come across some financial troubles"

    "As it turns out having a crippling gacha addiction is quite the strain on one's finances"

    "Regardless, you’re near destitute and really only have one option."

    "That option being tomb raiding."

    "You feel a sudden shift in weight, the truck hits an abrupt stop."

    "???: Alright, we’re here. Up and at’em"

    "As you step out of the truck and gaze upon the monumental tomb in front of you. It stands mighty tall and imperious over the barren wasteland that is the desert."

    "As you marvel at the tomb the men you came along with brush by you, completely uninterested in the temple"

    "Enough gawking, get to it!"

    "You’re shaken by a rather burly swarthy man and that sets you back on the task at hand"

    "As you wander the tomb for trinkets and baubles something catches your eye"

    "It’s a well adorned jar that depicts a jackal with piercing white eyes"

    menu:

        "As soon as it catches my eye, I decide..."

        "To take it":

            jump take

        "To leave it":

            jump take

label take: 
    "The floor beneath you rumbles and shakes and the small pebbles are falling from the ceiling."

    "???: Hey, it’s time to go!"

    "You make a mad dash following the gang of tomb raiders out of the tomb. Whilst running you can see a light, the exit!"

    "As you exit the tomb and you see the clear blue sky you suddenly hear a loud horn"

    "As you turn to see the horn you see a massive slab of steel moments before you feel the force of a thousand suns for one second. In the next you feel nothing and feel as if you're drifting asleep"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

"Whilst you drift you hear something, a voice?"

"???: Mortal, wake up"

"As you make out the words you feel something prod your side"

"???: Come on, we don't have all day"

scene river
with dissolve

"As you stir and your eyes open you see this hulking shadow towering over you"

"???: Alright, enough lying around, get up."

show anubis_un
with dissolve
jump opt
    # These display lines of dialogue.
label opt:
    menu: 
        "You are incredibly confused, you don't know how you got here, where this place is, or who he is..."

        "Who are you?":

            jump who

        "Where am I?":

            jump where

        "What's going on?":

            jump what

label who:

    $ who = True

    anubis " I am Anubis God of funerary rites, protector of grave, guide to the underworld and most importantly the judge if your soul"

    jump main
    
    return

label where: 

    $ where = True

    anubis "You’re in the afterlife, the duat."

    jump main

    return 

label what:

    $ how = True

    anubis "You’ve recently perished in the mortal world and now are here to be escorted to my temple where you will be judged"

    jump main

    return

label main: 
    if who and where and how:
        m "Alright alright, I’ll get up"
        
        anubis "Finally, follow me."
    else:
        jump opt


"Anubis walks towards a row boat, and when you reach it he gestures towards it"

"You get in the boat first and he gets in after you and begins to row"

"…(time passes)"

menu:

    "Hey, nice muscles, what’s your bench?":

        jump muscle
            
    "What’s it like here in the afterlife?":

        jump afterlife

label muscle:

    "He stops rowing for a second and glares at you"

    "…"

    "He resumes rowing as if nothing happened"

    jump de
    
label afterlife: 

    anubis "It’s quiet, and quiet. Many who enter here don’t stay here long. Means I don’t have to deal with nuisances for all too long"

    m "Doesn’t it get lonely then?"

    anubis "Not exactly, some spirits stay here. They are spirits who have sinned but have curried favor with the gods and have been permitted to work off their sins"

    m "	Can you permit souls to stay here?"

    anubis "I see what you’re doing mortal. The answer is yes, I can. But I have never done so, you are nothing more than a nuisance."

    jump de

label de:


    m "-I mean can you blame me? Who wouldn’t want to spend time around a hunk like yourself?"

"He stops rowing to slowly raise his hand and drag it down his face"

hide anubis_un

show anubis_an

anubis "I didn’t think it was possible, but I feel ill now. I a deity feel weak and sickened at your poor attempt at flirting. Please never do that again."

m "Heh, you saw right through me."

hide anubis_an

show anubis_default

anubis "Of course I did, you mortals are such simple creatures."

"…(time passes)"

"A shore line comes into view and with it a city"

hide anubis_default

show anubis_un

anubis "We have arrived, get out"

