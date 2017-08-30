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

    #call ch01_01_prologue1
    #call ch01_02_prologue2
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
    "{i}What was that?{/i}"
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
    "Dinner was underway.{w} The northbound road of a major highway is congested with vehicles, flashing red from the view of the TV screen.{w} It was not long before a news report followed that short scene."

    window show
    nvl clear
    narr "{i}Sacred Heart Village, the centre of the infamous curse killings reported since June of 2012, has witnessed its tenth victim this early morning.{/i}"
    narr "{i}Kugimiya Oizumi, also known as Lienel, was found dead at her bedroom six o’ clock.{w} In the same vein as the previous killings this academic year, she had suffered a brutal end.{/i}"
    narr "{i}According to her mother, she was about to ready her daughter for the graduation ceremony this afternoon when she found Oizumi hanging from her room’s ceiling fan.{w} Her head was laterally sliced in half.{/i}"
    narr "{i}In addition, she noticed her daughter distressed the previous evening after they had an argument regarding her college education.{w} Denied of any scholarship and support from her parents, this may have played a role in her alleged suicide.{/i}"
    narr "{i}While her mother and their neighbours deny any foul play in Oizumi’s death, authorities are investigating from that angle.{/i}"
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

    "Just then, the clock at the hallway sounded to tell the house’s tenants of the time.{w} Twelve times, to be exact. One more day has begun anew."

    unk "{i}Time's up!{/i}"
    unk "Game over... puku."
    unk "Hihihihihihihi! {b}{i}*cackle*{/i}{/b} {b}{i}*cackle*{/i}{/b}"

    return

label ch01_03_clubday:
    "JUNE 7, 2013 - 1430H"
    window show
    nvl clear
    narr "Maria St. Claire Institute."
    narr "With the new council taking over, its mood and reputation has gone back to as it was in its glory days. Blessed is the day, indeed!"
    narr "And as per tradition, it was Club and Org Day today!{w} New circle of friends to get along with or the same ones all over again. The former holds mostly true for the freshmen all of whom were guided by an authority figure."
    narr "That authority figure is Sayo Ronoroa.{w} She is the current student council president, always ready whenever her service is needed."
    narr "The one with the highest honors so far; thus, she was always looked high upon by her colleagues and her teachers.{w} She has an aura much more different than those of her peers."
    narr "She was guiding some freshmen in choosing their clubs."

    nvl clear
    window hide

    sr5 "Would you like to join the Science Club or the Journalism Org?{w} I was a member of both once. You’ll learn a lot, I promise!"

    "She would flash that smile.{w} The same charming smile she gave everyone. Well, those who are not bothering her, at least.{w} It captured the hearts of the freshmen;{w} hence, they followed her suggestion."

    sr5 "One at a time, children. Know how difficult it is to row two boats at once! {i}*giggle*{/i}"

    window show
    nvl clear
    narr "She was always like that. After seeing the students off, she turned around her heels and headed to the council room."
    narr "Sayo passed by the room neighbouring the Science Club.{w} Being the \"Queen of Science,\" this is where the Mathematics Club is being held.{w} Inside were a few officers busy with their preparations."
    narr "Like the others, they were relatively chill.{w} One of the officers, the Vice Preident, was going over the program guide a few times to check for any mistakes.{w} He snorts and fixes his glasses randomly."
    narr "Miyu Hirano,{w} a transferee student during his Sophomore years and one of the youngest in their batch.{w} He was particularly skilled at Math and one of his true passions.{w} Hence, he had been here for quite a long time."
    narr "A symbol of pride and excellence, he fulfills his duties as best as he could."

    nvl clear
    window hide

    mh8 "Awww... come on..."
    hy10 "What seems to be the problem, Miyu?"

    "The sweet-voiced girl approached Miyu and addressed his frustration.{w} He had forgotten to bring the materials for one of their games later."

    hy10 "Oh. That? Hehehe...{w} An acute problem if you would ask me. Shall we tell this to Ms. President?"
    mh8 "No need. No need. Let’s just make do with what we have. I’m a master of impromptu, you see?"
    hy10 "Whatever you say..."

    window show
    nvl clear
    narr "Her name is Hikaru Yamamoto, Miyu’s long-time friend and classmate.{w} She holds the position of Treasurer in their club."
    narr "She is usually the comic relief of her class. However, she holds a duality between it and being a distinguished student in their batch.{w} She had come close to Sayo once, the reigning First Placer in their early years."
    narr "A reliable friend and an only child, she embraces her youth. Hikaru is different to those who are around her age.{w} She has a special friend, a resident singer named Aria, her personal butt monkey."

    nvl clear
    window hide

    "{i}Pssst... Pssst...{/i}"

    "Someone was calling out from the window. It caught one of the officers’ attention and called for Miyu."

    iy1 "You guys still busy? I want to talk for a minute or two."

    "He put down the program guide and went out of the classroom as prompted. Miyu placed his hands in his pockets."

    mh8 "Ichirou, you’ve dropped by! I see you guys haven’t started yet as well.{w} What up?"
    iy1 "I’ve already talked to the others about this. You coming?"
    mh8 "Where to?"

    window show
    nvl clear
    narr "Miyu smirked and placed an arm over one side of the doorway.{w} Of course, this could be another mischievous prank by Ichirou."
    narr "Speaking of, his full name is Ichirou Yokohama, the projected valedictorian of the batch.{w} He has quite a humble nature, but he drops the act once the view of his teachers leaves him."
    narr "Like Miyu, Ichirou is very skilled in Mathematics and has gone on to join a few contests even having Miyu as a teammate.{w} Still, because of the fair match in their skill level, they are considered as rivals to each other."
    narr "That doesn’t stop them from being close friends, however."

    nvl clear
    window hide

    iy1 "Let’s bond. I mean, since it’s our last year and all... {i}*chuckle*{/i} why not we gather together for a friendly chat.{w} You know, jut a few of us?"
    mh8 "And you tapped people already? Who else is coming along?"
    iy1 "I’ve tapped four, making us five at the moment:{w} Sumiko, Akira, Kyou, and Hiroshi.{w} Well, not sure about Akira, though, being a council officer. But hey, he’s looking forward to it."
    mh8 "Count me in. Tell me what to do."
    iy1 "Yippee!!!{w} That’s six people. You might want to tap Hikaru to join us.{w} You know you want to..."

    "If Miyu had a newspaper in hand, he would have rolled it and hit Ichirou right on his crown.{w} Luckily, he was able to get away with it."
    "Miyu is often teased with Hikaru, given the gravity of their friendship.{w} Awkward, it may seem, but they both eventually got used to it."
    "It still doesn’t sound pleasurable to Miyu, though, as he has {i}other businesses{\i} to attend to."

    mh8 "Alright, alright. Whatever you say!{w} Don’t you have a club activity to attend to, huh, {i}Mr. SciClub Officer{/i}?"

    "Ichirou glanced at the neighbouring room.{w} Sumiko was inside, cross-armed and glaring at him. He motioned for Ichirou to come inside."

    iy1 "Half-past five near the auditorium, Miyu. Spread the word."

    "With a snap of a finger, the two parted ways and returned to their duties."

    "JUNE 7, 2013 - 1600H"
    window show
    nvl clear
    narr "After over an hour of club-related activities, the students went around to find their desired organization.{w} This time, the preparations were bigger and the number of choices reduced."
    narr "Some of the fellow club officers are also part of the same organization. Thus, this preserves their established chemistry."

    nvl clear
    narr "Sumiko Tokubei is the President of the Environmental Organization, with fellow officers Hiroshi and Yoshiro.{w} Being a hands-on person, he always ensures everything is according to plan."
    narr "Of course, he embodies the cliché description of a high IQ student.{w} His excellent performance in Science is complemented by his occasional forgetfulness. Kind of like a memory card."
    narr "He spoke with authority, addressing the crowd before them."

    nvl clear
    window hide

    st3 "Settle down, everyone. We would like to begin our first meeting at EO.{w} The {b}Environmental Organization{/b}, not the eye care center."
    "HAHAHAHAHAHAHAHA!!! Woo... WOO!!!! {b}*APPLAUSE*{/b}"
    
    "Sumiko gave his opening remarks as the presiding officer and their scheduled activities followed."
    "Yoshiro Suzuki, the resident puzzle geek, solved a 3x3x3 Rubik’s Cube in hand while he discussed the details of their organization."
    "Those who were listening to him were in awe, attention divided between his message and his puzzle-solving skills.{w} More than puzzles, though, he is quite a fan of riddles and whodunit mysteries."
    "That would come in handy whenever necessary."

    ys6 "So, to sum it up..."
    "{i}*crank*{/i} {i}*crank*{/i} {i}*crank*{/i}"
    ys6 "What you’re in for is basically adventure, tree-planting, waste segregation, and more! What else could you ask for?"

    "At that instant, his hands stopped.{w}"
    "He raised both eyebrows to everyone in the room.{w} He gave the cube a spin, showing all of its sides solved and free of any imperfections. A fine work at that."

    ys6 "Any questions?"

    "No answer, as expected."
    "Besides, the audience was left in awe, giving him the same treatment as Sumiko.{w} Afterwards, the ball moved to Hiroshi Kano, the Secretary of the organization."

    hk7 "Now that you’ve been introduced to our organization and what our goals are, let us have a short intermission."
    hk7 "..."
    hk7 "IIIIITTT'S... GAME TIME!!!"

    window show
    nvl clear
    narr "Hiroshi gave it his all.{w} The sourpusses became active, the monotonous room became livelier, jokes were made left and right...{w} It was all part of a package."
    narr "At the end of the intermission, the crowd pleaded for more. A pair of sly eyes responded, silent but manipulative."
    narr "An upright thumb shot high in the air."
    narr "The students went wild, one of them whistled merrily at Hiroshi’s approval. An impromptu intermission later for fanservice, no doubt."

    nvl clear
    narr "In contrast to the cheerful atmosphere of the classrooms around the school, the council’s office is different.{w} The officers held a four o’ clock meeting after the children were ushered to their desired organizations."
    narr "Perfect attendance."
    narr "All eyes upon Sayo Ronoroa, the President and the head of the meeting.{w} Twelve seats in the manner of the Round Table, save for the three highest officials who were seated together: the President and her Vice,{w} and the Secretary who was taking down the minutes."

    nvl clear
    narr "All of them were given an equal chance to speak, addressing each of their plans and concerns for the current academic year.{w} Of course, today’s activities were also part of their agenda, considering it a success."
    narr "After the Treasurer, the Auditor gave his report.{w} His manner seemed like a façade for some, yet he gave no questionable details. He had to express ethos during times like this and the same is true during classes."
    narr "He was none other than Akira Ichibana, the oftentimes aloof and light-hearted fellow.{w} A fool be the one who thinks he’s a fool."
    narr "He hides a lot of intelligence, recently acing the college exam reviews he took during summer."
    narr "This Akira is far different from his usual self.{w} In either case, he is respected by his fellow batch mates. Not unlike Hikaru, he is a joker but more often noisier than her."

    nvl clear
    narr "It was yet to manifest, long after he finished giving his report."
    narr "Then it went down to the Peace Officers, the Public Information Officer, and the Batch Representatives."

    nvl clear
    window hide
    
    "JUNE 7, 2013 - 1700H"
    window show
    nvl clear
    narr "Overall, it was a harmonious meeting."
    narr "If their adviser had been present, she would remark about their positive chemistry,{w} something which they have outdone the previous councils."
    narr "Admittedly, there were a few minor arguments in the process.{w} Still, the officers retained their cool."

    nvl clear
    narr "The bell has already rung."
    narr "Their first week of classes is over and so did the council’s meeting. Everyone tidied themselves up.{w} In behalf of their adviser, Sayo took charge of the adjournment."

    nvl clear
    window hide

    sr5 "I would like to thank you all for being present at this meeting."
    sr5 "Frankly, I expected less for all of us.{w} All of our visions align towards a single direction, but we should always keep in mind the responsibilities we have at hand."
    sr5 "We accepted this job; thus, we must know how to balance it.{w} That is all. Have a safe trip home everyone and I wish you all a pleasant Saturday."
    sr5 "Watanabe, kindly remind everyone about the PTC tomorrow. I might be seeing some of you here, then."
    sr5 "Off you go! Meeting adjourned."

    "Slowly, the officers got up and left the small conference room."
    "The main office had four cubicles placed strategically near the middle of the room, two on each side. All four faced the exit."
    "Akira was going around, inviting the officers for Ichirou’s gig in about thirty minutes."

    ai2 "You coming?{w} No? It will be fun. Promise..."
    ai2 "There’s only a few of us...{w} Let’s go together."

    "Unfortunately, those whom he asked refused his invitation.{w} They either had other matters to attend to or have decided beforehand to go home immediately."

    ai2 "Drat! So, we are still the same count as before.{w} But, presumably, Miyu has accepted Ichirou’s invitation. That makes us six,{w} but what who shall I tap? Hmmm…"

    "He strokes his lower lip, thinking hard...{w} hard enough that he became almost detached to his surroundings."
    "A light tap on the back returned him to his senses."

    ai2 "{b}{i}*GASP*{/i}{/b} Sayo... don’t do that!"
    sr5 "Pardon. {i}*giggle*{/i}{w} But you’ve been asking everybody else about some... get-together, am I not mistaken?"
    ai2 "Oh, yeah. Ichirou’s been planning on this gig since June started.{w} It was whimsical. I don’t even know what he’s up to with this one."
    ai2 "But as long as it looks fun, I wouldn’t dare pass it up."
    sr5 "Say, you guys've got a lot of time in your hands..."
    ai2 "..."
    ai2 "{i}Say the word... I dare you.{/i}"
    sr5 "...but don’t bother.{w} Would you first accompany me to Mrs. Genkai? I’ll just pass these documents and keys to her and {i}maybe{/i} I’ll make up my mind on the way."
    sr5 "You know, have a friendly chit-chat to alleviate boredom."
    ai2 "Oh! Thank you! Thank you! Thank you! Anything for you, Ms. President.{w} We have plenty of time to loiter around – er, I mean, finish up everything. Hehehe..."

    "Sayo gave a sugary smile, moving her head slightly to her left."
    "After ensuring all appliances were turned off, they locked the council’s office behind them.{w} IV-A’s room is their direct neighbor. They only took a few steps to the west staircase, which is directly across the room."

    sr5 "And what will we do exactly when we get there?"
    ai2 "I honestly don’t know what he’s planning to do. We’ll find out on the spot. Last thing I know is that we’ll be playing cards together."
    sr5 "Cards? You mean like Poker or Go Fish?"
    ai2 "No, the friendlier version, UNO.{w} Wait...{w} did you say {i}Poker{/i}?"
    sr5 "I did. I was hoping to challenge someone to a game. {i}*exhale*{/i} Shame I’ve never played it for over a year."
    ai2 "Legit?! I never knew – I’ve never heard someone mention Poker as a first impression on you. You surprise me."
    sr5 "I’m not surprised. Hm. Hm. You’re not going to challenge me, are you? For the experience, maybe?"
    ai2 "No. I don’t even understand its rules, let alone hoping to win as a novice.{w} I’ll be willing to wait, if that’s what you want. Hehehe..."
    
    "In her eyes, Akira is a different customer and an honest one.{w} All but two who knew of her secret hobby has challenged her for a few rounds of Texas Hold ‘em."
    "And none has ever prevailed against her.{w} But why has this not spread out yet?"

    sr5 "Before we play, I firmly ask my opponents not to disclose anything about it.{w} We’d always come to an agreement. What fun would it be if everyone knows about it?"
    ai2 "{i}She... has a point.{w} While singing, dancing and online gaming are the most common hobbies one could have in our batch, she’s a rare gem. Hence, the excitement would die out if everyone knows about it.{/i}"
    ai2 "{i}Sayo knows that very well. As a sign of respect, I’ll keep my mouth shut.{w} She can do the talking herself if she wishes.{/i}"
    ai2 "{i}From our vantage point on the second floor, I can already distinguish I few faces from afar:{w} Ichirou, Hiroshi, Kyou, and Yoshiro. Sumiko has just arrived.{/i}"
    ai2 "{i}Wait.{w} That makes us eight, counting Sayo in, too!{/i}"
    ai2 "{i}There’s someone coming - actually, three of them:{w} Miyu, Hikaru, and Inoue.{w} That guy managed to drag Inoue along?! A brave soul, I have to say.{/i}"

    "Ten people, gathered in a single place,{w} counting down the last ten months of their high school years as a senior."
    "The countdown is to commence soon."
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