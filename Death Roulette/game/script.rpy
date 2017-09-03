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
define tomonori = Character("Tomonori")
define ikuko = Character("Ikuko")
define t_gen = Character("Mrs. Genkai")
define t_har = Character("Ms. Harada")
define t_kan = Character("Mrs. Kanako")
define prin = Character("Mrs. Sokoguchi")
define ms_shi = Character("Mrs. Shinozaki")
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
    #call ch01_03_clubday
    #call ch01_04_tenvictims
    #call ch01_05_sacredheart
    #call ch01_06_kyou
    #call ch01_07_countdown
    #call ch01_08_disappearance
    #call ch01_09_labkyou1
    #call ch01_10_labinoue1
    #call ch01_11_labkyou2
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
    "After ensuring all appliances were turned off, they locked the council’s office behind them.{w} IV-A’s room is their direct neighbour. They only took a few steps to the west staircase, which is directly across the room."

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
    "At the side of the auditorium near the backstage entrance sat a circle of eight.{w} Clockwise from Ichirou were Kyou, Hiroshi, Miyu, Inoue, Hikaru, Sumiko, and Yoshiro."
    "They began by greeting each other and telling how their day went and all.{w} Questions were raised about why they were so few and what they will do."
    "Without an agenda, however, they are free to do anything as they wish."

    iy1 "Cards. You brought the cards, Sumiko?"
    st3 "Why not? This is the go-to game for gatherings."

    "He dropped a pack of UNO cards at the center. Much to their delight, the conversations stopped and all eyes were on it."

    iy1 "So, we start when Akira gets here. We don’t want to leave anybody out, don’t we?"
    mh8 "I can’t see from here. How about you, Ichirou? Have they come out yet?"
    iy1 "\'They?\'{w} Oh, Sayo and Akira? Haven’t noticed them.{w} Hey – you think she’ll come along?"
    mh8 "How should I know? You’re the one who set up this gathering.{w} And you gave instructions to tap anyone who’s willing to join, didn’t you?"
    is4 "Could’ve said, \'maybe.\'"
    mh8 "Yeah, but I’m just trying to explain things across."
    is4 "You always over explain things, Miyu – an acquired habit, perhaps? *giggle*"
    mh8 "{i}*sigh*{/i} Fine.{w} {i}I’ll just shut up and watch Yoshiro. I’m bored.{i}"

    "After the second one-minute solve by Yoshiro, footsteps –{w} a pair sounded from behind Miyu’s side.{w} Looking up, Ichirou and Hiroshi acknowledged the tenth participant."

    sr5 "Hey, everyone!"

    "Sayo was trailing behind Akira, giving her sweetest smile to the group.{w}"
    "She took her place between Miyu and Inoue, the closest to the stairs where they came from.{w} Akira, on the other hand, sat beween Sumiko and Yoshiro."
    "Likewise, the rest welcomed the new arrivals."

    sr5 "Pardon. We had to give a detailed report to Mrs. Genkai. Were you about to start?"
    iy1 "We chose to wait. But actually, we didn’t expect you to come – so, thanks... welcome!"
    sr5 "I feel the same. I was about to go home until Akira told me about it.{w} A one in a thousand chance, so why not? I might as well squeeze in some fun time while I’m at it."

    "The conversation was cut short by Sumiko, who was already dealing cards to the players - five a hand, as per usual rules.{w} He placed the deck in the middle and dealt a card as a start."

    window show
    nvl clear
    narr "The rules are simple."
    narr "The deck consists of cards numbered from 0 to 9, all colored red, blue, yellow, or green.{w} Depending on the game type, there are different special cards and rules available. The first is of the regular type."
    narr "First, one player drops a card from his hand, after which he determines the turn order."
    narr "Then, the next player must drop one of two kinds of cards: either of the same value or the same color as the previous card dropped.{w} If he has neither, then he draws cards until he gets a suitable one."

    nvl clear
    narr "To further add strategy and suspense to the game, there are special cards available.{w} When a player drops one of these, the next player has to drop a card with the specified color."
    narr "First are the {i}Wild Cards{/i}.{w} It can follow any card dropped by a player;{w} anyone who drops one specifies the next color to drop."
    narr "Second are the {i}Draw Cards{/i} which add cards to the next player’s hand.{w} Two types: the {i}+2 cards{/i}, which are colored and can be stacked;{w} the {i}+4 cards{/i}, also stackable but is also a {i}Draw Card{/i} hybrid.{w} These cards cannot be mixed in subsequent moves."
    narr "Third are the {i}Turn Manipulation Cards{/i}, a collective category containing the {i}Reverse{/i} and {i}Skip Turn{/i} cards. The former does exactly as its name, the latter skips the next player’s turn."

    nvl clear
    narr "Anytime a player has one card left in hand, he must declare \"UNO!\" before anyone else. In the group’s case, the first hand to the floor."
    narr "If another player gets to the ground first, it is an automatic +2 Draw for the player."
    narr "A player wins if he empties his hand first.{w} The game may continue until all or a set number of players finish. The deck replenishes infinitely unless agreed otherwise."

    nvl clear
    window hide

    is4 "One more thing.{w} Anyone who’s dead last in the \"UNO!\" declaration shall get a {i}ketchup{/i} from the other players."
    is4 "...Right, Miyu?"
    mh8 "Yes...{w} I suppose so."

    call ch01_04A_uno # To Be Added

    window show
    nvl clear
    narr "It is a little before six o’ clock, with the sun setting down. Its beautiful colors of red and orange reflected all over the open field.{w} While not a reflection, these colors are on everybody’s arms as well."
    narr "{i}Ketchup{/i} as Inoue refers to it."
    narr "After one suspenseful round, the small party decided to wind down and share a few stories. All ears were on those who spoke.{w} Laughter, sorrow, fright, and other emotions exhibited on their faces."

    nvl clear
    window hide

    hy10 "Then Aria and I went to the arcade at Blue Wave. We tried one of those Whack-A-Mole games.{w} Unsuspectingly, she got a hammer on her head. {i}*snort*{/i} Poor thing if I say so."
    hk7 "What a meanie!"
    hy10 "Afterwards, she suggested that we play a light-gun horror game. It’s part of the series I am currently playing so I gave it a shot.{w} Halfway through the first stage, I died."
    is4 "And... what about it?"
    hy10 "I begged her for a few more tokens, but she didn’t have any.{w} Eventually, she died and the countdown screen showed up. We walked away, and I noticed she left my side."
    hy10 "The kicker?{w} Turns out she had a lot of tokens stashed away secretly! Hmph. What nerve!"

    "Though half-humorous, she managed to elicit a few laughs.{w} Miyu shrugged, knowing that this is a common occurrence between the two best friends."
    "A quarter of an hour passed.{w} Sayo fumbled through her backpack, long enough for someone to take notice."

    st3 "Is something amiss?"
    sr5 "My music sheets. I must have forgotten it somewhere.{w} Ah! It must be inside the auditorium."
    hy10 "Can’t you get it next week? Besides, the main entrance is already closed off."
    sr5 "No – you don’t understand.{w} The music sheets contain some songs we’ll use at Sunday. I’m glad I didn’t head straight home just yet. Could anyone find it for me?"

    "A minute passed with eyes looking at each other. Miyu finally broke the silence and rose from his seat."

    mh8 "How many was it?"
    sr5 "It’s a book of music sheets.{w} You should find it somewhere in the backstage or in the main auditorium. I know since I was the last to leave after Mass."
    mh8 "I'll go. Just tell me the cover's color."
    sr5 "Thank you, Miyu!{w} It's black - you do have a flashlight with you? You can borrow mine if you wish."

    "Miyu pointed at his phone's flashlight.{w} He went around the circle, laying his hand on the backstage door. He twisted the knob and gave the door a light push."
    "Activating the flashlight, he entered the dark room and searched for the light switch.{w} Once he found it, Miyu flipped it up.{w}.. Except..."

    mh8 "Power’s out.{w} Oh, silly of me - it’s past six o’ clock. They must have cut the power from the main building. Moving on..."
    st3 "Make it quick, Miyu. I think the guard’s already signaling us to leave. He’s going to make a second whistle in fifteen minutes."

    "Light shuffling and occasional sounds of objects being moved emanated from the backdoor.{w} As time passed by, the sound became softer and softer...{w} until Miyu can no longer be heard."
    "To combat silence, the party was able to squeeze in another story, this time coming from Sayo.{w} In contrast to the previous stories, there was no opportunity to laugh.{w} All eyes were on her."
    "It was serious, a subject Miyu is especially interested on. Shame he is currently navigating around the dark building."

    kk9 "I remember it being on the news, yes. A year ago, if I remember correctly."
    sr5 "That’s right.{w} Ten students snuffed out one by one throughout the year in brutal ways - all from Sacred Heart Village.{w} It was definitely news back then, the hot topic of the neighbourhood."
    is4 "But the deed is done, right? I mean, what did they call it?{w} \"Curse Killings\"?"
    sr5 "The Sacred Heart Curse Killings, derived from the name of the victims’ school.{w} It’s also the name of the place they lived in."
    kk9 "Senior-level high school students, weren't they?{w} So close to graduation... a tragedy indeed. May God bless their souls."
    sr5 "I haven’t dug deep into the details yet. All I’ve got were information from news reports and conspiracy theories around the internet.{w} Frankly, I wouldn’t touch the latter, but I guess they’d make a good topic."

    "From her backpack, Sayo took out a small notepad.{w} She opened it to a page containing bullet points of the theories she researched. She recited each point, not yet filtering the factual from the trivial."

    ys6 "Planned from the beginning, you say? It doesn’t look that way to me considering the news reports and your statements. There’s no exact way to fit it."
    sr5 "I know, but what if it was?{w} I considered every possible angle I could look upon. It all leads to that in some way. I might formulate my own theory some time later when I look it up again."
    ys6 "How about the identities of potential suspects? Have you got ‘em?"
    sr5 "Unfortunately, still zero. All suspects were acquitted.{w} It’s one of the main reasons why this case is still open. How about all of you? Your thoughts?"
    iy1 "You know, if Miyu was here, he’d be delighted to share something.{w} He’s still inside and, from here, I can’t seem to detect his presence."

    "Ichirou took a quick glance towards the backstage door. Just plain blackness.{w} No Miyu in sight, no footsteps to hear.{w} For a moment, the party silenced themselves to think."

    hk7 "You might want to consider this, Sayo.{w} Before we went here, we decided to drop by the guard’s post for a little chat. You might not have noticed us."
    sr5 "I’m listening."
    hk7 "He asked us how our activities went and we asked how his day went in return.{w} The ball came to the recent Curse Killings. We pretended to listen given how we felt the theories he talked about was absurd."
    hk7 "That is... until he mentioned Suzumoto-san."
    sr5 "Ikari Suzumoto,{w} two batches ahead of us and part of the honor roll? How is she involved in the tragedies?"

    "Before proceeding, Hiroshi made everyone promise that whatever he tells must not be spilled.{w} Everyone agreed on his conditions and he related the story he was told."
    "Shock –{w} the single word to accurately describe the party’s collective reaction."

    is4 "Preposterous! It’s beyond the rules – there’s no rational way...{w} Still, I never expected the poor girl to be that way. She looked... alright."
    ys6 "That’s what he told us.{w} I, too, am in disbelief.{w} And take note, it didn’t come from him but from Suzumoto herself."
    kk9 "A deal made to the devil – certainly not a proper way to stop the curse.{w} But the idea is there. There’s still no way these things are related. Pestilence and death do not necessarily go hand in hand."
    ys6 "Exactly. We were certainly not placed under high security.{w} Some of our upperclassmen were inflicted with dangerous illnesses, that’s all. They all managed to survive by a miracle."
    ys6 "Sacred Heart Academy suffered death, blunt I may sound.{w} They contrast each other!"
    kk9 "A {i}catalyst{/i} if you want to put Suzumoto-san that way, otherwise none."
    ys6 "But she did the conjuration, not them.{w} {b}*grunt*{/b} Sometimes, supernatural forces need to stay as they are."
    hy10 "So what does this mean for us?"
    sr5 "Nothing. We’re left out of it.{w} Kyou and Yoshiro are correct.{w} There must exist no connection. Nothing at all."
    is4 "Then we leave it as a campfire story she made up on the spot. A commendable effort, I should say, to pull that off.{w} Anyway, I’m more interested in the latter part of the story. What did the symbol look like again?"
    hk7 "From what I can remember, he said Suzumoto formed a pseudo-circle resembling a clock. Ten, not twelve, graduation pictures were pinned along its perimeter.{w} She was among those – I don’t know. I haven’t seen it personally."
    is4 "Interesting.{w} Now, I’ve thought of something. How many are we right now?"
    is4 "One."

    "Clockwise from Inoue, each member of the circle counted themselves."

    sr5 "Nine."
    is4 "It’s all good. Forget I said any-"
    mh8 "Ten!"

    "Everyone jumped at the voice.{w} Miyu emerged from the door, a small book under his left arm. He approached Sayo and gave it to her.{w} With a smile on her face, she scanned the pages for any missing sheets."
    "They were all complete.{w} She replaced the book into her backpack and thanked Miyu for his trouble."

    mh8 "So what were they about? Sunday School? I saw some nursery rhymes contained inside."
    sr5 "That’s right.{w} My older sister brings this with her every Sunday for that purpose. The rest of the week, it’s with me, especially on First Friday Mass."

    "Miyu responded with a look of satisfaction. He asked the others a rundown of what he missed.{w} Hiroshi repeated the story to him in a brief manner."

    mh8 "I missed a lot! How dare you exclude me, guys?{w} I'm just kidding. Hahaha..."
    st3 "Strange... what took you so long, Miyu?"
    mh8 "I had a bit of difficulty navigating around the place. My flashlight isn’t that bright either.{w} I might have missed the book several times.{w} {i}*grunt* Why did it have to be black{/i}?"
    st3 "Fair enough. And since you’re here, we can leave now, right?"
    iy1 "Oh, that.{w} Let me thank everyone for coming. I honestly did not expect that much for this gathering - I planned to do it only once."
    ai2 "Well, it was fun while it lasted.{w} We’ve ten months ahead of us. Lots of time to fool around with each other again."    
    sr5 "It was a wonderful idea, Ichirou! Let me know if you plan to hold another one.{w} It’s good to join this every once in a while.{w} I think {i}I{/i} can influence the others to come along."
    iy1 "You spoke for me, and I am left with no words.{w} Well, until we meet again – tomorrow! That’s right, I’ll be seeing you at the Parents-Teachers Conference tomorrow morning."
    iy1 "Have a safe trip home!"

    "Exactly when the group tidied up, the guard motioned them to leave.{w} The sun was nowhere in sight, coloring the sky a dark shade of blue. A few casual conversations were made along the way."
    "Inoue approached Sayo, the latter noticing her grim expression and anticipated her words.{w} She took the initiative."

    sr5 "You look a bit pale. Can you make it tomorrow?"
    is4 "I’ll be fine. It’s just that –{w} look, I know I’m not into that kind of stuff.{w} Yet, it disturbs me, the first to do so."

    "Sayo’s smile dropped and was replaced by a look of concern. Her pace slowed down."

    sr5 "Inoue, be specific. The Sacred Heart mystery or Suzumoto’s story?"
    is4 "Both.{w} I’ve thought about it, compared the two events, and I seem to have found a link. What if –"
    sr5 "I get it.{w} That’s why you counted how many we are earlier, isn’t it? It’s not going to happen, I assure you. A majority of us have already agreed on that."
    is4 "Alright, but I just want my curiosities cleared.{w} I need someone rational enough to delve deeper into the subject.{w} That’s why I came to you."
    sr5 "Then I’ll research further on the Curse Killings if I have time,{w} but what interest is there?"
    sr5 "Get a good night’s sleep, Inoue - chase away whatever hex is lingering in your brain.{w} Besides, we have two days to unwind."
    is4 "I suppose you’re right.{w} I probably should stop thinking about it..."
    "They were nearly overtaken by the group of Sumiko, Akira, Yoshiro, and Miyu."
    "What interest is there, indeed?"
    return

label ch01_04A_uno:
    "--OPTIONAL--"
    return

label ch01_05_sacredheart:
    "JUNE 13, 2013 - 1900H"
    window show
    nvl clear
    narr "Thursday night."
    narr "A peaceful night almost devoid of sound, save for the light tapping made by the raindrops - not enough to suspend classes the following day."
    narr "And cutlery! They accompanied the aroma of the sumptuous meal that the Shinozakis enjoyed.{w} Elegant candelabra in the middle to match the aesthetics.{w} It had class, though they were not that wealthy at all."
    narr "Dinner talk was the usual: how did school go, what trips and appointments to attend to at work and where to go for the weekend – ordinary family matters.{w} Once they had their fill, they tidied themselves up, as no maid is in their employ."
    narr "While their parents headed straight up to the master bedroom, Inoue and her brother stayed behind in the living room. They tuned in to their favorite channel after watching the primetime news."

    nvl clear
    window hide

    "{b}*RING* *RING*{/b}"

    "Who could be calling us tonight? I am expecting nobody.{w} Probably for big brother again... not my business."

    tomonori "Inoue, this call's for you."

    "He handed the receiver to me, moving away and lowering the volume. A polite chap, he is."

    is4 "Hello? Inoue Shinozaki speaking."
    unk "Good evening!{w} Sayo Ronoroa here. How are you?"
    is4 "Pleasant. You must feel the same.{w} I didn’t expect you to call tonight, so what brings you to?"
    sr5 "I was hoping for a quick chat with you. The evening weather probably will become worse by midnight.{w} But I want you to hold on for... an hour or so, I think. Am I not a bother?"

    "I sat down, preparing the couch pillow. Involuntarily, I looked around even though I didn’t need to.{w} Brother is there – enjoying the TV show by himself."

    is4 "This is about last week, isn’t it? When we were heading back home?"
    sr5 "Yes, yes. In fact, I wanted to come to you earlier during lunch break.{w} I just didn’t know how to put it in a {i}pleasant{/i} way then. I feared I might ruin your day."
    is4 "It’s alright. We’re on the line now – just the two of us. What did you find?"
    sr5 "Lots.{w} Besides the facts I’ve researched a few months ago, there have been quite some developments.{w} I noticed a pattern – the time frames at which the victims were killed."
    sr5 "There was exactly one victim per month – starting from June 2012 until March 2013."
    is4 "Ten months, ten victims.{w} A grand-scale murder if it ever was one. But what was the motive?{w} It seems all random and disconnected to me – yet, somehow they all connect!"
    sr5 "Not motive... {i}motives{/i}.{w}. There is no single method in each of the killings – those who knew the victims related the manner of their death to... some aspect of their life."
    sr5 "There must exist a mastermind, then, {i}if{/i} the deaths were orchestrated.{w} Who were the accomplices? None proven, hence why this case is still open."
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

    is4 "Hold up!"

    "Did I just hear that right? A direct assault!{w} But... how come is the October victim’s death part of the ten? Unless..."

    is4 "If not direct assault, then the drill must be faulty or rigged."
    sr5 "Correct. Bad luck on his part.{w} With the previous deaths occurring, those who witnessed it saw it a part of the Curse Killings, dismissing any rational explanation.{w} Home Economics classes were suspended for a month to make room for investigations."
    sr5 "They had one suspect, Rika Suzumiya, whose fingerprints were found on the drill.{w} She and Shibuya shared a long-time argument regarding a botched group project, even taking it personally."
    sr5 "However, she was proven innocent by reliable witness statements.{w} Another dead end was created."
    is4 "That’s horrible! Even in school they weren’t safe.{w} What caused all this?{w} This phenomenon is beyond science – supernatural! I’d be a believer if I ever saw it with my own eyes."
    sr5 "Noted."
    is4 "You may proceed.{w} Excuse the hysteria."

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
    is4 "Hmmm... One of them is the student council president, am I correct?{w} That sounds someone like you. Hehehehe..."
    sr5 "A haunting thought, I must admit. {i}*chuckle*{/i}{w} But it is all finished. What interest is there if no harm is expected?{w} Anything else?"

    "Let me enumerate each cause of death again."
    "Electrocution,{w} poisoning,{w} blunt trauma,{w} \"slaughtered\",{w} drilled in the throat,{w} gunshot wound,{w} drowning,{w} crushed to death,{w} third-degree burns,{w} and hanging."
    "Six to four, and on the latter half of each month!{w} Half a grand-scale murder in my book, but the absence of \"Who, Why, and How\" deems it a supernatural case, no wonder!"
    "Sayo seems to agree with me."

    sr5 "Yes... We are on the same track so far."
    is4 "Brutal – what lack of a better word to describe it all."
    sr5 "Hmph. Lame.{w} I have {i}better{/i} ideas."
    is4 "Excuse me?"
    sr5 "That reminds me. There is one other detail I nearly forgot to bring up –{w} the story of Ikari Suzumoto."

    "My attention was replenished and I changed my seating position.{w} I might as well catch another outburst from her."

    is4 "The upperclassman? Tomonori-kun's batchmate?{w} Did you find any link between her and the crimes?"
    sr5 "I love how you label them as {i}crimes{/i}.{w} Actually, that's true. Our girl is a Sacred Heart Village resident herself."
    sr5 "There’s even a corresponding news article of her interview, published at the aftermath of Oizumi’s death."

    "I had forgotten about Suzumoto.{w} Yes. Her interview was in the front page of The Correspondent. She did address the victims, but never can you read a word about the night guard’s story."
    "It’s an obscure secret, outrageous to many if it's leaked.{w} And as Kyou described, a catalyst and precursor to the following tragedy.{w} It is,{w} however, far-fetched."

    sr5 "It’s doubtful, but all roads lead there.{w} The passage of time enforces the belief.{w} What interest is there in fighting the unknown?"
    sr5 "We, the firm believers of the scientific method,{w} have no ground against this{w} – an established supernatural phenomenon.{w} Quantum mechanics is the closest weapon, yes, but not enough. What’s to prove that dark matter truly exists?"
    is4 "You must be joking. The absence of evidence does not imply the work of demonic forces!{w} It is clear that the law has simply given up!{w} Such a gullible superstitious society we live in..."
    sr5 "{i}*sigh*{/i}"

    "I might have offended Sayo.{w} I haven't even thanked her for her efforts.{w} Best option is to lower my pride and {i}listen{/i}."

    sr5 "Do you believe in God?"

    "Definitely!{w} In my days here on Earth, how could I have lived not knowing the presence of{w} – I’m smothered.{w} This is where she wants me to be."
    "As a fellow theist, she’ll question my true belief – whether I’m truly devoted to it.{w} As a fellow rational student, however, she’ll find holes in my reasoning{w} – thus, there’s no way out!"
    "Silence, what Sayo wanted to hear.{w} I shook my head, acknowledging her words."

    sr5 "See? All knowledge cannot be done away with science.{w} There exists, however, at least {i}one{/i} explanation for everything{w} – under a superset of truths."
    is4 "This is getting off-hand.{w} Can we return to our previous topic, please?{w} You’re just making my head spin. You always do."
    sr5 "Forgive me. {i}*giggle*{/i} I tend to get touchy.{w} Philosophy is an intriguing subject, is it not? Hehehehe...{w} That is all I have uncovered; the past is done away with.{w} The question is, what of the present?"
    is4 "Uncertainty."
    sr5 "Say, an hour has passed by quickly.{w} It was a pleasure conversing with you tonight. Have your curiosities been quelled?"
    is4 "Yeah.{w} I honestly found it a healthy discussion.{w} But there are still some details that bother me..."
    sr5 "Try not to think about it that much. You have other problems to worry about.{w} Do keep in mind tonight’s discussion, though. There are a lot to ponder upon."

    window show
    nvl clear
    narr "The next last minute was spent exchanging farewells.{w} After hanging up, I am free to do whatever I wish.{w} What I need is a bed to fall upon."
    narr "I went upstairs, still thinking about it{w} – no, I shouldn’t let it bother me.{w} You’ve got things to do, Inoue. Focus.{w}"
    narr "Another hour passed{w} and I drifted off to sleep."

    nvl clear
    narr "The clock chimed nine times."
    narr "The sounds of {i}pitter{/i} {i}patter{/i} were still there, albeit more audible.{w} From the outside, Inoue’s face looked peaceful.{w} Internally, it’s a different story."
    narr "The chiming of the clock{w} – its pattern so hypnotizing it resonated a subconscious voice,{w} that of Sayo."

    nvl clear
    window hide

    sr5 "Star light, star bright,"
    sr5 "The first star I see tonight..."
    sr5 "I wish I may, I wish I might,"
    sr5 "Have the wish I wish tonight!"
    sr5 "Sleep tight, Inoue-chan.{w} Ehehehehehehehehe... {i}*giggle* *giggle*{/i}"

    "{b}{i}*beep* *beep* *beep*{/i}{/b}"
    return

label ch01_06_kyou:
    "JUNE 14, 2013 - 1140H"
    window show
    nvl clear
    narr "Lunch time."
    narr "The pathways are filled with students scurrying about looking for a good place to eat.{w} Most routines are simple{w} – buy from the canteen and return to the classroom."
    narr "The space around the campus is vast.{w} Maria St. Claire, being a single building,{w} has an open grassfield and trees overshadowing the walkways.{w} In fact, they constitute more than three-quarters of the total space!"
    narr "It offers a conducive environment for anything, barely having litter in sight.{w} The school is also the spearhead in keeping its surroundings healthy, what with its own organization dedicated to that task."

    nvl clear
    narr "Plate in hand, Kyou Kirisaki traveled back to his classroom, IV-A,{w} whilst having a chat with Sumiko, a IV-C student.{w} He sat at the third-row aisle, letting his eyes wander as he ate."
    narr "And he laid his eyes upon the front row.{w} Inoue,{w} uncharacteristically withdrawn and mind wandering aimlessly."
    narr "She was not a person to bother at her current circumstance.{w} It concerned almost no one.{w} Her friends were somewhere else, probably at the canteen or at the other classroom."

    nvl clear
    window hide

    kk9 "\"Anxiety in the heart causes burden,{w} but kind words cheer it up.\"{w} - Proverbs 12:25."

    "Slowly,{w} Inoue removed her hand from under her chin.{w} She turned to face the voice behind her."
    "She was greeted by a smile, the first few she had received that morning.{w} It took her an effort to show one herself{w} – false, nevertheless."

    is4 "I thank you for that,{w} but {i}that{/i} is the exact cause of my worries.{w} {i}*sigh*{/i}"
    is4 "Religion... is it ever true?{w} I still think it is but{w} they’re all the same."
    kk9 "You’re confounded.{w} Perhaps something went wrong last evening?"
    is4 "I’m not one to disclose secrets{w} and you know that, Kirisaki."
    kk9 "Ah, then I’m correct, I presume.{w} Say, how about I tell you a story, a parable, to ease yourself? Then it’s up to you to trust me or not.{w} Fair game?"
    is4 "No game.{w} I’m tired of it myself. I might have known every single one by heart – by {i}repetition{/i}."

    "I smiled in full understanding.{w} I gathered my thoughts - what she did for the past few days and anything that was a cause for concern.{w} Nothing, perhaps..."
    "Oh! I remember now{w} – the conversation nine of us had last week."

    kk9 "Tell me about it, Inoue.{w} You’ve looked it up. I mean,{w} the \"Sacred Heart Curse Killings,\" were they?"
    is4 "You know of it?{w} Who told you?!"
    kk9 "I know nothing beyond our gathering last Friday.{w} I see you harvested some new knowledge.{w} Worry not, for I know how to zip my mouth."
    is4 "To tell you the truth, Kirisaki,{w} the tragedy itself is not my concern.{w} I’ve seen far too many horror movies bearing a similar premise. Is this alright?"
    kk9 "{i}*chuckle*{/i} What is?"
    is4 "It’s Sayo.{w} I talked to her{w} – no, she contacted me yesterday evening to talk about it.{w} And she mentioned some... {i}trivial{/i} quotes."
    is4 "There are a few things I want to consult with you.{w} You’re the pious one, someone wiser than me."
    kk9 "Hmmmm...{w} Was there anything off in her manner?"
    is4 "Set that aside for now.{w} I’d like to momentarily clear up some affairs,{w} {i}personal{/i} things."

    window show
    nvl clear
    narr "I gave attention to her words and her delivery.{w} Perhaps, not as I had initially thought,{w} there is something deeper behind her anxiety."
    narr "Only then I knew."
    narr "She related to me the details of the tragedy, one I know beforehand.{w} I researched it myself. Then came the bits after that{w} – questions about science, theology, and the supernatural."
    narr "There are times she’d get herself lost in her story,{w} so I demanded she get to the point."

    nvl clear
    window hide

    kk9 "So, I ask of you,{w} what do you truly believe in?"
    is4 "That all of these have plausible explanations, however difficult,{w} and none involve the Hand of God whatsoever."
    kk9 "That’s in your heart,{w} hundred percent?{w} Or a ninety-nine?"
    is4 "*{i}sigh*{/i} Less.{w} I can’t give you an exact figure."
    kk9 "Inoue, I may be a religious person, as you say,{w} but there are times where certain explanations hold water and there are those where they do not.{w} The tragedy has more of the former."
    kk9 "The concept of karma shades some of these, as in the case of Shibuya and Suzumiya.{w} The two died in different ways{w} – every one of them did, correct?{w} Science still holds water."
    kk9 "The aftermath of each death is definitely subjective.{w} In my view, the souls of the dead undergo judgment, depending on their character.{w} That, however, has little bearing on the motive unless otherwise."

    "Inoue was quite puzzled, no matter how brief an explanation I gave her.{w} A long pause occurred, allowing me to finish my meal.{w} She raised another question."

    is4 "If not religion, then what about quantum theory or the supernatural?{w} I’ve been told that not everything can be touched by science{w} – yet there exists a superset of truths...{w} I don’t know."
    kk9 "Then it appears you are mistaken."
    is4 "Mistaken?{w} It is too convoluted!{w} There is only so much for me to comprehend."
    kk9 "If that’s so, let’s untwist the facts slowly.{w} First, how did you distinguish those that were accidents rather than murders?"
    is4 "The nature of the deaths themselves."
    kk9 "Even as a possibility?"
    is4 "Based on the way they were told.{w} If I judged corrcetly, six to four."
    kk9 "There’s a minor detail I picked up.{w} You said Suzumiya was {i}killed{/i} when she drowned {i}by accident{/i}{w} – a clear dissonance."

    "Her eyes widened in genuine surprise.{w} Inoue contemplated upon herself whether her version is correct."

    is4 "Kirisaki, are trying to insinuate{w} foul play?"
    kk9 "Unless you meant the waters killed her, but that would be a morbid personification.{w} If not, then the scores are even.{w} That disproves the idea of an accident."
    is4 "How? I... I’m lost.{w} The conditions for an accident are favorable around the time of her death."
    kk9 "Let no accident or intuitions assist the detective,{w} or so it says."
    is4 "Kirisaki, this isn’t a murder mystery!{w} This is real life – anything could happen.{w} Are you trying to Sherlock me?"
    kk9 "Hehehehe... Pardon.{w} I may seem to have taken it too far."
    kk9 "But my point is this{w} – for every effect there is a cause, the evidence present or not.{w} Take my word on Suzumoto-san’s story seriously, but take care not to venture into the unknown excessively."
    kk9 "That, and pray you keep a rational thought ready.{w} Naivety won’t get you too far,{w} but I’m not saying you are."
    is4 "I understand.{w} And Kirisaki, I must offer my thanks for suppressing my worries.{w} I’ve been thinking about them since last night."
    kk9 "My pleasure. {i}*chuckle*{/i}{w} Is there anything else you wish to consult me about?"
    is4 "Darn! My meal’s gone cold, but that’s fine.{w} Luckily, my seatmates aren’t here yet.{w} About my last point..."
    kk9 "Ah, yes! It almost slipped my mind.{w} It was my concern anyway, so please continue."

    window show
    nvl clear
    narr "Inoue is quite a hospitable and level-headed person,{w} save for situations such as this.{w} Just like the first part of our conversation, she spoke while I listened."
    narr "Then, in the middle of it, I was struck with concern – with doubt.{w} Sayo and I were classmates during our sophomore years,{w} and I can recall specific instances when we’ve talked."
    narr "But not in the way Inoue described their conversation to me."

    nvl clear
    window hide
    return

label ch01_07_countdown:
    "JUNE 15, 2013 - 2300H"
    window show
    nvl clear
    narr "Pairs of feet shuffled across the function room.{w} Though busy, the Youth Group members eased themselves through friendly chatter.{w} A six-hour prayer vigil is scheduled at midnight."
    narr "The front-right door creaked, letting in a small figure with spectacles.{w} Sayo Ronoroa approached the chancel, greeted her church mates, and placed the music book on the stand."
    narr "She opened it a few pages from the middle.{w} Satisfied, she went over to the other members to help."

    nvl clear
    narr "The banner, already set in front of the room, proclaims -"
    narr "SQUIRES OF THE HERALD KING YOUTH GROUP"
    narr "They were a relatively small group, having fifteen registered members.{w} They attend a 3rd Sunday Prayer Vigil as a regular devotion. Attendance is non-compulsory in case of emergency."
    narr "At the back, Sayo wiped away the sweat from her forehead.{w} She entertained thoughts during her idleness, and to each she smiled dearly."

    nvl clear
    narr "The conception of the highest seat during the last gathering{w} and this night for the school year’s blessing!{w} How fortunate it is to have been a member of this Youth Group."

    nvl clear
    narr "It was all thanks to Ikuko Mimori, a classmate one year longer in service.{w} The month after Sophomore year, she invited Sayo to the Youth Group.{w} As a result, their relationship deepened between themselves and the Higher Being."
    narr "Sayo is forever grateful."
    narr "As they waited for the bell, they brought up a variety of topics. How they have been, the current events, personal thoughts,{w} anything they could come up with."
    narr "They left no room for gossip, strictly adhering to their moral code.{w} Sayo mentioned the gathering once more, but no traces of neither the previous tragedy nor her conversation with Inoue.{w} She chose her stories well so as not to gloom the night."
    narr "Instead, they opted to discuss the vigil’s flow, midnight to dawn.{w} They rehearsed the words in their minds, filling in gaps whenever there is one."

    nvl clear
    window hide

    sr5 "1 Corinthians 16:9-13...{w} it comes with the Daily Bread.{w} At two in the morning, preferably?"
    ikuko "Yes. That would be a good placement,{w} though I’d rather have it at five, just before dawn."
    sr5 "Then five it is if you wish!{w} You’re the one in charge of the overall flow."

    window show
    nvl clear
    narr "The Daily Bread Reading is one of their primary segments during a vigil.{w} Unlike other activities, it is spontaneously placed at any timeslot the members prefer, usually within an hour before dawn."
    narr "Its placement is left to the one in charge of the program, Ikuko at present."
    narr "As an assignment, each member is asked to give their reflection about the passage used in the reading.{w} This is to deepen their spiritual understanding and to learn from each other."

    nvl clear
    window hide

    sr5 "Here’s what I make of this{w} – the truth of human nature.{w} To make an effort in concealing what’s underneath is a natural process; it persists against all effort."
    sr5 "Fear, not courage, is what makes men truly interesting.{w} To exploit those as a weapon is to have him realize the insufferable truth – stigmas that last forevermore."
    ikuko "And when misfortune befalls one, the mask vanishes and all impression falls apart with it.{w} Empathy bridges the effects as a ripple."
    sr5 "Correct.{w} Hence the relevance of the vigil’s theme."
    ikuko "It skirts the wishes of St. Paul; at the same time, you’ve struck the chord.{w} Isn’t that common knowledge though?"
    sr5 "A safe assumption, if not banal.{w} Only a heartless would be as bold as to fear nothing.{w} Death perhaps,{w} but it bars none!"
    ikuko "Compose yourself, my friend. Your emotions are driving you away again. {i}*chuckle*{/i}"
    sr5 "My apologies."
    ikuko "But surely, you’ll drop some of it in the discussion later?"
    sr5 "It perturbs most, admittedly.{w} I’d rather discuss it in private and to those with an open mind.{w} Fascinating, isn’t it? {i}*chuckle*{/i}"

    "Their smile drew a mutual air of satisfaction.{w} What could possibly make the night more interesting?"

    "Earlier This Evening..."
    window show
    nvl clear
    narr "Ichirou, as class president of IV-B, made his final announcements online."
    narr "With books and backpack made up, he called it a night.{w} But not before going for a few rounds of Candy Crush."

    nvl clear
    narr "In contrast, Miyu retired to bed with his cell phone radio, a perfect opportunity to lose himself in thoughts.{w} Occasionally, he would exchange messages with Sanae Yoshida, a former classmate of his."
    narr "A healthy friendship they had – a durable link.{w} \"Nothing better than to pass away the dullness!\" he would reason.{w} And when it stops, he would return to his activities."
    narr "First Law, indeed."

    nvl clear
    narr "Ever forgetful, Sumiko’s eyes ran through the monitor several times.{w} His mind relaxed upon the sight of his announcement on class IV-C’s FB group."
    narr "\"Wear your PE uniforms on Tuesday – we have a social dance activity at first period. Just this Tuesday, friends. Good night!\""
    narr "Akira commented on the post, volunteering to bump it the following day.{w} Sumiko liked this idea, despite realizing it only as a jest."

    nvl clear
    narr "{b}*BEEP* *BEEP* *BEEP*{/b}"
    narr "The thermometer read 39.0C."
    narr "As Inoue suspected, she had symptoms of flu.{w} She took a tablet of paracetamol and her mother advised her to stay in bed for the weekend.{w} Inoue desired to protest, but she could not."
    narr "It was peculiar, as she traced the cause to none.{w} Thankfully, she was free from dengue – that could have been much worse.{w} It is possible that she will miss Monday’s activity so her mother prepared a letter in case."
    narr "At present, Inoue relaxed her mind;{w} her body comfortably snuggled under the fluffy blankets.{w} No signs of worry as it might worsen her condition."

    nvl clear
    narr "Yoshiro decided to look up the Sacred Heart tragedy, finding its \"cursed\" label intriguing.{w} It was, as he thought, as grounded as possible{w} – yet inhuman."
    narr "He remembered the upperclassman’s story and tried to establish a connection.{w} Zero,{w} apart from the latter’s residency similar to that of the victims."
    narr "Just then, questions came to him."
    narr "What if the \"catalyst\" perceived an omen?{w} It made no sense even as an aversion – an inverse example – yet...{w} if it was actually delayed, then..."

    nvl clear
    narr "Hiroshi placed {i}The Battle of the Labyrinth{/i} down after the last chapter.{w} It had him thinking, given the nature of the book.{w} Its theme blended too well with their topic, triggering some thoughts within him as he read."
    narr "In the darkness, he laid in silence tuning his mind the same as Yoshiro's is.{w} He considered the possibility of having Suzumoto as a suspect."
    narr "He laughed at himself, aware of the idea’s absurdity."
    narr "Suppose it happens again?{w} That is a haunting thought, but it better be fairer than the last.{w} Best case if it doesn’t.{w} Ever."

    nvl clear
    narr "There was nothing different about Hikaru, spending the weekend on her laptop as usual.{w} She was streaming shows from the US, indulging herself as much as she wished."
    narr "The props for Tuesday’s activity lay at her bedside.{w} Sumiko gave her a spare key should she ever arrive before six."

    nvl clear
    narr "Kyou received the same instructions from Inoue.{w} However, the class president was ailing and unsure of her condition come Monday.{w} He possesses one of the keys being the earliest in their class."
    narr "He heard of Inoue’s condition and wished her health to return.{w} Kyou thought that she was merely stressed out."
    narr "But as he thought about the previous day, he considered the cause."

    nvl clear
    narr "There were things out of place, such as Sayo’s behavior during the phone call.{w} He only has Inoue’s word for it, and she could be making it up.{w} But it was genuine – nobody would dare lie to him; he abhors those."
    narr "But words alone wouldn’t cause an ailment{w} – or rather..."
    narr "At times like this, he would do some soul-searching to quell himself.{w} He picked up his Bible and began meditating on a few verses."
    narr "Afterwards, he opened his Daily Bread and marked the entry for June 15.{w} He scanned the next entry for June 16, {i}Strength of a Man{/i}, and reflected upon himself."

    nvl clear
    window hide

    kk9 "Quite fitting.{w} {i}*sigh*{/i} I’ll save this for tomorrow evening."

    "{b}{i}*RING* *DING* *RING* *DING*{/i}{/b}"

    window show
    nvl clear
    narr "The oft familiar tune called everyone’s attention, all fifteen of them.{w} The two girls walked together to the front and took their places at the chancel."
    narr "Sayo led the small choir by playing the keyboard, with the music book page in full view.{w} Ikuko glanced at her friend, twinkled, and began the vigil."
    narr "By the twelfth strike, the Youth Group members performed the opening hymn.{w} No hiccups and all went smooth from there.{w} Everything went as planned."
    narr "Brilliantly executed – one should say."

    nvl clear
    window hide
    return

label ch01_08_disappearance:
    "JUNE 18, 2013 - 1130H"
    window show
    nvl clear
    narr "Class IV-C was livelier than usual.{w} Topics about the social dance activity buzzed around the students - who looked handsome and lovely, who made the most graceful steps, and whatnot.{w} Some were even considering their prom dates this early."
    narr "There are a few exceptions, such as Sumiko and Akira."
    narr "At present, the three – adding Ichirou – discussed the upcoming College Entrance Exam review sessions.{w} The Science Club is one of the event's major facilitators."
    narr "Miyu handed the signed document to Ichirou, which the latter accepted."

    nvl clear
    window hide

    mh8 "I shouldn’t be the one doing this.{w} Isn’t she in good health already?"
    iy1 "Nope.{w} We’d be chewed out if we waited until tomorrow. Today’s the deadline."

    "Miyu acknowledged it and went out to have lunch.{w} Sumiko signed a similar document."

    st3 "So Kyou followed after Shinozaki, huh? Hehehehe. What rain could do to people...{w} I saw him yesterday during the assembly and he looked fine."
    iy1 "So did I.{w} If only we were given the agreement yesterday, I wouldn’t have come to you.{w} But then again, Shinozaki still has flu."
    st3 "Flu? Who told you that?"
    iy1 "Kyou.{w} I exchanged a few words with him yesterday during break time and he mentioned Inoue's condition. Hope she gets better."
    ai2 "That aside, you’ll send this to Sayo after Nakashima signs?{w} They are in the same class."
    iy1 "Ayumi? Yeah, I’ll send her copy before giving it to Sayo.{w} The girl’s probably buying some food right now."

    window show
    nvl clear
    narr "The conversation went on for a bit until Ichirou noticed Ayumi return.{w} He left the two and thanked them.{w} At the same time, Miyu returned, sitting one row ahead of the two."
    narr "At exactly noon, Sayo passed by IV-C.{w} It was an unusual sight –{w} the bubbly girl worried about something this early in the year.{w} Her face evidenced her anxiety, but her gait remained the same."
    narr "When she was no longer in sight, Akira shook his head in sympathy."

    nvl clear
    window hide

    ai2 "Gosh. Don’t tell me their class didn’t do well in the activity.{w} Poor Sayo looks like she lost some stocks{w} or a pile of chips."
    st3 "Hahahahahaha! That’s a good one.{w} But I suggest we make no further jokes. It could be worse than we think."
    ai2 "Or maybe she could be tired. Seriously, it’s the same for us."
    ai2 "Oh!{w} Here’s the spare key.{w} I might risk losing it."

    "Akira produced a small silver key from his wallet and gave it to Sumiko.{w} The latter hesitated, asking if he will come later than usual.{w} Akira, however, insisted."
    "Sumiko shrugged and passed it to Akira’s service mate.{w} She glared at Akira whose face contorted with embarrassment.{w} She threw the spare key back to him."

    window show
    nvl clear
    narr "{i}The subscriber cannot be reached. Please try again later.{/i}"
    narr "The same robotic voice returned my call for the third time.{w} I tried to reach Inoue since morning, hoping to check on her, but without luck."
    narr "That alone was unusual{w} – she never misses calls twice or even thrice during weekdays.{w} I knew that since we were freshmen.{w} If today was Sunday, that’ll be alright."
    narr "I don’t have Kirisaki’s number so I’ll just have to ask their adviser about it."

    nvl clear
    narr "I opened the door to the faculty room and looked around.{w} There’s Mrs. Genkai chatting with Ms. Harada."
    narr "Perfect.{w} I’ll hand these to Mrs. Genkai before I ask Ms. Harada about the two."
    narr "Before I conducted my business, I gave a polite gesture they received gracefully.{w} I wasted no time."
    narr "Luckily, Ms. Harada took the initiative by asking me about Inoue and Kirisaki.{w} Having no idea on their condition either, she took out her smart phone and dialed the Shinozaki residence first."
    narr "We all waited in anticipation."

    nvl clear
    window hide

    t_gen "You’ve eaten well, Sayo-chan?"
    sr5 "Yes, but not as well.{w} I’ve been trying to contact Shinozaki since this morning and I couldn’t reach her.{w} Whatever happened to that girl?"
    t_gen "Well, at least Hirano is present for these papers.{w} Tokubei too.{w} I’ll save the questions until we get through."
    sr5 "I’ll stay for a while.{w} I too, am worried about them."
    t_har "Uh, hello? Is this Inoue Shinozaki's mother?{w} This is her adviser, Ms. Harada, speaking."

    "She managed to connect within a minute.{w} The conversation with Mrs. Shinozaki took place in loudspeaker, with Mrs. Genkai and me listening closely."
    "I gathered the following after the pleasantries."

    t_har "I apologize for calling on such short notice, Mrs. Shinozaki. You might be busy.{w} Tell me, how is Inoue doing?"
    ms_shi "She’s alright.{w} Her fever went away yesterday morning and she’s her former self, thankfully. {i}*chuckle*{/i}{w} Did she miss anything important, madame?"
    t_har "Some agreement paper due this afternoon, which is already done away with,{w} and a practical activity.{w} The latter is alright provided she’s in the condition to perform."
    ms_shi "I’m sorry. When was this? Monday?"
    t_har "This morning – second period. Eight o’ clock."

    "There was silence.{w} I sensed the confusion from the other end."

    ms_shi "That’s not possible. I saw her off this morning at quarter to six.{w} She didn’t go off anywhere, did she?!"
    t_har "I refuse to believe that.{w} Unless I'm mistaken, we never saw her this morning.{w} Being in my advisory class, I never forget a student – {i}especially{/i} our class president."

    "What?! How is that...?{w} A crack in Mrs. Shinozaki's voice... and in disbelief.{w} There must be a mistake!"

    window show
    nvl clear
    narr "Even without continuing, we shared the same conclusion{w} – Inoue Shinozaki has vanished.{w} No traces of her anywhere,{w} neither in her home nor here at school."
    narr "As Ms. Harada tried to calm Inoue’s mother down, I settled down to think.{w} However, the shock I received clouded my thoughts.{w} I wanted to cry, but I retained my resolve."
    narr "Who would want to see the head of the student body cry? That'll shatter the morale of people."

    nvl clear
    narr "Ms. Harada gave instructions to file a missing person report immediately in case of kidnapping.{w} Then, she cut the line."
    narr "Seeing her distressed from the facts, I offered my seat and gave her a glass of water."
    narr "My fears worsened. I even considered alerting the student body to prevent a future case.{w} However, with no knowledge of Inoue’s condition, I refused to take action.{w} It was rash."
    narr "Mrs. Genkai kept a level head throughout the whole affair, agreeing to keep it among the three of us.{w} No other faculty member was in proximity."

    nvl clear
    narr "I left the faculty room, requesting to keep in touch with Ms. Harada for any updates.{w} I last saw her feebly picking up her smart phone and dialing another number, most likely the Kirisakis.{w} I felt sorry but I have to zip my mouth."
    narr "What interest is there, I suppose?{w} Announcing it publicly would cause discord and panic."
    narr "I returned to IV-E, avoiding to speak to anyone.{w} I needed to think, and take my mind off it."

    nvl clear
    narr "Ten minutes before the fifth period, a murmur emanated from outside.{w} Normally, a few of my classmates would check it out only to dismiss it immediately.{w} I paid it no attention."
    narr "This time, more and more people went out.{w} I glanced at the window, noticing a crowd forming from even the other classes.{w} I recognized that sound."
    narr "An ambulance!"
    narr "I joined the crowd and saw the source personally.{w} Sprinting towards it, I saw the patient being taken away.{w} Mrs. Genkai stood at the walkway, wiping her sweat. She looked pale."

    nvl clear
    window hide

    sr5 "Excuse me, madame. What’s the commotion?"
    t_gen "I had to assist a fellow faculty down after an attack.{w} {i}*sigh* Could this day go any worse? She’s had enough already.{i}"
    sr5 "She? You mean –"
    t_gen "Correct.{w} The patient is Ishii-san.{w} She called Kirisaki’s residence immediately after you left.{w} He was the other student absent from her class, if I recall."

    "Oh no. Tell me the worst."

    t_gen "Before she blacked out, I heard the following over the line, though it wasn’t in loudspeaker,"
    t_gen "'{i}Don’t tell me my son is missing!{i}'"

    "JUNE 18, 2013 - 1650H"
    window show
    nvl clear
    narr "{i}Attention to all students.{w} Please remain at your homerooms for the next half hour. Your advisers have an urgent matter to discuss with you.{w} Class IV-A, your co-adviser shall meet you in behalf of Ms. Harada.{w} Thank you for your cooperation.{/i}"
    narr "The impromptu announcement caused an air of concern among the students.{w} While some of the underclassmen were already dismissed an hour ago, the rest were forbidden from leaving."
    narr "They all saw it{w} – the image of Ms. Harada out cold on the gurney.{w} A few sulked, with some others discussing.{w} Exactly what happened? Why are they being detained?"

    nvl clear
    window hide

    "Mrs. Ren Kanako entered IV-C, settling down immediately.{w} Sumiko took second-charge in handling the class."

    t_kan "Hope you’re all well.{w} Let’s see... One, two...{w} 42 heads. Good!"
    t_kan "You must have witnessed the scene at 12:30 this afternoon and must be concerned for Ms. Harada’s condition.{w} She’s presently stable, if a little somber."

    "Audible sighs of relief were heard, yet they were not satisfied.{w} The teacher proceeded with the announcement, almost cut short by an uproar in the neighboring class."

    t_kan "You heard IV-B –{w} this is no pleasant news.{w} Two of your batch mates from IV-A, Inoue Shinozaki and Kyou Kirisaki...{w} they disappeared this morning."

    window show
    nvl clear
    narr "These words induced fear to the students.{w} Someone dared to ask a question{w} but Sumiko shot him down, asking him to wait."
    narr "She grew stern discussing the details of each disappearance,{w} laying them down fact by fact, disallowing herself to speculate.{w} The cases have been reported to the authorities and an investigation shall commence soon."
    narr "Until then, the students are urged to head straight home as soon as classes end or when their cleaning duties are over.{w} When it was all done, she entertained Yoshiro, who attempted to ask earlier."

    nvl clear
    window hide

    ys6 "Pardon the interruption earlier, madame.{w} This is more of a thought than a question in itself, but{w} is kidnap possible?"
    t_kan "That’s the likely case.{w} In fact, we advised both families not to respond to any ransom until the suspects are identified."

    "Sumiko was no longer able to contain the crowd’s restlessness.{w} Mrs. Kanako soothed her students, unwilling to worsen their emotions."
    "Minutes passed with seemingly endless queries about the incident –{w} where and when they were last seen and a few personal questions.{w} Then, Miyu stepped forward to speak."

    mh8 "Madame, we may just have enough information mostly from you."
    mh8 "From what I can surmise, while they may have been abducted between five to six in the morning,{w} I believe the two instances are {i}not{/i} related in any way."
    "\"WHAT?!\" {b}*GASP*{/b} \"What is he talking about?\""
    t_kan "Please clarify. I did not catch the last bit."
    mh8 "What I meant is,{w} despite the similarity in time of Shinozaki and Kirisaki’s disappearance,{w} I doubt the two bumped into each other this morning beforehand."
    mh8 "How do I know?{w} Simple. I arrive here every 5:45,{w} and most of the time, I see Kirisaki sitting out at the bench – this morning an exception.{w} Shinozaki arrives at around six, latest delay at fifteen minutes."
    ai2 "He isn’t lying, madame.{w} I’ve only gotten here twice without Miyu already inside.{w} I support his statement as well, but I honestly don’t see how the two didn’t meet this morning."
    hy10 "Excuse me, madame. If I may,{w} I was temporarily given the second spare key as I needed to arrive at 5:30 for the dance activity preparations.{w} I never saw anyone else inside, up until Akira arrived."
    hy10 "I never saw Miyu."
    mh8 "You didn't.{w} I was in the bathroom at the time.{w} When you've got to go, you have to. {i}*giggle*{/i}"
    hy10 "..."

    window show
    nvl clear
    narr "Regardless, Inoue’s case is a dead end.{w} It hinges on everyone thinking she is still unwell.{w} Then again, they only have Mrs. Shinozaki’s word for it."
    narr "As for Kyou, however, his is a legitimate case.{w} Consequently, Inoue's case becomes one."
    
    nvl clear
    narr "Rather than intensify the situation, nobody chose to speak further.{w} Instead, Mrs. Kanako arranged for a few changes in their activities.{w} She informed them of the stricter curfew time,{w} from 6:30 to 6:00."
    narr "After forty minutes, the meeting adjourned.{w} She ensured that the students empty the classroom, save for the day’s cleaners.{w} When they were nearly done, she gave her final instructions to Sumiko."

    nvl clear
    window hide

    t_kan "Sumiko, see to it that none of your classmates go astray.{w} I plead you, we shun another case!{w} Please relay my words to the rest."
    t_kan "I’ll leave the rest to you."
    st3 "Understood{w} Keep safe, madame."

    "As the teacher faded from his view, so did the sun.{w} It bore witness to the day’s events – times of order and confusion{w} – similar events repeating themselves too often they can be glossed over safely."
    "And curiosity?{w} What interest is there, indeed?{w} Hence, no further mention is necessary."
    return

label ch01_09_labkyou1:
    "JUNE 18, 2013 - Time Unknown"
    window show
    nvl clear
    narr "I’ve never arrived this early at the city square.{w} The moon and incandescent lamps as light sources, my brother and I walked across to the wet market.{w} He needed report materials; so did I,{w} but for a different reason."
    narr "I brought the class’s materials in advance yesterday,{w} but the Creatives Committee ran short late at night, our progress barely satisfactory.{w} As the earliest to arrive, I volunteered myself."
    narr "Our head told me that the market stalls would be open as early as five.{w} My brother insisted on coming along; I accepted, since we always went to school together."
    narr "Along the way, we ran into a vagrant sniffing from a plastic bag.{w} With God watching us, no harm may befall us."
    narr "We exited the market, the sun peering out a bit.{w} The square slightly increased its population, mostly students and employees."
    
    nvl clear
    narr "We wished Onifuchi-san, the gate guard, a blessed day as usual.{w} The same went for the other guard at the front desk."
    narr "We parted ways, giving each other a fist bump, once we reached the staircase near IV-A.{w} The Senior-Year classrooms were devoid of life{w} – not even Akira, Miyu, Sayo, nor any of my classmates are present."
    narr "I inserted the key and unlocked the classroom door.{w} The creepy vibe left me once the lights turned on.{w} I neatly arranged the materials – a ball of nylon thread, assorted colored papers, fans, among others."
    narr "The sky brightened a little,{w} and I settled myself down.{w} Once more, I ran through our list and messaged the committee.{w} With a beep of confirmation, I let myself doze off."

    nvl clear
    window hide

    unk "{b}*COUGH*{/b}"

    window show
    nvl clear
    narr "It bothered me since weekend.{w} Just go away... the medicine should off you soon enough.{w} The placebo should quicken the process."
    narr "Now that’s much better.{w} Praise the Lord."
    narr "The air is giving me the chills.{w} The radio anchor reported a 24-degree morning, not a ten! What time is it now?"

    nvl clear
    narr "{i}*clatter* *clatter*{/i}"

    nvl clear
    narr "Only muddled sounds registered in my ears.{w} I feel detached from my body, much like in a lucid dream.{w} It’s another experience of mine, yet it feels{w} quite peculiar, more than ever."
    narr "I only felt my head, pounding from a lack of sleep.{w} I could’ve brought the pillow we made in Home Economics class before."
    narr "My eyes opened, waiting for the image to focus itself."
    narr "Hang on...{w} the ceiling’s farther than before.{w} Surely, I haven’t –"

    nvl clear
    narr "{i}*clatter* *clatter* {b}*CLATTER*{/b}{/i}"

    nvl clear
    narr "Wait...{w} This isn’t our homeroom!{w} Where am I?!"
    narr "{i}{b}*CLATTER* *CLATTER*{/b}{/i}"
    narr "A maniac – a demon{w} – is holding me hostage!"
    narr "I rested myself for an hour, trying to endure the painful bout in my head.{w} It feels worse than being a zombie."

    nvl clear
    narr "Floor to ceiling, I studied the room’s layout.{w} The room I’m in is at best,{w} depressing,{w} barely any furniture in sight, save for the bed and desk at my side."
    narr "I cannot go any farther{w} – my feet are shackled tightly at the two foot-side bedposts.{w} The other option, therefore,{w} is to search. Plenty points of interest in sight."
    narr "There are three drawers –{w} the middle containing a few markers and a rug, the top with a spare light bulb, and the bottom empty."
    narr "Other points of interest – the lampshade’s underside and the space beneath the bed,{w} nothing."
    narr "I scrutinized the pillow last, feeling it all over.{w} At the underside, I felt a thin solid rectangle with a bump converging to the middle.{w} My eyes flashed when I found the object."

    nvl clear
    narr "An envelope!"
    narr "The devil must’ve inserted this before I was detained.{w} A small key accompanied the letter, which fit the chain's lock perfectly.{w} It gave me a bit of freedom,{w} but there is still that barred door with a weird device beside it."
    narr "The letter piqued my curiosity,{w} so I sat down and examined its contents.{w} Addressed at the back of the envelope is my full name – no sender or a postage stamp visible."
    narr "The parchment looks new but creased, courtesy of myself.{w} I didn’t recognize the handwriting, but{w} it does strike some familiarity."
    narr "What follows is a short message from whom I dub \"Mr. X.\""

    nvl clear
    narr "{i}You’ve awaken,{w} Kyou Kirisaki.{/i}"
    narr "{i}No doubt, you lived the past few days on repeat {w}– only to end, sadly, in pain.{w} If not, what is the term again?{w} Apnea – yes, I figured you would cease breathing at some point in limbo.{/i}"
    narr "{i}It’s a meager, nevertheless.{w} I’ve no desire to waste your time, so I present my terms, \"rules\" you may refer them.{/i}"
    narr "{i}First,{w} you seek the truth for yourself.{w} I know well enough that you are a man of God and an enthusiast of Science;{w} thus, you can piece the facts scattered around here. Empty your mind...{w} \"Naivety won’t get you too far, but I’m not saying you are.\"{/i}"
    narr "{i}Second,{w} know that you aren’t alone in this place.{w} It could be me, another soul, or your God, if you prefer.{w} The catch is, you come out of here alone – no companions.{w} Leave everything behind and think for yourself...{w} think as if nobody exists.{w} I don’t either.{/i}"
    narr "{i}The third applies if{w} I don’t find you as a cadaver the next morning.{w} You’ll tell me everything{w} – how you perceive rationality – they all intrigue me.{w} What is a \"catalyst\" in your sense?{w} Whatever you hold, I'm certainly expecting more than that.{/i}"

    nvl clear
    narr "{i}Otherwise,{w} you keep your word.{w} I’ll tell you everything in return{w} – about me and why I involved you in this.{w} You best hasten your steps{w} – your dear brother is worked up, with lack of a better word.{w} In fact, you share a mutual feeling.{/i}"
    narr "{i}I must warn you,{w} no refusals.{w} You MUST play by the rules.{w} The clock is already ahead of you – once it stops, you can never start it again.{w} A fair bargain if you consider my offer carefully.{/i}"
    narr "{i}Welcome to purgatory.{w} I sincerely hope you find your stay rather... endearing.{w} I shall see you soon.{/i}"
    narr "{i}Signed,{w}\nL.C.{/i}"

    nvl clear
    narr "Malice – the letter is peppered with it. Mr. X,{w} or rather, L.C., makes no effort to mask it.{w} He wants my skin, no doubt.{w} It just bugs me why he opted for his theatrics instead of doing away with me immediately."
    narr "Speaking of, where is my watch{w} and my phone?!{w} He disposed of them, unsurprisingly."
    narr "No time to waste! I’ve no choice but to play his game if I wish to live.{w} I’ll keep this letter for reference."

    nvl clear
    narr "What truth is he talking about?{w} He knows more than I am – far too much to be a stalker.{w} Set aside the second reading for later. Getting out is top priority{w} ...if only I can crack this device."
    narr "An electronic device, Dvorak-styled keyboard and LCD screen, barring my escape.{w} The magnanimous fellow fitted a similarly-sized transparent board which functions as its cover."
    narr "There are instructions above the device, printed this time."
    narr "{i}You could just brute-force the passcode, but I’ve removed the bots from your vicinity should it occur to you.{w} Might as well retain the cover where it’s supposed to be than vainly trying to remove it.{/i}"

    nvl clear
    narr "Nonsense!{w} There must be an inscription in this room or a keyword in this letter.{w} An expected reaction from me, nonetheless. Well-played!{w} I typed several words from the letter, hoping they would come through."
    narr "The bars did not move an inch.{w} {i}Access Denied{/i} – all of them!{w} At this point, I’m tempted to follow his ridiculous advice.{w} Sadly, I don’t even know the length of the passcode.{w} Let’s try something else, shall we?"
    narr "Specimen A:{w} the items in the middle drawer.{w} Probably useful for something else that I have no idea at present."
    narr "Specimen B:{w} the spare bulb in the top drawer.{w} If I replace the lamp’s bulb, what would be different?{w} It looks fine to me, evidently fresh. I only glossed over the former, honestly."
    narr "The bulb caught my attention. The glass is dark in color.{w} So, this must be a UV light bulb.{w} I switched the one currently installed with it."
    narr "My eyes confirmed my thoughts."

    nvl clear
    narr "With this, there are now stray marks visible on the letter,{w} just random scribbles.{w} Flipping it around, a message eventually turned up on the paper’s middle section."
    narr "{i}Double lens. EASY, does it?{/i}"
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
    narr "The bars gave way to me, allowing the metal door to open freely.{w} From beyond is an empty corridor, well-lit unlike this cell.{w} Two doors are visible – one at the other end, the second just near the first at the left side."
    narr "Sneaky devil – I should be grateful for his invocation.{w} He might be clever, but as long as God is with me, nothing is impossible.{w} That’s the spirit.{w} As Dostoyevsky once said through Rodion Raskolnikov, \"May the Devil take the fool.\""
    narr "He’ll not lay a finger upon me{w} – never!"
    narr "{b}*BOOM* *CRACKLE*{/b} {i}*hiss*{/i}"

    nvl clear
    window hide
    return

label ch01_10_labinoue1:
    "Date Unknown - Time Unknown"
    window show
    nvl clear
    narr "I feel worse than a caged canary."
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
    unk "Thus, I welcome you as a guest,{w} and a guest you’ll {i}no longer be{i}.{w} Godspeed, Shinozaki, and retain your resolve.{w} The facility does not take such matters lightly."

    window show
    nvl clear
    narr "I didn’t hear the recording cut itself; I let it run just to be safe.{w} The piano keyboard has 36 keys, starting with C and ending with B.{w} Pressing each once, they worked just fine."
    narr "A little tune broke through the silence."
    narr "It’s probably a nursery rhyme, judging from the music box-like arrangement.{w} The music soothed my nerves.{w} I’ve no clue of the next step, so I lied down.{w} I awaited an answer,{w} or better,{w} death."

    nvl clear
    narr "This is the extent of it all, eh?{w} Secluded in a world not my own, there exists an odd feeling of serenity.{w} The ceiling animated itself,{w} projecting my subconscious thoughts.{w} I can see myself perfectly without a mirror."
    narr "This is the face I never showed anyone,{w} not even Sayo.{w} I gave a ninety-nine at best, a façade Kirisaki almost saw through.{w} L.C. is a special cookie, making him or her an exception."
    narr "Images flashed across the ceiling.{w} Memories of the past days manifested on those."
    narr "{i}Ten{/i} victims from Sacred Heart Academy...{w} and one impacting detail still etched into my mind.{w} Perhaps it was thanks to Sayo that I found the tracks to the truth I’m seeking."
    narr "What business do I have with them?{w} Ikari is involved somehow{w} in the most minimal way possible.{w} I know her personally – she and big brother were classmates.{w} I asked him about it last Sunday."
    narr "There’s nothing new initially, yet I convinced him to disclose further."

    nvl clear
    window hide

    tomonori "This is just a speculation, but Ikari has been off her head for some time after Christmas break."
    is4 "You’ve heard of the incident in the storage room that February, didn’t you?{w} The one where –"
    tomonori "She personally told me;{w} I’m among the few, in fact.{w} I thought she was cuckoo, saying that our batchmates’ illnesses were abnormal and that she was next{w} – It was wild!{w} There’s just no truth beyond the books!"
    is4 "Roll along the next four months..."
    tomonori "...To the following March, this year.{w} Seeing her on the newsprint, I wanted to retract my judgement.{w} But I never said it to her face, so why would I apologize?"
    is4 "..."
    tomonori "Satisfied? Hope so.{w} If you please, do {i}not{/i} transpire our conversation with anyone else.{w} While she may be a familiar face to the public, the details connecting her and the recent tragedy are not."
    is4 "But I heard it first from Sayo. Does that count?"
    tomonori "She knows her limits. I can say Suzumoto’s still in the safe zone.{w} Just heed my advice."

    "I kept my promise, didn’t I?{w} So why am I convicted like a criminal?{w} This world has double standards. It makes me laugh."

    window show
    nvl clear
    narr "{i}~Va chez la voisine,\n~Je crois qu’elle y est,\n~Car dans sa cuisine\n~On bat le briquet.{/i}"
    narr "The brief buzz afterwards made me jump.{w} I slapped myself awake from my temporal daze.{w} It degraded to silence once more, before L.C. spoke again."

    nvl clear
    window hide

    unk "An elementary rhyme, common amongst the French.{w} Tonight, the moon takes the front seat, awaiting your performance.{w} Kindly reproduce it – just this part.{w} Be swift or be driven mad from the endless repetition."

    window show
    nvl clear
    narr "The same verse of {i}Au Clair De La Lune{/i} played after the transmission.{w} This time, I listened more closely."
    narr "Elementary enough, I say,{w} so the notes must be distinct."
    narr "This is a version different from the one I first played on the piano.{w} If I think about it, it kind of fits.{w} The amount of facts he presented creeps me out."

    nvl clear
    narr "From the drawer, I retrieved some writing materials.{w} Then, I drew a staff and marked the notes where I thought they should be.{w} Three drawings to check for any discrepancies."
    narr "I returned to the piano and marked the keys.{w} My strokes matched the tempo of the song as a fail-safe.{w} Most of the time, the notes match save for one or two.{w} They're only an estimation."
    narr "Nothing happened after three attempts, so I re-checked my paper."
    narr "This is jarring{w} – it appears that I’ve distorted some notes by mistake.{w} For instance, the G-flat in {i}feu{/i},{w} I transcribed it as a C.{w} The reverse happened in another note.{w} Oddly enough, I happened to get different results with the last note, C."
    narr "Before the next attempt, I performed some statistical analysis to help my case.{w} Fourth time and counting."

    nvl clear
    narr "{b}*CLANK* *HUM*{/b}"

    nvl clear
    narr "The mechanism drowned my breath.{w} As my heart raced in anticipation, I waited as the metal bars reveal the opening.{w} My way out – a step closer, it seems."
    narr "My ear tingled, and a lava-like sensation rose up my neck.{w} My fever is returning, it seems,{w} and I haven’t any medicine with me.{w} In fact, my personal items aren’t, too{w} – not even my watch!"
    narr "How much time has passed, no one can tell."
    narr "There seems to be no alternative to that door.{w} I left the writing materials in the drawer and turned to leave this hellhole."

    nvl clear
    window hide

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

    is4 "Haa... Haa... Haa...{w} {i}*GULP*{/i} Kuh..."

    "{b}*THUD*{/b}"

    window show
    nvl clear
    narr "I never want to hear that demonic voice again{w} – especially that mocking laugh!{w} The wild throbbing filled my ears,{w} my face drained of blood.{w} My posture is that of a doll,{w} left by its owner on the bed after playtime."
    narr "If I were to look through a mirror,{w} perhaps I’d see a monster."
    narr "But there’s no need{w} – I’m not the only one that changed.{w} Ticking sounds replaced the pulsations.{w} It better be what I think of it – a ninety-nine in my books."

    nvl clear
    narr "I watched the door.{w} At any minute, a figure might emerge from the dark corridor.{w} He sees me, vulnerable and weak,{w} and does the most horrifying thing imaginable...{w} the end."
    narr "Nobody came, contrary to my expectation."
    narr "With what little strength remained, I forced myself up.{w} I held it in, pacing once per second as I made my way to the door."
    narr "The sides supported my weight.{w} For another minute, I stared into the void.{w} I couldn’t make out a figure, but there are two doors in sight{w} – one across from here, and the second to my left."
    narr "But which one?"

    nvl clear
    window hide
    return

label ch01_11_labkyou2:
    "Date Unknown - Time Unknown"
    window show
    nvl clear
    narr "I made the cell as my lantern, walking at the sides of the corridor.{w} Eventually, a door, similar to the previous one, came into contact.{w} It offered little resistance when it opened."
    narr "The space felt more enclosed.{w} My hand immediately traversed the wall for a switch.{w} There was nothing to be found.{w} Hesitantly, I stomached my way into the void."
    narr "I shut the door in the off-chance that a stalker is behind me.{w} It wouldn’t make a difference if I close my eyes now, would it?{w} The pressure heightened,{w} no sound permitted itself to emanate from me."

    nvl clear
    narr "The next minute felt like a dream,{w} a trance.{w} The walls revealed themselves,{w} distanced farther than where I thought they should be.{w} Endless is the ceiling, so is the space beneath.{w} Some things were talking,{w} defying the silence."
    narr "Were they the walls?{w} Couldn’t be.{w} If it were from an angel, or God Himself,{w} my salvation is guaranteed.{w} If it were from the Devil, then all is fair{w} – I’m damned, maybe from the beginning."
    narr "I wanted to go up, but gravity is in effect.{w} It sure is a long way down; none can tell what’s at the bottom.{w} Maybe I’ll be stuck in a wormhole if I risk it{w} – a donut-shaped passageway, if I add!{w} But there is always the door."

    nvl clear
    window hide

    "{i}*RATTLE* *RATTLE*{/i}"
    "If I could just{w} – tsk. That’s one pesky doorknob.{w} It wouldn’t even let my hand grip it."
    "Breathe, Kyou.{w} An insignificant object will not defeat you."

    kk9 "Ugh! Come on!"

    "{i}*RATTLE*{/i}"

    kk9 "Phew... You’re putting up quite a fight!{w} Now let me out, if you please?"

    "Pull, pull, pull..."
    "It won’t budge, and I’m already using all my strength!{w} There must be a superglue applied to this knob.{w} It doesn’t smell like it – I can’t even smell anything!"
    "{b}*BUGH* *BUGH* *SLAM*{/b}"

    kk9 "I know you’re there! Open up!"

    "{i}*snicker* Hihihihihihi... Nyihihihihihihihi!{/i}"

    window show
    nvl clear
    narr "The platform shook.{w} It’s as if the force on the door caused a quake,{w} or was it that...{w} that...{w} whatever that is.{w} My feet numbed from the tremor; I can hardly get up.{w} I rolled over."
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

    nvl clear
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
    narr "This is the aversion of death,{w} and that fall made me realize something.{w} Just how much damage can a mortal take?{w} Is he unbreakable as he is not led to believe?{w} My purpose is clear, and I hope to find a Grail at journey’s end."
    narr "I felt my head, warm near the crown.{w} The tips of my finger spouted a thick crimson liquid.{w} No signs of nausea, but I should cover the wound with a tourniquet – if there ever is one."
    narr "Debris scattered all over the floor.{w} Splinters of wood and broken bulbs littered the space where I lied down – a few inches away from a laceration."
    narr "Have I been that stupefied to even notice?"

    nvl clear
    narr "Then I remembered why I came here."
    narr "Next to my feet glinted a tiny object – a metal key.{w} It could fit the other door’s keyhole perfectly, unless there are some special instructions entailed with it."
    narr "I’m in a closet, looking ransacked from whatever episode I had earlier.{w} I spotted a flashlight on the top-most shelf.{w} As it went with my hand, a small paper came flying.{w} I caught it, running a quick scan of its contents."
    narr "The room plunged into darkness – a lucky save by the flashlight.{w} Illuminated, the letter gave off a short message."

    nvl clear
    narr "{i}One does not speak, write, listen, and live forever.{w} He is part of a multitude of cycles, even which the universe is a major component.{w} Eventually, everything shall return the way they should be at the beginning of time.{/i}"
    narr "{i}For the love of God, would you kindly provide for me a pen to write with?{w} Fetch the torch for me too, please, as I may have forgotten it in a hurry.{w} Only then shall you pave your own path to the truth{w} – to me.{/i}"
    narr "{i}I shall be waiting,{w} stranger.{/i}"

    nvl clear
    narr "This is a joke.{w} He refers to my name one minute, regards me as a stranger the next.{w} Ah, well. I’ll be on my way. It’s not like he knows where I am right now.{w} No pens, though."
    narr "At this point, the torch became my source of light.{w} The cell door apparently shut itself.{w} Nevertheless, I focused on the other unexamined door.{w} The key I found is a perfect fit, but the rust inside the lock made some resistance."
    narr "{b}*CLICK*{/b}"
    narr "That mundane sound lifted me up. With a push, a blinding light seeped out of the opening.{w} I shielded my eyes while opening the door to its furthest limit."
    narr "My whole system stopped as the image registered into my mind."

    nvl clear
    narr "I’m in a living quarters.{w} Just compare the bleakness of the cell I’ve been into – it’s absent here.{w} No word is sufficient to describe how peculiar to see its kind, especially in this place."
    narr "There are couches, ornaments, tables, to mention a few.{w} The center table sports a bonsai on top. Lovely as it is, yet unaesthetic at its position."
    
    nvl clear
    narr "Only when I closed the door did its artistic features sink in.{w} Symmetry is present, down to the most minute detail.{w} Each side has a door at the center, save for the one on my left."
    narr "It has a coffee table, same height as the one on the center.{w} In front of the wooden book display is a book stand and a pair of unlit candles."
    narr "A painting adorned the wall above it.{w} Moving it is not an option; it’s too heavy and pinned tightly to the wall."
    narr "It shows a ship bearing {i}Q 1347{/i} on its hull, painted by R. Jeffs.{w} If it were a person instead of a ship, I’d say it was a shrine.{w} His eyes would meet the door across in that case. Doesn’t take a guess to figure out its state."

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

    window show
    nvl clear
    narr "My hand reached for the first book.{w} Upon opening the first page, a bookmark fell on the table.{w} It piqued my attention, particularly the small letterings near the ribbon:"
    narr "{i}Numbers – p. 16{/i}"
    narr "Then I turned the pages to the section indicated.{w} I briefly relived my first moments in Nihongo class.{w} Sensei was firm even at basic topics such as this; everybody was interested mostly on writing, the Kanas and even Kanji!"
    narr "Before my eyes lay the first steps, like in any language, to count.{w} My recollection continued until I noticed an oddity{w} – {i}go{/i} underlined in blue.{w} That shade is familiar..."
    narr "Regardless, I scanned the rest of the book, but there were no other markings.{w} Just that one.{w} Perhaps a clue?{w} I’ll have it as a quick reference."

    nvl clear
    narr "The latter nine books shared similar circumstances, bookmark and highlighted word someplace inside."
    narr "In the end, I collected the following:{w} nurse,{w} check,{w} table,{w} eye,{w} alone,{w} tree,{w} ankle,{w} don't,{w} reason.{w} Random, aren’t they?"
    narr "Ten blue words, a nonsensical message if taken whole.{w} I deemed it necessary to inspect the room once more, checking for oversights."

    nvl clear
    window hide

    "A second view of the painting helped calmed my nerves as I peacefully gathered my thoughts."

    kk9 "So, a boat. A WWII warship, maybe?{w} A string of ten words...{w} What’s the connection?{w} {i}*sigh*{/i} God, help me."

    "My attention altered between the painting and the open books.{w} Each travel puzzled my mind further,{w} but the subconscious is conjuring something bit by bit."
    "Using the blank pages at the books' ends, I played with the words, rearranging and reading them slowly.{w} Nonsensical messages appeared more often than those which are sensible, unsurprisingly."
    "{b}*CLAP*{/b}"

    kk9 "Eureka!{w} So that was the message after all. It reads..."
    kk9 "Straightforward enough, and works for me!"
    kk9 "You’re telling me to check that bonsai out?!{w} My pleasure. I’d even dispose of it should you desire."

    "A smile flashed on my lips, the same time as my feet began heading towards the plant.{w} Who would’ve thought? It’s in plain sight from the beginning!"
    "My hands reached for it without hesitation, exploring and digging the soil.{w} It’s all in our dut –"

    kk9 "Ow! That hurt..."

    "The tree or something... pricked my finger!{w} It felt like a needle.{w} A red spot appeared amongst the stains.{w} I rubbed my hands vigorously, despite the absence of any sign of infection."
    "{b}*CRASH*{/b}"

    kk9 "That’ll teach you."

    "Something was off about that plant. The moment my eyes wandered about the room, it captured them.{w} Now it’s gone, no longer able to bother anyone."
    "This is{w} catharsis."
    "Fully tucked into the sofa, I gave myself some breathing space.{w} A minute or two passed before it caught my attention{w} – a scrap of paper from within the soil.{w} I cautiously dug it up and examined its contents."

    kk9 "1-6-6-5.{w} I have no idea what this means or where does this fit into.{w} Oh, what’s the message this time?"

    "And I stood, prepared to give the books a second reading."

    "{b}*THUD*{/b}"
    "My feet lost balance, giving in to the peculiar sensation in my head.{w} The fever returned and my body slowly succumbed to it.{w} I shut my eyes and prayed.{w} This is worse than worst – I’m losing my hold."
    "{i}*rattle* *rattle* *rattle*{/i}"

    kk9 "Who goes there?!"

    "Something{w} or someone{w} is trying to break in.{w} It could only be in my head, but..."
    "{b}{i}*RATTLE* *RATTLE*{/i}{/b}"

    kk9 "Begone, you spawn!{w} By the power of Christ, I shall not allow you to take me.{w} Stay there... go back to whence you came!"

    window show
    nvl clear
    narr "The shaking stopped."
    narr "My legs weakened as much as my breath shortened.{w} Patches of blue and white covered my vision, ever so slowly being invaded by darker shades of grey."
    narr "But it won’t stop.{w} The rattles continued, louder than ever{w} – to my left, to my right, even in front of me!{w} I can hear somebody laughing behind me,{w} not to my neck, no.{w} Farther than that."
    narr "{i}Ha... hahaha... hahahahahahaha... gyahahahahahahahaha... Woohahahahahaha!!!{/i}"
    narr "The warship; rather, its dead crewmen{w} are feasting upon my predicament.{w} Purgatory? Bah!"

    nvl clear
    window hide

    "{b}*SNAP*{/b}"

    kk9 "Hngh!{w} AAAAAAAAAAAAAAAAAAHHHHHH!!!!!!"
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