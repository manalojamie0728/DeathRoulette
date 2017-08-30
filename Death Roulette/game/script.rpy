# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# PRIMARY
define narr = nvl_narrator
define iy1 = Character("Ichirou")
define ai2 = Character("Akira")
define st3 = Character("Sumiko")
define is4 = Character("Inoue")
define sr5 = Character("Sayo")
define ys6 = Character("Yoshiro")
define hk7 = Character("Hiroshi")
define mh8 = Character("Miyu")
define kk9 = Character("Kyou")
define hy10 = Character("Hikaru")

# SECONDARY
define guard = Character("Guard")
define unk = Character("???")

# The game starts here.
init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

label start:

    scene bg room with fade

    "Introducing..."
    iy1 "The name's Ichirou Yokohama."
    ai2 "Akira Ichibana."
    st3 "Sumiko Tokubei."
    is4 "Inoue Shinozaki."
    sr5 "Sayo Ronoroa."
    ys6 "Yoshiro Suzuki."
    hk7 "Hiroshi Kano."
    mh8 "Miyu Hirano."
    kk9 "Kyou Kirisaki."
    hy10 "Hikaru Yamamoto."

    call ch01_01_prologue1
    call ch01_02_prologue2
    call ch01_03_clubday
    call ch01_04_tenvictims
    call ch01_05_sacredheart
    call ch01_06_kyou
    call ch01_07_countdown
    call ch01_08_disappearance
    call ch01_09_labkyou1
    call ch01_10_labinoue1
    call ch01_11_labkyou2
    call ch01_12_labinoue2
    call ch01_13_facts1
    call ch01_14_labinoue3
    call ch01_15_labkyou3
    call ch01_16_death01
    call ch01_17_facts2
    call ch01_18_aftermath
    call ch01_19_funeral
    call ch01_20_epilogue
    return

label ch01_01_prologue1:
    "MARCH 17, 2012 - 2100H"
    window show
    nvl clear
    narr "Night.{w} The crickets filling in the silence that blankets the area.{w} No one to be seen nor heard as all have went home to rest, ready for the day to come."
    narr "Except it was Saturday, three hours before the Sabbatical Day sets in."

    nvl clear
    narr "A small beam of light cuts through the darkness.{w} From one end, the sound of footsteps and metal jingling can be heard."
    narr "It was the night guard, making his last rounds before he returns to his post to rest."
    narr "There was nothing out of the ordinary to report. The situation was the same as the previous nights."

    nvl clear
    window hide

    "{b}*YAWN*{/b}"

    window show
    nvl clear
    narr "The guard stretched his arms up into the air.{w} The classrooms were all clear, the faculty room, the council’s office, everything."
    narr "His companion is already at his post by the school gate, which had been locked an hour ago.{w} What remains is the school auditorium, across the small street separating it and the main building."
    narr "At a shrug and desire for coffee, the guard set foot towards the small structure."

    nvl clear
    narr "The sidewalk at the auditorium’s side resembled that of a waiting shed, about twenty times as long."
    narr "He walked up the stone steps, towards the increasingly darkening area.{w} He knew of the stories that surrounded the auditorium yet he continued to fulfill his duties."
    narr "Nothing went out of the ordinary as far as he is concerned."
    narr "The guard decided to go around the building counter-clockwise so that he may see the interior first."
    narr "Right outside, he shone his flashlight at various parts of the auditorium:{w} the stage, backstage entrance and the small storage room."

    nvl clear
    narr "When he was done, he brought the metal barriers down and locked them in place, completely sealing the main interior.{w} With that, he continued with his rounds."
    narr "There was one more place he needed to check: the opening to the backstage. He breezed around the auditorium and quickly found the said door."
    narr "As always, it was slightly ajar. He fixed his cap and proceeded to lock the door, his other hand examining the keys tied to his belt."
    
    nvl clear
    window hide

    "{i}*whisper* *whisper* *whisper*{/i}"
    "What was that?"
    "His hand stopped.{w} The guard scratched his head for a bit and leaned a bit towards the dark room."

    guard "I can’t be imagining things, can I?"

    "It could be some leaves rustling or a cat making its own rounds searching for food,{w} yet the whispers did not fall under these two categories."
    "{b}*WHIMPER*{/b} {i}*whisper*{/i} {b}*WHIMPER*{/b}"
    "His eyes widened and his heart skipped a strong beat."

    guard "Very funny, Onifuchi,{w} but your ghost stories won’t get me!"

    window show
    nvl clear
    narr "Nothing.{w} It did nothing."

    nvl clear
    narr "Before it irritated him further, he finally stepped inside to investigate.{w} Though it did disturb him, he decided to search for the source of the sounds. He was going to double check for anything, anyway."
    narr "It was dusty and empty inside as the props were already in the main building’s storage.{w} Thus, the sounds can be heard all over the place synchronizing with the crickets singing on the grass outside."
    narr "Had it been raining, he would have just ended the night then and there.{w} But no,{w} the cries resonated louder and louder as he got closer to one spot.{w} It was the rear storage,{w} and a small phantom of light seeped through the door's underside."
    
    nvl clear
    window hide

    unk "Forgive me!"

    "He needed to help, fast. Whoever is behind that door could be in grave danger.{w} Yet..."

    guard "This is absurd. No student is supposed to be in school this late.{w} What could she be doing here?"

    "He paced towards the storage room, his footsteps became more intense."

    unk "!{w} {b}*WHIMPER*{/b} No! No! No!{w} Please, I beg of you... Uhuhuhuhu..."

    "The door swung hard and the guard shone his flashlight inside the room."

    guard "Alright! Playtime’s over. If you may p--"

    "There was a girl at the center, wearing a dark sweater.{w} She is a student, the guard recognized as she turned towards him."
    "She was crying, and she dropped an object at her side.{w} The guard saw this and he was mortified."

    guard "What... the... hell...?{w} What have you done?!"
    unk "I won... didn't I?"

    "For a split second, her palms were exposed.{w} A number was carved on each of her hands. She might have severed an artery in the process."
    "The numbers 2 and 7{w} etched on her left and right, respectively."
    "A circle of ten candles surrounded the female student, one of which was extinguished by her left hand."

    unk "Mu...huhuhu..."

    "The girl turned away from the security guard, still petrified to stop her from continuing."

    unk "I am so lucky. They weren’t...{w} mu...huhu...{w} fuhahahaha... HAHAHAHAHA!!! AHAHAHAHAHAHAHAHAHA!!!!!!!!!!"

    "The guard tackled the girl, knocking over a few candles in the process.{w} She didn’t resist, too busy attending to her own amusement. He looked up, finally getting what she meant."
    "Pinned to the wall were graduation pictures of her and nine other students, all of whom he recognized immediately.{w} They were her batch mates."
    "While definitely not a marking, she had arranged it in a way that it formed a circle.{w} She drew the guiding lines beforehand."
    "It looked like a clock, with one of the hands pointing towards the picture opposite hers."
    "But it wasn’t a clock."

    unk "I win... They don’t... Ehehehe... hehehehehehe..."

    "It was the image of a roulette wheel."

    return

label ch01_02_prologue2:
    "One Year Later"
    "MARCH 28, 2013 - 1900H"
    return

label ch01_03_clubday:
    "JUNE 7, 2013 - 1430H"
    "JUNE 7, 2013 - 1600H"
    "JUNE 7, 2013 - 1700H"
    return

label ch01_04_tenvictims:
    "JUNE 7, 2013 - 1730H"
    return

label ch01_05_sacredheart:
    "JUNE 13, 2013 - 1900H"
    return

label ch01_06_kyou:
    "JUNE 14, 2013 - 1140H"
    return

label ch01_07_countdown:
    "JUNE 15, 2013 - 2300H"
    "Earlier..."
    return

label ch01_08_disappearance:
    "JUNE 18, 2013 - 1130H"
    "JUNE 18, 2013 - 1650H"
    return

label ch01_09_labkyou1:
    "JUNE 18, 2013 - Time Unknown"
    return

label ch01_10_labinoue1:
    "Date Unknown - Time Unknown"
    return

label ch01_11_labkyou2:
    "Date Unknown - Time Unknown"
    return

label ch01_12_labinoue2:
    "Date Unknown - Time Unknown"
    return

label ch01_13_facts1:
    "JUNE 20, 2013 - 0900H"
    return

label ch01_14_labinoue3:
    "Date Unknown - Time Unknown"
    return

label ch01_15_labkyou3:
    "Date Unknown - Time Unknown"
    return

label ch01_16_death01:
    "Date Unknown - Time Unknown"
    return

label ch01_17_facts2:
    "JUNE 24, 2013 - 1645H"
    return

label ch01_18_aftermath:
    "JUNE 25, 2013 - 1800H"
    return

label ch01_19_funeral:
    "JUNE 30, 2013 - 0730H"
    return

label ch01_20_epilogue:
    "JUNE 30, 2013 - 2000H"
    "To be continued..."
    return