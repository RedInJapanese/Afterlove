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
default score = 0
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene city
    with fade
    play music "Engine.mp3"

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

    scene tomb
    with dissolve

    play music "ominous.mp3"

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

scene boat
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

    $ score -= 1

    "He stops rowing for a second and glares at you"

    "…"

    "He resumes rowing as if nothing happened"

    jump de
    
label afterlife: 

    $ score += 1

    anubis "It’s quiet, and quiet. Many who enter here don’t stay here long. Means I don’t have to deal with nuisances for all too long"

    m "Doesn’t it get lonely then?"

    anubis "Not exactly, some spirits stay here. They are spirits who have sinned but have curried favor with the gods and have been permitted to work off their sins"

    m "Can you permit souls to stay here?"

    anubis "I see what you’re doing mortal. The answer is yes, I can. But I have never done so, you are nothing more than a nuisance."

    jump de

label de:

    m "I mean can you blame me? Who wouldn’t want to spend time around a hunk like yourself?"

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

scene pyramid
with dissolve

play music "main.mp3"

show anubis_un

"You enter the town, there aren’t many buildings and all the buildings short of the megastructure at the town's center are fairly quaint. The town also seems to be sparsely populated."

anubis "Alright, enough sightseeing, let’s get a move on"

menu: 

    "What do you do?"

    "Alright, fine":

        jump body3

    "Not yet!":

        jump dlc

label dlc: 

    anubis "What do you mean, not yet?"

    m "Umm … there was something that caught my eye!"

    hide anubis_un
    show anubis_an

    anubis "And what pray tell was it?"

    m "That food vendor over there looks really good!"

    anubis "So, you just wanted to eat at a food cart?"

    m "I mean it’s not everyday I get to eat in the world between worlds"

    hide anubis_an
    show anubis_un

    anubis "Fine, I’ll indulge your whims"

    "You both go up to the stand and as you approach it a spirit bursts forth from behind the stand with a platter of sweet breads governed in a shimmer brown glaze."

    "You go and take one of these treats and as you do Anubis just stares blankly stares"

    m "Hey, you want one?"

    anubis "No, as a deity I have no need for such things and thus don’t care for them"

    menu: 

        "What do you do?"

        "Ah come on, one of these isn’t going to ruin your sick gains":

            jump bad_choice_food

        "Such a shame, these are real good, you sure you don’t want to try one?":

            jump good_choice_food

    label bad_choice_food:

        $ score -= 1

        hide anubis_un
        show anubis_an

        anubis "It was a mistake to allow you this reprieve."

        "As you finish your pastry he grabs you by the arm and brings you into the temple"

        jump body3

    label good_choice_food:

        $ score += 1

        hide anubis_un
        show anubis_an

        anubis "I suppose it’s been awhile since I’ve had one, I suppose I’ll humor you"

        "As his maw opens and the bread disappears a smile cracks across his face"

        hide anubis_an
        show anubis_default

        m "See, they’re good! You should allow yourself to enjoy what you can when you can!"

        hide anubis_default
        show anubis_un

        anubis "Hmm, I suppose minor diversions such as this wouldn’t cause too much of an issue. But enough diversions, we should get going."

        m "umm, what about that building over there!"

        hide anubis_un
        show anubis_an

        anubis "That one? Do you even know what that is?"

        menu: 

            "Yes it’s obviously an arcade":

                anubis "No, it’s not. Also what even is that? Wait, no, no more stalling, we’re going to the temple."

                jump body3
            
            "No I don’t, but I want to know":

                play music "cityambience.mp3"

                $ score += 1

                hide anubis_an
                show anubis_un

                anubis "I appreciate the honesty, I’ll indulge you"

                "As you both enter the building you see tomes line the walls, the floor is an intricate tiling and in the center is a kind of kiosk with a soul manning it"

                "As you both approach the kiosk Anubis quickly rushes by you for a moment and hunches over. He mutters something to the kiosk attendant and as quickly as he mutters the attendant produces and gives Anubis a book and a cup."

                m "What was that about?"

                anubis "It’s nothing"

                m "Well it’s obviously a book, what’s it about?"

                anubis "None of your concern."

                "You figure it’s a bad idea to keep pushing him about it and go up to the kiosk yourself. The kiosk has a catalog of books and warm beverages to choose from."

                "..."

                "The beverages are your standard fair of tea and coffee but the variety of books is oddly limited… it’s all young adult…"

                menu:

                    "Which book do you pick?"

                    "Action Adventure":

                        $ score -= 1

                        hide anubis_un
                        show anubis_an

                        anubis "Really? You picked that of all things?"

                        hide anubis_an
                        show anubis_un

                        anubis "I suppose taste is something that can only be refined with age, and frankly you don’t have such luxury"

                        "After being chastised for your choice you both sit down in the lounge and enjoy your literature and drinks."

                        "Anubis reaches for his tea and sips the last of. Afterwards he closes his book and gets up."

                        anubis "Alright, that break was long enough, let’s get you to that temple"

                        jump body3

                    "Romance Novel ":

                        $ score += 1

                        hide anubis_un
                        show anubis_default

                        anubis "I see someone here has impeccable taste"

                        m "What makes you say that?"

                        anubis "Any child can enjoy the whims of adventure and spectacle, but it takes a person of true character to appreciate something as refined as the slow passionate burn that romance demands!"

                        hide anubis_default
                        show anubis_un

                        anubis "Ahem, sorry, I mean it’s nothing of note just a matter of preference really."

                        m "Sure…"

                        "After that exchange you both recline and enjoy yourselves in the lounge for awhile..."

                        anubis "Alright, that break was long enough, let’s get you to that temple."

                        jump body3

label body3:

        "As you both walk towards the temple you notice the grandeur of it. It’s entry way flanked by massive titans and it’s walls engraved with glyphs that proudly stand boldly outward showing the rest of the duat of the excellence and significance of this place."
        
        "As you enter the magnificence continues with glyphs covering the walls and scenes from myth being depicted as well in stunning detail and vibrant color."

        "As you delve deeper the rooms suddenly are lit by lanterns of brass and holding flames as blue as the very lapis that embolden the scenes the lanterns illuminate."

        "After a while you both enter a room that has a vase and a scale. The scale has a feather resting on one end and an axe leaning against its center beam."

        hide anubis_an
        hide anubis_default
        show anubis_un
        
        anubis "Alright mortal, are you ready?"

        menu:

            "Yes":

                $ score += 1

                hide anubis_un
                show anubis_default

                anubis "Excellent"

                "He picks up the case and produces a heart out of it and sets it on the scale"

                jump ending

            "I don’t have a choice really":

                anubis "Correct, you don’t"

                "He picks up the case and produces a heart out of it and sets it on the scale"

                jump ending
            
            "I want to ask about something":

                hide anubis_un
                show anubis_an

                anubis "Make it quick."

                menu:

                    "Is there another way to go about this?":

                        $ score -= 1

                        anubis "You’re still trying to weasel your way out? No there isn’t"

                        "He picks up the case and produces a heart out of it and sets it on the scale"

                        jump ending

                    "I'm grateful you dealt with my antics":

                        $ score += 1

                        hide anubis_an
                        show anubis_default

                        anubis "Heh, yeah. You better be."

                        "He picks up the case and produces a heart out of it and sets it on the scale"

                        jump ending


label ending: 

        if score > 0:

            "Anubis puts your heart on the scale with the feather on the opposite end."

            "At first the scale waivers a little bit off balance, your heart continuously rising and sinking."

            "As scale continuous to be in a state of flux Anubis reaches his axe"

            "When his axe is firmly in his grasp he presses his axe gently against the scale and the scale stops wavering"

            "…"

            "You heart and the feather are level"

            hide anubis_un
            show anubis_default

            anubis "I feel generous today, which is no common sight, so be grateful."

            m "Was that really it?"

            hide anubis_default
            show anubis_un

            anubis "Well, I’ll grant that you were at least mildly interesting. I wouldn’t mind going to a food stall sometime…"

            "The two of you go on a second date together and live happily ever after…"

        else:

            "Anubis puts your heart on the scale with the feather on the opposite end"

            "As your heart touches the scale it sinks like a rock."

            "And as quickly as your heart sinks you barely catch some movement at the corner of your eyes"

            "Just as you turn to see what that movement was you see this hulking figure with an axe raised over it’s head and before you can even muster anything to say you hear something."

            hide anubis_un
            hide anubis_an
            show anubis_default

            anubis "Farewell, sinner"

            hide anubis_default
            hide anubis_an
            hide anubis_un
            with fade

            "Game Over"
