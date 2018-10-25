# JULY CHAPTER SCRIPT

label ch02_july:
    centered "{i}{b}For the beast has unleashed its evil; from within the shadows, it lurks.{w}\nBy watching those shadows, it leaves it little chance to conceal itself.{w}\nYet by that principle,{w} it has learned to live under the light without notice.{/b}{/i}"
    
    call ch02_01_prologue1 from _call_ch02_01_prologue1
    call ch02_02_prologue2 from _call_ch02_02_prologue2
    call ch02_03_reforms from _call_ch02_03_reforms
    call ch02_04_therapy from _call_ch02_04_therapy
    call ch02_05_volleyball from _call_ch02_05_volleyball
    call ch02_06_visit from _call_ch02_06_visit
    call ch02_07_security from _call_ch02_07_security
    call ch02_08_review1 from _call_ch02_08_review1
    call ch02_09_facts3 from _call_ch02_09_facts3
    call ch02_10_review2 from _call_ch02_10_review2
    call ch02_11_mockreview from _call_ch02_11_mockreview
    call ch02_12_posteval from _call_ch02_12_posteval
    call ch02_13_death02 from _call_ch02_13_death02
    call ch02_14_investigation from _call_ch02_14_investigation
    call ch02_15_facts4 from _call_ch02_15_facts4
    call ch02_16_suspicions from _call_ch02_16_suspicions
    call ch02_17_epilogue from _call_ch02_17_epilogue
    call credits from _call_credits
    return

label ch02_01_prologue1:
    scene black with fade
    "JULY 1, 2013 - 1715H"
    scene bg park evening with fade
    play music bg_theanthillganggoeswest loop

    window show
    nvl clear
    narr "I hope she’s home."
    narr "The ride here took only fifteen minutes, much quicker than I estimated.{w} My cleaning duties are scheduled tomorrow, so that’s a plus.{w} I scurried off, finishing any prior commitments by the end of lunch break."
    narr "I passed by my former school, its appearance unchanged.{w} Students and staff alike are busy inside the classrooms, but some elementary students nearby are playing at the field."
    narr "There is that one tree we used to sit under while waiting for our afternoon shift.{w} I went towards it and re-assessed my things."

    nvl clear
    narr "Every day, I have to carry three separate containers: a knapsack of textbooks and writing materials, a sling bag of notebooks, and a leather case.{w} One could say I have gotten a bit stronger with the weight I have been carrying."
    narr "I brought out a fluffy toy wrapped in manila paper. Written in black ink,"
    narr "{i}Happy 15th B-Day, Sanae! -- Miyu{/i}"

    nvl clear
    narr "Hey, we’re not a rich family so don’t judge! Effort is what’s important... at least for me."

    window hide
    scene bg smallstreet evening with dissolve
    window show
    narr "Five minutes later, her home is in sight.{w} A neighbor of hers is outside; no signs of her, though."

    nvl clear
    window hide

    show miyu smile at Three2 with Dissolve(0.2)
    mh8 "Excuse me. Do you know anyone named Sanae?"
    neighbor "Nana? Let me fetch her brother for you."

    show miyu nervous blushleft at Three2 with Dissolve(0.2)
    mh8 "Ummm... It's okay--"
    neighbor "Hey, someone’s looking for Nana! It’s one of her classmates, I think."

    show miyu panic blush at Three2 with Dissolve(0.2)
    "Almost immediately, her brother peeked out of their door.{w} He looked at me, and I flustered as heck in total embarrassment."

    sanae_bro "Well, well, if it isn't Miyu. Come inside."
    show miyu worried blush at Three1 with Dissolve(0.2)
    mh8 "Uuuuhhhh... I'm not sure about this. {b}{i}*GULP*{/i}{/b} Maybe I should --"
    sanae_bro "Hahahahaha! It's alright. Make yourself welcome."

    "I picked myself up, not wanting to stay a frozen puff of red at the sidewalk."
    hide miyu with Dissolve(0.2)
    stop music fadeout 2.0

    scene bg livingroom2 with dissolve
    play music bg_autumnday loop
    "They have a relatively small house. Cozy, bright, and welcoming, that is.{w} Sanae's mother is also home."

    ms_yos "How are you, Miyu? Getting along well?"
    show miyu embarrassed at Three1 with Dissolve(0.2)
    mh8 "Staying alive, I suppose. Things are quite heavy back at MSCI, but still a happy place to be at. {i}*chuckle*{/i}"

    "Sanae's brother served me some pandesal and a packet of peanut butter.{w} I already ate a bit before coming. Might as well help myself to show some respect."

    ms_yos "So, how did you know it's her birthday today?"
    show miyu smile at Three1 with Dissolve(0.2)
    mh8 "I asked her recently.{w} Actually, I do know the date since First Year, but my memory's a bit off back then. July 4 I thought, {i}*chuckle*{/i}"
    ms_yos "Glad you still remember and decided to visit. She's outside with her friends right now. I don't know how long before she's back."
    mh8 "I'll be waiting here for a while. I just wanted to personally greet her.{w} It's what I always do."
    ms_yos "By the way, has she already told you?"
    show miyu serious at Three1 with Dissolve(0.2)
    mh8 "What would that be, ma'am?"
    ms_yos "She's running for a position in the Youth Council this October! She'll be up against two of your former classmates."
    show miyu surprised at Three1 with Dissolve(0.2)
    mh8 "More reason to see her then! I wish her luck in her endeavors.{w} When did that girl start becoming politically active? Hm. Hm. Hm."
    ms_yos "It's better if she tells you directly.{w} You know, a lot has changed since you transferred. Lots of stories even I can't recall. {i}*chuckle*{/i}"
    stop music fadeout 2.0

    show miyu focusedpose at Three1 with Dissolve(0.2)
    "For a while, I watched the soap opera on TV.{w} It bored me, so I turned to solving some Math problems instead."
    "Just to keep my mind off of it.{w} Idleness can bring about the worst memories when one's guard is down."
    "It was already six o' clock. No sweet-voiced girl out the door yet.{w} Her mother stopped playing on her phone for a while and prepared for dinner. I replaced the textbook in my knapsack shortly after."

    show miyu worried at Three1 with Dissolve(0.2)
    unk "Hey, mother! Had a great time with them at the mall. What's for --{w} Well, I didn't expect you to actually come here."

    show miyu worried blush at Three1 with Dissolve(0.2)
    "Blood welled up my cheeks, and my head turned in excitement."
    play music bg_palingaroundparis loop
    show sanae naughtysmirk at Three3 with Dissolve(1.0)
    "Blood welled up my cheeks, and my head turned in excitement.{fast} There she is, hands on the door frame, slowly curving her lips to a cat-like grin."

    show miyu smile at Three1 with Dissolve(0.2)
    mh8 "Hi... Good evening."
    show sanae smiletalkclosed at Three3 with Dissolve(0.2)
    sanae "Hello, Mi-kun!"
    show sanae smileleft at Three3 with Dissolve(0.2)
    sanae "Ma, I'll be treating Miyu out for dinner."
    ms_yos "Okay! You guys have fun.{w} By the way, your brother will be joining you in a while. Enjoy!"
    show sanae smile at Three3 with Dissolve(0.2)
    sanae "Love you, ma! {i}*giggle*{/i} Let's go."
    hide miyu with Dissolve(0.2)
    hide sanae with Dissolve(0.2)

    scene bg park evening with dissolve
    play sound sfx_street loop
    show miyu smiletalk at Three1 with Dissolve(0.2)
    show sanae smiletalk at Three3 with Dissolve(0.2)
    "We never held hands while walking. It's out of our league... for now.{w} Rather, we resorted to friendly chatter -- how we've been and what we've been up to lately."
    "We bumped into one of her classmates' older brother, who also lives nearby.{w} To describe the encounter would be rather insufficient."

    neighbor "So, what are you up to this evening? Celebrating your birthday with this guy?"
    show sanae smile at Three3 with Dissolve(0.2)
    sanae "Yeah! Truth be told, I kind of expected Mi-kun to show up even if I actually didn't. {i}*giggle*{/i}"

    show miyu embarrassed2 blush at Three1 with Dissolve(0.2)
    "He gave a menacing glare at us, almost costing me all my cool."

    show sanae embarrassed at Three3 with Dissolve(0.2)
    sanae "Don't get the wrong idea! It's my birthday, after all. Who says I'm not treating a former classmate?"
    neighbor "If you say so, I'll be on my way. You two enjoy yourselves. {i}*snicker*{/i}"

    "I am just glad he went away.{w} Sanae dragged me by the arm as we continued walking."
    show sanae embarrassed at Three2 with Dissolve(0.2)
    hide sanae with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    stop sound

    scene bg jollibeerestaurant night with dissolve
    "Past the gym where we held PE classes is a mall.{w} We settled in one of the fast-food restaurants at our current direction.{w} It was packed as usual, but preserved its relaxed ambience regardless."

    show miyu smile at Three3 with Dissolve(0.2)
    "She ordered us both a Super Meal, consisting of a one-piece chicken, spaghetti, regular fries, and soda."
    show sanae smile at Three1 with Dissolve(0.2)
    "She ordered us both a Super Meal, consisting of a one-piece chicken, spaghetti, regular fries, and soda.{fast} We sat facing each other at one of the four-seaters on the left; I faced the window."

    show sanae smiletalk at Three1 with Dissolve(0.2)
    sanae "How are things, Mi-kun?"
    show miyu naughty smirk at Three3 with Dissolve(0.2)
    mh8 "Heh. You tell me. How are things on your side?"
    show sanae smirk at Three1 with Dissolve(0.2)
    sanae "Nothing much, but I can already feel the demands of being a Senior. {i}*sigh*{/i} We'll both be graduating in nine months and it's off to college."
    show miyu naughty smile at Three3 with Dissolve(0.2)
    mh8 "Say, you're running for a position in the Youth Council? Good luck!"
    show sanae smiletalk2 at Three1 with Dissolve(0.2)
    sanae "Don't mention it. {i}*giggle*{/i}{w} I just felt like it's my calling. You know, after heading the class one time and being a Youth Leader at our church."
    show miyu naughty closepose at Three3 with Dissolve(0.2)
    mh8 "Pleasant. Pleasant. Seems like things will be piling up this October in case you win.{w} Hope you serve your village well. My money is on you, hotshot."
    show sanae smiletalkclosed at Three1 with Dissolve(0.2)
    sanae "Sure do."
    show sanae embarrassed at Three1 with Dissolve(0.2)
    sanae "Sure do.{fast} What did you just call me?"
    show miyu proudclosed at Three3 with Dissolve(0.2)
    mh8 "Nothing. Let's eat. Enjoy the evening, birthday girl!"
    show miyu smile at Three3 with Dissolve(0.2)
    show sanae smiletalk2 at Three1 with Dissolve(0.2)
    sanae "Cheers!"

    play sound sfx_clink
    "{b}{i}*CLINK*{/i}{/b}"

    "Between each helping and sip, we exchanged stories no matter how serious or silly they are.{w} We kept the mood up for a good half hour or so."
    stop music fadeout 2.0

    show miyu confused at Three3 with Dissolve(0.2)
    show sanae blank at Three1 with Dissolve(0.2)
    "Stomachs full, we rested for a bit.{w} Sanae took out her smartphone and texted her brother. I was watching the window, counting passersby and parked cars."

    mh8 "I did see your brother leave not long after my arrival. He shouldn't take that long, I guess."
    sanae "Oh, I know exactly where he went. That guy..."
    show miyu bored at Three3 with Dissolve(0.2)
    mh8 "Not to ruin the night, but...{w} I held this in since it felt too sensitive to share. You might know this already."

    "Sanae placed her phone down and leaned closer. She lowered her voice."

    play music bg_decline loop
    show sanae serious at Three2 with Dissolve(0.2)
    sanae "What exactly happened in MSCI? I thought the school is a safe zone."
    mh8 "Not inside, but what happened {i}outside{/i}."
    show sanae worriedtalk at Three2 with Dissolve(0.2)
    sanae "Huh?"
    show miyu pissed at Three3 with Dissolve(0.2)
    mh8 "The morning the two, Kyou Kirisaki and Inoue Shinozaki, disappeared, there were no suspicious people in-campus at the time.{w} I arrived at my usual time, but I didn't see them both. Makes you wonder how an inside job could've taken place, doesn't it?"
    show miyu pissedclosed at Three3 with Dissolve(0.2)
    mh8 "After a few days, they were found. One is burnt alive and the other is left a total mess.{w} That evening at the hospital... Ugghhhh... I shudder at every thought of it."
    show sanae worriedleft at Three2 with Dissolve(0.2)
    sanae "That's horrible..."

    "It is an understatement,{w} to say nothing of what happened last night before the final prayer."
    hide miyu with Dissolve(0.2)
    hide sanae with Dissolve(0.2)
    stop music fadeout 2.0
    return

label ch02_02_prologue2:
    scene black with fade
    centered "{b}The Night Before{/b}"

    scene bg village night with fade
    "JUNE 30, 2013 - 2010H"

    play sound sfx_crickets loop
    "I was out the front porch, just ending a call from my mother."
    show sayo casual glass sleepy at Three1 with Dissolve(0.5)
    "I was out the front porch, just ending a call from my mother.{fast} Sayo's figure emerged from the left, looking rather sleepy."

    show sayo casual glass sleepytalk at Three1 with Dissolve(0.2)
    sr5 "The van is ready. We'll be leaving at nine after the prayer."
    mh8 "Sure.{w} *YAWN* Let's just get this over with."
    hide sayo with Dissolve(0.2)
    stop sound

    scene bg parlor with dissolve
    "Despite the cool breeze, we went back inside the house.{w} The others have already gathered in the parlor: the Kirisakis, the Yamamotos, Akira, Yoshiro, Ikuko, Hiroshi, Ayumi, Sumiko..."
    "Wait. Where's Ichirou?"

    ai2 "Sorry to bother you once more, but could you dial Ichirou? He's been out for too long now."

    scene bg village night with dissolve
    play sound sfx_crickets loop
    "With a grumpy look, I went out and contacted Ichirou.{w} Thankfully, he picked up immediately."

    mh8 "Where are you?"
    iy1 "Just went out to catch some air. Do you need me?"
    mh8 "Darn, yeah! Recklessly scurrying about when there's a monster on the loose, Einstein!{w} Now would you kindly get your butt back here to tell us you're alive?"

    "Of course, I only kept those in my head.{w} Seeing no cars presently traveling, I occupied the middle of the road. No matter how far I scout ahead on every possible direction, Ichirou's presence is absent."

    mh8 "Sorry. I can't see you from here. The prayer won't start without you, you know?"
    iy1 "That so? Okay! I'll be back in a jiffy."
    stop sound

    play sound sfx_beep2
    "{i}*BEEP*{/i}"

    window show
    nvl clear
    narr "I'm not going back inside until I see any sign of life from him. For now, let me enjoy the sparks from the bug zapper above."
    narr "Nothing happened for five minutes.{w} I would have made another call, but I was low on battery like everyone else."
    window hide
    show silhouette at Three3 with Dissolve(1.0)
    window show
    narr "Finally, a sign of life on my right.{w} Shuffling towards it, my lips curled to a slight grimace. Every step I made dissipated a part of my own fury. If one of us goes next tonight, then I'll be damned."

    nvl clear
    window hide

    mh8 "Hey! Is that you?"
    show silhouette at Three2 with Dissolve(0.2)
    play music bg_satiate loop

    window show
    nvl clear
    narr "But the figure was unmoving. It was static, facing away from my direction.{w} The lack of lighting concealed its identity and the road beyond. I should have called for backup moments ago, but..."
    narr "If I could just turn around and run, except it's not an option right now.{w} My eyes locked onto the figure, but its backed continued to face me. Sounds of static mixed with the wind, creating a music unheard of by many."
    narr "That, and my body is paralyzed.{w} At every passing second, the figure reeked of malevolence, transferring it within me. And it acted like poison, intoxicating my whole system."
    narr "Breathe... Breathe... Breathe...{w=0.5} You just need some sleep.{w=0.5} Just survive the night. Tomorrow's going to be a better day.{w=0.5} It's Sanae's birthday tomorrow!{w=1.0} I must not forget to send her --{nw}"

    nvl clear
    window hide
    stop music

    play sound sfx_whoosh
    scene black
    centered "{b}{i}*WHOOSH*{/i}{/b}{fast}{w=1.0}{nw}"

    mh8 "{b}*GASP*{/b}{w=1.0}{nw}"
    play sound sfx_thud2
    scene black with sshake

    scene bg abyss with fade
    play music bg_hazydisorientation loop
    window show
    nvl clear
    narr "For an instant, the world became enveloped in black.{w} Smoke clouded my vision, the creature's malevolent presence apparent. It posed a threat familiar to many, yet in truth unknown."
    narr "It rushed through my body, knocking me down to a shaded part of the road. I could not bear to open my eyes, fearing it was all over me. All but my ears shut down temporarily."
    narr "Someone was screaming, running; leaves rustling.{w} There's someone after that figure.{w} My brain worked itself to recognize that voice..."

    nvl clear
    window hide

    iy1 "Wait up! You haven't answered my question -- hey!"
    stop music

    "Ichirou...?"

    scene black with fade
    "JUNE 30, 2013 - 2015H"

    play music bg_interloper loop
    window show
    nvl clear
    narr "Where has that snitch gone off to?!"
    narr "I'm aware that I've dashed past Kyou's home, in favor of that... thing! He must know something about the crimes -- he must!"
    narr "He disappeared into a thicket. Blind with the thirst to squeeze some answers out of it, I followed.{w} Seconds passed, the snaps underneath gradually drowned those of the unknown figure's."
    narr "Then I took notice --{w} only my own snapping was audible.{w} It has disappeared, vanished into the night, never to be seen by anyone again. At least, it wouldn't allow itself to be."
    stop music fadeout 2.0

    window hide
    scene bg fields night with dissolve
    play sound sfx_wind loop
    window show
    nvl clear
    narr "And here I am, standing in the middle of the fields.{w} With all that frenzy, the return trip would be dangerous, especially as there were no tracks nor markers left behind by myself."
    narr "One teenager and an endless wall of shrubs combined make a perfect recipe for a crime."
    narr "There are news reports of young women getting gang-raped then sometimes salvaged in places like this.{w} Worse, the assailants would chop their body into pieces, seal them into plastic bags, and dispose of them anywhere."
    narr "Somehow like the Lucila Lalu case in 1969, or Samantha, our resident ghost.{w} Hell, why would I even mention those? Every step now became an effort against the frosty winds."

    nvl clear
    narr "You would be wrong -- even as a male, a psychopath can still sexually abuse me and I to suffer the same fate as those poor ladies. Though, it would be more probable to be killed first than otherwise."
    narr "Here in no man's land, I walk aimlessly and long for the crickets' singing.{w} That over my pulsating heart, ready to burst from its cage."
    narr "Instead, I could be getting warm like the others at Kyou's house. Yeah, they could've been starting the prayer without me.{w} Pray forgive me for irking my friends. They could just be worried about me, so..."

    nvl clear
    window hide
    stop sound

    unk "Finally!{w=0.5}{nw}"

    play sound sfx_thud2
    show miyu bored at Three2 with vpunch
    "Oh my God!"

    iy1 "That's not a nice thing to do at night, Miyu!"
    mh8 "Well, {i}*pant* *pant*{/i} no worse than trotting around in the fields at night, I suppose. Enjoying the fresh air... you could've been killed, you idiot!"
    iy1 "Okay! Okay! I'm sorry. Can we please walk back now? This place is starting to freak me out."
    hide miyu with Dissolve(0.2)

    scene bg pasteur night with dissolve
    play music bg_awkwardmeeting loop
    show miyu pissed at Three3 with Dissolve(0.2)
    show ichirou worried at Three1 with Dissolve(0.2)
    "With little battery we had, we took turns shining a flashlight in front of us.{w} Miyu took the lead, brisk walking through the dark path."
    "I've never been on the receiving end of a reprimand, at least not as harsh as his."

    show miyu bored at Three3 with Dissolve(0.2)
    mh8 "So you thought it was a genius idea to track down a perp -- at night and alone -- and you never thought of diverting for backup?{w} Anyone could have wished condolences like {i}it{/i} did."
    show ichirou focus at Three1 with Dissolve(0.2)
    iy1 "I know, but I saw that as the only chance to unmask the culprit.{i} You can't just leave a high-profile case like that for too long!{w=1.0} What if it remains unclosed like --{nw}"
    show miyu pissed at Three3 with Dissolve(0.2)
    mh8 "Knowing too much is what killed Kirisaki and pushed Inoue's mentality to its edge."
    show ichirou focusleft at Three1 with Dissolve(0.2)
    iy1 "Tch."
    show miyu pissedclosed at Three3 with Dissolve(0.2)
    mh8 "I hope you realize that."
    hide ichirou with Dissolve(0.2)
    hide miyu with Dissolve(0.2)

    scene bg parlor with dissolve
    show sayo casual glass serious at Three3 with Dissolve(0.2)
    show sumiko angry at Three1 with Dissolve(0.2)
    "We returned safely, and the rest were relieved of panic after seeing me.{w} Sayo and Sumiko had their arms folded, eyes glaring, obviously ready to strike me for my stupidity."
    hide sayo with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)

    "However, no word was spoken, and the prayer continued as usual."

    scene bg village night with fade
    show silhouette with Dissolve(1.0)
    "But...{w=0.5} who was...{w=0.5} that?"
    hide silhouette

    scene bg jollibeerestaurant night with fade
    show sanae worriedtalk at Three2 with Dissolve(0.2)
    show miyu confused at Three3 with Dissolve(0.2)
    sanae "You've reported this to the inspector?"
    show miyu bored at Three3 with Dissolve(0.2)
    mh8 "Of course, we did.{w} Ichirou may be a risk-taker, but he's not stupid enough to let a vital piece of information slip by. Everything is important in this case."
    show sanae serioustalk at Three2 with Dissolve(0.2)
    sanae "But what if all comes down to nothing like the case in Sacred Heart Academy?"
    show miyu pissed at Three3 with Dissolve(0.2)
    mh8 "That's the endgame plan...{w} for the opposing side, at least."
    stop music fadeout 2.0

    window show
    show miyu talk at Three3 with Dissolve(0.2)
    show sanae smile at Three1 with Dissolve(0.2)
    show miyu smile at Three3 with Dissolve(0.2)
    nvl clear
    narr "At that exact moment, Sanae’s brother and his fiancée entered the restaurant.{w} With a wave, Sanae moved to the seat beside mine and the two occupied the vacant seats across from us."
    narr "They ordered nothing. Just stopping for a quick chat with us -- seven o’ clock is only sixty ticks away.{w} It is already late, but my parents would not mind."
    narr "Besides, only one day is dedicated to her birthday so I should make it worthwhile."

    nvl clear
    window hide

    "A quick glance at the window, and behind it is a familiar face."
    show ichirou smile at Eight8
    hide ichirou with Dissolve(1.0)
    "A quick glance at the window, and behind it is a familiar face.{fast} He waved and went away as quickly as he appeared.{w=0.5} Though I acted friendly, my mind was puzzled."
    "What is he even doing here?"

    show miyu confused at Three3 with Dissolve(0.2)
    show sanae blank at Three1 with Dissolve(0.2)
    sanae_bro "Who's that?"
    show miyu smiletalk at Three3 with Dissolve(0.2)
    mh8 "It's a classmate. {i}*chuckle*{/i} Didn't expect him to be here."
    hide miyu with Dissolve(0.2)
    hide sanae with Dissolve(0.2)

    scene bg street night with dissolve
    play sound sfx_street loop
    "Minutes later, I parted ways with Sanae, already thinking of a flirty message to thank her for the evening."
    "On the jeepney ride home, the question lingered within my thoughts. It's strange and amusing enough, but of all the people who were there this evening..."
    stop sound fadeout 2.0

    scene black
    show ichirou smile at Three2
    "Ichirou?"
    hide ichirou

    call opening from _call_opening_1
    return

label ch02_03_reforms:
    scene black with fade
    centered "{b}Earlier{/b}"

    scene bg msci with fade
    "JULY 1, 2013 - 1200H"

    window show
    nvl clear
    narr "By noon, the delegations were official."
    narr "{i}Hiroshi Kano stepped up for Sumiko Tokubei in the Science Club leadership, the latter already a premier in the EO and in class IV-C.{/i}"
    narr "{i}All papers to the Mathematics Club shall be temporarily overseen by the acting president Miyu Hirano while Inoue Shinozaki is undergoing therapy.{/i}"

    window hide
    scene bg conferenceroom with dissolve
    play music bg_greatminds loop
    show sayo seriousnormal at Three2 with Dissolve(0.2)
    window show
    nvl clear
    narr "Despite the disconcerting incident a few days prior, the Seniors were able to accomplish a form for the national university's entrance exam.{w} It is the first and earliest, scheduled at the first weekend of August."
    narr "Thus, Sayo called for an emergency meeting to discuss the plans for next week's review sessions.{w} Additionally, the heads of the three organizing clubs were invited: Hiroshi, Miyu, and Ayumi Nakashima."
    narr "Only Mrs. Genkai, as usual, was absent."

    nvl clear
    window hide

    show sayo serioustalk2 at Three2 with Dissolve(0.2)
    sr5 "Good afternoon, ladies and gentlemen. I would like to apologize for calling everyone on such short notice, but I feel that this matter is not to be delayed to the first Friday."
    show sayo seriousnormalleft at Three2 with Dissolve(0.2)
    c_4r "Why, though? The review sessions next week are nearly polished.{w} We've already included this as part of our agenda during the pre-academic year meeting with the club heads."
    show sayo serioustalkleft at Three2 with Dissolve(0.2)
    sr5 "Exactly.{w} But you must keep in mind that Hiroshi and Miyu may not be fully aware of their responsibilities next week. If you recall, I only discussed our plans with Inoue and Kyou, in addition to Ayumi."
    show sayo serioustalk2 at Three2 with Dissolve(0.2)
    sr5 "I hope you all understand the current situation."
    show sayo seriousnormal at Three2 with Dissolve(0.2)
    "\"Affirmative.\""
    show sayo serioustalk2 at Three2 with Dissolve(0.2)
    sr5 "We already coordinated with the Science, Mathematics, and English teachers; hence, the contracts you signed on the 18th the previous month."

    "The flow will go like this."

    window show
    nvl clear
    narr "{i}Each class has assigned marshals who will handle and proctor the review sessions.{w} By default, this is left to the teachers themselves taking place on their scheduled period.{/i}"
    narr "{i}The sessions will be held Monday to Thursday class time, assuming no class suspensions. Each subject area will be provided with a study module as an aid for the current session.{/i}"
    narr "{i}Preceding the Club and Organization Activities on Friday would be the lighter final sessions.{w} All that is needed to be taught are techniques in general test-taking and may focus on specific parts of each subject area.{/i}"
    narr "{i}All will lead to a culminating activity on Saturday, a Mock Examination. All Seniors are required to participate, as it will simulate the entrance exam on August.{/i}"

    nvl clear
    window hide

    "As for the Student Council..."

    show sayo serioustalk2 at Three2 with Dissolve(0.2)
    sr5 "Yes. Even we will be participants."
    show sayo worried at Three2 with Dissolve(0.2)
    show ayumi serious at Three3 with Dissolve(0.2)
    ayumi "Question. Does that mean we he have an advantage over those not of the organizing committees?"
    show sayo normaltalk at Three2 with Dissolve(0.2)
    sr5 "Ah, I knew that would be brought up.{w} We prepared the teachers for that. All of the questions would be from the reviewers, so there's not much to worry about."
    show sayo worried at Three2 with Dissolve(0.2)
    show miyu naughty closepose at Three1 with Dissolve(0.2)
    mh8 "Of course, to foil those who merely memorize the answers by letter... That addresses the very problem too."

    show miyu naughty closepose2 at Three1 with Dissolve(0.2)
    "The Council snickered at his comment, lifting their spirits up from the gloomy atmosphere."
    hide miyu with Dissolve(0.2)
    hide ayumi with Dissolve(0.2)

    show sayo seriousnormalleft at Three2 with Dissolve(0.2)
    c_4r "How are we going to time the tests? We just have enough proctors available for the day."
    show sayo normaltalkleft at Three2 with Dissolve(0.2)
    sr5 "I'll have that arranged.{w} For now, your tasks are these: inform your fellow officers of the review sessions next week and prepare some modules, if you wish.{w} Tanaka, the Parent's Consent Forms for 202 students."
    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "Perform your duties well and have a nice day. Meeting adjourned."

    show sayo smileopen at Three2 with Dissolve(0.2)
    play sound sfx_schoolbell
    "At that exact moment, the bell rang, and the council room was empty within a minute."
    show sayo seriousnormal at Three2 with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    "At that exact moment, the bell rang, and the council room was empty within a minute.{fast} Sayo went up and delivered the minutes to Mrs. Genkai."
    stop music fadeout 2.0

    scene bg classroom1 with dissolve
    play music bg_calmertimes loop
    show akira smile2 at Three3 with Dissolve(0.2)
    show miyu smile at Three1 with Dissolve(0.2)
    "Miyu returned with Akira, engaging in banter along the way.{w} Both were visibly tired from the previous day's journey, yet they still arrived at their usual time, if only to sleep until the flag ceremony."

    show miyu talk at Three1 with Dissolve(0.2)
    mh8 "You noticed anything odd earlier?"
    show akira surprised at Three3 with Dissolve(0.2)
    ai2 "Nothing for me."
    show miyu confused at Three1 with Dissolve(0.2)
    mh8 "The meeting felt gloomy. Like, is that the usual atmosphere?"
    show akira surprised2 at Three3 with Dissolve(0.2)
    ai2 "Now that you mention it, yes, I actually felt the same."
    show miyu talk at Three1 with Dissolve(0.2)
    mh8 "What about her?"
    show akira smile2 at Three3 with Dissolve(0.2)
    ai2 "She doesn't let herself be distracted -- as if Sayo would ever be -- but she's not as enthusiastic as before, I can tell you that much."
    show miyu bored at Three1 with Dissolve(0.2)
    mh8 "Understandable. Understandable."

    "At the very least, they wished the event to have a smooth-sailing flow. Everyone would have collected themselves by then."
    stop music fadeout 2.0
    hide akira with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    return

label ch02_04_therapy:
    scene black with fade
    "JULY 4, 2013 - 1600H"

    window show
    nvl clear
    narr "Hey. It's nice to be back."
    narr "Been a long while since I've been within these walls that trigger a sense of familiarity, walls that do not enclose you to a box.{w} They describe, rather, a complex structure. Ironic, I know."
    narr "Leveled breathing, a chair few feet away from the rest of the furniture, hands on the lap, and guard down. Most importantly, the deafening silence. The rest of the phrases bitten off my tongue. These should suffice."
    narr "My memory is on Hibernation Mode for quite some time. The mind cannot remember -- it doesn't want to remember the agony it has been through these recent days. The body doesn't want to remember..."
    narr "The entire being refuses to remember all the suffering it's been through these recent days. How surprising a revelation it is to be a mongrel. No -- not even correct."

    nvl clear
    window hide

    play sound sfx_rumble loop
    "{b}{i}*WHIRR*{/i}{/b}"

    window show
    nvl clear
    narr "Another homely sound.{w} Air seeping in through the vents above, and the lights flickering to life in a set manner.{w} The dancing halted, and the once-blackened room blanched to life."

    window hide
    scene bg whiteroom with fade
    window show
    narr "Its emptiness brought suspicion over serenity.{w} A chair, indeed, and a room-length mirror facing each other. And among the normality stood out a third entity, something{w} {cps=3}-- or {i}someone.{/i}{/cps}"
    narr "A girl, her image waist-up, is a total mess on societal standards. With a single functional eye, only her face, hands, and hair are visible."
    narr "The girl refuses to remember... yet the bruises leave a scar on the mind --{w} another who refuses to remember... the Hell it went through...{w} {cps=10}It does not... It does not!{/cps}"

    nvl clear
    window hide

    stop sound

    scene black
    centered "{b}{i}Good afternoon, Ms. Shinozaki.{/i}{/b}{w=1.5}{nw}"

    scene bg whiteroom
    play music bg_controlledchaos loop
    "...but the outside dictates otherwise. The cycle begins once more..."

    f_is4 "YOU FUCKING DEVIL! HAVE YOU ANY SATISFACTION?!"
    unk "Compose yourself, Inoue. We mean no harm.{w} It's Inspector Emmerich -- one of the policemen who rescued you, remember?"
    is4 "Rescued?{w} {cps=5}Heh...{/cps} {cps=10}Hehehe...{/cps} AHAHAHAHAHAHAHA!!!{w} If you're telling the truth, then why am I in a place like this?"
    p_emm "It's hard to put into words.{nw}"
    is4 "ANSWER!"
    p_emm "You're confined in an asylum."
    is4 "..."
    is4 "Then I was better off in that damned place, then. A madhouse? You're no different..."
    p_emm "You're suffering from trauma, but we fear it's something worse.{w} A psychiatrist checked up on you and... your case is beyond counseling. Your memory is temporarily impaired because of the drugs they've administered."

    "Ha! Ridiculous! Where the hell have I heard of that?"

    is4 "I hardly think you're trustworthy at all."
    p_emm "Why not? I'm an authority figure here speaking to you. I can even show you my badge the next time we personally meet."
    is4 "Exactly, but my mind is beyond stupor.{w} A memory-blocking drug? Ha! You read science fiction way too much, Inspector!"
    stop music
    unk "Pardon the chap, my dear. It appears he had forgotten I approved of it myself."

    "That voice... someone who I haven't heard in a long time.{w} Finally, someone I can trust."

    is4 "{cps=10}Papa...? Is that you?{/cps}"

    play music bg_therunaway loop
    mr_shi "That's the daughter I remember!{w} You're doing just fine over there. Mama and I have been monitoring you everyday."

    "Throat dry, heart heaved, a stream of tears stealthily trickled down my cheeks. Relief came, but my hands insisted they wipe the tears later."

    mr_shi "Inspector here is a former crime laboratory assistant. I've known him for quite some time now.{w} It's just that he cannot grasp the details well enough even during his tenure, especially if it's jargon-filled."
    mr_shi "I'll summarize what he meant.{w} You underwent a series of instense traumatic events in the past few weeks, affecting your psyche. You were also in a state of frenzy the night you were found.{w} That explains the first few days of your confinement."
    mr_shi "The tranquilizers administered to you had a side effect; hence, the memory blocks you are not aware of.{w} I wish to go into more details, but focus on your recovery for now."
    mr_shi "Just let yourself know that you're in a safe place. This will be your home until you restabilize.{w} Then you worry about the details of you-know-what."

    window show
    nvl clear
    narr "Cut. Static. The room filled with silence once more. All tension dissipated gradually after hearing Papa talk."
    narr "And what was that gentleman's name? Emmerich? Commit that to memory.{w} Seems a shady guy, but I'll get him something nice for rescuing me."
    narr "Was I even? I don't know. And for how long? I stopped counting the seconds after a prolonged period of isolation."
    narr "Isolation... even now... with only voices as a means of communication. They can't show their faces to me at least, can they?{w} How am I to know --{nw}"

    nvl clear
    window hide

    stop music
    scene black
    centered "{i}You believe more in the things that you {b}cannot see{/b} yet {b}only feel?{/b}{/i}"

    scene bg whiteroom
    is4 "Can you even hear him?!"
    p_emm "Him? Who's him? Inoue, what's the matter?"

    play sound sfx_heartbeat loop
    "{cps=*0.75}The words came from my mouth...{/cps} {cps=10}without a doubt... without a doubt...{/cps}"
    "{cps=10}Naïve girl... Naïve girl...{/cps} One step closer to scorching along with him... One step closer to martyrdom... One step from the blade to claw the cat's paw!"

    p_emm "Respond, please. Are you alright?"

    "Where is he? Where is he? If he intends no harm, then why isn't he showing himself?! Up in the ceiling? Somewhere a hair's breadth behind me?"
    "Or is he there... staring straight into the lone girl sitting quietly at the box's center -- posing as the girl himself? {cps=4}Ha... Hahaha...{/cps}"

    is4 "I know you're there. {i}*snicker* *snicker*{/i}{w} Feast your eyes all you want. Come at me if you will. Break the glass that binds your presence! {cps=10}Come... Come... I'm waiting...{/cps}"
    "{i}Requesting assistance. Patient No. 4577 requires medical attention immediately!{/i}"

    scene black
    "Then everything plunged into an abyss."
    "The light vanished in an instant, resetting the environment into its initial state.{w} Darkness, silence, inertia -- that and all other descriptions applicable."
    "Nobody move, not even a single twitch. Nobody speak, not even a mere gasp."
    stop sound

    cen "{i}Hey... Over here...{/i}"

    "Where did that come from?"

    play sound sfx_static2
    "{b}{i}*WHIRR*{/i}{/b}"
    stop sound

    scene bg whiteroom nightmare
    play music bg_ghoststory loop
    window show
    nvl clear
    narr "Red lights. A black box where no one has looked into before, with the only way out coated by the void's color. And serenity became overshadowed by suspicion."
    window hide
    show inoue creepy smile2 with Dissolve(2.0)
    window show
    narr "The third entity became animated, independent to that of its own image.{w} It's closer than ever, pitter-pattering the glass with its finger. And like rain, it fell horizontally."
    narr "Its gaze enticed the image, urging it to come closer. The latter's feet bewitched, they brought it closer to the mirror...{w} {cps=5}closer... closer...{/cps}"
    window hide
    show inoue creepy smirk with Dissolve(2.0)
    window show
    narr "...and its playful smile curved upwards more than ever."

    nvl clear
    window hide

    show inoue creepy focused with Dissolve(0.2)
    u_is4 "Hi!"
    f_is4 "{cps=10}You... you can... huh?{/cps}"
    show inoue creepy smirk with Dissolve(0.2)
    u_is4 "Afraid of your own skin, now? Silly girl. I'd give you a dollar for that. Want to know why?{w} I am aware of this exact thing on your mind right now. Besides, I {i}am{/i} you, after all. Is that wonderful or not?"
    f_is4 "You're an image. There's no way you are my mind's projection. There's... there's no way..."
    show inoue creepy smile3 with Dissolve(0.2)
    u_is4 "Oh, but there is! You could not have lived without me -- better yet, could have stayed as an infant forever."
    show inoue creepy smirk with Dissolve(0.2)
    u_is4 "Oh, but there is! You could not have lived without me -- better yet, could have stayed as an infant forever.{fast} Look at you now. Look at how much you've grown! {i}*giggle*{/i}"
    f_is4 "Have it your way. What do you want?"
    show inoue creepy smile2 with Dissolve(0.2)
    u_is4 "You are locked up in this cage, aren't you? Sometimes, we wonder, \"When will I be away from this hellhole?\"{w=1.0}{nw}"
    show inoue creepy smile with Dissolve(0.2)
    u_is4 "You are locked up in this cage, aren't you? Sometimes, we wonder, \"When will I be away from this hellhole?\"{fast} Oh, wait! Not close enough, I guess. My bad!"
    f_is4 "Tell me..."

    cen "{cps=10}{i}It's useless... all useless...{/i}{/cps}"

    f_is4 "This asylum is driving me to bedlam more than it cures me! Just say something, damn it!"
    show inoue noglass proud with Dissolve(0.2)
    u_is4 "If thy fervent desires the world out the box yonder, much merriment... whatever the hell that means.{w} But would you, really?"
    f_is4 "A fist, do you fancy?"
    u_is4 "The box here is your cage, life sentence if I'd say so.{w} Why would you ever wish to opt out? It's peaceful here, much more than the chaotic world outside."
    f_is4 "Are you with me or against me?!{w} Have you forgotten how much shit we went through? {b}*GASP*{/b}"
    show inoue creepy focused with Dissolve(0.2)
    u_is4 "The mind may forget, but the flesh always houses an imprint even so miniscule.{w} Pain, Inoue... Pain... Why would you want out if there is pain ready to welcome you? Have you forgotten already?"
    f_is4 "..."
    show inoue creepy focusedpose with Dissolve(0.2)
    u_is4 "{cps=15}Your own pain -- it stings... or would you prefer to remind yourself of --{/cps}{nw}"
    hide inoue
    show bg fire
    play sound sfx_fire2
    hide bg fire with Dissolve(1.0)

    scene bg whiteroom nightmare
    show inoue creepy focusedpose
    f_is4 "Shut up."
    show inoue creepy smirkpose with Dissolve(0.2)
    u_is4 "Yes. The blaze... The blaze... Who does not want to forget? And those screams. Aren't they beautiful?"
    f_is4 "{cps=10}I want to forget... I want to forget...{/cps}"
    show inoue creepy smile3 with Dissolve(0.2)
    u_is4 "Have you been listening, or do I need to spell it out?{w} The flesh does not forget. It {b}never{/b} forgets! He was pleading, begging, and you never gave a damn."
    f_is4 "{cps=10}It wasn't my fault... I never intended to...{/cps}"
    stop sound
    stop music fadeout 2.0

    window show
    show inoue creepy blood angry
    cen "{i}THEN HE WOULDN'T HAVE BEEN DEAD!{w=1.0}\nGet it into that thick skull of yours!{/i}{w=1.0}{nw}"
    show inoue creepy blood snap
    cen "{i}{cps=*0.5}You killed him.{/cps}{w=1.0}\nYou killed him!{w=1.0}\n{cps=*1.5}YOU KILLED HIM!!!{/cps}{/i}{w=1.0}{nw}"
    show inoue creepy blood snap2
    play sound sfx_giggle
    cen "{i}{cps=15}Hahahahahaha...{/cps}{w=1.0} {cps=15}Hahahahahahahahaha!{/cps}{w=1.0}\n{cps=20}{b}AHAHAHAHAHAHAHAHAHAHAHAHAHAHA!!!{/b}{/cps}{/i}"
    window hide

    scene black
    f_is4 "I AM INNOCENT!!!"

    play sound sfx_whoosh
    "{i}*WHOOSH*{w=1.0}{nw}"
    play sound sfx_glass
    "{i}*WHOOSH*{fast} {b}*SHATTER*{/b}{/i}"

    scene bg blood
    c_is4 "Glk! Gah... {i}*croak*{/i}"

    "I buried my fist into that sentient monster, a cruel abomination that seeks to destroy.{w} Shut up... Just shut up..."
    "But it wouldn't.{w} Its figure cracked, yet its sentience remained intact. Its eyes fixated towards mine in a manner never so condescending.{w} A laugh... that same mocking laugh that --"

    u_is4 "What a waste. {i}*snicker* *snicker* *snicker*{/i} What are you gonna do about it?"

    "Just as the blood oozed from the shards my fist was buried in, the entity consumed it within an instant.{w=2.0}{nw}"
    play music bg_corruption loop
    "Just as the blood oozed from the shards my fist was buried in, the entity consumed it within an instant.{fast} It wants me... It wants me!"

    c_is4 "Let me go! Uh... Ahhhhh!!!"

    show bg eyesdark with Dissolve(1.0)
    hide bg eyesdark
    show bg darkhallway3 nightmare with Dissolve(1.0)
    hide bg darkhallway3
    show bg clinic with Dissolve(1.0)
    hide bg clinic
    scene bg whiteroom nightmare
    "No matter how hard I fight, it wouldn't release me. How about it? An organic chain in a cage.{w} The image flashed several times. How can the mind forget? How can it?"

    show inoue creepy blood snap with Dissolve(0.2)
    u_is4 "Don't be pushy. I'll let you free if you wish...{w=1.0} but for just a little longer, hm? I missed the human touch.{w} Being all alone must be so... sad, wouldn't you agree? Hehehehehe..."
    c_is4 "I'm begging you! Please! Please! Ugh!"
    u_is4 "{cps=10}Yes... That's it... The magic words... There's the good girl...{/cps} {i}*giggle*{/i}"
    play sound sfx_girlcry
    c_is4 "*SNIFF* *SNIFF*{w=1.0} {b}*SOB*{/b}"
    u_is4 "Awww... Don't cry. I'm sorry, okay? Never mind any of that. {i}*giggle*{/i}{w} I'm done playing with you. What do you say I give you a lollipop or something before you scurry along home?"
    stop sound
    show inoue creepy blood snap2 with Dissolve(0.2)
    u_is4 "Oh, I know! This!{w=1.0}{nw}"
    hide inoue with vpunch
    stop music fadeout 2.0

    play sound sfx_splatter
    "{b}*SPISH*{/b}{w=1.0}{nw}"

    scene white
    r_is4 "Gulk!{w=1.0}{nw}"

    "My gaze shot up into the sky, now white as before. The bastard got me with a bee sting, no doubt about it.{w=1.0}{nw}"
    "And slowly... slowly... the phantom of sleep drew itself over me.{w=1.0}{nw}"

    cen "{i}{cps=10}Star light, Star bright...{w=1.0}\nFirst star I see tonight...{/cps}{/i}{w=1.0}{nw}"

    "{cps=10}Slowly... Slowly... lulling me...{/cps}{w=1.0}{nw}"

    cen "{i}{cps=10}I wish I may, I wish I might...{w=1.0}\nHave the wish I wish tonight!{/cps}{/i}{w=1.0}{nw}"

    scene black with Dissolve(2.0)
    "{cps=10}...to sleep.{/cps}{w=1.0}{nw}"

    play sound sfx_thud2
    "{b}*THUD*{/b}"

    "Good night, dear Inoue..."
    return

label ch02_05_volleyball:
    scene black with fade
    "JULY 4, 2013 - 1730H"

    play sound sfx_volleyball loop
    scene bg school fields evening with fade
    window show
    nvl clear
    narr "Like fire, the ball blazed through the air and across the net, barely touching the fabric.{w} Two fists of equal ferocity sent it back to the opposing side. Immediately, five players rallied for the counter."
    narr "{b}{i}*THUD* *POW*{/i}{/b}"
    stop sound
    narr "Come the sixth player!"

    window hide
    show hiroshi pe angrytalk at Eight2 with Dissolve(0.5)
    show hiroshi pe angrytalk at Eight3 with Dissolve(0.25)
    play sound sfx_volleyball2
    show hiroshi pe angrytalk at Eight4 with vpunch
    window show
    nvl clear
    narr "Rushing down to the middle of the field, knees bent to jump, arm stretched upwards to the sky, Hiroshi delivered the spike.{w} A killing blow!{w} The force nearly made a crater out of the field."
    window hide
    show hiroshi pe smile2 at Eight3 with Dissolve(0.2)
    show ichirou pe happy at Eight2 with Dissolve(0.2)
    window show
    narr "One of the opposing players chased after the ball as Hiroshi's team celebrated their victory. Once he returned, the opposing sides exchanged high-fives under the net."
    window hide
    hide hiroshi with Dissolve(0.2)
    hide ichirou with Dissolve(0.2)
    play music bg_porchswingdays loop
    window show
    narr "Akira and Yoshiro from the opposing side, and Hiroshi and Ichirou the winning side, sat together on the auditorium steps. They enjoyed a ready-made iced tea Ichirou brought."

    nvl clear
    window hide

    show yoshiro pe smiletalk at Eight5 with Dissolve(0.2)
    show hiroshi pe smile at Eight1 with Dissolve(0.2)
    ys6 "You've shown real talent as always there, buddy. Been training for the Intramurals already?"
    hk7 "Easy. Easy. What's a man of few words got to do in his spare time? {i}*chuckle*{/i} I've already told you about my plans for this, remember?"
    show yoshiro pe smirk at Eight5 with Dissolve(0.2)
    ys6 "Of course, V-League rookie. You've been telling us that since First Year."
    show hiroshi pe determined at Eight1 with Dissolve(0.2)
    hk7 "Someday... Someday... When they allow men, that is."

    show akira pe blank at Eight3 with Dissolve(0.2)
    show ichirou pe smile at Eight7 with Dissolve(0.2)
    "The four finished their drink. Ichirou wiped the pitcher dry."

    show akira pe boredtalk at Eight3 with Dissolve(0.2)
    show yoshiro pe blankleft at Eight5 with Dissolve(0.2)
    show hiroshi pe bored at Eight1 with Dissolve(0.2)
    show ichirou pe serious at Eight7 with Dissolve(0.2)
    ai2 "How do we go about the review sessions next week? Science will overload our minds for sure!"
    show hiroshi pe boredtalk at Eight1 with Dissolve(0.2)
    hk7 "I've discussed this with Miyu, Ayumi, and Sayo.{w} The modules are scheduled to be distributed tomorrow morning. That way, all of us would have a head start for the weekend."
    show hiroshi pe boredtalkleft at Eight1 with Dissolve(0.2)
    hk7 "For each day, we focus on a specific area:{w} Gen. Sci. for Monday, Biology for Tuesday, Chemistry for Wednesday and Thursday, and Physics for Friday."
    show akira pe confused at Eight3 with Dissolve(0.2)
    ai2 "Wait. How is Physics low-priority? It'll get the least amount of time for sure."
    show hiroshi pe boredtalk at Eight1 with Dissolve(0.2)
    hk7 "Mrs. Kaida's got our backs, remember? She's been bugging us to study since the third week!{w} Don't even bother spending a full day on it."
    show yoshiro pe smile at Eight5 with Dissolve(0.2)
    ys6 "Besides, I've got a cousin who is at the top university right now. Swear, there's little to no Physics in the exam."
    show hiroshi pe boredtalk at Eight1 with Dissolve(0.2)
    hk7 "See my point?"
    show akira pe serious at Eight3 with Dissolve(0.2)
    ai2 "That's not even close to wthat you said!"

    show hiroshi pe smile2 at Eight1 with Dissolve(0.2)
    show ichirou pe smirkleft at Eight7 with Dissolve(0.2)
    show yoshiro pe smirk at Eight5 with Dissolve(0.2)
    "The group burst into laughter, stalling the discussion briefly."
    stop music fadeout 2.0

    show ichirou pe happy at Eight7 with Dissolve(0.2)
    show hiroshi pe smile at Eight1 with Dissolve(0.2)
    iy1 "Alright! Last game!"

    show ichirou pe smile at Eight7 with Dissolve(0.2)
    show yoshiro pe surprised at Eight5 with Dissolve(0.2)
    show hiroshi pe smile2 at Eight1 with Dissolve(0.2)
    show akira pe happy at Eight3 with Dissolve(0.2)
    "\"GAME!!!\""
    hide ichirou with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    hide akira with Dissolve(0.2)
    hide hiroshi with Dissolve(0.2)

    window show
    nvl clear
    narr "The four rejoined the others at the field.{w} This time, the twelve players agreed for a swap."
    show hiroshi pe determined at Eight3 with Dissolve(0.2)
    show akira pe determined at Eight2 with Dissolve(0.2)
    show ichirou pe smirk at Eight1 with Dissolve(0.2)
    narr "Akira, along with two others, joined Hiroshi's side."
    show yoshiro pe smile at Eight8 with Dissolve(0.2)
    narr "All twelve players move into position. Yoshiro steps in for the first service.{w} Hand raised, he visualizes the perfect shot for an ace. Ichirou, Akira, and Hiroshi, all in triangle-like formation, anticipated his move."
    window hide
    show yoshiro pe smile at Eight7 with Dissolve(0.5)
    play sound sfx_volleyball2
    show yoshiro pe smirk at Eight6 with hpunch
    play music bg_chasingvillains loop
    window show
    narr "BAM!"

    play sound sfx_volleyball loop
    nvl clear
    narr "The three at the front rush for a counterattack. A fist managed to send the ball floating once again, down for a pass, and a third for a blow!"
    narr "At Yoshiro's court, the players caught the ball easily, repeating the movements of the enemy team. Likewise, they sent it back at the third pass."
    narr "However, Akira had found a vantage point near the net, sending the ball down after barely passing it."
    stop sound
    stop music
    show akira pe serious at Eight4 with Dissolve(0.25)
    play sound sfx_volleyball2
    show akira pe fang at Eight4 with vpunch
    narr "SLAM!"

    nvl clear
    window hide

    show yoshiro pe surprised at Eight7 with Dissolve(0.2)
    show akira pe happy at Eight4 with Dissolve(0.2)
    ai2 "Yes! One for us!"
    stop music fadeout 2.0

    scene bg msci evening with fade
    play sound sfx_whistle
    play music bg_autumnday loop
    window show
    nvl clear
    narr "At six, the guard gave off the whistle and made his rounds to rally any stray students around the campus."
    show akira pe smile at Three2 with Dissolve(0.2)
    show hiroshi pe bored at Three1 with Dissolve(0.2)
    narr "Ichirou locked their classroom and rejoined Akira and Hiroshi near the front desk.{w} They were all covered in sweat."

    nvl clear
    window hide

    show ichirou pe smile at Three3 with Dissolve(0.2)
    iy1 "Want to cool off at 7-11 for old time's sake?"

    show akira pe surprisedtalkleft at Three2 with Dissolve(0.2)
    "Akira checked his phone and sent a quick text message to his parents. He took from his backpack a coin purse."

    show ichirou pe smirk at Three3 with Dissolve(0.2)
    iy1 "Wow! That milkfish design still a thing? {i}*chuckle*{/i}"
    show akira pe confused at Three2 with Dissolve(0.2)
    ai2 "Oh, this? I've been having this since First Year."
    show ichirou pe smirkleft at Three3 with Dissolve(0.2)
    show hiroshi pe smile2 at Three1 with Dissolve(0.2)
    iy1 "Really? We never saw that despite the countless number of times we did some projects at your place. Isn't that right, Hiroshi?"
    hk7 "Right. I might have been too oblivious to notice, but that's just me!"
    show akira pe smile at Three2 with Dissolve(0.2)
    ai2 "Guess I'm just too shy to let other eyes on it.{w} Not that you might not believe in these things, but this is my lucky charm."
    show ichirou pe proudclosed at Three3 with Dissolve(0.2)
    iy1 "Oooooohhhh... So you've been preserving its mojo for something big later on?{w} Tell you what, smart guy. You don't need a talisman to influence your future. I don't, so why should you?"
    show akira pe serious at Three2 with Dissolve(0.2)
    ai2 "Tell you what, {i}smarter guy{/i}, ever heard of {i}sentimental value{/i}?{w} Things like these can't be simply obtained from a random vendor. They have heart. Know what I'm saying?"
    show akira pe smile at Three2 with Dissolve(0.2)
    ai2 "Besides, this purse is just an object.{w} Isn't your item of sentimental value not a {i}what{/i} but a {i}who{/i}? {i}*snicker* *snicker*{/i}"
    show akira pe fang at Three2 with Dissolve(0.2)
    show hiroshi pe boredtalk at Three1 with Dissolve(0.2)
    show ichirou pe serioustalk at Eight5 with Dissolve(0.2)
    iy1 "Hey! Below the belt!"
    show hiroshi pe angrytalk at Three1 with Dissolve(0.2)
    hk7 "Break it up!{w} Let's just go to the store, buy some cone or chips, and{nw}"
    show hiroshi pe angrytalk2 at Three1 with Dissolve(0.2)
    hk7 "Break it up!{w} Let's just go to the store, buy some cone or chips, and{fast} chill out, you hotheads!"
    show akira pe serious at Three2 with Dissolve(0.2)
    show ichirou pe focus at Eight5 with Dissolve(0.2)
    "\"Grrrrrrr...\""
    hide ichirou with Dissolve(0.2)
    hide akira with Dissolve(0.2)
    hide hiroshi with Dissolve(0.2)

    scene bg freedompark night with dissolve
    window show
    nvl clear
    narr "The three boys gathered their belongings and exited through the school gate."
    narr "Their topics diverted from the fish purse, bringing them back to the usual school talk. There were mentions of TV shows and video games, but the discussions lasted short."
    narr "They passed by the park, now filled with students practicing some dances and lovers cuddling under the dimming lights.{w} Of course, the three took the shortest path through and ended up on the convenience store after crossing to the end of the next block."

    window hide
    stop music fadeout 2.0
    scene bg conveniencestore with dissolve
    window show
    nvl clear
    narr "Ichirou reserved three seats as Akira and Hiroshi went to purchase two bags of chicharron.{w} As they queued, Ichirou threw his Reward Card to Akira. They paid for the chips, used the card, and returned to Ichirou."
    window hide
    show ichirou pe worriedleft at Three1 with Dissolve(0.2)
    show hiroshi pe bored at Three2 with Dissolve(0.2)
    show akira pe bored at Three3 with Dissolve(0.2)
    play sound sfx_eatingchips loop
    window show
    narr "Unlike the walk, they silently munched away at the snack, probably running out of things to discuss.{w} At one point, none of them reached into the bag, instead staring silently through the glass."
    narr "The supposedly fun side trip turned to a dull moment in an instant."

    nvl clear
    window hide

    show akira pe sigh at Three3 with Dissolve(0.2)
    ai2 "Wrong move."
    show hiroshi pe boredtalk at Three2 with Dissolve(0.2)
    hk7 "What is?"
    show akira pe boredtalk at Three3 with Dissolve(0.2)
    ai2 "That. You know... I should've just gone home earlier. Every tick of the clock drives me nervous."

    show ichirou pe worried at Three1 with Dissolve(0.2)
    stop sound
    "Ichirou studied his friend carefully, surprised at such uncharacteristic remarks."

    play music bg_twotogether loop
    show hiroshi pe worriedleft at Three2 with Dissolve(0.2)
    hk7 "I feel the same. Everybody else does. Wish we had Kirisaki here to allay our worries, but...{w} {b}*SIGH*{/b} The bastard had to take him out first, doesn't he?"
    show ichirou pe worriedtalk at Three1 with Dissolve(0.2)
    iy1 "Wait. {i}first{/i}?"
    show hiroshi pe angry at Three2 with Dissolve(0.2)
    hk7 "You forgotten quickly. Say it happens again, the one at Sacred Heart Academy?"
    show ichirou pe surprised at Three1 with Dissolve(0.2)
    iy1 "Nonsense. What does a Curse Killing incident from another town have to do with ours?"
    show hiroshi pe angrytalk at Three2 with Dissolve(0.2)
    hk7 "Yeah. Like I'd buy any of that. Emphasis on the word, \"curse,\" please."
    show ichirou pe serious at Three1 with Dissolve(0.2)
    iy1 "Believe whatever you wish. No hard feelings if we disagree."

    "Eventually, they consumed the first bag and moved on to the second.{w} They munched away at the first few chips before continuing their discussion."

    show hiroshi pe smiletalk at Three2 with Dissolve(0.2)
    hk7 "I'm planning on visiting the clinic on the weekend. Hope I'll be getting some answers from her.{w} Who's with me?"
    show ichirou pe worriedtalk at Three1 with Dissolve(0.2)
    iy1 "But we're not even sure if Inoue is stable.{w} Like I have any guts or indecency to ask Ms. Harada or her parents about it. Do you, guys?"
    show akira pe blank at Three3 with Dissolve(0.2)
    ai2 "That's off limits for me. I'd rather sit here and wait."
    show hiroshi pe worriedleft at Three2 with Dissolve(0.2)
    hk7 "Come on, Pres. It's my former classmate we're talking about here. On top of that, a witness!"
    show akira pe boredtalk at Three3 with Dissolve(0.2)
    ai2 "Or a suspect if she ever was one."
    show ichirou pe serioustalkclosed at Three1 with Dissolve(0.2)
    iy1 "Or a suspect if she ever was -- Come on, Akira. Not you, too?{w} You're showing the same symptoms as she did a month back. Cheer up! You're scaring the hell out of me."
    show akira pe surprisedtalkleft2 at Three3 with Dissolve(0.2)
    ai2 "Fine. I'm sorry."
    show hiroshi pe boredtalk at Three2 with Dissolve(0.2)
    show ichirou pe serious at Three1 with Dissolve(0.2)
    hk7 "But Akira has a point.{w} There's a hole in this story we aren't seeing yet, an important piece of the puzzle we are missing.{w} There {i}is{/i} a possibility. There might be.{nw}"
    show akira pe surprisedtalkleft at Three3 with Dissolve(0.2)
    show hiroshi pe boredtalkleft at Three2
    show ichirou pe worriedtalkleft at Three1
    stop music fadeout 2.0
    ai2 "Hold on. Isn't that...?"
    hide akira
    hide hiroshi
    hide ichirou

    scene bg street night with dissolve
    show yoshiro pe blankleft at Eight6
    "In the middle of Hiroshi's contemplation, they all looked towards the direction of Akira's finger.{w} At the jeepney terminal across the street is Yoshiro, still in his changed clothes."

    ai2 "Didn't he leave before us?"
    hk7 "Well, that's true. We saw them -- he and his girlfriend -- out the gate while you were locking up the room."

    hide yoshiro with Dissolve(1.0)
    "At his last diction, Yoshiro left the queue and went further into the terminal. Ichirou looked more puzzled at the two than Yoshiro himself."

    scene bg conveniencestore with dissolve
    show ichirou pe serious at Three1 with Dissolve(0.2)
    show hiroshi pe bored at Three2 with Dissolve(0.2)
    show akira pe surprisedtalkleft at Three3 with Dissolve(0.2)
    play music bg_undaunted loop
    iy1 "Ohhhh... kaaayyy? You just spelled it out, so what's odd about it?"
    show hiroshi pe boredtalk at Three2 with Dissolve(0.2)
    hk7 "Check the time. Yoshiro left the campus right after the whistle.{w} Let me ask you, is thirty minutes enough to make a round trip to his girlfriend's house and back? That's five to ten minutes short!"
    show ichirou pe serioustalk at Three1 with Dissolve(0.2)
    iy1 "I agree, so what's your point?"
    show akira pe worriedleft at Three3 with Dissolve(0.2)
    ai2 "Doesn't that remind you of anything, Ichirou? Miyu told us about it early morning on Tuesday."
    show ichirou pe confused at Three1 with Dissolve(0.2)
    iy1 "Aaaaaahhh... He saw my double the night of his date, whatever it is. Yeah, he mentioned something about it."
    show ichirou pe surprised at Three1 with Dissolve(0.2)
    iy1 "Wait up!{w} What we just saw is something else. That could've been his look-alike, dummy! What's so scary about it?"
    stop music
    show akira pe smilefang at Three3 with Dissolve(0.2)
    ai2 "Nothing. I just wanted to mess with you. You know, break the ice. Hehehe... Hehehehehe!"

    play sound sfx_smack
    show ichirou pe focus at Eight5 with vpunch
    show hiroshi pe boredtalk at Three2
    show akira pe surprisedtalkleft at Three3
    "{b}*SMACK*{/b}"

    play music bg_merrygo loop
    show ichirou pe smirk at Three1 with Dissolve(0.2)
    iy1 "Now, we're talking, Akira. That's the mischievous kid I know."
    show hiroshi pe smile2 at Three2 with Dissolve(0.2)
    hk7 "I must admit, you caught me off-guard for a moment there. {i}*chuckle*{/i}"
    show ichirou pe proudclosed at Three1 with Dissolve(0.2)
    iy1 "Do they have Wi-Fi here? I'll just message Yoshiro.{w} Whatever caper you just brought had me thinking."
    show akira pe worried at Three3 with Dissolve(0.2)
    ai2 "Look. I'm sorry. Just don't beat me with that broadsheet again."
    show ichirou pe smile at Three1 with Dissolve(0.2)
    iy1 "Relax! I'm not going to.{w} There's just something I want to ask him. Nothing serious, by the way."
    show hiroshi pe smiletalk at Three2 with Dissolve(0.2)
    hk7 "Speaking of, where {i}did{/i} you get that broadsheet? Stuffed it into your backpack this whole time?"
    show ichirou pe proudclosed at Three1 with Dissolve(0.2)
    iy1 "From hammerspace if that satisfies you."
    stop music fadeout 2.0

    show ichirou pe smile at Three1 with Dissolve(0.2)
    show akira pe smile at Three3 with Dissolve(0.2)
    window show
    nvl clear
    narr "Soon, they consumed the second bag and moved on to the lighter topics."

    window hide
    scene bg street night with fade
    hide akira with Dissolve(0.2)
    window show
    
    narr "At seven, Ichirou called it a day and they dispersed. Akira went first, the jeepney to his village just across the street."
    narr "This left Ichirou and Hiroshi, walking through the jeepney terminal to the clock tower. Situated at the center is a majestic fountain, lights dancing in colorful patterns as the water spouts up from the distribution pipe."
    scene bg wetmarket night with dissolve
    narr "They crossed the street towards the market and stopped just in front of a grocery store."

    nvl clear
    window hide

    show hiroshi pe smile at Three3 with Dissolve(0.2)
    show ichirou pe seriousclosed at Three1 with Dissolve(0.2)
    iy1 "I forgot to ask Akira."
    show hiroshi pe angry at Three3 with Dissolve(0.2)
    hk7 "What?"
    show ichirou pe serioustalkclosed at Three1 with Dissolve(0.2)
    iy1 "What fruit their little investigation that evening has brought. The time when Kyou and Inoue's disappearances were announced?"
    show hiroshi pe bored at Three3 with Dissolve(0.2)
    hk7 "Didn't yield anything useful, I bet. Let's just hope for the best on Saturday."
    show ichirou pe serioustalk at Three1 with Dissolve(0.2)
    iy1 "Alright. Just tell me everything you'll get from her. Let Sayo know too, if possible.{w} And if you run into him, please say \"Hi\" to Inspector Emmerich for me, will you?"
    show hiroshi pe smile at Three3 with Dissolve(0.2)
    hk7 "Affirmative."
    show ichirou pe serious at Three1 with Dissolve(0.2)
    hide hiroshi with Dissolve(0.2)

    window show
    nvl clear
    narr "Within a few moments, Hiroshi had bid Ichirou farewell as he boarded a jeepney.{w} Ichirou skirted the current side of the market to a tricycle stop."
    hide ichirou with Dissolve(0.2)
    scene bg bedroom with fade
    narr "By half-past seven, he was home.{w} He ate dinner and went up to his room immediately. He checked for any updates on Facebook and messaged some friends before shifting his attention to his homework."
    play sound sfx_beep3
    narr "A notification bell sounded, catching Ichirou's attention."

    nvl clear
    n_hk7 "I've asked permission from Mr. Shinozaki. Inoue seems to have suffered a nervous breakdown some four hours ago, but he assured she'll be fit by tomorrow. Even better on Saturday.{fast}"
    n_iy1 "Wish you the best. :) Though, I hope you're doing our assignment due tomorrow.{fast}"
    play sound sfx_beep3
    n_hk7 "After one more chapter. Hehehehe. :) Good night, Pres.{fast}"
    n_iy1 "Night.{fast}"

    nvl clear
    narr "Ichirou put his laptop to sleep and focused on his work.{w} There were some road blocks here and there, so he occasionally went down to piss or to make some sandwiches."
    narr "By ten o' clock, he was too tired to continue, setting aside the remaining load for tomorrow morning.{w} He re-opened his laptop and saw a new message from Yoshiro."

    nvl clear
    n_ys6 "I... don't know where they're getting at with this one, but I'm certain you did see me at the jeepney stop.{fast}"
    n_iy1 "Wait. Didn't you leave with her? :O That's fast!{fast}"
    play sound sfx_beep3
    n_ys6 "I already dropped her off by the time you three left the school... 6:00, wasn't it? I stayed for a while. Had to help her with a few things.{fast}"
    n_iy1 "Sure? Honest?{fast}"
    play sound sfx_beep3
    n_ys6 "Yes. I wouldn't deny that.{fast}"
    n_iy1 "Okay. Thanks, anyway.{fast}"

    nvl clear
    window hide

    scene black with fade
    "Ichirou's hands clammed as he closed the laptop's lid. He went to bed, thinking about the day's events.{w} He whispered to himself before passing out."

    iy1 "That doesn't make sense..."
    return

label ch02_06_visit:
    scene bg elevator with fade
    play music guest_flymetothemoon loop
    "JULY 6, 2013 - 1300H"

    window show
    nvl clear
    narr "I see why people despise this facility.{w} Look at it. It's gloomy and unwelcoming. Not even a hint of threat like they were described in the books."
    narr "But that's just a lens. Who knows, a cuckoo might be behind the story's conception without anyone noticing."
    play sound sfx_elevator
    narr "And as the elevator stops, here I watch the sinister plot unfold."
    stop music
    window hide
    scene bg receptiondesk with dissolve
    window show
    narr "The fourth floor's reception desk had two nurses stationed for the day.{w} They seemed chatty, conveying how slow the afternoon might have been. And of course, anyone with eyes would agree."
    show elisha blank at Three2 with Dissolve(0.2)
    narr "As I approached, the cuter of them welcomed me."

    nvl clear
    window hide

    hk7 "I've come to visit a patient -- Ms. Inoue Shinozaki."
    nurse "Do you have an ID card, sir?"
    hk7 "Here. I'm a schoolmate and friend of hers. Dr. Shinozaki will recognize me...{w=1.0} {cps=*0.5}if he's present, that is.{/cps}"
    show elisha surprised at Three2 with Dissolve(0.2)
    nurse "An MSCI student!{w} Excuse for a moment. Please have a seat, sir."

    hide elisha with Dissolve(0.2)
    "The sweet nurse efficiently dialed the ward Inoue is at.{w} She mentioned my name, keeping the positive tone throughout the call's duration. She hung up and motioned me to the desk."

    show elisha smile at Three2 with Dissolve(0.2)
    nurse "Your ID, Mr. Kano.{w} Head to 431 along the east wing. Dr. Shinozaki is expecting you."
    hk7 "Have a pleasant afternoon, madame, and thank you very much."
    hide elisha with Dissolve(0.2)

    window show
    nvl clear
    narr "The nurse returned to her mundane duty, waiting for another visitor to accommodate.{w} I, on the other hand, went off with my own business."
    scene bg hospitalcorridor with dissolve
    play sound sfx_whispers loop
    narr "This is a source of fuel, alright. Hearing these moans and nervous laughter in the absence of light concocts the worst possible scenario imaginable.{w} It draws people in, dragging the sane to the patients' world of insanity."
    narr "Still not enough to challenge my mettle. I've seen far worse in recent memory.{w} It keeps bugging people endlessly, its reputation becoming more of an annoyance than genuine fear."
    stop sound fadeout 1.0

    nvl clear
    show emmerich serious at Eight5 with Dissolve(0.2)
    narr "A well-built figure came into view, followed by a lankier man in uniform.{w} The former, definitely Inoue's father. But the other authority figure looked unfamiliar. He walked towards me after their brief conversation."
    narr "He replaced a notepad and pen in his coat, exchanging it with a brown organizer.{w} As he passed by me, he slowed his pace."

    nvl clear
    window hide

    show emmerich smile at Eight3 with Dissolve(0.2)
    p_emm "Whomever that basket belongs to, I wish them well!"

    "A spontaneous individual, I must remark. Could be rude but friendly enough to be forgiven."

    hk7 "Someone sent their regards to you. The Pres says, \"Hi.\""
    show emmerich smileteeth at Eight3 with Dissolve(0.2)
    p_emm "Ah, I recognize you just now! You must be from MSCI."
    show emmerich smile at Eight3 with Dissolve(0.2)
    p_emm "Ah, I recognize you just now! You must be from MSCI.{fast} Take care of Lady Shinozaki in there. She just had a bad fit two days prior."
    hide emmerich with Dissolve(0.2)

    "Then I stopped, turning my neck towards the inspector. On his face, a warm and gentle smile."

    hk7 "Hiroshi Kano. Pleasant afternoon to you, Inspector E."
    show emmerich smile2 at Eight1 with Dissolve(0.2)
    p_emm "I return the greeting.{w} Just be careful out there and straight home afterwards. Oh, and don't forget to return my regards to Ichirou!"

    play sound sfx_footsteps2
    hide emmerich with Dissolve(0.5)
    "With a nod from me, he quickened his pace. His figure gradually became smaller until he was no longer in sight."

    mr_shi "If you don't mind, son, I'll handle the basket for you."

    "Though surprised, we exchanged firm handshakes and engaged in small talk for a few minutes.{w} He recognized me as Inoue's classmate during Sophomore Year. I felt more at ease."
    "Even more when he invited me to his daughter's ward after ascertaining I visited alone."
    play sound sfx_dooropen
    scene bg hospitalward with fade
    "At least this room tells a different story, only that the bed is obscured from the hallway's view by a curtain.{w} Her brother is present, laughing at the afternoon show's gags."

    mr_shi "We have a guest! Sweetheart, Hiroshi's come to visit.{w} Brought some fruits for you. Need to watch your nutrition, eh? You're starting to look like a scurvy-ridden sailor. {i}*chuckle*{/i}"
    play music bg_therunaway loop
    show inoue casual angry at Three1 with Dissolve(0.2)
    is4 "Papaaaa!{w=1.0}{nw}"
    show inoue casual determined at Three1 with Dissolve(0.2)
    is4 "Papaaaa!{fast} It's okay, Hiroshi. Welcome to my room."
    tomonori "Hey! What's up?"
    show hiroshi casual bored at Three3 with Dissolve(0.2)
    hk7 "I've seen better days. Can't imagine being cooped up here for days, let alone weeks."
    show hiroshi casual smirk at Three2 with Dissolve(0.2)
    hk7 "I've seen better days. Can't imagine being cooped up here for days, let alone weeks.{fast} Though I admit, this looks better."

    "Unlike the patient it houses.{w} Inoue is unkempt, the traces of rehabilitation screaming from her appearance. She looks too disorganized to hold a decent conversation with, but certainly stable enough to keep herself together."
    "She forced a grin but couldn't come up with a clever remark.{w=1.0} Understandable."

    show inoue casual sigh at Three1 with Dissolve(0.2)
    is4 "Finally, a change of wind! {b}*EXHALE*{/b} Ever since day one, that Emmerich guy comes to bombard me with questions upon questions without end!{w} How does {i}that{/i} expect me to recover?"
    show hiroshi casual smileteeth at Three2 with Dissolve(0.2)
    hk7 "I see your point, Inoue. {i}*chuckle*{/i}{w} You need to loosen up a bit like usual."
    show inoue casual schemingopen at Three1 with Dissolve(0.2)
    is4 "But, hey. I appeciate you dropping by this weekend. Thanks for the berries, too.{w} Don't you have more important things to attend to like...{w=1.0} sleeping? {i}*giggle*{/i}"
    show hiroshi casual smile at Three2 with Dissolve(0.2)
    hk7 "I thought of that, too.{w} But you'll forgive me.{w=0.5} I'm afraid I have to resort to Mr. Inspector's routine for the day."

    stop music fadeout 2.0
    show inoue casual seriouspose at Three1 with Dissolve(0.2)
    show hiroshi casual worried at Three2 with Dissolve(0.2)
    "Her expression darkened, eliminating her eyes' radiance upon hearing that sentence."

    show inoue casual serioustalk2 at Three1 with Dissolve(0.2)
    is4 "Good grief... How you've wasted your visit.{w} Overdose in medications and overdose of questions. You are aware how they {i}don't help{/i} with the situation, do you?"
    mr_shi "Now, now, dear. Calm down. Take a deep breath like I always tell you to."
    show inoue casual serioustalk at Three1 with Dissolve(0.2)
    is4 "But Papa..."
    mr_shi "Inoue, please show courtesy to your friend. You don't get to see him every visit.{w} Besides, friends like Hiroshi-kun can understand your situation better, isn't that right?"
    show inoue casual serious at Three1 with Dissolve(0.2)
    is4 "..."
    mr_shi "Don't worry about it, son. She doesn't sulk this often back home.{w} Feel free to invite your friends to see her. It will surely lift her spirits up faster."
    tomonori "Except that one {i}persona non grata{/i}. You know -- rather, ought to know -- who."

    show hiroshi casual bored at Three2 with Dissolve(0.2)
    "An unwelcome guest, huh? Bet they had a suspect already. Didn't even bother to ask Emmerich earlier.{w} The question... who is this {i}persona non grata{/i}?"

    mr_shi "It's best if Inoue tells you. You can ask Tomonori afterwards -- he was present at the time.{w} Now, if you'll excuse me..."

    play sound sfx_doorknob
    "He left the three of us in the room. Tomonori-san nodded at me as I approached the bedside."

    play music bg_ghoststory loop
    show inoue casual blank at Three1 with Dissolve(0.2)
    is4 "Tell me what you know so far."
    show hiroshi casual boredleft at Three2 with Dissolve(0.2)
    hk7 "That's an inversion..."
    show hiroshi casual boredclosed at Three2 with Dissolve(0.2)
    show inoue casual seriouspose at Three1 with Dissolve(0.2)
    hk7 "That's an inversion...{fast} Well, to start, we've been coordinating with the authorities, Emmerich mostly, and Kirisaki's family. After his burial, we discovered some interesting leads."

    "From the details of her disappearance to the unknown figure's appearance last Sunday, she heard the message delivered to us. Save for one thing."

    show hiroshi casual bored at Three2 with Dissolve(0.2)
    hk7 "I return the question and I want to hear from you personally. Who is this unwelcome guest your brother is speaking of?"
    show inoue casual sighpose at Three1 with Dissolve(0.2)
    is4 "You probably won't like my answer, but I have no choice..."
    stop music fadeout 2.0

    "At an impulse, my ears leaned closer to her mouth.{w} Her voice felt shaky, and a glance told of her paling color."

    show inoue casual creepy worriedleft at Three1 with Dissolve(0.5)
    is4 "It's Sayo.{w=1.0} Every time I see her face on TV...{w=1.0} {cps=15}Every time I hear that transmission...{/cps}{w=1.0}{nw}"
    play sound sfx_heartbeat loop
    show hiroshi casual worried at Three2
    is4 "It's Sayo. Every time I see her face on TV... Every time I hear that transmission...{fast} {cps=10}Every time I close my eyes...{/cps} {i}*GULP*{/i}{w=1.0} {cps=5}Her voice... Her voice...{/cps}{w=1.0}{nw}"
    show hiroshi casual worriedtalk at Three2 with Dissolve(0.2)
    hk7 "{cps=10}Inoue, breathe...{/cps}{w=1.0}{nw}"
    show inoue casual creepy worriedtalkleft at Three1 with Dissolve(0.2)
    is4 "{cps=5}Those{/cps} {cps=12}sinister intentions{/cps} {cps=15}hiding beneath that mask,{/cps} {cps=15}a mask so innocent, you'll never see it coming...{/cps}{w=1.0}{nw}"
    show inoue casual creepy smirk at Three1
    is4 "{cps=8}Hehehe...{/cps}{w=1.0}{nw}"
    show inoue casual creepy smileteeth at Three1
    stop sound
    play sound sfx_giggle
    is4 "{cps=15}Hehehehehehehehehehe...{/cps}{w=1.0}{nw}"
    show hiroshi casual screamleft at Three2 with Dissolve(0.2)
    hk7 "Tomonori-san!"
    stop music fadeout 1.0

    show inoue casual sighpose at Three1 with Dissolve(0.2)
    show hiroshi casual worried at Three2 with Dissolve(0.2)
    "Her brother rushed to our aid, soothing Inoue until she mellowed down.{w} I gave her a glass of water, hoping it would clear her head."

    show inoue casual troubledtalk at Three1 with Dissolve(0.2)
    is4 "Sorry for the outburst.{w} {b}*SIGH*{/b} Been like this for days."
    show hiroshi casual worriedtalk at Three2 with Dissolve(0.2)
    hk7 "I understand, but please refrain from doing that. You really terrified me."
    show inoue casual troubled at Three1 with Dissolve(0.2)
    is4 "Perhaps my brother is up? I might risk another attack if I tell you more."
    hide inoue with Dissolve(0.2)

    show hiroshi casual bored2 at Three3 with Dissolve(0.2)
    "Tomonori-san obliged and motioned me to the far end. He prepared a monoblock for me to sit down."

    tomonori "Please keep this discreet. We regarded Sayo as a hostile presence after the incident. I'm sure my sis' reaction need no further explanations."
    show hiroshi casual serioustalk at Three3 with Dissolve(0.2)
    hk7 "My mouth's zipped, but why?{w=1.0} Sayo...{w=0.5} of all people?!"
    is4 "{b}{i}*GROAN*{/i}{/b}"
    tomonori "Keep it down, please."
    show hiroshi casual serious at Three3 with Dissolve(0.2)
    hk7 "I'm sure she wouldn't do such a thing. You're up against slander charges if your accusation is false. Most importantly, what proof do you have?"
    tomonori "I know. I know. It's kind of hard to believe personally. Honest.{w} I wasn't on the receiver's side at the time."
    show hiroshi casual serious2 at Three3 with Dissolve(0.2)
    hk7 "So she phoned your house and the call was intended for Inoue. And then?"

    "From his hand appeared a flash drive, and he cupped it into my hands. Now, his claim is starting to gain substance, if little."

    play music bg_interloper loop
    tomonori "On the night of June 13...{w=1.0}{nw}"

    hide hiroshi
    scene bg livingroom with fade
    show inoue casual troubled at RS with Dissolve(0.2)
    window show
    nvl clear
    narr "After handing Inoue the receiver, he returned to watching TV, lowering the volume as courtesy. Occasionally, he would glance towards his sister and observe her throughout the call's duration.{w} When she moved to the window, he lowered the volume further to eavesdrop."
    narr "He went away from the living room some twenty minutes later to take a \"side trip,\" or so he says.{w} He hid behind the wall, making sure their parents were already in their room so the setup would not look awkward."
    narr "He concealed himself as he observed Inoue's conversation with Sayo up until the farewell exchange.{w} She was shaken, an expression he knew that would take some intense threatening to achieve."

    nvl clear
    show inoue casual troubledtalk at RS with Dissolve(0.2)
    n_is4 "Good night, Sayo. See you tom --{nw}"
    narr "She spoke the name, but the call didn't end just yet.{w} Instead, what followed is a short moment of silence from her end."

    nvl clear
    show inoue casual sigh at RS with Dissolve(0.2)
    n_is4 "That's sweet, now would you please --{nw}"
    narr "Inoue was already irked at the caller, urging her to cut it out. She seemed tired, or..."

    nvl clear
    show inoue casual angry at RS with Dissolve(0.2)
    n_is4 "I need to sleep now, okay? Bye!{nw}"
    show inoue casual troubled at RS with Dissolve(0.2)
    play sound sfx_breathing
    narr "She slammed the receiver, taking a few deep breaths as she stared at the machine.{w} He tried to approach her, but she was no longer in good spirits.{w} And from his observations..."
    stop sound
    hide inoue with Dissolve(0.2)

    nvl clear
    window hide

    scene bg hospitalward with fade
    show hiroshi casual serious2 at Three3 with Dissolve(0.2)
    tomonori "I know our youngest well enough. Too shaken to smile or weep a moment after. Instead, she spoke nothing, darted past me like I was a statue.{w} It was odd!"
    tomonori "Good thing we always record any transmissions from the landline. We don't usually listen to call logs especially if intended for someone else, but this is an exception."
    tomonori "That USB -- have a listen for yourself.{w} You wouldn't believe me anymore if even its contents I describe to you."

    "He went on, adding the time when they last spoke the weekend after -- about the alumna.{w} Her reaction to the call might have caused her fever, he speculates. Personally, agreeable."

    show hiroshi casual bored2 at Three3 with Dissolve(0.2)
    hk7 "Another point that bothers me -- Why'd you think it was a good idea to ring the Ronoroas after Inoue's disappearance?{w} Have you any evidence at the time, too?"
    tomonori "What I just gave you."
    show hiroshi casual serious at Three3 with Dissolve(0.2)
    hk7 "{cps=8}Yeah... no.{/cps} Maybe not this time.{w} You discounted the fact that she could be innocent -- Heck, that allegedly threatening call could just be a silly prank! We three have been classmates in First Year. It's natural to view it from {i}that{/i} angle."
    show hiroshi casual serioustalk at Three3 with Dissolve(0.2)
    hk7 "Besides, how do you even smuggle two people out of the campus that same morning undetected? How do you propose Sayo could have done it?{w} Face it, you don't have anything."

    "He bit his lip, shaking his fists in contempt and eyes glared at me."

    show hiroshi casual bored2 at Three3 with Dissolve(0.2)
    hk7 "But I suppose I must give you the benefit.{w} Let's hear it now. Brought a laptop with you?"

    stop music fadeout 2.0
    "A light shake. Instead, Tomonori-san scrawled a note on a Post-it, wrapped it around the flash drive, and asked me to pocket it."

    tomonori "Reach me by phone when you're done. Only then you can confirm we're not making this up."
    tomonori "Whatever you do, share this to no one. Don't bother with the inspector -- he already owns a copy."
    show hiroshi casual boredclosed at Three3 with Dissolve(0.2)
    hk7 "But please, know that I am accepting this on one condition. Whatever conclusion I reach from the contents of this device, I will stand by it until further evidence is produced."
    tomonori "As you wish, Hiroshi."

    play sound sfx_dooropen
    show hiroshi casual bored at Three3 with Dissolve(0.2)
    "The door opened.{w} Mrs. Shinozaki entered the room, acknowledging my presence. She set her large shoulder bag down at the bed's foot. It contained toiletries and some extra clothes, presumably for Inoue."
    "Inoue and her mother enjoyed the apples I brought while discussing some petty affairs.{w} She looked better than she was a while ago, back to the familiar vibe I've known her since."

    show inoue casual smile at Three1 with Dissolve(0.2)
    is4 "Hey, you should drop by more often. Though, I think I won't be staying here for long. Who knows?{w} How are things back in MSCI?"
    show hiroshi casual smileteeth at Three3 with Dissolve(0.2)
    hk7 "I'm the newly-appointed head of the Science Club. No need to celebrate nor congratulate me. Hahahaha!{w} And... Miyu's been performing his duties well as your substitute."
    show inoue casual determined at Three1 with Dissolve(0.2)
    is4 "Knew that guy had it from the beginning. I should make it up to him once I'm out of here. A sense of gratitude or a small token will do."
    show inoue casual smile2 at Three1 with Dissolve(0.2)
    is4 "And I wish you all the best. May things not go awry next week."
    show hiroshi casual smirk at Three3 with Dissolve(0.2)
    hk7 "Yes. Yes. Thing must {i}not{/i} go awry..."
    show inoue casual smile at Three1 with Dissolve(0.2)
    is4 "I'll be seeing all of you, then? Give my regards to Ms. Harada in case she might not drop by any time soon."
    show hiroshi casual smileteeth at Three3 with Dissolve(0.2)
    hk7 "Maybe? Haha! Of course you will!"
    hide hiroshi with Dissolve(0.2)
    hide inoue with Dissolve(0.2)

    window show
    nvl clear
    scene bg hospitalcorridor with dissolve
    narr "I bid them farewell at three, exchanging handshakes with everyone sans Inoue -- she preferred a fist bump.{w} Along the way, I encountered Dr. Shinozaki. He stopped to share some last words before parting ways."
    scene bg receptiondesk with dissolve
    narr "The sweet nurse is still there, albeit alone this time. She deserves my thanks.{w} Strangely enough, the ride down felt much lighter, erasing the negativity it gave off initially."
    scene bg park with dissolve
    play sound sfx_chirp loop
    narr "Out the front lobby and into the heat outside, I activated my umbrella.{w} Breezy air, but the sunlight's intensity is enough heat stroke upon an unlucky bum."

    window hide
    scene bg bedroom with fade
    window show
    nvl clear
    narr "The rest of the afternoon felt happier, applying a fluid motion to my thoughts.{w} It was close to Nirvana, if not the concept itself. How I value the sound of silence whenever I'm alone in the house."
    narr "I sat at my desk, examining the items I received from Tomonori-san. Unwrapped from the paper, with his cellphone number, is the flash drive.{w} I took a moment to collect my thoughts while there was still silence."
    stop sound
    narr "What soon followed is dusk... a subversion of the afternoon's story.{w} {cps=15}This oncoming eclipse... why does it not ease me as it's supposed to do?{/cps}"
    narr "Nevertheless, I readied the family desktop, device in hand."

    nvl clear
    window hide

    scene black with fade
    centered "{cps=10}The upliftment was a lie...{w=1.0} Things must {i}not{/i} go awry...{/cps}"
    return

label ch02_07_security:
    scene bg msci with fade
    play sound sfx_chirp loop
    "JULY 8, 2013 - 0630H"

    window show
    nvl clear
    narr "All the set pieces are in place."
    window hide
    scene bg school hallway with dissolve
    show sayo blankface at Three2 with Dissolve(0.2)
    window show
    narr "Sayo has left IV-E early to prepare for the flag ceremony, joining the rest of the Council on the second floor."
    scene bg classroom1 with dissolve
    narr "An endless stream of students dashed through the gate and into their classrooms, hoping to settle down before the bell rang.{w} There were at most three activities seen in every classroom: general cleaning, homework cramming, and, for the happy few, sleeping."
    stop sound

    play sound sfx_schoolbell
    scene bg msci with dissolve
    nvl clear
    narr "At precisely 6:30, the bell rang."
    play sound sfx_crowdtalking loop
    narr "The class presidents rounded up their respective classes and formed a line on their designated spots.{w} Just as how colorful each level is when they are all wearing their PE uniforms, the same can be said for each officer. Some are benevolent, others stoic and drill sergeant-like."
    narr "But the extremes are unmatched with the clouds preluding an oncoming rainfall by mid-morning. Truly, the heavens weep with the mortals; rather, it is about to."
    narr "At 6:40, the Council's Vice President appeared on the balcony, commanding the students to settle down."
    stop sound fadeout 1.0
    narr "And within a minute, they followed."

    nvl clear
    narr "First up, the National Anthem. The beat was conducted by the secretary while the Boy Scouts raised the country flag.{w} Sayo Ronoroa led the opening prayer, the Pledge of Allegiance to the Flag, and the Patriotic Oath."
    narr "Three more songs followed, the beat conducted by the Vice President save for the last: the Hymn of Department of Education - Kutsutochi, Kutsutochi's Hymn, and their school song, \"Pride of the Land, Eternal Glimmer.\" This was conducted by Sayo."

    nvl clear
    narr "A new sheet of silence covered the quadrangle."
    narr "The principal, Mrs. Sokoguchi, welcomed the students on their sixth week in MSCI.{w} She gave a few remarks about the previous week and made a few small announcements afterwards."

    nvl clear
    window hide

    prin "With that done, I would like to mention that we have a special guest joining us this afternoon."

    play sound sfx_crowdtalking
    "The student body cooed, heads turning and tongues whispering about who it could be."
    stop sound fadeout 2.0

    prin "Few of you, especially the Seniors, must have glimpsed upon our guest the previous month.{w} I would like to apologize for any potential trigger, but he is the lead investigator of the Kyou Kirisaki murder case."

    "Silence.{w} This time, it felt darker.{w} How insensitive could that remark be?"

    prin "My apologies once again, but he gave his time for you to make an important announcement, especially those who inquire us of our own safety. Ladies and gentlemen, Inspector Harold Emmerich."

    play sound sfx_applause
    "A thunderous applause welcomed Emmerich, maintaining his composure throughout his introduction. Not as bad as the girls thought -- a rather handsome young man."
    stop sound

    play sound sfx_crowdtalking2
    scene bg school hallway with dissolve
    show emmerich serious at Three2 with Dissolve(0.2)
    student "Is he married? Is he already taken? Boy! He's dreamy!"

    show emmerich seriousclosed at Three2 with Dissolve(0.2)
    stop sound fadeout 2.0
    "Emmerich cleared his throat and began his speech."

    show emmerich smile at Three2 with Dissolve(0.2)
    p_emm "Good morning, and I appreciate the compliment. Actually became the class escort twice in my days. {i}*chuckle*{/i} If there are any other compliments or insults, let us attend to those later, but for now, I have to discuss an important matter with you."
    show emmerich worried at Three2 with Dissolve(0.2)
    p_emm "I would like to apologize for reminding everyone of the recent tragedy, inasmuch as we're throwing everything we can to end this case before anyone else is involved. And the weather seems to agree with me."
    show emmerich talk at Three2 with Dissolve(0.2)
    p_emm "You may have been imposed upon a curfew for the past few weeks -- it's for our own goodwill."
    show emmerich smile at Three2 with Dissolve(0.2)
    p_emm "You may have been imposed upon a curfew for the past few weeks -- it's for our own goodwill.{fast} What I bring today is relief, not burden.{w} Ms. Sayo, would you please pass me the...{w=1.0}{nw}"
    show sayo smileopen at Eight6 with Dissolve(0.5)
    hide sayo with Dissolve(0.2)
    p_emm "Thank you."

    "He possessed a small remote control, pressing one of the buttons on its face."
    play sound sfx_beep2
    "{b}*BEEP*{/b}"
    "Around the campus perimeter, various spots of red glimmered. They divided the attention of the students, each wondering what these were for."

    show emmerich talk at Three2 with Dissolve(0.2)
    p_emm "The police and school officials came up with a contingency plan the previous week. Over the weekend, we installed various CCTV cameras on key locations around the campus, wired to the school security system."
    p_emm "The cameras are linked to our station, as well as the front desk guard station and the offices. They are active 24/7, with an emergency generator in case of a power interruption."
    p_emm "Don't bother trying to trick the system.{w} We gave strict orders to impose penalties upon those who are caught tampering with the devices. But I trust you guys wouldn't go that low, would you -- the cream of the crop of Kutsutochi?"

    play sound sfx_crowdtalking2
    "The students gave an affirmative response in a loud chorus."
    stop sound

    show emmerich serious at Three2 with Dissolve(0.2)
    p_emm "Now, on to my second point.{w} My senior and I agreed not to disclose details of the ongoing case, but we have decided to make an exception. Keep this among yourselves or your family, please. We've had enough with the media's involvement."

    "The inspector walked to the sound board and lowered the volume. In turn, the students anticipated his next words in silence.{w} Ichirou, Sumiko, Ayumi, and the rest of the class presidents moved forward."

    show emmerich talk at Three2 with Dissolve(0.2)
    p_emm "{cps=15}The circumstances of the disappearances last month...{w=1.0} we suspect an inside job --{/cps}{nw}"
    show emmerich worried at Three2
    ys6 "I knew it!"

    play music bg_roadtohell loop
    play sound sfx_crowdtalking3
    "After hushing him and a few others who voiced their support of this theory, the rest of the students caused an uproar.{w} Efforts were made to quell them, but the fear and anger overshadowed the firm pleads of their leaders."
    "Mrs. Sokoguchi snatched the microphone from Emmerich."
    hide emmerich with Dissolve(0.2)

    stop sound
    prin "Silence!"

    scene bg msci with dissolve
    "And silence they returned."

    prin "I understand how you feel and why the recent developments sound improbable, but we {i}need{/i} to make sure.{w} We haven't identified a suspect yet as even circumstantial evidence is insufficient. For now, all of the students and staff are innocent."
    prin "Please compose yourselves and remember to show some decency next time. Thank you."

    scene bg school hallway with dissolve
    show emmerich worried at Three2 with Dissolve(0.2)
    "Heads were hung in shame, and the inspector sympathized with them. He took the center stage once again."

    p_emm "My sincerest apologies... {i}*sigh*{/i} My senior was right to see this coming.{w} But, as our principal mentioned, we have zero persons of interest. There are suspicions but stay as suspicions."
    stop music fadeout 2.0

    "Probably like animals tamed with their tails between their legs, the students remained silent. A thousand pairs of eyes eerily stared towards him."

    show emmerich smile at Three2 with Dissolve(0.2)
    p_emm "{cps=15}Since I have nothing further to add, I... hope you all have a pleasant day.{/cps} I should be going now -- I'll entertain some questions later when we meet.{w} Thank you for your time."

    play sound sfx_applause
    hide emmerich with Dissolve(0.5)
    "He received another round of applause, albeit of lower intensity than before. He shook the Council members' hands and talked to Mrs. Sokoguchi for the moment."
    show sayo blankface at Three2 with Dissolve(0.2)
    "Sayo stepped forward, giving the final announcements of the morning."

    show sayo normaltalkleft at Three2 with Dissolve(0.2)
    sr5 "Let the officers of the following stay behind and meet us in the council room: Science Club, Mathematics Club, and English Club."
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "Let the officers of the following stay behind and meet us in the council room: Science Club, Mathematics Club, and English Club.{fast} The rest, you may go to your respective classrooms. Have a pleasant day."
    hide sayo with Dissolve(0.2)

    window show
    nvl clear
    narr "Hiroshi, Miyu, Ayumi, and their fellow officers deviated from the crowd and congregated at the central staircase.{w} A few moments later, Emmerich and Mrs. Sokoguchi descended from the staircase. The former exchanged handshakes with them."
    narr "Sayo fixed her blouse, appeared from the staircase and led the party to the conference room."

    window hide
    play music bg_thecomplex loop
    scene bg conferenceroom with fade
    show sayo smileopen at Three2 with Dissolve(0.2)
    show miyu smile at Eight3 with Dissolve(0.2)
    show ayumi serious at Eight6 with Dissolve(0.2)
    show hiroshi bored at Eight7 with Dissolve(0.2)
    window show
    nvl clear
    narr "She gave the officers handouts -- the program flow for the whole week.{w} Gathered at one side are two-hundred bundles of reviewers covered in plastic, waiting to be distributed later."
    narr "Other than that, there were no changes to the office -- no red dot or electronic devices mounted on the walls."
    narr "They gathered around the conference table. Sayo preceded the brief meeting."

    nvl clear
    window hide

    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "You all ready?"

    show miyu naughty smile at Eight3 with Dissolve(0.2)
    show ayumi smile at Eight6 with Dissolve(0.2)
    show hiroshi determined at Eight7 with Dissolve(0.2)
    "Though her smile forced, the officers responded cheerfully. It brightened their morning even if just a bit."

    show ayumi serious at Eight6 with Dissolve(0.2)
    show sayo normaltalk at Three2 with Dissolve(0.2)
    sr5 "Let us start. I have given you a timeline of events. Please, have at least one copy for each club. How you will conduct and what you will discuss during each session is up to you. Just keep our fellow Seniors in mind, alright?"
    show hiroshi boredtalk at Eight7 with Dissolve(0.2)
    hk7 "If I may, I have a request."
    show sayo blankface at Three2 with Dissolve(0.2)
    sr5 "Proceed, Hiroshi."
    show hiroshi worried at Eight7 with Dissolve(0.2)
    hk7 "We feel it would be unfair for the students if we cram all the topics of Science in one week.{w} May we have an extra week, or at least, extra sessions to accommodate that?"
    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "I must agree. And am I right to assume the other clubs are requesting the same? Miyu? Ayumi?"
    show miyu smiletalk at Eight3 with Dissolve(0.2)
    mh8 "I second the motion. Reinforcement is necessary especially since we do not want ourselves to burn out if we rush things."
    show ayumi happy at Eight6 with Dissolve(0.2)
    ayumi "We feel the same, especially if the extra week is for our own goodwill."
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "Carried. We shall arrange the schedule for the second set with teachers later. Any other concerns?"

    show sayo normaltalkleft at Three2 with Dissolve(0.5)
    show sayo normaltalk at Three2 with Dissolve(0.5)
    show ayumi seriousclosed at Eight6 with Dissolve(0.2)
    show miyu confused at Eight3 with Dissolve(0.2)
    show hiroshi worriedleft at Eight7 with Dissolve(0.2)
    "All heads shook at her inquiry."

    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "None?{w} I wish you all the best, and strive for the better! Your excuse letters are already with your respective teachers so you can conduct your activities without worry."
    show sayo worriedtalk at Three2 with Dissolve(0.2)
    sr5 "Keep in mind that you do {i}not{/i} and must {i}not{/i} preempt your non-major subjects for a session.{w} Only exception, if it is requested by the teacher."
    show sayo smileopen2 at Three2 with Dissolve(0.2)
    sr5 "Meeting adjourned. Godspeed!"
    stop music fadeout 2.0

    play sound sfx_dooropen
    hide hiroshi with Dissolve(0.1)
    hide ayumi with Dissolve(0.1)
    hide miyu with Dissolve(0.1)
    show sayo seriousserious at Three3 with Dissolve(0.5)
    "Thus, like sheep, they set out to fulfill their duties.{w} Sayo stayed behind, arranging some papers before heading to class, going back and forth between the conference room and the office."
    show sayo seriousnormalleft at Three3 with Dissolve(0.5)
    show sayo seriousnormal at Three3 with Dissolve(0.5)
    "Her eyes darted around the room, trying to think of something she forgotten. She dismissed it and returned to work."

    show sayo smileclosed at Three3 with Dissolve(0.2)
    sr5 "The brain is confused at sunrise, and stays the same at sunset...{w=1.0} Probably not. {i}*giggle*{/i}{w} What am I even thinking? Too early in the morning for entertaining weird thoughts."

    show sayo smileopen at Three1 with Dissolve(0.2)
    "She finished her errand and took one final scan of the room."

    show sayo smiletalk at Three1 with Dissolve(0.2)
    sr5 "God is watching us. He'll be our camera even in darkness."

    play sound sfx_dooropen
    scene black with fade
    "She made a cross and left the room."
    return

label ch02_08_review1:
    scene black with fade
    call ch02_08A_phonecall from _call_ch02_08A_phonecall

    return

label ch02_08A_phonecall:
    play sound sfx_rain loop
    scene bg msci rain with fade
    "{color=#bd0000}\[Day 2\]{/color}\nJULY 9, 2013 - 1130H"

    scene bg conferenceroom with dissolve
    show sayo seriousserious at Three3 with Dissolve(0.2)
    window show
    nvl clear
    narr "At around lunch time, as usual, Sayo made a quick stop to the council room to attend to some reports sent there for the day."
    narr "The green light on her phone desk blinked, and the LED screen showed one new voice message.{w} She started the recording, and her own sweet and mellow voice spoke the first sentences."

    stop sound fadeout 1.0
    show sayo seriousnormalleft at Three3 with Dissolve(0.2)
    nvl clear
    narr "{i}Good day. Student Council President here.{w=1.0} While I understand this may be of utmost importance, I am not able to attend to this as of present.{w=1.0} Please leave a message after the beep.{/i}{w=1.0}{nw}"
    play sound sfx_beep4
    narr "{i}{b}*BEEEEEEEEEEEEEEP*{/b}{/i}{w=1.0}{nw}"
    narr "{i}Good morning, Sayo. Inspector Harold Emmerich speaking.{w=1.0} Pardon the sudden call, but there seems to be a matter of concern regarding the current state of investigation.{w=1.0} As soon as you receive this message, please contact me immediately.{w=1.0} Thank you.{/i}"

    show sayo worried at Three3 with Dissolve(0.2)
    nvl clear
    narr "Sayo shook her head, expecting to have her lunch be cut into half once again.{w} But if it would help resolve Kyou's murder, then why remain silent?"
    narr "She input the numbers to the Regional Police, and after a few moments, a desk sergeant answered from the other end."

    nvl clear
    window hide

    officer "Capital Region Police District. How may I help you?"
    show sayo worriedtalk at Three3 with Dissolve(0.2)
    sr5 "Good morning, officer. This is Sayo Ronoroa from Maria St. Claire Institute.{w} I happen to have an on-the-phone appointment with Inspector Harold Emmerich. Could you please fetch him for me?"
    officer "Yes, Ms. Sayo. He did mention your name. I'll pass the line to his office immediately."
    show sayo worried at Three3 with Dissolve(0.2)
    sr5 "Thank you, officer."

    show sayo seriousclosed at Three2 with Dissolve(0.5)
    "While waiting, Sayo sat back on her chair, took a deep breath, and rested her eyes."

    p_emm "Hello, Sayo."
    show sayo happytalk at Three2 with Dissolve(0.2)
    sr5 "Inspector Emmerich! I suppose you have taken your meal for the afternoon, eh? Hahahahahaha."
    p_emm "That will have to wait after this conversation.{w} There are just a few things I need to clarify regarding the phone call last June 13. Do you mind if I record this conversation as your testimony?"
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "That will be no problem."
    p_emm "Thank you.{w=1.0}{nw}"
    p_emm "{i}This is Inspector Harold Emmerich. Timestamp: 9th of July, 2013 at approximately 1135H. Currently interviewing a witness named Sayo Ronoroa, Case File Code MH-0810.{/i}"
    p_emm "We may begin."
    play music bg_awkwardmeeting loop
    show sayo blankface at Three2 with Dissolve(0.2)
    sr5 "Before we do so, I must say there are far too many points to discuss. Could you please specify what this is about?"
    p_emm "Certainly. I won't take long.{w} You are aware that you've contacted the Shinozaki residence on the evening of June 13, and that you've spoken with Ms. Inoue Shinozaki?"
    show sayo normaltalkleft at Three2 with Dissolve(0.2)
    sr5 "That is true. I did have a conversation with Inoue. If I recall, she looked unusually spooked the following day, probably from what transpired in that conversation."
    p_emm "Spooked? What did you talk about, if you don't mind the intrusion?"

    show sayo seriousclosed at Three2 with Dissolve(0.2)
    "Sayo tapped her finger on the desk, rotating the chair to shorten the wire's length. After pondering for a moment, she continued."

    show sayo seriousnormalleft at Three2 with Dissolve(0.2)
    sr5 "Allow me to give some background on what I am about to say."
    show sayo serioustalkleft at Three2 with Dissolve(0.2)
    sr5 "Ten of us, {i}(lists names){/i}, gathered in front of the auditorium to bond -- play games and share stories since it was our last year in high school. I was only invited by our auditor, Akira, since it was arranged by Ichirou."
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "I forgot to take my music book with me after the First Friday Mass. I couldn't just go back because the auditorium was already plunged into darkness. Luckily, Miyu volunteered to search for it. Gallant and kind-hearted child, I must say."
    show sayo serioustalk at Three2 with Dissolve(0.2)
    sr5 "We divulged into campfire stories, eventually leading to real discussions about the supernatural -- the case of Ikari Suzumoto, and eventually, the Sacred Heart Curse Killings."
    show sayo serioustalk2 at Three2 with Dissolve(0.2)
    sr5 "As soon as Miyu came back and returned my music book, we all went home. I remember Inoue looking forlorn so I asked her about it. She said she was curious to learn the details of the case since...{w=1.0}{nw}"
    show sayo seriousnormal at Three2 with Dissolve(0.2)
    sr5 "As soon as Miyu came back and returned my music book, we all went home. I remember Inoue looking forlorn so I asked her about it. She said she was curious to learn the details of the case since...{fast} I'm not sure myself."
    p_emm "I'm sure she was. I remember it too well..."
    show sayo worried at Three2 with Dissolve(0.2)
    sr5 "Inspector? Is something the matter?"
    p_emm "So, you approached her, and...?"
    show sayo worriedtalk at Three2 with Dissolve(0.2)
    sr5 "I told her to take her mind off of it. It only occurred to me later on that we were the same number as the Sacred Heart victims. Inoue initiated a count-off just before Miyu returned."
    show sayo worried at Three2 with Dissolve(0.2)
    sr5 "Since we were former classmates, I decided to give her a helping hand just like before. I promised to research about the case and relay my findings as soon as I organized my notes."
    p_emm "Why didn't she do it herself? The information is already available on the internet."
    show sayo seriousclosed at Three2 with Dissolve(0.2)
    sr5 "Let's just say I have connections, Inspector. I have a better chance of gaining rare information through special means -- the psychology of the crimes, as some would put it. It's my specialty."
    p_emm "I understand. At least one point is cleared up."

    play sound sfx_ticktock loop
    "Sayo glanced at the clock. The minute hand was nearing the 45-minute mark."

    show sayo normaltalkleft at Three2 with Dissolve(0.2)
    sr5 "How is she doing, Inspector? I haven't had a chance to visit Inoue ever since she was rescued."
    stop sound fadeout 1.0
    stop music fadeout 2.0
    p_emm "Hmmmmmmmmm..."
    show sayo seriousnormalleft at Three2 with Dissolve(0.2)
    p_emm "How should I say this?"

    scene black with fade
    centered "{cps=30}{i}Let me guess... I have heard that momentary silence too many times in movies and in television.{w=1.0}\nWhat are those instances?{w=1.0}\nIs she in the ICU, going 50/50?{w=1.0}\nDid she disappear from the hospital and was already missing for a few days without us knowing?{w=1.0}\nDid I do anything to upset her?{w=1.5}\n{/cps}{/i}{i}Oh, of course!{w=1.0} I know exactly why...{/i}"

    scene bg conferenceroom with fade
    play sound sfx_ticktock loop
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "I suppose I should wait for her to come back physically in MSCI, then. I'd love to sit down and chat with her."
    p_emm "Very good, Sayo. I think the same."
    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "You know, should you have the time to visit her once again, could you check if she received the modules we sent her?"
    p_emm "She was reading her lessons the last time I visited her. No need to worry, Sayo."
    show sayo normaltalk at Three2 with Dissolve(0.2)
    sr5 "Greeting card? Did she get any?"
    p_emm "Not sure, but one of your friends did pay her a visit. Know anyone named...{w=1.0} uh..."
    show sayo blankface at Three2 with Dissolve(0.2)
    sr5 "Hiroshi Kano."
    p_emm "Yeah, Hiroshi!{w} He even brought her a fruit basket. How'd you know?"
    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "Our good auditor told me. He and Hiroshi are close friends, too, you know."
    p_emm "I see.{w=1.0} Anyway, I'll end the recording now.{w} I think you still need to eat, Sayo. Sorry for bothering you on such a busy day."
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "No, no. As long as I know you're doing this for the truth, that will be enough for me.{w} I, too, am searching for the answers my own way{w=1.0} -- the legal way."
    stop sound fadeout 1.0
    p_emm "I expected no less from an MSCI student.{w} I will look forward to hearing from you again soon. Who knows, we might even have a discussion on our findings should you ever pursue an independent investigation."
    p_emm "Rest assured, we will be one step closer to solving Inoue and Kyou's abduction, as well as to bring justice to the latter's murder.{w} Thank you for your cooperation, Sayo."

    play sound sfx_hangup
    show sayo worried at Three2 with Dissolve(0.2)
    "The line cut, Sayo placed the receiver down.{w} Instead of returning to her paperworks, she gathered them into a folder and placed them inside the drawer."
    stop sound
    play sound sfx_ticktock
    "She stared at the clock in deep thought, watching it tick down as the minute hand approached twelve."

    sr5 "What wrong have I done against her?{w} Ever since that incident, never a night passed without that question emerging from the depths of my mind."
    sr5 "If I seek my answers now, it might only worsen the situation. Imagine what can spark from a flame that no one but the two of us can see."

    play sound sfx_rain loop
    hide sayo with Dissolve(0.2)
    scene bg msci rain with fade
    "When the minute hand struck twelve, Sayo rose from her seat and walked towards the canteen.{w} She slowed her pace after two classrooms and looked behind towards the school gate."

    sr5 "Was it a grave mistake after all?"
    stop sound fadeout 1.0
    return

label ch02_09_facts3:
    scene black with fade
    "{color=#bd0000}\[Day 3\]{/color}\nJULY 10, 2013 - 1300H"

    scene bg monitorroom with fade
    window show
    nvl clear
    narr "The entirety of one side of the room was filled with images of the campus.{w} Only one officer was assigned to watch the live feed until the end of his shift at 6 PM."
    show emmerich serious at Three3 with Dissolve(0.2)
    narr "Emmerich accompanied him.{w} He tucked himself into a corner with his laptop -- a sound recording application open -- and headphones fully covering his ears. He was comparing the voices from the recording Tomonori gave him and his recorded phone conversation with Sayo."
    narr "The contours were similar, as he suspected, in accordance to similarity in pitch and tone by Inoue's testimony.{w} Supported by her brother's statement, Emmerich came to one conclusion."

    nvl clear
    window hide

    show emmerich smile2 at Three3 with Dissolve(0.2)
    p_emm "You know, in my days as a crime lab assistant, I have examined several voice clips myself.{w} The voice -- aside from Ms. Shinozaki's -- is unmistakably Ms. Ronoroa's."
    officer "And that makes her a suspect? Don't you follow rules regarding the use of voice clips as evidence?"
    show emmerich serious at Three3 with Dissolve(0.2)
    p_emm "Of course, we can't discount her, even though she openly admitted that voice was hers. Still, as they aren't as solid as videos and photographs, these clips have their flaws.{w} There is one more question we must ask."
    officer "And that is?"
    show emmerich seriousclosed at Three3 with Dissolve(0.2)
    p_emm "Is there anyone who can replicate such a voice?{w} I'm not saying she's hiding something by the way she testified on the phone, but let's consider the improbable."
    p_emm "I say Ms. Ronoroa's voice belong to a thousand other people. Far-fetched if you consider our current pool of suspects, but is yet to be proven impossible."

    "Unsure about his response, Emmerich's companion returned a puzzled look.{w} Whether his theory is serious enough is another question entirely."

    show emmerich smirk at Three3 with Dissolve(0.2)
    p_emm "Put it this way. By \"replicate,\" I meant having essentially a similar voice as hers. If I am right about what your face is telling me, perhaps such a theory is indeed impossible."
    show emmerich smirk2 at Three3 with Dissolve(0.2)
    p_emm "Who knows, it might have been a naughty jester's ploy all along. And the abduction case that soon followed we only thought connected just because they involve a common person -- Inoue Shinozaki."
    officer "I don't know, Harold. Can't find anyone else in the force who would have a theory wilder than yours."

    play sound sfx_dooropen
    show emmerich normal at Three2 with Dissolve(0.2)
    window show
    nvl clear
    narr "At that moment, the office door opened.{w} The two officers turned their heads to look, and gave Sergeant Deitch a salute once they saw it was him."
    show emmerich focusedleft at Three2 with Dissolve(0.2)
    narr "In his possession is a brown envelope, containing reports related to the current case.{w} He handed it to Emmerich and pulled a vacant chair towards him."

    nvl clear
    window hide

    p_dei "You know, my boy, I don't think my time is up yet."
    show emmerich smile at Three2 with Dissolve(0.2)
    p_emm "Maybe the Higher Powers bid you to accompany your protégé for one last journey."
    p_dei "Seems to be.{w} This and MH-0809...{w=1.0} {i}*sigh*{/i} God, please let MSCI not be another guinea pig playground of a psychopath."
    show emmerich determined at Three2 with Dissolve(0.2)
    p_emm "We have until the end of the month to see if your prayer will be answered. I vote for reclassifying the case after the deadline has passed."

    "Emmerich studied the documents he was given, and his superior took cursory glances at the monitors."
    hide emmerich with Dissolve(0.2)

    play sound sfx_pageturn
    play music bg_decisions loop
    scene bg brownenvelope with fade
    window show
    nvl clear
    narr "It was Kyou's initial autopsy report, examined by the coroner the night before his wake.{w} Emmerich skimmed the paper a few times, cross-checking the information written in the document and those from his personally-collected evidence."
    narr "Emmerich summarized the report in his notebook."

    nvl clear
    narr "{i}Kyou Kirisaki -- Aged 16 at time of death\nDate: 27th of June, 2013{/i}"
    narr "{i}Cause of death: Third-degree burns to external and internal organs of the body\nEstimated time of death: 0100-0500H; body already undergoing rigor mortis by the time of discovery{/i}"
    narr "{i}The patient has suffered light blunt trauma on the cranium, most likely glassware; small particles of glass buried within the scalp{/i}"
    narr "{i}Additionally, there are traces of unidentified chemicals on most of the patient's head. Stomach contents nearly empty; low nutrition for at least a week before death. Extracted from his bloodstream an alcohol-like substance.\nAnalysis incomplete -- chemical structure volatile{/i}"

    nvl clear
    window hide

    scene bg monitorroom with fade
    show emmerich focusedleft at Three2 with Dissolve(0.2)
    "Deitch glanced over to Emmerich's notebook. He only shook his head."

    p_dei "Leave nothing potentially important, Harold."
    show emmerich normaltalk at Three2 with Dissolve(0.2)
    p_emm "I've already skimmed through the report three times, sir. I can always refer to this at any time."
    p_dei "Certainly, you should; that is, until the final report is out after a few more weeks."
    show emmerich serious at Three2 with Dissolve(0.2)
    p_emm "Understood."
    p_dei "I've been thinking. If you could wrap this up before Christmas, then perhaps I made the right decision after all."
    show emmerich worried at Three2 with Dissolve(0.2)
    p_emm "You are far from your retirement, Sarge. Mid-50s I'd hardly call a retirement age range.{w} Why don't you serve the force for a few more years?"
    p_dei "Young ones understand most of the world we're living in the present, while we, the old-timers, are already well beyond our prime. Now, it's only us against Father Time."

    stop music fadeout 2.0
    show emmerich serious at Three2 with Dissolve(0.2)
    "From his pocket, he produced a cigarette stick and a lighter.{w} Emmerich and his companion silently protested, though they were used to the sergeant's smoking habits within the precinct rooms."

    play music bg_decline loop
    p_dei "I wonder{w=1.0} if all will be the same, after all?"
    show emmerich worriedclosed at Three2 with Dissolve(0.2)
    p_emm "If it is inevitable, then there is nothing I can do."
    show emmerich determined at Three2 with Dissolve(0.2)
    p_emm "If it is inevitable, then there is nothing I can do.{fast} But sir, come what may, I shall personally see this case to a close... even if it takes me a decade!"
    p_dei "{i}*chuckle*{/i} You speak big words, my boy. Why don't you surprise me more just like how you convinced me to uptake you as my successor?"
    p_dei "You think this is already at the middlegame, but trust me Harold, we are still at the opening. And I'm sure our finicky cat would agree."
    officer "Me, Sarge?"
    show emmerich smirkleft at Three2 with Dissolve(0.2)
    p_dei "No, of course not you, donut-boy!{w=1.0} Our bait, the snitch!{w=1.0} He goes by...{w=1.0} whochamacallit?"
    show emmerich normaltalk at Three2 with Dissolve(0.2)
    p_emm "Alias L.C., whatever it means."
    p_dei "Yes. Yes. L.C...{w} We searched through the records of every community here in Kutsutochi. There are several names here and there with those initials, but we ended up finding one of two things."
    show emmerich serious2 at Three2 with Dissolve(0.2)
    p_emm "Either the person of interest is deceased or out of town."
    p_dei "I'm not sure about the \"out of town\" part, Harold. Although, you are correct.{w} Guess it's another dead end for now."
    show emmerich serious2left at Three2 with Dissolve(0.2)
    p_emm "Or not."

    "The sergeant looked at Emmerich inquiringly.{w} Deitch nodded as he saw Emmerich's laptop screen."

    show emmerich talk at Three2 with Dissolve(0.2)
    p_emm "If we could find the truth from Ms. Ronoroa and Ms. Shinozaki's friends regarding this, then we may have another string to follow."
    show emmerich serious2left at Three2 with Dissolve(0.2)
    p_emm "Who really is this L.C. that Ms. Shinozaki described? What are their plans and motives?"
    p_dei "Questions and more damn questions that keep popping up by the day. It looks like she's starting to rub off on you. How is she, anyway?"
    show emmerich seriousclosed at Three2 with Dissolve(0.2)
    p_emm "She needs time to recuperate after that grand emotional drain. Looks like it's just you and me for now, sir."
    p_dei "I guess I'll hang around the spectators' seats, my boy. Perhaps it's my age speaking, but I still can't wrap my head around the opportunity."
    p_dei "How were they whisked out of the campus on a school morning? I think it's better if you answer that first before anything."
    p_dei "And if you can't do it yourself, I wonder how close you'll arrive at the answer before you require assistance?"
    show emmerich determinedclosed at Three2 with Dissolve(0.2)
    p_emm "How close, indeed...?"
    stop music fadeout 2.0
    return

label ch02_10_review2:
    scene black with fade
    call ch02_10A_preparations from _call_ch02_10A_preparations

    return

label ch02_10A_preparations:
    scene bg msci evening with fade
    play music bg_calmertimes loop
    "{color=#bd0000}\[Day 5\]{/color}\nJULY 12, 2013 - 1645H"

    window show
    nvl clear
    narr "Immediately after the Club and Organization Day activities ended, the students, save for a select few, headed straight home.{w} Sayo, leaving IV-E to its class president, Ayumi, headed to the council room to prepare for a meeting."
    scene bg conferenceroom with dissolve
    show sayo seriousnormal at Eight4 with Dissolve(0.2)
    show akira smile2 at Eight7 with Dissolve(0.2)
    narr "Once inside, Sayo (and Akira, who joined her a bit later), prepared the conference room.{w} Akira moved the whiteboard behind her seat and prepared a few markers and erasers."

    nvl clear
    show sayo seriousnormal at Three2 with Dissolve(0.2)
    show akira proud at Eight1 with Dissolve(0.2)
    narr "Within the next fifteen minutes, the Student Council officers took their designated places."
    show sayo seriousnormalleft at Eight7 with Dissolve(0.2)
    hide akira with Dissolve(0.2)
    narr "The secretary prepared her notebook to record the minutes and Sayo wrote the bullet points of the evening's agenda."
    show sayo seriousnormalleft at Three2 with Dissolve(0.2)
    show sayo seriousnormal at Three2 with Dissolve(0.2)
    narr "At exactly 5:10 PM, every student required to attend the meeting -- including the club officers and assigned marshals -- was already present."
    stop music fadeout 2.0

    nvl clear
    window hide

    show sayo seriousserious at Three2 with Dissolve(0.2)
    sr5 "Let's see. All Student Council officers accounted for: Ronoroa, Yasuda, Tanaka, Dojima, Ichibana, Watanabe, Orihime, Onizuka."
    show sayo serioustalk2 at Three2 with Dissolve(0.2)
    show hiroshi bored at Eight6 with Dissolve(0.2)
    show sumiko angry at Eight7 with Dissolve(0.2)
    show yoshiro smile at Eight8 with Dissolve(0.2)
    sr5 "And the club officers with us today: Kano, Tokubei, and Suzuki from the Science Club;{w=2.0}{nw}"
    hide hiroshi with Dissolve(0.1)
    hide sumiko with Dissolve(0.1)
    hide yoshiro with Dissolve(0.1)

    show sayo serioustalkleft at Three2 with Dissolve(0.2)
    show miyu smile at Eight3 with Dissolve(0.2)
    show hikaru smile at Eight2 with Dissolve(0.2)
    sr5 "And the club officers with us today: Kano, Tokubei, and Suzuki from the Science Club;{fast} Hirano and Yamamoto from the Mathematics Club;{w=2.0}{nw}"
    hide miyu with Dissolve(0.1)
    hide hikaru with Dissolve(0.1)

    show sayo serioustalk at Three2 with Dissolve(0.2)
    show ayumi seriousleft at Eight6 with Dissolve(0.2)
    show ikuko smile at Eight7 with Dissolve(0.2)
    sr5 "And the club officers with us today: Kano, Tokubei, and Suzuki from the Science Club; Hirano and Yamamoto from the Mathematics Club;{fast} Nakashima and Mimori from the English Club.{w=2.0}{nw}"
    hide ayumi with Dissolve(0.1)
    hide ikuko with Dissolve(0.1)

    play music bg_greatminds loop
    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "Alright! A pleasant afternoon to all of you.{w=1.0} First, I would like to thank everyone for your time and dedication for the whole week. We can safely say the review sessions are successful."
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "I also acknowledge our teachers who, likewise, coordinated with the City Office to provide us with review materials.{w=1.0} Have you chosen your college yet?{w=1.0} I sure have."

    play sound sfx_applause
    "{b}*APPLAUSE*{/b}"
    stop sound fadeout 1.0

    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "Next, will the representatives of each club report on their progress for the week? If you have any suggestions, like those raised from our pre-event meeting, you may choose to raise them during your report or at the end."
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "Hiroshi, the Science Club first."

    show sayo smileopenpose at Three2 with Dissolve(0.1)
    show hiroshi bored at Three3 with Dissolve(0.2)
    show sumiko serious at Eight7 with Dissolve(0.2)
    hide sumiko with Dissolve(0.1)
    play sound sfx_pageturn
    "Hiroshi stood up and borrowed the notes from Sumiko."

    show hiroshi boredtalk at Three3 with Dissolve(0.2)
    hk7 "As a school for the sciences, we contacted MSCI alumni to assist us with the topics.{w} We asked them to describe the general situation on the Science parts of the various entrance exams."
    show sayo normaltalkpose at Three2 with Dissolve(0.2)
    show hiroshi bored at Three3 with Dissolve(0.1)
    sr5 "I take it you filtered those from the Big Four and those that are not?"
    show hiroshi boredtalk at Three3 with Dissolve(0.2)
    hk7 "Exactly.{w} Out of the fifty respondents we interviewed, Chemistry seems to be the common bottleneck and mostly varied of the natural science.{w=1.0} This is followed by Biology, General Science, and Physics by a wide margin."
    show sumiko surprised2 at Eight7 with Dissolve(0.2)
    st3 "Additionally, on the review proper, we focused mostly on Stoichiometry, as most of the test items involved that. Plus, there seems to be a problem, for the majority, with calculation."
    st3 "Of course, with the Mathematics Club, we discussed how would we review the students regarding word problems and any mathematical concepts some questions might entail."
    show sumiko seriousleft at Eight7 with Dissolve(0.2)
    st3 "But that we leave to Miyu's team. It's more on their area of expertise, I should say."
    show akira proudclosed at Eight2 with Dissolve(0.2)
    ai2 "Wrong possessive, Sumiko.{w=1.0} It's {i}his{/i}."

    show sayo smirkpose at Three2
    show hiroshi smile2 at Three3
    show sumiko smirkclosed at Eight7
    "The room burst into laughter, leaving Miyu red-faced."
    hide akira with Dissolve(0.1)
    hide sumiko with Dissolve(0.1)

    show sayo smileopenpose at Three2 with Dissolve(0.2)
    sr5 "Hiroshi, if you may continue, please."
    show hiroshi smile at Three3 with Dissolve(0.2)
    hk7 "Thanks, Sumiko.{w} Since Science is inarguably the largest area of the pie, we decided to split ourselves into three teams."
    hk7 "I'm the team leader for Biology, Yoshiro for General Science and Earth Science, and Sumiko for Chemistry and Physics because he's that awesome.{w=1.0}{cps=15}.. Not to downplay our contributions as a whole, of course.{/cps}"
    show hiroshi smileleft at Three3 with Dissolve(0.2)
    c_vp "I have a question. Do your teams still coordinate with each other in terms of crossing into other fields of Science?{w=1.0} Or, wait..."
    show sayo normaltalkleftpose at Three2 with Dissolve(0.2)
    sr5 "I've personally seen some of them handle areas even if they are not assigned to those teams, especially if no one is available. I don't see any problem with it."
    c_vp "Or better, since it was already obvious... {i}*chuckle*{/i} You've mentioned Stoichiometry as the primary focus of Chemistry.{w} What about the others -- Biology, Gen. Sci., Earth Sci. and Physics?"
    show sayo blankfacepose at Three2 with Dissolve(0.2)
    show hiroshi bored at Three3 with Dissolve(0.2)
    hk7 "For Biology, the bulk of the questions were on Physiology and Anatomy...{w=1.0} which I will be getting into now."
    show hiroshi boredleft at Three3 with Dissolve(0.2)
    hk7 "As everyone here has experienced how complex the processes involved in energy circulation are, we had to slow down our pace for the students to digest the explanations more easily. We also introduced mnemonics."
    hk7 "And for the rest, we asked the students to keep a copy of the handouts we gave. They contain bullet points from almost every topic in Biology.{w} We tried to cover as much ground as we can, but we didn't finish as expected."
    show sayo blankfaceclosedpose at Three2 with Dissolve(0.1)
    show sayo blankfacepose at Three2 with Dissolve(0.1)
    hide hiroshi with Dissolve(0.2)

    show yoshiro surprised2 at Three3 with Dissolve(0.2)
    ys6 "We did not do much on General Science.{w} However, our team covered the essential information the students need about the Earth's structure and the various phenomena occuring around it."
    ys6 "We touched a few concepts in Biology and Physics such as ecology, force, and the like. There was also a bit of Geology involved, but we only covered the essentials."
    show yoshiro surprised2 at Three3 with Dissolve(0.2)
    ys6 "That's it from me."
    show sayo blankfaceclosedpose at Three2 with Dissolve(0.1)
    show sayo blankfacepose at Three2 with Dissolve(0.1)
    hide yoshiro with Dissolve(0.2)

    show sumiko surprisedtalk at Three3 with Dissolve(0.2)
    st3 "The materials we were procured with covered Physics from end to end.{w} As such, we focused more on the applications and mathematics behind each major concept. I'd wager at most five questions per topic."
    show sumiko surprised2 at Three3 with Dissolve(0.2)
    show hiroshi boredtalk at Eight7 with Dissolve(0.2)
    hk7 "Though we admit,{w=1.0} even if we covered all the areas required for the entrance exams, it would be no use without constant reviewing and application."
    hk7 "In summary, we enforced the ideas behind each topic. None of us expect the students to have retained their stock knowledge after over three years."
    hide hiroshi with Dissolve(0.2)
    show sayo smileopenpose at Three2 with Dissolve(0.2)
    sr5 "Thank you, members of the Science Club.{w} I agree with your viewpoints and methods in handling your parts of these sessions.{w} The surveys made during the first three days showed favorable results."
    hide sumiko with Dissolve(0.2)

    show sayo normaltalkleftpose at Three2 with Dissolve(0.2)
    sr5 "Now, if there are no further questions, we shall move on to the Mathematics Club.{w} Miyu, please begin."
    show sayo blankfacepose at Three2 with Dissolve(0.2)
    show miyu naughty smile at Three1 with Dissolve(0.2)
    mh8 "I confirm Sumiko's statement earlier."
    show miyu focusedpose at Three1 with Dissolve(0.2)
    mh8 "The problem with most of the students in test-taking lies on two aspects: reading comprehension and fact-finding,{w=1.0} both of which are necessary for problem solving."
    mh8 "Likewise, we found Mathematics to be too large of a subject to merit each area equal attention."
    show miyu smile at Three1 with Dissolve(0.2)
    mh8 "We split our team into two.{w} I handled the parts involving Geometry and Trigonometry, while we \"imported\" Ichirou to focus on Algebra."
    stop music fadeout 2.0

    show sayo seriousnormalpose at Three2 with Dissolve(0.2)
    show sayo seriousnormalleftpose at Three2 with Dissolve(0.2)
    show miyu confused at Three1 with Dissolve(0.2)
    "This stirred up a discussion among the Student Council members. Sayo watched the other members calmly."

    c_4r "If I may raise an objection.{w} I thought it was already implied at best that the Science Club members were spread thinly among three teams."
    c_4r "Furthermore, may I remind everyone that Ichirou is the secretary of the Science Club?{w} Why would you not delegate Algebra to a member of your own club?"
    show miyu naughty focuspose at Three1 with Dissolve(0.2)
    show hikaru angry at Eight1 with Dissolve(0.2)
    hy10 "Onizuka, I think that question is directed at me.{w} Miyu assigned me as the lead handler for Algebra, if you noted my attendance at the pre-event meeting."
    show hikaru worried at Eight1 with Dissolve(0.2)
    hy10 "In reality, we couldn't find a good substitute for Inoue until the last minute. I actually didn't want the part since I thought I may not handle things well."
    show hikaru smile at Eight1 with Dissolve(0.2)
    hy10 "Instead, we sought Ichirou's help despite being in another club. With Hiroshi's approval, he replaced me from Day 2 onwards."
    c_4r "Hiroshi, can you confirm this?"
    show sayo seriousnormalpose at Three2 with Dissolve(0.2)
    show hiroshi boredtalk at Eight7 with Dissolve(0.2)
    hk7 "There was an agreement between our club and theirs to lend out Ichirou.{w} This is due to their lack of manpower and members willing to spearhead the sessions."
    hk7 "We understand the situation fully, mind you.{w} In a similar vein to Yoshiro substituting the late Kyou Kirisaki in Gen. Sci., Miyu asked for Inoue's substitute in handling Algebra."
    show hiroshi smile at Eight7 with Dissolve(0.2)
    hk7 "We possess an official document should you wish to view it.{w} Sayo and Tanaka should have a copy each."
    hide hiroshi with Dissolve(0.2)

    play sound sfx_pageturn
    "From the drawer, the secretary produced a signed agreement between the two parties involved.{w} He passed it around the table."

    show sayo normaltalkleftpose at Three2 with Dissolve(0.2)
    sr5 "Does that answer your question, Onizuka?"

    play music bg_greatminds loop
    "He nodded, satisfied with the document, and motioned Miyu to continue."

    show miyu naughty closepose at Three1 with Dissolve(0.2)
    mh8 "Now that we have dealt with these trivial matters, let us proceed with our findings."
    show miyu talk at Three1 with Dissolve(0.2)
    mh8 "We aimed for mastery of the topics -- formulas and conditions for each, and the mathematical basis of each problem."
    mh8 "Once the students mastered the problem-solving process, we would then focus on techniques and shortcuts.{w} We applied Singaporean Math to shorten their solving times."
    mh8 "We held surprise unit tests during Calculus and Analytic Geometry, courtesy of our teachers. As a precaution, we did not choose the questions, of course."
    show miyu smile at Three1 with Dissolve(0.2)
    mh8 "I don't think the students found Geometry troubling.{w} We already have the theorems memorized and derivations grasped, what with the rigorous proving we've done in Third Year."

    show sayo smirkpose at Three2 with Dissolve(0.2)
    "\"Hahahahahahahahahaha...\""

    show sayo blankfacepose at Three2 with Dissolve(0.2)
    sr5 "I see.{w} But who will give the report on Algebra on Ichirou's behalf?"
    hide miyu with Dissolve(0.2)

    show hikaru smile at Three1 with Dissolve(0.2)
    hy10 "That would be me.{w} I may have turned down the role, but I still stayed on his team."
    show sayo normaltalkleftpose at Three2 with Dissolve(0.2)
    sr5 "Give us a rundown, Hikaru."
    show sayo smileopenpose at Three2 with Dissolve(0.2)
    show hikaru angry at Three1 with Dissolve(0.2)
    hy10 "Like Miyu said, the students did not find Geometry that difficult.{w} Algebra is a different matter, however, as it relied more on word problems than figures."
    hy10 "On Ichirou's suggestion, we focused more on Intermediate Algebra and a bit of Precalculus.{w} The hows, whats, whys, and wheres -- closest description I can think of. Like Miyu, we focused on those aspects."
    show hikaru smile at Three1 with Dissolve(0.2)
    hy10 "Although, we factored in those who attended Saturday Math classes before.{w} They had a higher learning curve than average, so they helped us identify those who were struggling with Math."
    show hikaru smirk at Three1 with Dissolve(0.2)
    hy10 "Because, you know, not everyone is good with numbers and letters.{w} That's it from us."
    hide hikaru with Dissolve(0.2)

    show sayo smileopenpose at Three2 with Dissolve(0.2)
    sr5 "Thank you, Miyu and Hikaru.{w} Since Ichirou is, as you say, a team lead for your subject area, I shall speak with him tomorrow or Monday when we meet. Still, your report is sufficient, Hikaru."
    show sayo serioustalkpose at Three2 with Dissolve(0.2)
    sr5 "It's already twenty minutes to six -- ten minutes past the curfew.{w} Ayumi, how did the students fare on English?"
    show sayo seriousnormalpose at Three2 with Dissolve(0.2)
    show ayumi smile at Three3 with Dissolve(0.2)
    ayumi "Everyone has a good grasp of the subject, we must say, if the results we've got accurately represent their performance."
    ayumi "In addition to grammar and reading exercises, we also held five-minute writing exercises to test the students' articulation.{w} Its purpose is to prepare them for essays in case there would be any."
    show sayo seriousnormalleftpose at Three2 with Dissolve(0.2)
    show akira proud at Eight2 with Dissolve(0.2)
    ai2 "Let me guess...{w=1.0} You also split your handlers into teams?"
    show ayumi happy at Three3 with Dissolve(0.2)
    ayumi "Predictably."
    show akira proud2 at Eight2 with Dissolve(0.2)
    ai2 "You all seem to be into this \"splitting into two\" business. Is that an ongoing trend?"
    show ayumi smile at Three3 with Dissolve(0.2)
    ayumi "Why, yes! That's because one is never satisfactory enough nowadays, isn't it?"

    show sayo seriousclosedpose at Three2 with Dissolve(0.2)
    "\"Hahahahahahahahahahahahahaha!\""

    sr5 "Ahem."
    show akira fangblush at Eight2 with Dissolve(0.2)
    hide akira with Dissolve(0.1)
    show sayo seriousnormalpose at Three2 with Dissolve(0.2)
    show ayumi serious at Three3 with Dissolve(0.2)
    ayumi "So, I handled the grammar and writing sessions. Ikuko's team focused on reading comprehension."
    show ayumi seriousleft at Three3 with Dissolve(0.2)
    ayumi "There is nothing much to report aside from what I've said earlier.{w} We focused on repetition and enforcement of grammar rules, not unlike what our English teachers are doing."
    ayumi "We found those to be major contributing factors to the students' great performance on the subject."
    show ayumi seriousclosed at Three3 with Dissolve(0.2)

    show ikuko talk at Eight7 with Dissolve(0.2)
    ikuko "Though we wouldn't say the same for reading comprehension.{w} This is the basis of problem-solving as already mentioned a few times."
    ikuko "In general, the students are expected to collect and retain important facts from each passage to answer some of the basic questions.{w} Then, they collate them together to deduce a reasonable main idea and other inferences that can be made."
    show ikuko blank at Eight7 with Dissolve(0.2)
    ikuko "Unfortunately, recognizing connotations and metaphors are just half of the problem. What more if we ask them which theories apply and what themes are present for each text?"
    ikuko "Time is the greatest enemy of every student.{w=1.0} There were only a few who finished the sample exams when it came to our segment."
    ikuko "It was then we switched to the recommended approach: questions first before the text.{w=1.0} The students finished more quickly that way.{w} Then we asked ourselves, is there another way?"
    show ayumi serious at Three3 with Dissolve(0.2)
    ayumi "Thus, we decided to incorporate Mathematics and Science into our sessions through one means --{w=1.0} applying logic."
    stop music fadeout 2.0

    show sayo smileclosedpose at Three2 with Dissolve(0.2)
    sr5 "Why do you deem this necessary?"
    play music bg_regrouping loop
    ayumi "Because we believe that motive is the most important element, both in terms of the characters and the writer.{w} Whether the laws governing each world are rigid or nonsensical, surely there must be a semblance of reason for the readers to comprehend."
    show ayumi seriousleft at Three3 with Dissolve(0.2)
    hide ikuko with Dissolve(0.5)
    ayumi "From there, we can make conclusions and interpretations on both literary and meta levels."
    ayumi "If the readers lack motive -- driving questions, though provided -- themselves, how can they expect to ace the test, right?"
    show sayo seriousclosedpose at Three2 with Dissolve(0.2)
    sr5 "In the course of finding the answers to the provided questions, you are correct in asserting that idea.{w} But it is still their decision whether to dig deeper, since these questions are always not enough. More than the motive, impact also matters."
    show ayumi seriousclosed at Three3 with Dissolve(0.2)
    ayumi "Exactly.{w=1.0} And when time runs short, they realize that they should not have dwelled upon each passage for too long. There is no definite telling whether the problem lies in the method, motive, or impact, for it is subjective."
    show sayo smirkpose at Three2 with Dissolve(0.2)
    sr5 "Very well said.{w=1.0} Thank you for your interesting insights."
    show ayumi smile at Three3 with Dissolve(0.2)
    hide ayumi with Dissolve(0.2)
    stop music fadeout 2.0

    play sound sfx_applause
    show sayo smileopen at Eight7 with Dissolve(0.2)
    "After another round of applause, Sayo stood up and walked towards the whiteboard."
    play sound sfx_schoolbell
    "{i}*RRIIIIIIIIIIIIIIIIIIINNNGGG*{/i}"
    show sayo normaltalkleft at Eight7 with Dissolve(0.2)
    "It was already six in the evening -- second bell after curfew.{w} Some of the attendees looked frantic, tapping their watches to remind Sayo of the curfew."

    show sayo smileopen at Eight7 with Dissolve(0.2)
    sr5 "Not to worry. The front desk is just a few doors away.{w} Mrs. Genkai won't leaving until the meeting is adjourned."

    play music bg_thecomplex loop
    show sayo seriousserious at Eight7 with Dissolve(0.2)
    "Sayo erased a portion of the board and began writing the schedule for the mock exam proper."

    show sayo serioustalk2 at Eight7 with Dissolve(0.2)
    sr5 "As agreed upon, the mock exam tomorrow is mandatory and we expect all 202 Seniors to participate -- minus two from the original 204, of course."
    sr5 "Assembly time tomorrow is 6:30 AM {i}sharp{/i}. This is to simulate the first entrance exam on August 3-4."
    sr5 "Male and female students, alphabetically arranged, will be divided proportionately by gender among the Fourth Year classrooms."
    sr5 "The test proper will run for four hours, time-controlled by the proctors.{w} There will be no breaks inbetween, so bring your own snacks if you wish."
    show sayo seriousnormal at Eight7 with Dissolve(0.2)
    sr5 "And just in case, we will have this ready for synchronization."

    show sayo seriousnormalleft at Eight7 with Dissolve(0.2)
    "Sayo held up a flash drive for everyone to see. It had a pink label with two signatures: Sayo's and Mrs. Genkai's.{w} She passed it around the table."

    show sayo serioustalkleft at Eight7 with Dissolve(0.2)
    sr5 "At eight o' clock, I will engage this to the central stairs sound system.{w} It contains a single MP3 file of a pre-recorded countdown for each subject area."
    sr5 "There are four milestones recorded for each hour:{w=0.5} 30 minutes remaining, 15 minutes remaining, 5 minutes remaining, and 2 minutes remaining."
    show sayo seriousnormalleft at Eight7 with Dissolve(0.2)
    mh8 "And this is failsafe?"
    show sayo serioustalkleft at Eight7 with Dissolve(0.2)
    sr5 "It is. I already checked this through my computer and the file ran with no errors."

    show sayo blankface at Three2 with Dissolve(0.2)
    "When the USB returned to Sayo's possession, she replaced it into her pocket and continued the meeting."

    sr5 "All Fourth Year advisers will act as observers, in addition to the proctors. This is with the exception of Ms. Harada, who is expected to return next week."
    show sayo normaltalkleft at Three2 with Dissolve(0.2)
    sr5 "Tanaka, were the PCFs already distributed?"
    c_sec "And collected.{w=1.0} All set for tomorrow, Sayo."
    sr5 "Good. Please post the minutes at the council group chat.{w} Watanabe, you know what to do. Just ensure everyone knows the details of tomorrow's event."
    stop music fadeout 2.0
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "As for everyone, I would like to thank you once again for your time and contribution in the review sessions.{w} While we may not yet rest easy, I certainly hope we will by noon tomorrow."
    show sayo worriedtalk at Three2 with Dissolve(0.2)
    sr5 "And Hiroshi, give us until the post-evaluation to consider your suggestion."
    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "Keep safe on your way home, everyone. Meeting adjourned."
    hide sayo with Dissolve(0.2)
    return

label ch02_11_mockreview:
    scene black with fade
    centered "{b}Mock Examinations{/b}"

    scene bg msci with fade
    play sound sfx_chirp loop
    "JULY 13, 2013 - 0700H"

    window show
    nvl clear
    narr "We arranged ourselves according to surname.{w} I was assigned to Test Room 5, Classroom IV-E on a normal day."
    show hikaru naughty at Three3 with Dissolve(0.2)
    narr "And it looks like I'll be in the same room as my former classmate, Hikaru. She can't stop herself from giving hand signals to Aria, doesn't she? It's like they'll never see each other again."
    hide hikaru with Dissolve(0.2)

    window hide
    scene bg classroom2 with dissolve
    window show
    nvl clear
    narr "The proctor was already waiting inside, a thick pile of test booklets and answer sheets on his desk."
    narr "He directed each one of us to a particular seat according to the arrangement he was referencing.{w} I was at the second-to-last column, back row."
    play sound sfx_pageturn
    narr "Afterwards, he distributed the testing materials face down to the first row, instructing them not to open the booklets until he says so."

    nvl clear
    window hide

    scene bg classroom1 with dissolve
    proctor "I hope you've brought your No. 2s and other writing materials as instructed.{w} Please fill out the form on the first page. I have written some of the information you need on the blackboard."

    window show
    nvl clear
    narr "He directed our attention to the School ID and Division Number written in big letters."
    play sound sfx_pencilwriting loop
    narr "As for the rest of the details, we shaded the circles according to the information required on each item.{w} It took us a good fifteen minutes for everything -- just five on our name alone."

    nvl clear
    narr "And if I may be excused, there are just some things that always fascinate me whenever I get a hold of these glossy papers.{w} It's the fact that both our personal information and answers are fed into a machine for automated checking."
    narr "That machine checks for the position of the marks through those black dashes on the right. After validation, it is used for database input."
    narr "Which parts are which? The front page contains, as everyone already knows, our personal information. The back page contains the answer sheet with which we have to shade even more circles."
    narr "...Some basic stuff that people may never need to know."
    stop sound fadeout 1.0

    window hide
    scene bg msci with Dissolve(0.2)
    show sayo seriousnormalleft at Eight3 with Dissolve(0.5)
    window show
    nvl clear
    narr "Sayo made one last round trip sometime after I finished answering the front page. She headed into Test Room 4."
    hide sayo with Dissolve(0.5)
    play sound sfx_whistle
    narr "After another ten minutes, the teachers gave the proctors a signal. At that moment, they synchronized their timer to begin at 8 AM sharp."
    narr "The time limit is until noon, and nobody is allowed to leave the campus until then."
    play sound sfx_schoolbell
    narr "When the bell rang at eight, everyone opened their test booklets.{w} The proctor sat chin on fingers behind the desk, watching us as we answered the first part -- Language."

    scene bg msci with dissolve
    nvl clear
    play sound sfx_pencilwriting loop
    narr "There was just one other person that caught my eye.{w} In one of the few times I glanced out the window, I saw Ms. Harada patrolling with the other teachers."
    narr "I thought it strange at the time since I didn't even notice her earlier in the assembly. We were told she would be back by Monday.{w} I guess it probably means she got over things quicker than we thought."
    narr "After all, it must be more emotionally taxing when you're alone. That's what I think, at least."
    stop sound fadeout 1.0

    nvl clear
    window hide

    scene bg classroom1 with fade
    proctor "The first hour has ended. Please proceed to the next part -- Mathematics."
    proctor "Take note that you will {i}not{/i} be allowed to return to the previous section as you were given enough time to answer.{w} However, you are allowed to finish shading the circles of your answers."
    proctor "Proceed."

    "This is going to be a breeze, especially since I taught more than half of the items -- conceptually -- here.{w} So for the final hour, we have Science and Reading Comprehension."
    "There's the trouble alright. I love how they ordered this according to difficulty.{w} It didn't take long before we were already in Science."

    play sound sfx_static2
    "{b}*BUZZ*{/b}"
    stop sound

    "That was the sound system. It was supposed to have been fixed yesterday.{w} Or rather, it had engaged far too early. I thought they would start announcing the remaining time at eleven? Only two hours have barely passed!"

    play sound sfx_fire2 loop
    unk "AAAAAAAAAAAAAAAAAAAAAAHHHHHHH!!! {b}{i}*BREATHE*{/i}{/b} HAAAAAAAAAAAAAAHHH!!!{w=1.5}{nw}"

    "{cps=10}What the?!{w=2.0} Is that...?{/cps}{nw}"

    u_kk9 "{b}*WHEEZE*{/b}{w=1.0} AAAAAAAAAAHHH!!! It burns!{w=1.0} Haa... Haa... It burns! Gah...! Ino... ue...{w=1.0} HELP ME! SOMEBODY!!!{w=1.0}{nw}"
    stop sound

    play sound sfx_loudbuzz loop
    scene bg classroom2 with sshake
    "{b}{i}*STATIC*{/i} *BUZZ*{/b}"
    "Pencils started dropping on the floor, either by intense shock or by the pain caused by that stupid buzz! OW!{w} Whoever set that up is sick...{w=1.0} beyond sick! Heck, the whimpering from the girls in the room are penetrating these walls.{w} I can even hear those from the other room."
    stop sound
    play sound sfx_static2
    "{b}{i}*STATIC*{/i}{/b}"

    stop sound fadeout 2.0
    unk "{cps=10}Good day, my friends.{/cps}"

    "And a voice spoke, somewhat robotic or otherworldly, none of whom we recognized at all.{w} Somewhere beneath that gentlemanly tone there hides...{w=1.0} how would Sayo put it?"

    play music bg_decisions loop
    unk "First of all, I would like to humbly apologize for the commotion I may have caused. It seems that I have come at an inappropriate time.{w} Again, I extend my apologies."

    "The proctor ran outside, shouting at somebody off-view."

    proctor "Can somebody shut that thing off? It's unnerving everybody!"
    show ichirou serioustalk at Eight6
    iy1 "No, sir! We have to let them keep going."
    proctor "Keep going? An official assessment is underway, Mr. Yokohama!"
    show ichirou serioustalkleft at Eight6 with Dissolve(0.2)
    iy1 "Evidence, sir. Please, we must let them talk. Besides, it's about time they revealed themselves to us."
    show hikaru worried at Eight4 with Dissolve(0.2)
    hy10 "Please, sir! It might be the only chance we'll get from the culprit. It's for our friend, see?"
    proctor "{cps=10}The... culprit...?{/cps}{w=1.0} Fine. But I'll be calling the police once this guy is done."
    show ichirou serious at Eight6 with Dissolve(0.2)
    iy1 "Thank you."
    hy10 "But what about Ms. Harada?"

    show ichirou focusleft at Eight6
    "I placed a finger over my mouth."

    unk "I admit it.{w=1.0} I am the one to blame for all that has happened the previous month.{w=3.0}{nw}"
    scene bg classroom1 with dissolve
    show miyu pissedclosed at Eight3 with Dissolve(0.2)
    show akira serious at Eight5 with Dissolve(0.2)
    unk "You have just listened to the final moments of Kyou Kirisaki{w=1.0} as I am certain he still lingers within your memories.{w=1.0} How does one start to forget, I wonder?{w=3.0}{nw}"
    hide miyu with Dissolve(0.1)
    hide akira with Dissolve(0.1)

    scene bg classroom2 with dissolve
    show ayumi seriousleft at Eight8 with Dissolve(0.2)
    show ikuko worried at Eight7 with Dissolve(0.2)
    show hiroshi serious at Three2 with Dissolve(0.2)
    unk "A valiant attempt to save his life{w=0.5}, but the moment the flame was permitted to let loose{w=1.0} fate had chosen to be kind not to this poor soul.{w=3.0}{nw}"
    hide hiroshi with Dissolve(0.1)
    hide ayumi with Dissolve(0.1)
    hide ikuko with Dissolve(0.1)

    scene bg classroom1 with dissolve
    show yoshiro serious at Eight2 with Dissolve(0.2)
    show sumiko seriousleft at Eight7 with Dissolve(0.2)
    unk "A waste,{w=0.5} but nevertheless one less nuisance on my end.{w=1.0} And as for you, one more to create a zero sum game.{w=3.0}{nw}"
    hide yoshiro with Dissolve(0.1)
    hide sumiko with Dissolve(0.1)

    scene bg classroom2 with fade
    show ichirou focusleft at Eight6 with Dissolve(0.2)
    show hikaru worried at Eight4 with Dissolve(0.2)
    unk "So now, I question myself,{w=0.5} who is next? Answer this for me.{w=4.0}{nw}"

    cen "{cps=15}{i}Who wishes to go next, I wonder?{/i}{/cps}"

    stop music
    play sound sfx_fistbang
    hide ichirou with vpunch
    hide hikaru
    "{b}*SLAM*{/b}"
    "That bastard!"

    scene bg classroom1 with dissolve
    student "Ichirou!"
    iy1 "Who the hell do you think you are?! Some kind of God?{w} You can't just take our lives for this sadistic game of yours!"
    proctor "Mr. Yokohama, please settle down."

    play sound sfx_dooropen
    scene bg msci
    "I turned a deaf ear on him and burst out of the classroom.{w} He didn't follow me, only shaking his head in disappointment and disbelief."

    unk "It is rather fascinating --{w=0.5} that ecstacy one feels when his conjectures are correct.{w=1.0} You expose those who live with a mask{w=0.5} and tear them down along with the others of their own kind.{w=3.0}{nw}"
    unk "And as made clear by these recent events, there are merely two possibilities --{w=1.0} {cps=10}a shattered persona,{w=0.5} or the end of life.{/cps}{w=3.0}{nw}"
    unk "If you were given the choice,{w=0.5} would you rather live on in this world full of sorrow and anguish{w=0.5} living the lies you yourself have created,{w=1.0} or would you choose mercy and carry on to the next life{w=0.5} where all your imagined Utopias would come to fruition?{w=3.0}{nw}"
    unk "The world is naught but an illusion,{w=0.5} and all its inhabitants live with an illusion they cannot rid of themselves of.{w=1.0} So what is the point in struggling against the chains in order to see the light?{w=3.0}{nw}"
    unk "And I offer salvation --{w=0.5} I have finally come.{w=1.0} Those who are the chosen few, I congratulate you in advance.{w=3.0}{nw}"
    unk "But when the time comes,{w=0.5} will you be ready?{w=1.0} Let it be known that the sands on the upper glass run thin,{w=0.5} for the {i}Second Indian{/i} will soon come to pass.{w=3.0}{nw}"

    "Hang on... Second Indian?{w} That's something I would never expect an Anti-Christ to be talking about.{nw}"
    play sound sfx_loudbuzz
    "{b}*BUZZ*{/b}"
    "Argh! What the hell?"

    play music bg_chloeslullaby loop
    window show
    nvl clear
    narr "{i}{cps=15}One little,{w=0.5} Two little,{w=0.5} Three little Indians~ puku!{w=1.0}{/cps}\n{cps=20}Swing, swing, swing...{w=0.5} Who will be chosen by this roulette?{w=1.0}{/cps}\n\n{cps=15}Four little,{w=0.5} Five little,{w=0.5} Six little Indians~ puku!{w=1.0}{/cps}\n{cps=20}Swing, swing, swing...{w=0.5} In this quandary of life and death?{w=1.0}{/cps}\n\n{cps=15}Seven little,{w=0.5} Eight little,{w=0.5} Nine little Indians~ puku!{w=1.0}{/cps}\n{cps=20}Swing, swing, swing...{w=0.5} Ready?!{w=1.0}{/cps}\n\n{cps=15} You bet, puku!!!{w=1.0}\n{b}TEN LITTLE INDIAN BOYS!!!{/b}{/cps}{/i}"
    play sound sfx_giggle
    narr "{i}Kyekyekyekyekyekyehahahahahahaha... Ihihihihihihihihihihi...{/i}"

    nvl clear
    window hide

    "I get it now...{w} That rhyme from my childhood, now used as a framework for this \"savior's\" method of {i}salvation{/i}.{w} Sayo and Inoue have told me about this, read it from somewhere."

    sr5 "On that island, ten people died according to the rhyme -- a timeless story, I must say.{w} From there, this very same rhyme became one of those used to foretell an omen of death."
    stop music
    show sayo creepy serious at Three2 with vpunch
    show sayo seriousnormal at Three2 with Dissolve(2.0)
    iy1 "Sayo! How long have you been standing there?{w=1.0} And how did you know what I was --{nw}"
    show sayo seriousclosed at Three2 with Dissolve(0.2)
    sr5 "Have you learned nothing, Ichirou?{w=1.0} But that isn't the issue at hand."
    show sayo seriousclosedpose at Three2 with Dissolve(0.2)
    sr5 "{cps=15}It's finally coming to me. Only now have I realized the true meaning of it...{/cps}"
    iy1 "What do you mean?"
    show sayo serioustalkpose at Three2 with Dissolve(0.2)
    sr5 "Surely, Kyou is the First Indian if we consider this little rhyme of his.{w} They are challenging us, Ichirou. Their gambit relies on them picking us off one by one whilst remaining undercover.{w} {i}*sigh*{/i} Talk about the highest form of hypocrisy."
    iy1 "I suppose you're right, but don't you think...?"
    show sayo serioustalk2 at Three2 with Dissolve(0.2)
    sr5 "Yes. Listen to how this all makes little sense."
    sr5 "{i}Two little Indians sitting in the sun;{w=1.0}\nOne got frizzled up and then there was One.{/i}"
    show sayo serioustalkleft at Three2 with Dissolve(0.2)
    sr5 "By now, there would already have been eight victims before Kyou.{w=1.0} And that makes this Second Indian of theirs more confusing. It should be their last.{w} {cps=4}Unless...{/cps}"

    play sound sfx_static2
    "{b}*BUZZ*{/b}"
    stop sound fadeout 2.0

    play music bg_satiate loop
    iy1 "Inoue! They're going after her!"
    show sayo serioustalk2 at Three2
    sr5 "Hold it!{w} We can't say for sure they're going after a vulnerable girl, let alone one who just survived the horrors they inflicted.{w} I sense them as principled, whoever they are. Meticulous, if you prefer that word."
    iy1 "Well, I'm not just gonna stand around here and let them make their move. Right after this, damn everything, I'm going to the hospital to warn Inoue!"
    show sayo upset at Three2 with Dissolve(0.2)
    sr5 "You do realize your impulsive behavior will do more harm than good to her?{w} Stay put. I'll make sure Emmerich will hear everything that transpired just now."
    iy1 "And what if he doesn't?{w=1.0} Tell me how, Sayo.{w=1.0}{nw}"
    show sayo seriousnormalleft at Three2 with Dissolve(0.2)
    sr5 "Shhh!"
    unk "And do not think I will be done just yet.{w=3.0}{nw}"
    unk "Yawn at the words I speak and leave this all behind you.{w=1.0} But there are those before you who were foolhardy enough to do so,{w=0.5} enough for them to have a {i}rather pleasurable experience{/i}.{w=1.0} You wouldn't want a repeat performance of that, would you?{w=1.0} Don't be as naive as that girl...{w=3.0}{nw}"
    unk "If I were able to capture two birds in the most unimaginable circumstances possible,{w=1.0} {cps=10}then I can do it again...{/cps}{w=0.5} {cps=8}and again...{w=0.5} and again...{w=0.5} Hehehehehe...{/cps}{w=3.0}{nw}"
    unk "You keep your wits about you,{w=0.5} and keep an eye on your peers as best as you can.{w=1.0} I have waited long for our intellects to clash --{w=0.5} a cat and mouse on equal footing.{w=3.0}{nw}"
    unk "{cps=12}I expect great things from you...{/cps}{w=1.0}{nw}"
    stop music fadeout 2.0

    cen "{cps=12}{i}...Student Council President{w=0.5} {b}Sayo Ronoroa.{/b}{/i}{/cps}"

    play sound sfx_static2
    "{b}*BUZZ* {i}*STATIC*{/i}{/b}"
    stop sound fadeout 1.0

    "Sayo...?{w=1.0} But why? What does she have to do with that maniac?! I don't understand."

    iy1 "What did they mean, Sayo? What's up with that last bit?"
    show sayo upset at Three2 with Dissolve(0.2)
    sr5 "{cps=3}...{/cps}"
    iy1 "{cps=5}Sayo-chan?{/cps}"
    hide sayo
    play music bg_controlledchaos loop
    play sound sfx_whoosh
    sr5 "Back to your rooms, everyone! Nobody leaves until the authorities arrive.{w} All proctors, please suspend the mock examinations. We have an emergency."

    window show
    nvl clear
    narr "She finally lost her composure, the first I've seen since First Year.{w} And why wouldn't she? Sayo's been {i}threatened{/i} -- I wouldn't call that a {i}challenge{/i}."
    narr "At this point, the path beyond is obscured by a smoke screen.{w=0} Whether the smoke is gray or red, I couldn't tell...{w=1.0} nobody couldn't.{w} It's death or insanity for us."
    narr "{cps=10}For now,{w=0.5} they win.{/cps}"

    nvl clear
    window hide

    scene black with fade
    "JULY 13, 2013 - 1030H"

    scene bg classroom1 with dissolve
    show akira worriedleft at Eight5 with Dissolve(0.2)
    "This can't be real, can it?{w} We're in danger.{w=1.0} I never thought..."
    "{i}*tap*{w=0.5} *tap*{w=0.5} *tap*{/i}"
    "It's been half an hour already since Sayo contacted the police.{w=1.0} Where are they? I'm starving!"
    "Or maybe it's just... The crackers must have been completely digested by my system. What bad luck do we have?"
    stop music fadeout 2.0

    show miyu bored at Eight3 with Dissolve(0.2)
    mh8 "You know, it's out of your character to be fidgeting all over the place like that."
    show akira surprised2 at Eight5 with Dissolve(0.2)
    ai2 "How can you be so calm after all that?{w} Didn't you hear what that guy said? He's after our heads, and the President is in danger!"
    show miyu naughty closepose at Eight3 with Dissolve(0.2)
    mh8 "Oh, I see. I understand now.{w} Why would I be surprised anymore when the things I've seen through my eyes are far too much?"
    show miyu naughty focuspose at Eight3 with Dissolve(0.2)
    mh8 "That phantom figure who passed through me{w=1.0} or that mysterious doppelganger the following evening...{w} You do realize Ichirou and I have been stalked for a while now."
    show akira worried at Eight5 with Dissolve(0.2)
    ai2 "Did it follow you here?"
    mh8 "No. I'm sure of that.{w} It's more of a feeling than anything physical, though. Never experienced anything uncanny after the latter."
    show miyu bored at Eight3 with Dissolve(0.2)
    mh8 "{cps=10}...Until now.{/cps}"

    play music bg_onthingstocome loop
    "I don't know. Miyu's intense glare just provokes the butterflies."
    "Perhaps he's right. I haven't even been in his shoes to question his feelings.{w} He may as well be quaking in fear much like the rest of us. But he's hiding it, putting on a brave face instead."
    "If my impression of him is right, I'd say he's scared too. On the contrary, that scowl tells a different story."

    show miyu confused at Eight3 with Dissolve(0.2)
    mh8 "Where is Sayo?"
    show akira annoyed at Eight5 with Dissolve(0.2)
    ai2 "With Ms. Harada on the center stairs, most likely investigating the source of that eerie broadcast.{w} The entire Council has a copy of the audio file{w=0.5} -- no way something like that would play before the pre-recorded countdown!"
    show miyu serious at Eight3 with Dissolve(0.2)
    mh8 "Don't overexplain, Akira. It's not like we'll accuse any of you for pulling such a tasteless stunt.{w} No. I'm just asking where she is, and am not in the mood to play detective."
    show akira fangblush at Eight5 with Dissolve(0.2)
    ai2 "Oh? But I though you already had your eyes on Hikaru?"
    show miyu pissedclosed at Eight3 with Dissolve(0.2)
    mh8 "You're lucky I didn't bring a broadsheet with me...{w} Of course, I'll be concerned for her and you should be too."
    show akira happy at Eight5 with Dissolve(0.2)
    ai2 "Awww... Can't you lighten up at a time like this, Miyu? You'll die young if you keep that attitude up."
    show miyu pissed at Eight3 with Dissolve(0.2)
    mh8 "Tch."
    show miyu worried at Eight3 with Dissolve(0.2)
    mh8 "Fine. I'm sorry.{w} I'm just thinking about my own hide."
    mh8 "They got us by the throat, and they'll slit with their blade if given the chance.{w} And when is that?{w=1.0} We'll never know until someone --{nw}"

    show akira serious at Eight5 with Dissolve(0.2)
    "Yeah, spare me the word. It's not something I want to hear right now."

    show miyu proudclosed at Eight3 with Dissolve(0.2)
    mh8 "A madman madder than the Mad Hatter.{w=1.0} Alliterative and witty, yes, but there is no description more appropriate for them!"
    ai2 "The Anti-Christ, I say to them."
    show akira annoyed at Eight5 with Dissolve(0.2)
    ai2 "But that rhyme --{w=0.5} their version --{w=0.5} makes me shaky. How should I put it?{w} Ten Little Indians and the second one will go bye bye real soon. When is {i}soon{/i}?"
    show miyu pissed at Eight3 with Dissolve(0.2)
    mh8 "Like I have any idea.{w} Although, if we base it on Kyou and Inoue's abduction, I'd wager the clock begins ticking {i}sometime next week{/i}."

    "Next week! What about tomorrow or today?{w} That's right...{w=1.0} It took place sometime around the morning of the 17th or 18th. Miyu's estimation is correct."
    "Most importantly, who are the other \"Indians?\" Only two of the ten are confirmed -- Kyou and Inoue.{w} Ack! I almost forgot about Pres."

    show miyu focusedpose at Eight3 with Dissolve(0.2)
    mh8 "Three Indians we know -- Kyou Kirisaki, Inoue Shinozaki, and Sayo Ronoroa -- and seven others whose identities remain unknown.{w} The chances are 7 in 200 for each of those not mentioned, including you and me."
    mh8 "As for those who will be offed next?{w} I just hope the odds drop to zero as soon as possible. Yes, that is the only winning probability against this phantom."
    show akira serious at Eight5 with Dissolve(0.2)
    ai2 "They must have chosen his victims from the start and when they will attack them.{w} Why don't they just tell us? Do we have to wait for either Inoue or Sayo to go first?"
    show miyu talk at Eight3 with Dissolve(0.2)
    mh8 "If they have at least half a brain, going after Inoue is not a smart move. No, not fair enough.{w} Second, if you were the culprit, would you go after the one you've challenged immediately?{w=1.0} Absolutely not. It's all too predictable if either would be the case."
    show akira surprised2 at Eight5 with Dissolve(0.2)
    ai2 "Then he's going for one of the seven?"
    show miyu bored at Eight3 with Dissolve(0.2)
    mh8 "Yes.{w=1.0} {cps=15}And most likely, one of your propositions are correct; that is --{/cps}{nw}"
    stop music

    play sound sfx_police
    "{i}*SIREN*{/i}"
    hide akira with Dissolve(0.2)
    hide miyu with Dissolve(0.2)

    scene bg msci with dissolve
    show emmerich serious at Three1 with Dissolve(0.5)
    show sayo blankface at Three2 with Dissolve(0.2)
    window show
    nvl clear
    narr "The cops have finally arrived. Thank goodness!"
    stop sound fadeout 2.0
    narr "Out the mobile emerged Inspector Emmerich, greeted by Mrs. Sokoguchi and Sayo.{w} He asked them a few questions before they accompanied him to the central stairs."
    narr "I felt relieved after their arrival,{w=1.0} yet there is something I can't just ignore.{w} I don't know what, but whatever they find won't be very pleasant."
    hide sayo with Dissolve(0.2)
    hide emmerich with Dissolve(0.2)
    narr "I'm both excited and afraid of Monday. I want to know, but at the same time, I don't want to."

    nvl clear
    window hide
    return

label ch02_12_posteval:
    scene black with fade
    "JULY 15, 2013 - 1130H"

    play sound sfx_fistbang
    scene bg conferenceroom with vpunch
    play music bg_interloper loop
    c_4r "What the hell did you say?"

    "Not five minutes into the meeting, the pot had already boiled."

    show sayo serioustalkpose at Three2 with Dissolve(0.2)
    sr5 "Mind your language, Onizuka. I never say anything damaging to anyone without proof."

    show sayo seriousnormalpose at Three2 with Dissolve(0.2)
    window show
    nvl clear
    narr "She showed the flash drive to everyone -- the pink label with her and Mrs. Genkai's signatures intact.{w} Apparently, it was the one used by the culprit to play those horrifying clips through the intercom."
    narr "Our initial thoughts were that the USB was swapped."
    narr "In that case, however, the culprit could have also replicated the two signatures perfectly{w=1.0} and they are very difficult to forge.{w} If not, then the label could have been tampered with and plastered into a similar-looking USB."
    narr "It was neither of those.{w} And this raised only more questions about the ominous recording last Saturday."

    nvl clear
    window hide

    show sayo seriousnormalleftpose at Three2 with Dissolve(0.2)
    c_vp "I did a runthrough of the file in that flash drive. I heard nothing of the sort."
    c_po "Indeed. How anyone was able to insert such a clip is beyond me.{w} The surveillance cameras around the central stairs show no suspicious individual going there."
    show sayo serioustalkpose at Three2 with Dissolve(0.2)
    sr5 "That's correct.{w} I crossed-checked both the USB's contents and the entire surveillance footage that morning with the inspector. He was able to tell me as much when I had it analyzed.{w} Even the physical condition of the USB he verified no tampers."
    stop music
    ai2 "Strange.{w=1.0} There is no other way to transmit sound through the intercom but that soundboard.{w} Tell me, we didn't imagine that broadcast? We all heard it?"

    play music bg_hazydisorientation loop
    show sayo seriousnormalpose at Three2 with Dissolve(0.5)
    "And all I got from that last sentence is a horde of blank stares.{w=1.0} Those faces so emotionless they could disappear at any moment."
    hide sayo with Dissolve(0.2)
    scene bg conferenceroom dark with dissolve
    "For the first time in years, I felt that I was alone...{w=0.5}{cps=15} an oddball of the bunch.{w=1.0} No amount of humor can save me from this.{/cps}"
    show sayo creepy seriouspose at Three2 with Dissolve(1.0)
    "{cps=20}Of the ten other pairs, Sayo's eyes made the coldest stare.{/cps}"
    show sayo creepy smirkpose at Three2 with Dissolve(0.5)
    "{cps=20}She must think I'm going crazy, brushing aside my words as mere ramblings.{w=1.0} The way her eyes jitter is breaking down the shield around me.{/cps}"
    show sayo creepy smirkpose2 at Three2 with Dissolve(0.5)
    "{cps=15}This isn't like her at all.{w=1.0} When the smile fades and returns more slowly than usual, I never knew she could turn into a bogeyman.{/cps}"
    stop music

    play sound sfx_giggle
    show sayo creepy smileteethpose at Three2 with vpunch
    r_sr5 "{cps=10}Hihihi...{w=1.0}{/cps} {cps=12}Hihihihihihihehehehehehe...{/cps}"

    "{cps=12}She's giggling...{w=1.0} No way I made that up.{w=0.5} I didn't!{/cps}"

    scene bg conferenceroom
    show sayo smileopenpose at Three2
    sr5 "No. We all heard it.{w} Don't ever think you were the only one."
    ai2 "Oh, right. Right. Ahem.{w} Couldn't stop thinking about it over the weekend. It was too surreal to be true, see? Ahahaha..."

    "One by one, they flashed genuine smiles. I gave them one of my own whilst I wiped the sweat off of myself.{w} At the very least, in this hour of confusion, we made ourselves a small bubble of relief."
    "Then what I was supposed to say clicked into my mind."

    ai2 "Right. Since the mock exam was cut short last Saturday, is there any chance we'll have a second one? Say, this July 27?"
    show sayo worriedpose at Three2 with Dissolve(0.2)
    sr5 "It's an understatement if I say the proctors were spooked after that conundrum. It would be much harder to approve Hiroshi's request, though."
    sr5 "If you recall, we had prepared everything before the school year started. It will be difficult to procure another set of test materials. We had agreed that we hold only one mock exam for the review sessions."
    ai2 "Is that so?{w=1.0} That's a shame."
    show sayo normaltalkpose at Three2 with Dissolve(0.2)
    sr5 "Besides, instructions are to return the review materials the first Monday of August.{w} We have more than enough time to self-study and become capable enough after the review sessions last week."

    window show
    nvl clear
    narr "The rest of the meeting went smoothly after that, no further word about the mock exam. Besides, it must have been our stomachs speaking, forming these malformed images and sensations within our minds."
    show sayo blankface at Eight6 with Dissolve(0.2)
    narr "At noon, Sayo adjourned the meeting.{w} She remained in the room to perform her post-meeting routine."
    show akira worriedleft at Eight4 with Dissolve(0.2)
    narr "I stayed behind, not what I would do when my stomach is growling."

    nvl clear
    window hide

    show sayo normaltalkleft at Eight6 with Dissolve(0.2)
    sr5 "Don't mind me, Akira. You go on and have your lunch."
    show akira worried at Eight4 with Dissolve(0.2)
    ai2 "{cps=10}Ummm... Sayo?{/cps}"
    ai2 "I don't feel hungry, actually. There's just something that's been bugging me.{w=1.0} Mind if I ask you something?"
    show sayo smileopen at Eight6 with Dissolve(0.2)
    sr5 "Ask away!{w=1.0} But just give me a minute to finish arranging these papers. Help me with these, please.{w=0.5} Thank you."

    "I helped her fill out the remaining paperwork. Basic stuff, and I'm always happy to help with that."

    play music bg_undaunted loop
    show akira serious at Eight4 with Dissolve(0.2)
    ai2 "Pres, what was that all about? You know, when I asked if what we experienced last Saturday was real?"
    show sayo worried at Eight6 with Dissolve(0.2)
    sr5 "..."
    show sayo worriedtalk at Eight6 with Dissolve(0.2)
    sr5 "I didn't mean to scare you like that earlier.{w=1.0} I apologize for my demeanor."
    show akira proud at Eight4 with Dissolve(0.2)
    ai2 "It's okay."
    show sayo seriousnormal at Eight6 with Dissolve(0.2)
    sr5 "Let me ask you this.{w} Have you ever experienced a situation where it feels real when it truly is not? Or one that feels real but it turns out to be an illusion?"
    show akira happy at Eight4 with Dissolve(0.2)
    ai2 "Huh? I don't get it.{w} I guess my default answer is yes, so let's go with that. Hehehehe..."
    show sayo serioustalkleft at Eight6 with Dissolve(0.2)
    sr5 "Then let us define the extremity of these questions.{w} Did you ever wish that everything has only been a product of your own imagination...{w=1.0} that everything will end in a {i}finger snap{/i}?"
    sr5 "Is it euphoria, the one you wish will never end?{w=1.0} Is it despair, the one that continually haunts your dreams for as long as it wishes to linger?{w} Tell me, what kind of reality do you think we are in?"
    show akira proud at Eight4 with Dissolve(0.2)
    ai2 "The second.{w=0.5} It's what I think, anyway."
    show sayo serioustalk2 at Eight6 with Dissolve(0.2)
    sr5 "What if you never wake up?"
    show akira surprised at Eight4 with Dissolve(0.2)
    ai2 "I surely don't want that scenario to happen. So, what then?"
    show sayo seriousnormal at Eight6 with Dissolve(0.2)
    sr5 "You must realize it just as I did.{w} This is a nightmare we're sucked into without our consent.{w=1.0} That very fact we're blinded from until the day that mysterious phantom revealed himself to us."
    sr5 "What kind of toxin they fed Kyou and Inoue?{w=1.0} Why did it result in death?{w=1.0} Who will go next?{w=1.0} These are the questions we must answer in the coming days, and some these answers we may never know."
    show akira surprised2 at Eight4 with Dissolve(0.2)
    ai2 "\"We\"? Do you mean {i}all{/i} or {i}some{/i}?"
    show sayo normaltalk at Eight6 with Dissolve(0.2)
    sr5 "What do you think, Akira? Can you really tell even at this early stage?"
    show akira annoyed at Eight4 with Dissolve(0.2)
    ai2 "{cps=10}I can't...{/cps}"
    stop music fadeout 2.0

    play sound sfx_schoolbell
    "{i}*RIIIIIIIIIIIIIIINNNGGG*{/i}"

    show sayo blankface at Eight6 with Dissolve(0.2)
    sr5 "You missed your lunch.{w} See you later, then?"

    window show
    nvl clear
    narr "That was fast.{w} Twenty minutes flew by like they were nothing."
    play sound sfx_dooropen
    hide akira with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    narr "She set aside the paperworks into her drawer and made a cross as we left the room.{w} On the way, she shut the lights off."

    nvl clear
    window hide

    scene bg msci with dissolve
    play sound sfx_wind loop
    show akira surprised at Three1 with Dissolve(0.2)
    show sayo blankface at Three3 with Dissolve(0.2)
    ai2 "By the way, do you have any idea who are the Indians the mysterious voice mentioned?"
    show sayo serioustalk at Three3 with Dissolve(0.2)
    sr5 "Do I?{w} {cps=15}If my conjecture is right, then those would be me, Inoue, Kyou, and...{/cps}"

    show sayo seriousclosed at Three3 with Dissolve(0.2)
    "She stopped walking and stared at the ground in deep thought."
    "Although her expression didn't change, I could tell. She must've rubbed off on me."

    show akira worried at Three1 with Dissolve(0.2)
    show sayo worriedtalk at Three3 with Dissolve(0.2)
    sr5 "I'm not sure. I'm not sure. I hope I'm wrong.{w} You better head back to class. You don't want to be late."
    show sayo worried at Three3 with Dissolve(0.2)
    sr5 "Goodbye, Akira."
    stop sound fadeout 1.0

    hide sayo with Dissolve(0.2)
    show akira worriedleft at Three1 with Dissolve(0.2)
    "She paced quickly towards IV-E, never looking back after saying farewell.{w} What's gotten into her?{w=1.0} That's another big question mark on my face."
    hide akira with Dissolve(0.2)

    return

label ch02_13_death02:
    scene bg msci rain with fade
    play music sfx_rain loop
    "JULY 19, 2013 - 1630H"

    scene bg classroom1 with dissolve
    window show
    nvl clear
    narr "It had been raining for the last few days. In fact, the sun had been hiding behind the clouds since morning. Its light shone through, regardless."
    narr "In a few minutes, Mrs. Ritsuko will dismiss us for the weekend.{w} As our adviser, she'll probably spend another five minutes praising and ranting about the cleanliness of our homeroom. That never gets old."
    narr "We could barely hear her and the reporters in front because of the intense downpour outside.{w} She was critiquing them about their project idea{w=1.0} -- to create a sustainable irrigation system that will benefit the agriculture industry; at the same time, to solve the problem of flashfloods in our country."

    nvl clear
    window hide

    t_rit "So tell us, how feasible do you think is this idea of yours?"
    student "Our aim is to service those living in the countryside. With the prevalence of flashfloods during the wet season, the irrigation system would store the rain water for the benefit of those in the agricultural sector."
    student "It may be one of one-hundred solutions with a similar idea, but the major scope is there:{w=1.0} to help those in flood-prone areas, and turning the problem into a valuable resource."
    t_rit "You speak volumes about this benefits that and converting a problem into a resource."
    t_rit "How do you plan on getting your idea approved if, for example, one of those ninety-nine ideas you mentioned are theoretically more efficient and more feasible than yours? Could you be more direct with your answer?"

    "The reporter hesitated to think, all eyes on her.{w} One of her groupmates is signalling some ideas for her to speak, yet somehow she could not articulate her thoughts properly."
    play sound sfx_schoolbell
    "{i}*RIIIIIIIIIIIIINNNGGG*{/i}"

    t_rit "That will do. I want you to think about your response next meeting.{w} Please return to your seats now."

    window show
    nvl clear
    narr "Mrs. Ritsuko stood up in front and delivered her final comments for the reporters."
    narr "When she transitioned into homeroom matters, she gave some comments about the state of our classroom and inquired about the well-being of her students. As our adviser, naturally."
    narr "We packed our things to go home.{w} However, little has changed from the situation outside. Those who would leave now would risk catching a cold from the rain.{w} A few others, like me, need to stay for an hour or so. Hopefully, the showers might have at least lightened by then."

    nvl clear
    window hide

    show ichirou happy at Three3 with Dissolve(0.2)
    show hiroshi smile at Three2 with Dissolve(0.2)
    iy1 "Yo. You heading to the meeting now?"
    hk7 "Of course. {i}*chuckle*{/i} Wouldn't want to keep the Council waiting."
    show ichirou smile at Three3 with Dissolve(0.2)
    iy1 "I'll catch up later. Just gotta finish my Friday duties before I go.{w} See you, Hiroshi."
    hide hiroshi with Dissolve(0.2)
    hide ichirou with Dissolve(0.2)

    scene bg msci rain with dissolve
    window show
    nvl clear
    narr "A front slap, back slap, and a chest bump later, I left our class president and headed to the Student Council office."
    narr "As with the usual rainy days, students convened at the front guard's desk. Either they are waiting for their rides home, or they are equipping their rain gears.{w} Though, they could have done the latter at their classrooms."
    scene bg conferenceroom with dissolve
    stop music fadeout 3.0
    play sound sfx_thunder
    show sayo smileopenpose at Three2 with Dissolve(0.2)
    narr "Just past IV-A, I immediately went through the first door on the right.{w} Sayo and a few other officers were already seated and engaging in small talk."

    nvl clear
    narr "Where is Akira, by the way?{w} One good guess is that he'll arrive right after the meeting starts.{w} Second guess...{w=1.0} Drop the idea. I know how these types work all too well."
    narr "After the next ten minutes, our numbers increased to ten, with Ichirou and Sumiko joining me.{w=1.0} Then came the other three from IV-C -- Yoshiro, Hikaru, and Miyu.{w=1.0} Closely following them is the last two -- Ayumi and Ikuko."
    narr "Yep. It seems I've hit the dots about that guy."
    narr "We finished the roll call without him. About half of those present, particularly the officers, shook their heads."

    nvl clear
    window hide

    show sayo normaltalk at Three2 with Dissolve(0.2)
    play music bg_greatminds loop
    sr5 "It's five o' clock, so let's start."
    stop music fadeout 1.0

    play sound sfx_knock
    show sayo normaltalkleft at Three2
    "A knock on the door."
    play sound sfx_dooropen
    "A familiar face hurriedly went inside and took his place."

    show akira fangblush at Eight2 with Dissolve(0.2)
    show sumiko smile at Eight7 with Dissolve(0.2)
    st3 "I'm not surprised these three made it here before you."
    ai2 "It's an emergency, I tell you! An emergency of utmost importance!"
    show sumiko smirk at Eight7 with Dissolve(0.2)
    st3 "Got it."

    show sayo smileopen at Three2 with Dissolve(0.2)
    "\"AHAHAHAHAHAHAHAHAHAHAHAHAHA!!!\""
    hide sumiko with Dissolve(0.2)

    show akira happy at Eight2 with Dissolve(0.2)
    ai2 "Pardon me, Pres. I'm late."
    sr5 "Late by one sentence, I must say. {i}*giggle*{/i}{w=1.0} Ah, it looks as though the urgency of the matter warrants no further delay."
    show akira proud at Eight2 with Dissolve(0.2)
    ai2 "Thank you very much.{w=1.0} Sorry...{w=0.5} If we may continue, please."
    show sayo smileopenpose at Three2 with Dissolve(0.2)
    sr5 "Unless I wish it, too.{w=1.0} Let's stick with the schedule more often for our future endeavors, shall we?"
    hide akira with Dissolve(0.2)

    play music bg_greatminds loop
    window show
    nvl clear
    narr "The secretary moved to the whiteboard and wrote the agenda while Sayo gave her opening remarks."
    narr "It seems my request had been granted after all.{w} However, in light of recent events, the review sessions originally scheduled this week was postponed."

    nvl clear
    window hide

    show sayo normaltalkpose at Three2 with Dissolve(0.2)
    sr5 "Coincidentally, the first quarter exams are scheduled on the week of the first entrance exams.{w} So, this is the plan we propose."
    sr5 "We decided to schedule the sessions at Thursday and Friday next week. That way, we will all have time to arrange our requirements for the quarter.{w} The concerned had already approved this."
    show sayo smileopenpose at Three2 with Dissolve(0.2)
    sr5 "The Council collectively evaluated your performances for the first iteration of these review sessions.{w} You may continue with your delegations if you find it effective.{w=1.0} We all agree."

    "After a few more updates and small debates, Sayo invited us to ask questions.{w} Three attendees raised their fingers."

    show yoshiro surprised2 at Eight8 with Dissolve(0.2)
    ys6 "Question. What if we take this approach --{w=1.0} We set two-thirds of the class time for the actual review sessions, then the remaining third for the exams?"
    show sayo normaltalkpose at Three2 with Dissolve(0.2)
    sr5 "If it works for you, then you may do as you wish. Allotting one hour for the whole session is not mandatory, anyway."
    hide yoshiro with Dissolve(0.2)
    show miyu talk at Eight3 with Dissolve(0.2)
    mh8 "What if one facilitator is absent for the day? Say, he is assigned to a team and he is the only one free to handle the session."
    show sayo normaltalkleftpose at Three2 with Dissolve(0.2)
    sr5 "Then the session may not be held.{w} Worst case, a certain area in Math may not be held at all."
    sr5 "Again, you may elect to use the period for study time or class.{w=1.0} The latter, I assure you, is very unlikely."
    hide miyu with Dissolve(0.2)
    show ikuko talk at Eight8 with Dissolve(0.2)
    show sayo blankfacepose at Three2 with Dissolve(0.2)
    ikuko "If we feel that there is nothing further to teach, can we cross over to another subject?{w} How about subjects aside from Science, Math, or English?"
    show ikuko blank at Eight8 with Dissolve(0.2)
    show sayo normaltalkpose at Three2 with Dissolve(0.2)
    show sayo normaltalkleftpose at Three2 with Dissolve(0.2)
    sr5 "What say you? Hiroshi? Miyu?"
    show hiroshi bored at Eight6 with Dissolve(0.2)
    hk7 "Frankly, if I were the teacher of the timeslot you're using, I would rather have regular class.{w} There is no issue with us. Because why not?"
    show miyu smile at Eight3 with Dissolve(0.2)
    mh8 "I agree. There wouldn't be any issue if you decide to integrate Math into your sessions.{w} You can help us study for Social Studies or Mandarin, for example."
    show sayo smileopenpose at Three2 with Dissolve(0.2)
    sr5 "Word of advice, Ikuko.{w=1.0} If the teacher allows you to hold a review session, use it as much as possible.{w} Ask Mrs. Ichimiya for advice. She'll know what to do if you ever get stuck."
    hide miyu with Dissolve(0.2)
    hide ikuko with Dissolve(0.2)
    hide hiroshi with Dissolve(0.2)
    stop music fadeout 2.0

    window show
    nvl clear
    narr "And all is settled."
    narr "The minute hand slowly approaches the twelve mark, and the rain shows no sign of stopping any time soon.{w} Although the pattering of rain drops are soothing, I'm more worried about the road home. Another wet socks for the laundry."
    narr "I hope not."
    hide sayo with Dissolve(0.2)

    nvl clear
    window hide

    scene bg conferenceroom with fade
    "JULY 19, 2013 - 1750H"

    window show
    nvl clear
    narr "Ten minutes to six; Sayo recited the usual closing remarks and adjourned the meeting.{w} The council members, except Sayo and I, left immediately."
    narr "The club officers are sticking around, too --{w=1.0} Miyu, Hikaru, Yoshiro, Sumiko, Ichirou, Ayumi, Ikuko, and Hiroshi. Ten of us in the room.{w} Isn't this sweet?"

    nvl clear
    window hide

    show hiroshi boredtalk at Three3 with Dissolve(0.2)    
    hk7 "Akira, if I may excuse you for a moment..."
    hide hiroshi with Dissolve(0.2)

    "He ushered me towards the office.{w} I was quite confused at first about why he invited me there. If I remember correctly, he asked a certain favor a few days ago."

    play music bg_twotogether loop
    scene bg facultyroom with Dissolve(0.2)
    show hiroshi bored at Three2 with Dissolve(0.2)
    ai2 "MY workstation?"
    show hiroshi determined at Three2 with Dissolve(0.2)
    hk7 "Yes. If I could borrow it for...{w=0.5} thirty minutes, tops."
    ai2 "I don't know, Hiroshi. I can't guarantee your flash drive's safety or my terminal's. Besides, don't you have a laptop or a desktop?"
    show hiroshi worried at Three2 with Dissolve(0.2)
    hk7 "It's under repair for two weeks now.{w} It never woke up just as I was about to insert the device."

    "Oh, how convenient!"

    show hiroshi boredleft at Three2 with Dissolve(0.2)
    hk7 "And this isn't something I can access at any internet café, either. I need time...{w=1.0} and privacy."

    "Pffffffffffttttt... What the?!{w=1.0} Of all people!"

    show hiroshi determined2 at Three2 with Dissolve(0.2)
    hk7 "I know it sounds convenient and ridiculous, but could you stop snickering and understand the situation first?!"
    ai2 "Whoa! Whoa! Easy.{w} It isn't what I think it is?"
    show hiroshi serious at Three2 with Dissolve(0.2)
    hk7 "No.{w=1.0} Along with your polo, bleach your mind on laundry day, please."

    "I lightened up. He didn't.{w} Hiroshi has always been this stoic...{w=1.0} at first.{w} Give him a few minutes and the roles reverse in being the jester."
    "Come on.{w=1.0} Anytime soon.{w=1.0} Show a hint of your teeth, will you?"
    "{cps=10}Hmmmmmmmmmm...{/cps}"
    "I resign."

    ai2 "Fine. You don't need to explain. I understand.{w} I'll let you borrow the workstation for {i}thirty minutes{/i}{w=0.5}, tops!{w} If I ain't back by then, consider me dead."
    show hiroshi determined at Three2 with Dissolve(0.2)
    hk7 "Deal, Mr. Injun Boy."
    ai2 "{cps=15}Ehehehehe... Ehahahahahahaha!!!{/cps}{w} {cps=20}See? That's more like it!{/cps}"
    stop music fadeout 2.0
    ai2 "..."
    ai2 "What did you just call me?!"

    play sound sfx_knock
    show hiroshi smileleft at Three2 with Dissolve(0.2)
    "{i}{b}*knock* *knock* *knock*{/b}{/i}"

    play sound sfx_dooropen
    iy1 "Hey. Black humor aside, isn't it time to go?{w} The rain is tolerable now. Yoshiro and Ayumi have gone home already."
    ai2 "I'll leave it all into your hands. Don't make a mess of things while I'm gone."
    show hiroshi happyblush at Three2 with Dissolve(0.2)
    hk7 "You can count on me.{w} Go on ahead because you'll take a while on the road home."
    ai2 "Well, okay. Just be responsible with how you use that machine."
    hide hiroshi with Dissolve(0.5)

    play sound sfx_rain loop
    scene bg conferenceroom with dissolve
    "I left the workstation to Hiroshi. He was booting up the terminal and taking out a flash drive from his wallet."
    show sayo worried at Eight6 with Dissolve(0.2)
    "Sayo is in the conference room, writing in her journal.{w} It's weird to see her stay behind and do something she could have done at home."
    "I can't blame her. Must be a routine thing."

    show sayo worriedtalk at Eight6 with Dissolve(0.2)
    sr5 "You go on ahead.{w=1.0} I'll keep watch of things while I'm still here. Let me just finish today's entry."
    ai2 "If you say so.{w=1.0} Good night!"
    show sayo smiletalk at Eight6 with Dissolve(0.2)
    sr5 "Have a safe trip home...{w=0.5} you four."
    hide sayo with Dissolve(0.2)

    scene bg msci night rain with dissolve
    window show
    nvl clear
    narr "After giving her a salute (Sayo returned it with an amused look), we left the room in her care."
    narr "Hikaru was sitting at the bench, playing on her smartphone. Mr. Yamamoto seems to be a bit late than usual."
    narr "Ikuko seems to have gone, too. If Ichirou is right, however, then that means she's still here somewhere.{w} Probably upstairs in the faculty room?"

    nvl clear
    narr "Okay! The rain is allowing us to pass through.{w} Just a dash to the terminal and I'll be breezing on the way home.{w} Now, I can remove the smart kid cap and waste myself on the new game dad bought. After that, I can rest,{w=0.5} enjoy the weekend,{w=0.5} and...{w=1.0}{nw}"
    play sound sfx_rumble
    narr "{cps=15}And be bothered by the rumbling within.{/cps}"

    nvl clear
    window hide

    show miyu confused at Eight5 with Dissolve(0.2)
    mh8 "Something wrong?"
    ai2 "{cps=10}Oof...{w=0.5} Ummm...{w=0.5}{/cps} {cps=15}Don't worry about me.{w=1.0} Let's just --{/cps}{nw}"

    play music bg_theanthillganggoeswest loop
    play sound sfx_rumble
    "{b}{i}*GRUMBLE*{/i}{/b}"

    "One step...{w=1.0} There we go.{w=0.5} Take your mind off of it. It's not bothering you. Go home as soon as possible."

    show ichirou confused at Eight2 with Dissolve(0.2)
    iy1 "If you're hungry, we can stop by at 7-11. {i}*snicker*{/i} Looks like your buddy is unusually impatient."
    ai2 "Don't mind me.{w=1.0} Just keep moving, guys. Ehehehe..."

    "To my insistence, we kept pushing forward.{w} I could see, from my peripheral vision, Ichirou and Sumiko occasionally shooting weird glances at each other."
    "{cps=15}Only a few steps to the gate and two blocks to the jeepney terminal...{/cps}{nw}"
    play sound sfx_rumble
    "{b}{i}*crunch*{w=0.5} *GRUMBLE*{/i}{/b}"
    "In the middle of the shower, I stopped.{w=1.0} We stopped."

    show ichirou worried at Eight2 with Dissolve(0.2)
    ai2 "I'm sorry. But can you go on ahead? I can't really hold it in any longer."
    show sumiko serious at Eight4 with Dissolve(0.2)
    st3 "Did you take your anti-motility medicine already? That's the third time since morning...{w=0.5} and you're sweating bullets!"
    ai2 "I forgot to take some with me."
    show sumiko sighclosed at Eight4 with Dissolve(0.2)
    st3 "{cps=8}Oh, for...{/cps}{nw}"

    play sound sfx_smack
    "Facepalm.{w} Already on the way to breaking his personal record of facepalm instances."

    show miyu bored at Eight5 with Dissolve(0.2)
    mh8 "I know this sounds awkward, but did you pack an adult diaper, at least?"
    ai2 "No?"
    show miyu naughty smile at Eight5 with Dissolve(0.2)
    mh8 "Oh! Who would think of bringing such things?{w} Quality baby diapers already cost half a dollar a four-pack. Quadruple that the cost apiece."
    show ichirou smile at Eight2 with Dissolve(0.2)
    ai2 "Would you quit that already?! When I say I'm going, I'm going!"
    stop music

    play sound sfx_whoosh
    hide miyu with hpunch
    hide ichirou
    hide sumiko
    "I broke off from the trio and dashed to the restroom on the other side of the campus."

    play music bg_fullon loop
    mh8 "Hey, Akira! You know we can't just leave you alone!"
    st3 "Come back, you dummy!"

    window show
    nvl clear
    narr "They were screaming at me to slow down.{w} I didn't, already focused on the most urgent goal of the evening."
    stop sound fadeout 3.0
    scene bg mensroom with fade
    narr "I reached the men's bathroom in time.{w} I entered the second-leftmost stall, locked it, and went about my business."
    play sound sfx_footsteps2
    narr "Three sets of footsteps approached the restroom, at least two of them huffing from exhaustion.{w} They stopped by the entrance, presumably sitting at the nearby bench."
    stop music fadeout 2.0

    nvl clear
    window hide

    play sound sfx_breathing
    mh8 "Hey...{w=0.5} Haa...{w=0.5} Haa...{w=0.5} Be done with it quickly. This area is a blind spot.{w} More importantly, the rain will become stronger in the next five minutes."
    ai2 "Five minutes?! Not enough.{w} Give me another five and we'll talk."

    play sound sfx_thunder
    "{b}*THUNDER*{/b}"

    ai2 "GYAH!"
    iy1 "See? It's a no deal."
    iy1 "We'll just sit here at the bench. Give us a yell if a ghost pops its head from the next stall. {i}*snicker*{/i}"
    ai2 "Enough of that pants-soiling tactic, Ichirou."
    st3 "...Which is exactly what you're doing."
    ai2 "Oh. Hahahahahahaha...{w=0.5} Good one."

    window show
    nvl clear
    play sound sfx_waterdrip loop
    narr "They left me alone for quite some time, conversing at the bench while they waited."
    narr "I checked my watch regularly, watching it tick and counting the number of minutes passed.{w} Aside from the occasional thunderclap and constant raining, the next five minutes were peaceful."

    nvl clear
    narr "{cps=12}{color=#bd0000}Hail Mary! Full of grace, the Lord is with thee...{/color}{/cps}"

    nvl clear
    window hide

    ai2 "{b}*WHEEZE*{/b}{w=0.5} HA!{w=0.5} HA!{w=0.5} HA!{w=0.5} Very funny, Ichirou! You're helping me more than scaring me, you know?"
    iy1 "Yes, I know! And I'm gonna keep doing it while you take your sweet time inside.{w} But don't say we're lying when we say the rain is gonna get stronger anytime soon."
    mh8 "Nice job blowing our lead, champ. Hikaru is already on the way home...{w=1.0} {cps=12}Not that it has any value...{/cps}"

    play sound sfx_rain loop
    window show
    nvl clear
    narr "Another five minutes passed.{w=1.0} And they were right.{w} The rain definitely got stronger as forecasted, not to mention the added humiliation I received for wasting their time.{w} {cps=15}If only those horrible incidents never happened...{/cps}"
    narr "Not to be a gossip, but I listened in on their conversation. It helps me feel safe and probably sane from this loneliness.{w} Any chance they would lead to {i}that{/i} topic, they tried to steer clear of it."
    narr "Although, the supernatural enthusiast can't just stop himself from talking, can he?"

    nvl clear
    window hide

    play music bg_nightofchaos loop
    mh8 "{i}Nine little Indians sat up very late;{w=1.0} One overslept himself and then there were Eight.{/i}"
    mh8 "When you think about it in a certain manner, it could very well be any one of us."
    st3 "Isn't that too broad and too large of a target pool, Miyu?"
    mh8 "That's true. I can't think of anyone suffering from insomnia. I haven't gotten close to everybody to know."
    st3 "So if that creepy message is to be taken seriously, our phantom suspect is going after ten people. We already know the identities of at least two."
    mh8 "We can ascertain that the victims of last month's abduction case is part of the ten -- Inoue may or may not be a red herring.{w} Sayo, on the other hand..."
    iy1 "Could be the last."
    st3 "That's probably true."
    iy1 "I was outside with her -- don't know how she suddenly popped up by my side -- when the phantom voice threw the gauntlet down.{w} {cps=12}Student Council President Sayo Ronoroa...{/cps}{w=1.0} {cps=10}Chilling...{/cps}"
    st3 "That's more than enough reason to complete eight hours starting tonight. It's counterintuitive, but if anyone is caught with deep eyebags, you can be sure they are at the hit list."
    mh8 "Hey, Ichirou.{w} When you said \"phantom,\" did nothing strike you when you mentioned that word?"

    "What are they talking about? Is there something I don't know yet?"

    iy1 "That's right. It takes us back to that night.{w} Sumiko, we haven't told this to anybody yet. We may have had a run on with the culprit the night I went for a walk."
    st3 "Why didn't you tell us before? Miyu, you went after him too?"
    mh8 "Not the culprit; rather, I was finding this guy until I found him in the middle of the rice fields.{w} If I didn't find him then, he could very well be dead."
    iy1 "Yeah, it was a very stupid move for me."
    mh8 "I may have mentioned this to you already, Ichirou. Remember when I visited Sanae for her birthday after class?"
    iy1 "I was already on the way home by then. I, Sumiko, and a few others stopped by at 7-11 for a snack.{w} When you mentioned that the day after, it was very creepy. Besides, what reason would I have to go there?"
    mh8 "Right, it's your doppelganger.{w} But if you say so, then that contradicts what I saw. Doppelgangers represent the desire of someone who wants to engage in a certain activity."
    iy1 "You'll find mine odd.{w} Has Yoshiro been wearing speed shoes lately or am I just bad at recognizing faces?"
    st3 "One evening, we saw Yoshiro waiting at the jeepney terminal in front of 7-11. Ichirou, however, attests that he saw Yoshiro leaving with his girlfriend way before we left the campus ourselves."
    mh8 "Oh! There's nothing strange about it. Why such a fuss?"
    st3 "Miyu,{w=1.0} if you've ever been to her house, you know that the time to walk to her house and back does not take less than twenty minutes.{w} When we settled down, Yoshiro was nowhere to be found beforehand."
    mh8 "If you say so. It must be a spiritual double, alright. No big deal."
    stop music

    play sound sfx_thunder
    "{b}*THUNDER*{/b}"
    "I hate it when that happens!"

    scene bg mensroom dark
    play sound sfx_rumble
    "{i}*WHIRR*{w=1.0}{nw}{/i}"
    play sound sfx_spark
    "{i}*WHIRR*{fast} *crackle* *crackle*{/i}"
    stop sound

    scene black with fade
    "JULY 19, 2013 - 1800H"

    scene bg facultyroom with fade
    window show
    nvl clear
    narr "It seems he's sticking to his thirty-minute time limit.{w} I cannot mistake those frantic footsteps from outside for someone else's. Moreover, there are other pairs trailing behind it."
    narr "As for me, I'm only praying this device won't do this computer in, the same way it did to our family desktop. Just praying to God this device isn't cursed or anything."
    play sound sfx_static2
    narr "Sayo tuned in the radio to the primetime news.{w} We shall be expecting a moderate rainshower in the next ten minutes, it seems."

    nvl clear
    window hide
    stop sound fadeout 1.0

    f_sr5 "My, aren't we unlucky? Hope we get home without catching a cold."
    f_hk7 "I hope so.{w} I'm wishing the skies would clear up by Sunday evening. This rain is a nuisance!"
    f_sr5 "I agree."

    play sound sfx_footsteps2
    "For a moment, she went inside the office and searched through the drawers for paperwork, perhaps? Is it really that handful?"

    stop sound fadeout 2.0
    show sayo serioustalk at Three1 with Dissolve(0.2)
    f_sr5 "You know, I suggest you wrap whatever it is you're doing as soon as you can.{w} The power lines are swaying with the wind and are taking a beating from the rain."
    show sayo worriedtalk at Three1 with Dissolve(0.2)
    f_sr5 "By the way, what is it you're doing? A project?"
    f_hk7 "Yes. That's exactly it.{w} Our desktop got busted a few weeks ago so I asked Akira to borrow his station for the moment."
    show sayo worried at Three1 with Dissolve(0.2)
    f_sr5 "I see.{w} Carry on."
    hide sayo with Dissolve(0.2)

    scene bg laptop with dissolve
    window show
    nvl clear
    narr "By the time she returned to the conference room, the computer has finished booting up.{w} In my hands, I held the flash drive Tomonori-san entrusted me with at the hospital."
    narr "{i}Whatever you do, share this to no one.{/i}"
    narr "Those words, pleading and firm, I had to take heed. Otherwise, this whole investigation could turn around in favor of the culprit."

    nvl clear
    window hide

    play sound sfx_dooropen
    f_sr5 "Keep watch of the office if you can, Hiroshi.{w} I'll step out for a moment."

    window show
    nvl clear
    narr "I watched Sayo leave through the door -- affirmative but quite hesitant of my decision to stay behind. Give or take fifteen minutes before she comes back from reporting to Mrs. Genkai."
    narr "Once more, I looked over the division between the workstation and the door."
    narr "She was there.{w=0.5}{nw}"

    window hide
    scene bg conferenceroom
    show sayo creepy smirkpose2 at Three2
    show sayo creepy smirkpose2 at Three2 with Dissolve(2.0)
    hide sayo
    play sound sfx_dooropen
    window show
    nvl clear
    narr "She was there...{fast} staring with that naughty-looking smile -- a split second before the door shut."
    narr "Let her think whatever she wants to, but this is a vital piece of information I'm digging into. I cannot afford anyone else to see it."

    play music bg_ghoststory loop
    scene bg laptop with dissolve
    nvl clear
    narr "The contents of the flash drive consisted of only an MP3 file.{w} Clearly, this was done as a sort of countermeasure, treating it as a boot-up drive so no other files can be saved safely into it.{w} I do hope Emmerich and I are listening to the same file."
    narr "I wore my headphones and clicked the file. A few seconds later, the Media Player opened."
    narr "The Sacred Heart Curse Killings...{w=1.0} She really did look them up.{w} Why didn't she relay her findings to us, though? Although I can't blame her since half of us barely remember it."

    nvl clear
    n_sr5 "Actually, our girl is linked to the curse killings..."
    narr "Really?{w} I thought the guard was just telling a silly ghost story{w=0.5} -- oh, of course!{w} Suzumoto-san did appear on an interview related to Kugimiya Oizumi's death,{w=1.0} about how she's sorry and all."
    narr "Hmmmmmm...{w} What's she talking about?{w=1.0} Enlighten me when I get home, Sayo."

    nvl clear
    n_is4 "Good night, Sayo.{w=1.0} See you tom --{nw}"
    n_sr5 "{cps=12}Sleep tight, dear Inoue.{/cps}"
    n_is4 "That's sweet.{w=-0.5} Now, would you please --{nw}"

    nvl clear
    n_sr5 "{cps=5}Star light...{w=1.0} Star bright...{w=1.0} {i}*hum* *hum* *hum*{/i}{/cps}"
    n_is4 "I need to sleep now, okay?{w=1.0} Bye!"
    play sound sfx_thud2
    "{b}{i}*SLAM*{/i}{/b}"
    n_sr5 "{cps=12}...have the wish{w=1.0} I wish tonight.{w=1.0}{/cps}{nw}"
    play sound sfx_giggle
    n_sr5 "...have the wish I wish tonight.{fast} {cps=20}{i}*giggle* *giggle* *giggle*{/i} Nyehahahahahahaha...{/cps}"
    play sound sfx_hangup
    stop music fadeout 2.0

    nvl clear
    narr "Silence followed after the beep."
    play sound sfx_rain loop
    narr "The sound file's contours ended as a flat line.{w} Normally, I would have closed the file there, but I needed to see how long this goes."
    narr "Dragging the scroll bar to the right, I watched as the line went on,{w=1.0} and on,{w=1.0} and on..."

    nvl clear
    narr "I took the headphones off for a minute{w=0.5} as they were already squeezing my head into a pulp."
    narr "Amidst the light pitter-pattering of the rain, there were people passing by the room. Few of those I recognize.{w} Still, I kept tracing the line."
    narr "It seemed crazy at first, but it was indeed possible.{w} There was a sharp vertical contour hidden far from where the call has ended. I wonder what this is."
    narr "Headphones reworn, I played the file a few seconds before that section."

    nvl clear
    window hide
    stop sound

    play sound sfx_loudbuzz
    scene bg laptop with sshake
    "{b}{i}*RIIIIIIIIIIIIIIIIIIIIINNNNNNGGGGGG*{/i}{/b}"
    c_hk7 "Aaaaaaaaaaaaaaaarrrrrgggghhhh!!!{w=1.0} Damn, that hurts!"
    stop sound fadeout 1.0
    "Stupid prank...{w} My ears are still ringing from whatever crevice of Hell that came from.{w} I did not just say that, did I?"
    play sound sfx_thunder
    "{b}*THUNDER*{/b}"
    
    scene black
    play sound sfx_rumble
    "{i}*WHIRR*{w=1.0}{nw}{/i}"
    play sound sfx_spark
    "{i}*WHIRR*{fast} *crackle* *crackle*{/i}"
    stop sound

    play sound sfx_waterdrip loop
    window show
    nvl clear
    narr "Black.{w=1.0} I became enshrouded in darkness.{w} The rain, or rather, the wind must have caused the outage."
    narr "This can't be good.{w} The storm had taken out the electricity of the entire campus, possibly even the adjacent college's.{w} It's the first of many during the rainy months."

    nvl clear
    narr "I've heard what I needed to hear, so I can just pack up and leave.{w} However, under two conditions it is not yet time for me to commute home."
    narr "First, the downpour is already at its worst tonight."
    narr "Second, there are several classified and possibly sensitive documents in this room.{w} Without the aid of CCTV, I won't have anything to prove my case should anything gets lost."

    play sound sfx_footsteps3 loop
    nvl clear
    narr "Pacing around the room, back and forth,{w=0.5} back and forth,{w=0.5} back and forth...{w} I played with some apps on my half-charged smartphone to alleviate my boredom."
    narr "It makes no difference whether I leave the room or not. There is only one possible entrance to this two-room office space, the hallway door.{w} If I keep my eye on it, my safety is ascertained."
    narr "I have known this situation all too well.{w=1.0} I may be the source of energy among my circle of friends,{w} but the same cannot be said for other places."

    play sound sfx_waterdrip loop
    scene bg conferenceroom dark with dissolve
    nvl clear
    narr "Darkness,{w=0.5} solitude,{w=0.5} ambience --{w=1.0} the few of many ingredients to live the life of a hermit.{w} That was a hyperbole, but there is no perfect definition to describe it. What do people think about introverts, anyway?"
    narr "When you're shut up inside a box with only a few items of your choice,{w=0.5} it restores the balance in a holistic sense.{w} The stillness of my surroundings help me in piecing together the fragments my mind creates.{w} Connections are made,{w=0.5} the bigger picture is constructed,{w=0.5} and the heart restabilizes."
    narr "The feeling of waking up in the morning ready to take the day on?"
    narr "Exactly."

    scene bg msci night rain with dissolve
    nvl clear
    narr "Sure, there is that constant need to plug in my thoughts for further scrutiny. I am not forbidden to speak them through a facet whenever that feeling comes.{w} I would rather not regret anything that may start a destructive ripple."
    narr "The moment of realization only steps in when you feel the effects...{w=1.0} when the waves hit you.{w} There is a blind spot only a few would notice -- sometimes none.{w} It is a truth you would rather avert your eyes from, yet is so unavoidable you must deal with it regardless."
    narr "For instance, the small world of a restroom stall."

    scene bg mensroom dark with dissolve
    nvl clear
    narr "The magic sets in as soon as you lock the door and settle down.{w} Take a moment and augment your senses.{w=1.0} {cps=15}What do you hear,{w=0.5} smell,{w=0.5} and feel?{w=1.0} Do you see anything?{/cps}"
    narr "{cps=20}It could be a momentary reprieve.{w=1.0} You feel that nobody is there, judging you of your actions and leaving you free to do whatever you please.{w=1.0} Only the rainfall,{w=0.5} the occasional thunder,{w=0.5} and the howling wind are registered by your senses.{/cps}"
    narr "{cps=15}It could be the onset of negativity.{w=1.0} What you would normally ignore, manifests itself in front of you...{w=1.0} all around you.{w=1.0}{/cps} {cps=10}The sound of footsteps louden,{/cps}{w=0.5} {cps=10}the sound of breathing become distinct from the wind,{/cps}{w=0.5} {cps=10}and the feeling you are being watched...{w=1.0} your own weaknesses loom over you like a shadow.{/cps}"
    narr "{cps=12}A shadow you can see...{w=0.5} but can never touch...{/cps}"

    nvl clear
    window hide

    f_ai2 "{cps=8}Guys...{/cps}{w=0.5} {cps=12}are you still there?{/cps}{w=1.0} {cps=15}Answer me, come on!{/cps}"

    scene bg mensroom nightmare with dissolve
    window show
    nvl clear
    narr "{cps=20}You call for help, yet there is no answer.{w=0.5} Is there any reason why?{w=0.5} Where there is one, there is oftentimes none.{/cps}"
    narr "{cps=15}Just when you thought there is none, only does the problem rear itself at its nastiest.{/cps}"
    narr "{cps=15}The upliftment was a {i}lie{/i}...{w=1.0} Things must not go awry...{/cps}"
    stop music fadeout 2.0

    nvl clear
    window hide

    play sound sfx_rattle loop
    "{i}*rattle* *rattle* *rattle*{/i}"

    f_ai2 "Not funny, guys!{w=1.0} Anyone!{w=0.5} Ichirou, Sumiko, Miyu...{w=0.5} If I see you three behind this, you'll be having a crown knuckle coming for you. My treat, Akira Ichibana special!"
    stop sound

    play sound sfx_creepylaugh loop
    cen "{i}{cps=15}Hehehehehehehehe...{/cps}{w=0.5}\n{space=15}{cps=15}Kukukukukuhahahahaha...{/cps}{w=0.5}\n{space=30}{cps=15}Kyekyekyekyehihihihihihihi...{/cps}{/i}{w=1.0}{nw}"
    stop sound fadeout 5.0

    play music sfx_heartbeat loop
    window show
    nvl clear
    narr "{cps=15}In this enclosed space, it is only your intellect and your conscience fighting against each other.{w=1.0} The hot and cold fronts work to form these isolated thoughts and emotions.{/cps}"
    narr "{cps=15}When chaos escalates instead of the intended balance, there are two ways to hope for a last-minute restoration.{/cps}"
    narr "{cps=12}First,{w=0.5} allow sheep to pervade the thoughts and count as they pass the waist-high fence.{/cps}"

    nvl clear
    play sound sfx_clang
    narr "{i}{cps=10}One... Two... Three... Hah...{/cps}{/i}{w=1.0}{nw}"
    play sound sfx_clang
    narr "{i}{cps=10}Four... Five... Six... Hah...{/cps}{/i}{w=1.0}{nw}"
    play sound sfx_clang
    narr "{i}{cps=10}Seven... Eight... Nine...{/cps}{/i}{w=1.0}{nw}"
    play sound sfx_clang
    narr "{i}{cps=10}Ten...{/cps}{w=1.0}{nw}{/i}"

    nvl clear
    narr "{cps=15}Second,{w=0.5} if all else fails, in whatever manner appropriate for the situation...{/cps}{w=1.0} {cps=10}scream...{/cps}"
    play sound sfx_splatter
    narr "{cps=10}I can't scream...{/cps}{w=1.0} {cps=5}Help...{/cps}"
    stop music

    nvl clear
    window hide

    play sound sfx_clang
    scene bg mensroom nightmare with vpunch
    "{b}{i}*SLAM*{/i}{/b}"

    f_iy1 "Whoa! What the fudge happened inside?"

    show akira creepy angry at Three2 with Dissolve(1.0)
    play sound sfx_heartbeat loop
    "..."

    r_ai2 "{cps=15}I know you, Ichirou.{w=1.0} And I've already warned you enough times.{w=1.0} You didn't listen to me.{/cps}"

    play sound sfx_footsteps3
    "{i}*step*{w=1.0} *step*{/i}"
    play sound sfx_heartbeat loop

    f_iy1 "Hey! That ghost in the restroom story was just made up. Bursting out of the stall scared the heck out of us, you know?"
    play sound sfx_fistbang
    show akira creepy angryscream at Three2 with vpunch
    r_ai2 "Do you think this is funny? You could've killed me through a heart attack!"

    show akira creepy angry2 at Three2
    play sound sfx_footsteps3
    "{i}*step*{w=1.0} *step*{/i}"
    play sound sfx_heartbeat loop

    f_mh8 "Don't come any closer, Akira. Stay where you are!"
    f_st3 "You're agitated, Akira.{w} Take a few deep breaths...{w=0.5} enjoy the soothing sound of the rain."
    f_st3 "I know you're scared. We all are.{w} Take a moment to recover before you decide to use that fist of yours."
    stop sound fadeout 2.0

    show akira annoyedclosed at Three2 with Dissolve(0.5)
    "Okay...{w=0.5} Okay...{w=0.5} Sumiko is right.{w} Things will only get worse if I deliver them the goods. Everything should be fine. I'm no longer alone."

    scene bg mensroom dark
    show akira annoyedclosed at Three2
    show akira annoyedclosed at Three2 with Dissolve(0.5)
    show akira fangblush at Three2 with Dissolve(0.2)
    f_ai2 "Ah. Ahehehehe...{w} Why don't we just call this a night an meet again on Monday? Shall we scurry along?"
    show ichirou worried at Eight7 with Dissolve(0.2)
    f_iy1 "Much better, dude. I thought you were going to bash my head to the floor for sure!"
    show sumiko seriousleft at Eight2 with Dissolve(0.2)
    f_st3 "That reminds me. Don't you have some errand to attend to?"
    show akira surprised2 at Three2 with Dissolve(0.2)
    f_ai2 "What errand? I have nothing on the backlog."
    show sumiko surprised2 at Eight2 with Dissolve(0.2)
    f_st3 "No, it's not an errand. It's called something else. I must have confused yours with Sayo's.{w} What was it again?"
    f_mh8 "Check if Hiroshi is done with his task."
    show akira smirk at Three2 with Dissolve(0.2)
    f_ai2 "Right! To the council room, then. If we dilly-dally, the rainshower might strand us for another thirty minutes."

    scene bg msci night rain with dissolve
    play sound sfx_rain loop
    "Armed with only phone flashlights, we made our way back towards the Student Council's office.{w} The clock read 6:30 PM, exactly at the end of Hiroshi's deadline."
    show sayo blankface at Three3 with Dissolve(0.2)
    "Just as we approached the door, Sayo emerged from the stairs. She was already gripping the door knob when she noticed us."

    show sayo normaltalk at Three3 with Dissolve(0.2)
    f_sr5 "Oh! You boys still here? I thought you already went ahead."
    show akira surprised at Three1 with Dissolve(0.2)
    f_ai2 "Well, you know...{w=0.5} Complications arose and we -- I had to deal with it."
    show sayo smiletalk at Three3 with Dissolve(0.2)
    f_sr5 "I understand. Just be sure you can make it all the way home without making a mess, Akira."
    stop sound fadeout 1.0

    play music sfx_rain
    play sound sfx_dooropen
    hide sayo with Dissolve(0.2)
    hide akira with Dissolve(0.2)
    scene bg conferenceroom dark with dissolve
    "When she opened the door, the void greeted us, anything barely visible beyond three feet.{w} Sayo went to the other end of the table, wore her backpack, and waited by the door."

    f_sr5 "I hope Hiroshi was done before the power outage. He might have gone already.{w} Akira, if you're done checking your workstation, we may leave."
    f_ai2 "What you said is half true, Pres. We aren't the only ones leaving this room soon."
    f_iy1 "You can navigate around the office without a flashlight?! Wow! Need me to shine on you?"
    f_ai2 "It's alright! I got this.{w} Just need a good shove to wake this lazybone up."

    window show
    nvl clear
    narr "Hiroshi was doing his thinking regimen again, dozing off as usual whenever he does this.{w} I remember in Junior Year we devised several methods just to wake this guy up. We even almost soaked him with ice water just to open his eyelids, for goodness' sake!"
    narr "And our sneaky boy here had been doing some {i}very naughty{/i} things with my workstation.{w} There's a substantial amount of fluid on his finger.{w=1.0} Sticky...{w=0.5} and disgusting."
    play sound sfx_thud
    narr "I nudged him, hoping he'll snap out of his trance."

    nvl clear
    window hide

    f_ai2 "Hey, Hiroshi. What did I tell you right before I let you work on my computer? I was right, wasn't I?"
    f_sr5 "Hmmm... Looks like I should make a note of that."
    f_ai2 "Hey, did you hear that? Well, well, you're in trouble now, you little devil! Perhaps you ought to wipe away your gunk so we can lighten your sentence."

    stop music fadeout 2.0
    play sound sfx_spark
    scene bg conferenceroom
    "{i}*crackle* *WHIRR*{/i}"
    stop sound

    "\"Yes! Finally!\""

    scene bg facultyroom with dissolve
    show akira smile at Three3 with Dissolve(0.2)
    "Exactly my sentiments.{w} The lights are back on as well as the air conditioning unit. Turning on the generator took a bit longer than expected."

    f_sr5 "Thanks, Onifuchi-san!"

    "Now that the pleasantries are out of the way, let's see what sight beholds us toni --{nw}"

    scene bg conferenceroom
    show miyu serious at Three3 with vpunch
    show ichirou serious at Three1
    f_ai2 "WHAT THE HELL???"
    hide miyu with Dissolve(0.2)
    f_mh8 "What's with the expletives?!{w=1.0}{nw}"
    play music bg_roadtohell
    f_mh8 "{b}*GASP*{/b}{w=1.0} {cps=10}Hiroshi... You didn't...{/cps}"

    scene bg blood with dissolve
    window show
    nvl clear
    narr "Perhaps my bladder is raring to go for a fourth round, but the case is different this time.{w} Sitting on my chair is Hiroshi.{w=1.0} Surely, there can be no doubt...{w=0.5} it's him."
    narr "His head was tilted towards his spine, his eyes wide open from shock, and his mouth and neck bound tightly with masking tape. Both his hands were on the table.{w} More accurately, only the base remained attached to his arm -- the digits were scattered across the keyboard."
    scene bg blood2 with sshake
    narr "What I touched was Hiroshi's blood!"

    nvl clear
    window hide

    scene bg conferenceroom with dissolve
    show sayo worriedtalkcry at Three2 with Dissolve(0.2)
    f_sr5 "Good Lord! {i}*hic*{/i}{w=1.0} {cps=15}Of all the people...{w=0.5} Of all the places this could have happened...!{/cps}"
    show ikuko worried at Three1 with Dissolve(0.2)
    ikuko "Sayo-chan! What has happened here?"
    show ikuko worried at Three3 with Dissolve(0.2)
    show ikuko shocked at Three3 with Dissolve(1.0)
    show ikuko shockedtears at Three1 with Dissolve(0.5)

    window show
    nvl clear
    narr "I directed her towards the office, and Ikuko immediately averted her eyes from Hiroshi's corpse. Instead, she and Sayo comforted each other.{w} Ichirou had run to the guard to call the police."
    scene bg blood with dissolve
    narr "The flash drive Hiroshi inserted into the computer was no longer in the port. We can't search the body without proper consent.{w} There is, however, one more spot of interest."
    narr "On the table right next to a puddle, with one of its letters ending on the tip of Hiroshi's left index finger, reads..."
    narr "{color=#bd0000}{i}The mind only stops when the body does,{w=1.0}\nThe roulette's outcome, indeed, is a loss.{/i}{/color}"

    nvl clear
    narr "If I remember Miyu, Ichirou, and Yoshiro's stories correctly, there should be {i}something else{/i} that can confirm our suspicions.{w} I turned his hands over and opened his palms."
    narr "Number {color=#bd0000}7{/color} on the left,{w=0.5} number {color=#bd0000}10{/color} on the right, etched with probably the same knife used to chop Hiroshi's fingers."
    narr "We found him,{w=1.0} and within a short period of time,{w=1.0} reality has transformed itself into a scenario we thought would only remain our dreams...{w=1.0}{nw}"
    stop music fadeout 3.0
    scene black with fade
    narr "{cps=12}...A waking nightmare.{/cps}"

    nvl clear
    window hide

    return

label ch02_14_investigation:
    scene black with fade
    "JULY 20, 2013 - 0730H"

    scene bg interrogationroom with fade
    play music bg_decline loop
    window show
    nvl clear
    narr "It was still fresh in our minds.{w=1.0} The memories linger and have yet to disturb our sleep."
    narr "Despite all the efforts we made in suppressing that horrifying reality, we can never deny it.{w} Kyou Kirisaki and Hiroshi Kano were killed by the same culprit,{w=1.0} an unknown specter whom we know nothing about."
    narr "As our numbers dwindle, so does the chances we have in learning the truth.{w=1.0} Inoue may be our only chance for now."

    nvl clear
    narr "We secured the crime scene for fifteen muntes until the police arrived.{w} Inspector Emmerich called the six of us who witnessed the body -- myself, Akira, Miyu, Ichirou, Sumiko, and Ikuko."
    narr "After informing our parents of our whereabouts and the reason why, he led us down to the basement. We were being questioned individually at the interrogation room.{w} I was first, as the last person to see him alive."

    nvl clear
    window hide

    show emmerich serious at Three3 with Dissolve(0.2)
    p_emm "You said he was working on a project before the power outage. Did you not check on him after that?"
    show sayo worried at Three1 with Dissolve(0.2)
    d_sr5 "Not exactly, Inspector.{w} At 6:15, moments before the blackout, I was in the faculty room discussing with our adviser. We were looking at a possible extension for our review sessions we held last week. Ikuko accompanied me, if I recall."
    d_sr5 "I've forgotten some papers at the office, so I headed back there to retrieve them."
    show sayo worriedtalk at Three1 with Dissolve(0.2)
    d_sr5 "As soon as I stepped out to the hallway, the electricity went out.{w} I asked Onifuchi-san, the front desk guard, if it can be restored by restarting the generator."
    show emmerich seriousclosed at Three3 with Dissolve(0.2)
    p_emm "That explains why we couldn't get a live feed of the school for fifteen minutes.{w=1.0} And then?"
    d_sr5 "As I went inside the office, I left the door open and searched through the file cabinet with my phone light. Hiroshi was still there, medidating while waiting for the rain to subside."
    show emmerich serious2 at Three3 with Dissolve(0.2)
    p_emm "Does he do this often?"
    show sayo worried at Three1 with Dissolve(0.2)
    d_sr5 "Sometime after First Year. I'm still clueless as to why he didn't go home afterwards."
    show emmerich serious2left at Three3 with Dissolve(0.2)
    p_emm "Did you notice anything off? Like, something that felt out of place?"
    show sayo worriedtalk at Three1 with Dissolve(0.2)
    d_sr5 "No.{w=0.5} If there was another visitor, the camera feeds would have picked them up. I even asked him if everything was alright and he responded normally. I closed the door as I left."
    show emmerich serious at Three3 with Dissolve(0.2)
    p_emm "But then that would mean opening the doorknob before entering the office. There were no signs of a struggle except on your auditor's workstation. Are you sure he did not hear that?"
    show sayo worried at Three1 with Dissolve(0.2)
    d_sr5 "It is all one big mystery, Inspector."
    hide sayo with Dissolve(0.2)
    hide emmerich with Dissolve(0.2)
    stop music fadeout 2.0

    "After a few more clarifications, he let me go and asked me to call the next witness."
    "Each took at least fifteen minutes to finish depending on their degree of involvement with Hiroshi.{w} We exchanged stories while waiting. I wrote on my journal after two more went inside."

    play sound sfx_pageturn
    scene bg book with fade
    play music bg_vulcan loop
    window show
    nvl clear
    narr "{i}July 20, 2013{/i}"
    play sound sfx_pencilwriting
    narr "{i}Thirteen hours have passed since the time of Hiroshi's murder.{/i}"
    narr "{i}Emmerich has excused us to cooperate in their investigation. Not to lose faith in our policemen, but this is already the second murder involving an MSCI student... and our batchmate, no less!{/i}"
    narr "{i}This is also the second time the culprit has branded their victim with a pair of numbers. What could they mean? Surely, neither of those represented an Indian Boy -- in relation to that sabotage by the same perpetrator. Though, Kyou's definitely matched the order. Are they trying to replicate the series of incidents two years ago?{/i}"

    nvl clear
    narr "{i}Let me assess the situation from the first sign of danger -- the mock exams.{/i}"
    narr "{i}I kept the countdown file within the council members. Not even the teachers nor the club officers have a copy. All of us swear that the only content in the flash drive as a sound file. It contains a digital countdown, synchronizing the start time and checkpoints for the entire duration of the test.{/i}"
    narr "{i}I, the voice in the countdown file, would announce how many minutes remaining until the end of a test section. After that, I would instruct everyone to move on to the next section.{/i}"
    narr "{i}What I don't get is, even as Ms. Harada and Mrs. Genkai have attested to it, how somebody managed to insert such a disturbing clip just to incite fear among the Seniors. They could have tampered with it, which we have already disproved during the post-evaluation. Maybe they made a duplicate? If that's true, they did an excellent job replicating even the anti-forgery seals tapes onto the device.{/i}"
    narr "{i}Ah, but what interest is there pondering upon such a minor predicament? At best, it might just lead us to the culprit's identity. For now, the heart lies in the hour of the crime.{/i}"

    nvl clear
    narr "{i}Yet again, another near-impossible mystery is in our hands, right on top of the ongoing case. Though I am a suspect, I am confident about my actions and aware of my surroundings to the best of my abilities.{/i}"
    narr "{i}How about the others? Ikuko, I can vouch for her. The four boys... what are their stories, I wonder? Ask them and they would essentially tell the same story at its core.{/i}"
    narr "{i}Akira was a blind man the entire time, relying mainly on what he heard while doing his business. What happened outside, he only learns after the fact. He was uncharacteristically dreadful, most probably as the one closest to the body. He mentioned about something stalking him from the shadows and seeing apparitions at various times, even mentioning about doppelgangers.{/i}"
    narr "{i}Our eyes rarely met during our conversation, darting around in random places as he spoke. It makes him look like a liar, but I believe his story fully.{/i}"
    narr "{i}Ichirou eneded up scaring Akira when he pulled the restroom ghost trick on him. Last night, it was the first time Ichirou saw him genuinely infuriated, ready to assault him had Sumiko and Miyu not intervened.{/i}"

    nvl clear
    narr "{i}The devil, while Akira was in the interrogation room, admitted to leading the prank. Miyu went around to the small window next to the boys' restroom to assist in the act. Sumiko remained at the bench and recorded the entire ordeal. They regretted it afterwards, though. It showed in the tone of their voice.{/i}"
    narr "{i}It would not be long before Emmerich has finished questioning everyone and leave us to our normal lives. \"Normal\" is such a big word.{/i}"
    narr "{i}While I wish for Inoue's fast recovery, I can already tell how she would feel and react. Her mind's fog would thicken, her family's disdain against me would worsen, and...{/i}"
    narr "{i}I elect to write nothing further. Allow me a few more words so I may rest.{/i}"

    nvl clear
    narr "{i}After that incident, sometimes I ask myself, \"What have I done?\" More appropriately, \"What have WE done?\"{/i}"
    narr "{i}May Hiroshi's soul find his reprieve just Kyou's did.{/i}"
    narr "{i}'Til I ramble again,{w=1.0}\nSayo Ronoroa{/i}"

    nvl clear
    narr "I bound the journal and replaced it into my backback.{w} Akira was done exactly as I finished writing."
    stop music fadeout 2.0
    scene bg park with dissolve
    play sound sfx_chirp loop
    narr "By the time we returned to the surface, our parents were anxiously waiting for us.{w} My mother brought me a cheesecake slice for breakfast, although I kindly refused."
    narr "I do not want food.{w=1.0} I want sleep.{w=1.0} I need to rest."
    stop sound

    nvl clear
    window hide

    return

label ch02_15_facts4:
    scene black with fade
    "JULY 21, 2013 - 1850H"

    play sound sfx_handbell
    scene bg church with fade
    play music bg_regrouping loop
    window show
    nvl clear
    narr "My sisters and I waited as my parents were receiving Communion.{w=0.5} Four long queues of sheep on the middle lane and the side aisles of the church and we just broke off from the crowd."
    narr "I managed to sneak in a quick peek at Facebook since I had data.{w} Aside from the usual notifications, I had three unread messages -- two from group chats."

    nvl clear
    narr "First one is from the IV-B group chat."
    narr "Some of my classmates asked about the details of Hiroshi's funeral. Others asked about what happened last Friday.{w} Despite my obligations as the class president -- answering their queries whenever they raised one -- I ignored them.{w} They won't accept \"police orders\" as an answer, not especially after what happened with Kyou and Inoue."
    narr "Second is from the Science Club executive council."
    narr "For the second time this year, and within a month, we are left without a leader.{w=1.0} And it is all due to death.{w=1.0} Unbelievable!{w} It would've been fine if they were by resignation or by impeachment.{w} Thus, I don't plan on replacing Hiroshi even if they were offering me the position. I wouldn't last long if that was the case."

    nvl clear
    narr "The last is a private message from Miyu."
    n_mh8 "Ichi, please talk to me after Mass. There's something I need to tell you.{fast}"
    narr "For what?{w} Not bemused by the slightest, I made a quick reply as our parents were already on the way back."
    n_iy1 "Maybe tomorrow. We have a family dinner tonight. Sorry.{fast}"

    nvl clear
    narr "Afterwards, I kept my phone inside my pocket.{w} The celebrant proceeded with the rest of the Mass shortly after."
    scene bg diningroom with fade
    narr "Until the end of the Mass and throughout the entirety of the family dinner, I did not check my notifications no matter how tempting it may be. I made that rule to myself, enjoying the moment in this generation of social media prevalence.{w} I enjoyed dinner as best as I can, even though my family is aware how bad the previous two days were affecting me."
    stop music fadeout 2.0

    play sound sfx_dooropen
    scene bg bedroom with dissolve
    nvl clear
    narr "By ten o' clock, I settled down at my bed and prepared what I need for tomorrow. Only then I logged in to Facebook, my Inbox flooded with more messages than usual."
    narr "What the hell...?"
    narr "It wasn't from the IV-B or SciClub GC, but a new group chat formed just this late afternoon.{w} There were six other members: Sumiko, Akira, Yoshiro, Hikaru, Miyu, and Sayo. Some of them privately messaged me shortly after Miyu did."

    nvl clear
    n_ys6 "Ichirou, reply ASAP. Did you get one, too?{fast}"
    narr "I back read to the first message, timestamped 5:28 PM."
    n_sr5 "Hi, everyone. If you're curious as to what this GC is for, then... welcome? Hikaru and Yoshiro messaged me earlier, asking if I received a letter similar to theirs.{fast}"
    narr "Letter? Why are you all so worked up about a harmless letter?"

    nvl clear
    window hide

    play sound sfx_dooropen
    mr_yok "Ichi, there's an envelope here addressed to you. The seal is still intact. You might want to check it out later."
    play sound sfx_pageturn
    iy1 "Thanks, pops."

    "So this is what they're talking about. I wonder what's inside."
    "{i}*crunch* *crackle*{/i}"

    scene bg envelopefour with fade
    window show
    nvl clear
    narr "The parchment gave off a sweet spearmint-like fragrance. I could smell this all day!{w=0.5} Whoever sent this didn't need to spend this much for a measly letter."
    scene bg letter a with fade
    narr "{cps=15}{i}Every month is divided into two halves --{w=1.0} the former where you can ease yourselves,{w=0.5} and the latter where the amusement is.{/i}{/cps}"
    narr "This is what is written on the paper.{w=1.0} I'm not sure what it means myself, but perhaps they can clarify it for me.{w} At the backside is a circle with ten dots around the circumference.{w=1.0} Two letters at the center: S and R."
    scene bg bedroom with fade
    narr "I relayed its contents to the GC. While I waited, I continued reading through the chat."

    nvl clear
    n_sr5 "From what I can tell, the sender seems to be running a network of sorts. For what reason, I cannot say. It seems that the mail I received is only a fragment.{fast}"
    n_sr5 "{cps=15}{i}There are ten chosen people.{w=1.0} Whoever they are, you will find out soon if have not already.{/i}{/cps}"
    n_sr5 "End of letter. As of this time, we are three. Hikaru, Yoshiro, and anybody who received a similar letter, please share the contents in the chat. We need to discuss this puzzle of sorts.{fast}"
    
    nvl clear
    n_hy10 "That's right. Mine was pretty vague in meaning. I wonder what this means.{fast}"
    n_hy10 "{cps=15}{i}The period and the scope are final.{w=1.0} No bargaining allowed.{/i}{/cps}"
    n_ys6 "{cps=15}{i}I permit you to do my work for me.{w=1.0} However, it is in my discretion to postpone the event for the month or to choose a replacement.{/i}{/cps}"
    n_hy10 "Is this a game? What are the prizes, I wonder? Is it a cruise-for-three? Oh my! I wish it is!{fast}"
    n_ys6 "Ooooorrr... This could be the work of a good-humored individual. Maybe a promotion for a college scholarship? Maybe a recruitment strategy by a spy agency? Either case, I'm not surprised.{fast}"

    nvl clear
    narr "From 5:50 PM onwards, more people gradually joined the chat.{fast}"
    n_ai2 "If you guys find your letters amusing or funny, mine didn't sound as cheerful. Have a look.{fast}"
    n_ai2 "{cps=15}{i}No two people are alike. Do no bother finding the pattern as it is useless.{w=1.0} There is, however, one way to find out if it is my own doing.{/i}{/cps}"
    play sound sfx_beep3
    narr "The bell chimed, but I chose to continue reading."

    play music bg_decisions loop
    nvl clear
    narr "At this point, the tone of the conversation shifted completely.{fast}"
    play sound sfx_beep3
    n_sr5 "For goodness' sake... That can only mean one thing.{fast}"
    n_ai2 "Yes. I thought for sure I was the only one. If Yoshiro hadn't messaged me...{fast}"
    play sound sfx_beep3
    n_hy10 "Guys, I've messaged Miyu and am composing one for Inoue.{fast}"
    n_ys6 "Don't!{fast}"
    play sound sfx_beep3
    n_hy10 "Why?{fast}"

    nvl clear
    n_ys6 "We don't have a whole picture of everything yet. It's best if we keep Inoue in the dark for now. As it stands, we are bound to make some wrong assumptions.{fast}"
    n_hy10 "But I sent the message.{fast}"
    play sound sfx_beep3
    n_ys6 "Oh... no...{fast}"
    play sound sfx_beep3
    n_sr5 "Take it easy, Yoshiro. I'm sure Hikaru is smart enough to choose her words in this situation.{fast}"

    nvl clear
    n_mh8 "Hikaru, is this the chat?{fast}"
    play sound sfx_beep3
    n_hy10 "Yep.{fast}"
    play sound sfx_beep3
    n_mh8 "{cps=15}{i}Can you trust what you see, feel, and her with your senses?{/i}{/cps}"
    play sound sfx_beep3
    narr "The GC chimed in almost quick succession.{w} I fought the urge to skip ahead and read their replies."

    nvl clear
    play sound sfx_beep3
    n_hy10 "What a buzzkill! I thought for sure this whole setup was a life-changing lottery or something like that. We've been had the whole time!{fast}"
    n_mh8 "Not exactly. Besides, what lottery would send something cryptic for its potential contestants? This is too weird or too philosophical to be a standard preliminary question. I imagine laymen sniding at this.{fast}"
    play sound sfx_beep3
    n_ai2 "Can we trust our senses, though? I think not! Hahahahahaha! Whoever sent this must have a sense of humor from the 22nd century.{fast}"
    play sound sfx_beep3
    n_st3 "If you can still laugh your butt off after I share mine, maybe you ought to reconsider.{fast}"
    play sound sfx_beep3
    n_st3 "{cps=15}{i}My identity is your responsibility.{w=1.0} Even if all of this shall come to pass, I shall forever be enshrouded in mystery.{/i}{/cps}"

    nvl clear
    play sound sfx_beep3
    n_ai2 "These are not too unfamiliar words from a certain someone. The one named, \"He-Who-Must-Never-Name-Himself.\"{fast}"
    play sound sfx_beep3
    n_ys6 "See, Hikaru? Now, you know why you shouldn't have sent that message.{fast}"
    play sound sfx_beep3
    n_hy10 "I'm sorry, okay? Just like what Sayo said, I didn't tell her everything.{fast}"
    n_ys6 "What did you tell her?{fast}"
    n_hy10 "I asked her if she received a letter, plain and simple. I told her it could be a scholarship grant of sorts. She received nothing.{fast}"
    n_ys6 "I guess it's my turn to say sorry.{fast}"

    nvl clear
    narr "The rest of the conversation contained theories about the meaning of these letters, who sent them, and how we were chosen.{w} We already have a rough idea on the second point, thanks to Yoshiro and Akira's ideas."
    narr "I skipped to the latest messages -- the ones after mine."
    play sound sfx_beep3
    n_sr5 "There's your answer, Akira. I didn't want to share my guess in case I was wrong. You were feeling a bit shaken when you asked me before.{fast}"
    play sound sfx_beep3
    n_ai2 "Yeah. I think everyone would agree.{fast}"
    play sound sfx_beep3
    stop music
    n_sr5 "The seven Little Indians are, indeed, us -- everyone in this GC.{fast}"

    play music bg_hazydisorientation loop
    nvl clear
    narr "My heart sank.{w=1.0} I almost dropped my phone on my face and I could barely move after Sayo's declaration."
    narr "From the messages in the GC as well as the contents of the mail we received, I came to a few conclusions."
    narr "One of them is this:{w=0.5} the culprit.{w=1.0} The embodiment of the mysterious voice is someone who knows {i}who{/i} we are. Maybe even where we live, but the exact depth I cannot even begin to describe."
    narr "We have compiled seven letters, yet somehow we don't have all of the pieces yet.{w} If we were to subtract Kyou and Inoue from the equation, this leaves us with the obvious choice."

    nvl clear
    play sound sfx_beep3
    n_hy10 "Did Inoue receive one, too?{fast}"
    play sound sfx_beep3
    n_sr5 "Either she didn't or she will soon. I reckon the eighth letter won't reach her until she's discharged from the hospital. I'm told her ward is under heavy surveillance from the police.{fast}"
    play sound sfx_beep3
    n_st3 "Maybe that inspector has it? It's the only logical end I can come up with.{fast}"
    play sound sfx_beep3
    n_sr5 "Inspector Emmerich?{fast}"
    play sound sfx_beep3
    n_sr5 "That reminds me, I'll ring him up tomorrow to collect our letters. If you analyze the seven letters individually, they either mean nonsense or various unrelated ideas. If they were to be read collectively in a certain manner, you have a set of threat letters.{fast}"

    nvl clear
    play sound sfx_beep3
    n_hy10 "Miyu's probably asleep right now. I'll text him to bring the letter so we can submit ours as evidence.{fast}"
    play sound sfx_beep3
    n_st3 "I'll do it. Shall I meet you break time at IV-E, Sayo?{fast}"
    play sound sfx_beep3
    n_sr5 "I expect to receive six letters, not including mine. Ichirou, bring yours, too.{fast}"
    n_iy1 "Will do. Night."
    stop music fadeout 2.0

    nvl clear
    scene black with fade
    narr "I logged out of Facebook and shut my eyes."
    narr "{cps=12}I wonder what tomorrow brings...{w=0.5} what the following months will bring?{w=0.5} I'm fairly sure the others are thinking the same thing.{/cps}"

    nvl clear
    centered "{cps=10}{i}Is there truly no way out but death?{/i}{/cps}"

    nvl clear
    window hide

    return

label ch02_16_suspicions:
    scene black with fade
    "JULY 24, 2013 - 0900H"

    scene bg msci with fade
    play music bg_regrouping loop
    window show
    nvl clear
    narr "Two days passed by. The school was notably much more peaceful than around the time the abductions took place."
    narr "The witnesses, the Student Council, the school faculty and staff, the police, and Hiroshi's family agreed to keep the crime a secret. But for how long?{w} Long enough for Emmerich to complete his analysis. Long enough before Inoue returns in time for the first quarter examinations."
    narr "Sayo gathered the letters at break time on the 22nd.{w=1.0} Emmerich arrived to collect them after classes ended, 5 PM."
    narr "Unlike what Sayo and company expected, the police had intercepted no such letter.{w} Thus, they decided to wait,{w=0.5} either until the analysis finishes or the eighth letter arrives."
    narr "By early morning on the 23rd, Emmerich's initial findings were relayed to Sayo.{w} Although he managed to piece the meaning together, without the eighth letter the true meaning is still incomplete.{w=1.0} In exchange, Emmerich offered protection for the seven recipients. He understood that one of them --{w=0.5} including Inoue --{w=0.5} would be targeted next."

    scene bg classroom2 with fade
    nvl clear    
    narr "Hiroshi's classmates began to notice his unusual three-day absence.{w} Ichirou, already pressured from the elaborate lie he fabricated regarding the matter, looked unfocused during their classes."
    narr "The same could be said for Sumiko.{w} At least half of IV-C, having been former classmates with Hiroshi, also took notice.{w} It was more difficult.{w=0.5} Akira had lost his chipper, traumatized at the aftermath of the crime. Miyu, Yoshiro, and Hikaru less considerably so."
    show sayo blankface at Three3 with Dissolve(0.2)
    narr "Sayo took longer between helpings of her homemade macaroni salad than usual.{w} A lot of thoughts ran through her head --{w=1.0} the letters,{w=0.5} how long would their cover-up last,{w=0.5} Inoue's safety,{w=0.5} their safety..."

    nvl clear
    window hide

    scene bg classroom1
    play sound sfx_knock
    "{i}*knock* *knock* *knock*{/i}"

    show ayumi smile at Three1 with Dissolve(0.2)
    ayumi "Good morning, Mrs. Genkai."
    t_gen "Lovely morning to you, Ayumi.{w=1.0} Is Sayo inside--{nw}"
    stop music fadeout 2.0
    t_gen "Sayo-chan! Come with me to the office.{w=1.0} This is an important {i}matter{/i} you need to deal with."
    hide ayumi with Dissolve(0.2)

    show sayo normaltalk at Three3 with Dissolve(0.5)
    hide sayo with Dissolve(0.2)
    "Her eyes glinted in anticipation, already knowing what Mrs. Genkai referred to.{w} She excused herself and paced quickly with Mrs. Genkai to the principal's office."
    scene bg classroom2 with dissolve
    show miyu confused at Three1 with Dissolve(0.2)
    "Miyu, having no intention to eat, watched people as they walked past the window."
    show miyu bored at Three2 with Dissolve(0.2)
    show yoshiro worriedleft at Three3 with Dissolve(0.2)
    "He caught a glimpse of Sayo and Mrs. Genkai moving towards the right.{w} He shifted his position to the empty seat beside Yoshiro and tapped him while he was solving with his cube."

    mh8 "Just saw Sayo and Mrs. Genkai moving to the principal's office.{w=1.0} Looks like Inspector E. had paid us a visit."

    show yoshiro serious at Three3 with Dissolve(0.2)
    show akira smile at Three1 with Dissolve(0.2)
    "Yoshiro placed his cube down and signaled Akira to move closer. Without Sumiko and Hikaru, both of whom were absent from the room, they began the conversation."

    play music bg_decisions loop
    ys6 "Any guess on what Inoue's letter contains? I already have a hypothesis, and it possibly coincides with that of Sayo."
    show miyu serious at Three2 with Dissolve(0.2)
    mh8 "Hold it.{w=1.0} Are we certain that there are only eight letters and that Inoue is the recipient of the last one?{w=0.5} If we go by the nursery rhyme, there should be ten."
    show yoshiro angry at Three3 with Dissolve(0.2)
    ys6 "What's the point of sending letters to the deceased? To waste paper and ink, that is.{w=1.0} Of course not. It's a given they already met the two in person."
    ys6 "From what I recall about my discussion with Inspector Emmerich, the perpetrator is a meticulous creature. I say that because their actions borderline classify them as {i}beyond human{/i}.{w=1.0} A bold claim, but perhaps they are a vicious serial killer rivalling Jack the Ripper."
    show akira surprised at Three1 with Dissolve(0.2)
    ai2 "But Jack the Ripper is a product of a journalist's creative imagination.{w=1.0} What's different now is, behind that phantom omnipotent-like persona is a deranged human being with gravely malicious intent."
    show miyu focusedpose at Three2 with Dissolve(0.2)
    mh8 "You know, I'm starting to notice a pattern even if this is just the second murder."
    show akira surprised2 at Three1 with Dissolve(0.2)
    ai2 "{i}Just{/i} the second murder? How are you even sure if a third will take place?"
    show miyu pissedclosed at Three2 with Dissolve(0.2)
    mh8 "Take your mind far back when all of you were discussing this by the auditorium.{w=1.0} Why?{w=0.5} Because I'm starting to get an image on who our friendly-neighborhood phantom killer is."
    mh8 "{cps=15}Kyou and Hiroshi's deaths mirror those of Ayanami Hayashibara and Rika Suzumiya, respectively.{/cps}"
    show akira angry at Three1 with Dissolve(0.2)
    ai2 "What?!"
    show yoshiro surprised2 at Three3 with Dissolve(0.2)
    show akira serious at Three1 with Dissolve(0.2)
    ys6 "Shhh...!"
    show yoshiro serious2 at Three3 with Dissolve(0.2)
    ys6 "So you're saying that the culprit is the same as the one from the Sacred Heart Curse Killings?{w=1.0} What you are proposing contradicts the existence of the letters."
    show miyu talk smile at Three2 with Dissolve(0.2)
    mh8 "Not exactly, of course. That would be too obvious of an idea for the \"meticulous creature.\""
    mh8 "What I'm saying is that {i}someone{/i} is trying to imitate the nature of the sensational curse killings in Sacred Heart Academy. Give people a shock, and the most recent event they'll connect no matter how disjoint it may be."
    show yoshiro worried at Three3 with Dissolve(0.2)
    ys6 "\"The Butcher-on-the-bus...\"{w} False recognition!"
    mh8 "Do you see it now?{w=1.0} For them, it's a battle of wits where fear, though not naked, is the ultimate hold. It's a matter of the past and the future, both of which play an important factor in deciding the present."
    show yoshiro talkleft at Three3 with Dissolve(0.2)
    ys6 "And the framework for the past and the future, if I follow your reasoning correctly, is the Sacred Heart Curse Killings?"
    show miyu serious at Three2 with Dissolve(0.2)
    mh8 "Basically, yes.{w} It's probably why Inspector E. can't make a move. Even he can't detach Kyou and Hiroshi's deaths from those tragic incidents."
    mh8 "And then you have that rhyme...{w=1.0} Why does it always have to be creepy children and nursery rhymes these days?"
    ai2 "They were killing people according to the rhyme, right? So, why does our culprit chose to do it out of order?"
    show miyu bored at Three2 with Dissolve(0.2)
    mh8 "Because it's cliche if they follow it to the letter?{w=1.0} Isn't Agatha Christie's {i}And Then There Were None{/i} so well known that people recognize how the rhyme works?"
    show yoshiro worried at Three3 with Dissolve(0.2)
    ys6 "Other than that, it's not because they are sloppy, but remember that this is only a game for them.{w=1.0} It takes the fun out of it when you safeguard yourself from anything remotely related to the next verse of the rhyme."
    ys6 "To do that would be utter madness.{w=1.0} Though, I suppose our culprit exhibits a special kind of madness and would want to part that in the most appropriate way they see fit."

    show miyu bored at Three2 with Dissolve(0.2)
    "The three shifted their eyes among each other, exchanging silent messages only they could understand.{w=1.0} A nod.{w=0.5} A smirk.{w=0.5} An affirming eye-close."
    stop music fadeout 2.0

    show akira worried at Three1 with Dissolve(0.2)
    ai2 "{cps=15}I take it from our discussion...{w=1.0} we can pinpoint who the killer is?{/cps}"
    show miyu naughty focuspose2 at Three2 with Dissolve(0.2)
    mh8 "{cps=5}Yes...{/cps}{w=1.0} {cps=15}Chances are they are always watching... even now, perhaps.{/cps}{w=1.0}{nw}"
    show akira worriedleft at Three1 with Dissolve(0.2)
    show yoshiro smile at Three3 with Dissolve(0.2)
    ys6 "{cps=15}Madness is merely a smoke screen.{w=1.0} Once you understand how the mind of a serial killer works, only then can you comprehend what {i}that special kind of madness{/i} truly entails.{/cps}{w=1.0}{nw}"
    show yoshiro smirk at Three3
    show miyu naughty smirkpose at Three2
    "\"He{w=0.5}he{w=0.5}he{w=0.5}he{w=0.5}he{w=0.5}he...\""
    show akira smirk at Three1 with Dissolve(0.2)
    ai2 "Okaaaaaay...?{w=1.0} This isn't unsettling at the slightest. Ahehehehe...?"

    show akira annoyed at Three1
    show yoshiro serious at Three3
    show miyu focusedpose at Three2
    play sound sfx_beep4
    "{i}*BEEEEEEEEEEP*{/i}"
    stop sound

    sr5 "{i}Urgent announcement.{/i}{nw}{w=1.0}"
    sr5 "{i}Requesting to excuse the following students for a meeting in the Student Council room immediately:{w=1.0} Ichirou Yokohama,{w=0.5} Sumiko Tokubei,{w=0.5} Miyu Hirano,{w=0.5} Akira Ichibana,{w=0.5} Yoshiro Suzuki,{w=0.5} and Hikaru Yamomoto.{/i}"
    sr5 "{i}Thank you.{/i}"

    window show
    nvl clear
    narr "The three boys checked their watches.{w} Even though it was almost the end of their recess, they got up and left for the council room. Hikaru, Sumiko, and Ichirou joined them at the conference room shortly after."
    window hide

    play sound sfx_dooropen
    scene bg conferenceroom with dissolve
    show sayo seriousclosedpose at Three2 with Dissolve(0.1)
    show ichirou focus at Eight3 with Dissolve(0.1)
    show miyu worried at Eight6 with Dissolve(0.1)
    show akira serious at Eight2 with Dissolve(0.1)
    show yoshiro serious at Eight8 with Dissolve(0.1)
    show hikaru focusleft at Eight7 with Dissolve(0.1)
    show sumiko surprised2 at Eight1 with Dissolve(0.1)

    window show
    narr "The door to the main office was locked while the investigations were taking place.{w} To maintain its cover, a small team led by Emmerich -- with special permission from the principal -- conducted their investigations at night.{w} Important file cabinets were also relocated to one corner of the conference room."
    narr "Sayo sat at her usual place, looking down with her hands entwined under her chin. The six other occupants sat around the table and moved closer to the front."
    narr "The atmosphere inside the room was tense,{w=0.5} its occupants waiting in anticipation what Sayo would share to them.{w} Ideas danced around their heads, contradicting or supporting one another."

    nvl clear
    window hide

    play sound sfx_schoolbell
    "{i}*RIIIIIIIIIIIIINNNGGG*{/i}"

    show sayo serioustalkpose at Three2 with Dissolve(0.2)
    sr5 "We were correct after all."

    show sayo seriousnormalpose at Three2 with Dissolve(0.2)
    play sound sfx_pageturn
    "From her jacket, she produced a familiar envelope."
    "The seal was already broken, having been examined by Emmerich and Sayo at the principal's office earlier.{w} Ichirou, the person closest to her, took it and examined the parchment."

    sr5 "Just this early morning, Inspector Emmerich intercepted a mail addressed to Inoue's ward -- we have Dr. Shinozaki to thank for that.{w} He called me as soon as he finished comparing it to our letters."
    show ichirou serious at Eight3 with Dissolve(0.2)
    iy1 "It's authentic.{w} The clock-like circle and the S and R letters in the center...{w=0.5} It's just like the symbol at the back of the letters we received."
    show hikaru angry at Eight7 with Dissolve(0.2)
    hy10 "What does it say?"
    show ichirou serioustalkleft at Eight3 with Dissolve(0.2)
    iy1 "{cps=10}It says here --{/cps}{nw}"
    show ichirou confused at Eight3 with Dissolve(0.2)
    iy1 "{b}*GASP*{/b}"

    scene black with fade
    play sound sfx_pageturn
    "Slowly,{w=0.5} Ichirou's grip lessened and let the paper fall to the table's center.{w=1.0} Everyone leaned from their positions to read the contents."

    scene bg letter a with dissolve
    centered "{cps=15}{i}{color=#bd0000} Share this to no one lest you face the consequences.{w=1.0} One of you is me.{/i}{/cps}{w=2.0}{nw}"

    play sound sfx_fistbang
    play music bg_controlledchaos loop
    scene bg conferenceroom with vpunch
    "{b}*SLAM*{/b}"

    show ichirou serioustalk at Eight3 with Dissolve(0.2)
    iy1 "Forgive me, but you can all read what's on this paper.{w=1.0} Can you mistake this as a plant? Would you dismiss this as nothing?!"
    show yoshiro surprised at Eight8 with Dissolve(0.2)
    ys6 "Ichirou, settle down!"
    show ichirou serioustalkleft at Eight3 with Dissolve(0.2)
    show yoshiro surprised2 at Eight8 with Dissolve(0.1)
    iy1 "You know, ever since Hiroshi's murder --{w=0.5} Hell! Even back to the abduction case last month --{w=1.0} there is {i}this{/i} certain suspicion that always seem to bother me.{w=1.0} I can't just ignore it. I have to let it out...{w=1.0}{nw}"
    show ichirou happy2 at Eight3 with Dissolve(0.2)
    iy1 "As long as we are all gathered in this room!"
    show ichirou serious at Eight3 with Dissolve(0.2)
    show miyu pissed at Eight6 with Dissolve(0.2)
    mh8 "You don't know what you're saying, Ichirou.{w} Why are you even going as far as to consider that possibility? This is a ruse to incite chaos among us. Do you not understand that?"
    show ichirou serioustalk at Eight3 with Dissolve(0.2)
    iy1 "Shut up!{w=0.5} Even you can't deny it because you saw it with your own eyes.{w} Did it keep you up at night?{w=0.5} No! You never even gave a damn in the first place, Miyu."
    show miyu happytalk at Eight6 with Dissolve(0.2)
    mh8 "Then I suggest you stop dilly-dallying and spit it out already!"
    hide ichirou with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    stop music fadeout 2.0

    scene bg conferenceroom dark with dissolve
    "Ichirou clenched his fist, scanning the eyes of his companions around the room."
    "This time, it was not only Sayo and Sumiko glaring at him.{w=1.0} Miyu clenched his teeth, emotions mixed with outrage and fear."
    play sound sfx_heartbeat loop

    # Sayo
    show ichirou focus at Three3 with Dissolve(0.5)
    centered "{color=#808080}{cps=15}{i}From your demeanor, I can already tell what is on your mind.{w=0.5} You are hesitating to spit it out.{w=1.0}\nWhy?{w=1.0}\nYou could not even believe it yourself.{w=0.5} I am sure everyone here would agree with me.{w=1.0}\n And those emotions which are packaged within the ink,{w=0.5} those doubts which have been implanted in their hearts,{w=0.5} those would ironically turn the tides into your favor.{/i}{/cps}{w=2.0}{nw}"
    hide ichirou with Dissolve(0.2)

    # Miyu
    show ichirou focus at Three2 with Dissolve(0.5)
    show sayo seriousnormalleftpose at Three3 with Dissolve(0.5)
    centered "{color=#808080}{cps=15}{i}I knew it.{w=0.5} This was an inevitable scenario from the beginning.{w=1.0}\nIf you hold back now, you would look more like a fool than you are at present.{w=1.0}\nMove forward.{w=0.5} Be aggressive.{w=0.5} Our fates have already changed sometime ago. We are now simply treading down the very path it created.{/i}{/cps}{w=2.0}{nw}"
    hide ichirou with Dissolve(0.2)
    hide sayo with Dissolve(0.2)

    # Hikaru
    show yoshiro angry at Three1 with Dissolve(0.3)
    show ichirou focus at Three2 with Dissolve(0.3)
    show sayo seriousnormalleftpose at Three3 with Dissolve(0.3)
    centered "{color=#808080}{cps=20}{i}He's going to point fingers at one of us.{w=0.5} I'm innocent! That I'm sure of.{w=1.0}\nThe others?{w=0.5} I can't be certain with them.{w=1.0}\nHowever, if one of those letters is really telling the truth,{w=0.5} then where does that leave us?{/i}{/cps}{w=2.0}{nw}"
    hide yoshiro with Dissolve(0.2)
    hide ichirou with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    
    # Yoshiro
    show akira worriedleft at Three1 with Dissolve(0.5)
    show miyu pissedclosed at Three3 with Dissolve(0.5)
    centered "{color=#808080}{cps=20}{i}We've already discussed this many times.{w=0.5} I've also considered every possibility to the best of my knowledge.{w=1.0}\nAt this point, there always exists one instance that contradicts the facts!{w=0.5} If this eighth letter is truly consistent with the rest, then it follows this fact:{w=1.0}\nSomeone in this room is lying.{/i}{/cps}{w=2.0}{nw}"
    hide akira with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    
    # Sumiko
    show ichirou focus at Three2 with Dissolve(0.5)
    show yoshiro angry at Three1 with Dissolve(0.5)
    centered "{color=#808080}{cps=20}{i}I kept silent throughout most of the issues,{w=0.5} but this boy's bravado is admirable!{w=0.5} It seems that abandoning silence is the best move.{w=1.0}\nIf we close our minds off this, we may never know the truth.{w=0.5} And the truth is...{/i}{/cps}{w=2.0}{nw}"
    hide ichirou with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    
    # Akira
    show sayo seriousnormalpose at Three1 with Dissolve(0.3)
    show hikaru worried at Three2 with Dissolve(0.3)
    show sumiko angry at Three3 with Dissolve(0.3)
    centered "{color=#808080}{cps=20}{i}I've seen it too.{w=0.5} I've thought of it, too.{w=0.5} Yet what holds me back is the unlikelihood of such a thing to be real.{w=0.5} After all, isn't this part of the culprit's evil plans?{w=1.0}\nWell, maybe not in that sense.{w=1.0} But the point here is that whatever goal they are trying to achieve can't be pleasant for us.{w=1.0}\nIt's chilling and torturous to be caught in the crossfire!{/i}{/cps}{w=2.0}{nw}"
    hide sayo with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)
    
    # Ichirou
    centered "{color=#808080}{cps=15}{i}I've been waiting for this moment -- no other witnesses involved.{w=0.5} Just the seven of us enclosed in this room.{w=1.0}\nFinally...{w=0.5} Finally!{w=0.5} If a confession is warranted from that ONE particular person, then the proper time is now.{w=1.0}\nWe cannot wait for Inoue any longer.{w=0.5} I feel that this is within her best interests.{/i}{/cps}{w=2.0}{nw}"
    stop sound fadeout 1.0

    scene bg conferenceroom with dissolve
    "Ichirou sighed, affirming his own decision."

    show ichirou focus at Three2 with Dissolve(0.2)
    iy1 "{cps=15}There can be no other plausible explanation.{/cps}{w=1.0} {cps=20}All of these crimes could only have been done by you...{/cps}{w=1.0}{nw}"

    play sound sfx_whoosh
    scene white with dissolve
    "{cps=10}Time stopped{w=1.0} as Ichirou named his suspect.{/cps}{w=1.0}{nw}"

    play sound sfx_fistbang
    scene bg conferenceroom
    show sayo seriousclosedpose at Three2 with sshake
    play music bg_corruption loop
    iy1 "Sayo Ronoroa!{w=1.0} There can be no other!"
    mh8 "Oh, for God's sake..."

    "The other occupants were stunned by Ichirou's bold accusation...{w=1.0} except for Sayo. The girl was unwavered despite the case made against her."

    show sayo seriousclosedpose at Eight1
    show sumiko serioustalk at Eight8
    st3 "You're insane!"
    show hikaru angry at Eight5 with Dissolve(0.2)
    hy10 "I'm sorry, Ichirou, but I agree. Don't you realize what you're doing is slander against the Student Council President?{w=0.5} Please take back what you just said!"
    show sayo serioustalkpose at Eight1 with Dissolve(0.2)
    sr5 "Let him be, Hikaru. It is not in my duty to run away from this controversy.{w=0.5} After all, I foresaw all of this after analyzing everything from the start."
    show hikaru focusleft at Eight5 with Dissolve(0.2)
    hy10 "What do you mean, Sayo-chan?"
    show miyu happytalk at Eight4 with Dissolve(0.2)
    mh8 "It means the idiot who's standing over there took the bait.{w} This inevitable scenario and the accusation against Sayo...{w=1.0} it is all according to the culprit's plan."
    show miyu serious at Eight4 with Dissolve(0.2)
    mh8 "Excuse my rude interruption, Sayo."
    show miyu bored at Eight4 with Dissolve(0.2)
    show sayo seriousnormalpose at Eight1 with Dissolve(0.2)
    sr5 "No offense taken. You're absolutely correct."
    hide miyu with Dissolve(0.2)
    hide sayo with Dissolve(0.2)

    show hikaru focusright at Eight6 with Dissolve(0.2)
    show sumiko serious at Eight1 with Dissolve(0.2)
    "At this point, Yoshiro stood up and slowly moved around the table, letting his fingers slide across the varnished wood."

    show yoshiro worried at Eight3 with Dissolve(0.2)
    ys6 "To tell you the truth, I had a hard time believing it either.{w} If we consider the plausibility of each and every one of us in committing the crimes, we must ask ourselves:{w=0.5} Who would be the most resourceful?"
    show hikaru worried at Eight6 with Dissolve(0.2)
    hy10 "{cps=12}Sayo and me...{/cps}"
    show yoshiro smile at Eight3 with Dissolve(0.2)
    ys6 "That deserves half the full marks.{w} You said, \"Sayo and me.\" So, for what reason?{w=1.0} It's not just about resources, but also of mental capability.{w} Ask yourself, Hikaru,{w=0.5} can you stomach the image of yourself ending a person's life in cold blood?"
    hy10 "..."
    show yoshiro serious at Eight3 with Dissolve(0.2)
    ys6 "I'm with Ichirou on this matter,{w=0.5} unless you can convince me to change my mind."
    hide yoshiro with Dissolve(0.2)
    hide hikaru with Dissolve(0.1)
    hide sumiko with Dissolve(0.1)

    show miyu bored at Three1 with Dissolve(0.2)
    show hikaru worried at Three2 with Dissolve(0.2)
    show sumiko seriousleft at Three3 with Dissolve(0.2)
    "Sumiko stormed out of his seat and joined Miyu and Hikaru at the other side. Yoshiro took his place."
    stop music fadeout 2.0
    hide miyu with Dissolve(0.1)
    hide hikaru with Dissolve(0.1)
    hide sumiko with Dissolve(0.1)

    show sayo seriousclosedpose at Three2 with Dissolve(0.2)
    show akira serious at Eight2 with Dissolve(0.2)
    ai2 "While I admittedly don't have solid evidence to link you to the crimes the previous month, I have enough reason to believe you murdered Hiroshi."
    show akira annoyed at Eight2 with Dissolve(0.2)
    ai2 "As for why, I'm not even sure myself.{w=0.5} I don't know..."
    show miyu serious at Eight6 with Dissolve(0.2)
    mh8 "Then why don't you come over here so we can discuss the reasons why {i}not{/i} Sayo is the culprit?"
    show ichirou serioustalk at Eight3
    iy1 "Akira, don't!{w} These three don't see the truth yet because of their blind loyalty to her."
    show miyu happytalk at Eight6 with Dissolve(0.2)
    mh8 "What the hell, Ichirou?{w=0.5} This isn't a question of {i}blind loyalty{/i}. It is of {i}rationality{/i}.{w=1.0} You're the one who is misguiding people from the truth, and your arguments are just unsound as you are."
    show akira angry at Eight2 with Dissolve(0.2)
    show miyu confused at Eight6 with Dissolve(0.2)
    ai2 "Enough!{w} I've made up my mind."
    show sayo smileopenpose at Three2 with Dissolve(0.2)
    sr5 "Don't worry.{w=0.5} You are free to side with anyone whom you feel closer to your heart. I won't hold you in contempt nor force you to resign your position as auditor."
    show akira annoyedclosed at Eight2 with Dissolve(0.2)
    play music bg_regrouping loop
    ai2 "{cps=12}I'm sorry, Pres...{/cps}"
    sr5 "Accepted.{w} For whatever purpose you are there right now, for loyalty or genuine service, I trust you are mature enough to reach that decision yourself."
    show miyu serious at Eight6 with Dissolve(0.2)
    mh8 "I have made my decision, Sayo.{w=1.0} I believe in your innocence! We can all reach a favorable conclusion if we hang on.{w=0.5} I say that even at the cost of {i}some{/i} precious friendships."
    show hikaru angry at Eight7 with Dissolve(0.2)
    hy10 "Me too!{w=1.0} I don't even get {i}why{/i} you're the culprit of all people. Whoever it is needs to pay! They're breaking us apart!"
    show sumiko serioustalk at Eight8 with Dissolve(0.2)
    show ichirou focus at Eight3 with Dissolve(0.1)
    show yoshiro serious at Eight1 with Dissolve(0.1)
    st3 "I am disgusted with all three of you --{w=0.5} especially you, Ichirou --{w=0.5} who hold on to that stupid delusion.{w} What has happened to {i}innocence until proven guilty{/i}?{w=1.0} And where is your evidence?"
    iy1 "I admit I don't have anything on me.{w=1.0} But one thing can clear this up for us, or rather, one person.{w=0.5} It won't be long before she is discharged."
    show miyu pissedclosed at Eight6 with Dissolve(0.2)
    mh8 "I'm sorry you have to feel this way, Ichirou."
    show ichirou focusleft at Eight3 with Dissolve(0.2)
    iy1 "Don't pity me. That's the lowest anyone has ever felt towards me.{w} Besides, what could be worse than being betrayed by the people you trusted?"
    show miyu bored at Eight6 with Dissolve(0.2)
    mh8 "You have no right to tell me that.{w=1.0} It's as if you know exactly what betrayal truly feels like..."
    hide sayo with Dissolve(0.1)
    hide ichirou with Dissolve(0.1)
    hide miyu with Dissolve(0.1)
    hide akira with Dissolve(0.1)
    hide yoshiro with Dissolve(0.1)
    hide hikaru with Dissolve(0.1)
    hide sumiko with Dissolve(0.1)

    scene bg conferenceroom dark with dissolve
    window show
    nvl clear
    narr "Half the current class period had already passed by the time Sayo adjourned the meeting and dismissed everyone."
    narr "The day ended in tragedy, not by murder but by polarizing the group into two different stands.{w} Is Sayo Ronoroa truly guilty of the crimes against Kyou Kirisaki, Inoue Shinozaki, and Hiroshi Kano as Ichirou asserted?{w=1.0} Or is she innocent as Miyu's group maintains?"
    narr "Even this conflict they had to keep a secret amongst themselves.{w} It effectively shattered the relationships of those involved, especially the ones from IV-C."
    narr "Only time knows how long this feud will go on.{w} More importantly, how long can they maintain this farce before everything explodes out to the open?"
    stop music fadeout 2.0

    nvl clear
    window hide

    return

label ch02_17_epilogue:
    scene black with fade
    "JULY 29, 2013 - 1330H"

    window show
    nvl clear
    narr "How many days has it been?{w=1.0} Five?{w=0.5} Ten?"
    narr "Ever since that wild stunt Ichirou pulled off in the council room, I never spoke to him."
    narr "Akira and Yoshiro, on the other hand...{w=0.5} despite the three of us having a civil discussion prior to the meeting, still they believed in such improbable ideas.{w} The nerve...{w=0.5} to think they would be swayed by such nonsense."

    window hide
    scene bg smallstreet evening with fade
    window show
    nvl clear
    narr "Day one of the first quarter exams had just ended."
    narr "The happiest I have been in the interim is my birthday celebration.{w=0.5} I just turned fifteen yesterday -- at which I must mention I am one of the youngest amongst my batchmates.{w} But that does not mean I will allow myself to be babied."
    narr "I have saved enough money since last month to celebrate with a special person.{w=1.0} I ought to return the favor for Sanae's treat on her birthday."
    narr "I forgot how grim the previous days were as I chanced upon her.{w=1.0} She smiled, so ever honestly surprised to see me."

    nvl clear
    window hide

    play music bg_palingaroundparis loop
    show miyu smile at Three1 with Dissolve(0.2)
    show sanae smile at Three3 with Dissolve(0.2)
    sanae "Hey, Mi-kun! What brought you here?"
    show miyu naughty smirk at Three1 with Dissolve(0.2)
    mh8 "You know why I'm here. I've come to treat you.{w} Consider it as a repayment for your kindness."
    show sanae smiletalk at Three3 with Dissolve(0.2)
    sanae "Oh, I see! I'll let mother know we'll be eating out."
    hide sanae with Dissolve(0.2)

    show miyu naughty blush at Three1 with Dissolve(0.2)
    "She disappeared into their house.{w} I can hear her voice, although not as lighthearted as my last visit.{w=1.0} Awkward, tomato-faced once again.{w=0.5} The embarrassment was slowly turning into shame.{w=0.5} My presence felt unwelcome."
    show miyu smile at Three1 with Dissolve(0.2)
    show sanae smile at Three3 with Dissolve(0.2)
    "Within a minute, she re-emerged at the door, wore her sandals, and handed me a chocolate bar."

    show sanae smiletalkclosed at Three3 with Dissolve(0.2)
    sanae "Happy birthday, Mi-kun!{w=0.5} Shall we?"
    hide miyu with Dissolve(0.2)
    hide sanae with Dissolve(0.2)

    scene bg park with dissolve
    play sound sfx_street loop
    show miyu confused at Three1 with Dissolve(0.2)
    show sanae blank at Three3 with Dissolve(0.2)
    "Away we went.{w=0.5} This time, I led the way."
    "We did not have a conversation as engaging as before. Sanae was tired and so was I, albeit for different reasons."

    show miyu nervous blushleft at Three1 with Dissolve(0.2)
    mh8 "I hope I didn't disturb your rest period."
    show sanae smile at Three3 with Dissolve(0.2)
    sanae "No, it's okay. Don't get yourself worked up over it.{w} This is what I normally am after school. We're Seniors, after all. {i}*giggle*{/i}"
    show miyu smile at Three1 with Dissolve(0.2)
    mh8 "That's good to hear. I thought I bothered you or something, so I was kind of worried."
    show sanae smileleft at Three3 with Dissolve(0.2)
    sanae "Where are we eating, anyway?"
    show miyu smiletalk at Three1 with Dissolve(0.2)
    mh8 "Somewhere iconic..."
    hide miyu with Dissolve(0.2)
    hide sanae with Dissolve(0.2)
    stop sound fadeout 2.0

    "She nodded, and we headed to the same restaurant she treated me on her birthday."
    scene bg jollibeerestaurant with dissolve
    show miyu focusedpose at Three3 with Dissolve(0.2)
    "We sat at the same place and I let her order her food. She asked mine but I passed."
    show sanae blank at Three1 with Dissolve(0.2)
    "She returned with a burger-and-fries meal, eating ahead while my mind was swimming in thoughts."

    show sanae smile at Three1 with Dissolve(0.2)
    sanae "Thanks for this, Mi-kun. I really appreciate it. I'm sorry I haven't prepared any gift for you."
    show miyu naughty focuspose at Three3 with Dissolve(0.2)
    mh8 "No problem."
    show miyu focusedpose at Three3 with Dissolve(0.2)
    mh8 "Confirm this for me, if you don't mind.{w=0.5} You're also fifteen, right?"
    show sanae worried at Three1 with Dissolve(0.2)
    sanae "Hmmmmm... Sixteen."
    show miyu talk at Three3 with Dissolve(0.2)
    mh8 "Huh? But I thought..."
    show sanae smileleft at Three1 with Dissolve(0.2)
    sanae "I was born in 1997.{w} The idea started sometime when I was still in elementary school. Someone had made the same mistake as you did. It buzzed around quickly that I never bothered to correct people about it anymore."
    show sanae smile at Three1 with Dissolve(0.2)
    sanae "Only my closest friends know this fact, but I can share the info as long as they ask me."
    show miyu proudclosed at Three3 with Dissolve(0.2)
    mh8 "That makes sense.{w} Ah, have I been feeding myself the wrong information again?"
    show sanae worriedleft at Three1 with Dissolve(0.2)
    show miyu pissedclosedpose at Three3 with Dissolve(0.2)
    stop music fadeout 2.0

    window show
    nvl clear
    narr "While she munched on her burger, I reflected on the events of this morning."
    narr "We heard from Ikuko last Friday that Inoue was already at home, currently reviewing for the first quarter exams.{w} Ms. Harada passed the news down to her advisory class. For the first time in over a month, IV-A's atmosphere flourished anew."
    narr "I spoke with our club adviser about it and she was delighted.{w} We agreed that I hold the position as acting president for one more week, personally requested by Inoue herself. She needed the time and energy for her academics and the entrance exam this weekend."

    nvl clear
    window hide

    show sanae worriedtalk at Three1 with Dissolve(0.2)
    sanae "You haven't texted me in a week, Mi-kun. I have no idea how you've been doing.{w=1.0} Did something wrong happen?"

    "{i}Should I say it?{w=1.0}\nWe all agreed not to disclose the details of what happened last July 19, as well as the closed-doors meeting involving Sayo.{/i}"

    show miyu pissedleftpose at Three3 with Dissolve(0.2)
    mh8 "Ahem. I believe this is the best way to put things without compromising anyone..."
    show sanae worried at Three1 with Dissolve(0.2)
    sanae "I'm sorry for prying.{w=0.5} You don't need to let it out if you're feeling uncomfortable. I can understand."
    show miyu pissedpose at Three3 with Dissolve(0.2)
    mh8 "Let's say things have been difficult... rough...{w=1.0} however I want to describe it.{w} In all honesty, the past few days have been too chaotic to even talk about."
    show sanae blank at Three1 with Dissolve(0.2)
    sanae "Is that so?{w=1.0} Thanks for the update, Mi-kun. Again, I'm not obliging you."

    show miyu pissedclosedpose at Three3 with Dissolve(0.2)
    "I nodded, letting my thought train run once more."
    show sanae worriedleft at Three1 with Dissolve(0.2)
    "She finished the burger and offered me some fries.{w} I took a few, taking my turn to eat while she checked her phone."

    play music bg_therunaway loop
    show miyu naughty closepose at Three3 with Dissolve(0.2)
    mh8 "Let's have a simple thought experiment.{w} I'll be laying down the story and you share to me your insights. Game?"
    show sanae smirk at Three1 with Dissolve(0.2)
    sanae "Game! What is it?"
    show miyu naughty focuspose2 at Three3 with Dissolve(0.2)
    mh8 "First, I want you to close your eyes.{w=1.0} Ignore the world around you. There won't be any tricks and I'll keep my eyes open. All you need to do is relax."
    show sanae worriedclosed at Three1 with Dissolve(1.0)
    sanae "{cps=8}{i}*inhale*{/i}{/cps}{w=1.0} {cps=15}I'm ready.{/cps}"
    scene black with fade
    mh8 "Imagine you have a balloon."
    mh8 "When you pop it, the sound it produces is sometimes loud enough to ring your ears. The abruptness is not good for your heart either."
    mh8 "But first, as vivid as you can, please describe the balloon for me."
    sanae "{cps=20}I have a medium-size{w=0.5} oblong-shaped{w=0.5} violet balloon.{w=1.0} It smells of rubber{w=0.5} and it screeches when I roughly scratch the surface.{w=1.0} It is plump enough for me to give it a light squeeze every now and then.{/cps}"
    mh8 "Is the air tightly packed?"
    sanae "{cps=20}Newly filled up; oxygen.{/cps}"
    mh8 "Now, I have a pin.{w} You remove your hands from the sides and place them on its vertical axis -- the tips facing sidewards.{w=1.0} I pierce the balloon and it {b}{i}POPS{/i}{/b}!{w} How loud was that?"
    sanae "{cps=20}It made me jump,{w=0.5} almost as if a firecracker had set off inches away from my face.{/cps}"
    mh8 "We've reached the end.{w=1.0} You may now open your eyes."

    scene bg jollibeerestaurant with fade
    show miyu naughty focuspose2 at Three3 with Dissolve(0.2)
    show sanae smile at Three1 with Dissolve(0.5)
    "Her smile from before returned, easing away the tension and resetting the clock as it was three years ago."

    show sanae smiletalk2 at Three1 with Dissolve(0.2)
    sanae "It felt short, but I had fun! {i}*giggle*{/i}{w=0.5} Did you make that up, Mi-kun?"
    show miyu naughty smirkpose at Three3 with Dissolve(0.2)
    mh8 "Neat piece of work, isn't it?"
    show sanae smiletalk at Three1 with Dissolve(0.2)
    sanae "Wow! {i}*clap* *clap* *clap*{/i}{w} Can you explain the principle behind it?"
    show sanae smile at Three1 with Dissolve(0.2)

    show miyu naughty focuspose at Three3 with Dissolve(0.5)
    show miyu naughty focuspose2 at Three3 with Dissolve(0.5)
    "I finished eating the fries, looked around, and began my explanation."

    show miyu talk at Three3 with Dissolve(0.2)
    mh8 "Are you familiar with the Schrodinger's Cat?{w=0.5} The paradox where the readers are asked if the cat trapped inside a locked box is dead or alive?"
    show sanae blank at Three1 with Dissolve(0.2)
    sanae "I remember it being mentioned during Chemistry class before. Why did you bring it up?"
    show miyu smiletalk at Three3 with Dissolve(0.2)
    mh8 "I based the balloon scenario on that famous thought experiment.{w=1.0} I'll explain some of the core ideas involved so you won't need to worry about that."
    show miyu smile at Three3 with Dissolve(0.2)
    mh8 "Describing the balloon you pictured with your senses is the essential step.{w=1.0} I have no idea what your balloon is like nor have I any power to influence your mind. In fact, there is no special meaning to any certain description."
    show sanae serious at Three1 with Dissolve(0.2)
    sanae "Okay, so what was the point of all that?"
    show miyu naughty smile at Three3 with Dissolve(0.2)
    mh8 "If I told you to describe the balloon once more, will you be able to do it?"
    show sanae smiletalk at Three1 with Dissolve(0.2)
    sanae "That's easy.{w} My balloon is... ummm..."
    show sanae blank at Three1 with Dissolve(0.2)
    mh8 "You have a medium-sized...{w=0.5}{nw}"
    show sanae worriedtalk at Three1 with Dissolve(0.2)
    sanae "Yes, it is medium-sized, colored violet...{w=1.0}{nw}"
    mh8 "Oblong-shaped, plump and smells of rubber...{w=0.5}{nw}"
    show sanae worried at Three1 with Dissolve(0.2)
    sanae "An oblong-shaped violet balloon of medium size, plump to touch and has a rubbery smell...{w=1.0}{nw}"
    mh8 "And...?{w=1.0}{nw}"
    sanae "Tightly packed with...{w=1.0}{nw}"
    mh8 "With...?{w=1.0}{nw}"
    sanae "...with helium, newly-filled.{w=1.0}{nw}"
    show miyu confused at Three3 with Dissolve(0.2)
    mh8 "..."
    show sanae worriedtalk at Three1 with Dissolve(0.2)
    sanae "I think I remembered it wrong."
    show miyu serious at Three3 with Dissolve(0.2)
    mh8 "Indeed. You never said it was filled with helium the first time.{w=1.0} I won't hold it against you, since the issue is with your perception, not mine."
    show sanae blank at Three1 with Dissolve(0.2)
    mh8 "Right. The catbox in the Schrodinger's thought experiment is based on the Copenhagen interpretation of quantum mechanics."
    mh8 "The smallest particle whose properties we know with certainty is the atom, discovered by the Greek philosopher Democritus."
    mh8 "Because of the hierarchical organization of life, scientists have also discovered what is known as subatomic particles. These are the protons, electrons, et cetera."
    scene black with fade
    mh8 "By \"certainty,\" I meant the smallest particle apart from light and EM waves that we can see with the naked eye.{w} Through analogy, the atom is the box and its subatomic particles are the cat's features inside the container."
    scene bg conferenceroom with fade
    show inoue happyopen at Three2 with Dissolve(0.5)
    show miyu smiletalk at Three1 with Dissolve(0.5)
    mh8 "The way you described your balloon is a parallel to the cat's description. In that experiment, however, there is only one question:{w} Is the cat dead or alive?"
    show miyu smile at Three1 with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    sanae "You can tell if the cat is dead by just smelling the box closely, right?"
    show inoue dullsurprise at Three2 with Dissolve(0.5)
    mh8 "It is the realistic situation, yes.{w=1.0} Ideally, it is impenetrable."
    show inoue seriousleft at Three2 with Dissolve(0.5)
    mh8 "I know this sounds unpleasant, but bear with me here.{w} Its rotting corpse gives off a foul smell,{w=0.5} the stench becoming worse by the minute."
    mh8 "The odor needs to dissipate into the open air, else it explodes and steals the lives of any nearby plants. What if one of those plants is essential for life?{w} Such is the loud bang of a tightly-packed balloon."
    show inoue serious at Three2 with Dissolve(0.5)
    mh8 "If the cat was alive until you opened it, or vice versa, wouldn't you at least remember the most striking details?{w} That's why the brain is the ideal catbox."
    mh8 "A person's memories, when distorted even by just a tiny bit, can alter the truth such that its owner cannot trust the memories themselves!{w} That one-minute was enough to show how whimsical the human mind is."
    show inoue serious at Three3 with Dissolve(0.5)
    sanae "So then, it doesn't matter how I describe the balloon or whether it's filled with oxygen or helium.{w=1.0} What matters is the information revealed to the outside, correct?"
    play sound sfx_dooropen
    show ikuko blank at Three1 with Dissolve(0.2)
    show inoue smile at Three3 with Dissolve(0.2)
    show ikuko smile at Three1 with Dissolve(0.2)
    mh8 "Exactly."
    show inoue talk at Three3 with Dissolve(0.2)
    show ikuko talk at Three1 with Dissolve(0.2)
    sanae "But then that means I can lie...{w=1.0} or rather, my mind can make up lies and package it as the truth.{w=1.0} Yet, to me, they are {i}indeed{/i} true."
    show ikuko worried at Three1 with Dissolve(0.2)
    hide ikuko with Dissolve(0.1)
    show inoue worried at Three3 with Dissolve(0.2)
    mh8 "Exactly."
    stop music fadeout 2.0

    scene bg jollibeerestaurant with fade
    show miyu naughty focuspose2 at Three3 with Dissolve(0.2)
    show sanae worried at Three1 with Dissolve(0.2)
    "Sanae made no further questions, the look of awe or befuddlement evident across her face.{w} I made no effort to hide my amusement."
    "However, it all comes down to one grim reality."

    show miyu naughty closepose at Three3 with Dissolve(0.2)
    mh8 "Did I answer your question?"
    show sanae blank at Three1 with Dissolve(0.2)
    sanae "Yes. It is enough to satisfy me."
    show miyu naughty smile at Three3 with Dissolve(0.2)
    mh8 "Very good.{w=1.0} I did say I would try my best."

    scene bg conferenceroom with fade
    play sound sfx_dooropen
    show inoue worried at Eight8 with Dissolve(0.5)
    "{cps=10}Because...{w=1.0} a few hours prior...{w=1.0}{/cps} {cps=20}I heard a sound as deafening as a loud bang from a balloon pop...{/cps}"

    show inoue creepy worried at Eight8 with Dissolve(0.3)
    show inoue creepy worriedtalk at Eight8 with Dissolve(0.5)
    scene bg blood2 with vpunch
    play sound sfx_girlscream
    is4 "AAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHH!!!"

    scene black with fade
    centered "{i}{b}Oh, poor little child... Pity she found out...{w}\nWhat awaited her was not reprieve but tragedy, no doubt!{/i}{/b}"

    centered "{b}***END OF JULY CHAPTER***\n\n{i}TO BE CONTINUED...{/i}{/b}"
    return