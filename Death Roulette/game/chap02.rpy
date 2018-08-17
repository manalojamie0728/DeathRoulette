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
    narr "Five minutes later, her home is in sight.{w} A neighbor of hers is outside; no signs of her, though."

    nvl clear
    window hide

    mh8 "Excuse me. Do you know anyone named Sanae?"
    neighbor "Nana? Let me fetch her brother for you."
    mh8 "Ummm... It's okay--"
    neighbor "Hey, someone’s looking for Nana! It’s one of her classmates, I think."

    "Almost immediately, her brother peeked out of their door.{w} He looked at me, and I flustered as heck in total embarrassment."

    sanae_bro "Well, well, if it isn't Miyu. Come inside."
    mh8 "Uuuuhhhh... I'm not sure about this. {b}{i}*GULP*{/i}{/b} Maybe I should --"
    sanae_bro "Hahahahaha! It's alright. Make yourself welcome."

    "I picked myself up, not wanting to stay a frozen puff of red at the sidewalk."
    "They have a relatively small house. Cozy, bright, and welcoming, that is.{w} Sanae's mother is also home."

    ms_yos "How are you, Miyu? Getting along well?"
    mh8 "Staying alive, I suppose. Things are quite heavy back at MSCI, but still a happy place to be at. {i}*chuckle*{/i}"

    "Sanae's brother served me some pandesal and a packet of peanut butter.{w} I already ate a bit before coming. Might as well help myself to show some respect."

    ms_yos "So, how did you know it's her birthday today?"
    mh8 "I asked her recently.{w} Actually, I do know the date since First Year, but my memory's a bit off back then. July 4 I thought, {i}*chuckle*{/i}"
    ms_yos "Glad you still remember and decided to visit. She's outside with her friends right now. I don't know how long before she's back."
    mh8 "I'll be waiting here for a while. I just wanted to personally greet her.{w} It's what I always do."
    ms_yos "By the way, has she already told you?"
    mh8 "What would that be, ma'am?"
    ms_yos "She's running for a position in the Youth Council this October! She'll be up against two of your former classmates."
    mh8 "More reason to see her then! I wish her luck in her endeavors.{w} When did that girl start becoming politically active? Hm. Hm. Hm."
    ms_yos "It's better if she tells you directly.{w} You know, a lot has changed since you transferred. Lots of stories even I can't recall. {i}*chuckle*{/i}"

    "For a while, I watched the soap opera on TV.{w} It bored me, so I turned to solving some Math problems instead."
    "Just to keep my mind off of it.{w} Idleness can bring about the worst memories when one's guard is down."
    "It was already six o' clock. No sweet-voiced girl out the door yet.{w} Her mother stopped playing on her phone for a while and prepared for dinner. I replaced the textbook in my knapsack shortly after."

    unk "Hey, mother! Had a great time with them at the mall. What's for --{w} Well, I didn't expect you to actually come here."

    "Blood welled up to my cheeks, and my head turned in excitement.{w} There she is, hands on the door frame, slowly curving her lips to a cat-like grin."

    mh8 "Hi... Good evening."
    sanae "Hello, Mi-kun!"
    sanae "Ma, I'll be treating Miyu out to dinner."
    ms_yos "Okay! You guys have fun.{w} By the way, your brother will be joining you in a while. Enjoy!"
    sanae "Love you, ma! {i}*giggle*{/i} Let's go."

    "We never held hands while walking. It's out of our league... for now.{w} Rather, we resorted to friendly chatter -- how we've been and what we've been up to lately."
    "We bumped into one of her classmate's older brother, who also lives nearby.{w} To describe the encounter would be rather insufficient."

    neighbor "So, what are you up to this evening? Celebrating your birthday with this guy?"
    sanae "Yeah! Truth be told, I kind of expected Mi-kun to show up even if I actually didn't. {i}*giggle*{/i}"

    "He gave a menacing glare at us, almost costing me all my cool."

    sanae "Don't get the wrong idea! It's my birthday, after all. Who says I'm not treating a former classmate?"
    neighbor "If you say so, I'll be on my way. You two enjoy yourselves. {i}*snicker*{/i}"

    "I am just glad he went away.{w} Sanae dragged me by the arm as we continued walking."
    "Past the gym where we held PE classes is a mall.{w} We settled in one of the fast-food restaurants at our current direction.{w} It was packed as usual, but preserved its relaxed ambience regardless."
    "She ordered us both a Super Meal, consisting of a one-piece chicken, spaghetti, regular fries, and soda.{w} We sat facing each other at one of the four-seaters on the left; I faced the window."

    sanae "How are things, Mi-kun?"
    mh8 "Heh. You tell me. How are things on your side?"
    sanae "Nothing much, but I can already feel the demands of being a Senior. {i}*sigh*{/i} We'll both be graduating in nine months and it's off to college."
    mh8 "Say, you're running for a position in the Youth Council? Good luck!"
    sanae "Don't mention it. {i}*giggle*{/i}{w} I just felt like it's my calling. You know, after heading the class one time and being a Youth Leader at our church."
    mh8 "Pleasant. Pleasant. Seems like things will be piling up this October in case you win.{w} Hope you serve your village well. My money is on you, hotshot."
    sanae "Sure do.{w} What did you just call me?"
    mh8 "Nothing. Let's eat. Enjoy the evening, birthday girl!"
    sanae "Cheers!"

    "{b}{i}*CLINK*{/i}{/b}"

    "Between each helping and sip, we exchanged stories no matter how serious or silly they are.{w} We kept the mood up for a good half hour or so."
    "Stomachs full, we rested for a bit.{w} Sanae took out her smartphone and texted her brother. I was watching the window, counting passersby and parked cars."

    mh8 "I did see your brother leave not long after my arrival. He shouldn't take that long, I guess."
    sanae "Oh, I know exactly where he went. That guy..."
    mh8 "Not to ruin the night, but...{w} I held this in since it felt too sensitive to share. You might know this already."

    "Sanae placed her phone down and leaned closer. She lowered her voice."

    sanae "What exactly happened in MSCI? I though the school is a safe zone."
    mh8 "Not inside, but what happened {i}outside{/i}."
    sanae "Huh?"
    mh8 "The morning the two, Kyou Kirisaki and Inoue Shinozaki, disappeared, there were no suspicious people in-campus at the time.{w} I arrived at my usual time, but I didn't see them both. Makes you wonder how an inside job could've taken place, doesn't it?"
    mh8 "After a few days, they were found. One is burnt alive and the other is left a total mess.{w} That evening at the hospital... Ugghhhh... I shudder at every thought of it."
    sanae "That's horrible..."

    "It is an understatement,{w} to say nothing of what happened last night before the final prayer."
    return

label ch02_02_prologue2:
    scene black with fade
    centered "{b}The Night Before{/b}"

    scene black with fade
    "JUNE 30, 2013 - 2010H"

    "I was out the front porch, just ending a call from my mother.{w} Sayo's figure emerged from the left, looking rather sleepy."

    sr5 "The van is ready. We'll be leaving at nine after the prayer."
    mh8 "Sure.{w} *YAWN* Let's just get this over with."

    "Despite the cool breeze, we went back inside the house.{w} The others have already gathered in the parlor: the Kirisakis, the Yamamotos, Akira, Yoshiro, Ikuko, Hiroshi, Ayumi, Sumiko..."
    "Wait. Where's Ichirou?"

    ai2 "Sorry to bother you once more, but could you dial Ichirou? He's been out for too long now."

    "With a grumpy look, I went out and contacted Ichirou.{w} Thankfully, he picked up immediately."

    mh8 "Where are you?"
    iy1 "Just went out to catch some air. Do you need me?"
    mh8 "Darn, yeah! Recklessly scurrying about when there's a monster on the loose, Einstein!{w} Now would you kindly get your butt back here to tell us you're alive?"

    "Of course, I only kept those in my head.{w} Seeing no cars presently traveling, I occupied the middle of the road. No matter how far I scout ahead on every possible direction, Ichirou's presence is absent."

    mh8 "Sorry. I can't see you from here. The prayer won't start without you, you know?"
    iy1 "That so? Okay! I'll be back in a jiffy."

    "{i}*BEEP*{/i}"

    window show
    nvl clear
    narr "I'm not going back inside until I see any sign of life from him. For now, let me enjoy the sparks from the bug zapper above."
    narr "Nothing happened for five minutes.{w} I would have made another call, but I was low on battery like everyone else."
    narr "Finally, a sign of life on my right.{w} Shuffling towards it, my lips curled to a slight grimace. Every step made deissipated a part of my own fury. If one of us goes next tonight, then I'll be damned."

    nvl clear
    window hide

    mh8 "Hey! Is that you?"

    window show
    nvl clear
    narr "But the figure was unmoving. It was static, facing away from my direction.{w} The lack of lighting concealed its identity and the road beyond. I should have called for backup moments ago, but..."
    narr "If I could just turn around and run, except it's not an option right now.{w} My eyes locked onto the figure, but its backed continued to face me. Sounds of static mixed with the wind, creating a music unheard of by many."
    narr "That, and my body is paralyzed.{w} At every passing second, the figure reeked of malevolence, transferring it within me. And it acted like poison, intoxicating my whole system."
    narr "Breathe... Breathe... Breathe... You just need some sleep. Just survive the night. Tomorrow's going to be a better day. It's Sanae's birthday tomorrow! I must not forget to send her --{nw}"

    nvl clear
    window hide

    centered "{b}{i}*WHOOSH*{/i}{/b}"

    mh8 "{b}*GASP*{/b}"

    window show
    nvl clear
    narr "For an instant, the world became enveloped in black.{w} Smoke clouded my vision, the creature's malevolent presence apparent. It posed a threat familiar to many, yet in truth unknown."
    narr "It rushed through my body, knocking me down to a shaded part of the road. I could not bear to open my eyes, fearing it was all over me. All but my ears shut down temporarily."
    narr "Someone was screaming, running; leaves rustling.{w} There's someone after that figure.{w} My brain worked itself to recognize that voice..."

    nvl clear
    window hide

    "Ichirou."

    iy1 "Wait up! You haven't answered my question -- hey!"

    "Ichirou...?"

    scene black with fade
    "JUNE 30, 2013 - 2015H"

    window show
    nvl clear
    narr "Where has that snitch gone off to?!"
    narr "I'm aware that I've dashed past Kyou's home, in favor of that... thing! He must know something about the crimes -- he must!"
    narr "He disappeared into a thicket. Blind with the thirst to squeeze some answers out of it, I followed.{w} Seconds passed, the snaps underneath gradually drowned those of the unknown figure's."
    narr "Then I took notice --{w} only my own snapping was audible.{w} It has disappeared, vanished into the night, never to be seen by anyone again. At least, it wouldn't allow itself to be."

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

    unk "Finally!"

    "Oh my God!"

    iy1 "That's not a nice thing to do at night, Miyu!"
    mh8 "Well, {i}*pant* *pant*{/i} no worse than trotting around in the fields at night, I suppose. Enjoying the fresh air... you could've been killed, you idiot!"
    iy1 "Okay! Okay! I'm sorry. Can we please walk back now? This place is starting to freak me out."

    "With little battery we had, we took turns shining a flashlight in front of us.{w} Miyu took the lead, brisk walking through the dark path."
    "I've never been on the receiving end of a reprimand, at least not as harsh as his."

    mh8 "So you thought it was a genius idea to track down a perp -- at night and alone -- and you never thought of diverting for backup?{w} Anyone could have wished condolences like {i}it{/i} did."
    iy1 "I know, but I saw that as the only chance to unmask the culprit.{i} You can't just leave a high-profile case like that for too long! What if it remains unclosed like --{nw}"
    mh8 "Knowing too much is what killed Kirisaki and pushed Inoue's mentality to its edge."
    iy1 "Tch."
    mh8 "I hope you realize that."

    "We returned safely, and the rest were relieved of panic after seeing me.{w} Sayo and Sumiko had their arms folded, eyes glaring, obviously ready to strike me for my stupidity."
    "However, no word was spoken, and the prayer continued as usual."
    "But... who whas... that?"

    sanae "You've reported this to the inspector?"
    mh8 "Of course, we did.{w} Ichirou may be a risk-taker, but he's not stupid enough to let a vital piece of information slip by. Everything is important in this case."
    sanae "But what if all comes down to nothing like the case in Sacred Heart Academy?"
    mh8 "That's the endgame plan...{w} for the opposing side, at least."

    window show
    nvl clear
    narr "At that exact moment, Sanae’s brother and his fiancée entered the restaurant.{w} With a wave, Sanae moved to the seat beside mine and the two occupied the vacant seats across from us."
    narr "They ordered nothing. Just stopping for a quick chat with us -- seven o’ clock is only sixty ticks away.{w} It is already late, but my parents would not mind."
    narr "Besides, only one day is dedicated to her birthday so I should make it worthwhile."

    nvl clear
    window hide

    "A quick glance at the window, and behind it is a familiar face.{w} He waved and went away as quickly as he appeared. Though I acted friendly, my mind was puzzled."
    "What is he even doing here?"

    sanae_bro "Who's that?"
    mh8 "It's a classmate. {i}*chuckle*{/i} Didn't expect him to be here."

    "Minutes later, I parted ways with Sanae, already thinking of a flirty message to thank her for the evening."
    "On the jeepney ride home, the question lingered within my thoughts. It's strange and amusing enough, but of all the people who were there this evening..."
    "Ichirou?"
    return

label ch02_03_reforms:
    scene black with fade
    centered "{b}Earlier{/b}"

    scene black with fade
    "JULY 1, 2013 - 1200H"

    window show
    nvl clear
    narr "By noon, the delegations were official."
    narr "{i}Hiroshi Kano stepped up for Sumiko Tokubei in the Science Club leadership, the latter already a premier in the EO and in class IV-C.{/i}"
    narr "{i}All papers to the Mathematics Club shall be temporarily overseen by the acting president Miyu Hirano while Inoue Shinozaki is undergoing therapy.{/i}"

    nvl clear
    narr "Despite the disconcerting incident a few days prior, the Seniors were able to accomplish a form for the national university's entrance exam.{w} It is the first and earliest, scheduled at the first weekend of August."
    narr "Thus, Sayo called for an emergency meeting to discuss the plans for next week's review sessions.{w} Additionally, the heads of the three organizing clubs were invited: Hiroshi, Miyu, and Ayumi Nakashima."
    narr "Only Mrs. Genkai, as usual, was absent."

    nvl clear
    window hide

    sr5 "Good afternoon, ladies and gentlemen. I would like to apologize for calling everyone on such short notice, but I feel that this matter is not to be delayed to the first Friday."
    c_4r "Why, though? The review sessions next week are nearly polished.{w} We've already included this as part of our agenda during the pre-academic year meeting with the club heads."
    sr5 "Exactly.{w} But you must keep in mind that Hiroshi and Miyu may not be fully aware of their responsibilities next week. If you recall, I only discussed our plans with Inoue and Kyou, in addition to Ayumi."
    sr5 "I hope you all understand the current situation."
    "\"Affirmative.\""
    sr5 "We already coordinated with the Science, Mathematics, and English teacher last month; hence, the contracts you signed on the 18th last month."

    "The flow will go like this."

    window show
    nvl clear
    narr "{i}Each class has assigned marshals who will handle and proctor the review sessions.{w} By default, this is left to the teacher themselves taking place on their scheduled period.{/i}"
    narr "{i}The sessions will be held Monday to Thursday class time, assuming no class suspensions. Each subject area will be provided with a study module as an aid for the current session.{/i}"
    narr "{i}Preceding the Club and Organization Activities on Friday would be the lighter final sessions.{w} All that is needed to be taught are techniques in general test-taking and may focus on specific parts of each subject area.{/i}"
    narr "{i}All will lead to a culminating activity on Saturday, a Mock Examination. All Seniors are required to participate, as it will simulate the entrance exam on August.{/i}"

    nvl clear
    window hide

    "As for the Student Council..."

    sr5 "Yes. Even we will be participants."
    ayumi "Question. Does that mean we he have an advantage over those not of the organizing committees?"
    sr5 "Ah, I knew that would be brought up.{w} We prepared the teachers for that. All of the questions would be from the reviewers, so there's not much to worry about."
    mh8 "Of course, to foil those who merely memorize the answers by letter... That addresses the very problem too."

    "The Council snickered at his comment, lifting their spirits up from the gloomy atmosphere."

    c_4r "How are we going to time the tests? We just have enough proctors available for the day."
    sr5 "I'll have that arranged.{w} For now, your tasks are these: inform your fellow officers of the review sessions next week and prepare some modules, if you wish.{w} Tanaka, the Parent's Consent Forms for 202 students."
    sr5 "Perform your duties well and have a nice day. Meeting adjourned."

    "At that exact moment, the bell rang, and the Council room was empty within a minute.{w} Sayo went up and delivered the minutes to Mrs. Genkai."
    "Miyu returned with Akira, engaging in banter along the way.{w} Both were visibly tired from the previous day's journey, yet they still arrived at their usual time, if only to sleep until the flag ceremony."

    mh8 "You noriced anything odd earlier?"
    ai2 "Nothing for me."
    mh8 "The meeting felt gloomy. Like, is that the usual atmosphere?"
    ai2 "Now that you mention it, yes, I actually felt the same."
    mh8 "What about her?"
    ai2 "She doesn't let herself be distracted -- as if Sayo would ever be -- but she's not as enthusiastic as before, I can tell you that much."
    mh8 "Understandable. Understandable."

    "At the very least, they wished the event to have a smooth-sailing flow. Everyone would have collected themselves by then."
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

    "{b}{i}*WHIRR*{/i}{/b}"

    window show
    nvl clear
    narr "Another homely sound.{w} Air seeping in through the vents above, and the lights flickering to life in a set manner.{w} The dancing halted, and the once-blackened room blanched to life."
    narr "Its emptiness brought suspicion over serenity.{w} A chair, indeed, and a room-length mirror facing each other. And among the normality stood out a third entity, something{w} {cps=3}-- or {i}someone.{/i}{/cps}"
    narr "A girl, her image waist-up, is a total mess on societal standards. With a single functional eye, only her face, hands, and hair are visible."
    narr "The girl refuses to remember... yet the bruises leave a scar on the mind --{w} another who refuses to remember... the Hell it went through...{w} {cps=5}It does not... It does not!{/cps}"

    nvl clear
    window hide

    centered "Good afternoon, Ms. Shinozaki."

    "...but the outside dictates otherwise. The cycle begins once more..."

    is4 "YOU FUCKING DEVIL! HAVE YOU ANY SATISFACTION?!"
    unk "Compose yourself, Inoue. We mean no harm.{w} It's Inspector Emmerich -- one of the policemen who rescued you, remember?"
    is4 "Rescued?{w} {cps=3}Heh...{/cps} {cps=5}Hehehe...{/cps} AHAHAHAHAHAHAHA!!!{w} If you're telling the truth, then why am I in a place like this?"
    p_emm "It's hard to put into words.{nw}"
    is4 "ANSWER!"
    p_emm "You're confined in an asylum."
    is4 "..."
    is4 "Then I was better off in that damned place, then. A madhouse? You're no different..."
    p_emm "You're suffering from trauma, but we fear it's something worse.{w} A psychiatrist checked up on you and... your case is beyond counseling. Your memory is temporarily impaired because of the drugs they've administered."

    "Ha! Ridiculous! Where the hell have I heard of that?"

    is4 "I hardly think you're trustworthy at all."
    p_emm "Why not? I'm an authority figure here speaking to you. I can even show you my badge the next time we personally meet."
    is4 "Exactly, but my mind is beyond stupor.{w} A memory-blocking drug? Ha! You read science fiction way too much, inspector!"
    unk "Pardon the chap, my dear. It appears he had forgotten I approved of it myself."

    "That voice... someone who I haven't heard in a long time.{w} Finally, someone I can trust."

    is4 "{cps=4}Papa...? Is that you?{/cps}"
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

    centered "{i}You believe more in the things that you {b}cannot see{/b} yet {b}only feel?{/b}{/i}"

    is4 "Can you even hear him?!"
    p_emm "Him? Who's him? Inoue, what's the matter?"

    "{cps=*0.75}The words came from my mouth...{/cps} {cps=10}without a doubt... without a doubt...{/cps}"
    "{cps=10}Naïve girl... Naïve girl...{/cps} One step closer to scorching along with him... One step closer to martyrdom... One step from the blade to claw the cat's paw!"

    p_emm "Respond, please. Are you alright?"

    "Where is he? Where is he? If he intends no harm, then why isn't he showing himself?! Up in the ceiling? Somewhere a hair's breadth behind me?"
    "Or is he there... staring straight into the lone girl sitting quietly at the box's center -- posing as the girl himself? {cps=4}Ha... Hahaha...{/cps}"

    is4 "I know you're there. {i}*snicker* *snicker*{/i}{w} Feast your eyes all you want. Come at me if you will. Break the glass that binds your presence! {cps=10}Come... Come... I'm waiting...{/cps}"
    "{i}Requesting assistance. Patient No. 4577 requires medical attention immediately!{/i}"

    "Then everything plunged into an abyss."
    "The light vanished in an instant, resetting the environment into its initial state.{w} Darkness, silence, inertia -- that and all other descriptions applicable."
    "Nobody move, not even a single twitch. Nobody speak, not even a mere gasp."

    centered "{i}Hey... Over here...{/i}"

    "Where did that come from?"

    "{b}{i}*WHIRR*{/i}{/b}"

    window show
    nvl clear
    narr "Red lights. A black box where no one has looked into before, with the only way out coated by the void's color. And serenity became overshadowed by suspicion."
    narr "The third entity became animated, independent to that of its own image.{w} It's closer than ever, pitter-pattering the glass with its finger. And like rain, it fell horizontally."
    narr "Its gaze enticed the image, urging it to come closer. The latter's feet bewitched, they brought it closer to the mirror...{w} {cps=5}closer... closer...{/cps}"
    narr "...and its playful smile curved upwards more than ever."

    nvl clear
    window hide

    u_is4 "Hi!"
    f_is4 "{cps=10}You... you can... huh?{/cps}"
    u_is4 "Afraid of your own skin, now? Silly girl. I'd give you a dollar for that. Want to know why?{w} I am aware of this exact thing on your mind right now. Besides, I {i}am{/i} you, after all. Is that wonderful or not?"
    f_is4 "You're an image. There's no way you are my mind's projection. There's... there's no way..."
    u_is4 "Oh, but there is! You could not have lived without me -- better yet, could have stayed as an infant forever.{w} Look at you now. Look at how much you've grown! {i}*giggle*{/i}"
    f_is4 "Have it your way. What do you want?"
    u_is4 "You are locked up in this cage, aren't you? Sometimes, we wonder, \"When will I be away from this hellhole?\" Oh, wait! Not close enough, I guess. My bad!"
    f_is4 "Tell me..."

    centered "{cps=10}{i}It's useless... all useless...{/i}{/cps}"

    f_is4 "This asylum is driving me to bedlam more than it cures me! Just say something, damn it!"
    u_is4 "If thy fervent desires the world out the box yonder, much merriment... whatever the hell that means.{w} But would you, really?"
    f_is4 "A fist, do you fancy?"
    u_is4 "The box here is your cage, life sentence if I'd say so.{w} Why would you ever wish to opt out? It's peaceful here, much more than the chaotic world outside."
    f_is4 "Are you with me or against me?!{w} Have you forgotten how much shit we went through? {b}*GASP*{/b}"
    u_is4 "The mind may forget, but the flesh always houses an imprint even so miniscule.{w} Pain, Inoue... Pain... Why would you want out if there is pain ready to welcome you? Have you forgotten already?"
    f_is4 "..."
    u_is4 "{cps=15}Your own pain -- it stings... or would you prefer to remind yourself of --{/cps}{nw}"
    f_is4 "Shut up."
    u_is4 "Yes. The blaze... The blaze... Who does not want to forget? And those screams. Aren't they beautiful?"
    f_is4 "{cps=10}I want to forget... I want to forget...{/cps}"
    u_is4 "Have you been listening, or do I need to spell it out?{w} The flesh does not forget. It {b}never{/b} forgets! He was pleading, begging, and you never gave a damn."
    f_is4 "{cps=10}It wasn't my fault... I never intended to...{/cps}"

    centered "{i}THEN HE WOULDN'T HAVE BEEN DEAD!{w=1.0}\nGet that into your thick skull!{/i}{w=1.0}"
    centered "{i}{cps=*0.5}You killed him.{/cps}{w=1.0}\nYou killed him!{w=1.0}\n{cps=*1.5}YOU KILLED HIM!!!{/cps}{/i}{w=1.0}"
    centered "{i}{cps=5}Hahahahahaha...{/cps}{w=1.0} {cps=10}Hahahahahahahahaha!{/cps}{w=0.5}\n{cps=15}{b}AHAHAHAHAHAHAHAHAHAHAHAHAHAHA!!!{/b}{/cps}{/i}"

    f_is4 "I AM INNOCENT!!!"

    "{i}*WHOOSH*{w=0.5} {b}*SHATTER*{/b}{/i}"

    c_is4 "Glk! Gah... {i}*croak*{/i}"

    "I buried my fist into that sentient monster, a cruel abomination that seeks to destroy.{w} Shut up... Just shut up..."
    "But it wouldn't.{w} ITs figure cracked, yet its sentience remained intact. Its eyes fixated towards mine in a manner never so condescending.{w} A laugh... that same mocking laugh that --"

    u_is4 "What a waste. {i}*snicker* *snicker* *snicker*{/i} What are you gonna do about it?"

    "Just as the blood oozed from the shards my fist was buried in, the entity consumed it within an instant.{w} It wants me... It wants me!"

    c_is4 "Let me go! Uh... Ahhhhh!!!"

    "No matter how hard I fight, it wouldn't release me. How about it? An organic chain in a cage.{w} The image flashed several times. How can the mind forget? How can it?"

    u_is4 "Don't be pushy. I'll let you free if you wish...{w=0.5} but for just a little longer, hm? I missed the human touch.{w} Being all alone must be so... sad, wouldn't you agree? Hehehehehe..."
    c_is4 "I'm begging you! Please! Please! Ugh!"
    u_is4 "{cps=10}Yes... That's it... The magic words... There's the good girl...{/cps} {i}*giggle*{/i}"
    c_is4 "*SNIFF* *SNIFF*{w=0.5} {b}*SOB*{/b}"
    u_is4 "Awww... Don't cry. I'm sorry, okay? Never mind any of that. {i}*giggle*{/i}{w} I'm done playing with you. What do you say I give you a lollipop or something before you scurry along home?"
    u_is4 "Oh, I know! This!"

    "{b}*SPISH*{/b}"

    c_is4 "Gulk!"

    "My gaze shot up into the sky, now white as before. The bastard got me with a bee sting, no doubt about it."
    "And slowly... slowly... the phantom of sleep drew itself over me."

    centered "{i}{cps=5}Star light, Star bright...{w=0.5}\nFirst star I see tonight...{/cps}{/i}"

    "{cps=10}Slowly... Slowly... lulling me...{/cps}"

    centered "{i}{cps=5}I wish I may, I wish I might...{w=0.5}\nHave the wish I wish tonight!{/cps}{/i}"

    "{cps=5}...to sleep.{/cps}"

    "{b}*THUD*{/b}"

    "Good night, dear Inoue..."
    return

label ch02_05_volleyball:
    scene black with fade
    "JULY 4, 2013 - 1730H"

    window show
    nvl clear
    narr "Like fire, the ball blazed through the air and across the net, barely touching the fabric.{w} Two fists of equal ferocity sent it back to the opposing side. Immediately, five players rallied for the counter."
    narr "{b}{i}*THUD* *POW*{/i}{/b}"
    narr "Come the sixth player!"

    nvl clear
    narr "Rushing down to the middle of the field, knees bent to jump, arm stretched upwards to the sky, Hiroshi delivered the spike.{w} A killing blow!{w} The force nearly made a crater out of the field."
    narr "One of the opposing players chased after the ball as Hiroshi's team celebrated their victory. Once he returned, the opposing sides exchanged high-fives under the net."
    narr "Akira and Yoshiro from the opposing side, and Hiroshi and Ichirou the winning side, sat together on the auditorium steps. They enjoyed a ready-made iced tea Ichirou brought."

    nvl clear
    window hide

    ys6 "You've got real talent there, buddy. Been training for the Intramurals already?"
    hk7 "Easy. Easy. What's a man of few words got to do in his spare time? {i}*chuckle*{/i} I've already told you about my plans for this, remember?"
    ys6 "Of course, V-League rookie. You've been telling us that since First Year."
    hk7 "Someday... Someday... When they allow men, that is."

    "The four finished their drink and took turns going to the auditorium to change."

    ai2 "How do we go about the review sessions next week? Science will overload our minds for sure!"
    hk7 "I've discussed this with Miyu, Ayumi, and Sayo.{w} The modules are scheduled to be distributed tomorrow morning. That way, all of us would have a head start for the weekend."
    hk7 "For each day, we focus on a specific area:{w} Gen. Sci. for Monday, Biology for Tuesday, Chemistry for Wednesday and Thursday, and Physics for Friday."
    ai2 "Wait. How is Physics low-priority? It'll get the least amount of time for sure."
    hk7 "Mrs. Kaida's got our backs, remember? She's been bugging us to study since the third week!{w} Don't even bother spending a full day on it."
    ys6 "Besides, I've got a cousin who is at the top university right now. Swear, there's little to no Physics in the exam."
    hk7 "See my point?"
    ai2 "That's not even close to wthat you said!"

    "The group burst into laughter, stalling the discussion briefly."

    iy1 "Alright! Last game!"
    "\"GAME!!!\""

    window show
    nvl clear
    narr "The four rejoined the others at the field.{w} This time, the twelve players agreed for a swap."
    narr "Akira, along with two others, joined Hiroshi's side."
    narr "All twelve players move into position. Yoshiro steps in for the first service.{w} Hand raised, he visualizes the perfect shot for an ace. Ichirou, Akira, and Hiroshi, all in triangle-like formation, anticipated his move."

    nvl clear
    narr "The three at the front rush for a counterattack. A fist managed to send the ball floating once again, down for a pass, and a third for a blow!"
    narr "At Yoshiro's court, the players caught the ball easily, repeating the movements of the enemy team. Likewise, they sent it back at the third pass."
    narr "However, Akira had found a vantage point near the net, sending the ball down after barely passing it. Slam!"

    nvl clear
    window hide

    ai2 "Yes! One for us!"

    window show
    nvl clear
    narr "At six, the guard gave off the whistle and made his rounds to rally any stray students around the campus."
    narr "Ichirou locked their classroom and rejoined Akira and Hiroshi near the front desk.{w} They were all covered in sweat."

    nvl clear
    window hide

    iy1 "Want to cool off at 7-11 for old time's sake?"

    "Akira checked his phone and sent a quick text message to his parents. He took from his backpack a coin purse."

    iy1 "Wow! That milkfish design still a thing? {i}*chuckle*{/i}"
    ai2 "Oh, this? I've been having this since First Year."
    iy1 "Really? We never saw that despite the countless number of times we did some projects at your place. Isn't that right, Hiroshi?"
    hk7 "Right. I might have been too oblivious to notice, but that's just me!"
    ai2 "Guess I'm just too shy to let other eyes on it.{w} Not that you might not believe in these things, but this is my lucky charm."
    iy1 "Oooooohhhh... So you've been preserving its mojo for something big later on?{w} Tell you what, smart guy. You don't need a talisman to influence your future. I don't, so why should you?"
    ai2 "Tell you what, {i}smarter guy{/i}, ever heard of {i}sentimental value{/i}?{w} Things like these can't be simply obtained from a random vendor. They have heart. Know what I'm saying?"
    ai2 "Besides, this purse is just an object.{w} Isn't your item of sentimental value not a {i}what{/i} but a {i}who{/i}? {i}*snicker* *snicker*{/i}"
    iy1 "Hey! Below the belt!"
    hk7 "Break it up!{w} Let's just go to the store, buy some cone or chips, and chill out, you hotheads!"
    "\"Grrrrrrr...\""

    window show
    nvl clear
    narr "The three boys gathered their belongings and exited through the school gate."
    narr "Their topics diverted from the fish purse, bringing them back to the usual school talk. There were mentions of TV shows and video games, but the discussions lasted short."
    narr "They passed by the park, now filled with students practicing some dances and lovers cuddling under the dimming lights.{w} Of course, the three took the shortest path through and ended up on the convenience store after crossing to the end of the next block."

    nvl clear
    narr "Ichirou reserved three seats as Akira and Hiroshi went to purchase two bags of chicharron.{w} As they queued, Ichirou threw his Reward Card to Akira. They paid for the chips, used the card, and returned to Ichirou."
    narr "Unlike the walk, they silently munched away at the snack, probably running out of things to discuss.{w} At one point, none of them reached into the bag, instead staring silently through the glass."
    narr "The supposedly fun side trip turned to a dull moment in an instant."

    nvl clear
    window hide

    ai2 "Wrong move."
    hk7 "What is?"
    ai2 "That. You know... I should've just gone home earlier. Every tick of the clock drives me nervous."

    "Ichirou studied his friend carefully, surprised at such uncharacteristic remarks."

    hk7 "I feel the same. Everybody else does. Wish we had Kirisaki here to allay our worries, but...{w} {b}*SIGH*{/b} The bastard had to take him out first, doesn't he?"
    iy1 "Wait. {i}first{/i}?"
    hk7 "You forgotten quickly. Say it happens again, the one at Sacred Heart Academy?"
    iy1 "Nonsense. What does a Curse Killing incident from another town have to do with ours?"
    hk7 "Yeah. Like I'd buy any of that. Emphasis on the word, \"curse,\" please."
    iy1 "Believe whatever you wish. No hard feelings if we disagree."

    "Eventually, they consumed the first bag and moved on to the second.{w} They munched away at the first few chips before continuing their discussion."

    hk7 "I'm planning on visiting the clinic on the weekend. Hope I'll get some answers from her.{w} Who's with me?"
    iy1 "But we're not even sure if Inoue is stable.{w} Like I have any guts or indecency to ask Ms. Harada or her parents about it. Do you, guys?"
    ai2 "That's off limits for me. I'd rather sit here and wait."
    hk7 "Come on, Pres. It's my former classmate we're talking about here. On top of that, a witness!"
    ai2 "Or a suspect if she ever was one."
    iy1 "Or a suspect if she ever was -- Come on, Akira. Not you, too?{w} You're showing the same symptoms as she did a month back. Cheer up! You're scaring the hell out of me."
    ai2 "Fine. I'm sorry."
    hk7 "But Akira has a point.{w} There's a hole in this story we aren't seeing yet, an important piece of the puzzle we are missing. There {i}is{/i} a possibility. There might be."
    ai2 "Hold on. Isn't that...?"

    "In the middle of Hiroshi's contemplation, they all looked towards the direction of Akira's finger.{w} At the jeepney terminal across the street is Yoshiro, still in his changed clothes."

    ai2 "Didn't he leave before us?"
    hk7 "Well, that's true. We saw them -- he and his girlfriend -- out the gate while you were locking up the room."

    "At his last diction, Yoshiro left the queue and went further into the terminal. Ichirou looked more puzzled at the two than Yoshiro himself."

    iy1 "Ohhhh... kaaayyy? You just spelled it out, so what's odd about it?"
    hk7 "Check the time. Yoshiro left the campus right after the whistle.{w} Let me ask you, is thirty minutes enough to make a round trip to his girlfriend's house and back? That's five to ten minutes short!"
    iy1 "I agree, so what's your point?"
    ai2 "Doesn't that remind you of anything, Ichirou? Miyu told us about it early morning on Tuesday."
    iy1 "Aaaaaahhh... He saw my double the night of his date, whatever it is. Yeah, he mentioned something about it."
    iy1 "Wait up!{w} What we just saw is something else. That could've been his look-alike, dummy! What's so scary about it?"
    ai2 "Nothing. I just wanted to mess with you. You know, break the ice. Hehehe... Hehehehehe!"

    "{b}*POW*{/b}"

    iy1 "Now, we're talking, Akira. That's the mischievous kid I know."
    hk7 "I must admit, you caught me off-guard for a moment there. {i}*chuckle*{/i}"
    iy1 "Do they have Wi-Fi here? I'll just message Yoshiro.{w} Whatever caper you just brought had me thinking."
    ai2 "Look. I'm sorry. Just don't beat me with that broadsheet again."
    iy1 "Relax! I'm not going to.{w} There's just something I want to ask him. Nothing serious, by the way."
    hk7 "Speaking of, where {i}did{/i} you get that broadsheet? Stuffed it into your backpack this whole time?"
    iy1 "From hammerspace if that satisfies you."

    window show
    nvl clear
    narr "Soon, they consumed the second bag and moved on to the lighter topics.{w} At seven, Ichirou called it a day and they dispersed. Akira went first, the jeepney to his village just across the street."
    narr "This left Ichirou and Hiroshi, walking through the jeepney terminal to the clock tower. Situated at the center is a majestic fountain, lights dancing in colorful patterns as the water spouts up from the distribution pipe."
    narr "They crossed the street towards the market and stopped just in front of a grocery store."

    nvl clear
    window hide

    iy1 "I forgot to ask Akira."
    hk7 "What?"
    iy1 "What fruit their little investigation that evening has brought. The time when Kyou and Inoue's disappearances were announced?"
    hk7 "Didn't yield anything useful, I bet. Let's just hope for the best on Saturday."
    iy1 "Alright. Just tell me everything you'll get from her. Let Sayo know too, if possible.{w} And if you run into him, please say \"Hi\" to Inspector Emmerich for me, will you?"
    hk7 "Affirmative."

    window show
    nvl clear
    narr "Within a few moments, Hiroshi had bid Ichirou farewell as he boarded a jeepney.{w} Ichirou skirted the current side of the market to a tricycle stop."
    narr "By half-past seven, he was home.{w} He ate dinner and went up to his room immediately. He checked for any updates on Facebook and messaged some friends before shifting his attention to his homework."
    narr "A notification bell sounded, catching Ichirou's attention."

    nvl clear
    n_hk7 "I've asked permission from Mr. Shinozaki. Inoue seems to have suffered a nervous breakdown some four hours ago, but he assured she'll be fit by tomorrow. Even better on Saturday.{fast}"
    n_iy1 "Wish you the best. :) Though, I hope you're doing our assignment due tomorrow.{fast}"
    n_hk7 "After one more chapter. Hehehehe. :) Good night, Pres.{fast}"
    n_iy1 "Night.{fast}"

    nvl clear
    narr "Ichirou put his laptop to sleep and focused on his work.{w} There were some road blocks here and there, so he occasionally went down to piss or to make some sandwiches."
    narr "By ten o' clock, he was too tired to continue, setting aside the remaining load for tomorrow morning.{w} He re-opened his laptop and saw a new message from Yoshiro."

    nvl clear
    n_ys6 "I... don't know where they're getting at with this one, but I'm certain you did see me at the jeepney stop.{fast}"
    n_iy1 "Wait. Didn't you leave with her? :O That's fast!{fast}"
    n_ys6 "I already dropped her off by the time you three left the school... 6:00, wasn't it? I stayed for a while. Had to help her with a few things.{fast}"
    n_iy1 "Sure? Honest?{fast}"
    n_ys6 "Yes. I wouldn't deny that.{fast}"
    niy1 "Okay. Thanks, anyway.{fast}"

    nvl clear
    window hide

    "Ichirou's hands clammed as he closed the laptop's lid. He went to bed, thinking about the day's events.{w} He whispered to himself before passing out."

    iy1 "That doesn't make sense..."
    return

label ch02_06_visit:
    scene black with fade
    "JULY 6, 2013 - 1300H"

    window show
    nvl clear
    narr "I see why people despise this facility.{w} Look at it. It's gloomy and unwelcoming. Not even a hint of threat like they were described in the books."
    narr "But that's just a lens. Who knows, a cuckoo might be behind the story's conception without anyone noticing.{w} And as the elevator stops, here I watch the sinister plot unfold."
    narr "The fourth floor's reception desk had two nurses stationed for the day.{w} They seemed chatty, conveying how slow the afternoon might have been. And of course, anyone with eyes would agree."
    narr "As I approached, the cuter of them welcomed me."

    nvl clear
    window hide

    hk7 "I've come to visit a patient -- Ms. Inoue Shinozaki."
    nurse "Do you have an ID card, sir?"
    hk7 "Here. I'm a schoolmate and friend of hers. Dr. Shinozaki will recognize me...{w=1.0} {cps=*0.5}if he's present, that is.{/cps}"
    nurse "An MSCI student!{w} Excuse for a moment. Please have a seat, sir."

    "The sweet nurse efficiently dialed the ward Inoue is at.{w} She mentioned my name, keeping the positive tone throughout the call's duration. She hung up and motioned me to the desk."

    nurse "Your ID, Mr. Kano.{w} Head to 431 along the east wing. Dr. Shinozaki is expecting you."
    hk7 "Have a pleasant afternoon, madame, and thank you very much."

    window show
    nvl clear
    narr "The nurse returned to her mundane duty, waiting for another visitor to accommodate.{w} I, on the other hand, went off with my own business."
    narr "This is a source of fuel, alright. Hearing these moans and nervous laughter in the absence of light concocts the worst possible scenario imaginable.{w} It draws people in, dragging the sane to the patients' world of insanity."
    narr "Still not enough to challenge my mettle. I've seen far worse in recent memory.{w} It keeps bugging people endlessly, its reputation becoming more of an annoyance than genuine fear."

    nvl clear
    narr "A well-built figure came into view, followed by a lankier man in uniform.{w} The former, definitely Inoue's father. But the other authority figure looked unfamiliar. He walked towards me after their brief conversation."
    narr "He replaced a notepad and pen in his coat, exchanging it with a brown organizer.{w} As he passed by me, he slowed his pace."

    nvl clear
    window hide

    p_emm "Whomever that basket belongs to, I wish them well!"

    "A spontaneous individual, I must remark. Could be rude but friendly enough to be forgiven."

    hk7 "Someone sent their regards to you. The Pres says, \"Hi.\""
    p_emm "Ah, I recognize you just now! You must be from MSCI.{w} Take care of Lady Shinozaki in there. She just had a bad fit two days prior."

    "Then I stopped, truning my neck towards the inspector. On his face, a warm and gentle smile."

    hk7 "Hiroshi Kano. Pleasant afternoon to you, Inspector E."
    p_emm "I return the greeting.{w} Just be careful out there and straight home afterwards. Oh, and don't forget to return my regards to Ichirou!"

    "With a nod from me, he quickened his pace. His figure gradually became smaller until he was no longer in sight."

    mr_shi "If you don't mind, son, I'll handle the basket for you."

    "Though surprised, we exchanged firm handshakes and engaged in small talk for a few minutes.{w} He recognized me as Inoue's classmate during Sophomore Year. I felt more at ease. Even more when he invited me to his daughter's ward after ascertaining I visited alone."
    "At least this room tells a different story, only that the bed is obscured from the hallway's view by a curtain.{w} Her brother is present, laughing at the afternoon show's gags."

    mr_shi "We have a guest! Sweetheart, Hiroshi's come to visit.{w} Brought some fruits for you. Need to watch your nutrition, eh? You're starting to look like a scurvy-ridden sailor. {i}*chuckle*{/i}"
    is4 "Papaaaa! It's okay, Hiroshi. Welcome to my room."
    tomonori "Hey! What's up?"
    hk7 "I've seen better days. Can't imagine being cooped up here for days, let alone weeks. Though I admit, this looks better."

    "Unlike the patient it houses.{w} Inoue is unkempt, the traces of rehabilitation screaming from her appearance. She looks to disprganized to hold a decent conversation with, but certainly stable enough to keep herself together."
    "She forced a grin but couldn't come up with a clever remark.{w=0.5} Understandable."

    is4 "Finally, a change of wind! {b}*EXHALE*{/b} Ever since day one, that Emmerich guy comes to bombard me with questions upon questions without end!{w} How does {i}that{/i} expect me to recover?"
    hk7 "I see your point, Inoue. {i}*chuckle*{/i}{w} You need to loosen up a bit like usual."
    is4 "But, hey. I appeciate you dropping by this weekend. Thanks for the berries, too.{w} Don't you have more important things to attend to like...{w=0.5} sleeping? {i}*giggle*{/i}"
    hk7 "I thought of that, too. But you'll forgive me.{w} I'm afraid I have to resort to Mr. Inspector's routine for the day."

    "Her expression darkened, eliminating her eyes' radiance upon hearing that sentence."

    is4 "Good grief... How you've wasted your visit.{w} Overdose in medications and overdose of questions. You are aware how they {i}don't help{/i} with the situation, do you?"
    mr_shi "Now, now, dear. Calm down. Take a deep breath like I always tell you to."
    is4 "But Papa..."
    mr_shi "Inoue, please show courtesy to your friend. You don't get to see him every visit.{w} Besides, friends like Hiroshi-kun can understand your situation better, isn't that right?"
    is4 "..."
    mr_shi "Don't worry about it, son. She doesn't sulk this often back home.{w} Feel free to invite your friends to see her. It will surely lift her spirits up faster."
    tomonori "Except that one {i}persona non grata{/i}. You know -- rather, ought to know -- who."

    "An unwelcome guest, huh? Bet they had a suspect already. Didn't even bother to ask Emmerich earlier.{w} The question... who is this {i}persona non grata{/i}?"

    mr_shi "It's best if Inoue tells you. You can Tomonori afterwards -- he was present at the time.{w} Now, if you'll excuse me..."

    "He left the three of us in the room. Tomonori-san nodded at me as I approached the bedside."

    is4 "Tell me what you know so far."
    hk7 "That's an inversion...{w} Well, to start, we've been coordinating with the authorities, Emmerich mostly, and Kirisaki's family. After his burial, we discovered some interesting leads."

    "From the details of her disappearance to the unknown figure's appearance last Sunday, she heard the message delivered to us. Save for one thing."

    hk7 "I return the question and I want to hear from you personally. Who is this unwelcome guest your brother is speaking of?"
    is4 "You probably won't like my answer, but I have no choice..."

    "At an impulse, my ears leaned closer to her mouth.{w} Her voice felt shaky, and a glance told of her paling color."

    is4 "It's Sayo.{w} Every time I see her face on TV...{w=0.5} {cps=10}Every time I hear that transmission...{/cps}{w=0.5} {cps=5}Every time I close my eyes...{/cps} {i}*GULP*{/i}{w=0.5} {cps=5}Her voice... Her voice...{/cps}"
    hk7 "{cps=8}Inoue, breathe...{/cps}"
    is4 "{cps=5}Those{/cps} {cps=8}sinister intentions{/cps} {cps=10}hiding beneath that mask,{/cps} {cps=12}a mask so innocent, you'll never see it coming...{/cps}{w=0.5} {cps=5}Hehehe...{/cps} Hehehehehehehehehehe..."
    hk7 "Tomonori-san!"

    "Her brother rushed to our aid, soothing Inoue until she mellowed down.{w} I gave her a glass of water, hoping it would clear her head."

    is4 "Sorry for the outburst.{w} {b}*SIGH*{/b} Been like this for days."
    hk7 "I understand, but please refrain from doing that. You really terrified me."
    is4 "Perhaps my brother is up? I might risk another attack if I tell you more."

    "Tomonori-san obliged and motioned me to the far end. He prepared a monoblock for me to sit down."

    tomonori "Please keep this discreet. We regarded Sayo as a hostile presence after the incident. I'm sure my sis' reaction need no further explanations."
    hk7 "My mouth's zipped, but why? Sayo... of all people?!"
    is4 "{b}{i}*GROAN*{/i}{/b}"
    tomonori "Keep it down, please."
    hk7 "I'm sure she wouldn't do such a thing. You're up against slander charges if your accusation is false. Most importantly, what proof do you have?"
    tomonori "I know. I know. It's kind of hard to believe personally. Honest.{w} I wasn't on the receiver's side at the time."
    hk7 "So she phoned your house and the call was intended for Inoue. And then?"

    "From his hand appeared a flash drive, and he cupped it into my hands. Now, his claim is starting to gain substance, if little."

    tomonori "On the night of June 13..."

    window show
    nvl clear
    narr "After handling Inoue the receiver, he returned to watching TV, lowering the volume as courtesy. Occasionally, he would glance towards his sister and observe her throughout the call's duration.{w} When she moved to the window, he lowered the volume further to eavesdrop."
    narr "He went away from the living room some twenty minutes later to take a \"side trip,\" or so he says.{w} He hid behind the wall, making sure their parents were already in their room so the setup would not look awkward."
    narr "He concealed himself as he observed Inoue's conversation with Sayo up until the farewell exchange.{w} She was shaken, an expression he knew that would take some intense threatening to achieve."

    nvl clear
    n_is4 "Good night, Sayo. See you tom --"
    narr "She spoke the name, but the call didn't end just yet.{w} Instead, what followed is a short moment of silence from her end."

    nvl clear
    n_is4 "That's sweet, now would you please --"
    narr "Inoue was already irked at the caller, urging her to cut it out. She seemed tired, or..."

    nvl clear
    n_is4 "I need to sleep now, okay? Bye!"
    narr "She slammed the receiver, taking a few deep breaths as she stared at the machine.{w} He tried to approach her, but she was no longer in good spirits.{w} And from his observations..."

    nvl clear
    window hide

    tomonori "I know our youngest well enough. Too shaken to smile or weep a moment after. Instead, she spoke nothing, darted past me like I was a statue.{w} It was odd!"
    tomonori "Good thing we always record any transmissions from the landline. We don't usually listen to call logs especially if intended for someone else, but this is an exception."
    tomonori "That USB -- have a listen for yourself.{w} You wouldn't believe me anymore if even its contents I describe to you."

    "He went on, adding the time when they last spoke the weekend after -- about the alumna.{w} Her reaction to the call might have caused her fever, he speculates. Personally, agreeable."

    hk7 "Another point that bothers me -- Why'd you think it was a good idea to ring the Ronoroas after Inoue's disappearance?{w} Have you any evidence at the time, too?"
    tomonori "What I just gave you."
    hk7 "{cps=5}Yeah... no.{/cps} Maybe not this time.{w} You discounted the fact that she could be innocent -- Heck, that allegedly threatening call could just be a silly prank! We three have been classmates in First Year. It's natural to view it from {i}that{/i} angle."
    hk7 "Besides, how do you even smuggle two people out of the campus that same morning undetected? How do you propose Sayo could have done it?{w} Face it, you don't have anything."

    "He bit his lip, shaking his fists in contempt and eyes glared at me."

    hk7 "But I suppose I must give you the benefit.{w} Let's hear it now. Brought a laptop with you?"

    "A light shake. Instead, Tomonori-san scrawled a note on a Post-it, wrapped it around the flash drive, and asked me to pocket it."

    tomonori "Reach me by phone when you're done. Only then you can confirm we're not making this up."
    tomonori "Whatever you do, share this to no one. Don't bother with the inspector -- he already owns a copy."
    hk7 "But please, know that I am accepting this on one condition. Whatever conclusion I reach from the contents of this device, I will stand by it until further evidence is produced."
    tomonori "As you wish, Hiroshi."

    "The door opened.{w} Mrs. Shinozaki entered the room, acknowledging my presence. She set her large shoulder bag down at the bed's foot. It contained toiletries and some extra clothes, presumably for Inoue."
    "Inoue and her mother enjoyed the apples I brought while discussing some petty affairs.{w} She looked better than she was a while ago, back to the familiar vibe I've known her since."

    is4 "Hey, you should drop by more often. Though, I think I won't be staying here for long. Who knows?{w} How are things back in MSCI?"
    hk7 "I'm the newly-appointed head of the Science Club. No need to celebrate nor congratulate me. Hahahaha!{w} And... Miyu's been performing his duties well as you substitute."
    is4 "Knew that guy had it from the beginning. I should make it up to him once I'm out of here. A sense of gratitude or a small token will do."
    is4 "And I wish you all the best. May things not go awry next week."
    hk7 "Yes. Yes. Thing must {i}not{/i} go awry..."
    is4 "I'll be seeing all of you, then? Gvie my regards to Ms. Harada in case she might not drop by."
    hk7 "Maybe? Haha! Of course you will!"

    window show
    nvl clear
    narr "I bid them farewell at three, exchanging handshakes with everyone sans Inoue -- she preferred a fist bump.{w} Along the way, I encountered Dr. Shinozaki. He stopped to share some last words before parting ways."
    narr "The sweet nurse is still there, albeit alone this time. She deserves my thanks.{w} Strangely enough, the ride down felt much lighter, erasing the negativity it gave off initially."
    narr "Out the front lobby and into the heat outside, I activated my umbrella.{w} Breezy air, but the sunlight's intensity is enough heat stroke upon an unlucky bum."

    nvl clear
    narr "The rest of the afternoon felt happier, applying a fluid motion to my thoughts.{w} It was close to Nirvana, if not the concept itself. How I value the sound of silence whenever I'm alone at the house."
    narr "I sat alone at my desk, examining the items I received from Tomonori-san. Unwrapped from the paper, with his cellphone number, is the flash drive.{w} I took a moment to collect my thoughts while there was still silence."
    narr "What soon followed is dusk... a subversion of the afternoon's story.{w} {cps=15}This oncoming eclipse... why does it not ease me as it's supposed to do?{/cps}{w} Nevertheless, I readied the family desktop, device in hand."

    nvl clear
    window hide

    "{cps=10}The upliftment was a lie...{w=0.5} Things must {i}not{/i} go awry...{/cps}"
    return

label ch02_07_security:
    scene black with fade
    "JULY 8, 2013 - 0630H"

    window show
    nvl clear
    narr "All the set pieces are in place."
    narr "Sayo has left IV-E early to prepare for the flag ceremony, joining the rest of the Council on the second floor."
    narr "An endless stream of students dashed through the gate and into their classrooms, hoping to settle down before the bell rang.{w} There were at most three activities seen in every classroom: general cleaning, homework cramming, and, for the happy few, sleeping."

    nvl clear
    narr "The class presidents rounded up their respective classes and formed a line on their designated spots.{w} Just as how colorful each level is when they are all wearing their PE uniforms, the same can be said for each officer. Some are benevolent, others stoic and drill sergeant-like."
    narr "But the extremes are unmatched with the clouds preluding an oncoming rainfall by mid-morning. Truly, the heavens weep with the mortals; rather, it is about to."
    narr "At 6:40, the Council's Vice President appeared on the balcony, commanding the students to settle down. And within a minute, they followed."

    nvl clear
    narr "First up, the National Anthem. The beat was conducted by the secretary while the Boy Scouts raised the country flag.{w} Sayo Ronoroa led the opening prayer, the Pledge of Allegiance to the Flag, and the Patriotic Oath."
    narr "Three more songs followed, the beat conducted by the Vice President save for the last: the Hymn of Department of Education - Kutsutochi, Kutsutochi's Hymn, and their school song, \"Pride of the Land, Eternal Glimmer.\" This was conducted by Sayo."

    nvl clear
    narr "A new sheet of silence covered the quadrangle."
    narr "The principal, Mrs. Sokoguchi, welcomed the students on their sixth week in MSCI.{w} She gave a few remarks about the prevoius week and made a few small announcements afterwards."

    nvl clear
    window hide

    prin "With that done, I would like to mention that we have a special guest joining us this afternoon."

    "The student body cooed, heads turning and tongues whispering about who it could be."

    prin "Few of you, especially the Seniors, must have glimpsed upon our guest the previous month.{w} I would like to apologize for any potential trigger, but he is the lead investigator of the Kyou Kirisaki murder case."

    "Silence.{w} This time, it felt darker.{w} How insensitive could that remark be?"

    prin "My apologies once again, but he gave his time for you to make an important announcement, especially those who inquire us of our own safety. Ladies and gentlemen, Inspector Harold Emmerich."

    "A thunderous applause welcomed Emmerich, maintaining his composure throughout his introduction. Not as bad as the girls thought -- a rather handsome young man."

    student "Is he married? Is he already taken? Boy! He's dreamy!"

    "Emmerich cleared his throat and began his speech."

    p_emm "Good morning, and I appreciate the compliment. Actually became the class escort twice in my days. {i}*chuckle*{/i} If there are any other compliments or insults, let us attend to those later, but for now, I have to discuss an important matter with you."
    p_emm "I would like to apologize for reminding everyone of the recent tragedy, inasmuch as we're throwing everything we can to end this case before anyone else is involved. And the weather seems to agree with me."
    p_emm "You may have been imposed upon a curfew for the past few weeks -- it's for our own goodwill. What I bring today is relief, not burden.{w} Ms. Sayo, would you please pass me the...{w=0.5} Thank you."

    "He possessed a small remote control, pressing one of the buttons on its face."

    "{b}*BEEP*{/b}"

    "Around the campus perimeter, various spots of red glimmered. They divided the attention of the students, each wondering what these were for."

    p_emm "The police and school officials came up with a contingency plan the previous week. Over the weekend, we installed various CCTV cameras on key locations around the campus, wired to the school security system."
    p_emm "The cameras are linked to our station, as well as the front desk guard station and the offices. They are active 24/7, with an emergency generator in case of a power interruption."
    p_emm "Don't bother trying to trick the system.{w} We gave strict orders to impose penalties upon those who are caught tampering with the devices. But I trust you guys wouldn't go that low, would you -- the cream of the crop of Kutsutochi?"

    "The students gave an affirmative response in a loud chorus."

    p_emm "Now, on to my second point.{w} My senior and I agreed not to disclose details of the ongoing case, but we have decided to make an exception. Keep this among yourselves or your family, please. We've had enough with the media's involvement."

    "The inspector walked to the sound board and lowered the volume. In turn, the students anticipated his next words in silence.{w} Ichirou, Sumiko, Ayumi, and the rest of the class presidents moved forward."

    p_emm "{cps=15}The circumstances of the disappearances last month...{w=1.0} we suspect an inside job --{/cps}{nw}"
    ys6 "I knew it!"

    "After hushing him and a few others who voiced their support of this theory, the rest of the students caused an uproar.{w} Efforts were made to quell them, but the fear and anger overshadowed the firm pleads of their leaders."
    "Mrs. Sokoguchi snatched the microphone from Emmerich."

    prin "Silence!"

    "And silence they returned."

    prin "I understand how you feel and why the recent developments sound improbable, but we {i}need{/i} to make sure.{w} We haven't identified a suspect yet as even circumstantial evidence is insufficient. For now, all of the students and staff are innocent."
    prin "Please compose yourselves and remember to show some decency next time. Thank you."

    "Heads were hung in shame, and the inspector sympathized with them. He took the center stage once again."

    p_emm "My sincerest apologies... {i}*sigh*{/i} My senior was right to see this coming.{w} But, as our principal mentioned, we have zero persons of interest. There are suspicions but stay as suspicions."

    "Probably like animals tamed with their tails between their legs, the students remained silent. A thousand pairs of eyes eerily stared towards him."

    p_emm "{cps=10}Since I have nothing further to add, I... hope you all have a pleasant day.{/cps} I should be going now -- I'll entertain some questions later when we meet.{w} Thank you for your time."

    "He received another round of applause, albeit of lower intensity than before. He shook the Council members' hands and talked to Mrs. Sokoguchi for the moment."
    "Sayo stepped forward, giving the final announcements of the morning."

    sr5 "Let the officers of the following stay behind and meet us in the Council office: Science Club, Mathematics Club, and English Club.{w} The rest, you may go to your respective classrooms. Have a pleasant day."

    window show
    nvl clear
    narr "Hiroshi, Miyu, Ayumi, and their fellow officers deviated from the crowd and congregated at the central staircase.{w} A few moments later, Emmerich and Mrs. Sokoguchi descended from the staircase. The former exchanged handshakes with them."
    narr "Sayo fixed her blouse, appeared from the staircase and led the party to the office."

    nvl clear
    narr "She gave the officers handouts -- the program flow for the whole week.{w} Gathered at one side are two-hundred bundles of reviewers covered in plastic, waiting to be distributed later."
    narr "Other than that, there were no changes to the office -- no red dot or electronic devices mounted on the walls."
    narr "They gathered around the conference table. Sayo preceded the brief meeting."

    nvl clear
    window hide

    sr5 "You all ready?"

    "Though her smile forced, the officers responded cheerfully. It brightened their morning even if just a bit."

    sr5 "Let us start. I have given you a timeline of events. Please, have at least one copy for each club. How you will conduct and what you will discuss during each session is up to you. Just keep our fellow Seniors in mind, alright?"
    hk7 "If I may, I have a request."
    sr5 "Proceed, Hiroshi."
    hk7 "We feel it would be unfair for the students if we cram all the topics of Science in one week.{w} May we have an extra week, or at least, extra sessions to accommodate that?"
    sr5 "I must agree. And am I right to assume the other clubs are requesting the same? Miyu? Ayumi?"
    mh8 "I second the motion. Reinforcement is necessary especially since we do not want ourselves to burn out if we rush things."
    ayumi "We feel the same, especially if the extra week is for our own goodwill."
    sr5 "Carried. We shall arrange the schedule for the second set with teachers later. Any other concerns?"

    "All heads shook at her inquiry."

    sr5 "None?{w} I wish you all the best, and strive for the better! Your excuse letters are already with your respective teachers so you can conduct your activities without worry."
    sr5 "Keep in mind that you do {i}not{/i} and must {i}not{/i} preempt your non-major subjects for a session.{w} Only exception, if it is requested by the teacher."
    sr5 "Meeting adjourned. Godspeed!"

    "Thus, like sheep, they set out to fulfill their duties.{w} Sayo stayed behind, arranging some papers before heading to class, going back and forth between the conference room and the office."
    "Her eyes darted around the room, trying to think of something she forgotten. She dismissed it and returned to work."

    sr5 "The brain is confused at sunrise, and stays the same at sunset...{w=0.5} Probably not. {i}*giggle*{/i}{w} What am I even thinking? Too early in the morning for entertaining weird thoughts."

    "She finished her errand and took one final scan of the room."

    sr5 "God is watching us. He'll be our camera even in darkness."

    "She made a cross and left the room."
    return

label ch02_08_review1:
    scene black with fade
    call ch02_08A_phonecall

    return

label ch02_08A_phonecall:
    scene black with fade
    "{color=#bd0000}\[Day 2\]{/color}\nJULY 9, 2013 - 1130H"

    window show
    nvl clear
    narr "At around lunch time, as usual, Sayo made a quick stop to the council room to attend to some reports sent there for the day."
    narr "The green light on her phone desk blinked, and the LED screen showed one new voice message.{w} She started the recording, and her own sweet and mellow voice spoke the first sentences."

    nvl clear
    narr "{i}Good day. Student Council President here.{w=1.0} While I understand this may be of utmost importance, I am not able to attend to this as of present.{w=1.0} Please leave a message after the beep.{/i}{w=1.0}{nw}"
    narr "{i}{b}*BEEEEEEEEEEEEEEP*{/b}{/i}{w=1.0}{nw}"
    narr "{i}Good morning, Sayo. Inspector Harold Emmerich speaking.{w=1.0} Pardon the sudden call, but there seems to be a matter of concern regarding the current state of investigation.{w=0.5} As soon as you receive this message, please contact me immediately.{w=0.5} Thank you.{/i}"

    nvl clear
    narr "Sayo shook her head, expecting to have her lunch be cut into half once again.{w} But if it would help resolve Kyou's murder, then why remain silent?"
    narr "She input the numbers to the Regional Police, and after a few moments, a desk sergeant answered from the other end."

    nvl clear
    window hide

    officer "Capital Region Police District. How may I help you?"
    sr5 "Good morning, office. This is Sayo Ronoroa from Maria St. Claire Institute.{w} I happen to have an on-the-phone appointment with Inspector Harold Emmerich. Could you please fetch him for me?"
    officer "Yes, Ms. Sayo. He did mention your name. I'll pass the line to his office immediately."
    sr5 "Thank you, officer."

    "While waiting, Sayo sat back on her chair, took a deep breath, and rested her eyes."

    p_emm "Hello, Sayo."
    sr5 "Inspector Emmerich! I suppose you have taken your meal for the afternoon, eh? Hahahahahaha."
    p_emm "That will have to wait after this conversation.{w} There are just a few things I need to clarify regarding the phone call last June 13. Do you mind if I record this conversation as your testimony?"
    sr5 "That will be no problem."
    p_emm "Thank you.{w=0.5}{nw}"
    p_emm "{i}This is Inspector Harold Emmerich. Timestamp: 9th of July, 2013 at approximately 1135H. Currently interviewing a witness named Sayo Ronoroa, Case File Code MH-0810.{/i}"
    p_emm "We may begin."
    sr5 "Before we do so, I must say there are far too many points to discuss. Could you please specify what this is about?"
    p_emm "Certainly. I won't take long.{w} You are aware that you've contacted the Shinozaki residence on the evening of June 13, and that you've spoken with Ms. Inoue Shinozaki?"
    sr5 "That is true. I did have a conversation with Inoue. If I recall, she looked unusually spooked the following day, probably from what transpired in that conversation."
    p_emm "Spooked? What did you talk about, if you don't mind the intrusion?"

    "Sayo tapped her finger on the desk, rotating the chair to shorten the wire's length. After pondering for a moment, she continued."

    sr5 "Allow me to give some background on what I am about to say."
    sr5 "Ten of us, {i}(lists names){/i}, gathered in front of the auditorium to bond -- play games and share stories since it was our last year in high school. I was only invited by our auditor, Akira, since it was arranged by Ichirou."
    sr5 "I forgot to take my music book with me after the First Friday Mass and I couldn't just go back because the auditorium was already plunged into darkness. Luckily, Miyu volunteered to search for it. Gallant and kind-hearted child, I must say."
    sr5 "We divulged into campfire stories, eventually leading to real discussions about the supernatural -- the case of Ikari Suzumoto, and eventually, the Sacred Heart Curse Killings."
    sr5 "As soon as Miyu returned and he found my music book, we all went home. I remember Inoue looking forlorn so I asked her about it. She said she was curious to learn the details of the case since...{w=0.5} I'm not sure myself."
    p_emm "I'm sure she was. I remember it too well..."
    sr5 "Inspector? Is something the matter?"
    p_emm "So, you approached her, and...?"
    sr5 "I told her to take her mind off of it. It only occurred to me later on that we were the same number as the Sacred Heart victims. Inoue initiated a count-off just before Miyu returned."
    sr5 "Since we were former classmates, I decided to give her a helping hand just like before. I promised to research about the case and relay my findings as soon as I organized my notes."
    p_emm "Why didn't she do it herself? The information is already available on the internet."
    sr5 "Let's just say I have connections, inspector. I have a better chance of gaining rare information through special means -- the psychology of the crimes, as some would put it. It's my specialty."
    p_emm "I understand. At least one point is cleared up."

    "Sayo glanced at the clock. The minute hand was nearing the 45-minute mark."

    sr5 "How is she doing, inspector? I haven't had a chance to visit Inoue ever since she was rescued."
    p_emm "Hmmmmmmmmm..."
    p_emm "How should I say this?"

    window show
    nvl clear
    centered "{cps=30}{i}Let me guess... I have heard that momentary silence too many times in movies and in television.{w=1.0}\nWhat are those instances?{w=1.0}\nIs she in the ICU, going 50/50?{w=1.0}\nDid she disappear from the hospital and was already missing for a few days without us knowing?{w=1.0}\nDid I do anything to upset her?{w=1.5}\n{/cps}Oh, of course!{w=0.5} I know exactly why...{/i}"

    nvl clear
    window hide

    sr5 "I suppose I should wait for her to come back physically in MSCI, then. I'd love to sit down and chat with her."
    p_emm "Very good, Sayo. I think the same."
    sr5 "You know, should you have the time to visit her once again, could you check if she received the modules we sent her?"
    p_emm "She was reading her lessons the last time I visited her. No need to worry, Sayo."
    sr5 "Greeting card? Did she get any?"
    p_emm "Not sure, but one of your friends did pay her a visit. Know anyone named...{w=0.5} uh..."
    sr5 "Hiroshi Kano."
    p_emm "Yeah, Hiroshi!{w} He even brought her a fruit basket. How'd you know?"
    sr5 "Our good auditor told me. He and Hiroshi are close friends, too, you know."
    p_emm "I see.{w=0.5} Anyway, I'll end the recording now.{w} I think you still need to eat, Sayo. Sorry for bothering you on such a busy day."
    sr5 "No, no. As long as I know you're doing this for the truth, that will be enough for me.{w} I, too, am searching for the answers my own way{w=0.5}-- the legal way."
    p_emm "I expected no less from an MSCI student.{w} I will look forward to hearing from you again soon. Who knows, we might even have a discussion on our findings should your ever pursue an independent investigation."
    p_emm "Rest assured, we will be one step close to solving Inoue and Kyou's abduction, as well as to bring justice to the latter's murder.{w} Thank you for your cooperation, Sayo."

    "The line cut, Sayo placed the receiver down.{w} Instead of returning to her paperworks, she gathered them into a folder and placed them inside the drawer."
    "She stared at the clock in deep thought, watching it tick down as the minute hand approached twelve."

    sr5 "What wrong have I done against her?{w} Ever since that incident, never a night passed without that question emerging from the mind's depths.{w} If I seek my answers now, it might only worsen the situation. Imagine what can spark from a flame that no one but the two of us can see."

    "When the minute hand struck twelve, Sayo rose from her seat and walked towards the canteen.{w} She slowed her pace after two classrooms and looked behind towards the school gate."

    sr5 "Was it a grave mistake after all?"
    return

label ch02_09_facts3:
    scene black with fade
    "{color=#bd0000}\[Day 3\]{/color}\nJULY 10, 2013 - 1300H"

    window show
    nvl clear
    narr "The entirety of one side of the room was filled with images of the campus.{w} Only one officer was assigned to watch the live feed until the end of his shift at 6 PM."
    narr "Emmerich accompanied him.{w} He tucked himself into a corner with his laptop -- a sound recording application open -- and headphones fully covering his ears. He was comparing the voices from the recording Tomonori gave him and his recorded phone conversation with Sayo."
    narr "The contours were similar, as he suspected, in accordance to similarity in pitch and tone by Inoue's testimony.{w} Supported by her brother's statement, Emmerich came to one conclusion."

    nvl clear
    window hide

    p_emm "You know, in my days as a crime lab assistant, I have examined several voice clips myself.{w} The voice -- aside from Ms. Shinozaki's -- is unmistakably Ms. Ronoroa's."
    officer "And that makes her a suspect? Don't you follow rules using voice clips as evidence?"
    p_emm "Of course, we can't discount her, even though she openly admitted that voice was hers. Still, as they aren't as solid as videos and photographs, these clips have their flaws.{w} There is one more question we must ask."
    officer "And that is?"
    p_emm "Is there anyone who can replicate such a voice?{w} I'm not saying she's hiding something by the way she testified on the phone, but let's consider the improbable."
    p_emm "I say Ms. Ronoroa's voice belong to a thousand other people. Far-fetched if you consider our current pool of suspects, but is yet to be proven impossible."

    "Unsure about his response, Emmerich's companion returned a puzzled look.{w} Whether his theory is serious enough is another question entirely."

    p_emm "Put it this way. By \"replicate,\" I meant having essentially a similar voice as hers. If I am right about what your face is telling me, perhaps such a theory is indeed impossible."
    p_emm "Who knows, it might have been a naughty jester's ploy all along. And the abduction case that soon followed we only thought connected just because they involve a common person -- Inoue Shinozaki."
    officer "I don't know, Harold. Can't find anyone else in the force who would have a theory wilder than yours."

    window show
    nvl clear
    narr "At that moment, the office door opened.{w} The two officers turned their heads to look, and gave Sergeant Deitch a salute once they saw it was him."
    narr "In his possession is a brown envelope, containing reports related to the current case.{w} He handed it to Emmerich and pulled a vacant chair towards him."

    nvl clear
    window hide

    p_dei "You know, my boy, I don't think my time is up yet."
    p_emm "Maybe the Higher Powers bid you to accompany your protégé for one last journey."
    p_dei "Seems to be.{w} This and MH-0809...{w=0.5} {i}*sigh*{/i} God, please let MSCI not be another guinea pig playground of a psychopath."
    p_emm "We have until the end of the month to see if your prayer will be answered. I vote for renumbering the code after the deadline has passed."

    "Emmerich studied the documents he was given, and his superior took cursory glances at the monitors."

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

    "Deitch glanced over to Emmerich's notebook. He only shook his head."

    p_dei "Leave nothing potentially important, Harold."
    p_emm "I've already skimmed through the report three times, sir. I can always refer to this at any time."
    p_dei "Certainly, you should; that is, until the final report is out after a few more weeks."
    p_emm "Understood."
    p_dei "I've been thinking. If you could wrap this up before Christmas, then perhaps I made the right decision after all."
    p_emm "You are far from your retirement, Sarge. Mid-50s I'd hardly call a retirement age range.{w} Why don't you serve the force for a few more years?"
    p_dei "Young ones understand most of the world we're living in the present, while we, the old-timers, are already well beyond our prime. Now, it's only us against Father Time."

    "From his pocket, he produced a cigarette stick and a lighter.{w} Emmerich and his companion silently protested, though they were used to the sergeant's smoking habits within the precinct rooms."

    p_dei "I wonder{w=0.5} if all will be the same, after all?"
    p_emm "If it is inevitable, then there is nothing I can do.{w} But sir, come what may, I shall personally see this case to a close... even if it takes me a decade!"
    p_dei "{i}*chuckle*{/i}You speak big words, my boy. Why don't you surprise me more just like how you convinced me to uptake you as my successor?"
    p_dei "You think this is already at the middlegame, but trust me Harold, we are still at the opening. And I'm sure our finicky cat would agree."
    officer "Me, Sarge?"
    p_dei "No, of course not you, donut-boy!{w=0.5} Our bait, the snitch!{w=0.5} He goes by...{w=0.5} whochamacallit?"
    p_emm "Alias L.C., whatever it means."
    p_dei "Yes. Yes. L.C...{w} We searched through the records of every community here in Kutsutochi. There are several names here and there with those initials, but we ended up finding one of two things."
    p_emm "Either the person of interest is deceased or out of town."
    p_dei "I'm not sure about the \"out of town\" part, Harold. Although, you are correct.{w} Guess it's another dead end for now."
    p_emm "Or not."

    "The sergeant looked at Emmerich inquiringly.{w} Deitch nodded as he saw Emmerich's laptop screen."

    p_emm "If we could find the truth from Ms. Ronoroa and Ms. Shinozaki's friends regarding this, then we may have another string to follow."
    p_emm "Who really is this L.C. that Ms. Shinozaki described? What are their plans and motives?"
    p_dei "Questions and more damn questions that keep popping up by the day. It looks like she's starting to rub off on you. How is she, anyway?"
    p_emm "She needs time to recuperate after that grand emotional drain. Looks like it's just you and me for now, sir."
    p_dei "I guess I'll hang around the spectators' seats, my boy. Perhaps it's my age speaking, but I still can't wrap my head around the opprtunity.{w} How were they whisked out of the campus on a school morning? I think it's better if you answer that first before anything."
    p_dei "And if you can't do it yourself, I wonder how close you'll arrive at the answer before you require assistance?"
    p_emm "How, indeed..."
    return

label ch02_10_review2:
    scene black with fade
    call ch02_10A_preparations

    return

label ch02_10A_preparations:
    scene black with fade
    "{color=#bd0000}\[Day 5\]{/color}\nJULY 12, 2013 - 1645H"

    window show
    nvl clear
    narr "Immediately after the Club and Organization Day activities ended, the students, save for a select few, headed straight home.{w} Sayo, leaving IV-E to its class president, Ayumi, headed to the council room to prepare for a meeting."
    narr "Once inside the office, Sayo (and Akira, who joined her a bit later), prepared the conference room.{w} Akira moved the whiteboard behind her seat and prepared a few markers and erasers."

    nvl clear
    narr "Within the next fifteen minutes, the Student Council officers took their designated places."
    narr "The secretary prepared her notebook to record the minutes and Sayo wrote the bullet points of the evening's agenda."
    narr "At exactly 5:10 PM, every one required to attend the meeting -- including the club officers and assigned marshals -- was already present."

    nvl clear
    window hide

    sr5 "Let's see. All Student Council officers accounted for: Ronoroa, Yasuda, Tanaka, Dojima, Ichibana, Watanabe, Orihime, Onizuka."
    sr5 "And the club officers with us today: Kano, Tokubei, and Suzuki from the Science Club;{w=0.5} Hirano and Yamamoto from the Mathematics Club;{w=0.5} Nakashima and Mimori from the English Club."
    sr5 "Alright! A pleasant afternoon to all of you.{w=1.0} First, I would like to thank everyone for your time and dedication for the whole week. We can safely say the review sessions are successful."
    sr5 "I also acknowledge our teachers who, likewise, coordinated with the City Office to provide us with review materials.{w=1.0} Have you chosen your college yet?{w=0.5} I sure have."

    "{b}*APPLAUSE*{/b}"

    sr5 "Next, will the representatives of each club report on their progress for the week? If you have any suggestions, like those raised from our pre-event meeting, you may choose to raise them during your report or at the end."
    sr5 "Hiroshi, the Science Club first."

    "Hiroshi stood up and borrowed the notes from Sumiko."

    hk7 "As a school for the sciences, we contacted MSCI alumni to assist us with the topics.{w} We asked them to describe the general situation on the Science parts of the various entrance exams."
    sr5 "I take it you filtered those from the Big Four and those that are not?"
    hk7 "Exactly.{w} Out of the fifty respondents we interviewed, Chemistry seems to be the common bottleneck and mostly varied of the natural science.{w=1.0} This is followed by Biology, General Science, and Physics by a wide margin."
    st3 "Additionally, on the review proper, we focused mostly on Stoichiometry, as most of the test items involved that. Plus, there seems to be a problem, for the majority, with calculation."
    st3 "Of course, with the Mathematics Club, we discussed how would we review the students regarding word problems and any mathematical concepts some questions might entail."
    st3 "But that we leave to Miyu's team. It's more on their area of expertise, I should say."
    ai2 "Wrong possessive, Sumiko.{w=0.5} It's {i}his{/i}."

    "The room burst into laughter, leaving Miyu red-faced."

    sr5 "Hiroshi, if you may continue, please."
    hk7 "Thanks, Sumiko.{w} Since Science is inarguably the largest area of the pie, we decided to split ourselves into three teams."
    hk7 "I'm the team leader for Biology, Yoshiro for General Science and Earth Science, and Sumiko for Chemistry and Physics because he's that awesome.{w=0.5}{cps=15}.. Not to downplay our contributions as a whole of course.{/cps}"
    c_vp "I have a question. Do your teams still coordinate with each other in terms of crossing into other fields of Science?{w=0.5} Or, wait..."
    sr5 "I've personally seen some of them handle areas even if they are not assigned to those teams, especially if no one is available. I don't see any problem with it."
    c_vp "Or better, since it was already obvious... {i}*chuckle*{/i} You've mentioned Stoichiometry as the primary focus of Chemistry.{w} What about the others -- Biology, Gen. Sci., Earth Sci. and Physics?"
    hk7 "For Biology, the bulk of the questions were on Physiology and Anatomy...{w=0.5} which I will be getting into now."
    hk7 "As everyone here has experienced how complex the processes involved in energy circulation, we had to slow down our pace for the students to digest the explanations more easily. We also introduced mnemonics."
    hk7 "And for the rest, we asked the students to keep a copy of the handouts we gave. They contain bullet points from almost every topic in Biology.{w} We tried to cover as much ground as we can, but we didn't finish as expected."
    ys6 "We did not do much on General Science.{w} However, our team covered the essential information the students need about the Earth's structure and the various phenomena occuring around it."
    ys6 "We touched a few concepts in Biology and Physics such as ecology, force, and the like. There was also a bit of Geology involved, but we only covered the essentials."
    ys6 "That's it from me."
    st3 "The materials we were procured with covered Physics from end to end.{w} As such, we focused more on the applications and mathematics behind each major concept. I'd wager at most five questions per topic."
    hk7 "Though we admit,{w=0.5} even if we covered all the areas required for the entrance exams, it would be no use without constant reviewing and application."
    hk7 "In summary, we enforced the ideas behind each topic. None of us expect the students to have retained their stock knowledge after over three years."
    sr5 "Thank you, members of the Science Club.{w} I agree with your viewpoints and methods in handling your parts of these sessions.{w} The surveys made during the first three days showed favorable results."
    sr5 "Now, if there are no further questions, we shall move on to the Mathematics Club.{w} Miyu, please begin."
    mh8 "I confirm Sumiko's statement earlier."
    mh8 "The problem with most of the students in test-taking lies on two aspects: reading comprehension and fact-finding,{w=0.5) both of which are necessary for problem solving."
    mh8 "Likewise, we found Mathematics to be too large of a subject to merit each area equal attention."
    mh8 "We split our team into two.{w} I handled the parts involving Geometry and Trigonometry, while we \"imported\" Ichirou to focus on Algebra."

    "This stirred up a discussion among the Student Council members. Sayo watched the other members calmly."

    c_4r "If I may raise an objection.{w} I thought it was already implied at best that the Science Club members were spread thinly among three teams."
    c_4r "Furthermore, may I remind everyone that Ichirou is the secretary of the Science Club?{w} Why would you not delegate Algebra to a member of your own club?"
    hy10 "Onizuka, I think that question is directed at me.{w} Miyu assigned me as the lead handler for Algebra, if you noted my attendance at the pre-event meeting."
    hy10 "In reality, we couldn't find a good substitute for Inoue until the last minute. I actually didn't want the part since I thought I may not handle things well.{w} Instead, we sought Ichirou's help despite being in another club. With Hiroshi's approval, he replaced me from Day 2 onwards."
    c_4r "Hiroshi, can you confirm this?"
    hk7 "There was an agreement between our club and theirs to lend out Ichirou.{w} This is due to their lack of manpower and members willing to spearhead the sessions."
    hk7 "We understand the situation fully, mind you.{w} In a similar vein to Yoshiro substituting the late Kyou Kirisaki in Gen. Sci., Miyu asked for Inoue's substitute in handling Algebra."
    hk7 "We possess an official document should you wish to view it.{w} Sayo and Tanaka should have a copy each."

    "From the drawer, the secretary produced a signed agreement between the two parties involved.{w} He passed it around the table."

    sr5 "Does that answer your question, Onizuka?"

    "He nodded, satisfied with the document, and motioned Miyu to continue."

    mh8 "Now that we have dealt with these trivial matters, let us proceed with our findings."
    mh8 "We aimed for mastery of the topics -- formulas and conditions for each, and the mathematical basis of each problem."
    mh8 "Once the students mastered the problem-solving process, we would then focus on techniques and shortcuts.{w} We applied Singaporean Math to shorten their solving times."
    mh8 "We held surprise unit tests during Calculus and Analytic Geometry, courtesy of our teachers. As a precaution, we did not choose the questions, of course."
    mh8 "I don't think the students found Geometry troubling.{w} We already have the theorems memorized and derivations grasped, what with the rigorous proving we've done in Third Year?"

    "\"Hahahahahahahahahaha...\""

    sr5 "I see.{w} But who will give the report on Algebra on Ichirou's behalf?"
    hy10 "That would be me.{w} I may have turned down the role, but I still stayed on his team."
    sr5 "Give us a rundown, Hikaru."
    hy10 "Like Miyu said, the students did not find Geometry that difficult.{w} Algebra is a different matter, however, as it relied more on word problems than figures."
    hy10 "On Ichirou's suggestion, we focused more on Intermediate Algebra and a bit of Precalculus.{w} The hows, whats, whys, and wheres -- closest description I can think of. Like Miyu, we focused on those aspects."
    hy10 "Although, we factored in those who attended Saturday Math classes before.{w} They had a higher learning curve than average, so they helped us identify those who were struggling with Math."
    hy10 "Because, you know, not everyone is good with numbers and letters.{w} That's it from us."
    sr5 "Thank you, Miyu and Hikaru.{w} Since Ichirou is, as you say, a team lead for your subject area, I shall speak with him tomorrow or Monday when we meet. Still, your report is sufficient, Hikaru."
    sr5 "It's already twenty minutes to six -- ten minutes past the curfew.{w} Ayumi, how did the students fare on English?"
    ayumi "Everyone has a good grasp of the subject, we must say, if the results we've got accurately represent their performance."
    ayumi "In addition to grammar and reading exercises, we also held five-minute writing exercises to test the students' articulation.{w} Its purpose is to prepare them for essays in case there would be any."
    ai2 "Let me guess...{w=0.5} You also split your handlers into teams?"
    ayumi "Predictably."
    ai2 "You all seem to be into this \"splitting into two\" business. Is that an ongoing trend?"
    ayumi "Why, yes! That's because one is never satisfactory enough nowadays, isn't it?"

    "\"Hahahahahahahahahahahahahaha!\""

    ayumi "So, I handled the grammar and writing sessions. Ikuko's team focused on reading comprehension."
    ayumi "There is nothing much to report aside from what I've said earlier.{w} We focused on repetition and enforcement of grammar rules, not unlike what our English teachers are doing. We found those to be major contributing factors to the students' great performance on the subject."
    ikuko "Though we wouldn't say the same for reading comprehension.{w} This is the basis of problem-solving as already mentioned a few times."
    ikuko "In general, the students are expected to collect and retain important facts from each passage to answer some of the basic questions.{w} Then, they collate them together to deduce a reasonable main idea and other inferences that can be made."
    ikuko "Unfortunately, recognizing connotations and metaphors are just half of the problem. What more if we ask them which theories apply and what themes are present for each text?"
    ikuko "Time is the greatest enemy of every student.{w=0.5} There were only a few who finished the sample exams when it came to our segment."
    ikuko "It was then we switched to the recommended approach: questions first before the text.{w=0.5} The students finished more quickly that way.{w} Then we asked ourselves, is there another way?"
    ayumi "Thus, we decided to incorporate Mathematics and Science into our sessions through one means --{w=0.5} applying logic."
    sr5 "Why do you deem this necessary?"
    ayumi "Because we believe that motive is the most important element, both in terms of the characters and the writer.{w} Whether the laws governing each world are rigid or nonsensical, surely there must be a semblance of reason for the readers to comprehend."
    ayumi "From there, we can make conclusions and interpretations on both literary and meta levels."
    ayumi "If the readers lack motive -- driving questions, though provided -- themselves, how can they expect to ace the test, right?"
    sr5 "In the course of finding the answers to the provided questions, you are correct in asserting that idea.{w} But it is still their decision whether to dig deeper, since these questions are always not enough. More than the motive, impact also matters."
    ayumi "Exactly.{w=0.5} And when time runs short, they realize that they should not have dwelled upon each passage for too long. There is no definite telling whether the problem lies in the method, motive, or impact, for it is subjective."
    sr5 "Very well said.{w=0.5} Thank you for your interesting insights."

    "After another round of applause, Sayo stood up and walked towards the whiteboard."
    "{i}*RRIIIIIIIIIIIIIIIIIIINNNGGG*{/i}"
    "It was already six in the evening -- second bell after curfew.{w} Some of the attendees looked frantic, tapping their watches to remind Sayo of the curfew."

    sr5 "Not to worry. The front desk is just a few doors away.{w} Mrs. Genkai won't leaving until the meeting is adjourned."

    "Sayo erased a portion of the board and began writing the schedule for the mock exam proper."

    sr5 "As agreed upon, the mock exam tomorrow is mandatory and we expect all 202 Seniors to participate -- minus two from the original 204, of course.{w} Assembly time tomorrow is 6:30 AM {i}sharp{/i}. This is to simulate the first entrance exam on August 3-4."
    sr5 "Male and female students, alphabetically arranged, will be divided proportionately by gender among the Fourth Year classrooms."
    sr5 "The test proper will run for four hours, time-controlled by the proctors.{w} There will be no breaks inbetween, so bring your own snacks if you wish."
    sr5 "All Fourth Year advisers will act as observers, in addition to the proctors. This is with the exception of Ms. Harada, who is expected to return next week."
    sr5 "Tanaka, were the PCFs already distributed?"
    c_sec "And collected.{w=0.5} All set for tomorrow, Sayo."
    sr5 "Good. Please post the minutes at the council group chat.{w} Watanabe, you know what to do. Just ensure everyone knows the details of tomorrow's event."
    sr5 "As for everyone, I would like to thank you once again for your time and contribution in the review sessions.{w} While we may not yet rest easy, I certainly hope we will by noon tomorrow."
    sr5 "And Hiroshi, give us until the post-evaluation to consider your suggestion."
    sr5 "Keep safe on your way home, everyone. Meeting adjourned."
    return

label ch02_11_mockreview:
    scene black with fade
    centered "{b}Mock Examinations{/b}"

    scene black with fade
    "JULY 13, 2013 - 0700H"

    window show
    nvl clear
    narr "We arranged ourselves according to surname.{w} I was assigned to Test Room 5, Classroom IV-E on a normal day."
    narr "And it looks like I'll be in the same room as my former classmate, Hikaru. She can't stop herself from giving hand signals to Aria, doesn't she? It's like they'll never see each other again."

    nvl clear
    narr "The proctor was already waiting inside, a thick pile of test booklets and answer sheets on his desk."
    narr "He directed each one of us to a particular seat according to the arrangement he was referencing.{w} I was at the second-to-last column, back row."
    narr "Afterwards, he distributed the testing materials face down to the first row, instructing them not to open the booklets until he says so."

    nvl clear
    window hide

    proctor "I hope you've brought your No. 2s and other writing materials as instructed.{w} Please fill out the form on the first page. I have written some of the information you need on the blackboard."

    window show
    nvl clear
    narr "He directed our attention to the School ID and Division Number written in big letters."
    narr "As for the rest of the details, we shaded the circles according to the information required on each item.{w} It took us a good fifteen minutes for everything -- just five on our name alone."

    nvl clear
    narr "And if I may be excused, there is just some things that always fascinate me whenever I get a hold of these glossy papers.{w} It's the fact that both our personal information and answers are fed into a machine for automated checking."
    narr "That machine checks for the position of the marks through those black dashes on the right. After validation, it is used for database input."
    narr "Which parts are which? The front page contains, as everyone already knows, our personal information. The back page contains the answer sheet with which we have to shade even more circles."
    narr "...Some basic stuff that people may never need to know."

    nvl clear
    narr "Sayo made one last round trip sometime after I finished answering the front page. She headed into Test Room 4."
    narr "After another ten minutes, the teachers gave the proctors a signal. At that moment, they synchronized their timer to begin at 8 AM sharp."
    narr "The time limit is until noon, and nobody is allowed to leave the campus until then."
    narr "When the bell rang at eight, everyone opened their test booklets.{w} The proctor sat chin on fingers behind the desk, watching us as we answered the first part -- Language."

    nvl clear
    narr "There was just one other person that caught my eye.{w} In one of the few times I glanced out the window, I saw Ms. Harada patrolling with the other teachers."
    narr "I thought it strange at the time since I didn't even notice her earlier in the assembly. We were told she would be back by Monday.{w} I guess it probably means she got over things quicker than we thought."
    narr "After all, it must be more emotionally taxing when you're alone. That's what I think, at least."

    nvl clear
    window hide

    proctor "The first hour has ended. Please proceed to the next part -- Mathematics."
    proctor "Take note that you will {i}not{/i} be allowed to return to the previous section as you were given enough time to answer.{w} However, you are allowed to finish shading the circles of your answers."
    proctor "Proceed."

    "This is going to be a breeze, especially since I taught more than half of the items -- conceptually -- here.{w} So for the final hour, we have Science and Reading Comprehension."
    "There's the trouble alright. I love how they ordered this according to difficulty.{w} It didn't take long before we were already in Science."

    "{b}*BUZZ*{/b}"

    "That was the sound system. It was supposed to have been fixed yesterday.{w} Or rather, it had engaged far too early. I thought they would start announcing the remaining time at eleven? Only two hours have barely passed!"

    unk "AAAAAAAAAAAAAAAAAAAAAAHHHHHHH!!! {b}{i}*BREATHE*{/i}{/b} HAAAAAAAAAAAAAAHHH!!!"

    "{cps=8}What the?! Is that...?{/cps}"

    u_kk9 "{b}*WHEEZE*{/b}{w=0.5} AAAAAAAAAAHHH!!! It burns!{w=0.5} Haa... Haa... It burns! Gah...! Ino... ue...{w=0.5} HELP ME! SOMEBODY!!!"

    "{b}{i}*STATIC*{/i} *BUZZ*{/b}"
    "Pencils started dropping on the floor, either by intense shock or by the pain caused by that stupid buzz! OW!{w} Whoever set that up is sick...{w=0.5} beyond sick! Heck, the whimpering from the girls in the room are penetrating these walls.{w} I can even hear those from the other room."
    "{b}{i}*STATIC*{/i}{/b}"

    unk "{cps=10}Good day, my friends.{/cps}"

    "And a voice spoke, somewhat robotic or otherworldly, none of whom we recognized at all.{w} Somewhere beneath that gentlemanly tone there hides...{w=0.5} how would Sayo put it?"

    unk "First of all, I would like to humbly apologize for the commotion I may have caused. It seems that I have come at an inappropriate time.{w} Again, I extend my apologies."

    "The proctor ran outside, shouting at somebody off-view."

    proctor "Can somebody shut that thing off? It's unnerving everybody!"
    iy1 "No, sir! We have to let them keep going."
    proctor "Keep going? An official assessment is underway, Mr. Yokohama!"
    iy1 "Evidence, sir. Please, we must let them talk. Besides, it's about time they revealed themselves to us."
    hy10 "Please, sir! It might be the only chance we'll get from the culprit. It's for our friend, see?"
    proctor "{cps=8}The... culprit...?{/cps}{w} Fine. But I'll be calling the police once this guy is done."
    iy1 "Thank you."
    hy10 "But what about Ms. Harada?"

    "I placed a finger over my mouth."

    unk "I admit it.{w=0.5} I am the one to blame for all that has happened the previous month.{w=1.0}{nw}"
    unk "You have just listened to the final moments of Kyou Kirisaki{w=0.5} as I am certain he still lingeres within your memories.{w=0.5} How does one start to forget, I wonder?{w=1.0}{nw}"
    unk "A valiant attempt to save his life{w=0.25}, but the moment the flame was permitted to let loose{w=0.5} fate had chosen to be kind not to this poor soul.{w=1.0}{nw}"
    unk "A waste,{w=0.25} but nevertheless one less nuisance on my end.{w=0.5} And as for you, one more to create a zero sum game.{w=1.0}{nw}"
    unk "So now, I question myself,{w=0.25} who is next? Answer this for me.{w=1.0}{nw}"

    window show
    nvl clear
    centered "{cps=10}{i}Who wishes to go next, I wonder?{/i}{/cps}"

    nvl clear
    window hide

    "{b}*SLAM*{/b}"
    "That bastard!"

    student "Ichirou!"
    iy1 "Who the hell do you think you are?! Some kind of God?{w} You can't just take our lives for this sadistic game of yours!"
    proctor "Mr. Yokohama, please settle down."

    "I turned a deaf ear on him and burst out of the classroom.{w} He didn't follow me, only shaking his head in disappointment and disbelief."

    unk "It is rather fascinating --{w=0.25} that ecstacy one feels when his conjectures are correct.{w=0.5} You expose those who live with a mask{w=0.25} and tear them down along with the others of their own kind.{w=1.0}{nw}"
    unk "And as made clear by these recent events, there are merely two possibilities --{w=0.5} {cps=10}a shattered persona,{w=0.25} or the end of life.{/cps}{w=1.0}{nw}"
    unk "If you were given the choice,{w=0.25} would you rather live on in this world full of sorrow and anguish{w=0.25} living the lies you yourself have created,{w=0.5} or would you choose mercy and carry on to the next life{w=0.25} where all your imagined Utopias would come to fruition?{w=1.0}{nw}"
    unk "The world is naught but an illusion,{w=0.25} and all its inhabitants live with an illusion they cannot rid of themselves of.{w=0.5} So what is the point in struggling against the chains in order to see the light?{w=1.0}{nw}"
    unk "And I offer salvation --{w=0.25} I have finally come.{w=0.5} Those who are the chosen few, I congratulate you in advance.{w=1.0}{nw}"
    unk "But when the time comes,{w=0.25} will you be ready?{w=0.5} Let it be known that the sands on the upper glass run thin,{w=0.25} for the {i}Second Indian{/i} will soon come to pass.{w=1.0}{nw}"

    "Hang on... Second Indian?{w} That's something I would never expect an Anti-Christ to be talking about.{nw}"
    "{b}*BUZZ*{/b}"
    "Argh! What the hell?"

    window show
    nvl clear
    narr "{cps=10}One little,{w=0.25} Two little,{w=0.25} Three little Indians~ puku!{w=0.5}{/cps}\n{cps=15}Swing, swing, swing...{w=0.25} Who will be chosen by this roulette?{w=0.5}{/cps}\n\n{cps=10}Four little,{w=0.25} Five little,{w=0.25} Six little Indians~ puku!{w=0.5}{/cps}\n{cps=15}Swing, swing, swing...{w=0.25} In this quandary of life and death?{w=0.5}{/cps}\n\n{cps=10}Seven little,{w=0.25} Eight little,{w=0.25} Nine little Indians~ puku!{w=0.5}{/cps}\n{cps=15}Swing, swing, swing...{w=0.25} Ready?!{w=0.5}{/cps}\n\n{cps=15} You bet, puku!!!{w=0.5}\n{b}TEN LITTLE INDIAN BOYS!!!{/b}{/cps}"

    nvl clear
    narr "{i}Kyekyekyekyekyekyehahahahahahaha... Ihihihihihihihihihihi...{/i}"

    nvl clear
    window hide

    "I get it now...{w} That rhyme from my childhood, now used as a framework for this \"savior's\" method of {i}salvation{/i}.{w} Sayo and Inoue have told me about this, read it from somewhere."

    sr5 "On that island, ten people died according to the rhyme -- a timeless story, I must say.{w} From there, this very same rhyme became one of those used to foretell an omen of death."
    iy1 "Sayo! How long have you been standing there?{w=0.5} And how did you know what I was --"
    sr5 "Have you learned nothing, Ichirou?{w=0.5} But that isn't the issue at hand."
    sr5 "{cps=15}It's finally coming to me. Only now have I realized the true meaning of it...{/cps}"
    iy1 "What do you mean?"
    sr5 "Surely, Kyou is the First Indian if we consider this little rhyme of his.{w} They are challenging us, Ichirou. Their gambit relies on them picking us off one by one whilst remaining undercover.{w} {i}*sigh*{/i} Talk about the highest form of hypocrisy."
    iy1 "I suppose you're right, but don't you think...?"
    sr5 "Yes. Listen to how this all makes little sense."
    sr5 "{i}Two little Indians sitting in the sun;{w=0.5}\nOne got frizzled up and then there was One.{/i}"
    sr5 "By now, there would already have been eight victims before Kyou.{w=0.5} And that makes this Second Indian of theirs more confusing. It should be their last.{w} {cps=4}Unless...{/cps}"

    "{b}*BUZZ*{/b}"

    iy1 "Inoue! They're going after her!"
    sr5 "Hold it!{w} We can't say for sure they're going after a vulnerable girl, let alone one who just survived the horrors they inflicted.{w} I sense them as principled, whoever they are. Meticulous, if you prefer that word."
    iy1 "Well, I'm not just gonna stand around here and let them make their move. Right after this, damn everything, I'm going to the hospital to warn Inoue!"
    sr5 "You do realize your impulsive behavior will do more harm than good to her?{w} Stay put. I'll make sure Emmerich will hear everything that transpired just now."
    iy1 "And what if he doesn't? Tell me how, Sayo."
    sr5 "Shhh!"
    unk "And do not think I will be done just yet.{w=1.0}{nw}"
    unk "Yawn at the words I speak and leave this all behind you.{w=0.5} But there are those before you who were foolhardy enough to do so,{w=0.25} enough for them to have a {i}rather pleasurable experience{/i}.{w=0.5} You wouldn't want a repeat performance of that, would you?{w=0.5} Don't be as naive as that girl...{w=1.0}{nw}"
    unk "If I were able to capture two birds in the most unimaginable circumstances possible,{w=0.5} {cps=10}then I can do it again...{/cps}{w=0.25} {cps=8}and again...{w=0.25} and again...{w=0.25} Hehehehehe...{/cps}{w=1.0}{nw}"
    unk "You keep your wits about you,{w=0.25} and keep an eye on your peers as best as you can.{w=0.5} I have waited long for our intellects to clash --{w=0.25} a cat and mouse on equal footing.{w=1.0}{nw}"
    unk "{cps=12}I expect great things from you...{/cps}{w=1.0}{nw}"

    window show
    nvl clear
    centered "{cps=12}{i}...Student Council President{w=0.25} {b}Sayo Ronoroa.{/b}{/i}{/cps}"

    nvl clear
    window hide

    "{b}*BUZZ* {i}*STATIC*{/i}{/b}"
    "Sayo...?{w=0.5} But why? What does she have to do with that maniac?! I don't understand."

    iy1 "What did they mean, Sayo? What's up with that last bit?"
    sr5 "{cps=1}...{/cps}"
    iy1 "{cps=5}Sayo-chan?{/cps}"
    sr5 "Back to your rooms, everyone! Nobody leaves until the authorities arrive.{w} All proctors, please suspend the mock examinations. We have an emergency."

    window show
    nvl clear
    narr "She finally lost her composure, the first I've seen since First Year.{w} And why wouldn't she? Sayo's been {i}threatened{/i} -- I wouldn't call that a {i}challenge{/i}."
    narr "At this point, the path beyond is obscured by a smoke screen.{w=0} Whether the smoke is gray or red, I couldn't tell...{w=0.5} nobody couldn't.{w} It's death or insanity for us."
    narr "{cps=10}For now,{w=0.25} they win.{/cps}"

    nvl clear
    window hide

    return

label ch02_12_posteval:
    scene black with fade
    return

label ch02_13_death02:
    scene black with fade
    return

label ch02_14_investigation:
    scene black with fade
    return

label ch02_15_facts4:
    scene black with fade
    return

label ch02_16_suspicions:
    scene black with fade
    return

label ch02_17_epilogue:
    scene black with fade
    return