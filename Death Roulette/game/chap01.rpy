# JUNE CHAPTER SCRIPT

label ch01_june:
    centered "{i}{b}Illusions abound; darkness on the inside and chaos on the outside.{w}\nHow is truth able to fit in both places?{w}\nWe may never know for sure,{w} yet someone has already found the answer.{/b}{/i}"
    
    call ch01_01_prologue1 from _call_ch01_01_prologue1
    call ch01_02_prologue2 from _call_ch01_02_prologue2
    call ch01_03_clubday from _call_ch01_03_clubday
    call ch01_04_tenvictims from _call_ch01_04_tenvictims
    call ch01_05_sacredheart from _call_ch01_05_sacredheart
    call ch01_06_kyou from _call_ch01_06_kyou
    call ch01_07_countdown from _call_ch01_07_countdown
    call ch01_08_disappearance from _call_ch01_08_disappearance
    call ch01_09_labkyou1 from _call_ch01_09_labkyou1
    call ch01_10_labinoue1 from _call_ch01_10_labinoue1
    call ch01_11_labkyou2 from _call_ch01_11_labkyou2
    call ch01_12_labinoue2 from _call_ch01_12_labinoue2
    call ch01_13_facts1 from _call_ch01_13_facts1
    call ch01_14_labinoue3 from _call_ch01_14_labinoue3
    call ch01_15_labkyou3 from _call_ch01_15_labkyou3
    call ch01_16_death01 from _call_ch01_16_death01
    call ch01_17_facts2 from _call_ch01_17_facts2
    call ch01_18_aftermath from _call_ch01_18_aftermath
    call ch01_19_funeral from _call_ch01_19_funeral
    call ch01_20_epilogue from _call_ch01_20_epilogue
    call credits from _call_credits_1
    return

label ch01_01_prologue1:
    scene black with fade
    "MARCH 17, 2012 - 2100H"
    scene bg moon with fade
    play sound sfx_crickets loop

    window show
    nvl clear
    narr "Night.{w} The crickets filling in the silence that blankets the area.{w} No one to be seen nor heard as all have went home to rest, ready for the day to come."
    narr "Except it was Saturday, three hours before the Sabbatical Day sets in."

    window hide
    scene bg msci night with dissolve
    window show
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

    window hide
    scene bg school fields night with dissolve
    window show
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

    scene black with fade
    stop sound
    "{i}*whisper* *whisper* *whisper*{/i}"
    "{i}What was that?{/i}"
    "His hand stopped.{w} The guard scratched his head for a bit and leaned a bit towards the dark room."

    guard "I can’t be imagining things, can I?"

    "It could be some leaves rustling or a cat making its own rounds searching for food,{w} yet the whispers did not fall under these two categories."
    play sound sfx_girlcry
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

    play music bg_roadtohell loop
    unk "Forgive me!"

    "He needed to help, fast. Whoever is behind that door could be in grave danger.{w} Yet..."

    guard "This is absurd. No student is supposed to be in school this late.{w} What could she be doing here?"

    "He paced towards the storage room, his footsteps became more intense."

    unk "!{w} {b}*WHIMPER*{/b} No! No! No!{w} Please, I beg of you... Uhuhuhuhu..."

    play sound sfx_dooropen
    "The door swung hard and the guard shone his flashlight inside the room."

    guard "Alright! Playtime’s over. If you may p--"

    play sound sfx_girlcry
    "There was a girl at the center, wearing a dark sweater.{w} She is a student, and the guard recognized her as she turned towards him."
    stop sound
    play sound sfx_metaldrop
    "She was crying, and she dropped an object at her side.{w} The guard saw this and he was mortified."

    guard "What... the... hell...?{w} What have you done?!"
    unk "I won... didn't I?"

    "For a split second, her palms were exposed.{w} A number was carved on each of her hands. She might have severed an artery in the process."
    scene bg hands suzumoto with dissolve
    "The numbers 2 and 7{w} etched on her left and right, respectively."
    scene black with dissolve
    "A circle of ten candles surrounded the female student, one of which was extinguished by her left hand."

    unk "Mu...huhuhu..."

    "The girl turned away from the security guard, still petrified to stop her from continuing."

    unk "I am so lucky. They weren’t...{w} mu...huhu...{w} fuhahahaha... HAHAHAHAHA!!! AHAHAHAHAHAHAHAHAHA!!!!!!!!!!"

    play sound sfx_thud
    "The guard tackled the girl, knocking over a few candles in the process.{w} She didn’t resist, too busy attending to her own amusement. He looked up, finally getting what she meant."
    "Pinned to the wall were graduation pictures of her and nine other students, all of whom he recognized immediately.{w} They were her batch mates."
    "While definitely not a marking, she had arranged them in a way that they formed a circle.{w} She drew the guiding lines beforehand."
    "It looked like a clock, with one of the hands pointing towards the picture opposite hers."
    "But it wasn’t a clock."

    unk "I win... They don’t... Ehehehe... hehehehehehe..."

    scene bg roulette with dissolve
    "It was the image of a roulette wheel."
    stop music fadeout 1.0
    return

label ch01_02_prologue2:
    scene black with fade
    "One Year Later"
    "MARCH 28, 2013 - 1900H"
    scene bg street night with dissolve
    "Dinner was underway.{w} The northbound road of a major highway is congested with vehicles, flashing red from the view of the TV screen.{w} It was not long before a news report followed that short scene."

    scene bg apartment night with dissolve
    window show
    nvl clear
    narr "{i}Sacred Heart Village, the centre of the infamous curse killings reported since June of 2012, has witnessed its tenth victim this early morning.{/i}"
    narr "{i}Kugimiya Oizumi, also known as Lienel, was found dead at her bedroom six o’ clock.{w} In the same vein as the previous killings this academic year, she had suffered a brutal end.{/i}"
    narr "{i}According to her mother, she was about to ready her daughter for the graduation ceremony this afternoon when she found Oizumi hanging from her room’s ceiling fan.{w} Her head was laterally sliced in half.{/i}"
    narr "{i}In addition, she noticed her daughter distressed the previous evening after they had an argument regarding her college education.{w} Denied of any scholarship and support from her parents, this may have played a role in her alleged suicide.{/i}"
    narr "{i}While her mother and their neighbours deny any foul play in Oizumi’s death, authorities are investigating from that angle.{/i}"
    scene bg tvstatic with dissolve
    play sound sfx_static loop
    narr "{i}This is Akane Yuuichi,{w} Channel 27 News Tonite.{/i}"

    nvl clear
    narr "The specter of death had laid its hand on its tenth victim. The curse killings the reporter mentioned was already on its second year. This time, it was more ruthless than ever."
    narr "How is this connected to the previous years’ curse killings?{w} They were all the same in nature.{w} A common denominator existed both in the place of interest and the origin of the curse."
    narr "Sacred Heart Village… and the girl who initiated the curse killings unwillingly,{w} a graduate of Maria St. Claire Institute in Kutsutochi.{w} Has there been any fruit from her ritual?"
    narr "Nay, it seemed.{w} Yet for her, it was already over."

    nvl clear
    narr "{i}I wish to express both my apologies and condolences to the families of those lives taken by the curse. Had it not been for our interference back then, none of this would have happened.{/i}"
    narr "{i}They got what they want. It’s over.{/i}"

    nvl clear
    window hide

    stop sound
    play music bg_chloeslullaby loop
    "Those eyes, cold {i}dead{/i} eyes. She had never been the same.{w} What could the specter of death want to stop its rampage? Has it been satisfied?"

    unk "{i}Swing{/i}, {i}swing{/i}, {i}swing{/i}. Nevertheless, it was a foolish mistake to play with spiritual games, little girl."

    "An honest sentiment, the spectator expressed. A sugary sweet \"game\" that almost cost the lives of a few{w} – no, it cost ten.{w} Ten too many to be a coincidence or anything light."

    unk "{i}Puku{/i}, it was a foolish mistake indeed.{w} Once you start it, you can never stop."

    "{b}*POP*{/b}"

    unk "Is it the time? Summer vacation is about to start. Two months of goofing around, two months of exploring the world. {i}*chew*{/i} {i}*chew*{/i} {i}*chew*{/i}"
    unk "Yes. Two months, more than enough for our leisure time. What do you have in mind, {i}puku{/i}?"
    unk "{i}Swing{/i}, {i}swing{/i}, {i}swing{/i}. Thoughts, come to my mind – mind, give me some thoughts to think about.{w} I wonder what it could be... Hmmmm..."
    unk "Oh, I know!"

    "Two hands clasped, the sound heard all around the room.{w} As if in merriment or agreement, another pair of hands clasped, ringing the room once more."

    unk "{i}Puku{/i}, the thoughts have reached my mind. Pu... ku..."

    play sound sfx_ticktock
    "Just then, the clock at the hallway sounded to tell the house’s tenants of the time.{w} Twelve times, to be exact. One more day has begun anew."
    
    scene black with fade
    unk "{i}Time's up!{/i}"
    unk "Game over... puku."
    play sound sfx_giggle
    play sound sfx_giggle
    unk "Hihihihihihihi! {b}{i}*cackle*{/i}{/b} {b}{i}*cackle*{/i}{/b}"
    stop music
    call opening from _call_opening

    return  

label ch01_03_clubday:
    scene black with fade
    "JUNE 7, 2013 - 1430H"
    scene bg msci with dissolve

    play music bg_autumnday loop fadeout 1.0
    window show
    nvl clear
    narr "Maria St. Claire Institute."
    narr "With the new council taking over, its mood and reputation has gone back to as it was in its glory days. Blessed is the day, indeed!"
    narr "And as per tradition, it was Club and Org Day today!{w} New circle of friends to get along with or the same ones all over again. The former holds mostly true for the freshmen all of whom were guided by an authority figure."

    window hide
    show sayo smileopen at Three2 with Dissolve(0.2)
    window show
    narr "That authority figure is Sayo Ronoroa.{w} She is the current student council president, always ready whenever her service is needed."
    narr "The one with the highest honors so far; thus, she was always looked high upon by her colleagues and her teachers.{w} She has an aura much more different than those of her peers."
    narr "She was guiding some freshmen in choosing their clubs."

    nvl clear
    window hide

    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "Would you like to join the Science Club or the Journalism Org?{w} I was a member of both once. You’ll learn a lot, I promise!"

    "She would flash that smile.{w} The same charming smile she gave everyone. Well, those who are not bothering her, at least.{w} It captured the hearts of the freshmen;{w} hence, they followed her suggestion."

    show sayo happyclosed at Three2 with Dissolve(0.2)
    sr5 "One at a time, children. Know how difficult it is to row two boats at once! {i}*giggle*{/i}"

    show sayo smileopen at Three2 with Dissolve(0.2)
    window show
    nvl clear

    scene bg school hallway with dissolve
    narr "She was always like that. After seeing the students off, she turned around her heels and headed to the council room."
    hide sayo with Dissolve(0.2)
    narr "Sayo passed by the room neighbouring the Science Club.{w} Being the \"Queen of Science,\" this is where the Mathematics Club is being held.{w} Inside were a few officers busy with their preparations."
    scene bg classroom1 with dissolve
    narr "Like the others, they were relatively chill.{w} One of the officers, the Vice President, was going over the program guide a few times to check for any mistakes.{w} He snorts and fixes his glasses randomly."
    window hide
    show miyu confused at Three2 with Dissolve(0.2)
    window show
    narr "Miyu Hirano,{w} a transferee student during his Sophomore year and one of the youngest in their batch.{w} He was particularly skilled at Math, one of his true passions since Elementary."
    narr "A symbol of pride and excellence, he fulfills his duties as best as he could."

    nvl clear
    window hide

    show miyu serious at LS with Dissolve(0.2)
    mh8 "Awww... come on..."
    hy10 "What seems to be the problem, Miyu?"

    "The sweet-voiced girl approached Miyu and addressed his frustration.{w} He had forgotten to bring the materials for one of their games later."

    show hikaru smile at RS with Dissolve(0.2)
    hy10 "Oh. That? Hehehe...{w} An acute problem if you would ask me. Shall we tell this to Ms. President?"
    show miyu surprised at LS with Dissolve(0.2)
    mh8 "No need. No need. Let’s just make do with what we have. I’m a master of impromptu, you see?"
    show hikaru talk at RS with Dissolve(0.2)
    hy10 "Whatever you say..."

    hide miyu with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)
    show hikaru smile at Three2 with Dissolve(0.2)
    window show
    nvl clear
    narr "Her name is Hikaru Yamamoto, Miyu’s long-time friend and classmate.{w} She holds the position of Treasurer in their club."
    narr "She is usually the comic relief of her class. However, she holds a duality between it and being a distinguished student in their batch.{w} She had come close to Sayo once, the reigning First Placer in their early years."
    narr "A reliable friend and an only child, she embraces her youth. Hikaru is different to those who are around her age.{w} She has a special friend, a resident singer named Aria, her personal butt monkey."

    nvl clear
    window hide

    hide hikaru with Dissolve(0.2)
    stop music fadeout 1.0
    "{i}Pssst... Pssst...{/i}"

    "Someone was calling out from the window. It caught one of the officers’ attention and called for Miyu."

    show ichirou happy at LS with Dissolve(0.2)
    iy1 "You guys still busy? I want to talk for a minute or two."
    hide ichirou with Dissolve(0.2)

    "He put down the program guide and went out of the classroom as prompted. Miyu placed his hands in his pockets."

    scene bg school hallway with dissolve
    play music bg_theanthillganggoeswest loop fadein 1.0

    show ichirou happy at LS with Dissolve(0.2)
    show miyu smile at RS with Dissolve(0.2)
    mh8 "Ichirou, you’ve dropped by! I see you guys haven’t started yet as well.{w} What up?"
    show ichirou smile at LS with Dissolve(0.2)
    iy1 "I’ve already talked to the others about this. You coming?"
    show miyu confused at RS with Dissolve(0.2)
    mh8 "Where to?"

    show miyu naughty smirk at RS with Dissolve(0.2)
    window show
    nvl clear
    narr "Miyu smirked and placed an arm over one side of the doorway.{w} Of course, this could be another mischievous prank by Ichirou."
    window hide
    hide miyu with Dissolve(0.2)
    hide ichirou
    show ichirou smile at Three2 with Dissolve(0.2)
    window show
    narr "Speaking of, his full name is Ichirou Yokohama, the projected valedictorian of the batch.{w} He has quite a humble nature, but he drops the act once the view of his teachers leaves him."
    narr "Like Miyu, Ichirou is very skilled in Mathematics and has gone on to join a few contests even having Miyu as a teammate.{w} Still, because of the fair match in their skill level, they are considered as rivals to each other."
    narr "That doesn’t stop them from being close friends, however."
    hide ichirou with Dissolve(0.2)

    nvl clear
    window hide

    show miyu naughty smirk at RS with Dissolve(0.2)
    show ichirou happy2 at LS with Dissolve(0.2)
    iy1 "Let’s bond. I mean, since it’s our last year and all... {i}*chuckle*{/i} why not we gather together for a friendly chat.{w} You know, jut a few of us?"
    show miyu surprised at RS with Dissolve(0.2)
    mh8 "And you tapped people already? Who else is coming along?"
    show ichirou confused at LS with Dissolve(0.2)
    iy1 "I’ve tapped four, making us five at the moment:{w} Sumiko, Akira, Kyou, and Hiroshi.{w} Well, not sure about Akira, though, being a council officer. But hey, he’s looking forward to it."
    show miyu smile at RS with Dissolve(0.2)
    mh8 "Count me in. Tell me what to do."
    show ichirou happy2 at LS with Dissolve(0.2)
    iy1 "Yippee!!!{w} That’s six people. You might want to tap Hikaru to join us.{w} You know you want to..."

    show miyu naughty blush at RS with Dissolve(0.2)
    "If Miyu had a newspaper in hand, he would have rolled it and hit Ichirou right on his crown.{w} Luckily, he was able to get away with it."
    "Miyu is often teased with Hikaru, given the gravity of their friendship.{w} Awkward, it may seem, but they both eventually got used to it."
    "It still doesn’t sound pleasurable to Miyu, though, as he has {i}other businesses{\i} to attend to."

    show miyu naughty smile at RS with Dissolve(0.2)
    mh8 "Alright, alright. Whatever you say!{w} Don’t you have a club activity to attend to, huh, {i}Mr. SciClub Officer{/i}?"

    show ichirou focusleft at LS with Dissolve(0.2)
    "Ichirou glanced at the neighbouring room.{w} Sumiko was inside, cross-armed and glaring at him. He motioned for Ichirou to come inside."

    show ichirou embarassed at LS with Dissolve(0.2)
    iy1 "Half-past five near the auditorium, Miyu. Spread the word."

    hide ichirou with Dissolve(0.2)
    show miyu naughty smirk at RS with Dissolve(0.2)
    "With a snap of a finger, the two parted ways and returned to their duties."

    hide miyu with Dissolve(0.2)
    stop music fadeout 2.0
    scene bg classroom1 with dissolve

    "JUNE 7, 2013 - 1600H"
    play music bg_merrygo loop fadein 1.0
    window show
    nvl clear
    narr "After over an hour of club-related activities, the students went around to find their desired organization.{w} This time, the preparations were bigger and the number of choices reduced."
    narr "Some of the fellow club officers are also part of the same organization. Thus, this preserves their established chemistry."

    window hide
    show sumiko serious at Three2 with Dissolve(0.2)
    window show
    nvl clear
    narr "Sumiko Tokubei is the President of the Environmental Organization, with fellow officers Hiroshi and Yoshiro.{w} Being a hands-on person, he always ensures everything is according to plan."
    narr "Of course, he embodies the cliché description of a high IQ student.{w} His excellent performance in Science is complemented by his occasional forgetfulness. Kind of like a memory card."
    narr "He spoke with authority, addressing the crowd before them."

    nvl clear
    window hide

    show sumiko serioustalk at Three2 with Dissolve(0.2)
    st3 "Settle down, everyone. We would like to begin our first meeting at EO.{w} The {b}Environmental Organization{/b}, not the eye care center."
    show sumiko smirk at Three2 with Dissolve(0.2)
    play sound sfx_applause
    "HAHAHAHAHAHAHAHA!!! Woo... WOO!!!! {b}*APPLAUSE*{/b}"
    stop sound
    
    "Sumiko gave his opening remarks as the presiding officer and their scheduled activities followed."
    hide sumiko with Dissolve(0.2)
    show yoshiro smile at Three2 with Dissolve(0.2)
    stop music fadeout 1.0
    play sound sfx_rubikscube loop
    "Yoshiro Suzuki, the resident puzzle geek, solved a 3x3x3 Rubik’s Cube in hand while he discussed the details of their organization."
    "Those who were listening to him were in awe, attention divided between his message and his puzzle-solving skills.{w} More than puzzles, though, he is quite a fan of riddles and whodunit mysteries."
    "That would come in handy whenever necessary."

    ys6 "So, to sum it up..."
    "{i}*crank*{/i} {i}*crank*{/i} {i}*crank*{/i}"
    show yoshiro smirkclosed at Three2 with Dissolve(0.2)
    ys6 "What you’re in for is basically adventure, tree-planting, waste segregation, and more! What else could you ask for?"

    stop sound
    "At that instant, his hands stopped."
    "He raised both eyebrows to everyone in the room.{w} He gave the cube a spin, showing all of its sides solved and free of any imperfections. A fine work at that."

    show yoshiro smirk at Three2 with Dissolve(0.2)
    ys6 "Any questions?"

    show yoshiro smirkclosed at Three2 with Dissolve(0.2)
    "No answer, as expected."
    play sound sfx_applause
    "Besides, the audience was left in awe, giving him the same treatment as Sumiko."
    hide yoshiro with Dissolve(0.2)
    stop sound
    show hiroshi bored at Three2 with Dissolve(0.2)
    "Afterwards, the ball moved to Hiroshi Kano, the Secretary of the organization."

    show hiroshi boredtalk at Three2 with Dissolve(0.2)
    hk7 "Now that you’ve been introduced to our organization and what our goals are, let us have a short intermission."
    show hiroshi bored at Three2 with Dissolve(0.2)
    hk7 "..."
    show hiroshi happyblush at Three2 with Dissolve(0.2)
    hk7 "IIIIITTT'S... GAME TIME!!!"
    play music bg_merrygo loop fadein 1.0

    show hiroshi smile at Three2 with Dissolve(0.2)
    window show
    nvl clear
    narr "Hiroshi gave it his all.{w} The sourpusses became active, the monotonous room became livelier, jokes were made left and right...{w} It was all part of a package."
    narr "At the end of the intermission, the crowd pleaded for more. A pair of sly eyes responded, silent but manipulative."
    window hide
    show hiroshi smile2 at Three2 with Dissolve(0.2)
    window show
    narr "An upright thumb shot high in the air."
    narr "The students went wild, one of them whistled merrily at Hiroshi’s approval. An impromptu intermission later for fanservice, no doubt."

    window hide
    hide hiroshi with Dissolve(0.2)
    stop music fadeout 1.0
    scene bg classroom2 with dissolve
    window show
    nvl clear
    narr "In contrast to the cheerful atmosphere of the classrooms around the school, the council’s office is different.{w} The officers held a four o’ clock meeting after the children were ushered to their desired organizations."
    narr "Perfect attendance."
    narr "All eyes upon Sayo Ronoroa, the President and the head of the meeting.{w} Twelve seats in the manner of the Round Table, save for the three highest officials who were seated together: the President and her Vice,{w} and the Secretary who was taking down the minutes."

    window hide
    show sayo seriousserious at Three2 with Dissolve(0.2)
    window show
    nvl clear
    narr "All of them were given an equal chance to speak, addressing each of their plans and concerns for the current academic year.{w} Of course, today’s activities were also part of their agenda, considering it a success."
    narr "After the Treasurer, the Auditor gave his report.{w} His manner seemed like a façade for some, yet he gave no questionable details. He had to express ethos during times like this and the same is true during classes."
    window hide
    show sayo seriousserious at LS with Dissolve(0.2)
    show akira proud at RS with Dissolve(0.2)
    window show
    narr "He was none other than Akira Ichibana, the oftentimes aloof and light-hearted fellow.{w} A fool be the one who thinks he’s a fool."
    narr "He hides a lot of intelligence, recently acing the college exam reviews he took during summer."
    show akira fang at RS with Dissolve(0.2)
    narr "This Akira is far different from his usual self.{w} In either case, he is respected by his fellow batch mates. Not unlike Hikaru, he is a joker but more often noisier than her."

    nvl clear
    narr "It was yet to manifest, long after he finished giving his report."
    hide akira with Dissolve(0.2)
    narr "Then it went down to the Peace Officers, the Public Information Officer, and the Batch Representatives."

    nvl clear
    window hide

    hide sayo with Dissolve(0.2)
    
    "JUNE 7, 2013 - 1700H"
    window show
    nvl clear
    narr "Overall, it was a harmonious meeting."
    narr "If their adviser had been present, she would remark about their positive chemistry,{w} something which they have outdone the previous councils."
    narr "Admittedly, there were a few minor arguments in the process.{w} Still, the officers retained their cool."

    nvl clear
    narr "The bell has already rung."
    narr "Their first week of classes is over and so did the council’s meeting. Everyone tidied themselves up."
    window hide
    show sayo seriousserious at Three2 with Dissolve(0.2)
    window show
    narr "In behalf of their adviser, Sayo took charge of the adjournment."

    nvl clear
    window hide

    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "I would like to thank you all for being present at this meeting."
    show sayo normaltalk at Three2 with Dissolve(0.2)
    sr5 "Frankly, I expected less for all of us.{w} All of our visions align towards a single direction, but we should always keep in mind the responsibilities we have at hand."
    sr5 "We accepted this job; thus, we must know how to balance it.{w} That is all. Have a safe trip home everyone and I wish you all a pleasant Saturday."
    show sayo normaltalkleft at Three2 with Dissolve(0.2)
    sr5 "Watanabe, kindly remind everyone about the PTC tomorrow. I might be seeing some of you here, then."
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "Off you go! Meeting adjourned."

    "Slowly, the officers got up and left the small conference room."
    "The main office had four cubicles placed strategically near the middle of the room, two on each side. All four faced the exit."
    hide sayo with Dissolve(0.2)
    show akira happy at LS with Dissolve(0.2)
    "Akira was going around, inviting the officers for Ichirou’s gig in about thirty minutes."

    ai2 "You coming?{w} No? It will be fun. Promise..."
    show akira proud at LS with Dissolve(0.2)
    ai2 "There’s only a few of us...{w} Let’s go together."

    "Unfortunately, those whom he asked refused his invitation.{w} They either had other matters to attend to or have decided beforehand to go home immediately."

    show akira worriedleft at LS with Dissolve(0.2)
    ai2 "Drat! So, we are still the same count as before.{w} But, presumably, Miyu has accepted Ichirou’s invitation. That makes us six,{w} but what who shall I tap? Hmmm…"

    "He strokes his lower lip, thinking hard...{w} hard enough that he became almost detached to his surroundings."
    "A light tap on the back returned him to his senses."

    show akira angry at LS with Dissolve(0.2)
    ai2 "{b}{i}*GASP*{/i}{/b} Sayo... don’t do that!"
    show sayo happyclosed at RS with Dissolve(0.2)
    sr5 "Pardon. {i}*giggle*{/i}"
    show sayo smileopen at RS with Dissolve(0.2)
    sr5 "But you’ve been asking everybody else about some... get-together, am I not mistaken?"
    show akira happy at LS with Dissolve(0.2)
    ai2 "Oh, yeah. Ichirou’s been planning on this gig since June started.{w} It was whimsical. I don’t even know what he’s up to with this one."
    ai2 "But as long as it looks fun, I wouldn’t dare pass it up."
    show sayo smileclosed at RS with Dissolve(0.2)
    sr5 "Say, you guys've got a lot of time in your hands..."
    ai2 "..."
    show akira fang at LS with Dissolve(0.2)
    ai2 "{i}Say the word... I dare you.{/i}"
    show sayo smiletalk at RS with Dissolve(0.2)
    sr5 "...but don’t bother.{w} Would you first accompany me to Mrs. Genkai? I’ll just pass these documents and keys to her and {i}maybe{/i} I’ll make up my mind on the way."
    sr5 "You know, have a friendly chit-chat to alleviate boredom."
    show akira fangblush at LS with Dissolve(0.2)
    ai2 "Oh! Thank you! Thank you! Thank you! Anything for you, Ms. President.{w} We have plenty of time to loiter around – er, I mean, finish up everything. Hehehe..."

    show sayo smileopen2 at RS with Dissolve(0.2)
    "Sayo gave a sugary smile, moving her head slightly to her left."
    hide sayo with Dissolve(0.2)
    hide akira with Dissolve(0.2)
    "After ensuring all appliances were turned off, they locked the council’s office behind them.{w} IV-A’s room is their direct neighbour. They only took a few steps to the west staircase, which is directly across the room."

    scene bg school hallway with dissolve
    show sayo blankface at LS with Dissolve(0.2)
    show akira smile2 at RS with Dissolve(0.2)
    sr5 "And what will we do exactly when we get there?"
    show akira smileleft at RS with Dissolve(0.2)
    ai2 "I honestly don’t know what he’s planning to do. We’ll find out on the spot. Last thing I know is that we’ll be playing cards together."
    show sayo normaltalk at LS with Dissolve(0.2)
    sr5 "Cards? You mean like Poker or Go Fish?"
    show akira smileleft at RS with Dissolve(0.2)
    ai2 "No, the friendlier version, UNO."
    show akira surprised2 at RS with Dissolve(0.2)
    ai2 "No, the friendlier version, UNO.{fast} Wait...{w} did you say {i}Poker{/i}?"
    show sayo smileopen at LS with Dissolve(0.2)
    sr5 "I did. I was hoping to challenge someone to a game. {i}*exhale*{/i} Shame I’ve never played it for over a year."
    ai2 "Legit?! I never knew – I’ve never heard someone mention Poker as a first impression on you. You surprise me."
    show sayo smirknormal at LS with Dissolve(0.2)
    sr5 "I’m not surprised. Hm. Hm. You’re not going to challenge me, are you? For the experience, maybe?"
    show akira smirk at RS with Dissolve(0.2)
    ai2 "No. I don’t even understand its rules, let alone hoping to win as a novice.{w} I’ll be willing to wait, if that’s what you want. Hehehe..."
    
    "In her eyes, Akira is a different customer and an honest one.{w} All but two who knew of her secret hobby has challenged her for a few rounds of Texas Hold ‘em."
    "And none has ever prevailed against her.{w} But why has this not spread out yet?"

    sr5 "Before we play, I firmly ask my opponents not to disclose anything about it.{w} We’d always come to an agreement. What fun would it be if everyone knows about it?"
    
    show akira smile at RS with Dissolve(0.2)
    "{i}She... has a point.{w} While singing, dancing and online gaming are the most common hobbies one could have in our batch, she’s a rare gem. Hence, the excitement would die out if everyone knows about it.{/i}"
    "{i}Sayo knows that very well. As a sign of respect, I’ll keep my mouth shut.{w} She can do the talking herself if she wishes.{/i}"
    show sayo smileopen at LS with Dissolve(0.2)
    "{i}From our vantage point on the second floor, I can already distinguish I few faces from afar:{w} Ichirou, Hiroshi, Kyou, and Yoshiro. Sumiko has just arrived.{/i}"
    show akira smileleft at RS with Dissolve(0.2)
    "{i}Wait.{w} That makes us eight, counting Sayo in, too!{/i}"
    show akira surprised2 at RS with Dissolve(0.2)
    "{i}There’s someone coming - actually, three of them:{w} Miyu, Hikaru, and Inoue.{w} That guy managed to drag Inoue along?! A brave soul, I have to say.{/i}"

    hide akira with Dissolve(0.2)
    hide sayo with Dissolve(0.2)

    scene black with fade
    centered "{i}{b}Ten people, gathered in a single place,{w} counting down the last ten months of their high school years as a senior.{/b}{/i}"
    centered "{i}{b}The countdown is to commence soon.{/b}{/i}"
    return

label ch01_04_tenvictims:
    "JUNE 7, 2013 - 1730H"

    scene bg school fields evening with fade
    play music bg_calmertimes loop fadein 1.0
    "At the side of the auditorium near the backstage entrance sat a circle of eight."
    show ichirou proud at Eight3 with Dissolve(0.2)
    show kyou smile at Eight4 with Dissolve(0.2)
    show hiroshi bored at Eight5 with Dissolve(0.2)
    show miyu focusedpose at Eight6 with Dissolve(0.2)
    play sound sfx_rubikscube loop
    "At the side of the auditorium near the backstage entrance sat a circle of eight.{fast} Clockwise from Ichirou were Kyou, Hiroshi, Miyu,"
    show inoue smile at Eight7 with Dissolve(0.2)
    show hikaru naughty at Eight8 with Dissolve(0.2)
    show sumiko surprised2 at Eight1 with Dissolve(0.2)
    show yoshiro serious at Eight2 with Dissolve(0.2)
    "At the side of the auditorium near the backstage entrance sat a circle of eight. Clockwise from Ichirou were Kyou, Hiroshi, Miyu,{fast} Inoue, Hikaru, Sumiko, and Yoshiro."
    hide sumiko with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    hide ichirou with Dissolve(0.2)
    hide kyou with Dissolve(0.2)
    hide hiroshi with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    hide inoue with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)
    "They began by greeting each other and telling how their day went and all.{w} Questions were raised about why they were so few and what they will do."
    "Without an agenda, however, they are free to do anything as they wish."

    show ichirou confused at Eight3 with Dissolve(0.2)
    iy1 "Cards. You brought the cards, Sumiko?"
    show sumiko smirkclosed at Eight1 with Dissolve(0.2)
    st3 "Why not? This is the go-to game for gatherings."

    show sumiko smirk at Eight1 with Dissolve(0.2)
    "He dropped a pack of UNO cards at the center. Much to their delight, the conversations stopped and all eyes were on it."

    show ichirou smile at Eight3 with Dissolve(0.2)
    iy1 "So, we start when Akira gets here. We don’t want to leave anybody out, don’t we?"
    show miyu confused at Eight6 with Dissolve(0.2)
    mh8 "I can’t see from here. How about you, Ichirou? Have they come out yet?"
    show ichirou confused at Eight3 with Dissolve(0.2)
    iy1 "\"They?\"{w} Oh, Sayo and Akira? Haven’t noticed them.{w} Hey – you think she’ll come along?"
    show miyu worried at Eight6 with Dissolve(0.2)
    mh8 "How should I know? You’re the one who set up this gathering.{w} And you gave instructions to tap anyone who’s willing to join, didn’t you?"
    show inoue schemingclosed at Eight7 with Dissolve(0.2)
    is4 "Could’ve said, \"maybe.\""
    show miyu pissedclosed at Eight6 with Dissolve(0.2)
    mh8 "Yeah, but I’m just trying to explain things across."
    show inoue schemingopen at Eight7 with Dissolve(0.2)
    is4 "You always over explain things, Miyu – an acquired habit, perhaps? *giggle*"
    show miyu pissed at Eight6 with Dissolve(0.2)
    mh8 "{i}*sigh*{/i} Fine.{w} {i}I’ll just shut up and watch Yoshiro. I’m bored.{i}"

    hide ichirou with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    hide inoue with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)
    stop sound
    play sound sfx_footsteps2 loop
    "After the second one-minute solve by Yoshiro, footsteps –{w} a pair sounded from behind Miyu’s side.{w} Looking up, Ichirou and Hiroshi acknowledged the tenth participant."

    stop sound
    show akira happy at LS with Dissolve(0.2)
    show sayo happyclosed at RS with Dissolve(0.2)
    sr5 "Hey, everyone!"

    show sayo smileopen2 at RS with Dissolve(0.2)
    "Sayo was trailing behind Akira, giving her sweetest smile to the group."
    hide akira with Dissolve(0.2)
    show sayo smileopen at Three2 with Dissolve(0.2)
    show miyu smile at Three1 with Dissolve(0.2)
    show inoue smile at Three3 with Dissolve(0.2)
    "She took her place between Miyu and Inoue, the closest to the stairs where they came from."
    hide miyu with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    hide inoue with Dissolve(0.2)

    show akira proudclosed at Three2 with Dissolve(0.2)
    show sumiko surprised at Three1 with Dissolve(0.2)
    show yoshiro smile at Three3 with Dissolve(0.2)

    "She took her place between Miyu and Inoue, the closest to the stairs where they came from.{fast} Akira, on the other hand, sat beween Sumiko and Yoshiro."
    hide sumiko with Dissolve(0.2)
    hide akira with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)

    "Likewise, the rest welcomed the new arrivals."

    show sayo serioustalk at RS with Dissolve(0.2)
    sr5 "Pardon. We had to give a detailed report to Mrs. Genkai. Were you about to start?"
    show ichirou happy at LS with Dissolve(0.2)
    iy1 "We chose to wait.{w} But actually, we didn’t expect you to come so, thanks... welcome!"
    show sayo smiletalk at RS with Dissolve(0.2)
    sr5 "I feel the same. I was about to go home until Akira told me about it.{w} A one in a thousand chance, so why not? I might as well squeeze in some fun time while I’m at it."

    stop music fadeout 1.0
    play music bg_merrygo loop fadein 1.0
    "The conversation was cut short by Sumiko, who was already dealing cards to the players - five a hand, as per usual rules.{w} He placed the deck in the middle and dealt a card as a start."
    hide ichirou with Dissolve(0.2)
    hide sayo with Dissolve(0.2)

    window show
    nvl clear
    narr "The rules are simple."
    narr "The deck consists of cards numbered from 0 to 9, all colored red, blue, yellow, or green.{w} Depending on the game type, there are different special cards and rules available. The first is of the regular type."
    narr "First, one player drops a card from his hand, after which he determines the turn order."
    narr "Then, the next player must drop one of two kinds of cards: either of the same value or the same color as the previous card dropped.{w} If he has neither, then he draws cards until he gets a suitable one."

    nvl clear
    narr "To further add strategy and suspense to the game, there are special cards available.{w} When a player drops one of these, the next player has to drop a card with the specified color."
    narr "First are the {i}Wild Cards{/i}.{w} It can follow any card dropped by a player;{w} anyone who drops one specifies the next color to drop."
    narr "Second are the {i}Draw Cards{/i} which add cards to the next player’s hand.{w} Two types: the {i}+2 cards{/i}, which are colored and can be stacked;{w} the {i}+4 cards{/i}, also stackable but is also a {i}Wild Card{/i} hybrid.{w} These cards cannot be mixed in subsequent moves."
    narr "Third are the {i}Turn Manipulation Cards{/i}, a collective category containing the {i}Reverse{/i} and {i}Skip Turn{/i} cards. The former does exactly as its name, the latter skips the next player’s turn."

    nvl clear
    narr "Anytime a player has one card left in hand, he must declare \"UNO!\" before anyone else. In the group’s case, the first hand to the floor."
    narr "If another player gets to the ground first, it is an automatic +2 Draw for the player."
    narr "A player wins if he empties his hand first.{w} The game may continue until all or a set number of players finish. The deck replenishes infinitely unless agreed otherwise."

    nvl clear
    window hide

    show inoue happyclosed at Three3 with Dissolve(0.2)
    is4 "One more thing.{w} Anyone who’s dead last in the \"UNO!\" declaration shall get a {i}ketchup{/i} from the other players."
    show inoue happyopen at Three3 with Dissolve(0.2)
    is4 "...Right, Miyu?"
    show miyu focusedpose at Three1 with Dissolve(0.2)
    mh8 "Yes...{w} I suppose so."

    hide inoue with Dissolve(0.2)
    hide miyu with Dissolve(0.2)

    #call ch01_04A_uno # To Be Added

    stop music fadeout 1.0
    play music bg_porchswingdays loop fadein 1.0
    scene bg school fields evening with fade
    window show
    nvl clear
    narr "It is a little before six o’ clock, with the sun setting down. Its beautiful colors of red and orange reflected all over the open field.{w} While not a reflection, these colors are on everybody’s arms as well."
    narr "{i}Ketchup{/i} as Inoue refers to it."
    narr "After one suspenseful round, the small party decided to wind down and share a few stories. All ears were on those who spoke.{w} Laughter, sorrow, fright, and other emotions exhibited on their faces."

    nvl clear
    window hide

    show ichirou serious at Eight3 with Dissolve(0.2)
    show akira smile at Eight2 with Dissolve(0.2)
    show sumiko surprised2 at Eight1 with Dissolve(0.2)
    show kyou confused2 at Eight4 with Dissolve(0.2)
    show miyu naughty focuspose2 at Eight6 with Dissolve(0.2)
    show hikaru naughty at Eight8 with Dissolve(0.2)
    hy10 "Then Aria and I went to the arcade at Blue Wave. We tried one of those Whack-A-Mole games.{w} Unsuspectingly, she got a hammer on her head. {i}*snort*{/i} Poor thing if I say so."
    show hiroshi boredtalk at Eight5 with Dissolve(0.2)
    hk7 "What a meanie!"
    show hikaru talk at Eight8 with Dissolve(0.2)
    hy10 "Afterwards, she suggested that we play a light-gun horror game. It’s part of the series I am currently playing so I gave it a shot.{w} Halfway through the first stage, I died."
    show inoue smile at Eight7 with Dissolve(0.2)
    is4 "And... what about it?"
    hy10 "I begged her for a few more tokens, but she didn’t have any.{w} Eventually, she died and the countdown screen showed up. We walked away, and I noticed she left my side."
    show hikaru pissed at Eight8 with Dissolve(0.2)
    hy10 "The kicker?{w} Turns out she had a lot of tokens stashed away secretly! Hmph. What nerve!"

    show ichirou embarassed at Eight3 with Dissolve(0.2)
    show akira smirk at Eight2 with Dissolve(0.2)
    show sumiko sighclosed at Eight1 with Dissolve(0.2)
    show kyou happyclosed at Eight4 with Dissolve(0.2)
    show hiroshi happyblush at Eight5 with Dissolve(0.2)
    show inoue happyclosed at Eight7 with Dissolve(0.2)
    show miyu naughty closepose2 at Eight6 with Dissolve(0.2)
    "Though half-humorous, she managed to elicit a few laughs.{w} Miyu shrugged, knowing that this is a common occurrence between the two best friends."
    hide ichirou with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)
    hide akira with Dissolve(0.2)
    hide kyou with Dissolve(0.2)
    hide hiroshi with Dissolve(0.2)
    hide inoue with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)
    "A quarter of an hour passed."
    show sayo worried at Eight7 with Dissolve(0.2)
    stop music
    "A quarter of an hour passed.{fast} Sayo fumbled through her backpack, long enough for someone to take notice."

    show sumiko surprisedtalk at Eight1 with Dissolve(0.2)
    st3 "Is something amiss?"
    show sayo normaltalk at Eight7 with Dissolve(0.2)
    sr5 "My music sheets. I must have forgotten it somewhere.{w} Ah! It must be inside the auditorium."
    show hikaru focusright at Eight8 with Dissolve(0.2)
    hy10 "Can’t you get it next week? Besides, the main entrance is already closed off."
    show sayo worried at Eight7 with Dissolve(0.2)
    sr5 "No – you don’t understand.{w} The music sheets contain some songs we’ll use at Sunday; I’m glad I didn’t head straight home just yet.{w} Could anyone find it for me?"

    show sumiko surprised2 at Eight1 with Dissolve(0.2)
    "A minute passed with eyes looking at each other. Miyu finally broke the silence and rose from his seat."

    show miyu talk at Eight6 with Dissolve(0.2)
    mh8 "How many was it?"
    sr5 "It’s a book of music sheets.{w} You should find it somewhere in the backstage or in the main auditorium. I know since I was the last to leave after Mass."
    show miyu proudclosed at Eight6 with Dissolve(0.2)
    mh8 "I'll go. Just tell me the cover's color."
    show sayo smiletalk at Eight7 with Dissolve(0.2)
    sr5 "Thank you, Miyu!{w} It's black - you do have a flashlight with you? You can borrow mine if you wish."

    hide miyu with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)
    hide sayo with Dissolve(0.2)

    scene black with dissolve
    "Miyu pointed at his phone's flashlight.{w} He went around the circle, laying his hand on the backstage door. He twisted the knob and gave the door a light push."
    "Activating the flashlight, he entered the dark room and searched for the light switch.{w} Once he found it, Miyu flipped it up.{w}.. Except..."

    mh8 "Power’s out.{w} Oh, silly of me - it’s past six o’ clock. They must have cut the power from the main building. Moving on..."
    st3 "Make it quick, Miyu. I think the guard’s already signaling us to leave. He’s going to make a second whistle in fifteen minutes."

    "Light shuffling and occasional sounds of objects being moved emanated from the backdoor.{w} As time passed by, the sound became softer and softer...{w} until Miyu can no longer be heard."
    scene bg school fields evening with dissolve
    show sayo normaltalkleft at Eight6 with Dissolve(0.2)
    show inoue seriousleft at Eight7 with Dissolve(0.2)
    show hikaru focusleft at Eight8 with Dissolve(0.2)
    show sumiko surprised at EightM with Dissolve(0.2)
    show akira serious at Eight1 with Dissolve(0.2)
    show yoshiro serious at Eight2 with Dissolve(0.2)
    show ichirou focus at Eight3 with Dissolve(0.2)
    show kyou confused2 at Eight4 with Dissolve(0.2)
    show hiroshi worried at Eight5 with Dissolve(0.2)
    play music bg_onthingstocome loop fadein 1.0
    "To combat silence, the party was able to squeeze in another story, this time coming from Sayo.{w} In contrast to the previous stories, there was no opportunity to laugh.{w} All eyes were on her."
    "It was serious, a subject Miyu is especially interested on.{w} Shame he is currently navigating around the dark building."
    hide kyou with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)
    hide akira with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    hide ichirou with Dissolve(0.2)
    hide hiroshi with Dissolve(0.2)

    show sayo seriousnormal at Three2 with Dissolve(0.2)
    show inoue seriouspose at Three3 with Dissolve(0.2)
    show kyou serious talk at Three1 with Dissolve(0.2)
    kk9 "I remember it being on the news, yes. A year ago, if I remember correctly."
    sr5 "That’s right.{w} Ten students snuffed out one by one throughout the year in brutal ways - all from Sacred Heart Village.{w} It was definitely news back then, the hot topic of the neighbourhood."
    is4 "But the deed is done, right? I mean, what did they call it?{w} \"Curse Killings\"?"
    show sayo seriousnormalleft at Three2 with Dissolve(0.2)
    sr5 "The Sacred Heart Curse Killings, derived from the name of the victims’ school.{w} It’s also the name of the place they lived in."
    show kyou worriedclosed at Three1 with Dissolve(0.2)
    kk9 "Senior-level high school students, weren't they?{w} So close to graduation... a tragedy indeed. May God bless their souls."
    show sayo seriousserious at Three2 with Dissolve(0.2)
    sr5 "I haven’t dug deep into the details yet.{w} All I’ve got were information from news reports and conspiracy theories around the internet."
    sr5 "Frankly, I wouldn’t touch the latter, but I guess they’d make a good topic."

    "From her backpack, Sayo took out a small notepad."
    play sound sfx_pageturn
    "She opened it to a page containing bullet points of the theories she researched.{w} She recited each point, not yet filtering the factual from the trivial."
    hide inoue with Dissolve(0.2)
    hide kyou with Dissolve(0.2)

    show sayo seriousnormal at Three3 with Dissolve(0.2)
    show ichirou worried at Three2 with Dissolve(0.2)
    show yoshiro serious2 at Three1 with Dissolve(0.2)
    ys6 "Planned from the beginning, you say?{w} It doesn’t look that way to me considering the news reports and your statements. There’s no exact way to fit it."
    show sayo seriousclosed at Three3 with Dissolve(0.2)
    sr5 "I know, but what if it was?{w} I considered every possible angle I could look upon. It all leads to that in some way. I might formulate my own theory some time later when I look it up again."
    show yoshiro surprised2 at Three1 with Dissolve(0.2)
    ys6 "How about the identities of potential suspects? Have you got ‘em?"
    show sayo normaltalk at Three3 with Dissolve(0.2)
    sr5 "Unfortunately, still zero. All suspects were acquitted.{w} It’s one of the main reasons why this case is still open. How about all of you? Your thoughts?"
    show ichirou confused at Three2 with Dissolve(0.2)
    iy1 "You know, if Miyu was here, he’d be delighted to share something.{w} He’s still inside and, from here, I can’t seem to detect his presence."

    "Ichirou took a quick glance towards the backstage door. Just plain blackness.{w} No Miyu in sight, no footsteps to hear."
    "For a moment, the party silenced themselves to think."
    hide ichirou with Dissolve(0.2)

    show hiroshi boredtalk at Three2 with Dissolve(0.2)
    hk7 "You might want to consider this, Sayo.{w} Before we went here, we decided to drop by the guard’s post for a little chat. You might not have noticed us."
    show sayo seriousserious at Three3 with Dissolve(0.2)
    sr5 "I’m listening."
    show hiroshi worried at Three2 with Dissolve(0.2)
    hk7 "He asked us how our activities went and we asked how his day went in return, until the ball came to the recent Curse Killings."
    hk7 "We pretended to listen given how we felt the theories he talked about was absurd."
    show hiroshi worriedleft at Three2 with Dissolve(0.2)
    hk7 "That is... until he mentioned Suzumoto-san."
    show sayo worriedtalk at Three3 with Dissolve(0.2)
    sr5 "Ikari Suzumoto,{w} two batches ahead of us and part of the honor roll?{w} How is she involved in the tragedies?"

    "Before proceeding, Hiroshi made everyone promise that whatever he tells must not be spilled.{w} Everyone agreed on his conditions and he related the story he was told."
    "Shock{w} – the single word to accurately describe the party’s collective reaction."

    show sayo upset at Eight6 with Dissolve(0.2)
    show hiroshi worried at Eight5 with Dissolve(0.2)
    show yoshiro angry at Eight2 with Dissolve(0.2)
    show kyou worriedclosed at Eight4 with Dissolve(0.2)
    show hikaru worried at Eight8 with Dissolve(0.2)
    show inoue serioustalk2 at Eight7 with Dissolve(0.2)
    is4 "Preposterous!{w} It’s beyond the rules – there’s no rational way..."
    show inoue serioustalk at Eight7 with Dissolve(0.2)
    is4 "Preposterous!{w} It’s beyond the rules – there’s no rational way...{fast} Still, I never expected the poor girl to be that way.{w} She looked... alright."
    ys6 "That’s what he told us.{w} I, too, am in disbelief.{w} And take note, it didn’t come from him but from Suzumoto herself."
    show kyou worriedleft at Eight4 with Dissolve(0.2)
    kk9 "A deal made to the devil – certainly not a proper way to stop the curse.{w} But the idea is there. There’s still no way these things are related. Pestilence and death do not necessarily go hand in hand."
    show yoshiro serious2 at Eight2 with Dissolve(0.2)
    ys6 "Exactly. We were certainly not placed under high security.{w} Some of our upperclassmen were inflicted with dangerous illnesses, that’s all. They all managed to survive by a miracle."
    show yoshiro surprised at Eight2 with Dissolve(0.2)
    ys6 "Sacred Heart Academy suffered death, blunt I may sound.{w} They contrast each other!"
    show kyou serious pose at Eight4 with Dissolve(0.2)
    kk9 "A {i}catalyst{/i} if you want to put Suzumoto-san that way, otherwise none."
    show yoshiro worried at Eight2 with Dissolve(0.2)
    ys6 "But she did the conjuration, not them."
    show yoshiro worriedleft at Eight2 with Dissolve(0.2)
    ys6 "But she did the conjuration, not them.{fast} {b}*grunt*{/b} Sometimes, supernatural forces need to stay as they are."
    hy10 "So what does this mean for us?"
    sr5 "Nothing. We’re left out of it.{w} Kyou and Yoshiro are correct.{w} There must exist no connection. Nothing at all."
    show inoue serious at Eight7 with Dissolve(0.2)
    is4 "Then we leave it as a campfire story she made up on the spot. A commendable effort, I should say, to pull that off."
    show inoue seriousleft at Eight7 with Dissolve(0.2)
    is4 "Anyway, I’m more interested in the latter part of the story.{w} What did the symbol look like again?"
    show hiroshi boredtalk at Eight5 with Dissolve(0.2)
    hk7 "From what I can remember, he said Suzumoto formed a pseudo-circle resembling a clock.{w} Ten, not twelve, graduation pictures were pinned along its perimeter."
    hk7 "She was among those – I don’t know. I haven’t seen it personally."
    show inoue seriouspose at Eight7 with Dissolve(0.2)
    stop music fadeout 1.0
    is4 "Interesting.{w} Now, I’ve thought of something. How many are we right now?"
    show inoue serioustalk at Eight7 with Dissolve(0.2)
    is4 "One."
    show hikaru angry at Eight8 with Dissolve(0.2)
    hy10 "Two."
    hide yoshiro with Dissolve(0.2)
    hide kyou with Dissolve(0.2)
    hide hiroshi with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    hide inoue with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)

    show sumiko serioustalk at Three1 with Dissolve(0.2)
    show akira proud2 at Three2 with Dissolve(0.2)
    show yoshiro serious2 at Three3 with Dissolve(0.2)
    "Three... Four... Five..."
    hide sumiko with Dissolve(0.2)
    hide akira with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    show ichirou confused at Three1 with Dissolve(0.2)
    show kyou surprisedleft at Three2 with Dissolve(0.2)
    show hiroshi boredtalk at Three3 with Dissolve(0.2)
    "Six... Seven... Eight..."
    hide ichirou with Dissolve(0.2)
    hide kyou with Dissolve(0.2)
    hide hiroshi with Dissolve(0.2)

    show sayo serioustalk at Three1 with Dissolve(0.2)
    show inoue seriousleft at Three2 with Dissolve(0.2)
    show hikaru angry at Three3 with Dissolve(0.2)
    sr5 "Nine."
    show inoue smile at Three2 with Dissolve(0.2)
    is4 "It’s all good.{w} Forget I said any-{nw}"
    show sayo worriedtalk at Three1
    show inoue serioustalk2 at Three2
    show hikaru worried at Three3
    mh8 "Ten!"

    show miyu naughty smirk at Eight1
    "Miyu emerged from the door, a small book under his left arm.{w} He approached Sayo and gave it to her."
    hide inoue with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)
    show sayo happytalk at RS with Dissolve(0.2)
    show miyu smile at LS with Dissolve(0.2)
    play sound sfx_pageturn loop
    "With a smile on her face, she scanned the pages for any missing sheets."
    stop sound
    show sayo happytalkblush at RS with Dissolve(0.2)
    "With a smile on her face, she scanned the pages for any missing sheets.{fast} They were all complete."

    sr5 "Oh, Miyu.{w} Thank you! Thank you! Thank you!"
    show miyu naughty smile at LS with Dissolve(0.2)
    mh8 "So what were they about? Sunday School?{w} I saw some nursery rhymes contained inside."
    show sayo happytalk at RS with Dissolve(0.2)
    sr5 "That’s right.{w} My older sister brings this with her every Sunday for that purpose. The rest of the week, it’s with me, especially on First Friday Mass."

    "Miyu responded with a look of satisfaction."
    hide sayo with Dissolve(0.2)
    show miyu naughty talk at RS with Dissolve(0.2)
    show hiroshi boredtalk at LS with Dissolve(0.2)
    "Miyu responded with a look of satisfaction.{fast} He asked the others a rundown of what he missed.{w} Hiroshi summarized the whole story for him."
    hide hiroshi with Dissolve(0.2)

    show miyu happytalk at Three3 with Dissolve(0.2)
    mh8 "I missed a lot! How dare you exclude me, guys?"
    show miyu naughty smirk at Three3 with Dissolve(0.2)
    mh8 "I missed a lot! How dare you exclude me, guys?{fast} I'm just kidding. Hahaha..."
    show sumiko serious at Three1 with Dissolve(0.2)
    st3 "Strange... what took you so long, Miyu?"
    show miyu naughty talk at Three3 with Dissolve(0.2)
    mh8 "I had a bit of difficulty navigating around the place.{w} My flashlight isn’t that bright either, and I might have missed the book several times.{w} {i}{b}*grunt*{/b} Why did it have to be black{/i}?"
    show sumiko smile at Three1 with Dissolve(0.2)
    st3 "Fair enough.{w} And since you’re here, we can leave now, right?"
    show ichirou happy at Three2 with Dissolve(0.2)
    iy1 "Oh, that.{w} Let me thank everyone for coming. I honestly did not expect that much for this gathering, the first and last."
    hide sumiko with Dissolve(0.2)
    show akira happy at Three1 with Dissolve(0.2)
    ai2 "Well, it was fun while it lasted.{w} We’ve ten months ahead of us. Lots of time to fool around with each other again."    
    hide miyu with Dissolve(0.2)
    show sayo smileopen at Three3 with Dissolve(0.2)
    sr5 "It was a wonderful idea, Ichirou!{w} Let me know if you plan to hold another one. It’s good to join this every once in a while.{w} I think {i}I{/i} can influence the others to come along, too."
    show ichirou proud at Three2 with Dissolve(0.2)
    iy1 "You spoke for me, and I am left with no words.{w} Well, until we meet again – tomorrow! That’s right, I’ll be seeing you at the Parents-Teachers Conference tomorrow morning."
    show ichirou smile at Three2 with Dissolve(0.2)
    iy1 "Have a safe trip home!"
    hide akira with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    hide ichirou with Dissolve(0.2)

    scene bg school gate evening with dissolve
    play sound sfx_wind loop
    "Exactly when the group tidied up, the guard motioned them to leave.{w} The sun was nowhere in sight, coloring the sky a dark shade of blue.{w} A few casual conversations were made along the way."
    show inoue worried at RS with Dissolve(0.2)
    show sayo smileopen at LS with Dissolve(0.2)    
    "Inoue approached Sayo, the latter noticing her grim expression and anticipated her words.{w} She took the initiative."

    show sayo blankface at LS with Dissolve(0.2)
    sr5 "You look a bit pale. Can you make it tomorrow?"
    is4 "I’ll be fine. It’s just that –"
    show inoue sigh at RS with Dissolve(0.2)
    is4 "I’ll be fine. It’s just that –{fast} {i}*sigh*{/i} look, I know I’m not into that kind of stuff.{w} Yet, it disturbs me, the first to do so."

    show sayo worried at LS with Dissolve(0.2)  
    "Sayo’s smile dropped entirely and was replaced by a look of concern. Her pace slowed down."

    show sayo worriedtalk at LS with Dissolve(0.2)
    sr5 "Inoue, be specific. The Sacred Heart mystery or Suzumoto’s story?"
    show inoue sighclosed at RS with Dissolve(0.2)
    is4 "Both.{w} I’ve thought about it, compared the two events, and I seem to have found a link.{w} What if –"
    show sayo upset at LS with Dissolve(0.2)
    sr5 "I get it.{w} That’s why you counted how many we were earlier, didn't you?{w} It’s not going to happen, I assure you. A majority of us have already agreed on that."
    show inoue sighclosed at RS with Dissolve(0.2)
    is4 "Alright, but I just want my curiosities cleared.{w} I need someone rational enough to delve deeper into the subject.{w} That’s why I came to you."
    show sayo normaltalkleft at LS with Dissolve(0.2)
    sr5 "Then I’ll research further on the Curse Killings if I have time,{w} but what interest is there?"
    show sayo normaltalk at LS with Dissolve(0.2)
    sr5 "Get a good night’s sleep, Inoue - chase away whatever hex is lingering in your brain."
    show sayo smiletalk at LS with Dissolve(0.2)
    sr5 "Get a good night’s sleep, Inoue - chase away whatever hex is lingering in your brain.{fast} Besides, we have two days to unwind."
    show inoue dullsurprise at RS with Dissolve(0.2)
    is4 "I suppose you’re right.{w} I probably should stop thinking about it..."
    stop sound
    "They were nearly overtaken by the group of Sumiko, Akira, Yoshiro, and Miyu."
    "What interest is there, indeed?"
    hide inoue with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    return

label ch01_04A_uno:
    # Part 1: The first round/cycle (Done)
    # Part 2: Inoue vs. Miyu (Done)
    # Part 3: The UNO Declarations and the Resolution
    return

label ch01_05_sacredheart:
    scene black with fade
    "JUNE 13, 2013 - 1900H"
    scene bg street rain with fade
    play sound sfx_rain
    window show
    nvl clear
    narr "Thursday night."
    narr "A peaceful night almost devoid of sound, save for the light tapping made by the raindrops - not enough to suspend classes the following day."
    scene bg diningroom with dissolve
    narr "And cutlery! They accompanied the aroma of the sumptuous meal that the Shinozakis enjoyed.{w} Elegant candelabra in the middle to match the aesthetics.{w} It had class, though they were not that wealthy at all."
    narr "Dinner talk was the usual: how did school go, what trips and appointments to attend to at work and where to go for the weekend – ordinary family matters.{w} Once they had their fill, they tidied themselves up, as no maid is in their employ."
    scene bg livingroom with dissolve
    stop sound
    window hide
    show inoue casual smile at RS with Dissolve(0.2)
    window show
    narr "While their parents headed straight up to the master bedroom, Inoue and her brother stayed behind in the living room. They tuned in to their favorite channel after watching the primetime news."

    nvl clear
    window hide

    play sound sfx_phonering
    "{b}*RING* *RING*{/b}"
    stop sound

    show inoue casual confused at RS with Dissolve(0.2)
    "Who could be calling us tonight? I am expecting nobody.{w} Probably for big brother again... not my business."

    tomonori "Inoue, this call's for you."

    "He handed the receiver to me, moving away and lowering the volume. A polite chap, he is."

    show inoue casual confusedtalk at RS with Dissolve(0.2)
    is4 "Hello? Inoue Shinozaki speaking."
    unk "Good evening!{w} Sayo Ronoroa here. How are you?"
    show inoue casual determined at RS with Dissolve(0.2)
    is4 "Pleasant. You must feel the same.{w} I didn’t expect you to call tonight, so what brings you to?"
    sr5 "I was hoping for a quick chat with you. The evening weather probably will become worse by midnight.{w} But I want you to hold on for... an hour or so, I think. Am I not a bother?"

    show inoue casual confused at RS with Dissolve(0.2)
    "I sat down, preparing the couch pillow. Involuntarily, I looked around even though I didn’t need to.{w} Brother is there – enjoying the TV show by himself."

    play music bg_ghoststory loop fadein 2.0
    show inoue casual serious at RS with Dissolve(0.2)
    is4 "This is about last week, isn’t it? When we were heading back home?"
    sr5 "Yes, yes. In fact, I wanted to come to you earlier during lunch break.{w} I just didn’t know how to put it in a {i}pleasant{/i} way then. I feared I might ruin your day."
    show inoue casual serioustalk at RS with Dissolve(0.2)
    is4 "It’s alright. We’re on the line now – just the two of us. What did you find?"
    sr5 "Lots.{w} Besides the facts I’ve researched a few months ago, there have been quite some developments.{w} I noticed a pattern – the time frames at which the victims were killed."
    sr5 "There was exactly one victim per month – starting from June 2012 until March 2013."
    show inoue casual serioustalk2 at RS with Dissolve(0.2)
    is4 "Ten months, ten victims.{w} A grand-scale murder if it ever was one. But what was the motive?{w} It seems all random and disconnected to me – yet, somehow they all connect!"
    sr5 "Not motive... {i}motives{/i}.{w}. There is no single method in each of the killings – those who knew the victims related the manner of their death to... some aspect of their life."
    sr5 "There must exist a mastermind, then, {i}if{/i} the deaths were orchestrated.{w} Who were the accomplices? None proven, hence why this case is still open."
    show inoue casual seriouspose at RS with Dissolve(0.2)
    is4 "Can you give me the names?"
    sr5 "They are as follows:"

    window show
    nvl clear
    narr "Fuuko Rikiyama{w} - died by electrocution, June 28th.{w} He supposedly hanged herself using a live wire. Not certain how {i}that{/i} is possible."
    narr "Utsune Mushido{w} – died on a hiking accident, July 21st.{w} His was determined to be an overdose of chemicals from several poison darts."
    narr "Rioichi Yasuda{w} – death by hemorrhage, August 26th.{w} A marble figurine dropped to his head while in the ICU."
    narr "Ukemi Hajime{w} – death by hypothermia, September 30th.{w} Found inside her family’s slaughterhouse in one of the freezers, the same state as the other meat."
    narr "Domina Shibuya{w} – drilled in the throat during their Home Economics class, October 19th –"

    nvl clear
    window hide

    show inoue casual surprised at RS with Dissolve(0.2)
    is4 "Hold up!"

    "Did I just hear that right? A direct assault!{w} But... how come is the October victim’s death part of the ten? Unless..."

    show inoue casual serioustalk2 at RS with Dissolve(0.2)
    is4 "If not direct assault, then the drill must be faulty or rigged."
    sr5 "Correct. Bad luck on her part.{w} With the previous deaths occurring, those who witnessed it saw it a part of the Curse Killings, dismissing any rational explanation.{w} Home Economics classes were suspended for a month to make room for investigations."
    sr5 "They had one suspect, Rika Suzumiya, whose fingerprints were found on the drill.{w} She and Shibuya shared a long-time argument regarding a botched group project, even taking it personally."
    sr5 "However, she was proven innocent by reliable witness statements.{w} Another dead end was created."
    show inoue casual serioustalk3 at RS with Dissolve(0.2)
    is4 "That’s horrible! Even in school they weren’t safe.{w} What caused all this?{w} This phenomenon is beyond science – supernatural! I’d be a believer if I ever saw it with my own eyes."
    sr5 "Noted."
    show inoue casual sighpose at RS with Dissolve(0.2)
    is4 "You may proceed.{w} Excuse the hysteria."

    show inoue casual seriouspose at RS with Dissolve(0.2)
    window show
    nvl clear
    narr "The sixth is Eiko Shikata, council president{w} - victim of a gunshot wound to the heart, November 23rd.{w} The weapon was triggered by a device planted on her chair."
    narr "Seventh victim is Rika Suzumiya{w} – formerly accused of Shibuya’s murder, was killed herself on Christmas Day.{w} She drowned in the icy waters during a night beach trip, dead on arrival."
    narr "The eighth is Ikaruga Takezono{w} – found drugged inside a crushed car in a junkyard, January 25th.{w} Likewise, dead on arrival."
    narr "The ninth is named Ayanami Hayashibara{w} – suffered third-degree burns from a faulty tanning machine, February 24th.{w} It is akin to one of those horror movie deaths, the ones that seemed impossible in real life."
    narr "And finally, Kugimiya Oizumi{w} – hanged in her own room, head sliced in half by a hatchet, March 28th.{w} Such a shame for the girl – it was her school’s Commencement Exercises."

    nvl clear
    window hide

    sr5 "All in all, that’s ten.{w} What are your thoughts, Inoue? I want your input."
    is4 "Hmmm... One of them is the student council president, am I correct?"
    show inoue casual determined at RS with Dissolve(0.2)
    is4 "Hmmm... One of them is the student council president, am I correct?{fast} That sounds someone like you. Hehehehe..."
    sr5 "A haunting thought, I must admit. {i}*chuckle*{/i}{w} But it is all finished. What interest is there if no harm is expected?{w} Anything else?"

    "Let me enumerate each cause of death again."
    "Electrocution,{w} poisoning,{w} blunt trauma,{w} \"slaughtered\",{w} drilled in the throat,{w} gunshot wound,{w} drowning,{w} crushed to death,{w} third-degree burns,{w} and hanging."
    "Six to four, and on the latter half of each month!{w} Half a grand-scale murder in my book, but the absence of \"Who, Why, and How\" deems it a supernatural case, no wonder!"
    "Sayo seems to agree with me."
    stop music fadeout 2.0

    sr5 "Yes... We are on the same track so far."
    show inoue casual sigh at RS with Dissolve(0.2)
    is4 "Brutal – what lack of a better word to describe it all."
    sr5 "Hmph. Lame.{w} I have {i}better{/i} ideas."
    show inoue casual serioustalk2 at RS with Dissolve(0.2)
    is4 "Excuse me?"
    sr5 "That reminds me. There is one other detail I nearly forgot to bring up –"
    play music bg_vulcan loop
    sr5 "That reminds me. There is one other detail I nearly forgot to bring up –{fast} the story of Ikari Suzumoto."

    show inoue casual troubled at RS with Dissolve(0.2)
    "My attention was replenished and I changed my seating position.{w} I might as well catch another outburst from her."

    show inoue casual troubledtalk at RS with Dissolve(0.2)
    is4 "The upperclassman? Tomonori-kun's batchmate?{w} Did you find any link between her and the crimes?"
    sr5 "I love how you label them as {i}crimes{/i}.{w} Actually, that's true. Our girl is a Sacred Heart Village resident herself."
    sr5 "There’s even a corresponding news article of her interview, published at the aftermath of Oizumi’s death."

    "I had forgotten about Suzumoto.{w} Yes. Her interview was in the front page of The Correspondent. She did address the victims, but never can you read a word about the night guard’s story."
    "It’s an obscure secret, outrageous to many if it's leaked.{w} And as Kyou described, a catalyst and precursor to the following tragedy.{w} It is,{w} however, far-fetched."

    sr5 "It’s doubtful, but all roads lead there.{w} The passage of time enforces the belief.{w} What interest is there in fighting the unknown?"
    sr5 "We, the firm believers of the scientific method,{w} have no ground against this{w} – an established supernatural phenomenon.{w} Quantum mechanics is the closest weapon, yes, but not enough. What’s to prove that dark matter truly exists?"
    show inoue casual serioustalk at RS with Dissolve(0.2)
    is4 "You must be joking. The absence of evidence does not imply the work of demonic forces!{w} It is clear that the law has simply given up!{w} Such a gullible superstitious society we live in..."
    sr5 "{i}*sigh*{/i}"
    stop music fadeout 2.0

    show inoue casual troubled at RS with Dissolve(0.2)
    "I might have offended Sayo.{w} I haven't even thanked her for her efforts.{w} Best option is to lower my pride and {i}listen{/i}."

    sr5 "Do you believe in God?"

    show inoue casual determined at RS with Dissolve(0.2)
    "Definitely!{w} In my days here on Earth, how could I have lived not knowing the presence of"
    show inoue casual troubledtalk at RS with Dissolve(0.2)
    "Definitely!{w} In my days here on Earth, how could I have lived not knowing the presence of{fast} – I’m smothered.{w} This is where she wants me to be."
    "As a fellow theist, she’ll question my true belief – whether I’m truly devoted to it.{w} As a fellow rational student, however, she’ll find holes in my reasoning{w} – thus, there’s no way out!"
    show inoue casual sighpose at RS with Dissolve(0.2)
    "Silence, what Sayo wanted to hear.{w} I shook my head, acknowledging her words."

    sr5 "See? All knowledge cannot be done away with science.{w} There exists, however, at least {i}one{/i} explanation for everything{w} – under a superset of truths."
    show inoue casual sigh at RS with Dissolve(0.2)
    is4 "This is getting off-hand.{w} Can we return to our previous topic, please?{w} You’re just making my head spin. You always do."
    sr5 "Forgive me. {i}*giggle*{/i} I tend to get touchy.{w} Philosophy is an intriguing subject, is it not? Hehehehe...{w} That is all I have uncovered; the past is done away with.{w} The question is, what of the present?"
    show inoue casual troubledtalk at RS with Dissolve(0.2)
    is4 "Uncertainty."
    sr5 "Say, an hour has passed by quickly.{w} It was a pleasure conversing with you tonight. Have your curiosities been quelled?"
    show inoue casual smile at RS with Dissolve(0.2)
    is4 "Yeah.{w} I honestly found it a healthy discussion."
    show inoue casual troubled at RS with Dissolve(0.2)
    is4 "Yeah.{w} I honestly found it a healthy discussion.{fast} But there are still some details that bother me..."
    sr5 "Try not to think about it that much. You have other problems to worry about.{w} Do keep in mind tonight’s discussion, though. There are a lot to ponder upon."

    hide inoue with Dissolve(0.2)
    play sound sfx_ticktock
    window show
    nvl clear
    narr "The next last minute was spent exchanging farewells.{w} After hanging up, I am free to do whatever I wish.{w} What I need is a bed to fall upon."
    narr "I went upstairs, still thinking about it{w} – no, I shouldn’t let it bother me.{w} You’ve got things to do, Inoue. Focus.{w}"
    narr "Another hour passed{w} and I drifted off to sleep."

    scene black with fade
    play voice sfx_rain
    nvl clear
    narr "The clock chimed nine times."
    narr "The sounds of {i}pitter{/i} {i}patter{/i} were still there, albeit more audible.{w} From the outside, Inoue’s face looked peaceful.{w} Internally, it’s a different story."
    narr "The chiming of the clock{w} – its pattern so hypnotizing it resonated a subconscious voice,{w} that of Sayo."
    stop sound
    stop voice

    nvl clear
    window hide

    sr5 "Star light, star bright,"
    sr5 "The first star I see tonight..."
    sr5 "I wish I may, I wish I might,"
    sr5 "Have the wish I wish tonight!"
    sr5 "Sleep tight, Inoue-chan."
    play sound sfx_giggle
    sr5 "Sleep tight, Inoue-chan.{fast} Ehehehehehehehehe... {i}*giggle* *giggle*{/i}"

    play sound sfx_hangup
    "{b}{i}*beep* *beep* *beep*{/i}{/b}"
    stop sound
    return

label ch01_06_kyou:
    scene black with fade
    "JUNE 14, 2013 - 1140H"
    scene bg school outside with fade
    play music bg_twotogether loop fadein 1.0

    window show
    nvl clear
    narr "Lunch time."
    narr "The pathways are filled with students scurrying about looking for a good place to eat.{w} Most routines are simple{w} – buy from the canteen and return to the classroom."
    narr "The space around the campus is vast.{w} Maria St. Claire, being a single building,{w} has an open grassfield and trees overshadowing the walkways.{w} In fact, they constitute more than three-quarters of the total space!"
    narr "It offers a conducive environment for anything, barely having litter in sight.{w} The school is also the spearhead in keeping its surroundings healthy, what with its own organization dedicated to that task."

    scene bg msci with dissolve
    window hide
    show kyou smile at Three3 with Dissolve(0.2)
    show sumiko surprisedtalk at Three2 with Dissolve(0.2)
    window show
    nvl clear
    narr "Plate in hand, Kyou Kirisaki traveled back to his classroom, IV-A,{w} whilst having a chat with Sumiko, a IV-C student."
    window hide
    hide sumiko with Dissolve(0.2)
    scene bg classroom1 with dissolve
    show kyou smile at LS with Dissolve(0.2)
    window show
    narr "He sat at the third-row aisle, letting his eyes wander as he ate.{w} And he laid his eyes upon the front row."
    window hide
    show inoue blank at RS with Dissolve(0.2)
    window show
    narr "Inoue,{w} uncharacteristically withdrawn and mind wandering aimlessly."
    narr "She was not a person to bother at her current circumstance.{w} It concerned almost no one.{w} Her friends were somewhere else, probably at the canteen or at the other classroom."

    nvl clear
    window hide

    stop music fadeout 1.0
    show kyou calmleft at Three2 with Dissolve(0.2)
    kk9 "\"Anxiety in the heart causes burden,{w} but kind words cheer it up.\"{w} - Proverbs 12:25."

    show inoue serious at RS with Dissolve(0.2)
    "Slowly,{w} Inoue removed her hand from under her chin.{w} She turned to face the voice behind her."
    show kyou smile at Three2 with Dissolve(0.2)
    "She was greeted by a smile, the first few she had received that morning.{w} It took her an effort to show one herself{w} – false, nevertheless."

    show inoue smile at RS with Dissolve(0.2)
    is4 "I thank you for that,"
    show inoue worried at RS with Dissolve(0.2)
    is4 "I thank you for that,{fast} but {i}that{/i} is the exact cause of my worries.{w} {i}*sigh*{/i}"
    show inoue sigh at RS with Dissolve(0.2)
    is4 "Religion... is it ever true?{w} I still think it is but{w} they’re all the same."
    show kyou surprised2 at Three2 with Dissolve(0.2)
    kk9 "You’re confounded.{w} Perhaps something went wrong last evening?"
    show inoue seriousleft at RS with Dissolve(0.2)
    is4 "I’m not one to disclose secrets{w} and you know that, Kirisaki."
    show kyou smileleft at Three2 with Dissolve(0.2)
    kk9 "Ah, then I’m correct, I presume.{w} Say, how about I tell you a story, a parable, to ease yourself? Then it’s up to you to trust me or not.{w} Fair game?"
    show inoue dullsurprise at RS with Dissolve(0.2)
    is4 "No game.{w} I’m tired of it myself. I might have known every single one by heart – by {i}repetition{/i}."

    "I smiled in full understanding.{w} I gathered my thoughts - what she did for the past few days and anything that was a cause for concern.{w} Nothing, perhaps..."
    "Oh! I remember now{w} – the conversation nine of us had last week."

    show kyou serious smileclosedpose at Three2 with Dissolve(0.2)
    kk9 "Tell me about it, Inoue.{w} You’ve looked it up. I mean,{w} the \"Sacred Heart Curse Killings,\" were they?"
    play music bg_undaunted loop fadein 1.0
    show inoue serioustalk2 at RS with Dissolve(0.2)
    is4 "You know of it?{w} Who told you?!"
    show kyou serious smilepose at Three2 with Dissolve(0.2)
    kk9 "I know nothing beyond our gathering last Friday.{w} I see you harvested some new knowledge.{w} Worry not, for I know how to zip my mouth."
    show inoue worriedpose at RS with Dissolve(0.2)
    is4 "To tell you the truth, Kirisaki,{w} the tragedy itself is not my concern.{w} I’ve seen far too many horror movies bearing a similar premise. Is this alright?"
    show kyou happyclosed at Three2 with Dissolve(0.2)
    kk9 "{i}*chuckle*{/i} What is?"
    show inoue sigh at RS with Dissolve(0.2)
    is4 "It’s Sayo.{w} I talked to her{w} – no, she contacted me yesterday evening to talk about it.{w} And she mentioned some... {i}trivial{/i} quotes."
    is4 "There are a few things I want to consult with you.{w} You’re the pious one, and someone wiser than me."
    show kyou focusleft at Three2 with Dissolve(0.2)
    kk9 "Hmmmm...{w} Was there anything off in her manner?"
    show inoue serious at RS with Dissolve(0.2)
    is4 "Set that aside for now.{w} I’d like to momentarily clear up some affairs,{w} {i}personal{/i} things."

    window show
    nvl clear
    narr "I gave attention to her words and her delivery.{w} Perhaps not as I had initially thought,{w} as there is something deeper behind her anxiety."
    window hide
    show kyou confused at Three2 with Dissolve(0.2)
    window show
    narr "Only then I knew."
    show inoue seriouspose at RS with Dissolve(0.2)
    narr "She related to me the details of the tragedy, one I know beforehand.{w} I researched it myself. Then came the bits after that{w} – questions about science, theology, and the supernatural."
    narr "There are times she’d get herself lost in her story,{w} so I demanded she get to the point."

    nvl clear
    window hide

    show kyou confused at Three2 with Dissolve(0.2)
    kk9 "So, I ask of you,{w} what do you truly believe in?"
    show inoue serioustalk at RS with Dissolve(0.2)
    is4 "That all of these have plausible explanations, however difficult,{w} and none involve the Hand of God whatsoever."
    show kyou confusedtalk at Three2 with Dissolve(0.2)
    kk9 "That’s in your heart,{w} hundred percent?{w} Or a ninety-nine?"
    show inoue seriousleft at RS with Dissolve(0.2)
    is4 "*{i}sigh*{/i} Less.{w} I can’t give you an exact figure."
    show kyou serious talk at Three2 with Dissolve(0.2)
    kk9 "Inoue, I may be a religious person, as you say,{w} but there are times where certain explanations hold water and there are those where they do not.{w} The tragedy has more of the former."
    show kyou serious leftpose at Three2 with Dissolve(0.2)
    kk9 "The concept of karma shades some of these, as in the case of Shibuya and Suzumiya.{w} The two died in different ways{w} – every one of them did, correct?{w} Science still holds water."
    show kyou serious pose at Three2 with Dissolve(0.2)
    kk9 "The aftermath of each death is definitely subjective.{w} In my view, the souls of the dead undergo judgment, depending on their character.{w} That, however, has little bearing on the motive unless otherwise."

    show inoue worried at RS with Dissolve(0.2)
    "Inoue was quite puzzled, no matter how brief an explanation I gave her.{w} A long pause occurred, allowing me to finish my meal.{w} She raised another question."

    show inoue worriedpose at RS with Dissolve(0.2)
    is4 "If not religion, then what about quantum theory or the supernatural?{w} I’ve been told that not everything can be touched by science{w} – yet there exists a superset of truths...{w} I don’t know."
    show kyou surprisedleft2 at Three2 with Dissolve(0.2)
    kk9 "Then it appears you are mistaken."
    show inoue serioustalk at RS with Dissolve(0.2)
    is4 "Mistaken?"
    show inoue serioustalk2 at RS with Dissolve(0.2)
    is4 "Mistaken?{fast} It is too convoluted!{w} There is only so much for me to comprehend."
    show kyou surprisedleft at Three2 with Dissolve(0.2)
    kk9 "If that’s so, let’s untwist the facts slowly.{w} First, how did you distinguish those that were accidents from those that were actual murders?"
    show inoue serious at RS with Dissolve(0.2)
    is4 "The nature of the deaths themselves."
    show kyou surprisedtalk at Three2 with Dissolve(0.2)
    kk9 "Even as a possibility?"
    show inoue seriousleft at RS with Dissolve(0.2)
    is4 "Based on the way they were told.{w} If I judged corrcetly, six to four."
    show kyou serious2 at Three2 with Dissolve(0.2)
    kk9 "There’s a minor detail I picked up.{w} You said Suzumiya was {i}killed{/i} when she drowned {i}by accident{/i}{w} – a clear dissonance."

    show inoue surprised at RS with Dissolve(0.2)
    "Her eyes widened in genuine surprise.{w} Inoue contemplated upon herself whether her version is correct."

    stop music fadeout 1.0
    is4 "Kirisaki, are trying to insinuate{w} foul play?"
    show kyou confused at Three2 with Dissolve(0.2)
    kk9 "Unless you meant the waters killed her, but that would be a morbid personification.{w} If not, then the scores are even.{w} That disproves the idea of an accident."
    show inoue worried at RS with Dissolve(0.2)
    is4 "How? I... I’m lost.{w} The conditions for an accident are favorable around the time of her death."
    show kyou serious smilepose at Three2 with Dissolve(0.2)
    kk9 "Let no accident or intuitions assist the detective,{w} or so it says."
    show inoue serioustalk2 at RS with Dissolve(0.2)
    is4 "Kirisaki, this isn’t a murder mystery!{w} This is real life – anything could happen.{w} Are you trying to Sherlock me?"
    show kyou serious smileclosedpose at Three2 with Dissolve(0.2)
    kk9 "Hehehehe... Pardon.{w} I may seem to have taken it too far."
    show kyou serious leftpose at Three2 with Dissolve(0.2)
    kk9 "But my point is this{w} – for every effect there is a cause, the evidence present or not."
    kk9 "Take my word on Suzumoto-san’s story seriously, but take care not to venture into the unknown excessively."
    show kyou serious pose at Three2 with Dissolve(0.2)
    kk9 "That, and pray you keep a rational thought ready.{w} Naivety won’t get you too far,{w} but I’m not saying you are."
    show inoue sighclosed at RS with Dissolve(0.2)
    is4 "I understand."
    show inoue smile at RS with Dissolve(0.2)
    is4 "I understand.{fast} And Kirisaki, I must offer my thanks for suppressing my worries.{w} I’ve been thinking about them since last night."
    show kyou smirk at Three2 with Dissolve(0.2)
    kk9 "My pleasure. {i}*chuckle*{/i}{w} Is there anything else you wish to consult me about?"
    show inoue seriousleft at RS with Dissolve(0.2)
    is4 "Darn! My meal’s gone cold, but that’s fine.{w} Luckily, my seatmates aren’t here yet."
    show inoue talk at RS with Dissolve(0.2)
    is4 "Darn! My meal’s gone cold, but that’s fine.{w} Luckily, my seatmates aren’t here yet.{fast} Now, about my last point..."
    show kyou happy at Three2 with Dissolve(0.2)
    kk9 "Ah, yes! It almost slipped off my mind.{w} It was my concern anyway, so please continue."

    show kyou smile at Three2 with Dissolve(0.2)
    window show
    nvl clear
    narr "Inoue is quite a hospitable and level-headed person,{w} save for situations such as this.{w} Just like the first part of our conversation, she spoke while I listened."
    show kyou confused at Three2 with Dissolve(0.2)
    narr "Then, in the middle of it, I was struck with concern – with doubt.{w} Sayo and I were classmates during our sophomore years,{w} and I can recall specific instances when we’ve talked."
    show kyou serious2 at Three2 with Dissolve(0.2)
    narr "But not in the way Inoue described their conversation to me."

    nvl clear
    window hide
    hide kyou at Dissolve(0.2)
    hide inoue at Dissolve(0.2)
    return

label ch01_07_countdown:
    scene black with fade
    "JUNE 15, 2013 - 2300H"
    scene bg ministryroom with fade
    play sound sfx_footsteps2 loop

    window show
    nvl clear
    narr "Pairs of feet shuffled across the function room.{w} Though busy, the Youth Group members eased themselves through friendly chatter.{w} A six-hour prayer vigil is scheduled at midnight."
    narr "The front-right door creaked, letting in a small figure with spectacles."
    window hide
    show sayo casual glass smile at Three2 with Dissolve(0.2)
    play music bg_twotogether loop
    window show
    narr "Sayo Ronoroa approached the chancel, greeted her church mates, and placed the music book on the stand."
    narr "She opened it a few pages from the middle.{w} Satisfied, she went over to the other members to help."
    stop sound

    nvl clear
    narr "The banner, already set in front of the room, proclaims -"
    narr "SQUIRES OF THE HERALD KING YOUTH GROUP"
    narr "They were a relatively small group, having fifteen registered members.{w} They attend a 3rd Sunday Prayer Vigil as a regular devotion. Attendance is non-compulsory in case of emergency."
    narr "At the back, Sayo wiped away the sweat from her forehead.{w} She entertained thoughts during her idleness, and to each she smiled dearly."

    nvl clear
    window hide
    show sayo casual glass smileclosed at RS with Dissolve(0.2)
    window show
    narr "The conception of the highest seat during the last gathering{w} and the blessing of the school year for tonight!{w} How fortunate it is to have been a member of this Youth Group."

    window hide
    show ikuko casual smirk at LS with Dissolve(0.2)
    window show
    nvl clear
    narr "It was all thanks to Ikuko Mimori, a classmate one year longer in service.{w} The month after Sophomore year, she invited Sayo to the Youth Group.{w} As a result, their relationship deepened between themselves and the Higher Being."
    narr "Sayo is forever grateful."
    window hide
    show sayo casual glass smiletalk at RS with Dissolve(0.2)
    show ikuko casual smile at LS with Dissolve(0.2)
    window show
    narr "As they waited for the bell, they brought up a variety of topics. How they have been, the current events, personal thoughts,{w} anything they could come up with."
    narr "They left no room for gossip, strictly adhering to their moral code.{w} Sayo mentioned the gathering once more, but no traces of neither the previous tragedy nor her conversation with Inoue.{w} She chose her stories well so as not to gloom the night."
    narr "Instead, they opted to discuss the vigil’s flow, midnight to dawn.{w} They rehearsed the words in their minds, filling in gaps whenever there is one."

    nvl clear
    window hide

    show sayo casual glass normaltalkleft at RS with Dissolve(0.2)
    sr5 "1 Corinthians 16:9-13...{w} it comes with the Daily Bread.{w} At two in the morning, preferably?"
    show ikuko casual smiletalk at LS with Dissolve(0.2)
    ikuko "Yes. That would be a good placement,{w} though I’d rather have it at five, just before dawn."
    show sayo casual glass smiletalk at RS with Dissolve(0.2)
    sr5 "Then five it is if you wish!{w} You’re the one in charge of the overall flow."

    window show
    nvl clear
    narr "The Daily Bread Reading is one of their primary segments during a vigil.{w} Unlike other activities, it is spontaneously placed at any timeslot the members prefer, usually within an hour before dawn."
    narr "Its placement is left to the one in charge of the program, Ikuko at present."
    narr "As an assignment, each member is asked to give their reflection about the passage used in the reading.{w} This is to deepen their spiritual understanding and to learn from each other."

    nvl clear
    window hide
    stop music

    show sayo casual glass seriousleft at RS with Dissolve(0.2)
    sr5 "Here’s what I make of this{w} – the truth of human nature.{w} To make an effort in concealing what’s underneath is a natural process; it persists against all effort."
    show sayo casual glass serious at RS with Dissolve(0.2)
    sr5 "Fear, not courage, is what makes men truly interesting.{w} To exploit those as a weapon is to have him realize the insufferable truth – stigmas that last forevermore."
    show ikuko casual talk at LS with Dissolve(0.2)
    ikuko "And when misfortune befalls one, the mask vanishes and all impression falls apart with it.{w} Empathy bridges the effects as a ripple."
    show sayo casual glass serioustalk at RS with Dissolve(0.2)
    sr5 "Correct.{w} Hence the relevance of the vigil’s theme."
    show ikuko casual blank at LS with Dissolve(0.2)
    ikuko "It skirts the wishes of St. Paul; at the same time, you’ve struck the chord.{w} Isn’t that common knowledge though?"
    show sayo casual glass serioustalkleft at RS with Dissolve(0.2)
    sr5 "A safe assumption, if not banal.{w} Only a heartless would be as bold as to fear nothing.{w} Death perhaps,{w} but it bars none!"
    show ikuko casual smiletalk at LS with Dissolve(0.2)
    ikuko "Compose yourself, my friend. Your emotions are driving you away again. {i}*chuckle*{/i}"
    show sayo casual glass smile2 at RS with Dissolve(0.2)
    sr5 "My apologies."
    show ikuko casual talk at LS with Dissolve(0.2)
    ikuko "But surely, you’ll drop some of it in the discussion later?"
    show sayo casual glass normaltalk at RS with Dissolve(0.2)
    sr5 "It perturbs most, admittedly.{w} I’d rather discuss it in private, especially to those with an open mind."
    show sayo casual glass smiletalk at RS with Dissolve(0.2)
    sr5 "It perturbs most, admittedly.{w} I’d rather discuss it in private, especially to those with an open mind.{fast} Fascinating, isn’t it? {i}*chuckle*{/i}"

    show sayo casual glass smile at RS with Dissolve(0.2)
    show ikuko casual happy at LS with Dissolve(0.2)
    "Their smile drew a mutual air of satisfaction.{w} What could possibly make the night more interesting?"
    hide ikuko with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    scene black with fade

    "Earlier This Evening..."
    scene bg bedroom with fade
    play sound sfx_ticktock loop
    window show
    nvl clear
    show ichirou smile at LS with Dissolve(0.2)
    narr "Ichirou, as class president of IV-B, made his final announcements online."
    show ichirou proud at LS with Dissolve(0.2)
    narr "With books and backpack made up, he called it a night.{w} But not before going for a few rounds of Candy Crush."
    hide ichirou with Dissolve(0.2)

    nvl clear
    show miyu proudclosed at RS with Dissolve(0.2)
    narr "In contrast, Miyu retired to bed with his cell phone radio, a perfect opportunity to lose himself in thoughts.{w} Occasionally, he would exchange messages with Sanae Yoshida, a former classmate of his."
    narr "A healthy friendship they had – a durable link.{w} \"Nothing better than to pass away the dullness!\" he would reason.{w} And when it stops, he would return to his activities."
    narr "First Law, indeed."
    hide miyu with Dissolve(0.2)

    nvl clear
    show sumiko seriousleft at RS with Dissolve(0.2)
    narr "Ever forgetful, Sumiko’s eyes ran through the monitor several times.{w} His mind relaxed upon the sight of his announcement on class IV-C’s FB group."
    narr "\"Wear your PE uniforms on Tuesday – we have a social dance activity at first period. Just this Tuesday, friends. Good night!\""
    narr "Akira commented on the post, volunteering to bump it the following day.{w} Sumiko liked this idea."
    narr "As if he would buy it, that is."
    hide sumiko with Dissolve(0.2)
    stop sound

    play sound sfx_beep
    nvl clear
    narr "{b}*BEEP* *BEEP* *BEEP*{/b}"
    narr "The thermometer read 39.0C."
    show inoue casual troubledtalk at LS with Dissolve(0.2)
    narr "As Inoue suspected, she had symptoms of flu.{w} She took a tablet of paracetamol and her mother advised her to stay in bed for a few more days.{w} Inoue desired to protest, but she could not."
    narr "It was peculiar, as she traced the cause to none.{w} Thankfully, she was free from dengue – that could have been much worse.{w} Faced with the possibility of missing Monday's activity, her mother prepared a letter in case."
    show inoue casual troubled at LS with Dissolve(0.2)
    narr "Presently, Inoue relaxed her mind;{w} her body comfortably snuggled under the fluffy blankets.{w} Any signs of worry might worsen her condition."
    hide inoue with Dissolve(0.2)

    play sound sfx_ticktock loop
    nvl clear
    show yoshiro serious at RS with Dissolve(0.2)
    narr "Yoshiro decided to look up the Sacred Heart tragedy, finding its \"cursed\" label intriguing.{w} It was, as he thought, as grounded as possible{w} – yet the actions inhuman."
    narr "He remembered the upperclassman’s story and tried to establish a connection.{w} Zero,{w} apart from the latter’s residency being similar to that of the victims."
    show yoshiro serious2 at RS with Dissolve(0.2)
    narr "Just then, questions came to him."
    narr "What if the \"catalyst\" perceived an omen?{w} It made no sense even as an aversion – an inverse example – yet...{w} if it was actually delayed, then..."
    hide yoshiro with Dissolve(0.2)

    stop sound
    play sound sfx_pageturn
    nvl clear
    show hiroshi worried at LS with Dissolve(0.2)
    narr "Hiroshi placed {i}The Battle of the Labyrinth{/i} down after the last chapter.{w} It had him thinking, given the nature of the book.{w} Its theme blended too well with their topic, triggering some thoughts within him as he read."
    show hiroshi worriedleft at LS with Dissolve(0.2)
    play sound sfx_ticktock loop
    narr "In the darkness, he laid in silence tuning his mind in the same way Yoshiro's is.{w} He considered the possibility of having Suzumoto as a suspect."
    show hiroshi determined at LS with Dissolve(0.2)
    narr "He laughed at himself, aware of the idea’s absurdity."
    narr "Suppose it happens again?{w} That is a haunting thought, but it better be fairer than the last.{w} Best case if it doesn’t.{w} Ever."
    hide hiroshi with Dissolve(0.2)

    play sound sfx_ticktock loop
    nvl clear
    show hikaru smile at LS with Dissolve(0.2)
    narr "There was nothing different about Hikaru, spending the weekend on her laptop as usual.{w} She was streaming shows from the US, indulging herself as much as she wished."
    narr "The props for Tuesday’s activity lay at her bedside.{w} Sumiko gave her a spare key should she ever arrive before six."
    hide hikaru with Dissolve(0.2)

    nvl clear
    show kyou surprisedleft2 at RS with Dissolve(0.2)
    narr "Kyou received the same instructions from Inoue.{w} However, the class president was ailing and unsure of her condition come Monday.{w} He possesses one of the keys being the earliest in their class."
    narr "He heard of Inoue’s condition and wished her health to return.{w} Kyou thought that she was merely stressed out."
    show kyou serious leftpose at RS with Dissolve(0.2)
    narr "But as he thought about the previous day, he considered the cause."

    nvl clear
    narr "There were things out of place, such as Sayo’s behavior during the phone call.{w} He only has Inoue’s word for it, and she could be making it up.{w} But it was genuine – nobody would dare lie to him; he abhors those."
    narr "Words alone would not cause an ailment{w} – or rather..."
    show kyou serious2 at RS with Dissolve(0.2)
    narr "At times like this, he would do some soul-searching to quell himself.{w} He picked up his Bible and began meditating on a few verses."
    narr "Afterwards, he opened his Daily Bread and marked the entry for June 15.{w} He scanned the next entry for June 16, {i}Strength of a Man{/i}, and reflected upon himself."

    nvl clear
    window hide

    show kyou serious smile2 at RS with Dissolve(0.2)
    kk9 "Quite fitting.{w} {i}*sigh*{/i} I’ll save this for tomorrow evening."
    hide kyou with Dissolve(0.2)
    stop sound

    scene bg ministryroom with dissolve
    play sound sfx_handbell
    "{b}{i}*RING* *DING* *RING* *DING*{/i}{/b}"

    play sound sfx_clockbell
    window show
    nvl clear
    narr "The oft familiar tune called everyone’s attention, all fifteen of them."
    show sayo casual glass smile at RS with Dissolve(0.2)
    show ikuko casual smile at LS with Dissolve(0.2)
    narr "The two girls walked together to the front and took their places at the chancel."
    hide ikuko with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    show sayo casual glass smile at LS with Dissolve(0.2)
    narr "Sayo led the small choir by playing the keyboard, with the music book at the opening hymns."
    hide sayo with Dissolve(0.2)
    show ikuko casual smirk at RS with Dissolve(0.2)
    narr "Ikuko glanced at her friend, twinkled, and began the vigil."
    hide ikuko with Dissolve(0.2)
    stop sound
    narr "By the twelfth strike, the Youth Group members performed the opening hymn.{w} No hiccups and all went smooth from there.{w} Everything went as planned."
    play sound sfx_revolver
    narr "Brilliantly executed – one should say."

    nvl clear
    window hide
    return

label ch01_08_disappearance:
    scene black with fade
    "JUNE 18, 2013 - 1130H"
    scene bg classroom2 with fade

    window show
    nvl clear
    narr "Class IV-C was livelier than usual.{w} Topics about the social dance activity buzzed around the students - who looked handsome and lovely, who made the most graceful steps, and whatnot.{w} Some were even considering their prom dates this early."
    narr "There are a few exceptions, such as Sumiko and Akira."
    window hide
    scene bg classroom1 with fade
    show akira proud at Eight2 with Dissolve(0.2)
    show sumiko serious at Eight3 with Dissolve(0.2)
    show ichirou worried at Eight7 with Dissolve(0.2)
    window show
    narr "At present, the three – adding Ichirou – discussed the upcoming College Entrance Exam review sessions.{w} The Science Club is one of the event's major facilitators."
    window hide
    show miyu bored at Eight6 with Dissolve(0.2)
    window show
    narr "Miyu handed the signed document to Ichirou, which the latter accepted."

    nvl clear
    window hide

    show miyu serious at Eight6 with Dissolve(0.2)
    mh8 "I shouldn’t be the one doing this.{w} Isn’t she in good health already?"
    show ichirou serious at Eight7 with Dissolve(0.2)
    iy1 "Nope.{w} We’d be chewed out if we waited until tomorrow. Today’s the deadline."

    hide miyu with Dissolve(0.2)
    "Miyu acknowledged it and went out to have lunch.{w} Sumiko signed a similar document."

    show sumiko smirkclosed at Eight3 with Dissolve(0.2)
    show ichirou confused at Eight5 with Dissolve(0.2)
    st3 "So Kyou followed after Shinozaki, huh? Hehehehe. What rain could do to people...{w} I saw him yesterday during the assembly and he looked fine."
    iy1 "So did I.{w} If only we were given the agreement yesterday, I wouldn’t have come to you.{w} But then again, Shinozaki still has flu."
    show sumiko surprisedtalk at Eight3 with Dissolve(0.2)
    st3 "Flu? Who told you that?"
    show ichirou serious at Eight5 with Dissolve(0.2)
    iy1 "Kyou.{w} I exchanged a few words with him yesterday during break time and he mentioned Inoue's condition. Hope she gets better."
    show akira proud2 at Eight2 with Dissolve(0.2)
    ai2 "That aside, you’ll send this to Sayo after Nakashima signs?{w} They are in the same class."
    show ichirou smile at Eight5 with Dissolve(0.2)
    iy1 "Ayumi? Yeah, I’ll send her copy before giving it to Sayo.{w} The girl’s probably buying some food right now."

    window show
    nvl clear
    narr "The conversation went on for a bit until Ichirou noticed Ayumi return.{w} He left the two and thanked them."
    hide ichirou with Dissolve(0.2)
    show miyu naughty smile at Eight5 with Dissolve(0.2)
    narr "Miyu returned not a minute after Ichirou left, sitting one row ahead of the two."
    hide miyu with Dissolve(0.2)
    scene bg msci with dissolve
    narr "At exactly noon, Sayo passed by IV-C."
    show sayo worried at Eight8 with Dissolve(0.2)
    narr "It was an unusual sight –{w} the bubbly girl worried about something this early in the year.{w} Her face evidenced her anxiety, but her gait remained the same."
    window hide
    show sayo worriedtalkclosed at Eight8 with Dissolve(0.2)
    hide sayo with Dissolve(1.0)
    scene bg classroom1 with dissolve
    window show
    narr "When she was no longer in sight, Akira shook his head in sympathy."

    nvl clear
    window hide

    show sumiko surprised at Eight5 with Dissolve(0.2)
    show akira worried at Eight3 with Dissolve(0.2)
    ai2 "Gosh. Don’t tell me their class didn’t do well in the activity.{w} Poor Sayo looks like she lost some stocks{w} or a pile of chips."
    show sumiko smirkclosed at Eight5 with Dissolve(0.2)
    st3 "Hehehehehe. That’s a good one."
    show sumiko seriousleft at Eight5 with Dissolve(0.2)
    st3 "Hehehehehe. That’s a good one.{fast} But I suggest we make no further jokes. It could be worse than we think."
    show akira worriedleft at Eight3 with Dissolve(0.2)
    ai2 "Or maybe she could be tired. Seriously, it’s the same for us."
    show akira surprised at Eight3 with Dissolve(0.2)
    ai2 "Oh!{w} Here’s the spare key.{w} I might risk losing it."

    show sumiko angry at Eight5 with Dissolve(0.2)
    "Akira produced a small silver key from his wallet and gave it to Sumiko.{w} The latter hesitated, asking if he will come later than usual.{w} Akira, however, insisted."
    show sumiko sighclosed at Eight1 with Dissolve(0.2)
    "Sumiko shrugged and passed it to Akira’s service mate."
    show sumiko smile at Eight1 with Dissolve(0.2)
    show akira fangblush at Eight3 with Dissolve(0.2)
    "Sumiko shrugged and passed it to Akira’s service mate.{fast} She glared at Akira whose face contorted with embarrassment.{w} She threw the spare key back to him."
    hide akira with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)

    scene black with fade
    window show
    nvl clear
    narr "{i}The subscriber cannot be reached. Please try again later.{/i}"
    scene bg school hallway with fade
    show sayo worried at LS with Dissolve(0.2)
    narr "The same robotic voice returned my call for the third time.{w} I tried to reach Inoue since morning, hoping to check on her, but without luck."
    narr "That alone was unusual{w} – she never misses calls twice or even thrice during weekdays.{w} I knew that since we were freshmen.{w} If today was Sunday, that’ll be alright."
    narr "I don’t have Kirisaki’s number so I’ll just have to ask their adviser about it."
    hide sayo with Dissolve(0.2)

    nvl clear
    scene bg facultyroom with dissolve
    play sound sfx_dooropen
    narr "I opened the door to the faculty room and looked around.{w} There’s Mrs. Genkai chatting with Ms. Harada."
    narr "Perfect.{w} I’ll hand these to Mrs. Genkai before I ask Ms. Harada about the two."
    show sayo smileopen at Three2 with Dissolve(0.2)
    narr "Before I conducted my business, I gave a polite gesture they received gracefully.{w} I wasted no time."
    show sayo seriousserious at Three2 with Dissolve(0.2)
    narr "Luckily, Ms. Harada took the initiative by asking me about Inoue and Kirisaki.{w} Having no idea on their condition either, she took out her smart phone and dialed the Shinozaki residence first."
    narr "We all waited in anticipation."

    nvl clear
    window hide

    t_gen "You’ve eaten well, Sayo-chan?"
    show sayo serioustalk at Three2 with Dissolve(0.2)
    sr5 "Yes, but not as well.{w} I’ve been trying to contact Shinozaki since this morning and I couldn’t reach her."
    show sayo worried at Three2 with Dissolve(0.2)
    sr5 "Yes, but not as well.{w} I’ve been trying to contact Shinozaki since this morning and I couldn’t reach her.{fast} Whatever happened to that girl?"
    t_gen "Well, at least Hirano is present for these papers.{w} Tokubei too.{w} I’ll save the questions until we get through."
    show sayo seriousnormal at Three2 with Dissolve(0.2)
    sr5 "I’ll stay for a while.{w} I too, am worried about them."
    t_har "Uh, hello? Is this Inoue Shinozaki's mother?{w} This is her adviser, Ms. Harada, speaking."

    "She managed to connect within a minute.{w} The conversation with Mrs. Shinozaki took place in loudspeaker, with Mrs. Genkai and me listening closely."
    "I gathered the following after the pleasantries."
    hide sayo with Dissolve(0.2)

    t_har "I apologize for calling on such short notice, Mrs. Shinozaki. You might be busy.{w} Tell me, how is Inoue doing?"
    ms_shi "She’s alright.{w} Her fever went away yesterday morning and she’s her former self, thankfully. {i}*chuckle*{/i}{w} Did she miss anything important, madame?"
    t_har "Some agreement paper due this afternoon, which is already done away with,{w} and a practical activity.{w} The latter is alright provided she’s in the condition to perform."
    ms_shi "I’m sorry. When was this? Monday?"
    t_har "This morning – second period. Eight o’ clock."

    "There was silence.{w} I sensed the confusion from the other end."

    ms_shi "That’s not possible. I saw her off this morning at quarter to six.{w} She didn’t go off anywhere, did she?!"
    t_har "I refuse to believe that.{w} Unless I'm mistaken, I never saw her this morning - none of her classmates did.{w} Being in my advisory class, I never forget a student – {i}especially{/i} our class president."

    play sound sfx_waterdrip loop
    show sayo worriedtalk at Three2 with Dissolve(0.2)
    "What?! How is that...?{w} A crack in Mrs. Shinozaki's voice... and in disbelief.{w} There must be a mistake!"

    window show
    nvl clear
    narr "Even without continuing, we shared the same conclusion{w} – Inoue Shinozaki has vanished.{w} No traces of her anywhere,{w} neither in her home nor here at school."
    narr "As Ms. Harada tried to calm Inoue’s mother down, I settled down to think.{w} However, the shock I received clouded my thoughts.{w} I wanted to cry, but I retained my resolve."
    narr "Who would want to see the head of the student body cry? That'll shatter the morale of people."

    stop sound
    nvl clear
    show sayo worried at Three2 with Dissolve(0.2)
    narr "Ms. Harada gave her instructions to file a missing person report immediately in case of kidnapping.{w} Then, she cut the line."
    narr "Seeing her distressed from the call, I offered my seat and a glass of water."
    narr "My fears worsened. I even considered alerting the student body to prevent a future case.{w} However, with no knowledge of Inoue’s condition, I refused to take action.{w} It was rash."
    narr "Mrs. Genkai kept a level head throughout the whole affair, agreeing to keep it among the three of us.{w} No other faculty member was in proximity."

    scene bg school hallway with dissolve
    nvl clear
    narr "I left the faculty room, requesting to keep in touch with Ms. Harada for any updates.{w} I last saw her feebly picking up her smart phone and dialing another number, most likely the Kirisakis."
    show sayo worriedtalkclosed at Three2 with Dissolve(0.2)
    narr "I felt sorry but I have to zip my mouth."
    narr "What interest is there, I suppose?{w} Announcing it publicly would cause discord and panic."
    hide sayo with Dissolve(0.2)
    scene bg classroom2 with dissolve
    narr "I returned to IV-E, avoiding to speak to anyone.{w} I needed to think, and take my mind off it."

    nvl clear
    narr "Ten minutes before the fifth period, a murmur emanated from outside.{w} Normally, a few of my classmates would check it out only to dismiss it immediately.{w} I paid it no attention."
    play sound sfx_ambulance1 loop
    narr "This time, more and more people went out.{w} I glanced at the window, noticing a crowd forming from even the other classes.{w} I recognized that sound."
    play music bg_undaunted loop fadein 1.0
    narr "An ambulance!"
    scene bg school outside with dissolve
    play sound sfx_ambulance2 loop
    narr "I joined the crowd and saw the source personally.{w} Sprinting towards it, I saw the patient being taken away.{w} Mrs. Genkai stood at the walkway, wiping her sweat. She looked pale."

    nvl clear
    window hide

    show sayo normaltalk at Three3 with Dissolve(0.2)
    sr5 "Excuse me, madame. What’s the commotion?"
    t_gen "I had to assist a fellow faculty down after an attack.{w} {i}*sigh* Could this day go any worse? She’s had enough already.{i}"
    show sayo worriedtalk at Three3 with Dissolve(0.2)
    sr5 "She? You mean –"
    t_gen "Correct.{w} The patient is Ishii-san.{w} She called Kirisaki’s residence immediately after you left.{w} He was the other student absent from her class, if I recall."

    show sayo seriousnormal at Three3 with Dissolve(0.2)
    stop sound
    stop music fadeout 1.0
    "Oh no. Tell me the worst."

    t_gen "Before she blacked out, I heard the following over the line, though it wasn’t in loudspeaker,"
    t_gen "\"{i}Don’t tell me my son is missing!{i}\""
    hide sayo with Dissolve(0.2)
    scene black with fade

    "JUNE 18, 2013 - 1650H"
    window show
    nvl clear
    narr "{i}Attention to all students.{w} Please remain at your homerooms for the next half hour. Your advisers have an urgent matter to discuss with you.{w} Class IV-A, your co-adviser shall meet you in behalf of Ms. Harada.{w} Thank you for your cooperation.{/i}"
    narr "The impromptu announcement stirred an air of concern among the students.{w} While some of the underclassmen were already dismissed an hour ago, the rest were forbidden from leaving."
    narr "They all saw it{w} – the image of Ms. Harada out cold on the gurney.{w} A few sulked, with some others discussing.{w} Exactly what happened? Why are they being detained?"

    nvl clear
    window hide

    scene bg classroom1 with fade
    show sumiko serious at RS with Dissolve(0.2)
    "Mrs. Ren Kanako entered IV-C, settling down immediately.{w} Sumiko took second-charge in handling the class."

    t_kan "Hope you’re all well.{w} Let’s see... One, two...{w} 42 heads. Good!"
    t_kan "You must have witnessed the scene at 12:30 this afternoon and must be concerned for Ms. Harada’s condition.{w} She’s presently stable, if a little somber."

    "Audible sighs of relief were heard, yet they were not satisfied.{w} The teacher proceeded with the announcement, almost cut short by an uproar in the neighboring class."

    play music bg_hazydisorientation loop
    t_kan "You heard IV-B –{w} this is no pleasant news.{w} Two of your batch mates from IV-A, Inoue Shinozaki and Kyou Kirisaki...{w} they disappeared this morning."

    window show
    nvl clear
    narr "These words induced fear to the students."
    show yoshiro serious2 at LS with Dissolve(0.2)
    narr "Someone dared to ask a question{w} but Sumiko shot him down, asking him to wait."
    hide yoshiro with Dissolve(0.2)
    narr "She grew stern discussing the details of each disappearance,{w} laying them down fact by fact, disallowing herself to speculate.{w} The cases have been reported to the authorities and an investigation shall commence soon."
    narr "Until then, the students are urged to head straight home as soon as classes end or when their cleaning duties are over.{w} When it was all done, she entertained Yoshiro, who attempted to ask earlier."

    nvl clear
    window hide

    show yoshiro serious2 at LS with Dissolve(0.2)
    ys6 "Pardon the interruption earlier, madame.{w} This is more of a thought than a question in itself, but{w} is kidnap possible?"
    t_kan "That’s the likely case.{w} In fact, we advised both families not to respond to any ransom until the suspects are identified."

    show sumiko serioustalk at RS with Dissolve(0.2)
    "Sumiko was no longer able to contain the crowd’s restlessness.{w} Mrs. Kanako soothed her students, unwilling to worsen their emotions."
    hide yoshiro with Dissolve(0.2)
    show sumiko serious at RS with Dissolve(0.2)
    "Minutes passed with seemingly endless queries about the incident –{w} where and when they were last seen and a few personal questions.{w} Then, Miyu stepped forward to speak."

    show miyu bored at Eight3 with Dissolve(0.2)
    mh8 "Madame, we may just have enough information mostly from you."
    show miyu focusedpose at Eight3 with Dissolve(0.2)
    mh8 "From what I can surmise, while they may have been abducted between five to six in the morning,{w} I believe the two incidences are {i}not{/i} related in any way."
    "\"WHAT?!\" {b}*GASP*{/b} \"What is he talking about?\""
    t_kan "Please clarify. I did not catch the last bit."
    show miyu naughty focuspose at Eight3 with Dissolve(0.2)
    mh8 "What I meant is,{w} despite the similarity in time of Shinozaki and Kirisaki’s disappearance,{w} I doubt the two bumped into each other this morning beforehand."
    show miyu naughty focuspose2 at Eight3 with Dissolve(0.2)
    mh8 "How do I know?{w} Simple. I arrive here every 5:45,{w} and most of the time, I see Kirisaki sitting out at the bench – this morning an exception.{w} Shinozaki arrives at around six, latest delay at fifteen minutes."
    show akira serious at Eight1 with Dissolve(0.2)
    ai2 "He isn’t lying, madame.{w} I’ve only gotten here twice without Miyu already inside.{w} I support his statement as well, but I honestly don’t see how the two didn’t meet this morning."
    hide akira with Dissolve(0.2)
    show hikaru angry at Eight1 with Dissolve(0.2)
    hy10 "Excuse me, madame. If I may,{w} I was temporarily given the second spare key as I needed to arrive at 5:30 for the dance activity preparations.{w} I never saw anyone else inside, up until Akira arrived."
    show hikaru serious at Eight1 with Dissolve(0.2)
    hy10 "Meaning, I never saw Miyu."
    show miyu naughty smirkpose at Eight3 with Dissolve(0.2)
    mh8 "You didn't.{w} I was in the bathroom at the time.{w} When you've got to go, you have to. {i}*giggle*{/i}"
    show hikaru focusright at Eight1 with Dissolve(0.5)
    show hikaru focusleft at Eight1 with Dissolve(0.5)
    hy10 "..."
    hide hikaru with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)

    window show
    nvl clear
    narr "Regardless, Inoue’s case is a dead end.{w} It hinges on everyone thinking she is still unwell.{w} Then again, they only have Mrs. Shinozaki’s word for it."
    narr "As for Kyou, however, his is a legitimate case.{w} Consequently, Inoue's case becomes one."
    
    nvl clear
    narr "Rather than intensify the situation, nobody chose to speak further.{w} Instead, Mrs. Kanako arranged for a few changes in their activities.{w} She informed them of the stricter curfew time,{w} from 6:30 to 6:00."
    stop music
    narr "After forty minutes, the meeting adjourned.{w} She ensured that the students emptied the classroom, leaving no one inside save for the day’s cleaners.{w} When they were nearly done, she gave her final instructions to Sumiko."

    nvl clear
    window hide

    show sumiko surprised at LS with Dissolve(0.2)
    t_kan "Sumiko, see to it that none of your classmates go astray.{w} I plead you, we shun another case!{w} Please relay my words to the rest."
    t_kan "I’ll leave the rest to you."
    show sumiko serioustalk at LS with Dissolve(0.2)
    st3 "Understood.{w} Keep safe, madame and have a pleasant evening."
    hide sumiko with Dissolve(0.2)
    play sound sfx_doorknob

    scene bg msci evening with fade
    "As the teacher faded from his view, so did the sun.{w} It bore witness to the day’s events – times of order and confusion{w} – similar events repeating themselves too often they can be glossed over safely."
    "And curiosity?{w} What interest is there, indeed?{w} Hence, no further mention is necessary."
    return

label ch01_09_labkyou1:
    scene black with fade
    play sound sfx_wind loop
    "JUNE 18, 2013 - Time Unknown"
    scene bg freedompark night with fade
    show kyou calmleft at RS with Dissolve(0.2)
    window show
    nvl clear
    narr "I’ve never arrived this early at the city square.{w} The moon and incandescent lamps as light sources, my brother and I walked across to the wet market.{w} He needed report materials; I went for a different reason."
    narr "I brought the class’s materials in advance yesterday,{w} but the Creatives Committee ran short late at night, our progress barely satisfactory.{w} As the earliest to arrive, I volunteered myself."
    hide kyou with Dissolve(0.2)
    scene bg wetmarket night with dissolve
    show kyou smile at RS with Dissolve(0.2)
    narr "Our head told me that the market stalls would be open as early as five.{w} My brother insisted on coming along; I accepted, since we always went to school together."
    show kyou surprisedleft2 at RS with Dissolve(0.2)
    narr "Along the way, we ran into a vagrant sniffing from a plastic bag.{w} With God watching us, no harm may befall us."
    hide kyou with Dissolve(0.2)
    scene bg freedompark night with dissolve
    narr "We exited the market, the sun peering out a bit.{w} The square slightly increased its population, mostly students and employees."
    
    nvl clear
    scene bg school gate morning with dissolve
    show kyou happy at LS with Dissolve(0.2)
    narr "We wished Onifuchi-san, the gate guard, a blessed day as usual.{w} The same went for the other guard at the front desk."
    scene bg msci night with dissolve
    show kyou smirk at Three2 with Dissolve(0.2)
    narr "We parted ways, giving each other a fist bump, once we reached the staircase near IV-A.{w} The Senior-Year classrooms were devoid of life{w} – not even Akira, Miyu, Sayo, nor any of my classmates are present."
    show kyou proud at RS with Dissolve(0.2)
    narr "I inserted the key and unlocked the classroom door."
    hide kyou with Dissolve(0.2)
    scene bg classroom2 morning with dissolve
    narr "The creepy vibe left me once the lights turned on.{w} I neatly arranged the materials – a ball of nylon thread, assorted colored papers, fans, among others."
    scene bg classroom1 morning with dissolve
    narr "The sky brightened a little,{w} and I settled myself down.{w} Once more, I ran through our list and messaged the committee.{w} With a beep of confirmation, I let myself doze off."

    stop sound
    scene black with fade
    nvl clear
    window hide

    play music sfx_static2 loop
    unk "{b}*COUGH*{/b}"

    window show
    nvl clear
    narr "It bothered me since weekend.{w} Just go away... the medicine should off you soon enough.{w} The placebo should quicken the process."
    narr "Now that’s much better.{w} Praise the Lord."
    narr "The air is giving me the chills.{w} The radio anchor reported a 24-degree morning, not a ten! What time is it now?"

    nvl clear
    play sound sfx_chain
    play sound sfx_chain
    narr "{i}*clatter* *clatter*{/i}"

    nvl clear
    narr "Only muddled sounds registered in my ears.{w} I feel detached from my body, much like in a lucid dream.{w} It’s another experience of mine, yet it feels{w} quite peculiar, more than ever."
    narr "I only felt my head, pounding from a lack of sleep.{w} I could’ve brought the pillow we made in Home Economics class before."
    narr "My eyes opened, waiting for the image to focus itself."
    narr "Hang on...{w} the ceiling’s farther than before.{w} Surely, I haven’t –"

    stop music
    nvl clear
    play sound sfx_chain
    play sound sfx_chain
    play sound sfx_chain
    narr "{i}*clatter* *clatter* {b}*CLATTER*{/b}{/i}"

    window hide
    scene bg emptycell with fade
    window show
    nvl clear
    narr "Wait...{w} This isn’t our homeroom!{w} Where am I?!"
    play sound sfx_chain
    play sound sfx_chain
    narr "{i}{b}*CLATTER* *CLATTER*{/b}{/i}"
    narr "A maniac – a demon{w} – is holding me hostage!"
    narr "I rested myself for an hour, trying to endure the painful bout in my head.{w} It feels worse than being a zombie."

    window hide
    scene bg emptycell2 with dissolve
    window show
    nvl clear
    narr "Floor to ceiling, I studied the room’s layout.{w} The room I’m in is at best,{w} depressing,{w} barely any furniture in sight, save for the bed and desk at my side."
    scene bg emptycell with dissolve
    narr "I cannot go any farther{w} – my feet are shackled tightly at the two foot-side bedposts.{w} The other option, therefore,{w} is to search. Plenty points of interest in sight."
    narr "There are three drawers –{w} the middle containing a few markers and a rug, the top with a spare light bulb, and the bottom empty."
    narr "Other points of interest – the lampshade’s underside and the space beneath the bed,{w} nothing."
    narr "I scrutinized the pillow last, feeling it all over.{w} At the underside, I felt a thin solid rectangle with a bump converging to the middle.{w} My eyes flashed when I found the object."

    window hide
    scene bg envelopefour with fade
    window show
    nvl clear
    narr "An envelope!"
    narr "The devil must’ve inserted this before I was detained.{w} A small key accompanied the letter, which fit the chain's lock perfectly.{w} It gave me a bit of freedom,{w} but there is still that barred door with a weird device beside it."
    narr "The letter piqued my curiosity,{w} so I sat down and examined its contents.{w} Addressed at the back of the envelope is my full name – no sender or a postage stamp visible."
    scene bg letter a with dissolve
    narr "The parchment looks new but creased, courtesy of myself.{w} I didn’t recognize the handwriting, but{w} it does strike some familiarity."
    narr "What follows is a short message from whom I dub \"Mr. X.\""

    nvl clear
    narr "{i}You’ve awaken,{w} Kyou Kirisaki.{/i}"
    narr "{i}No doubt, you lived the past few days on repeat {w}– only to end, sadly, in pain.{w} If not, what is the term again?{w} Apnea – yes, I figured you would cease breathing at some point in limbo.{/i}"
    narr "{i}It’s a meager, nevertheless.{w} I’ve no desire to waste your time, so I present my terms, \"rules\" you may refer them.{/i}"

    nvl clear
    narr "{i}First,{w} you seek the truth for yourself.{w} I know well enough that you are a man of God and an enthusiast of Science;{w} thus, you can piece the facts scattered around here. Empty your mind...{w} \"Naivety won’t get you too far, but I’m not saying you are.\"{/i}"
    narr "{i}Second,{w} know that you aren’t alone in this place.{w} It could be me, another soul, or your God, if you prefer.{w} The catch is, you come out of here alone – no companions.{w} Leave everything behind and think for yourself...{w} think as if nobody exists.{w} I don’t either.{/i}"
    narr "{i}The third applies if{w} I don’t find you as a cadaver the next morning.{w} You’ll tell me everything{w} – how you perceive rationality – they all intrigue me.{w} What is a \"catalyst\" in your sense?{w} Whatever you hold, I'm certainly expecting more than that.{/i}"

    nvl clear
    narr "{i}Otherwise,{w} you keep your word.{w} I’ll tell you everything in return{w} – about me and why I involved you in this.{w} You'd best hasten your steps{w} – your dear brother is worked up, with lack of a better word.{w} In fact, you share a mutual feeling.{/i}"
    narr "{i}I must warn you,{w} no refusals.{w} You MUST play by the rules.{w} The clock is already ahead of you – once it stops, you can never start it again.{w} A fair bargain if you consider my offer carefully.{/i}"
    narr "{i}Welcome to purgatory.{w} I sincerely hope you find your stay rather... endearing.{w} I shall see you soon.{/i}"
    scene bg letter b with dissolve
    narr "{i}Signed,\nL.C.{/i}"

    scene bg emptycell2 with dissolve
    nvl clear
    narr "Malice – the letter is peppered with it. Mr. X,{w} or rather, L.C., makes no effort to mask it.{w} He wants my skin, no doubt.{w} It just bugs me why he opted for his theatrics instead of doing away with me immediately."
    narr "Speaking of, where is my watch{w} and my phone?!{w} Had he disposed of them?"
    narr "No time to waste! I’ve no choice but to play his game if I wish to live.{w} I’ll keep this letter for reference."

    nvl clear
    narr "What truth is he talking about?{w} He knows more than I am – far too much to be a stalker.{w} Set aside the second reading for later. Getting out is top priority{w} ...if only I can crack this device."
    narr "An electronic device, Dvorak-styled keyboard and LCD screen, barring my escape.{w} The magnanimous fellow fitted a similarly-sized transparent board which functions as its cover."
    narr "There are instructions above the device, printed this time."
    narr "{i}You could just brute-force the passcode, but I’ve removed the bots from your vicinity should it occur to you.{w} Might as well retain the cover where it’s supposed to be than vainly trying to remove it.{/i}"

    nvl clear
    narr "Nonsense!{w} There must be an inscription in this room or a keyword in this letter.{w} An expected reaction from me, nonetheless. Well-played!{w} I typed several words from the letter, hoping they would come through."
    narr "The bars did not move an inch.{w} {i}Access Denied{/i} – all of them!{w} At this point, I’m tempted to follow his ridiculous advice.{w} Sadly, I don’t even know the length of the passcode.{w} Let’s try something else, shall we?"
    scene bg emptycell with dissolve
    narr "Specimen A:{w} the items in the middle drawer.{w} Probably useful for something else that I have no idea at present."
    narr "Specimen B:{w} the spare bulb in the top drawer.{w} If I replace the lamp’s bulb, what would be different?{w} It looks fine to me, evidently fresh. I only glossed over the former, honestly."
    narr "The bulb caught my attention. The glass is dark in color.{w} So, this must be a UV light bulb.{w} I switched the one currently installed with it."
    narr "My eyes confirmed my thoughts."

    nvl clear
    narr "With this, there are now stray marks visible on the letter,{w} just random scribbles.{w} Flipping it around, a message eventually turned up on the paper’s middle section."
    narr "{i}Double lens. EASY, does it?{/i}"
    scene bg emptycell with dissolve
    narr "It’s the word – I am certain of it.{w} Returning to the device, I typed in the word.{w} My heart throbbed wildly from the excitement, and I'm finally getting out of this wretched room."

    nvl clear
    narr "{i}Access Denied{/i}"
    narr "Two words alone made my heart sank and my brain nearly collapse in frustration.{w} Even after a double take, it caused no progress.{w} I had two choices:{w} to wallow in self-pity, or to sort this out more carefully."
    narr "I recall saying that quote he mentioned.{w} It was during the brief discussion with Shinozaki – after her distressful phone conversation with Sayo.{w} There’s a variation of the quote itself,{w} but I don’t recall additional instances where I’ve uttered it."
    narr "This is too easy, the culprit incriminating himself by this fact?{w} No. His curiosity about a {i}catalyst{/i} – Suzumoto, in point – muddles it. I believe this stems from the discussion the nine of us had, excluding Miyu. Hiroshi skipped a few details when he retold everything."

    nvl clear
    narr "I prayed to God, losing myself in meditation.{w} The information I gathered swum around my mind.{w} The hidden message, letter, items in the drawer, and the device itself."
    narr "It came to me...{w} it just!"
    narr "Taking a blue and red marker with me, I shut the lid and surveyed the device once more.{w} There’s something I overlooked, one I merely suspected at first glance."
    narr "Of course!{w} Never have I seen a Dvorak keyboard in my lifetime save for those as textbook figures.{w} It isn’t commonly found in schools, contrary to the QWERTY layout."
    narr "I reconstructed the layout, ensuring no mistakes.{w} It took another failure before I consulted myself once more.{w} Another word popped out of my mind after the deliberation..."

    nvl clear
    narr "{b}*CLANK* *HUM*{/b}"
    window hide
    scene bg darkhallway with fade
    window show
    narr "The bars gave way to me, allowing the metal door to open freely.{w} From beyond is an empty corridor, well-lit unlike this cell.{w} Two doors are visible – one at the other end, the second just near the first at the left side."
    narr "Sneaky devil – I should be grateful for his invocation.{w} He might be clever, but as long as God is with me, nothing is impossible.{w} That’s the spirit.{w} As Dostoyevsky once said through Rodion Raskolnikov, \"May the Devil take the fool.\""
    narr "He’ll not lay a finger upon me{w} – never!"
    scene black
    narr "{b}*BOOM* *CRACKLE*{/b} {i}*hiss*{/i}"

    nvl clear
    window hide
    return

label ch01_10_labinoue1:
    scene black with fade
    "Date Unknown - Time Unknown"
    window show
    nvl clear
    narr "I feel worse than a caged canary."
    scene bg emptycell with fade
    narr "There’s an unusual hospitality in that voice, but it still creeps me out.{w} What am I even doing here?{w} One minute I’m walking across the city square, then I wake up here the next."
    narr "The cell is minimalistic: bed, cabinet, and a CD player.{w} The last is of a similar brand to my own, but this isn’t mine. I’m sure of it.{w} In distress, I can only brush the piano keys with my fingers.{w} Damn me for forgetting my piano lessons!"
    narr "Instead of a working solution, the disembodied voice occupied my mind."

    nvl clear
    window hide

    unk "Dearest apologies, Inoue Shinozaki."
    unk "Let me assure that this is the first time I’ve spoken to you.{w} You might say we met, yet I doubt that.{w} Nevertheless, refer to me as{w} L.C.{w} Set the matter of my identity aside for now.{w} I’d like to momentarily clear up some affairs,{w} {i}personal{/i} things."
    unk "I recognize your perseverance to seek the truth, despite the pressure it causes on you.{w} I admire that, quite frankly, so I’ll give you a head start.{w} Think of it as a gift.{w} I’m a magnanimous person, I am."
    unk "Know that another soul dwells this place. I am not here somewhere{w} – yet.{w} I guarantee one other person, if that’s enough to quell your curiosity.{w} Pray you do not cross paths{w} – you are set to kill each other.{w} A heartbeat less is enough, if you catch my drift."
    unk "If you refuse my orders,{w} then {i}I’ll{/i} personally come to end you both.{w} I’ll give you just enough time to decide and escape. I ask of you nothing else."
    unk "Consider this a closed deal between us.{w} Keep your knowledge to yourself."
    unk "Thus, I welcome you as a guest,{w} and a guest you’ll {i}no longer be{/i}.{w} Godspeed, Shinozaki, and retain your resolve.{w} The facility does not take such matters lightly."

    scene bg emptycell2 with dissolve
    window show
    nvl clear
    narr "I didn’t hear the recording cut itself; I let it run just to be safe.{w} The piano keyboard has 36 keys, starting with C and ending with B.{w} Pressing each once, they worked just fine."
    narr "A little tune broke through the silence."
    narr "It’s probably a nursery rhyme, judging from the music box-like arrangement.{w} The music soothed my nerves.{w} I’ve no clue of the next step, so I lied down.{w} I awaited an answer,{w} or better,{w} death."

    nvl clear
    narr "This is the extent of it all, eh?{w} Secluded in a world not my own, there exists an odd feeling of serenity.{w} The ceiling animated itself,{w} projecting my subconscious thoughts.{w} I can see myself perfectly without a mirror."
    narr "This is the face I never showed anyone,{w} not even Sayo.{w} I gave a ninety-nine at best, a façade Kirisaki almost saw through.{w} L.C. is a special cookie, making him or her an exception."
    narr "Images flashed across the ceiling.{w} Memories of the past days manifested on those."
    scene black with fade
    narr "{i}Ten{/i} victims from Sacred Heart Academy...{w} and one impacting detail still etched into my mind.{w} Perhaps it was thanks to Sayo that I found the tracks to the truth I’m seeking."
    narr "What business do I have with them?{w} Ikari is involved somehow{w} in the most minimal way possible.{w} I know her personally – she and big brother were classmates.{w} I asked him about it last Sunday."
    scene bg livingroom with fade
    show inoue casual troubled at Three2 with Dissolve(0.2)
    narr "There’s nothing new initially, yet I convinced him to disclose further."

    nvl clear
    window hide

    tomonori "This is just a speculation, but Ikari has been off her head for some time after Christmas break."
    show inoue casual serioustalk2 at Three2 with Dissolve(0.2)
    is4 "You’ve heard of the incident in the storage room that February, didn’t you?{w} The one where –"
    tomonori "She personally told me;{w} I’m among the few, in fact.{w} I thought she was cuckoo, saying that our batchmates’ illnesses were abnormal and that she was next{w} – It was wild!{w} There’s just no truth beyond the books!"
    show inoue casual troubledtalk at Three2 with Dissolve(0.2)
    is4 "Roll along the next four months..."
    tomonori "...To the following March, this year.{w} Seeing her on the newsprint, I wanted to retract my judgement.{w} But I never said it to her face, so why would I apologize?"
    show inoue casual troubled at Three2 with Dissolve(0.2)
    is4 "..."
    tomonori "Satisfied? Hope so.{w} If you please, do {i}not{/i} transpire our conversation with anyone else.{w} While she may be a familiar face to the public, the details connecting her and the recent tragedy are not."
    show inoue casual worriedpose at Three2 with Dissolve(0.2)
    is4 "But I heard it first from Sayo. Does that count?"
    tomonori "She knows her limits. I can say Suzumoto’s still in the safe zone.{w} Just heed my advice."

    scene black with fade
    "I kept my promise, didn’t I?{w} So why am I convicted like a criminal?{w} This world has double standards. It makes me laugh."

    window show
    nvl clear
    narr "{i}~Va chez la voisine,\n~Je crois qu’elle y est,\n~Car dans sa cuisine\n~On bat le briquet.{/i}"
    narr "The brief buzz afterwards made me jump.{w} I slapped myself awake from my temporal daze.{w} It degraded to silence once more, before L.C. spoke again."

    nvl clear
    window hide

    scene bg emptycell with fade
    unk "An elementary rhyme, common amongst the French.{w} Tonight, the moon takes the front seat, awaiting your performance.{w} Kindly reproduce it – just this part.{w} Be swift or be driven mad from the endless repetition."

    window show
    nvl clear
    narr "The same verse of {i}Au Clair De La Lune{/i} played after the transmission.{w} This time, I listened more closely."
    narr "Elementary enough, I should say,{w} so the notes must be distinct."
    narr "This is a version different from the one I first played on the piano.{w} If I think about it, it kind of fits.{w} The amount of facts he presented creeps me out."

    scene bg emptycell2 with dissolve
    nvl clear
    narr "From the drawer, I retrieved some writing materials.{w} Then, I drew a staff and marked the notes where I thought they should be.{w} Three drawings to check for any discrepancies."
    narr "I returned to the piano and marked the keys.{w} My strokes matched the tempo of the song as a fail-safe.{w} Most of the time, the notes match save for one or two.{w} They're only an estimation."
    narr "Nothing happened after three attempts, so I re-checked my paper."
    narr "This is jarring{w} – it appears that I’ve distorted some notes by mistake.{w} For instance, the G-flat in {i}feu{/i},{w} I transcribed it as a C.{w} The reverse happened in another note.{w} Oddly enough, I happened to get different results with the last note, C."
    narr "Before the next attempt, I performed some statistical analysis to help my case.{w} Fourth time and counting."

    nvl clear
    narr "{b}*CLANK* *HUM*{/b}"

    scene bg darkhallway with dissolve
    nvl clear
    narr "The mechanism drowned my breath.{w} As my heart raced in anticipation, I waited as the metal bars reveal the opening.{w} My way out – a step closer, it seems."
    narr "My ear tingled, and a lava-like sensation rose up my neck.{w} My fever is returning, it seems,{w} and I haven’t any medicine with me.{w} In fact, my personal items aren’t, too{w} – not even my watch!"
    narr "How much time has passed, no one can tell."
    narr "There seems to be no alternative to that door.{w} I left the writing materials in the drawer and turned to leave this hellhole."

    nvl clear
    window hide

    scene black
    "{i}Impressive. I would have expected more.{\i}"
    is4 "{b}!{/b}"
    "{i}You have questions – I am aware of that.{w} Yes, I know you well enough, Shinozaki.{w} The choice of music is plain, if you’d realized.{w} The question now would be, \"is it mutual from your side?\"{w} You answer that for me.{/i}"

    "A sharp pain entered my temples."
    "Indeed, his voice constantly switched tones like the rhyme earlier.{w} I didn’t catch what he said for a few sentences,{w} but I eventually recovered."

    "{i}I’ll keep you alive for long enough – it interests me how far you’re willing to go.{/i}"
    "{i}You keep your wits about you, Shinozaki. I love an open prey.{w} As a bonus tip before I leave,{w} do mind your surroundings, will you?{w} You never want to leave a space unattended in this ever-changing world.{/i}"
    unk "Don't breathe."
    is4 "{b}*GASP*{/b} Damn it!"

    "I saw something move from my peripheral, and my eyes followed it quickly.{w} Left,{w} right,{w} everywhere I look, I find nothing.{w} That mustn’t be a trick! I know it!"

    "{i}Ku...kuku...kukukuhahahaha...{w} Oh, boy. This is gonna be a long night.{w} Ahahahahahaha!{w} {b}GAHAHAHAHAHAHAHAHA!!!!!!!{/b}{/i}"
    is4 "SHUT UUUUUUPPP!!!!!"

    "{b}*SLAM*{/b} {i}*hiss*{/i}"

    play sound sfx_breathing
    is4 "Haa... Haa... Haa...{w} {i}*GULP*{/i} Kuh..."

    "{b}*THUD*{/b}"

    scene bg emptycell with fade
    window show
    nvl clear
    narr "I never want to hear that demonic voice again{w} – especially that mocking laugh!{w} The wild throbbing filled my ears,{w} my face drained of blood.{w} My posture is that of a doll,{w} left by its owner on the bed after playtime."
    narr "If I were to look through a mirror,{w} perhaps I’d see a monster."
    narr "But there’s no need{w} – I’m not the only one that changed.{w} Ticking sounds replaced the pulsations.{w} It better be what I think of it – a ninety-nine in my books."

    nvl clear
    narr "I watched the door.{w} At any minute, a figure might emerge from the dark corridor.{w} He sees me, vulnerable and weak,{w} and does the most horrifying thing imaginable...{w} the end."
    narr "Nobody came, contrary to my expectation."
    narr "With what little strength remained, I forced myself up.{w} I held it in, pacing once per second as I made my way to the door."
    scene bg darkhallway with dissolve
    narr "The sides supported my weight.{w} For another minute, I stared into the void.{w} I couldn’t make out a figure, but there are two doors in sight{w} – one across from here, and the second to my left."
    narr "But which one?"

    nvl clear
    window hide
    return

label ch01_11_labkyou2:
    scene black with fade
    "Date Unknown - Time Unknown"
    scene bg darkhallway with fade
    window show
    nvl clear
    narr "I made the cell as my lantern, walking at the sides of the corridor.{w} Eventually, a door, similar to the previous one, came into contact.{w} It offered little resistance when it opened."
    narr "The space felt more enclosed.{w} My hand immediately traversed the wall for a switch.{w} There was nothing to be found.{w} Hesitantly, I stomached my way into the void."
    scene black with fade
    narr "I shut the door in the off-chance that a stalker is behind me.{w} It wouldn’t make a difference if I close my eyes now, would it?{w} The pressure heightened,{w} no sound permitted itself to emanate from me."

    nvl clear
    narr "The next minute felt like a dream,{w} a trance.{w} The walls revealed themselves,{w} distanced farther than where I thought they should be.{w} Endless is the ceiling, so is the space beneath.{w} Some things were talking,{w} defying the silence."
    narr "Were they the walls?{w} Couldn’t be.{w} If it were from an angel, or God Himself,{w} my salvation is guaranteed.{w} If it were from the Devil, then all is fair{w} – I’m damned, maybe from the beginning."
    narr "I wanted to go up, but gravity is in effect.{w} It sure is a long way down; none can tell what’s at the bottom.{w} Maybe I’ll be stuck in a wormhole if I risk it{w} – a donut-shaped passageway, if I add!{w} But there is always the door."

    nvl clear
    window hide

    play sound sfx_doorknob
    play sound sfx_doorknob
    "{i}*RATTLE* *RATTLE*{/i}"
    "If I could just{w} – tsk. That’s one pesky doorknob.{w} It wouldn’t even let my hand grip it."
    "Breathe, Kyou.{w} An insignificant object will not defeat you."

    kk9 "Ugh! Come on!"

    play sound sfx_doorknob
    "{i}*RATTLE*{/i}"

    kk9 "Phew... You’re putting up quite a fight!{w} Now let me out, if you please?"

    "Pull, pull, pull..."
    "It won’t budge, and I’m already using all my strength!{w} There must be a superglue applied to this knob.{w} It doesn’t smell like it – I can’t even smell anything!"
    "{b}*BUGH* *BUGH* *SLAM*{/b}"

    kk9 "I know you’re there! Open up!"

    play sound sfx_giggle
    "{i}*snicker* Hihihihihihi... Nyihihihihihihihi!{/i}"

    play music bg_hazydisorientation loop fadein 1.0
    window show
    nvl clear
    narr "The platform shook.{w} It’s as if the force on the door caused a quake,{w} or was it that...{w} that...{w} whatever that is.{w} My feet numbed from the tremor; I can hardly get up.{w} I rolled over."
    window hide
    scene bg abyss with dissolve
    window show
    narr "From beyond, the endless void defined the boundary.{w} There’s no alternative. I may be going to Hell if I jump{w} – yet in this secluded world, I {i}am{/i} in Hell.{w} But I’m very much alive... beyond reasonable doubt."
    narr "The shaking stopped{w} – a snap underneath."
    narr "A black line creeped from the door, branching out towards me.{w} I smiled, accepting what’s to come.{w} And the platform felt more unstable, matching that of my own resolve."
    narr "I closed my eyes. It makes no difference now, would it?{w} If only I could open it to welcome light."

    nvl clear
    window hide

    kk9 "Father, into Your hands I commend my spirit..."

    window show
    nvl clear
    narr "{b}*SNAP*{/b}"
    narr "I felt no fear throughout, as I believed a cushion at the bottom would come save me.{w} If not, then it’s alright.{w} The moment I fell, the darkness had consumed my entryway.{w} It’s chasing after me, vying against the light to get me in its clutches."
    narr "More than darkness, sounds of unrest enveloped me.{w} A deep echo emanated from the chasm,{w} which grew louder as time passed by.{w} Eventually, it washed out all other sounds,{w} culminating to a white noise."
    narr "It feels...{w} serene."

    stop music
    nvl clear
    play sound sfx_splatter
    play sound sfx_glass
    scene red
    narr "{b}*CRASH*{/b} {i}*SNAP*{/i} {b}*THUD*{/b}"

    nvl clear
    narr "Silence."
    narr "Nothing to be heard - not even the crickets, if it ever was nighttime.{w} The passage of time is unrecognized in this place, an eternal repose one would desire.{w} Darkness reigns in this domain, sheltering it from the chaos that pesters men on the outside."
    narr "And underneath lay a motionless body,{w} that of a human,{w} bloodless at hindsight.{w} It made no attempts to combat the weight over it.{w} Perhaps it was already crushed, its soul on its way to Heaven."
    narr "{i}......Ngh... K....{/i}"
    narr "It drew an image – the beginning of life itself, that of a pupa emerging from its cocoon.{w} But it was nowhere near that."

    nvl clear
    window hide

    kk9 "GAH! {b}*GASP*{/b} Haa... Haa... {i}*sigh*{/i}"

    window show
    nvl clear
    scene bg blood with fade
    narr "This is the aversion of death,{w} and that fall made me realize something.{w} Just how much damage can a mortal take?{w} Is he unbreakable as he is not led to believe?{w} My purpose is clear, and I hope to find a Grail at journey’s end."
    narr "I felt my head, warm near the crown.{w} The tips of my finger spouted a thick crimson liquid.{w} No signs of nausea, but I should cover the wound with a tourniquet – if there ever is one."
    narr "Debris scattered all over the floor.{w} Splinters of wood and broken bulbs littered the space where I lied down – a few inches away from a laceration."
    narr "Have I been that stupefied to even notice?"

    window hide
    scene bg storageroom with dissolve
    window show
    nvl clear
    narr "Then I remembered why I came here."
    narr "Next to my feet glinted a tiny object – a metal key.{w} It could fit the other door’s keyhole perfectly, unless there are some special instructions entailed with it."
    narr "I’m in a closet, looking ransacked from whatever episode I had earlier.{w} I spotted a flashlight on the top-most shelf.{w} As it went with my hand, a small paper came flying.{w} I caught it, running a quick scan of its contents."
    narr "The room plunged into darkness – a lucky save by the flashlight.{w} Illuminated, the letter gave off a short message."

    play sound sfx_pageturn
    nvl clear
    narr "{i}One does not speak, write, listen, and live forever.{w} He is part of a multitude of cycles, even which the universe is a major component.{w} Eventually, everything shall return the way they should be at the beginning of time.{/i}"
    narr "{i}For the love of God, would you kindly provide for me a pen to write with?{w} Fetch the torch for me too, please, as I may have forgotten it in a hurry.{w} Only then shall you pave your own path to the truth{w} – to me.{/i}"
    narr "{i}I shall be waiting,{w} stranger.{/i}"

    nvl clear
    narr "This is a joke.{w} He refers to my name one minute, regards me as a stranger the next.{w} Ah, well. I’ll be on my way. It’s not like he knows where I am right now.{w} No pens, though."
    scene bg darkhallway with dissolve
    narr "At this point, the torch became my source of light.{w} The cell door apparently shut itself.{w} Nevertheless, I focused on the other unexamined door.{w} The key I found is a perfect fit, but the rust inside the lock made some resistance."
    narr "{b}*CLICK*{/b}"
    narr "That mundane sound lifted me up. With a push, a blinding light seeped out of the opening.{w} I shielded my eyes while opening the door to its furthest limit."
    narr "My whole system stopped as the image registered into my mind."

    window hide
    scene bg parlor with dissolve
    window show
    nvl clear
    narr "I’m in a living quarters.{w} Just compare the bleakness of the cell I’ve been into – it’s absent here.{w} No word is sufficient to describe how peculiar to see its kind, especially in this place."
    narr "There are couches, ornaments, tables, to mention a few.{w} The center table sports a bonsai on top. Lovely as it is, yet unaesthetic at its position."
    
    play sound sfx_dooropen
    nvl clear
    narr "Only when I closed the door did its artistic features sink in.{w} Symmetry is present, down to the most minute detail.{w} Each side has a door at the center, save for the one on my left."
    narr "It has a coffee table, same height as the one on the center.{w} In front of the wooden book display is a book stand and a pair of unlit candles."
    window hide
    scene bg hdml1347 with dissolve
    window show
    narr "A painting adorned the wall above it.{w} Moving it is not an option; it’s too heavy and pinned tightly to the wall."
    narr "It shows a ship bearing {i}Q 1347{/i} on its hull, painted by R. Jeffs.{w} If it were a person instead of a ship, I’d say it was a shrine.{w} His eyes would meet the door across in that case. Doesn’t take a guess to figure out its state."

    window hide
    scene bg parlor with dissolve
    window show
    nvl clear
    narr "And should I mention{w} – the one thing that breaks the symmetry?{w} The device makes its return.{w} This time, however, it consists of only an LED screen with no apparent means of input."
    narr "Our host has resorted to a minimalistic approach.{w} Nothing is off the ordinary...{w} save for that bonsai.{w} Who would dare put one ON A CENTER TABLE?! Come on. The room has four corners!"
    narr "What about the other door?{w} Locked, as I expected, and hollow when I listened in."
    narr "I sat on a couch and contemplated my next move."

    nvl clear
    narr "In my possession are two separate letters.{w} I’m no expert, but I can tell the similarity between handwritings and syntaxes.{w} Believe me, these are written by L.C.,{w} yet it bugs me how he could’ve written the letters differently."
    narr "Maybe it was intended for the other person?{w} No, I should assume a thing wouldn’t exist without my eyes as witnesses."
    narr "...Now I know how Shinozaki feels."
    narr "I mustn’t forget I’m still in L.C.’s game, odds against me.{w} How easy it must have been for us to be in chokehold, a situation he favors above all."
    narr "Never mind the hospitable atmosphere{w} – I’m still in hostile territory.{w} I need to escape before I’m skinned alive or even worse."

    nvl clear
    narr "An idea popped out of my mind, suggesting my starting point."
    narr "I bent down, fishing my hand under the couch.{w} Aha! I feel a bump.{w} Upturning the couch, I revealed an ink bottle strapped by duct tape.{w} It is half-full, but it will do for now."
    narr "The same procedure was done for the other couches, albeit with nothing strapped underneath."
    narr "So, by the second letter, I need a{w} – that reminds me.{w} I lost the marker pens, and I refuse to go check that corridor. Time to find a quill or something.{w} But where do I write?"
    narr "The books, of course...{w} if vandals permit.{w} There are ten, all thick and worn out, all covering various subject matters.{w} I glossed over the titles."

    nvl clear
    narr "First two books cover Japanese culture, with the first an English-Japanese dictionary."
    narr "The third is a thick medical book, detailing major diseases and epidemics in mankind’s history."
    narr "Fourth book deals with quantum mechanics, higher level of science.{w} I’ll recommend Sumiko this – if I get out, that is."
    narr "The fifth deals with Greek Mythology and Legends."
    narr "That's a half of the total books;{w} the scope of knowledge L.C. possesses is astounding!{w} However, that does not soften my view of him."

    nvl clear
    narr "Sixth book is an Agatha Christie novel, {i}The Moving Finger{/i}.{w} I’ve read that, and the letters still send chills down my spine ever since."
    narr "The seventh and eighth are children’s literature, nursery rhyme collection and {i}Grimms’ Fairy Tales{/i}, respectively."
    narr "The last two are philosophical books, Wittgenstein and Kant.{w} Shame I couldn’t take these home. They’re worth hours of leisure."
    narr "Truly interesting.{w} One drawback..."

    nvl clear
    window hide

    kk9 "{b}{i}*groan*{/i}{/b} Thousands of pages?{w} Bah! I’d rather sit and die if that’s the method.{w} Excuse the antithesis, but let's begin."

    scene bg book with dissolve
    play sound sfx_pageturn
    window show
    nvl clear
    narr "My hand reached for the first book.{w} Upon opening the first page, a bookmark fell on the table.{w} It piqued my attention, particularly the small letterings near the ribbon:"
    narr "{i}Numbers – p. 16{/i}"
    play sound sfx_pageturn
    play sound sfx_pageturn
    narr "Then I turned the pages to the section indicated.{w} I briefly relived my first moments in Nihongo class.{w} Sensei was firm even at basic topics such as this; everybody was interested mostly on writing, the Kanas and even Kanji!"
    narr "Before my eyes lay the first steps, like in any language, to count.{w} My recollection continued until I noticed an oddity{w} – {i}go{/i} underlined in blue.{w} That shade is familiar..."
    narr "Regardless, I scanned the rest of the book, but there were no other markings.{w} Just that one.{w} Perhaps a clue?{w} I’ll have it as a quick reference."

    nvl clear
    narr "The latter nine books shared similar circumstances, bookmark and highlighted word someplace inside."
    narr "In the end, I collected the following:{w} nurse,{w} check,{w} table,{w} eye,{w} alone,{w} tree,{w} ankle,{w} don't,{w} reason.{w} Random, aren’t they?"
    narr "Ten blue words, a nonsensical message if taken whole.{w} I deemed it necessary to inspect the room once more, checking for oversights."

    nvl clear
    window hide

    scene bg hdml1347 with dissolve
    "A second view of the painting helped calmed my nerves as I peacefully gathered my thoughts."

    kk9 "So, a boat. A WWII warship, maybe?{w} A string of ten words...{w} What’s the connection?{w} {i}*sigh*{/i} God, help me."

    scene bg book with dissolve
    scene bg hdml1347 with dissolve
    scene bg book with dissolve
    "My attention altered between the painting and the open books.{w} Each travel puzzled my mind further,{w} but the subconscious is conjuring something bit by bit."
    "Using the blank pages at the books' ends, I played with the words, rearranging and reading them slowly.{w} Nonsensical messages appeared more often than those which are sensible, unsurprisingly."
    "{b}*CLAP*{/b}"

    scene bg parlor with dissolve
    kk9 "Eureka!{w} So that was the message after all. It reads..."
    kk9 "Straightforward enough, and works for me!"
    kk9 "You’re telling me to check that bonsai out?!{w} My pleasure. I’d even dispose of it should you desire."

    "A smile flashed on my lips, the same time as my feet began heading towards the plant.{w} Who would’ve thought? It’s in plain sight from the beginning!"
    "My hands reached for it without hesitation, exploring and digging the soil.{w} It’s all in our dut –"

    kk9 "Ow! That hurt..."

    "The tree or something... pricked my finger!{w} It felt like a needle.{w} A red spot appeared amongst the stains.{w} I rubbed my hands vigorously, despite the absence of any sign of infection."
    play sound sfx_glass
    "{b}*CRASH*{/b}"

    kk9 "That’ll teach you."

    "Something was off about that plant. The moment my eyes wandered about the room, it captured them.{w} Now it’s gone, no longer able to bother anyone."
    "This is{w} catharsis."
    "Fully tucked into the sofa, I gave myself some breathing space.{w} A minute or two passed before it caught my attention{w} – a scrap of paper from within the soil.{w} I cautiously dug it up and examined its contents."

    kk9 "1-6-6-5.{w} I have no idea what this means or where does this fit into.{w} Oh, what’s the message this time?"

    "And I stood, prepared to give the books a second reading."

    scene black
    "{b}*THUD*{/b}"
    "My feet lost balance, giving in to the peculiar sensation in my head.{w} The fever returned and my body slowly succumbed to it.{w} I shut my eyes and prayed.{w} This is worse than worst – I’m losing my hold."
    play sound sfx_doorknob
    play sound sfx_doorknob
    play sound sfx_doorknob
    "{i}*rattle* *rattle* *rattle*{/i}"

    kk9 "Who goes there?!"

    "Something{w} or someone{w} is trying to break in.{w} It could only be in my head, but..."
    play sound sfx_doorknob
    play sound sfx_doorknob
    "{b}{i}*RATTLE* *RATTLE*{/i}{/b}"

    kk9 "Begone, you spawn!{w} By the power of Christ, I shall not allow you to take me.{w} Stay there... go back to whence you came!"

    play sound sfx_heartbeat loop
    window show
    nvl clear
    narr "The shaking stopped."
    narr "My legs weakened as much as my breath shortened.{w} Patches of blue and white covered my vision, ever so slowly being invaded by darker shades of grey."
    narr "But it won’t stop.{w} The rattles continued, louder than ever{w} – to my left, to my right, even in front of me!{w} I can hear somebody laughing behind me,{w} not to my neck, no.{w} Farther than that."
    play sound sfx_giggle
    play sound sfx_giggle
    narr "{i}Ha... hahaha... hahahahahahaha... gyahahahahahahahaha... Woohahahahahaha!!!{/i}"
    narr "The warship; rather, its dead crewmen{w} are feasting upon my predicament.{w} Purgatory? Bah!"

    nvl clear
    window hide

    play sound sfx_splatter
    "{b}*SNAP*{/b}"

    scene red
    kk9 "Hngh!{w} AAAAAAAAAAAAAAAAAAHHHHHH!!!!!!"
    return

label ch01_12_labinoue2:
    scene black with fade
    "Date Unknown - Time Unknown"
    scene bg darkhallway with fade
    window show
    nvl clear
    narr "Don't breathe."
    narr "Though matterless, that scream was enough to paralyze my own body.{w} Around me is no light, save for the cell I was in earlier.{w} Yet even that is darkness, a prison I never wished to be in."
    narr "That other room?{w} It’s sealed tight.{w} I’m too weak to force it open, what with this pounding in my head.{w} I even searched for a crowbar or a makeshift lock pick – that’s what they do in the movies and books, right?"
    narr "Alas, I have nowhere to go."

    nvl clear
    narr "Beyond that door is a monster.{w} I count one... probably two of them inside and one of them is already being slaughtered.{w} Is our time already up? Why the hell isn’t a clock in sight?!"
    narr "How long have I been lying here? It feels like hours,{w} hours listening to the shuffling behind the door.{w} I loved the white noise more than that – why won’t you just break your way in already?"
    narr "Then I heard a familiar sound."
    narr "{b}*CLANK* *HUM*{/b}"

    nvl clear
    window hide

    "It came from a distance, some ten feet or so,{w} and it certainly wasn’t the door.{w} I’ve stuck an ear onto it{w} and from the other side, an acid voice spoke."

    unk "I've enough of you.{w} {i}*step* *step* *step*{/i} Another down the drain...{w} Goodbye, you spawn. I never liked your face, anyway."

    "Who the devil might that be?{w} It sparks my curiosity to know; at the same time, I don’t want to.{w} I heard a door shut{w} – another mechanism."
    play sound sfx_hiss
    "{i}*hissssssss*{/i}"

    is4 "{b}*GASP*{/b}!!!!!"

    "I didn’t expect that.{w} The moment that thing left the room, the door swung open by itself; it's kind of like magic.{w} However, I have to shake L.C.'s hands for orchestrating this well. He’d make a great puppet master."

    scene black with fade
    unk "{i}Point of no return... Point of no return...{/i}"

    play sound sfx_hiss
    "{i}*HISSSSSSS*{/i}"
    "I’m already waist-up into the new room{w} and the door is already closing by itself!"
    scene bg blood
    "{b}{i}*WHOOSH*{/i}{w} *SQUELCH* *SNAP*{/b}"

    is4 "Hgk!{w} .........Gulg!!!"

    scene bg blood2
    play sound sfx_splatter
    "{b}*SPLATTER*{/b}"

    window show
    nvl clear
    narr "My head felt like an orange, the air squeezed and the juice sucked out of it.{w} That juice came from my mouth, slowly forming a melted chocolate-like texture at the floor,{w} or was it strawberry mint?"
    narr "The cords to my legs have been severed – I feel nothing down there.{w} That part that makes me a woman is already gone... vanished.{w} But as long as I keep my head intact, I shall live,{w} right?"
    narr "Yup. Even my head alone would be alright."
    narr "Maybe not my mind, but are my eyes starting to betray me?"

    nvl clear
    window hide

    is4 "{b}*GASP*{/b}{w} WHAT THE FUCK?!"

    window show
    nvl clear
    narr "I withdrew my face in a flash."
    narr "I’m not sure...{w} but that isn’t my blood. It isn’t blood; not even a trace of iron!{w} It’s not just the face, but it snakes down my body as well."
    scene black with fade
    narr "My legs are intact, crumpled and barely touching the door.{w} There are red patches at the space where my waist has supposedly been crushed.{w} I don’t know how, but my eyes did the trick."
    narr "And if so..."

    nvl clear
    window hide

    is4 "My... God..."

    scene bg parlor with fade
    window show
    nvl clear
    narr "I’m in a living quarters{w} – how I’d wish I never went out of my cell."
    narr "Where shall I begin?{w} There’s the typical furniture set, but it suits a high-class owner.{w} Two coffee tables, with the right one having books on top and a painting overlooking it."
    narr "That’s not my concern, though.{w} At the couches’ center is a smashed coffee table, a fragment of a plant pot on one side.{w} That fragment has blood stains, small red patches trailing off to –"

    nvl clear
    window hide

    scene bg blood2
    is4 "Eeeeeeeeeekkk!!!!!!"

    window show
    nvl clear
    narr "I’ve found the rest of it."
    narr "Behind the disheveled couch is a corpse, head crushed with the plant.{w} And if it's fate wasn't enough, its neck is pierced by some twigs,{w} that of a bonsai."
    narr "It’s in a prone position, and I dare not to roll it over.{w} The fingers show signs of gangrene – apparent from the yellowish nails and blackened tips.{w} There’s a small cut on the left middle finger’s distal."
    narr "And the stench!{w} It’s as if a day has passed, but I’m certain he was killed a moment ago.{w} The torso’s a young male, a fellow student – his colors I assume are of ours, dark blue and white."
    narr "Eyes away from the corpse. Everywhere else is macabre at best.{w} A trail of soiled footprints leads to the exit door. The device beside it flashes a message."
    narr "{i}Access Denied{/i}"

    window hide
    scene bg parlor with dissolve
    window show
    nvl clear
    narr "The device itself lacks significant damage, unlike the rest of the room.{w} The doors have handprints all over, especially this one.{w} The middle couch is knocked to its side with a hole punched on its underside."
    window hide
    scene bg meadow with dissolve
    window show
    narr "The painting?{w} It depicts two cows in the meadow. Nothing special about it.{w} Finally, the books, if I can obtain another clue in one.{w} I didn’t bother reading them all{w} – there were no bookmarks of any sort."
    scene bg blood2 with fade
    narr "I’ve reached a dead end. And for whatever reason, my interest fell to the corpse.{w} It’s holding a crumpled paper strip in its hand.{w} If it doesn’t mind, I shall have a look."
    narr "A combination of four numbers – perhaps a code?{w} That’s a given.{w} But where is the device?{w} Not that non-operational one, of course.{w} Just in case, I’ll keep it."

    nvl clear
    narr "But what greater curiosity can the corpse bring to me,{w} an octave higher?"
    narr "With my foot, I rolled it over.{w} Because of the disorientation, I’m not certain if the face looked familiar – its shape is.{w} It lacks{w} features."
    narr "It struck a familiar chord; the heart given a freshly-made haunt.{w} It was greater, evoking even the most distant memory within myself."
    narr "From the mangled face,{w} I made it out to be..."

    nvl clear
    window hide

    "...Kirisaki."

    play music bg_controlledchaos loop
    is4 "Kirisaki-kun!{w} Who did this to you?! {i}*EXHALE*{/i} Where is he? Where is he? {i}*EXHALE*{/i}"
    "{i}I am nowhere. Do not bother trying to find me.{w} He simply knew too much – put it that way, simply.{w} It’s up to you now, what you do from here.{w} Never mind your friend; I’ll see to his honorable leave later.{/i}"
    "{i}The door is open, and you’re free to go.{w} Say, when was the last time you’ve ever stopped to question your environment,{w} your contacts,{w} and your existence?{/i}"

    play sound sfx_heartbeat loop
    window show
    nvl clear
    narr "I’ve forgotten how to move."
    narr "Whatever smack L.C. comes up with next will leave no effect on me – I’ve numbed too much.{w} And the numbness relieved me of fear, draining me of humanity."
    narr "I gained the desire to kill.{w} An animal deserves an animalistic punishment, the same way he did to my friend.{w} Who knows, the wretched bastard might be preying on the others, too!"
    narr "\"He simply knew too much...\" Why wasn’t I killed instead?{w} Am I not the nosy girl, the curious cat?{w} If only I knew, I would’ve asked in the first place – leave it all behind!"
    narr "He’s a liar, a malicious fiend.{w} I deserve nothing – Kirisaki, especially!{w} This is not my idea of atonement."

    nvl clear
    narr "Then again, maybe I’m just a bit too idealistic...{w} too naïve to think properly."
    narr "Sayo is right.{w} Thanks for slapping that to my face."

    stop sound
    stop music
    nvl clear
    narr "Did he say the door is open? I didn’t notice.{w} Perhaps the low rumble from behind overshadowed the device’s beeps,{w} or the latter made no sound at all.{w} At any rate..."
    narr "Hang on a minute..."
    narr "I swear there were two cows in the painting a minute ago. Small and indistinct cattle in the fields, they were.{w} The brushstrokes are the same, albeit the colors much lighter for this one.{w} The cows,{w} one has vanished.{w} And the other?"
    narr "It’s staring directly at me."

    nvl clear
    window hide
    scene bg cowpainting with dissolve

    play music bg_chloeslullaby loop
    "{b}{i}*CHIME*{/i}{/b}"

    window show
    nvl clear
    narr "Ugh! My neck...{w} I felt a bee sting.{w} Not literally, but the sharpness made the pain too real and nearly unbearable.{w} The sensation returned to bother me further.{w} My chest welled up with vomit, yet it refuses to leave."
    narr "My stomach's insides filled with acid,{w} my knees wobbled like jelly,{w} and everything else crashed to the ground.{w} I’ve lost control of my own body, forced to bear the pressure of a thousand unseen forces."
    narr "The pain was indescribable.{w} Accompanying it, a violent convulsion,{w} teeth biting down my tongue and lips until they bleed,{w} and hands tearing at my hair –"
    narr "Uguuu......{w} Go away! Just go away!{w} Hnggg... LEAVE ME ALONE!{w} AAAAAAAARRRRGGGGHHHHH!!!!!"

    nvl clear
    window hide

    scene black with fade
    "{b}*POP*{/b} {i}*SPARK*{w} *HUM*{/i}"
    stop sound
    ".........................................."

    window show
    nvl clear
    narr "It all ceased.{w} My eyes refused to open.{w} This time I felt nothing...{w} I’m dead.{w} The water all around{w} weighing me down, down, down...{w} into the abyss where I should be.{w} Away from all the pain I was made to suffer."
    narr "And with the lack of light, everything looks rightfully black...{w} damn everything.{w} But the air keeps coming, circulating the holes at my head."
    narr "Guess I’m still alive after all."

    nvl clear
    narr "Little by little, my senses returned.{w} A thick liquid slid down my throat,{w} and it tastes rusty.{w} Tongue tip and lips felt warm, as well as the forehead.{w} I might’ve popped a vein in all this madness."
    narr "Everything’s much fouler than before,{w} the air polluted with a mold-like scent.{w} Not even a beam of light intruding my eyes either. I won’t even dare to open my eyes and look...{w} but I did."
    narr "A blur.{w} My eyes took time to adjust to the darker surroundings.{w} I’m sure I haven’t gone anywhere, yet it all feels different.{w} A pair of orange spots caught my attention.{w} Slowly... slowly..."
    narr "The painting is at the center, and the orange spots are the flames.{w} This is an altar, no doubt. An altar for the sacred cow that {i}was{/i} in the painting.{w} Yes...{w} and I perfectly recognized the subject.{w} It registered immediately."

    scene bg minotaur with fade
    play music bg_roadtohell loop
    nvl clear
    narr "It’s a bull, covered with fur from tip to collarbone and horns slightly larger than usual.{w} From chest to bottom, the body of a muscular man. Not sure about the lower limbs."
    narr "Yep, it resembles that of a Minotaur,{w} from the Greek legend of the Labyrinth."

    nvl clear
    window hide

    is4 "Eh...he...{w} Ehehe...ehehehe...{w} Ahahaha... Ahahahahaha! HAHAHAHAHAHAHA!!! YAHAHAHAHAHAHA!!!{w} Ehe! Heh... {i}*EXHALE* *GASP*{/i}{w} That hurts..."

    window show
    nvl clear
    narr "I’m starting to like the fellow.{w} People these days would opt for goats instead; even Lovecraftian monsters tend to be common sight.{w} This – ridiculous as it seems{w} – is a masterpiece!"
    narr "And how did that happen{w} – two cows down to one then changing genders after every viewing?"
    narr "Only then I realized why this is the case."

    nvl clear
    narr "To describe it would sacrifice uniqueness.{w} Let’s have this scene:{w} the interior morphed into an abomination, a sepia touch in every direction{w} – turning me into an unwelcome guest.{w} Everywhere I move, a mix of moans and rings haunts my ears."
    narr "Somehow, I’ve descended to Hades...{w} No. I’m still on Earth,{w} an Earth warped in an unknown dimension.{w} Dreams and reality have inverted themselves, a possibility I feared long ago. Wishful thinking, indeed."
    narr "It all came back to me...{w} it all makes sense."

    scene bg parlor with dissolve
    nvl clear
    narr "Pick up...{w} pick yourself up."
    narr "Sooner or later, even the floor might consume me.{w} I dare to avert myself to share Kirisaki’s fate.{w} And the first step is to the rear."
    narr "Now, the LCD screen displays nothing but black, yet it hums as if electricity is flowing through it.{w} It is not even responsive when the device is given a rap.{w} Just give an {i}Access Granted{/i} message, will you?"
    stop music
    scene bg darkhallway
    narr "{i}*WHOOSH*{/i}"

    nvl clear
    window hide

    is4 "Ha! Not this time, you fiend!{w} Only a fool is befallen a second time by the same trick."

    window show
    nvl clear
    narr "Like before, the door opened without warning;{w} additionally, my knees were shaking at the same rate.{w} Yet the transition is minimal, darkness to darkness."
    narr "The faint light mapped the way out.{w} At the other side of the boundary lay another set of solid footprints.{w} It was not an average person's;{w} it was smaller than an adult woman’s six."
    narr "My estimate is a four, that of a small child.{w} And they appear to be heading towards the living quarters.{w} Both sets disappear upon {i}impact{/i}, as there is a midpoint on the doorway."
    narr "The corridor gave off the same vibe{w} – rusty walls, dirt-filled floors, and a few broken pipes running across the ceiling.{w} This facility has warped itself to a state even worse than before,{w} this as a chasm’s bottom."

    nvl clear
    window hide

    scene bg minotaur with dissolve
    "I swiped a candle without regard of the sinister subject it’s supposed to illuminate."
    "{b}*GRUMBLE*{/b}"
    scene bg darkhallway with dissolve
    "That was it,{w} the perfect time to scram.{w} The door shut itself as soon as I went through.{w} With a flat surface behind me, it is safe to breathe..."

    is4 "Phew. Finally."

    play sound sfx_explosion
    play music bg_satiate
    "{b}*CRASH*{w} *ROAR*{/b}"

    is4 "Ack, AH!{w} Hands off! Let me go! {i}*hic*{/i}{w} HELP!!!"

    window show
    nvl clear
    narr "The painting’s entity materialized itself to attack.{w} For a thief like me, he showed no mercy – something I never expected from itself.{w} Blood ceased flowing to my arms, which its hands crushed to a pulp.{w} The candle fell and almost died out."
    narr "Its burly hands continually wrapped themselves around me, already creating music with my bones,{w} made even worse by the ivy blocking my air!{w} How long is his damn tail?!"
    narr "The next moments felt like hours,{w} hours of enduring the torture forced upon me."
    narr "The ringing grew more intensive and I felt myself colorless, pathetically begging for air.{w} A few drops of saliva forced themselves out, gushing to a drool."
    narr "Soon, my body grew frail and I’ve lost all willpower."

    nvl clear
    window hide

    scene black with fade
    play sound sfx_breathing
    is4 "Mama... Papa... {i}*choke*{/i} brother...{w} Come rescue me......... {b}GAH!{/b}"

    "Somebody help me...{w} please..."
    stop sound
    stop music
    play sound sfx_thud2
    "{i}*SNAP* *CRACK*{/i}{w} {b}*THUD*{/b}"
    return

label ch01_13_facts1:
    scene black with fade
    "JUNE 20, 2013 - 0900H"
    scene bg msci with fade
    window show
    nvl clear
    narr "Following the announcement, a state of calamity was raised."
    narr "Students and staff alike grew paranoid with no knowledge if and when a third case might occur.{w} There were initially qualms from some students regarding the tighter policies, but they warmed up after seeing their effectiveness."

    nvl clear
    narr "To contain the outrage, an agreement was made to not involve the media for a certain period,{w} or until proof of grave malice is presented.{w} Since then, the police handed in zero evidence – an indication of a perfect crime."
    narr "And as model students, they were civil enough to not point fingers.{w} Theories spawned: stories about the resident ghost resurfaced, and a master criminal with a penchant for magic was conceptualized."
    narr "None were of substance."

    nvl clear
    narr "The previous morning saw Inoue and Kyou’s parents to the principal’s office.{w} Tears and pleas best describe the situation, one which Sayo oversaw.{w} Mrs. Genkai attended on behalf of Ms. Harada, the latter still recovering from her shock."
    narr "Kyou’s brother temporarily stopped attending classes.{w} He is currently undergoing therapy and medication to alleviate the trauma inflicted upon him{w} – even worse that he could’ve been the third victim himself!"
    window hide
    show sayo worried at LS with Dissolve(0.2)
    window show
    narr "Despite her constant reminder to stay collected, Sayo herself lapses, partially hindering her performance."
    narr "She went out of the classroom to breathe, sitting on a blue bench by the windows.{w} Thoughts and questions overwhelmed Sayo’s mind.{w} She buried her face, bending down in prayer."

    nvl clear
    window hide

    show hikaru worried at RS with Dissolve(0.2)
    hy10 "Sayo-chan...?"

    "Somehow, that sweet voice uplifted her spirits a bit.{w} Sayo composed herself and gave a subtle heave of confidence."

    show sayo normaltalk at LS with Dissolve(0.2)
    sr5 "Hikaru, good morning!{w} What have we?"

    show hikaru smile at RS with Dissolve(0.2)
    hy10 "Errr... not much, really, especially with all of this going on.{w} You alright? You look a bit pale."

    show sayo seriousserious at LS with Dissolve(0.2)
    "Sayo understood her intention{w} – Hikaru saw through the facade, reflecting it on her face.{w} The former made no attempts to sugar coat the situation."

    show sayo serioustalk at LS with Dissolve(0.2)
    sr5 "I appreciate if you’ll sit down with me; otherwise, I see no point in holding you.{w} Where’s Aria?"
    show hikaru smirk at RS with Dissolve(0.2)
    hy10 "Went by myself. I just needed to {i}go{/i}. {i}*giggle*{/i}"

    "With all the pleasantries dealt with, their conversation immediately flowed to the mysterious abductions.{w} Sayo handled the matter with care, as it was normally discussed with discretion."
    "She leaned closer to Hikaru."

    show sayo normaltalk at Three2 with Dissolve(0.2)
    sr5 "You’re aware of our teachers’ advice – not to accuse nor suspect without proof?{w} Let’s just say... there’s no stopping it."
    hy10 "Mouth zipped. Spill the name, please."
    show sayo seriousnormal at Three2 with Dissolve(0.2)
    sr5 "Not my point, you see. What I meant is...{w} {i}*sigh*{/i} Look, even the police are empty-handed until now.{w} And the gossip? Off the wall and senseless! When will we ever learn...?"
    show hikaru focusright at RS with Dissolve(0.2)
    hy10 "Don’t stress yourself, Sayo! There are much bigger things to worry about."
    sr5 "Yes, bigger things{w} of a smaller scale than this one.{w} Who would’ve thought? A crisis. And on the very first month!{w} To think that wasn’t enough to keep our hands full."
    sr5 "Say a scandal breaks out if this goes on far too long,{w} would the parents still choose to enroll their children here?{w} It'll become even worse if-"
    show hikaru focusleft at RS with Dissolve(0.2)
    hy10 "If someone was to re-enact the Sacred Heart murders, that is."
    show sayo serioustalk at Three2 with Dissolve(0.2)
    sr5 "Re-enact... copycat murders?{w} And on what motive? The truth never came out!{w} The closest link we’ve got is Suzumoto-san, but even she is a mere connection. What has she to do with it?"

    "Hikaru shrugged.{w} Even after countless times she was mentioned, Sayo always disregarded Suzumoto’s involvement{w} as all they have is the night guard’s horror story."
    "But the notion of copycat murders intrigues Sayo.{w} To some, it’s just another cozy mystery plot. However, the horror behind those is real."
    "Actual cases have been documented as of late, with the most deranged men following the likes of Jack the Ripper, H.H. Holmes, and Ted Bundy."

    show sayo seriousserious at Three2 with Dissolve(0.2)
    sr5 "Pardon. I seem to have chosen my words poorly.{w} Even I make mistakes, you see... even the most fatal ones."
    show hikaru talk at RS with Dissolve(0.2)
    hy10 "Everyone’s on edge, Sayo. You're not the only one I know that's been acting weird lately.{w} Besides, I’ve got your back. So, why worry? {i}*giggle*{/i}"
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "You flatter me. I should be the one to watch yours. Hehehehe.{w} Glad to have friends on their heads most of the time when you're not.{w} Ah, well. What interest is there?"
    show hikaru smile at RS with Dissolve(0.2)
    hy10 "..."
    sr5 "You’ve no intention to snack?"
    hy10 "No. I’ll hold this off until lunch.{w} Oh! That reminds me.{w} I have to study calculus. Our assignment, I mean."
    show sayo normaltalk at Three2 with Dissolve(0.2)
    sr5 "But as far as I remember, today you have no–"
    show sayo smirknormal at Three2 with Dissolve(0.2)
    sr5 "Oh... *chuckle*{w} Is that what I’ve heard?"
    show hikaru blush at RS with Dissolve(0.2)
    hy10 "Eh? Heard what?!"
    show sayo smirkblush at Three2 with Dissolve(0.2)
    sr5 "Hihihihihi..."
    hy10 "No! No! No no! I genuinely just want some tutoring, nothing more.{w} Sayo... who told you that? Grrrr..."
    sr5 "Hihihihihi...{nw}"
    show sayo happyclosed at Three2
    sr5 "Hihihihihi...{fast}nyahahaha! {i}*giggle*giggle*{/i}{w} Yeah. Be on your way then. And good luck~. {i}*wink* *wink*{/i}"

    hide hikaru with Dissolve(0.2)
    show sayo smileopen at LS with Dissolve(0.2)
    "Flustered, Hikaru pranced back to IV-C.{w} Sayo watched her subtly and amused herself by drawing hearts in the air, all towards Hikaru."
    "For a while, she enjoyed herself at the bench, greeting people as they passed by."

    show sayo worried at LS with Dissolve(0.2)
    play music bg_vulcan loop fadein 1.0
    window show
    nvl clear
    narr "Then she returned to her previous mood."
    scene bg classroom2 with dissolve
    show sayo worried at LS with Dissolve(0.2)
    narr "She went to her seat, searching through her backpack.{w} She took out her journal, a maroon hard-covered book fastened with a similarly-colored ribbon.{w} She unfastened it and opened a few pages."
    narr "Within the most recently written pages, she had written the following:"
    hide sayo with Dissolve(0.2)

    scene bg book with fade
    nvl clear
    narr "{i}June 19, 2013{/i}"
    narr "{i}It’s been a day since the disappearances of Inoue Shinozaki and Kyou Kirisaki, both of whom were my classmates during my First and Second Years, respectively{w} – at least from what I’ve heard first-hand from Mrs. Genkai and Ms. Harada.{/i}"
    narr "{i}I inquired of IV-A’s vice president.{w} She mentioned how caring their adviser was, having no children as of late.{w} It impacted them greatly, having potentially lost a sister in a senseless crime.{w} My sympathies.{/i}"
    narr "{i}The same goes for Kyou’s brother, his mother and his former adviser, Mrs. Genkai.{w} They have agreed to let his brother stay home while the investigations are underway.{w} To describe him as jarred is an understatement – he fears for his life, one we’ve felt gravely after we heard his story.{/i}"

    nvl clear
    narr "{i}It was half-past five when they arrived at the market to buy materials for their respective activities{w} – Kyou for their activity in PE, and his brother for an oral report in History.{/i}"
    narr "{i}They entered the school gate 15 minutes later, which Onifuchi-san confirmed,{w} finally parting ways at the first staircase.{/i}"
    narr "{i}That was the last time they met.{/i}"
    narr "{i}He remembered no suspicious person inside the classroom nor the storage area under the stairs.{w} He did, however, confirm seeing some other students at the second floor,{w} though he wasn’t able to distinguish which year level they were.{/i}"
    narr "{i}I recalled that Akira and Miyu usually arrives around that time, so I asked him if he saw them.{/i}"
    narr "{i}Negative.{/i}"

    nvl clear
    narr "{i}So, we decided to interview the Shinozakis next.{w} Inoue’s father spoke for her mother, who was too distressed to speak.{/i}"
    narr "{i}At five o’ clock, Dr. Shinozaki left home to attend to the Operating Room.{w} That leaves two people home as Tomonori-san is currently boarding out of town.{/i}"
    narr "{i}He repeated Mrs. Shinozaki’s story that morning, 5:45AM when Inoue left for school.{w} That means she would’ve found Kyou in IV-A,{w} but if that’s the case...{w} No. Let’s not be a bunny.{/i}"
    narr "{i}I personally asked Onifuchi-san if Inoue passed by, describing her features to him{w} – he wasn’t very good with faces.{/i}"
    narr "{i}\"Hair down or with a bun, no one?\" I added.{w} While he did see some students matching that description, he couldn’t confirm if he saw Inoue yesterday morning.{/i}"
    narr "{i}One last question, \"And the earliest student or staff, do you recall the time?\"{w} He replied, \"5:20, around the same time he assumed his post.\"{w} And I wondered who, but I couldn’t think of anyone.{w} I arrived ten minutes later than the usual time.{/i}"

    nvl clear
    narr "{i}These are the facts I gathered, mostly from the meeting this morning.{w} Mrs. Genkai excused me for my third period, coincidentally Ms. Harada’s scheduled time with us.{/i}"
    narr "{i}It only begs the question, \"Who?\"{w} He mustn’t be who I think he is. Too obvious a target, might I add.{w} Until the police have gained some significant leads or evidence, I shall withhold my tongue.{/i}"
    narr "{i}But I’ll keep my wits about me.{/i}"
    narr "{i}'Til I ramble again,{w}\nSayo Ronoroa{/i}"

    nvl clear
    narr "Having re-read the entry, Sayo replaced the journal in her backpack.{w} Then, she got the English textbook from under her desk, opening it to a random story."
    narr "All while contemplating what to write later that night."
    stop music fadeout 1.0

    nvl clear
    window hide

    scene bg classroom1 with fade
    show miyu naughty focuspose at Three2 with Dissolve(0.2)
    show hikaru focusright at Three1 with Dissolve(0.2)
    "Miyu glanced at the problem."
    "They were given a set of questions on Continuities, with functions and graphs as bases.{w} There is one question that baffled Hikaru,{w} a rational function that is discontinuous in hindsight – a type of removable discontinuity."

    show miyu naughty closepose at Three2 with Dissolve(0.2)
    mh8 "You need no formal conclusion. Just indicate the x-value that will zero both the numerator and denominator.{w} That’s it. Just solve it normally."
    show hikaru naughty at Three1 with Dissolve(0.2)
    hy10 "Ooooh... Nice. Nice.{w} Thanks for the help. You’re the best!"
    show miyu naughty closepose2 at Three2 with Dissolve(0.2)
    mh8 "Anytime."
    show miyu naughty focuspose2 at Three2 with Dissolve(0.2)
    mh8 "By the way, have you anything new about... {i}that{/i}?"

    show hikaru serious at Three1 with Dissolve(0.2)
    "Hikaru looked puzzled, scrutinizing what he meant..."
    show hikaru worried at Three1 with Dissolve(0.2)
    "Hikaru looked puzzled, scrutinizing what he meant...{fast} then she picked up."

    hy10 "Nothing, still on a roadblock. Tsk.{w} Even Mama is worried for me. She and Papa have agreed to pick me up at 5:30 everyday.{w} What about if there are projects? Such bad timing..."
    show miyu pissedclosed at Three2 with Dissolve(0.2)
    mh8 "Forget them. You know how our teachers value our safety.{w} I’ve heard they were changing their list of activities while the investigations are underway."
    show hikaru focusleft at Three1 with Dissolve(0.2)
    hy10 "Hmmm..."
    show miyu naughty focuspose2 at Three2 with Dissolve(0.2)
    mh8 "Perhaps Sayo knows something...{w} if she’s willing to disclose even the most minimal details."
    mh8 "But I find it more convenient to ask you{w} – you two were having a chat earlier, weren’t you?{w} Our council president is bound to slip something out for sure."
    show hikaru focusright at Three1 with Dissolve(0.2)
    hy10 "No. She just needed a faucet to rant on.{w} I related to her something from a documentary,{w} about copycat murders, I think she referred to them."
    show miyu naughty focuspose at Three2 with Dissolve(0.2)
    mh8 "Bingo. Anything else?"
    hy10 "I don't think so. She cut herself off after a while, upon realizing her error in {i}wording things{/i}.{w} Suffice to say she looked anxious when I first saw her."
    show miyu naughty closepose at Three2 with Dissolve(0.2)
    mh8 "Then she’s not telling everything..."

    show hikaru angry at Three1 with Dissolve(0.2)
    "This took Hikaru aback.{w} She recalled every instance of their brief dialogue,{w} and to her knowledge, Sayo was sincere throughout{w} – unless Miyu’s notion is true."
    show miyu naughty smirkpose at Three2 with Dissolve(0.2)
    "Sensing her confusion, Miyu shot back a delighted face."

    mh8 "Ahahahahaha! Make no mistake. I mean not to incriminate her.{w} In fact, I can vouch for her innocence.{w} She arrived after me and Akira’s service van – six o’ clock.{w} Still confused?"
    show hikaru serious at Three1 with Dissolve(0.2)
    hy10 "Yeah. Yeah. I get you. I don’t suspect her either.{w} But out of all the people here, why her specifically?{w} It’s absurd enough to think about it."
    show miyu naughty closepose2 at Three2 with Dissolve(0.2)
    mh8 "Yes. Yes. Absurd. {i}Truly{/i} absurd.{w} But what if this is another paranormal mystery? Yes... now that’s the tender meat..."
    show miyu bored at Three2 with Dissolve(0.2)
    mh8 "Wait. Don’t you have anything else to do?"
    show hikaru smile at Three1 with Dissolve(0.2)
    hy10 "Nothing more."
    show hikaru naughty at Three1 with Dissolve(0.2)
    hy10 "Nothing more.{fast} Hey, thanks for the help! Hahahaha!"
    hide hikaru with Dissolve(0.2)

    "Miyu responded by holding up three fingers: thumb, index, and middle."
    show miyu confused at Three2 with Dissolve(0.2)
    "After Hikaru returned to her seat, Miyu returned to his business earlier.{w} He glanced at his watch and held his arms behind his head."
    "His mind became clear, ignoring any external presence around him.{w} He lost himself in a sea of thoughts."

    show miyu pissed at Three2 with Dissolve(0.2)
    mh8 "I wonder what happened to those two.{w} Are they still breathing?"
    mh8 "The pieces don’t fit any way I look at them, but I reckon I must try harder.{w} Wish this ends as soon as possible.{w} I don’t even want us to stay like this forever."
    hide miyu with Dissolve(0.2)

    "{b}*RING* *RING* *RING*{/b}"
    return

label ch01_14_labinoue3:
    scene black with fade
    "Date Unknown - Time Unknown"
    play music sfx_heartbeat loop
    play sound sfx_breathing
    window show
    nvl clear
    narr "Crawl... Crawl...{w} Like a worm, you must."
    narr "Get away...{w} away from this place you’ve once known as paradise,{w} the place whose fangs desire your suffering.{w} This place is a prison, Purgatory...{w} Death is the sole entryway,{w} and death is the only exit."
    narr "I’ve been made a sacrifice, true to the facility’s nature.{w} But even then, this place could be worse than the Labyrinth itself,{w} a legend manifesting itself into reality."
    narr "My soul has been wandering around in this desolate place without any sense of direction{w} endlessly... endlessly...{w} until I realize that exhaustion is an illusion,{w} an illusion that rings true."
    narr "That constant fear of darkness blanketing the proximity{w} and of a malevolent force tailing you no matter how fast or how far you’ve treaded, seeking to crush your entirety.{w} One never feels much closer to death’s pangs."

    nvl clear
    narr "The moment I opened my eyes once more – a little before that{w} – death was ascertained.{w} Since then, I’d been a subject of torture, one that's able to break my dignity and had me questioning my beliefs."
    narr "Everything faded to black,{w} and a force transported me to a dimension contrasting the reality I’ve known since.{w} And I care not if I’ll ever return.{w} Besides, who even managed to resurrect from death?"
    narr "No one.{w} No man ever did."

    play sound sfx_thud
    nvl clear
    narr "The illusion has been shattered."
    narr "Heavy pressure crushed my body and my legs could propel me forward no longer,{w} but I won’t die.{w} Not if there’s an ounce of hope left."
    narr "And that ounce lay itself exposed to my delight."
    
    window hide
    stop music
    scene bg darkhallway3 nightmare with fade
    window show
    nvl clear
    narr "Among the cracked pieces of ceramic tiles and rusty paint, therein lies a crimson smear.{w} Initially hand-sized patches scattered around, they eventually converged to form a puddle,{w} But it was not just a puddle."
    narr "Somebody was dragged before me,{w} to the left passageway, I see.{w} Thus, I simply heeded my subconscious.{w} Though struggling, I managed to get on my feet and reached the door at the end."
    play sound sfx_dooropen
    narr "I threw myself inside,{w} and the door forced itself shut, leaving me in the darkness once more.{w} The heavy footsteps echoed louder and louder...{w} then it stopped.{w} The entity reversed direction as its steps gradually became lighter.{w} Lighter... lighter... {i}lighter{/i}..."
    narr "It’s gone now,{w} probably shifting its interests to something else.{w} What’s that foul smell?"

    nvl clear
    narr "Then, from across my position{w} appeared a faint light ray.{w} Its color was indistinguishable, making the room’s features more apparent.{w} The blood smear – slushing at every foot contact – led to the center,{w} eventually ending at the larger body of liquid."
    window hide
    scene bg pool with fade
    play music sfx_waterdrip loop
    window show
    narr "I managed a peek.{w} Dark-bluish water filled the pool, welling from the two tanks on one end.{w} The light’s reflection presented more detail to its surroundings."
    narr "The square pool, depth unknown, has straight columns on each corner.{w} It’s missing a ladder, but the surface is about two inches from the floor.{w} There are exposed wires hanging from the columns, two big ones from the ceiling.{w} A death trap in plain sight!"
    narr "I sat at the nearest left column{w} as my legs are too weary to walk around.{w} I shut my eyes, wishing for all this to end.{w} But I can’t.{w} I’m cursed to live through Hell with no means of escaping...{w} not even sleep will save me."
    stop music

    nvl clear
    narr "Half an hour passed{w} and the pain mellowed.{w} I’m able to walk, but only for a few moments, lest I spend another half hour recuperating;{w} worse, it might turn to hours."
    narr "The water illuminated the wall across me, if only faintly.{w} Near the middle are three valves,{w} each connected to pipes of various widths and has a common pipe perpendicular to them."
    narr "A valve’s size is proportional to its pipe.{w} Likewise, there are three similarly-sized tanks each fitted with a pressure gauge going up to 100 psi."
    narr "Farthest to the left are some lockers large enough to fit in a suit.{w} One of them has a broken padlock.{w} Suppose something is there..."

    play music guest_corpseparty loop
    nvl clear
    narr "A little later, my legs recovered;{w} thus, I can explore the area freely."
    narr "Inside the locker is a crowbar, much to my delight.{w} Ah, prepare for the mighty iron, you slobs!{w} And the crowbar mustered its magic."
    narr "The two lockers on its left were empty, while the remaining one contained a wet suit.{w} I removed it from the hook and unzipped its back.{w} A piece of bond paper is taped on the chest area."
    narr "I examined its contents.{w} Written in blue ink,"
    narr "{i}To initiate purification, apply the indicated pressure to all tanks: 70 psi minimum.\nWARNING! Explosion Risk – Do not overload tanks. Limit pressure to 100 psi.{/i}"

    nvl clear
    narr "I replaced the paper in the locker, shifting my attention to the pool.{w} My legs prohibited themselves to dip, as the color reeks of contamination."
    narr "The door across the pool, right of my entryway, became another point of interest.{w} Beside it is yet another device, its screen pulsating erratically.{w} There’s a slot on top to slide a keycard into."
    narr "There are two other doors as well,{w} but their respective devices are currently offline.{w} Thus, one choice remains.{w} Damn hell if I’m going back to that corridor – I’d get gutted."

    nvl clear
    narr "It may have been a mirage, but something glittered from the pool.{w} Chin on tiles, a submerged piece of plastic came into sight.{w} I skirted the edge, taking care not to fall into the liquid."
    narr "It’s a plastic container, inside of which is a card.{w} The crowbar is useless at this point{w} – the item is too far into the alcove{w} and the latter itself is too deep to angle the crowbar correctly."
    narr "And no. The wetsuit won’t save me from any adverse effect the water might have.{w} It’s all on the purification process now."

    nvl clear
    narr "Eyes on the pressure gauge and hands on the left valve, I gave the latter one full clockwise rotation.{w} The tanks’ pressure rose a certain value.{w} The values returned to initial state upon reversing the action."
    narr "The two other valves wouldn’t budge no matter how forceful a grip applied to them.{w} Why?{w} The left valve needed a full rotation first. Only then the middle valve would become movable.{w} I returned it to its previous state."
    narr "Still, the right valve wouldn’t budge.{w} I repeated the trick with the left valve using the middle.{w} This time, it moved."
    
    nvl clear
    narr "Thus, the valves work like this, in principle:{w} One rotation either pressurizes or depressurizes at least one tank."
    narr "After playing around, I took note of the following pressure changes, in tank order:"
    narr "{i}Left Valve: +25 psi, +40 psi, +10 psi\nMiddle Valve: +20 psi, -10 psi, +35 psi\nRight Valve: -15 psi, +20 psi, -45 psi{/i}"

    nvl clear
    narr "Then again, I might risk an explosion if I mess up.{w} Another note,{w} the movements need memorization, as a zero-pressure tank cannot be depressurized further{w} – non-zero pressure on other tanks in this case is possible."
    narr "Before starting, I made a double-check on the other door."
    narr "Silence...{w} dead silence..."
    narr "No time to waste; I’ve already waited enough.{w} Any longer and another bizarre occurrence might pop up.{w} You never know."
# Potential Puzzle on this Part

    scene black with fade
    nvl clear
    play sound sfx_hiss
    narr "{b}*WHIRR* *HUM*{/b}"
    narr "Oops...{w} That bellow doesn’t mean well.{w} What was the range again?{w} 70-100 psi,{w} and all movements restricted to a 100-psi maximum pressure."
    narr "Or is it trauma?{w} It wasn’t confined to the tanks nor the pipes.{w} A low sound came from the pool.{w} I spun around, witnessing the change in the water’s color.{w} In the process, the tanks might have partially drained the pool."
    narr "Perfect{w} – the alcove is just above the new level!"
    narr "The crowbar found another use, the last instance, I suppose.{w} All I need to do is bend down near the edge and bring the plastic pouch nearer, enough to grab it by hand.{w} A mediocre task if —"

    nvl clear
    window hide

    stop sound
    stop music
    is4 "Is this a joke?!{w} I thought it all ended there...?"

    scene bg pool nightmare with fade
    play music bg_satiate loop fadein 1.0
    window show
    nvl clear
    narr "From the drain emerged a red cloud, slowly engulfing the liquid until no clear area remained.{w} With it, came the seeds, a rare kind.{w} They are much larger and has a tail on one end."
    narr "It is a freshly-made watermelon juice – only unappetizing!"
    narr "With my eyes on the pool, electricity buzzed from above,{w} activating the lights in rapid succession.{w} The top half of the room revealed itself..."
    narr "And yes, it was all familiar sight.{w} At the ceiling near the hanging wires,{w} a flesh-like fluid plastered itself...{w} with no fluid dripping from it!{w} Once more, the pressure inside the room increased{w} – or is it just me... again?"
    narr "I stood there, petrified."

    nvl clear
    window hide

    play sound sfx_metaldrop
    "{b}{i}*CLANG*{/i}{/b}"
    "The crowbar fell from my hands, luckily not into the pool itself.{w} Its surface had apparitions swimming all around...{w} dancing... dancing...{w} forming figures once hidden in subconscious thoughts."

    play sound sfx_static2
    scene black with fade
    is4 "Gnnnkk... Gah... {i}*SQUEAL*{/i}{w} It hurts... It hurts... It hurts!"
    "{i}I’d like to clean – {b}SOME AFFAIRS{/b} – momentarily – personal {b}THINGS{/b}...{w} Naivety won’t get you too far. {b}I’M NOT SAYING YOU ARE{/b}...{w} {b}DO YOU{/b} – believe in – {b}GOD{/b}?{/i}"
    "...\n{w}...\n{w}......"
    is4 "AAAAAAAAAAAAAAAAHHHHHHHHHH!!!!!!! ENOUGH!!!!!!!"

    play sound sfx_static
    "{b}*BUZZ* *STATIC*{/b}"
    stop sound

    "{i}Clutch your head if you like. Scream until your voice dies away.{w} No one here is to help... except for yourself.{w} A naïve little girl you are, easily mended and easily swayed.{w} Swing, swing, swing.{w} Rocking like a hammock with a baby...{/i}"
    is4 "Shut up! I’m not afraid of you anymore!{w} All these monsters and gauntlets... you molded them out of my mind, didn’t you?!{w} And you dare mock me, Inoue Shinozaki?"
    "{i}You consented to a simple agreement at the start, didn’t you?{w} You are a guest,{w} and as a guest, you are bound to follow the rules, puku.{w} And as for the other guest, he exists no longer...{w} No longer, puku.{/i}"
    is4 "And for that I’m grateful?{w} No! Had I been earlier in the living quarters, I would’ve been disgraced the same way as the {i}other guest{/i}{w} – my friend, Kirisaki!{w} What has he done?!"
    "{i}Who is Kirisaki? Hmmm... Swing, swing, swing...{w} Let me see...{w} I don’t recall.{w} Does a \"Kirisaki\" exist?{w} Ah! He does{w} no longer – neither do you.{/i}"
    is4 "I’m flesh-and-blood, breathing ably well.{w} The foul smell, the carnage-filled corridors, and the pangs all over me... that doesn’t prove anything outright.{w} But I exist!{w} My friends... my teachers... and my family... to them I exist!"
    "{i}And where are they, puku?{/i}"
    is4 "Somewhere... home... outside!{w} I don't know!"
    "{i}*snicker* *cackle* *cackle*{/i}"
    is4 "Tsk!{w} {i}*hic* *hic*{/i} You bastard... Uhu...uhuhuhuhuhu..."
    "{i}Oh... you made her cry.{w} You bad, bad – you gonna get slapped in the butt-butt.{w} Swing, swing, swing... {b}POW{/b}! Naughty –{/i}"
    "{i}You started it, puku!{/i}"

    stop music
    "{b}*BUZZ* *RING*{w} *BUZZ*{/b}"
    play music sfx_heartbeat loop
    "Silence...{w} a relief{w} to never hear those damned voices again."
    "The tears continued to gush forth, a river sufficient enough to fill.{w} By this time, I had enough. Everything felt unnecessary.{w} Why wouldn’t they let me be?!"
    "The words resonated to my person, slowly infecting my system.{w} How could I consider something so toxic?{w} Have I... Have I..."

    unk "You would accept my pardons, yes?"
    is4 "Spare me the impudence.{w} I do not permit you to speak – such words do not flatter me."
    unk "Hoh?{w} A light beam to a mirror, or a man to his skull?{w} Every so often I wonder, is Inoue Shinozaki a stage actress on the sides?{w} It’s as though you’re able to focus the spotlight on yourself whenever you wish – dahlias within dystopian cosmos makes my heart go yonder."
    unk "Now you see why I’ve taken a fondness of you, despite the hostility you’ve shown the master.{w} A whip would be too old-fashioned, but the easy way{w} I have taken. {i}*snort* *snicker*{/i}"
    is4 "I may be born of noble birth, but I know when to bend the rules.{w} Rules are there to enforce authority or to allow abuse.{w} Certainly, rules do not add respect,{w} and respect is what you do not deserve."
    unk "Is that true? Is it not? No one can tell.{w} To begin with,{w} there is no proper way to begin.{w} And you’re clever enough to realize that, so far,{w} I gave you no rules. Did I?"
    is4 "You did, you amnesiac.{w} Either you let me out of here immediately or –"
    unk "Hmmm... I do not recall a single rule.{w} I do recall, however, saying that to you – if you count a few days old message, that is.{w} In fact, that is not a rule nor a restriction, no. {i}*chuckle*{/i}{w} It’s a warning."
    is4 "{b}!{/b}"
    is4 "What are you talking about?"
    unk "If you do not wish to hear my voice, shame.{w} I desired to exchange a few handshakes should you escape.{w} Thus, I remove the privilege from you, you who had treated our friendship a waste."
    unk "You aren’t a loss, Shinozaki{w} – I’ve got other friends to attend to.{w} {i}*sigh*{/i} The chance that you’ve blown... think about it."
    is4 "I’ve a lot... {i}*hic*{/i}{w} And {i}one{/i} of those is the same one {i}you{/i} murdered!{w} How cruel could you be to handpick an innocent boy? {i}*hic*{/i}"
    unk "Who? Murdered? I suggest you abstain from slander.{w} What have you to prove? Do you not see my hands, free from blood?{w} Of course, you don’t.{w} To you, I’m a voice from a location you’ve no knowledge about."
    unk "Besides, have you even considered doing another take?"
    is4 "What?!"
    unk "Your mind’s all mushy now. Sort your own problems out, dear.{w} Better for me to zip up and leave, since you’ve no need of my services.{w} Oh! Should you ever leave, do write a little something and leave it at the door."
    unk "We’ll still encounter each other again. {i}Ta-ta!{/i}"
    is4 "Hold it!{w} The children earlier...{w} who are they?!{w} What do they mean by those words?"
    unk "Again, you are confused.{w} Leave it all behind – it is nothing.{w} Besides, what interest is there to behold?"
    is4 "{b}*GASP*{/b}{w} Don’t tell me you’re..."
    stop music

    "{b}*BUZZ* *STATIC*{/b}"
    play sound sfx_waterdrip
    "And I never heard from him again."
    "Partially, I resent the hostile demeanor.{w} That could spell the difference between my end and my survival.{w} Perhaps he does not mind? I don’t either."
    scene bg pool nightmare with fade
    "I went with my business, sending the crowbar down to its job, before another spell effects on me.{w} I forbade my eyes to raise a single inch, knowing what’s down there."

    "{i}I didn't do it...{/i}"
    stop sound

    "Shut up. Urgh.{w} There it is again... the air... that whistle...{w} Keep going. The claw is nearing the prize.{w} Just to stretch a bit farther..."

    is4 "Alright! That must be it."

    "The card is within reach.{w} I dragged it towards the opening, maintaining full control despite the chaotic atmosphere.{w} Finally, I saw the plastic’s corner{w} and the crowbar served its purpose."

    is4 "Reach for it... {b}{i}*GRUNT*{/i}{/b}{w} Come on, now. Umph... {b}{i}*GRUNT*{/i}{/b}"
    is4 "Yes!"

    scene black
    "I removed the card from the plastic pouch and examined it.{w} In my hands, I have the ticket to freedom!"
    play sound sfx_explosion
    "{b}*BOOM*{/b}"

    is4 "NYAAAAAAAAAHHHHHHHHHH!!!!!!"

    play sound sfx_splash
    scene bg underwater nightmare
    "{b}{i}*SPLASH*{/i}{/b}"
    play music bg_corruption loop

    play sound sfx_splash2
    is4 "Gah! Help me!!!{w} Somebody... please! I can’t swim!"
    is4 "Wah - {b}{i}*GURGLE* *GURGLE*{/i}{/b}{w} HAH! Anybody... please{w} just get me out of here, quick!{w} {b}*GASP* *GASP*{/b} L.C., still there?!"

    "No answer.{w} Why would he bother? He closed his ears to my pleas{w} – I’ve sent him away.{w} Right when I needed him... No. Actually, anybody! Anybody to fish me out of this hellhole!"
    "I’m swimming with a bunch of anguished souls, vermin who had rotten for a few days, and...{w} juice! Say not the word.{w} If he could see this image of a damsel flailing her arms around in futility..."
    "If –"
    play sound sfx_splash2
    "{b}*SPLASH* {i}*GURGLE* *GURGLE*{/i}{/b}"

    is4 "HMPH! GRK!!! Ng... Ulk! {i}*GURGLE*{/i}"

    "Help..."

    scene bg underwater with dissolve
    window show
    nvl clear
    narr "The chilly waters began devouring my whole body.{w} I can only stay afloat for so long, having barely enough strength to fight my way back up.{w} The only way is down... down where the current is forcing me to go."
    narr "It all began at my heart, or somewhere within its proximity.{w} The pain radiated to my neck and chest, immobilizing my arms,{w} and acids frenzied inside my stomach.{w} They seem to sympathize with me, yet they are still thorns wearing me out as time passes."
    narr "By now, probably half of my lungs are submerged.{w} There’s still a pocket of air, at least.{w} Not a minute, I’d last. A damned way to spend your last minute, eh?{w} {i}Dead on the Spot{/i}...{w} I’m seeing it now."
    narr "Perhaps {i}Dead on Arrival{/i} if I’m lucky...{w} But..."

    nvl clear
    window hide

    scene bg underwater nightmare with dissolve
    "Somebody...{w} please..."

    scene white with dissolve
    "{i}Get her up! Up!{w} Hey you, hang on for a bit.{/i}"
    "{i}Somebody call the medics, please!{w} ...I’ll handle the CPR. Stay with me...{w} One, two, three. {b}*SUCK* *BREATHE*{/b}{w} One, two, three. {b}*SUCK* *BREATHE*{/b}{/i}"
    "{i}Get her on the stretcher. She needs oxygen.{/i}"

    window show
    nvl clear
    narr "Perhaps... they are already too late."
    narr "If only I had the chance to say sorry.{w} I never meant to inflict pain towards other people, especially my friends.{w} Do they still resent me?{w} That's a thought haunting enough to tether my soul to Earth at my passing."
    narr "But I am never guilty of anything. I never let blood stain my hands!{w} Absolve me, please!{w} That was just an accident. I had no hand in it!"
    play sound sfx_rumble
    narr "{b}*RUMBLE* *BUZZ*{/b}"

    nvl clear
    narr "Torn between two worlds, my body continued to sink.{w} Yet my soul began to ascend,{w} away from me, away from the humiliation its body shall suffer.{w} Never it was meant to be like this..."
    narr "That’s the price I have to pay for being snoopy, isn’t it?{w} When one acts without thinking{w} – rather, swallowing continually without delay...{w} I’m out of ways to describe this feeling."

    nvl clear
    window hide

    play sound sfx_ambulance1
    "{b}{i}*SIREN*{/i}{/b}"

    "{i}We’re here. Hold on...{w} Move! Move! Hurry!{/i}"

    window show
    nvl clear
    narr "Everything happened in total darkness."
    narr "The gurney flew through the double doors, a pair on each side to guide the head and foot.{w} Then came another,{w} and the ride ran faster."
    narr "Onwards, all words became a murmur.{w} High and low tones mixed in the air, ears too numb to even distinguish which.{w} My body continued to fall, supported by a cushion to soften the blow."
    play sound sfx_ekg loop
    narr "And it came to a halt{w} – body suspended in the air, stuck to that same cushion.{w} It has no grip on me... so..."
    narr "Now, only an unfamiliar pair remained.{w} Both were in a rush, flying past me at an incomprehensible pace."
    narr "More shouting...{w} all just a murmur.{w} At last, someone stopped,{w} standing right beside me."

    nvl clear
    window hide

    "{b}*SPARK* *CRACKLE* {i}*HUM*{/i}{/b}"

    "{i}CLEAR!!!{/i}"

    "A blow towards the device.{w} and another...{w} and another...{w} each time, my blood depletes gradually."
    "Have I any left?"

    "{i}CLEAR!!!{/i}"

    stop music
    stop sound
    play sound sfx_ekg2
    scene red with dissolve
    scene bg underwater nightmare with dissolve
    scene bg underwater with dissolve
    scene black with dissolve
    "{b}*BEEEEEEEEEEEEEEEEEEEEP*{/b}"
    "............................................."
    stop sound

    "{i}Dead on arrival.{w} Transfer her to the morgue immediately.{w} You, kindly prepare the certificate for this one.{/i}"

    "{b}*CRACKLE* *CRACKLE* {i}*SUCK*{/i}{/b}"
    return

label ch01_15_labkyou3:
    scene black with fade
    "Date Unknown - Time Unknown"
    window show
    nvl clear
    narr "Show me a glimmer of hope, a sign of salvation.{w} Let me be in this domain no longer{w} If I were to be crushed, then so be it.{w} Let me come to You... pray heed my calls.{w} I need to confess..."
    narr "Whatever my sins are, please...{w} I beg for repentance.{w} Whether they’re still in memory or not, I ask them to be erased.{w} What worth is becoming Your man if the beginning is a failure, isn’t it?"
    narr "Lastly,{w} please tell me...{w} what have I done to deserve this?"

    nvl clear
    window hide

    play sound sfx_spark
    "{b}*THUNDER*{/b}"

    unk "{i}*GASP*{/i}"

    play sound sfx_thud2
    "{i}*THUD*{/i}"

    window show
    nvl clear
    narr "So this is it...{w} one step closer to freedom – if I am sure of it, that is."
    narr "Still, everything I’ve witnessed is still an enigma.{w} The more I think about them, the more clouded the answers become, a fitting match to their master’s personality."
    narr "This is the heart of this world.{w} In the context of our own dimension, this is the generator room. No further analogy needed.{w} Still, I must thank Yoshiro for his knowledge in electricity.{w} Were it not for him, I’d be trapped in here."
    narr "Imagine if I went the other way.{w} Hmmm... I’m better off here.{w} Who knows, the passageway might’ve led to a slaughterhouse.{w} As if the path going here was any different."

    nvl clear
    narr "Aside from the running electricity and the occasional sparks in the room, everything is dead silent.{w} It’s one thing if the atmosphere gives off a serene feeling,{w} but rarely does it become dissonant to the eyes."
    narr "Black and orange, two colors that describe absolutely everything."
    narr "There’s not a soul anywhere since the living room.{w} If I composed myself then, I’d have known the other person’s identity.{w} Then again, if the odds were ill, I would’ve wished otherwise."
    narr "Another dilemma.{w} If I only know where this adds up to."

    play sound sfx_wind loop
    nvl clear
    narr "{b}*HUM*{/b}"
    narr "This time, the wall is barely visible within a few meters.{w} A light fixture illuminates the area, revealing a forked path upon closer inspection.{w} Which way to take this time, left or right?"
    narr "I haven’t drawn a mental image of the place, but is it truly worth it?{w} The facility defies perception in an unnatural manner,{w} and the evidence have already manifested themselves for quite some time."
    narr "For every step I take, the air becomes thicker.{w} Never mind the rust wafting around. I’ve been to meat shops and have already performed surgeries on animals, for goodness’ sake.{w} This is just another day."
    narr "However, I can’t shake that feeling...{w} the one when you’ve no control over your own body.{w} It might happen again, and at that time, I may no longer return.{w} No, not like a skin-walker,{w} but {i}something else{/i}."

    nvl clear
    narr "I’m at the center of the T-road.{w} Now where should I go, I wonder?{w} At the first fork, I took the right path.{w} It was a fifty-fifty, but it didn’t bother me that much.{w} Yet it left me curious."
    narr "{i}This{/i} leaves me curious too."
    narr "I can’t remember the exact details of the first fork.{w} Did it have a fixture over it?{w} No. I used my flashlight the whole time.{w} Even the floor looked different."

    nvl clear
    narr "But to be sure, I might as well invert my uniform.{w} Nothing in the breast pocket but the flashlight, anyway."
    narr "Wish anyone else wasn’t seeing me{w} – this is equivalent to blasphemy and is enough to kick me out.{w} Ah well, that takes care of the dirt."
    narr "{i}Invert{/i} it, not {i}reverse{/i} it, if I remember correctly."
    narr "Our uniform’s practically uncomfortable having the back side at the front, which makes it impossible to fasten the buttons behind.{w} If I am wrong, then the devil be damned.{w} {i}*sigh*{/i} If only I have a map of this place."

    window hide
    scene bg darkhallway3 with dissolve
    window show
    nvl clear
    narr "Thus, I’ve decided...{w} Let’s go left!{w} After a few steps, I shone my flashlight forward, its angle a little higher."
    narr "My feet stopped as I saw something obstructing the path."
    window hide
    scene bg eyesdark
    window show
    play sound sfx_static2
    narr "{b}*STATIC* *STATIC*{/b}"
    stop sound
    play music bg_echoesoftime loop fadein 1.0
    narr "There it is again.{w} How can this be more spontaneous than it already is?{w} Slowly... slowly... the beam raised its angle...{w} and it stopped."
    narr "The figure wasn’t staying put{w} – it made an effort to advance even one step.{w} Behind it is a trail, a liquid I cannot distinguish, coming from its legs.{w} No, the torso is wetter, but its hair is the worst.{w} It’s a mop."
    narr "Tattered clothes covering its body, a large stature and that darkened face...{w} those horns curved towards me.{w} {i}That{/i} I cannot mistake...{w} But!"

    nvl clear
    window hide

    unk "Who are you?!{w} What... what are... Did you...?"

    "It stopped in its tracks, returning a deathly glare at me.{w} Just like seeing a basilisk eye to eye, it petrified my whole body.{w} What must I do?!"

    stop music
    scene black
    "{i}Friend – Now’s not the time for questions.{w} I suggest you {b}RUN{/b}!!!{/i}"

    play music bg_controlledchaos loop
    scene bg darkhallway3 with dissolve
    "Without hesitation, I dashed towards the other direction.{w} My left ankle nearly snapped, but I maintained my balance.{w} There was no time to point the flashlight forward...{w} just keep going!"
    "My senses became numb. The thirst faded, replaced with the urge to run away.{w} What’s the point if I am to be mauled, anyway?{w} The buzzing returned,{w} becoming more intense as the creature closed the distance between us."
    "I don’t know how long this path is or where it will wind up, but I must get away.{w} Looking back, my efforts seem useless!"
    "Unless..."

    scene bg darkhallway3 nightmare with dissolve
    unk "Away with you!{w} Go find another prey to feed your appetite!"
    "{i}No...{w} wait... Stop! Come back!{/i}"
    "{i}No, keep moving! You’re almost there!{/i}"

    "It’s wishful thinking, but I doubt the flashlight is able to delay it.{w} To think that I used my only light source as a weapon..."
    "But then, I’ve lost all rationality already. What does it matter now?{w} Eh... Ehehehe... Ehehehehehehehehe..."
    play sound sfx_clang
    "{b}{i}*CLANG*{/i}{/b}"

    unk "OW!!!"

    "The resisting force shook my whole body and almost broke my nose.{w} No need for a second inspection{w} – a door!{w} The device beside it is now a proper keypad, with the buttons illuminating red."

    "{i}That hurt...{/i}"

    "Judging from the screen’s width, the lock requires a four-digit combination.{w} If I cannot recall one, I won’t even have time to brute force ten thousand numbers!{w} It’s closing in!"

    "{i}Wait up... {b}*GROAN*{/b} I’m not gonna hurt you{w} – I SAID!!!{/i}"
    unk "The numbers on the painting!"
    unk "How did the string go again?{w} 1{w}-3-4-7? Is that it?"

    "I had to give it a shot.{w} It must be!"
    "{i}Access Denied{/i}"
    "Blast it! It’s only a one-time use.{w} There has to be a second combination somewhere. In the generator room?{w} Ah! Why did I even throw the flashlight away?!"
    "If I just turn around..."

    unk "Ah!{w} You foul beast, stay away from me! By the power of Christ, begone from my sight! Back to the depths of Hell with you!"
    "{i}No... you don’t understand{w} – SUCH IMPUDENCE! {b}*GROWL*{/b}{w}{/i}"
    "{i}MORTALS LIKE YOU DESERVE TO DIE A CRUEL DEATH!{w} FOR THAT YOU’VE BEEN MADE A SACRIFICE,{w} A FACT YOU CHOSE TO IGNORE FROM THE START!{/i}"
    unk "What is that number?{w} Grrrr... Come on..."
    "{i}Come closer...{w} I know...{/i}"

    "If ever that poisonous voice would just shut up!{w} Wait! The code is at arm's reach now...{w} That’s it!"
    "With one last attempt, my fingers tapped in frantically,"
    "{i}1-6-6-5{/i}"
    "I’m not certain if the input is correct. I just wish...{w} Say the magic words, please..."
    scene black
    "{i}*BEEP*{w} {b}*CLANK* *HUM*{/b}{/i}"
    "Only about eight feet between us."
    "The metal doors opened faster than those I encountered before,{w} and even faster how I squeezed through it.{w} A hard slam on the other device was enough to force the door closed once more!"
    "And without changing positions, I looked around for any viable weapon."
    scene bg chemistrylab with fade
    "This is a fairly large room,{w} a Chemistry Laboratory to be accurate.{w} Four workstations, a wall lined with shelves, a fire cabinet, and a wardrobe for the lab coats."
    play sound sfx_clang
    "{b}*BUMP*{/b}"

    "{i}Let me in! – YOU OPEN THIS DOOR RIGHT NOW!{w} – He’s coming... He’s coming... He’s coming...{/i}"

    window show
    nvl clear
    narr "Ignoring its pleas, I immediately armed myself with the fire axe.{w} The next moments felt like an eternity{w} – each pounding became more violent and the creature grew in desperation."
    narr "There’s an unbolted door on the right.{w} It is the perfect escape route,{w} but what’s beyond it is unknown.{w} After all, there could be a malicious snare on the other side."
    narr "I will not take kindly to such things any longer!"
    narr "................................................"
    stop music fadeout 1.0

    play music bg_echoesoftime loop fadeout 2.0
    nvl clear
    narr "Finally, the disturbances ceased.{w} However, that’s no reason for me to lower my guard.{w} It could be waiting,{w} or rather, presently planning a fierce siege to this room.{w} In either case, I must hurry."
    narr "If the other door leads to the exit, then{w} it would be wise to bring some of these chemicals with me.{w} They can be used as evidence to track down my abductor's identity."
    narr "Never mind the other person{w} – somebody is after my skin.{w} Better get the authorities involved first."

    nvl clear
    narr "{i}The third applies if I don’t find you as a cadaver the next morning...{/i}"
    narr "Hang on. That’s the problem.{w} How {i}long{/i} have I been here?{w} Who in the world would operate a facility without having a {i}single{/i} clock in sight?{w} I can’t even estimate how much time has passed with all these bizarre occurrences."
    narr "{i}He’s coming... He’s coming... He’s coming...{/i}"
    narr "Then that means..."

    nvl clear
    window hide

    unk "At most twenty-four hours have passed, or at least daybreak has already happened!{w} That creature must not be lying then!{w} No, I mustn’t be swayed."

    window show
    nvl clear
    narr "Whatever the case, it’s needless to panic.{w} No way of telling if L.C. is serious or not.{w} Besides, what kind of drinks is he brewing here?{w} I propose a small supply of bottles to witches around the country – those of a shady variety."
    narr "I jest,{w} but the substances themselves are not so.{w} Random workstation – what do we have here?{w} Sumiko would be delighted to play with these{w} if he was present..."
    narr "There are various chemicals on the table; to name the common ones,{w} acetone, bicarbonate, salt, alcohol, and a few more.{w} Inside the drawers, I found a few more of interest,{w} or not."
    narr "First thing that came into sight is an ampoule of water{w} – clear, and opening it gave off a strong odor.{w} Chlorine-like but seems synthetic, not even close to that of a vitamin pill.{w} As for the taste..."

    nvl clear
    window hide

    unk "Hmmm... {i}*smack* *smack*{/i}{w} Ugh... Chlorine.{w} But why in a small container?{w} Ah, well. Not for swimming, I guess. {i}*chuckle*{/i}"

    window show
    nvl clear
    narr "Setting down the ampoule and continuing my search, I had found nothing else of interest{w} – no incriminating evidence against L.C.{w} There’s plenty of interesting points left to check."
    scene bg labdoor
    narr "...And I didn’t even bother to reinforce the door."
    narr "My heart sank, unable to think of anything...{w} except maybe to charge at it and off its head!"

    nvl clear
    window hide

    "{i}Wait!{w} You...{/i}"

    "The words almost escaped my tongue, \"Have you come to execute me?\"{w} Somehow, I felt the shadow as something familiar and the hostility absent."
    "Slowly... slowly...{w} it exposed itself."

    unk "Kirisaki,{w} You're alive!{w} But... how...?"

    play music bg_awkwardmeeting loop fadein 2.0
    show inoue noglass cry at Three2 with Dissolve(1.0)
    "Inoue Shinozaki, our class president.{w} She is the other person L.C. mentioned in his letter{w} – which means he has yet to arrive at this facility himself!{w} But the monster,{w} how come?"
    "She was dripping wet and leaving footprints on her path.{w} Poor girl was shivering...{w} If only I can find a cold medicine and a towel to comfort her."

    kk9 "I’m just as surprised as you are, maybe even more.{w} Ah! Inoue, come inside quickly.{w} It might still be there."
    hide inoue with Dissolve(0.2)

    "Without question, she closed the door behind her.{w} This time, we spent a minute reinforcing the door.{w} The wardrobe should be enough to seal the entrance."
    scene bg chemistrylab with dissolve
    "We sat down and savored our little reunion."

    show kyou sad2 at Three1 with Dissolve(0.2)
    show inoue noglass sad at Three3 with Dissolve(0.2)
    is4 "Perhaps you understand... What the hell even is this place?"
    kk9 "There are things I've witnessed beyond my comprehension,{w} things that aren’t even humanly possible."
    kk9 "Whoever’s responsible for this clearly knows us well{w} – trying to shatter our faith and ego at our most vulnerable state.{w} {i}*sigh*{/i} This is no ordinary psychopath we’re dealing with."
    show inoue noglass worried at Three3 with Dissolve(0.2)
    is4 "Only now you share my sentiments.{w} {i}This{/i} is the extent of our understanding.{w} Even with a superset of truths cannot do these away – otherworldly affairs.{w} Those aren’t even in the books!"

    show kyou serious2 at Three1 with Dissolve(0.2)
    "Amidst her speech, I pondered on what she said earlier.{w} It almost slipped my mind."

    show kyou serious talk at Three1 with Dissolve(0.2)
    kk9 "By the way, the first thing you’ve uttered is, \"You’re alive!\"{w} Did you happen to encounter a corpse resembling me?"
    show inoue noglass serious2 at Three3 with Dissolve(0.2)
    is4 "In the living quarters, or that’s what it seems to be.{w} Your face was smashed almost beyond recognition and neck pierced with twigs, if I recall correctly."

    hide kyou with Dissolve(0.2)
    hide inoue with Dissolve(0.2)
    "When I regained consciousness, I did feel a few stings around my neck,{w} with the most painful one at the back."
    "The poison must have taken its effect on me,{w} or maybe no longer.{w} It’s one thing to land face-first to a pot soil.{w} I’ve suffered but a scratch on my forehead, and it still stings."

    show kyou serious2 at Three1 with Dissolve(0.2)
    kk9 "You were the one knocking violently from the other end, weren’t you?{w} Why didn’t you answer?"

    show inoue noglass sadleft at Three3 with Dissolve(0.2)
    "Her eyes dropped, not knowing whether to feel shame or fear."

    show inoue noglass worried at Three3 with Dissolve(0.2)
    is4 "I hesitated, feared that there might something worse waiting on the other side.{w} Back in my cell, I felt like I was attacked.{w} It might’ve been all made up, but I clearly heard the words."
    show inoue noglass pissed at Three3 with Dissolve(0.2)
    is4 "{i}Don't breathe...{/i}"
    show inoue noglass angry at Three3 with Dissolve(0.2)
    is4 "And those sniggers!{w} My God, how could I even forget those? Who the hell brings their children in a place like this?!"
    show kyou worried at Three1 with Dissolve(0.2)
    kk9 "Children!{w} Could you elaborate?"
    show inoue noglass talk2 at Three3 with Dissolve(0.2)
    is4 "I’ve heard three distinct voices in my cell,{w} maybe more if you count everything.{w} One of them was definitely L.C., as I first heard his voice through a recording."
    show inoue noglass talk at Three3 with Dissolve(0.2)
    is4 "The remaining two sounded childish, one male and the other female."
    show inoue noglass cry at Three3 with Dissolve(0.2)
    is4 "The remaining two sounded childish, one male and the other female.{fast} Believe me, there’s no way I’m making it up!"
    show kyou confused2 at Three1 with Dissolve(0.2)
    kk9 "No worries.{w} We’ll try to distinguish between the real and the illusions later.{w} For now, let’s just lay everything together while we're here.{w} Escaping this facility is another priority."

    window show
    nvl clear
    narr "To my perception, approximately half an hour should have passed during our information exchange.{w} The circumstances surrounding our abduction sound similar and are downright chilling...{w} And both on the same day!"
    narr "The hellish experiences were nearly the same, too,{w} with both of us recall getting {i}killed{/i} at some point.{w} The thing is, has L.C. already executed us and this dimension is already Purgatory?{w} {i}THE{/i} Purgatory my Catholic friends occasionally mention?"
    narr "I would like to believe that, but{w} it would crush our hopes of getting out of here."

    nvl clear
    window hide

    show inoue noglass sadleft at Three3 with Dissolve(0.2)
    is4 "My family must be worried. {i}*hic*{/i} I just want to go home..."
    show kyou focusleft at Three1 with Dissolve(0.2)
    kk9 "I do, too.{w} And it appears our criminal will go after someone else.{w} For that, I feel that he’ll pick one of us – our batchmates, I mean."
    show inoue noglass angry at Three3 with Dissolve(0.2)
    is4 "Kirisaki!"

    show kyou confused at Three1 with Dissolve(0.2)
    "I clenched my fists in contempt, the first time I’ve done so in a long time.{w} L.C.... he better not lay a finger upon my brother.{w} He hasn’t done anything wrong."

    show inoue noglass serious2 at Three3 with Dissolve(0.2)
    is4 "The folks outside are in a commotion as we speak.{w} We can rely on their efforts, especially that of our friends.{w} If only we have a means to connect to the outside."

    show kyou confusedtalk at Three1 with Dissolve(0.2)
    "And so I thought, dropping my gaze to our feet."

    kk9 "Inoue,{w} may I ask you a favor?"
    show inoue noglass serious2 at Three3 with Dissolve(0.2)
    is4 "What is it?"
    show kyou sad2 at Three1 with Dissolve(0.2)
    kk9 "If I don’t come out of here alive – {i}that’s what he said, anyway{/i} – kindly check on my brother, will you?{w} I hate to say this, but rules are rules. {i}*sigh*{/i}"
    kk9 "You? Anything you wish to deliver?"

    show inoue noglass sadleft at Three3 with Dissolve(0.2)
    "Without glancing, I knew my words worried her.{w} I must’ve been rash, but it must be said."

    show inoue noglass sadcry2 at Three3 with Dissolve(0.2)
    is4 "I’ve nothing to think about.{w} My older brother is already on his way."
    kk9 "..."
    show inoue noglass sadcry at Three3 with Dissolve(0.2)
    is4 "Look, we received essentially the same message from L.C.{w} And from what we know, that bastard is coaxing us to murder each other.{w} We haven’t even seen the exit yet."
    show inoue noglass angrycry at Three3 with Dissolve(0.2)
    is4 "And damn the rules! He’s not even playing things fairly either, so why should we?{w} I know you respect the rules, Kirisaki, but this is one instance where we need to let loose.{w} You must realize that."

    "I didn’t answer her.{w} Out of confusion or loss of words, I cannot tell."

    show inoue noglass smilecry at Three3 with Dissolve(0.2)
    is4 "Proverbs 12:25."
    show kyou happyclosed at Three1 with Dissolve(0.2)
    kk9 "Pft...{w} He he... hehehe...{w} Ahahahahahahahaha!"

    show inoue noglass laughcry at Three3 with Dissolve(0.2)
    "She caught wind of my emotions, returning the unneeded favor I once gave her.{w} Inoue shared my laughter, removing some of my burden.{w} \"Kind words cheer the heart up.\""
    show inoue noglass proud at Three3 with Dissolve(0.2)
    show kyou calmleft at Three1 with Dissolve(0.2)
    stop music fadeout 1.0
    "The conversation provided enough room for relaxation."
    "I amused myself by learning to whistle which I, after a few lousy attempts, eventually resorted to humming.{w} Inoue sneaked in a few snorts.{w} It lightened up the mood even further."

    show inoue noglass talk2 at Three3 with Dissolve(0.2)
    is4 "Have you checked that door already?"

    "Her eyes were fixated on the unenforced door."

    show kyou serious smile at Three1 with Dissolve(0.2)
    kk9 "I have{w} for assurance.{w} I figured I needed to bring a few chemicals with me before going through...{w} For evidence."
    is4 "But he can’t afford to leave a mark, can he?"
    is4 "Besides, what knowledge do we have on the chemicals here?{w} Those of the common household variety, yes, but the Alkanes and other complicated substances we studied about in Chemistry?{w} We have yet to see their physical forms."
    show kyou serious surprisedtalk at Three1 with Dissolve(0.2)
    kk9 "That didn’t cross my mind, honestly.{w} Besides, the only oddball among those I found was{w} an ampoule containing water."

    show inoue noglass talk at Three3 with Dissolve(0.2)
    "She turned towards me."

    is4 "An ampoule, you say? Funny...{w} I saw some empty plastic bottles on the shelves.{w} Inside the drawer you were searching earlier?"

    show kyou surprised2 at Three1 with Dissolve(0.2)
    hide inoue with Dissolve(0.2)
    "I affirmed, and she searched the said drawer.{w} She thoroughly examined the lone ampoule's contents."

    is4 "Unlabeled. {i}*sniff* *sniff*{/i}{w} Smells like chlorine.{w} A sample of pool water, I think.{w} Nothing off about it."

    "Thereby confirming my observations. One more thing..."

    show kyou surprisedleft at Three1 with Dissolve(0.2)
    kk9 "Speaking of, the pool is at the opposite end of the corridor, isn’t it?{w} Do you, by any chance, have happened to encounter a creature?{w} Well-built and has curved horns on both sides of its head?"

    "She didn’t answer,{w} keeping her lips tight as she hid away the liquid in her skirt’s pocket.{w} She searched the shelves by herself,{w} herself noticeably indifferent to the task."

    show kyou worriedclosed at Three1 with Dissolve(0.2)
    kk9 "Forget about it. {i}*sigh*{/i} No, it is then."
    is4 "How did you know?"
    show kyou worried at Three1 with Dissolve(0.2)
    kk9 "Know what?"
    is4 "{i}That{/i}.{w} Don’t tell me you didn’t recognize it.{w} I never told you such a thing."

    "Something about her threw me off.{w} The chills she must’ve been feeling from being wet has transferred themselves to me,{w} albeit in a much lower temperature."
    "By this time, I had gotten used to the compressions in my head.{w} It looks as though the room itself contracted along with the sensations."

    is4 "I’m just glad it didn’t follow us inside.{w} Otherwise...{w} imagine the consequences.{w} That’s how the legend goes."

    show inoue noglass serious2 at Three3 with Dissolve(0.2)
    "She stopped her search. Probably the mere mention of it bothered her.{w} I wouldn’t dare ask{w} – she might snap if I do."

    show kyou confusedtalk at Three1 with Dissolve(0.2)
    kk9 "Hey. I haven’t asked you this yet.{w} The door we just came in through requires a keypad combination to unlock itself, right?{w} How did you figure out the combination?"
    kk9 "The paper must’ve been destroyed when –{nw}"
    show inoue noglass serious at Three2 with Dissolve(0.2)
    is4 "Here."

    "Without another word, she produced the paper strip,{w} soiled and soaked beyond writability."
    "Indeed, this is the same paper I found within the bonsai’s soil."

    show inoue noglass pissed at Three3 with Dissolve(0.2)
    is4 "I’ll be the one asking this time.{w} Short answers, no frills, please."
    show kyou confused2 at Three1 with Dissolve(0.2)
    kk9 "Uh... sure..."
    hide kyou with Dissolve(0.2)
    hide inoue with Dissolve(0.2)
    show inoue noglass pissed at Three2 with Dissolve(1.0)
    show inoue creepy serious at Three2 with Dissolve(0.2)
    play music bg_hazydisorientation loop fadein 1.0
    is4 "Do you exist?"
    kk9 "What's that for?"
    is4 "Do you {i}still{/i} exist?"

    "Of course, I do! What is the meaning of all this?!"

    kk9 "Definitely. Flesh, soul, and spirit.{w} If I were to return the question, do you?"
    show inoue creepy smile2 at Three2 with Dissolve(0.2)
    is4 "I do...{w} I don’t."
    kk9 "You’re not certain..."

    show inoue creepy smirk at Three2 with Dissolve(0.2)
    "She spun around wildly, facing me eye-to-eye.{w} Her face sparkled with delight, her teeth glinted despite their near-concealment, and head cocked to the right."
    "Inoue defied all restraints, expressing herself in a manner I couldn’t fathom what or how.{w} She never even went this far."

    is4 "I am Inoue Shinozaki, fifteen, and a student of Maria St. Claire Institute!{w} I could disclose a lot more details, but that would mean blabber to anyone who denies my existence."
    show inoue creepy smile at Three2 with Dissolve(0.2)
    is4 "What more proof do I need?! Tell me!!!"
    kk9 "Inoue...{w} I’m standing here in front of you, and you in front of me.{w} What do you mean by that?"

    "Retaining that grin, she lowered her eyes...{w} dead, cold eyes,{w} piercing enough to melt my heart’s barrier.{w} It managed to shorten my breath and hinder my thought process."

    kk9 "How did you find the time to read those books in the living quarters?{w} I’m amazed at your thinking prowess. Aren't you aware of the time limit?"
    show inoue creepy focusedpose at Three2 with Dissolve(0.2)
    is4 "What {i}time limit{/i}?{w} You're making things up, Kirisaki..."
    kk9 "I'm not.{w} Maybe you missed the detail?{w} Regardless, he could come at any time...{w} or maybe he has already arrived."
    show inoue creepy focused at Three2 with Dissolve(0.2)
    is4 "You don’t suppose?"
    kk9 "Just a hunch. Anything else?"

    show inoue creepy smirk at Three2 with Dissolve(0.5)
    hide inoue with Dissolve(0.5)
    "Satisfied, she flashed a grin before facing away from me,{w} towards the other door.{w} I couldn’t help but be wary at her sudden change in demeanor – jumping far too quickly within a short time span."
    stop music

    is4 "Darn. My meal’s gone cold.{w} But that’s fine... I guess..."
    kk9 "Hm? You were saying?"

    "Just as she turned the door knob, she took a long glance back..."
    "...to find a bladed weapon two feet away pointing at her face."
    play sound sfx_heartbeat loop
    show inoue creepy smirk at Three2 with Dissolve(0.5)
    "...to find a bladed weapon two feet away pointing at her face.{fast} It fueled her amusement, giggling as if it was a lollipop."

    kk9 "What’s so funny?"
    show inoue creepy smile2 at Three2 with Dissolve(0.2)
    is4 "{i}Hm. Hm. Hm.{/i} I’ve no need of that, Kirisaki.{w} I just took your words as they are; in fact, I’ve proven them {i}just{/i} now."

    "She shrugged it off, unaware that she entirely missed the point."

    show inoue creepy serious at Three2 with Dissolve(0.2)
    is4 "You’re the one who doesn’t comprehend."

    "What?!{w} But... but... how did she?"

    is4 "Listen to yourself.{w} What is presently running your thoughts is a toxin,{w} something even you cannot fight.{w} Trust me – we went through the same ordeal."
    show inoue creepy smirk at Three2 with Dissolve(0.2)
    is4 "Listen to yourself.{w} What is presently running your thoughts is a toxin,{w} something even you cannot fight.{w} Trust me – we went through the same ordeal.{fast} Hehehehe... Isn’t that right?"
    kk9 "Tch!"
    show inoue creepy focused at Three2 with Dissolve(0.2)
    is4 "Come on, Kirisaki...{w} embrace a bit of oddity for your own sake. Hehehehehehehe...{w} The outside is much weirder than we thought it was. How deranged can it get?"

    "................................................"
    stop music

    show inoue creepy smile2 at Three2 with Dissolve(0.2)
    is4 "Lower that thing. It’s unbecoming of you.{w} You’re already starting to look like a maniac, you know.{w} Slowly... slowly..."
    kk9 "On one condition.{w} Are {i}you{/i}{w} truly Inoue Shinozaki?{w} If not, then I've no reason to lower my weapon. You could be a mole for all I know."

    "Though speck-like in size, my own glare reflected in her eyes.{w} But she didn’t falter, leaving us both in a gridlock,{w} lasting long enough to have me realize how awkward this is."
    "No one{w} was willing to move."

    show inoue creepy serious at Three2 with Dissolve(0.2)
    is4 "Believe in whatever you wish to believe. I’ve made my point already."
    hide inoue with Dissolve(0.2)
    scene black

    play sound sfx_thud2
    "{b}{i}*THUD*{/i}{/b}"
    "No use being paranoid at this moment.{w} This is all according to the battle plan, one to keep us in the dark.{w} For now, I’ll trust everything as they are."
    "For now."

    show inoue creepy smile3 at Three2 with Dissolve(0.2)
    is4 "Back off!"
    kk9 "Humph!"
    hide inoue with Dissolve(0.2)

    window show
    nvl clear
    play voice sfx_clang
    play sound sfx_glass
    narr "{i}{b}*CRASH*{/b} *CLINK* *CLINK*{/i}"
    narr "The force was enough to slam myself to the wall... hard!{w} My head barely touched the shelves,{w} but the force sent glassware and other apparatus into a furious hailstorm to my head."
    narr "If I remember, some of the flasks contained chemicals{w} bearing a foul smell, sharp enough to damage my nose.{w} One of them felt like acid!"

    nvl clear
    window hide

    kk9 "{b}*WHEEZE*{/b} AAAAAAAAAHHHH!!!{w} It burns! Haa... Haa... It burns! Gah...! {i}*whimper* *whimper*{/i}"

    window show
    nvl clear
    narr "My face is covered with a hot blanket,{w} dripping liquid akin to a newly-cooked broth.{w} It damaged my nerves and probably derailed my mind to a state beyond repair."
    narr "Somebody...{w} anybody!{w} Wipe this off me...!"

    nvl clear
    show inoue creepy blank at Three2 with Dissolve(0.2)
    narr "{i}You made a fateful mistake.{/i}"
    narr "{i}That’s what you get for doubting a truth that’s blatantly exposing itself to you.{w} Like sheep, you follow your God as if you’ve truly seen him in person!{w} And yet...{w} this?!{/i}"
    narr "{i}You believe more in the things that YOU CANNOT SEE yet ONLY FEEL?{w} Eat your words, Kirisaki.{w} \"A man ought not to remove a speck on another’s eye when he himself has a slab on his own.\"{/i}"
    narr "{i}What’s the problem, fanatic? Regret having a blind faith?{/i}"
    show inoue creepy smirk at Three2 with Dissolve(0.2)
    play sound sfx_giggle
    hide inoue with Dissolve(1.0)
    narr "The disembodied voice came out of nowhere, rubbing the pain into me...{w} {b}{i}*Ack!*{/i}{/b}"
    narr "So what if I did?{w} This punishment has gone too far!"

    nvl clear
    narr "I’ve been dragged by the feet...{w} to someplace I’m unsure of.{w} The acid forced my eyes shut and my ears rang indefinitely.{w} Everything else became limp..."
    narr "...and the only thing active is my own consciousness."
    play sound sfx_doorknob
    play sound sfx_dooropen
    narr "A door opening...{w} and another...{w} The sound of metal clanking amongst themselves...{w} Glass toppled to the ground...{w} A bump on my side, with someone rolling me over and posturing my body straight."
    narr "The same person ran everywhere,{w} breathing ceaselessly as she opened cupboards, looking for supplies to aid my injury.{w} Every bump she caused synced well with the loud throbs of my heart."
    window hide
    scene bg clinic with fade
    window show
    narr "My vision slowly recovered from the blur,{w} drawing the figure of Inoue near the bed.{w} She was crying."
    show inoue noglass cry at Three2 with Dissolve(0.2)

    nvl clear
    window hide

    is4 "Don’t speak! It’ll take just another minute."
    hide inoue with Dissolve(0.2)

    window show
    nvl clear
    narr "She laid the apparatus on the small counter and brought my head carefully to the sink.{w} Clearly, she was trying to maintain her cool,{w} all while struggling to rotate the handle."
    narr "And then I saw{w} from inside the spout,{w} a black tube occupying the whole interior.{w} My eyes widened in shock."

    nvl clear
    window hide

    kk9 "Inoue...{w} wait..."

    "She had already turned the handle.{nw}"
    scene bg fire
    play sound sfx_fire
    "{b}*WHOOSH*{/b}{nw}"
    play sound sfx_fire3
    "{i}{b}GAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHH!!!!!!!{/b}{/i}{nw}"
    "{i}{b}IT BURNS!!! IT BURNS!!! HAAAAAAAA!!!!{/b}{/i}"

    play music bg_ringaroundtherosie loop
    window show
    nvl clear
    narr "{i}Ring around the rosie...{w=6.0}\nPocket full of posies...{w=6.0}\nAshes...{w=2.0} ashes...{w=2.0}\nWe all fall down...{/i}"
    play audio sfx_fire2 loop
    narr "Circling...{w=0.25} circling...{w=0.25} vision circling...{w} The chaotic blaze let a thousand tongues lick my face, down to my feet.{w} Not long, it engulfed my whole body."
    play sound sfx_giggle
    play sound sfx_giggle
    narr "The rhyme went on and on, repeating itself endlessly...{w} The sound of children laughing,{w} mocking my misery."
    stop music

    nvl clear
    play sound sfx_giggle
    narr "{i}Ring around the rosie... *giggle* *giggle*{w=5.5}\nPocket full of posies...{/i}{w=6.0}{nw}"
    narr "{i}A’tishoo! {b}*hiss*{/b}{w=2.0} A’tishoo! {b}*hiss*{/b}{w=2.0}\nWe all...{w=1.0} fall...{w=1.0} down...{w=1.0} *giggle* *giggle* {b}*cackle* *cackle*{/b}{/i}"
    stop music
    play sound sfx_giggle
    play sound sfx_giggle
    play sound sfx_giggle
    narr "{i}Hahahahahahahahahahaha!{/i}"
    narr "................................................"
    narr "{i}Hush! Hush!{w=1.5} Hush! Hush!{w=1.5}\nAnd all...{w=2.0} fell down...{/i}"
    stop sound

    nvl clear
    window hide
    return

label ch01_16_death01:
    scene black with dissolve
    "Date Unknown - Time Unknown"
    play music bg_corruption loop
    play sound sfx_fire2 loop
    "Kirisaki!{w} No!{w} What have I...{w} what have I done...?"
    "I was only trying to help.{w} How has it come to this?{w} If it weren’t for...{nw}"

    scene bg fire
    kk9 "Ugh... AAAAAAAHHHH!!! {b}*EXHALE*{/b} AAAAAAAAAAHHHHH!!!!!!!{fast}"

    window show
    nvl clear
    narr "The blast almost sent me flying{w} and one of the marble counters nearly impacted my spine.{w} Not just that, but my right ankle was sprained badly.{w} Had the glassware come crashing down, I would’ve suffered even greater damage."
    narr "Those alone are excessive."
    narr "Back home, we used to watch people getting slaughtered{w} – regardless of the genre – in ways only a camera and a skillful director can deliver."
    narr "But right now, the scene isn't inside the TV nor projected onto a theater screen.{w} What’s in front of me is live, no camera tricks.{w} No one to say, \"Cut!\" and extinguish the flames, with the actor getting up afterwards like it was nothing."
    narr "And I’m not seeing things either."

    nvl clear
    narr "My lip nearly bled from my teeth's pressure;{w} if it were my tongue instead, it could have been worse.{w} This is not even comparable to the moments that led up to this.{w} Even death was an illusion,{w} or perhaps not?"
    narr "This is the reality I became accustomed to,{w} the one where we all linger in.{w} I have to accept it – this is{w} a waking nightmare."
    narr "And as helpless as the victim is, {i}I{/i} am too.{w} Soon, the bellowing tongues would reach my position and consume me wholly with Kirisaki.{w} Such an ingenious way to open Hell’s portal,{w} within a dimension of Hell itself!"
    narr "The blaze and agonized screams filled the air, thick smoke blackening the field of vision.{w} I’ve no intention to get up;{w} I lost my will’s totality.{w} Someone is dying in front of me – because of me{w} – and all I have to do is wait..."
    narr "Just... wait..."

    nvl clear
    narr "{i}Then all your suffering shall be pointless.{/i}"
    narr "Damn you...{w} You could’ve spared us the torture and offed our heads instead, you freak!{w} My brain can no longer feel, numb to everything perceivable around me."
    narr "You{w} and your stupid little brats..."

    nvl clear
    narr "{i}He dies for nothing;{w} you shall die for nothing.{w} It will just make things harder for everyone.{/i}"
    narr "{i}And what about YOUR family?{w} Today, they weep, and they’ll weep even harder when they find your corpse the next evening.{w} Can you stomach that?{/i}"
    narr "{i}Kyou Kirisaki has already been done with,{w} which means he loses, plain and simple.{w} Rules are rules, young lady.{w} I need not reiterate our deal in the beginning. You remember them well, I suppose,{w} especially the conditions for your escape.{/i}"
    narr "{i}I’ll be waiting outside – that is, if you don’t decide to end your life there.{w} Death by fire is agonizingly slow, so take the second option.{w} There's a gun in the next room, thought I let you know.{/i}"
    narr "{i}Until then...{w} This won’t be our last meeting,{w} Inoue Shinozaki.{/i}"

    nvl clear
    window hide

    play audio sfx_doorknob
    play audio sfx_doorknob
    play audio sfx_dooropen
    "{i}*RATTLE* *RATTLE*{w} {b}*WHOOSH*{/b}{/i}"

    play voice sfx_breathing
    is4 "Haa... Haa... Haa...{w} {i}*gulp*{/i} Haa..."

    scene bg chemistrylab
    window show
    nvl clear
    narr "In the entire duration of his monologue, I managed to limp to the lab door."
    narr "One of these cabinets might be hiding an explosive.{w} Kirisaki would be displeased if his body is blown to pieces.{w} Imagine the trauma it would inflict upon his family,{w} especially his poor brother."
    narr "The flames have already consumed him whole.{w} His body ceased convulsing and can only utter moans at best.{w} Kirisaki’s anguish is at end,{w} but the flames are not{w} – I am not yet safe."
    narr "Inside the fire cabinet is a water hose, a fire blanket, and an empty extinguisher.{w} The water isn’t running – I checked beforehand.{w} Fire blanket in hand, I returned to the clinic."

    scene bg fire with dissolve
    nvl clear
    narr "The closer I move to Kirisaki’s bed, the more my eyes redden due to the violent smoke.{w} I stopped just a few feet away from the flames."
    narr "Pull the strings...{w} cover the body tight.{w} Wrap it tightly enough, leaving no flame astray.{w} Get back."
    stop sound
    stop music fadeout 1.0

    scene bg clinic with fade
    nvl clear
    narr "A long time has passed."
    narr "Kirisaki remains motionless.{w} A pulse check is unnecessary – the damage is too extensive for him to survive.{w} When the blanket matched his body temperature, I removed it and examined him."

    nvl clear
    narr "Kirisaki has suffered third-degree burns; most of his upper body has been charred.{w} His glasses have melted on his eyes,{w} and the eyeballs themselves oozed down the tear ducts.{w} It turned to {i}condensed milk{/i}."
    narr "His head gave off a sulfurous, or rotten, smell,{w} having only a few strands of hair left.{w} Some of his bones stung my skin, fresh off of burning.{w} Only little of his uniform remained, with the pants and the leather shoes especially intact."
    show inoue noglass blood sad at LS with Dissolve(0.2)
    narr "This is my first corpse,{w} long before I conceive my medical degree.{w} Even Papa would praise me for braving it.{w} A charred corpse is not a daily case he would sometimes bring home to share with us."
    narr "I covered him once again,{w} bearing no longer to see him like this..."

    nvl clear
    window hide

    "{i}{b}*THUD*{/b}{/i}"

    show inoue noglass blood cry at LS with Dissolve(0.2)
    is4 "{i}*SOB*{/i} ...Uhu...{w} {b}*EXHALE*{/b} Uhuhuhuhuhuhu......"

    window show
    nvl clear
    narr "I lay at the bedside, letting it all flow.{w} Once everyone finds out about this, what are they going to think of?{w} The reputation of our institution...{w} {i}tarnished{/i}!"
    narr "However, what do I care about reputation?{w} The police will eventually track him down, right?{w} Hehehehe... Simply not elementary, dear girl!{w} Remember Sacred Heart? It was a dead-end case!"
    narr "But I, Inoue Shinozaki,{w} have {i}lived{/i} to tell the tale...{w} the tale of a maniac who forced upon us a deadly game,{w} and I’ve won!{w} Hehehehehehehehe. What luck!"
    narr "It doesn’t end there.{w} All this chaos led me to forget my hunger and thirst.{w} What am I to vomit? Air?"

    nvl clear
    narr "From within the blur, I managed to glimpse a tiny glimmer.{w} A key!{w} It could well fit into that other door."
    narr "I picked myself up, having partially healed from my injuries earlier."
    narr "Yet would I leave a friend behind?"

    nvl clear
    window hide

    show inoue noglass blood sad at LS with Dissolve(0.2)
    is4 "Goodbye... Kyou..."

    "We shall see each other again...{w} or maybe not."
    hide inoue with Dissolve(0.2)
    scene bg longhallway with fade

    window show
    nvl clear
    play sound sfx_footsteps3 loop
    narr "As I walk this empty corridor, I could think of nothing.{w} My feet heaved my body towards the other end.{w} My whole being transformed itself to that of a robot, utterly devoid of any human emotion."
    narr "Footsteps and gasps echoed around the walls.{w} Nothing special about it."
    stop sound

    nvl clear
    play sound sfx_dooropen
    narr "Without regard, I shut the door behind me,{w} and looked around the new environment."
    window hide
    scene bg receptiondesk with fade
    window show
    narr "Across the reception desk is another enforced door with a device.{w} The LCD screen grabbed my attention."
    narr "{i}1...{w} 1...{w} 1...{/i}"
    narr "The number displayed itself endlessly."

    nvl clear
    narr "With the last remnant of curiosity, I approached the door.{w} The synthetic female voice spoke the magic words once I'm within three feet."
    narr "{i}Access Granted.{/i}"
    narr "Without effort, I walked through another puzzle – one that I find nonsensical.{w} The metal bars slowly lowered and the mechanical locks undid themselves."

    nvl clear
    window hide

    "{b}*CLANK*{w} *HUM*{/b}"
    "Only this time, at the other end..."
    scene bg darkhallway2 with dissolve
    "Daylight..."

    play sound sfx_footsteps3 loop
    "{i}{b}*STEP* *STEP* *STEP*{/b}{/i}"
    "............................................."
    "{i}{b}*step* *step*{/b} *step* *step* *step*{/i}"
    scene black with dissolve
    "............................................."
    stop sound
    play sound sfx_thud2
    "{b}*THUD*{/b}"
    return

label ch01_17_facts2:
    scene black with fade
    "JUNE 24, 2013 - 1645H"
    "Six days{w} – the amount of time passed since Kyou Kirisaki and Inoue Shinozaki’s disappearance.{w} Six days of anxious waiting,{w} even a call or letter for ransom would have sufficed."
    "Alas, none of those surfaced."
    scene bg msci evening with fade
    show sayo seriousnormal at Eight3 with Dissolve(0.2)
    "As she left, Sayo gave instructions to Ayumi not to let the cleaners surpass 5:30PM.{w} The students were issued a new order, reducing the curfew time by thirty minutes."
    show akira proud2 at Eight6 with Dissolve(0.2)
    show hiroshi smile at Eight7 with Dissolve(0.2)
    "She passed by Akira, who was chatting with Hiroshi at IV-B’s bench."
    hide akira with Dissolve(0.2)
    hide hiroshi with Dissolve(0.2)
    show miyu pissedclosed at Eight5 with Dissolve(0.2)
    "She passed by Akira, who was chatting with Hiroshi at IV-B’s bench.{fast} Just then, Miyu exited his classroom, exhausted as usual."

    show sayo serioustalk at Eight3 with Dissolve(0.2)
    sr5 "Do you have a minute?"
    show miyu talk at Eight5 with Dissolve(0.2)
    mh8 "Eh, what?{w} Me?"

    "Sayo turned her head, confirming his question silently.{w} Unable to refuse, he looked at her and slightly grinned."

    mh8 "Anything of concern, Sayo?"

    "She motioned him to the stairs across IV-A."
    hide sayo with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    scene bg school hallway with dissolve
    show sayo seriousnormal at Three3 with Dissolve(0.2)
    show miyu bored at Three2 with Dissolve(0.2)
    "She motioned him to the stairs across IV-A.{fast} They sat down at the fourth step and engaged in a discreet conversation."

    play music bg_decline loop
    show sayo normaltalkleft at Three3 with Dissolve(0.2)
    sr5 "You’re familiar with Tomonori Shinozaki, right? Inoue’s brother two batches up?"
    show miyu confused at Three2 with Dissolve(0.2)
    mh8 "I remember the fellow. He was part of the honor roll and the Top 10."
    show miyu serious at Three2 with Dissolve(0.2)
    mh8 "I remember the fellow. He was part of the honor roll and the Top 10.{fast} Wait,{w} did he speak of any developments about the case?"
    show sayo normaltalk at Three3 with Dissolve(0.2)
    sr5 "You could say that,{w} but this is more of a mere {i}concern{/i} than anything...{w} something that disturbs me to this day."

    "Thoughts raced to his mind, trying to deduce what she meant."

    show sayo serioustalkleft at Three3 with Dissolve(0.2)
    sr5 "He rang me up last Saturday.{w} I found it odd if it was about Inoue{w} – I mean, they are the primary contacts for the case, after all.{w} Instead, he talked to me briefly and asked me..."
    show sayo serioustalk2 at Three3 with Dissolve(0.2)
    sr5 "...if I was the one who set her up."
    show miyu happytalk at Three2 with Dissolve(0.2)
    mh8 "Absurd! Why would he make such an accusation?{w} Don’t tell me he’s resorted to random finger-pointing."
    show sayo upset at Three3 with Dissolve(0.2)
    sr5 "Of course, I got ticked off. Initially, at least."
    sr5 "On June 13, the Shinozakis received a call intended for Inoue.{w} He knew because Inoue confided the details of the exchange to him two days after."
    show miyu bored at Three2 with Dissolve(0.2)
    mh8 "Let me guess...{w} You’re the caller?"
    show sayo upsetcry at Three3 with Dissolve(0.2)
    sr5 "Yes, and I was being accused of blackmail.{w} I wanted to forgo my manners and explode on him!"
    show sayo worriedtalkcry at Three3 with Dissolve(0.2)
    sr5 "Yes, and I was being accused of blackmail.{w} I wanted to forgo my manners and explode on him!{fast} {i}*sniffle*{/i} I’m sorry, Miyu..."

    hide sayo with Dissolve(0.2)
    "She fished inside her backpack for a tissue, wiping her tears in frustration.{w} Miyu wanted to pat her back, but he stopped himself, thinking it would look awkward."

    show sayo normaltalk at Three3 with Dissolve(0.2)
    sr5 "Here we go. {i}{b}*BREATHE*{/b}{/i}"
    show sayo seriousnormal at Three3 with Dissolve(0.2)
    sr5 "You know, Inoue did mention something about the incident at Sacred Heart.{w} I told her to forget about it – she was visibly anxious.{w} It's her curiosity that's been giving her the edge."
    sr5 "Supposedly, {i}I{/i} called her that night, {i}Thursday night{/i}, to give the complete details of the incident.{w} Additionally, {i}I{/i} made her head spin by some philosophical terms even I can’t comprehend."
    mh8 "To be fair, you do have a penchant of speaking in riddles."
    show sayo seriousclosed at Three3 with Dissolve(0.2)
    sr5 "{i}Formal language{/i}, not riddled speech. Those are of two different levels, Miyu."
    show miyu worried at Three2 with Dissolve(0.2)
    mh8 "No offense, Sayo. I genuinely appreciate being a faucet for your concerns, but{w} why me?{w} Have you already spoken to Mrs. Genkai about this?"
    show sayo seriousnormal at Three3 with Dissolve(0.2)
    sr5 "Oh, I did,{w} just in case anything against me comes up.{w} For your first question..."
    stop music fadeout 1.0
    show sayo smileopen2 at Three3 with Dissolve(0.2)
    sr5 "Oh, I did,{w} just in case anything against me comes up.{w} For your first question...{fast} Well, let’s just say you’ve got this \"particular set of skills\" and whatnot..."
    show miyu naughty blush at Three2 with Dissolve(0.2)
    mh8 "{i}{b}*SNORT*{/b}{/i} I’m no spy!"
    show sayo smiletalk at Three3 with Dissolve(0.2)
    sr5 "No. No. You misunderstand.{w} She meant something else."
    show miyu focusedpose at Three2 with Dissolve(0.2)
    mh8 "She?{w} Wait a minute..."
    show miyu happytalk at Three2 with Dissolve(0.2)
    mh8 "She?{w} Wait a minute...{fast} {i}*GASP*{/i}{w} What did Hikaru tell you about me?!"
    show sayo smileopen at Three3 with Dissolve(0.2)
    sr5 "You have an affinity for the supernatural, haven’t you?{w} Or, let’s be more grounded.{w} Detective work, perhaps?"
    show miyu embarassed at Three2 with Dissolve(0.2)
    mh8 "What? Ahahahahaha!{w} I’m in no position for that, Sayo.{w} This isn’t a random flash game on the internet, we’re dealing with real crime here."

    "Ikuko and Ayumi passed by, the latter giving Sayo a thumbs up."
    show sayo smiletalk at Three3 with Dissolve(0.2)
    show miyu naughty smile at Three2 with Dissolve(0.2)
    "They continued their conversation up until the sun was beginning to set."
    "Miyu glanced at his watch,{w} noting the time to be 5:20PM."

    show sayo normaltalk at Three3 with Dissolve(0.2)
    sr5 "Oh! My apologies for delaying you."
    show miyu naughty smirk at Three2 with Dissolve(0.2)
    mh8 "Nah, don’t worry about it.{w} I found the exchange rather informative, and I do find your case {i}intriguing{/i}."
    show miyu naughty talk at Three2 with Dissolve(0.2)
    mh8 "Well, I better get going, then.{w} Hope to see you tomorrow, Sayo."
    sr5 "If ever, shall we discuss this over at break time?"
    show miyu smile at Three2 with Dissolve(0.2)
    mh8 "Hmmm... I’ll see what I can do with my schedule.{w} And if ever, you know where to find me."

    hide miyu with Dissolve(1.0)
    show sayo blankface at Three3 with Dissolve(0.2)
    "His figure disappeared around the corner.{w} Sayo silently contemplated for a while, before rising to go home herself."

    ikuko "{i}Hey, Miyu! Someone’s looking for Sayo in the office.{w} Is she still there?{/i}"

    show miyu naughty smile at Three2 with Dissolve(0.5)
    "He promptly peeked around the corner of the staircase.{w} Miyu silently motioned her to the principal’s office, which she acknowledged with an O.K. sign."
    hide miyu with Dissolve(0.5)
    hide sayo with Dissolve(0.2)
    "She hastened her steps, entering the office in a practiced manner.{w} The secretary guided her to the principal’s room, its interior visible through the glass door."
    scene bg principalsoffice with dissolve
    "Accompanying Mrs. Sokoguchi, the principal, are two men of authority."
    show emmerich serious at RS with Dissolve(0.2)
    "The middle-aged man is a police sergeant.{w} He currently handles the case, one he considers a higher caliber than those he handled before.{w} With him, a much younger protégé.{w} Meek, as he would look from the surface."

    p_serg "And to complement my age, I have with me an aide, younger and more robust than I am.{w} Isn’t that right, rookie? Gahahahahahaha..."
    show emmerich seriousclosed at RS with Dissolve(0.2)
    p_insp "Please,{w} refer to me as Emmerich...{w} not that I don’t mind, Sarge."
    p_serg "A diamond in the rough, I tell ‘ya.{w} He may be brusque, but he’s got the right mindset. Saw myself in ‘im.{w} Figured I might as well tag him along instead of being cooped up in that lab."
    show emmerich serious at RS with Dissolve(0.2)
    p_insp "Ah, yes. My first case in the field, this,{w} and a pretty bad apple for –"

    play sound sfx_knock
    "{i}{b}*knock* *knock* *knock*{/b}{/i}"
    "Seeing who is behind the door, the principal motioned Sayo to come inside.{w} The two men turned their attention to her, who slowly entered the room."
    show sayo smileclosed at LS with Dissolve(1.0)
    "The council president showcased her dignity, making her presence well-known before the two gentlemen.{w} Hand in heart, Sayo bowed down to an almost-right angle."
    show sayo smileopen at LS with Dissolve(0.2)
    "Sayo exchanged handshakes with the guests and settled down to the empty seat across them."

    prin "Then if we may, let us formally start our meeting."
    prin "Ms. Ronoroa is the incumbent council president, dear gentlemen.{w} Sayo, these are the two men I’ve told you and Mrs. Genkai about."
    sr5 "I see.{w} How are things, Sergeant?"
    p_serg "We’ve traced the call to the Shinozakis.{w} If witness accounts are accurate, the estimated duration is one hour starting at 1900H.{w} Source is a phone booth at the north end of the market."
    show sayo serioustalk2 at LS with Dissolve(0.2)
    sr5 "Market?{w} I was already away from Kutsutochi by seven."
    show emmerich talk at RS with Dissolve(0.2)
    p_emm "We’ve not confirmed anything yet, Ms. Ronoroa –"
    show sayo seriousnormal at LS with Dissolve(0.2)
    sr5 "Sayo, Inspector. I prefer it.{w} No need to worry. You haven't caused any offense."
    p_emm "Right.{w} As to that extent, we only have the witness’ word for it.{w} Same goes for you – circumstantial evidence at best."
    show sayo seriousnormalleft at LS with Dissolve(0.2)
    sr5 "Then I am at ease.{w} What about the Kirisakis?"
    show emmerich serious at RS with Dissolve(0.2)
    p_emm "Zero."
    prin "I shall answer that.{w} Kyou Kirisaki’s brother is still ordered to stay home until we find out his current condition.{w} Unlike the other family, they do not fault you nor do they suspect any one of his friends."
    show sayo serioustalkleft at LS with Dissolve(0.2)
    sr5 "Kyou has no enemies to my knowledge.{w} That kid is an optimist and genuinely cares for his schoolmates."
    show sayo serioustalk2 at LS with Dissolve(0.2)
    sr5 "And his presence is required, especially with the upcoming activities.{w} Without the Science Club’s head, the members are falling into confusion."
    p_serg "So he’s the club president, you say.{w} Could the motive be political?"
    show sayo worriedtalk at LS with Dissolve(0.2)
    sr5 "Dear, no!{w} The acting president, Tokubei, is a legitimate leader.{w} He actually didn’t want to accept the position because he's already holding similar duties at his homeroom."
    sr5 "We have yet to make formal arrangements should anything arise.{w} It seems that the most viable option is to wait."
    show emmerich seriousclosed at RS with Dissolve(0.2)
    p_emm "With lack of physical evidence, then, we arrive at another dead end.{w} How exciting for a field entry..."

    "The sergeant pat the young inspector's back, sympathizing with him."
    "The discussion continued until six,{w} at which the principal allowed Sayo to leave five minutes early.{w} The sergeant spoke for them both, promising an update within 24 hours{w} – if there ever will be."
    hide sayo with Dissolve(0.2)
    hide emmerich with Dissolve(0.2)
    return

label ch01_18_aftermath:
    scene black with fade
    "JUNE 25, 2013 - 1800H"
    window show
    nvl clear
    narr "But the twenty-four hours passed without another lead."
    narr "The sun’s rim is the only part visible on the horizon, giving way to the night.{w} Just as peaceful as the crickets were making it seem,{w} everyone at Maria St. Claire has agreed to be coy about the abductions, with parents joining in.{w} Thus, it was considered an {i}isolated case{/i}."
    narr "With the appearance of Emmerich and Sergeant Deitch – two from the regional police{w} – this was no longer the case.{w} Police visibility increased throughout Kutsutochi and its surrounding municipalities and cities."
    narr "Newsflashes broadcasted the case’s details despite efforts to bar the media’s involvement.{w} But the school officials switched sides after receiving no significant updates from the local authorities.{w} They deemed the move necessary lest they get detracted upon by mindless keyboard-wielding zombies."

    scene bg wetmarket night with fade
    play sound sfx_street loop
    nvl clear
    narr "Yoshiro escorted his girlfriend home as usual, passing by the wet market on the way.{w} Blue-uniformed men were occasionally seen patrolling the streets,{w} asking for information or keeping an eye around the area."
    narr "Somehow, it still did not feel safe.{w} His girlfriend held tightly, watching for any intruder they might come across.{w} They made it past the market,{w} through the small park at the North,{w} and finally to her home."
    narr "They exchanged hugs as they parted ways, urging Yoshiro to take care and to keep his mind sharp.{w} She locked the gate, and he scurried off the way they came."
    stop sound

    scene bg alley with dissolve
    nvl clear
    narr "Yoshiro passed by a narrow street resembling that of another in Vigan.{w} One of the houses resides an old comedian, with his image proudly plastered on the banner on his front door."
    narr "Before turning the corner is an art studio,{w} decrepit on the surface but still a popular entrepreneurial establishment."
    narr "People are fascinated by the artist, the one sitting on a stool in front,{w} and his unconventional style.{w} His style and eccentricity combined rings a familiar tune,{w} a homage to Van Gogh or even Francis Bacon to some."
    narr "Nevertheless, Yoshiro finds his appearance weird and quickens his pace whenever he passes by the shop.{w} The sight of it gets on his nerves easily,{w} especially the artist."
    scene bg eatery with dissolve
    narr "As he emerged from the alley, he saw a familiar face on one of the eateries on his left."

    nvl clear
    window hide

    show emmerich smile at Three2 with Dissolve(0.2)
    p_emm "Oi! You’re a familiar chap.{w} Would you come sit with me for a moment?"
    hide emmerich with Dissolve(0.2)

    show emmerich smile at Three1 with Dissolve(0.2)
    show yoshiro serious at Three2 with Dissolve(0.2)
    "Yoshiro felt an odd sense of security, immediately taking a seat beside the inspector.{w} The latter ordered some refreshments, which Yoshiro accepted."

    show yoshiro serious2 at Three2 with Dissolve(0.2)
    ys6 "You must be one of the primary investigators of the case.{w} Sayo mentioned you this morning. Sayo Ronoroa, I mean."
    show emmerich smirk2 at Three1 with Dissolve(0.2)
    p_emm "Ms. Ronoroa did?{w} Delightful. {i}*chuckle*{/i}{w} Old Man Deitch is with the other squad, somewhere at the boundary as we speak..."

    "The soft drinks arrived and the inspector paid his bill to the waitress."

    show emmerich smileteeth at Three1 with Dissolve(0.2)
    p_emm "My mistake!{w} Emmerich, Harold Emmerich."

    show yoshiro smile at Three2 with Dissolve(0.2)
    "Emmerich reached out his hand, and Yoshiro answered.{w} The two men pumped their hands warmly, solidifying their trust."

    show yoshiro surprised2 at Three2 with Dissolve(0.2)
    ys6 "Yoshiro Suzuki.{w} You don’t seem to match her description, do you?{w} I expected a firmer guy."
    show emmerich smirkleft at Three1 with Dissolve(0.2)
    p_emm "You speak of my senior, the one I mentioned earlier.{w} Sergeant Deitch and I might need a formal introduction to you students. Hahahahahaha.{w} But you know..."
    show emmerich smile2 at Three1 with Dissolve(0.2)
    p_emm "It’s all part of the trade.{w} ‘Ya sometimes gotta learn to be an actor to gain your respect, as my mentor puts it. {i}*wink*{/i}"
    p_emm "This is my first case, Mr. Suzuki.{w} Don't be surprised if I'm referred to as \"rookie\"."
    show yoshiro smirk at Three2 with Dissolve(0.2)
    ys6 "Oh, I see.{w} I dare not protest then...{w} {i}rookie{/i}."
    show emmerich smirk at Three1 with Dissolve(0.2)
    p_emm "Hahahahaha! That’s enough, you.{w} I can see potential, how far your wit can bring you, Mr. Suzuki."
    ys6 "Just Yoshiro. It’s amusingly mouthful for you. Hm. Hm. Hm."
    show emmerich smile at Three1 with Dissolve(0.2)
    p_emm "Right, right.{w} Then I’ll just refer to you and your classmates on a first-name basis. A tradition or a friendly habit, perhaps?"
    p_emm "Anyway, my squad mates are conducting a search elsewhere,{w} while I excused myself to think.{w} I first worked in the lab, analysis mainly, so that gives me a valid excuse."

    show emmerich serious at Three1 with Dissolve(0.2)
    show yoshiro serious at Three2 with Dissolve(0.2)
    play music bg_vulcan loop
    "He showed his little notebook to Yoshiro{w} and explained the clues and witness statements he gathered, including the connections he derived from them."

    show emmerich talk at Three1 with Dissolve(0.2)
    p_emm "Do you notice a pattern?"
    ys6 "Zero evidence equals zero leads, including any traces of the crime itself.{w} If there ever was, the perpetrator must’ve surfaced by now."

    "Emmerich nodded,{w} suggesting to Yoshiro a certain point."

    show yoshiro worried at Three2 with Dissolve(0.2)
    ys6 "You mean any search attempts were purposefully made useless{w} and that you were meant to be called on purpose?"
    show emmerich serious at Three1 with Dissolve(0.2)
    p_emm "Exactly."
    show yoshiro worriedleft at Three2 with Dissolve(0.2)
    ys6 "Odd.{w} And I thought criminals prefer to lay low.{w} Unless..."
    p_emm "Unless he is willing to show himself or he's showing off his work {i}purposely{/i}.{w} You know how these types work.{w} Is there anyone you know who might be of concern?"

    "Yoshiro pondered for a moment, remembering the details involving Kyou and Inoue:{w} anyone who had a previous conflict with the two,{w} what their daily schedules are, and all."
    "He only shook his head."

    show yoshiro surprised2 at Three2 with Dissolve(0.2)
    ys6 "Have you checked any outside contacts?{w} Relatives, old friends?{w} Personally, I find no fault in Kirisaki{w} – it’s hard to imagine him in a fight."
    show yoshiro talkleft at Three2 with Dissolve(0.2)
    ys6 "Inoue?{w} I admit she has this{w} arrogant attitude that turns people off,{w} but it has never become a serious problem.{w} No one has ever come close to –"
    stop music

    play sound sfx_static2
    "{i}{b}*BUZZ*{/b}{/i}"
    stop sound

    p_serg "Harold, you there?{w} You’ve got to hear this!"
    show emmerich talk at Three1 with Dissolve(0.2)
    p_emm "Excuse me for a moment, Yoshiro."
    hide emmerich with Dissolve(0.2)

    "The young inspector turned away from him."
    "From the other end, his senior officer sounded distressed,{w} made more evident by Emmerich’s tone shift.{w} Yoshiro pretended to close ears."

    play music bg_undaunted loop
    p_emm "You found the girl?!"

    show yoshiro surprised at Three2 with Dissolve(0.2)
    "This immediately caught the teenager’s attention.{w} As he listened, he picked up on some of the details."
    show yoshiro surprised2 at Three2 with Dissolve(0.2)
    "When the transmission ended, Emmerich returned to face Yoshiro, now piqued with curiosity.{w} However, the inspector saw through this."

    show emmerich talk at Three1 with Dissolve(0.2)
    p_emm "That’s the Sergeant.{w} And they have already found Shinozaki."
    ys6 "Where?"
    p_emm "Somewhere near the marketplace."
    show yoshiro angry at Three2 with Dissolve(0.2)
    ys6 "..."
    show emmerich worried at Three1 with Dissolve(0.2)
    p_emm "Look, I know what you’re thinking,{w} but please, head home immediately.{w} I didn’t like what I just heard, particularly..."
    show emmerich serious at Three1 with Dissolve(0.2)
    p_emm "{i}*sigh*{/i} You get my point? Good.{w} A pleasant evening to you,{w} and I apologize for your delay.{w} Now if you’ll excuse me..."
    hide emmerich with Dissolve(0.2)

    window show
    nvl clear
    narr "The inspector replaced his notebook in his jacket’s breast pocket and ran off."
    hide yoshiro with Dissolve(0.2)
    scene bg wetmarket night with dissolve
    narr "Having not realized the danger it might pose him, Yoshiro tailed the inspector.{w} He stopped a block away,{w} when he saw Emmerich meet up with the Sergeant outside an alley to the market’s East."
    narr "Some of the stalls were closing, the time at quarter past six.{w} Once the two officers disappeared, he went to an adjacent shop to buy a gift.{w} Because of the silence, he heard some inaudible voices from the other side of the wall."

    scene black
    nvl clear
    narr "{i}GAHAHAHAHAHAHAHAHAHAHA!!!{w} {b}*EXHALE*{/b} Hahahahahaha... *BREATHE*{w} Hahaha... Hu...{w} *whimper* *whimper*{/i}"
    narr "However, it was not what he expected to hear."
    narr "Furthermore, Inoue had never laughed as heartily as that.{w} No, it is not even the correct term.{w} He made his purchase and spied on the cops."
    narr "His eyes widened upon witnessing the scene."

    nvl clear
    window hide

    scene bg darkalley with fade
    show emmerich worried at RS with Dissolve(0.2)
    p_emm "Miss Shinozaki, you’re safe now.{w} {i}{b}*GRUNT*{/b}{/i} Please, pull yourself together!"
    show inoue creepy blood angry at LS
    is4 "I don’t believe you! {i}*whimper*{/i} Uhuhuhu..."
    show inoue noglass blood cry2 at LS with Dissolve(0.2)
    is4 "I don’t believe you! {i}*whimper*{/i} Uhuhuhu...{fast} I’m already... broken... {i}*hic*{/i} Uhuhuhuhuhuhuhuhu... {i}*hic*{/i}"
    show emmerich talk at RS with Dissolve(0.2)
    p_emm "She seems to be abused."
    p_serg "I hope it’s negative.{w} Poor girl’s been delirious when we found her.{w} Medical services are inbound – where the hell are they?!"
    hide emmerich with Dissolve(0.2)
    hide inoue with Dissolve(0.2)

    "Yoshiro felt a vibration in his pocket.{w} It was his smartphone,{w} with a new message from Ichirou."

    iy1 "{i}Have you found anything about Inoue yet???{w} This is TERRIBLE!{/i}"

    "Amidst the frenzied cries from within the alley, he typed in his reply."

    ys6 "{i}I’m currently undercover,{w} trying not to catch Inspector E.'s attention.{w} Inoue’s alive, but she seems... off...{w} I don’t know!{w} I can’t understand it!{/i}"
    iy1 "{i}That's good.{w} We, however, have a different story to tell.{/i}"
    ys6 "{i}Who's with you?{/i}"
    iy1 "{i}Miyu.{w} We were just going home together, and...{/i}"
    ys6 "{i}AND???{/i}"
    stop music
    iy1 "{i}You might want to hold off dinner for tonight.{/i}"

    "An image immediately followed."

    play music bg_controlledchaos loop
    ys6 "{i}WHAT THE HELL IS THAT???{w} If this is a joke, Ichirou...”{/i}"

    "Ichirou responded with more images,{w} each revealing more about the scene{w} and the corpse’s identity."
    "A burnt corpse on a gurney – none other than Kyou Kirisaki himself!"
    "His body is well into decomposition{w} – his temperature has dropped, the blood has dried, and maggots have already housed within his crevices."
    "But something else caught Yoshiro’s eye."

    show inoue creepy blood snap at LS with Dissolve(0.2)
    is4 "I won... didn’t I?{w} He wasn’t so clever... after all...{w} Heh. Hehehehehe..."

    "Kyou had his palms open,{w} and within the mosaic-like mix of red and black{w} etched a number on each.{w} Barely visible, but if examined close enough..."
    "Number 9 on the left,{w} number 7 on the right.{nw}"

    show inoue creepy blood snap2 at LS
    is4 "AHAHAHAHAHAHAHAHAHAHAHAHAHA!!!!!!!!! I won! He doesn’t! Would you believe it?!"
    hide inoue with Dissolve(0.2)

    "Petrified while viewing the images, Yoshiro did not notice an ambulance stopping across the alleyway.{w} A gurney was brought down and the policemen struggled to carry Inoue."

    show emmerich angry at Three2 with Dissolve(0.2)
    p_emm "Yoshiro?!{w} I gave you an order, didn’t I?"
    hide emmerich with Dissolve(0.2)

    window show
    nvl clear
    narr "The inspector caught his attention.{w} Though embarrassed, he meekly attempted to justify his presence,{w} ultimately gaining the former’s disapproval."
    narr "Both men watched Inoue as she was being taken away...{w} All while crooning a little tune."
    stop music fadeout 2.0
    scene black with fade
    narr "{i}Ring around... the rosie...{w}\nPocket full of posies...{/i}"
    window hide
    show inoue noglass blood sad at Three2 with Dissolve(0.2)
    show inoue noglass blood cry at Three2 with Dissolve(0.5)
    show inoue noglass blood cry2 at Three2 with Dissolve(0.5)
    show inoue creepy blood snap at Three2 with Dissolve(0.5)
    show inoue creepy blood snap2 at Three2
    window show
    narr "Inoue she was{w} no longer..."

    nvl clear
    window hide
    hide inoue with Dissolve(1.0)
    return

label ch01_19_funeral:
    scene black with fade
    "JUNE 30, 2013 - 0730H"
    play music bg_onthingstocome loop fadein 2.0
    window show
    nvl clear
    scene bg facultyroom with fade
    narr "The news broke out the following morning."
    narr "There was outrage,{w} with fingers pointing towards the administration and the authorities.{w} Had they taken appropriate measures immediately, it could have been prevented."
    narr "But who’s to say the culprit has not foreseen this?"

    nvl clear
    narr "Two students out of over nine-hundred{w} – small but significant in damage.{w} The Kirisakis mourned the loss of their son, Kyou,{w} and the Shinozakis were no different.{w} Inoue may have survived the crime, yet..."
    narr "Ms. Harada felt no different.{w} She filed a temporary leave to alleviate her pain. For only two weeks, it was approved,{w} and she would be paid without deduction provided she prepare a module."
    narr "And we saw her go, burdened with the tragedy of losing two children."
    narr "The close of the flag retreat felt like a funeral procession.{w} Students and teachers offered prayers.{w} It wasn’t just for Kyou and for Inoue’s recovery – it was for everyone."
    narr "We knew that it hasn’t stopped there yet.{w} Knock on the table, we might be under the killer’s watchful eye,{w} and he had already claimed his first victim.{w} Perhaps I’m wrong. I hope so."

    nvl clear
    narr "On political matters, the following changes are effective:{w} Sumiko is to succeed Kyou in the Science Club’s headship while I remain as Secretary,{w} and Inoue’s duties are temporarily upheld by her Vice officers."
    narr "Any complications the change would cause are yet to be resolved{w} – there may be one."
    window hide
    scene bg principalsoffice with fade
    show emmerich serious at Three2 with Dissolve(0.2)
    window show
    narr "Miyu and I gave our statements to the investigating officer,{w} Emmerich, it seems.{w} Business-like and frank, unlike how Yoshiro described him to us."

    nvl clear
    window hide

    p_emm "Have you any relatives that were admitted at the hospital on the 25th?"
    iy1 "No,{w} but I have a scheduled check-up every last Tuesday of the month.{w} It was only a two-minute walk to our houses so I had Miyu tag along."
    show emmerich talk at Three2 with Dissolve(0.2)
    p_emm "And how did you discover Kirisaki’s corpse?"
    iy1 "Not us, but the hospital staff.{w} In one of the hallways, Miyu caught a glimpse of someone being taken to the ER.{w} \"Wait! Isn’t that...?\" he said before following the gurney.{w} The rest is history."

    window show
    nvl clear
    narr "As brief as that, and Miyu repeated everything I’ve said.{w} There was really nothing suspicious about it.{w} I even showed him prescriptions dated {i}June 25th, 2013{/i} as proof."
    window hide
    hide emmerich with Dissolve(0.2)
    scene bg msci with dissolve
    show ichirou worried at Three2 with Dissolve(0.2)
    show miyu pissedclosed at Three3 with Dissolve(0.2)
    show sayo worried at Three1 with Dissolve(0.2)
    window show
    narr "We went out of the office,{w} encountering Sayo at the door.{w} She handed us a small scroll, spoke no words and abruptly left."
    hide sayo with Dissolve(0.2)
    narr "Its contents are short, only that of a notice."
    hide ichirou with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    
    nvl clear
    narr "{i}Greetings!{/i}"
    narr "{i}Please join us in celebrating the life of Kyou Kirisaki, who passed away this 25th of June, 2013,{w} at the Kirisaki family residence:{w} 82 Kasshoku St, Yama Province, Region IV-A.{/i}"
    narr "{i}Meet-up for the Funeral Procession at 10:00AM on Sunday, June 30th.{w}\nWe welcome those who would join us in commemoration of the departed until 3:00PM.{/i}"
    narr "{i}Lunch and snacks will be accommodated.{/i}"

    nvl clear
    narr "And at the bottom, a handwritten note:"
    narr "{i}Please do come.{w} Let us, who remain, pay our respects to Kyou and give him justice.{w} Notify me if you’ve decided – we’ll have a transport ready.{w} And do tell your parents of this, we might be staying for a while after.{/i}"
    narr "{i}Sayo{/i}"

    nvl clear
    narr "She went around handing papers to our batchmates."
    scene bg bedroom with fade
    narr "It may not amount to much, but I’ll go.{w} I messaged her that night after my parents approved of my trip."
    narr "Miyu will be tagging along, too.{w} That way, we can ensure each other’s safety, especially on the way home."
    narr "Those who went finished their responsibilities the day before;{w} Likewise, I’ve posted all announcements before leaving.{w} We might not have a Wi-Fi connection there."
    stop music fadeout 2.0

    nvl clear
    window hide
    play music bg_decline loop fadein 1.0
    scene bg freedompark with fade
    show akira serious at Eight2 with Dissolve(0.2)
    show sumiko seriousleft at Eight3 with Dissolve(0.2)
    show hiroshi worried at Eight5 with Dissolve(0.2)
    show yoshiro worriedleft at Eight6 with Dissolve(0.2)
    window show
    narr "Miyu and I joined the others at the city square;{w} that is, Akira, Sumiko, Hiroshi, and Yoshiro."
    window hide
    hide akira with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)
    hide hiroshi with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    show sayo casual glass serious at Three3 with Dissolve(0.2)
    window show
    narr "Sayo arrived at 8AM along with Ikuko and Ayumi,{w} telling us that Hikaru will be going with her parents."
    hide sayo with Dissolve(0.2)
    scene bg van with fade
    narr "We made small talk during the ride, mostly on random topics.{w} But if it would lead to something too disturbing, especially about the recent events,{w} someone would try to divert the issue.{w} At best, silence would befall us."
    narr "We are all shaken,{w} the imprint was still upon us.{w} Someone close to us{w} murdered in a way beyond forgiveness.{w} Heck, I don’t even want to know what exactly happened to Inoue!"
    narr "Maybe...{w} Maybe when she’s better...{w} Maybe if she’s willing to talk."

    nvl clear
    scene bg church with dissolve
    narr "At 10:30AM, all of Kyou’s friends and relatives gathered in the front garden.{w} After a short prayer, we all set out to the nearby church, where a mass was held.{w} The priest kept the casket closed while he sprinkled holy water{w} – kids would find the sight unpleasant."
    narr "We relayed back to the van and followed the funeral coach.{w} It played sorrowful songs,{w} particularly those of Gary V., Martin Nievera, Phil Collins, and Josh Groban.{w} Mourners of black and white walked around us carrying balloons and umbrellas."
    scene bg msci with dissolve
    narr "It brought us all back to the flag retreat.{w} Those thirty minutes sapped our energy coming to the weekend,{w} particularly, Ms. Harada’s heartfelt speech.{w} And Sayo, on behalf of the council..."

    nvl clear
    narr "{i}He may be a speck of dust compared to our numbers,{w} but the fact stands{w} – we’ve lost a brother.{w} May he pass on peacefully to the afterlife.{w} Let us offer a minute of prayer, and another of silence.{/i}"
    narr "After which, she looked towards our direction."
    narr "{i}I leave it all to you.{w} Thank you very much.{/i}"
    scene bg van with dissolve
    narr "Her pace that afternoon matched that of the mourners outside.{w} At the front seat, Sayo wrapped herself firmly and bit down on her lips.{w} There’s a lump in my throat, invoking me to tear up,{w} and I'm sure the others felt the same."
    narr "I resisted."

    nvl clear
    narr "When we reached the cemetery, the girls drew their handkerchiefs out, wiping away any tear they felt."
    narr "The men carrying the casket went first.{w} We followed, climbing up a set of slopes before we reached the burial site.{w} The priest from the Mass led the committal."
    narr "All of those present spoke a few words to Kyou.{w} He responded with brief gusts, something only Miyu and Ikuko noticed.{w} The small children were passed over the casket, crying,{w} even though the faces were familiar to them."
    narr "As Kyou was being sealed in, the priest gave his final blessings and everyone threw roses and ribbons.{w} Wailing and sniffles were prevalent;{w} even my companions shared their grief."
    stop music

    scene bg functionroom with dissolve
    nvl clear
    narr "The reception, though the dishes hearty,{w} was clouded in a somber atmosphere.{w} Sure, the attendants laughed while commemorating Kyou’s halcyon days,{w} but the joy stayed there."
    narr "And they realized how worse it became."
    narr "Pancit,{w} a noodle believed to lengthen one’s life.{w} How ironic{w} – the main dish enjoyed by those who survived the dead{w} – they’ll all join him no matter how much they consume."
    narr "And that includes me...{w} Forget about it."

    nvl clear
    narr "At three o’ clock, most of the guests have gone home.{w} Hikaru’s parents talked with the Kirisakis, while Sayo rounded us up to assist with the cleaning.{w} The activity relieved our minds of the grief even if partially."
    scene bg kitchen with dissolve
    play sound sfx_chirp loop
    narr "Hiroshi and I helped with the dishwashing."

    nvl clear
    window hide

    show hiroshi smileleft at LS with Dissolve(0.2)
    show ichirou focusleft at RS with Dissolve(0.2)
    hk7 "Funny how the birds sound like chicks, don’t they?"
    show ichirou surprised at RS with Dissolve(0.2)
    iy1 "Aw, spare me the image!{w} The wake has long passed, and you might want to move on, Hiroshi."
    show hiroshi smileleft at LS with Dissolve(0.2)
    hk7 "Hahahahahaha! Your heart, Ichirou. Keep it calm."
    show ichirou worried at RS with Dissolve(0.2)
    iy1 "{i}*sigh*{/i} But now that you mentioned it, does it really have an effect?"
    show hiroshi boredleft at LS with Dissolve(0.2)
    hk7 "Yes, I’m sure.{w} After all, this isn’t a husk we’re dealing with.{w} What man is born devoid of emotion?"
    show ichirou confused at RS with Dissolve(0.2)
    iy1 "Yeah... let’s mellow out of that prose.{w} You’re starting to sound like those YA novels you read."
    show hiroshi determined2 at LS with Dissolve(0.2)
    hk7 "What a spoilsport. Can’t you let me be?"
    show ichirou happy2 at RS with Dissolve(0.2)
    show hiroshi happyblush at LS with Dissolve(0.2)
    "\"\"Hahahahahahahahaha!\"\""
    hide hiroshi with Dissolve(0.2)
    hide ichirou with Dissolve(0.2)
    stop sound

    window show
    nvl clear
    narr "But he has a point."
    narr "Surely, the killer’s conscience must be upsetting him,{w} especially due to the extent of the damage he caused.{w} I would love to see that fearful look on his face."
    scene bg functionroom with dissolve
    narr "We gathered in the dining room save for Hikaru.{w} There, we rested for a while.{w} A few minutes later, Mrs. Kirisaki emerged from the door,{w} her tone delightful."

    nvl clear
    window hide

    play sound sfx_dooropen
    ms_kir "How are you doing, kids?{w} Join us in the living room, please, if you're already well-rested. We have a lot to discuss.{w} Oh, and calm yourselves. No pressure. {i}*chuckle*{/i}"

    scene bg parlor with dissolve
    window show
    nvl clear
    narr "With a nod, we followed her.{w} Inside the parlor, her husband and Mr. Yamamoto were already seated; Mrs. Yamamoto and Hikaru arrived shortly after we did.{w} Mr. Kirisaki exchanged hands with us and asked a few general questions."
    narr "And where was Kyou’s brother?{w} Upstairs in his room, studying.{w} He would be returning to school tomorrow, or so his parents told us."

    nvl clear
    window hide
    return

label ch01_20_epilogue:
    scene black with fade
    "JUNE 30, 2013 - 2000H"
    scene bg parlor with fade
    "{i}*RING* *RING*{/i}"

    show miyu pissed at Three3 with Dissolve(0.2)
    mh8 "Excuse me. My parents are calling."
    hide miyu with Dissolve(0.2)

    window show
    nvl clear
    narr "Dinner had ended,{w} and Sayo already called the van driver to shuttle us back to Kutsutochi.{w} My eyes are hurting, and everyone else is tired, too."
    narr "Only six of us are in the parlor:{w} Ayumi, Hikaru, Sumiko, Yoshiro, Hiroshi, and myself.{w} Everyone’s eyes are glued to their phones and tablets.{w} I didn’t bother to bring a charger for my low-battery phone, so I’m excepted."
    narr "I needed some fresh air.{w} The wind outside breezed through the open window, a good excuse to stay inside.{w} No. I prefer being outside.{w} The dim lights are dazing me, and I don’t want to drift off in the middle of the final prayer."

    nvl clear
    window hide

    show akira smile at RS with Dissolve(0.2)
    show ichirou focus at LS with Dissolve(0.2)
    iy1 "I'm gonna go outside for a while.{w} Give me a ring if we're all needed - I may not be able to hear an SMS tune."
    show akira proud2 at RS with Dissolve(0.2)
    ai2 "Yeah, whatever. Be on your way, then."
    hide ichirou with Dissolve(0.5)
    hide akira with Dissolve(0.2)

    scene bg pasteur night with dissolve
    play sound sfx_crickets loop
    nvl clear
    narr "A single light bulb illuminated the front porch.{w} It is mostly silent, occasionally broken by the bug zapper over the door.{w} Looking past the few buildings, the setting alone is fresh air for a city dweller like me."
    narr "Walks are perfect at night,{w} with the assurance of security so long as one doesn’t stray off the road.{w} Aside from the winds chilling your whole body, you’d be treated to a concert of the crickets.{w} It relieves tension, soothing the nerves so much they’ll absorb you wholly."
    narr "At the end of the wet season, cicadas would sometimes hang around a few trees.{w} There’s one buzzing on the right, two blocks from the Kirisaki residence."
    narr "{i}{b}*SNIFF*{/b}{/i} Aaaaaaahhhh..."
    narr "The roadside flowers are fragrant, too.{w} Only thing missing is the fruits, which are staples of the province."
    stop sound

    nvl clear
    window hide

    play sound sfx_ringtone loop
    "{i}*RING* *RING*{/i}"
    "I snapped out of my daydream.{w} Who could that be?"

    scene black with fade
    stop sound
    iy1 "Hello?"
    mh8 "Where are you?"
    iy1 "Just went out to catch some air.{w} Do you need me?"
    "..."
    iy1 "Hey, Miyu?"
    mh8 "Sorry. I can’t see you from here.{w} The prayer won’t start without you, ‘ya know?"
    iy1 "That so?!{w} OK! I’ll be back in a jiffy."

    "{i}*BEEP*{/i}"
    "And so ends my little journey.{w} I doubled the pace, making sure not to trouble the others."
    "They're probably itching to go home and sleep.{w} Even I miss my bed."

    "{i}Slow down...{/i}"
    play music bg_satiate loop

    window show
    nvl clear
    narr "Time halted after those two words."
    scene bg village night with dissolve
    show silhouette
    narr "Obstructing my path is a figure,{w} shadowy enough to conceal his identity.{w} He seems like a town drunkard or a junkie, something like that."
    narr "In any case, he’s not my problem.{w} But he’s not moving,{w} only facing towards me."

    nvl clear
    window hide

    iy1 "Are you talking to me?"

    "He took the hint.{w} Placing his hands in his coat, he turned the other way."
    "This time, the figure spoke a little louder."

    "{i}Condolence!{w} And I’m sorry to see your friend go...{/i}"

    "Condolence...? Friend...?{w} Hold on. This man is no stranger!"

    iy1 "Hold it!{w} What are you talking about?"

    hide silhouette
    "Without a word, he quickened his pace and started running.{w} What does he know?!"

    iy1 "Wait up! Hey!"

    scene black with fade
    stop music fadeout 2.0
    centered "{i}{b}And thus, the night became peaceful no longer.{w}\nWho's next, I wonder?{/i}{/b}"

    centered "{b}***END OF JUNE CHAPTER***\n\n{i}TO BE CONTINUED...{/i}{/b}"
    return