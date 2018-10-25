# AUGUST CHAPTER SCRIPT

init python:
    def parse_bin(x,b):    # For investigation switches
        if (x%(2**(b+1))) >= 2**b:  # Check if binary digit is 1; choices start from 0.
            return True
        else:
            return False

    path_b1 = 0 # Determines path in August Chapter.
    bonus_b1_i = 0 # Determines bonus dialogue (Innocent Questions) in August Chapter.
    bonus_b1_g = 0 # Determines bonus dialogue (Guilty Questions) in August Chapter.

    current_area = 0 # Determines current location.
    areas = 0 # Determines accessible areas during investigation segments.
    visited = 0 # Determines if area during an investigation is visited at least once.

    i1_office = 0 # Switch for I1 Office: Workstation [0-2]
    i1_conference = 0 # Switch for I1 Conference Room: Sayo Ronoroa [0-1], Akira Ichibana [2-3]

    i2a_circulation = 0 # Switch for I2 Circulation: Information Desk [0-3]
    i2a_genreference = 0 # Switch for I2 General Reference: Bookshelves [0-2], Akira Ichibana [3-4]
    i2a_periodicals = 0 # Switch for I2 Periodicals: Newspapers [0-2], Photographs [3-4], Inoue Shinozaki [5-7]
    i2b_reception = 0 # Switch for I2 Reception Area: Reception Desk [0], Sayo Ronoroa [1-3]
    i2b_office = 0 # Switch for I2 Office: Inspector Emmerich [0-2]
    i2b_archives = 0 # Switch for I2 Archives: Old Case Files [0-2], Walkie-talkie [3], Sumiko Tokubei [4-6], Hikaru Yamamoto [7-8]

label ch03_august:
    centered "{i}{b}When one entity splits into two, in retrospect, time is reversed.{w}\nThe bridges that exist shall exist no more.{w}\nAnd the most devastating, the science of fission;{w} such are the fools whose minds are that of a mongrel, unwitting pawns of a faceless adversary.{/b}{/i}"
    
    call ch03_01_prologue1
    call ch03_02_prologue2
    call ch03_03_extrareview
    call ch03_04_decision1
    call ch03_05_aftermath
    call ch03_06_investigation1
    call ch03_07_investigation2
    call ch03_08_facts5
    call ch03_09_ministryvisit
    call ch03_10_facts6
    call ch03_11_ceasefire
    call ch03_12_death03
    call ch03_13_epilogue
    call credits
    return

label ch03_01_prologue1:
    scene black with fade
    "AUGUST 4, 2013 - 0545H"

    window show
    nvl clear
    narr "In about five minutes, the sun shall grace the horizon once more."
    narr "In about five minutes, the jeepney shall reach the gate of its destination -- the premier university of the country, the National State University."
    narr "In about five minutes, all this three year-long anticipation shall reach its climax."

    nvl clear
    narr "The infamous NSUEE (National State University Entrance Exam) has seen tens of thousands of students annually vying for a slot.{w=1.0} Sadly, never have there been a passing rate exceeding one-fifth. Virtually, even a hundred is impossible."
    narr "Nevertheless, it is left to the student's own mileage whether the privilege, should it be granted, is truly worth it.{w=1.0} What lies ahead is a journey that relies on wits, perseverance, and a good heart, not some stroke of luck."
    narr "Past the low hum of the transport's motor are the sounds of nature.{w=1.0} Crickets perform their crescendo before sunrise. At night, they shall do it again. Leaves rustle as they are kissed by the soothing breeze."

    nvl clear
    window hide

    driver "Engineering!"

    window show
    nvl clear
    narr "I, along with a few others, signaled to stop."
    narr "While my companions immediately headed left towards the College of Engineering, I walked straight ahead.{w} My test center, according to my examination permit, is the College of Law. Two blocks away according to the map."
    narr "The road was nearly empty, devoid of even the usual joggers and bikers on the the inner half the oval. Dubbed the \"Academic Oval\" by NSU denizens, most of the major colleges and institutions are placed around its arc."

    nvl clear
    narr "I arrived at the Law building at around six, nearly the same time as the breaking of dawn.{w} There were already two long queues from the entrance, the right of which I joined."
    narr "The exterior is rather sophisticated.{w} The front pillars and overall architecture resembled that of an actual courthouse --{w=1.0} or at least, the Supreme Court."
    narr "Still, those budding lawyers have quite a home for the next six to seven years. Close to actuality, in fact."

    nvl clear
    narr "At 6:15 AM, the marshals and faculty members inspected our permits and guided us to our testing rooms.{w=1.0} An addendum -- these marbled floors are cleanly polished."
    narr "We were escorted to Courtroom No. 4 -- I mean, Lecture Hall No. 4.{w} It was a relatively small room for twenty students. The benches resemble those from a courtroom.{w=1.0} The professor, complete with raised podium, is the judge."
    narr "The aesthetics of this place is impressive. One has to wonder if court will be in session within a few minutes.{w=1.0} It feels as if the twenty of us are participants of a trial, audience or defendants."
    narr "I hope it stays as that. I would prefer being on the witness stand should the time come. Better yet, never set foot in a courthouse ever!"

    nvl clear
    narr "At 6:30 AM, the proctor arrived.{w=1.0} In hand, she had our test booklets and answer sheets. Hanging from her wrist is a timepiece."
    narr "She walked through the left aisle, distributing the test materials while we brought out our snacks and stationery."

    nvl clear
    window hide

    proctor "Please keep your belongings inside your bags. Turn off your cellphones and gadgets, and keep your test permit and school ID in front.{w=1.0} I will inspect the former to check if you're in the correct room."
    proctor "We will start at exactly seven o' clock. Please provide the necessary details in the front part of your answer sheets."

    window show
    nvl clear
    narr "Like what we did during the review sessions, I filled out the form in fifteen minutes.{w=1.0} The proctor was busy going around the room inspecting our permits."
    narr "She reappeared in front, giving out the next instructions and house rules.{w} The conditions are exactly the same as they were presented during the review sessions. That is to be expected from an event modeled after the actual NSUEE."
    narr "At seven, the proctor received the signal and turned to the calendar-like timekeeper on the whiteboard."

    nvl clear
    window hide

    proctor "The first part is Language. You have 60 items to answer in 60 minutes."
    proctor "You are not permitted to proceed to the next section without my instruction.{w=1.0} Instead, you may review your answers or eat, whichever you prefer."
    proctor "Keep the rules in mind and good luck!"

    "{cps=20}A deep breath...{w=0.5} Pencil in hand...{w=1.0} Turn the first page after the section with {i}Language{/i} at the center.{w=1.0} Read carefully...{/cps}"

    window show
    nvl clear
    narr "As mentioned several times already, the experience warrants no further repetition. The only difference is the heavier pressure."
    narr "After the humiliating finish to Junior Year, I made a promise to myself --{w=1.0} No matter what, I must pass this exam."

    nvl clear
    narr "It is not an easy task. As early as May, I began preparations using the reviewer my uncle gave me.{w=1.0} I answered at least two sections every morning until my brain could take it no longer."
    narr "By afternoon, I checked my own answers. From there, I can pinpoint my strengths and weaknesses.{w} The Math sections -- Algebra, Geometry, and Trigonometry -- are the highest, near-perfect if not for careless mistakes. Science is the weakest, averaging from 50-60 percent."
    narr "If the results are closer to actuality, then I have a good chance of securing a slot. I hope the extra attention devoted to Science would pay off and improve my chances."

    nvl clear
    narr "An hour passed without fanfare."
    narr "It was just as neutral as we, my batchmates and I, made it out to be.{w=1.0} I spent the last five minutes munching on my reward, a cheese sandwich."

    nvl clear
    window hide

    proctor "Okay! You may begin the second section, Mathematics. 60 items to answer in 75 minutes.{w=1.0} Use the scratch papers provided and approach me if you need an extra piece."
    proctor "Take note that you may not return to the previous section. You may only finish shading your answers."
    proctor "Proceed."

    window show
    nvl clear
    narr "I can do Mental Math just fine, but just to be sure, I wrote every question's solution in fine print.{w=1.0} The former, coupled with overconfidence, may be the source of said mistakes."
    narr "What impacted me the most is one of the last Logic questions -- the kind that would initiate a good conversation."

    nvl clear
    narr "It is worded as follows:"
    narr "{i}Diego and Juan are sent to the principal's office due to a scuffle between them. Pedro arrived as a witness. The following are their statements:{/i}"
    narr "{i}Pedro: Diego is not lying.\nDiego: All of us are telling the truth.\nJuan: Any one of us is lying.{/i}"
    narr "{i}Who is telling the truth{/i}"

    nvl clear
    narr "It took a good five minutes before I arrived at answer.{w=1.0} I contemplated upon this question the most while eating the second sandwich. It was, I decided, the best question of the entire test by far."
    narr "As a disclaimer -- to this day, I still have not confirmed what the answer was. Perhaps others have the same or a different idea as mine?"
    narr "When the time ran out, the proctor did not ask us to continue to the next section. Instead..."

    nvl clear
    window hide

    proctor "Okay, since you've been sitting there for two hours straight, please stand up. We will perform some stretching exercises."
    proctor "Stretch your arms forward, palms outward...{w=3.0} Arms upward...{w=3.0} Turn your neck to the left...{w=3.0} To the right...{w=3.0} Circular motion...{w=3.0} Inhale...{w=2.0} Exhale...{w=2.0} Inhale...{w=2.0} Exhale...{w=2.0}"
    proctor "Thank you. Enjoy the rest of the fifteen-minute break.{w=1.0} Those who wish to go to the restroom, you may do so."

    "Everyone chose to relax. A few of us munched away quietly."

    window show
    nvl clear
    narr "The section is Science, timed at 60 minutes for 45 items.{w=1.0} The fourth and last section, Reading Comprehension, would be timed at 45 minutes. Time sinks, these two... at least from my own experiences."
    narr "At the end of the short break, the proctor repeated her instructions from the previous section."
    narr "Stay calm, remember the key points in the review sessions, and things will be alright...{nw}"

    nvl clear
    window hide

    "{i}*BUZZ*{/i}"

    mh8 "{i}*GASP*{/i}"

    window show
    nvl clear
    narr "I am aware it is just a guard outside,{w=1.0} yet radio static still makes me jump."
    narr "Whatever. If the mind is derailed for even one second at this stage, everything will fall apart.{w=1.0} {cps=15}Just focus...{/cps}"

    nvl clear
    narr "I have nothing to say about this part. Nothing is certain here."
    narr "I have not gauged yet my performance from the reviewers we were provided with. Thus, my confidence level is much lower than in the previous sections."
    narr "The clock stopped while I was still shading my last answer."

    nvl clear
    window hide

    proctor "We now move on to the final section, Reading Comprehension. You have 40 items to answer within 45 minutes."
    proctor "Good luck!"

    "My, is that not a beaut?{w=1.0} It is worse than I imagined. Let us see how effective Ayumi and Ikuko's techniques are."
    "The first passage is from Fyodor Dostoevsky's {i}Crime and Punishment{/i}."
    "Ummm..."
    "{i}May the Devil take the fool... May the Devil take the fool...{/i}"
    "Aside from Raskolnikov, I can think of one more person who loves uttering this exact phrase."
    return

label ch03_02_prologue2:
    scene black with fade
    centered "{b}Six Days Ago{/b}"
    "JULY 29, 2013 - 1215H"

    window show
    nvl clear
    narr "Our club adviser, Mrs. Aibara, invited Inoue and I to the Student Council conference room.{w=1.0} We discussed my last responsibilities as acting president before returning the power to Inoue."
    narr "It was brief, and all throughout, Inoue was her jolly self."

    nvl clear
    window hide

    t_aib "By the end of this week, Mi-kun, you can resume your duties and let Inoue-chan handle her job.{w=1.0} I bet she still needs to rest a little longer. {i}*giggle*{/i}"
    mh8 "As a matter of fact, ma'am, she can rest until the following week, no more extensions.{w} We have planned to secure her responsibilities until then."
    is4 "You've done enough, Miyu. Let me shoulder my one-month absence.{w} Besides, it's time the Math Club has seen its original President in action, eh? {i}*snicker*{/i}"
    t_aib "I'll leave you kids to wrap up any loose threads in our discussion as well as any plans you might have. Goodbye, children."

    "She was a gentle lady, mother-like even. Except at the beginning when she asked about Inoue's condition, she smiled for the entire meeting."
    "Back to business."

    is4 "So, what are these things I'm hearing about you, hm?"
    mh8 "What do you mean? Did I do anything wrong?"
    is4 "Hmmmmm... Not quite wrong, per se. But I heard you've been doing {i}very{/i} naughty things while I was gone.{w=1.0} It feels good to be in the throne, right?"
    mh8 "You {i}could{/i} say that, but whatever the heck that means.{w=1.0} Of course, I've been doing --{nw}"
    is4 "Tsk.{w=0.5} I knew it!{w=1.0} Tsk.{w=0.5} Tsk.{w=0.5} Tsk."
    mh8 "Come on...{w=0.5} Let me explain myself!"
    is4 "I can ask Mrs. Aibara to return to my old post now, Mi-kun. I am {i}so{/i} disappointed in you. {i}*snicker* *snicker*{/i}"

    "I don't know whether Inoue is serious or not, but I'm not sure if I should feel guilty or relieved either."

    mh8 "{cps=15}Ku.{w=0.5} Kikikikikiki...{/cps}{w=1.0} Teeheeheeheeheeheeheeheehee..."
    is4 "Why are you laughing?"
    mh8 "Don't you see it? Heeheeheeheeheehee!{w=1.0} I'm happy."
    is4 "Eh?"
    mh8 "Welcome back."

    "Silence."
    "I swept the shoes from her feet and wore them instead.{w} Like a child she was a minute ago, it is now I who was becoming more childish."
    "Slowly, her smile revealed her true nature."

    is4 "{cps=20}Thank you, Mi-kun.{/cps}{w=1.0} I'm glad to be."

    "It was a genuine smile, a great relief to witness after bearing that heavy Cross.{w} She glanced at the office door."

    is4 "I don't remember the office door being closed this early."
    mh8 "That's probably because Sayo didn't come in today."
    is4 "It's Monday. Doesn't she have paperworks to do?"

    "She looked around the room.{w} Her eyes stopped at the stack of papers on the drawer near the whiteboard."

    is4 "Are those our official documents? Shouldn't they be inside the office drawer?"
    mh8 "For quick reference. I must have forgotten to put them away.{w=1.0} The month has been hectic, you know?"
    is4 "I understand.{w} In that case, let me put these away and --"
    mh8 "I'll do it."

    "I zipped past her, scooped the documents, and disappeared into the office. These were all done in under a minute.{w=1.0} She watched inquisitively."

    is4 "You work faster than usual --{w=0.5} {cps=20}too fast, if I may note.{/cps}{w=1.0} What's the deal?"
    mh8 "Ahehehehehehehe...{w=0.5} {cps=15}You see, I'm inspired.{/cps}"
    is4 "Ah! I forgot!{w=1.0} Belated happy birthday!"
    mh8 "Thank you! {i}*chuckle*{/i}"
    mh8 "{cps=20}If we have nothing further to discuss, then I should take my leave.{/cps}"
    is4 "Go ahead. I'll stay here for a little longer."
    mh8 "Okay. Remember to turn the lights off and close the door when you leave. You wouldn't want Mrs. Genkai to be mad at us."
    is4 "I {i}know{/i}. Run along and enjoy the rest of the day, Mi-kun!"

    "I wore my backpack and left the room."
    "Instead of leaving the campus and travelling to Sanae's house, I stayed and sat on the front desk bench.{w} My head feels light, heart racing, my mind in anticipation of the worst outcome."
    "{cps=25}Inoue is going to find out.{/cps}{w=1.0} {cps=20}She is not supposed to...{w=0.5} She is not supposed to...{/cps}{w=1.0}{nw}"

    ikuko "You alright, Miyu?"

    "That's right!{w=0.5} Ikuko knows what happened in that room."

    mh8 "Ikuko, she's still inside. I don't know far her curiosity will take her, but please, you must stall her."
    ikuko "Did you slip up?!"
    mh8 "Yes...{w=0.5} No.{w=0.5} I lied to buy some time. She might have picked up, but I'm not sure. She'll understand you more than me.{w=1.0} {i}*sigh*{/i} If she sees what's inside that office..."
    ikuko "Alright. I'll go there now. Just stay calm.{w=0.5} If anything happens, get in touch with Sayo."
    mh8 "{cps=15}Look normal.{/cps}"

    "She paid no more attention as she dashed to the Council Room."
    "My mind was conflicted.{w=1.0} Should I go ahead and visit Sanae, or do I stay and watch what happens next?"
    "That reminds me!{w} I forgot to visit Ms. Natsumoto earlier. The guidance counselor's room is adjacent to the Council room. Should anything untoward happen, I will be able to hear it."

    "{i}*knock* *knock* *knock*{/i}"

    t_nat "Come in!"

    "I greeted Ms. Natsumoto with a smile, although it cracked almost instantly.{w} She sensed my body shaking and urged me to have a seat."

    t_nat "Is there anything you need, son?"

    "I nodded, allowing my body to sink into a chair in front of her desk. I closed my eyes and stopped the clattering."

    mh8 "{i}*EXHALE*{/i}{w=1.5} I think I messed up."
    t_nat "Please elaborate."
    mh8 "It's Inoue.{w=0.5} She's still not stable even after undergoing intense therapy for a few weeks, right?"
    t_nat "I wouldn't call her {i}unstable{/i} but the trauma is still fresh in her mind.{w=1.0} If she comes across anything that would trigger those unpleasant memories, she would suffer a nervous breakdown."
    t_nat "You met her today?"
    mh8 "Earlier. We were having a club-related discussion in the Council room.{w=0.5} And she's still there as we speak."

    "I have said nothing more, yet her eyes turned wary. She caught on to the implications and wore an authoritative expression."

    t_nat "{cps=20}Mi-kun...{w=0.5} Did you tip her off about the {i}restricted area{/i}?{/cps}"
    mh8 "I didn't mean to. I haven't said anything.{w=1.0} Inoue's a bright girl; she'll catch on eventually.{w} The thought unsettles me. There's no telling what happens in the next few moments."

    "Ms. Natsumoto tapped my hand and pointed at the window.{w=0.5} Ikuko was standing there, a quick gesture to her neck before scurrying away."
    "Whatever it meant, it was foreboding to {i}the inevitable moment{/i}."
    "Damn."

    mh8 "{cps=15}Well, ma'am...{/cps}{w=2.0} Boom!{w=1.0}{nw}"
    is4 "AAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHH!!!"

    "That was the prompt! I excused myself and rushed to the Council room."
    "The door to the offices was open.{w} Inoue,{w=0.5} cowering on the floor in front of the file cabinet, wrapped her hands around her neck,{w=0.5} choking,{w=0.5} averting her eyes from the scene."

    r_is4 "{i}*SOB*{/i}{w=0.5} {cps=15}This can't be...{w=0.5} Even here...?{/cps}{w=0.5} {i}*SOB*{/i}"
    f_mh8 "{cps=10}Inoue...{/cps}{w=0.5}{nw}"
    r_is4 "Don't touch me!"

    "{b}*THUD*{/b}"

    c_mh8 "Calm down. It's me!"
    r_is4 "{cps=10}Haa...{w=0.5} Haa...{w=0.5} Haa...{w=0.5} Haa...{/cps}"
    r_is4 "{cps=25}Mi-kun...{w=1.0} What the hell is this?!{w=0.5} Why is there a corpse in one of the workstations?{/cps}"
    c_mh8 "Inoue..."
    r_is4 "You didn't tell me! You were hiding this from me,{w=0.5} you and Ikuko!{w=1.0} He followed us here, huh?{w=0.5} When?{w=1.0} When?!"
    c_mh8 "{b}GULK!{/b}"
    r_is4 "Answer me!"
    c_mh8 "{cps=15}I can't breathe. Let go...{/cps}"

    "I forced myself out of her grip.{w=1.0} Inoue, while still outraged from her discovery, sat on the wall and composed herself."

    f_mh8 "{b}*COUGH*{w=0.5} *COUGH*{w=0.5}{/b} That's right. L.C. terrorized us here while you were away. Some of us even thought they were going after you next."
    c_is4 "If not me, then who? Who did he take?"
    f_mh8 "..."
    c_is4 "{cps=20}Don't tell me it's...{/cps}{w=2.0}{nw}"
    f_mh8 "Yes, Inoue.{w=1.0} {cps=20}Hiroshi is dead.{/cps}"
    c_is4 "{cps=10}But...{/cps}{w=0.5}{nw}"

    "{b}*THUD*{/b}"

    c_is4 "It's all my fault. I should have stopped my brother from handing it to him."
    d_is4 "That's it. It must be the reason why he went after Hiroshi.{w=1.0} I'm useless. I'm a fool...{w=1.0} No. {i}He{/i} is the fool. The Devil chose him."
    r_is4 "{cps=15}May the Devil take the fool.{/cps}{w=1.0} Heh...{w=0.5} Hehehehehehehehehehe..."

    window show
    nvl clear
    narr "I could not bear seeing her like that any longer."
    narr "Ms. Natsumoto checked on us after hearing the noises from her office.{w} I left Inoue in her care after explaining the situation. She understood."
    narr "Don't do anything rash, Inoue. Don't make the same mistake he did."

    nvl clear
    window hide

    proctor "Five minutes left."

    window show
    nvl clear
    narr "And I was on the last passage with five questions remaining."
    narr "The intensity at which your heart races, the vigor of blood pumping up to your head, the excitement that causes the eyes to move up and down...{w=0.5} The enemy is always time."
    narr "It is a double-edged sword, jogging the memory to remember better or worse. With high stakes on the line, it is everything or nothing."

    nvl clear
    window hide

    proctor "Time's up!"
    proctor "Please finish shading your answers. After one minute, I will collect your test materials so you may leave."

    "We complied and closed our booklets after a minute passed."
    "The proctor went over to our seats and collected the materials. She also scanned our IDs."

    proctor "Say, hi, to the teachers for me. I'm also from MSCI."
    mh8 "Eh? Oh, okay."

    "Wow! I never expected an alumna would be my proctor.{w=1.0} At the latest, she would be from Batch '04, if her youthful appearance is anything to go by."
    "Nevertheless, she went on with her duty.{w=1.0} We waited for her to finish collecting papers before leaving."
    "The clock read 11:45; the sky was white.{w=0.5} A relief."

    window show
    nvl clear
    narr "I walked back to the College of Engineering jeepney stop and pondered upon a few things."
    narr "First, we cannot hide Hiroshi's demise any longer -- two weeks have passed since that dreadful eveing.{w} Tomorrow, we meet with Inoue and get her side of the story. She has already agreed and we would share the details of the heinous crime in exchange."
    narr "Second, why Sayo?{w} It takes one meticulous pair of eyes to disprove {i}that{/i} notion. Why would she disguise herself as a near-omnipotent criminal mastermind only to indict herself early on? It does not add up."
    narr "The next step is rather obvious, is it not?"

    nvl clear
    window hide
    return

label ch03_03_extrareview:
    scene black with fade
    centered "{b}Three Days Ago{/b}"
    "AUGUST 1, 2013 - 0930H"

    window show
    nvl clear
    narr "IV-D. Third session for the day but I'm already exhausted."
    narr "He is no longer with us -- the one who requested for these. What is the point?{w} Nevertheless, we have to keep rolling. The entrance exams are scheduled this weekend."
    narr "Pity...{w=1.0} I don't need pity. The mere mention of it disgusts me."

    nvl clear
    window hide

    odome "Ichi, let's begin the session. We don't want to keep Mrs. Kaida waiting."

    window show
    nvl clear
    narr "Right. It's time for molecular biology and genetics, two of my favorite topics centered on application."
    narr "Hisashi Odome is the class president of IV-D and a Science Club officer. In the future, he will replace me -- it is my duty to prepare him."
    narr "I don't plan on replacing Hiroshi despite the many clamors that I should.{w} Sumiko, the workaholic leader, is a better fit."
    narr "EO? I'll drop that, too.{w} Things have gone too far to continue."

    nvl clear
    window hide

    # INCOMPLETE

    return

label ch03_04_decision1:
    $ path_b1 = 0
    $ bonus_b1_i = 0
    $ bonus_b1_g = 0

    scene black with fade
    "AUGUST 5, 2013 - 1145H"

    window show
    nvl clear
    narr "With over half an hour remaining, some students have finished eating their meal."
    narr "Among them is Miyu, now pacing back to IV-C. Oftentimes, he would glance at his watch, and mumble to himself, \"Is she done yet?\""
    narr "Beyond the window, he spotted Inoue sitting underneath a large tree.{w=1.0} She was accompanied by Hikaru and Yoshiro, the three having a conversation."
    narr "Just as he stepped out of the door, a hand tapped him from behind."

    nvl clear
    window hide

    st3 "Let's go.{w=1.0} I don't want to miss what she has to say either."
    mh8 "Alright.{w} But I wonder if Sayo is on her way?"
    st3 "She'll come from either IV-E or the Student Council office. Paperworks or personal routine, I'd wager."
    mh8 "Which makes me wish she takes long.{w} We need to get as much information as we can before the situation turns dire. Inoue's bound to explode once she sees her."
    st3 "I agree."

    "The two boys approached the tree.{w} Hikaru waved at them, catching Inoue and Yoshiro's attention.{w} Akira, coming from the canteen's direction, trailed closed behind. He disposed his mango shake on the way."

    hy10 "Aren't we IV-C folks so diligent? Five plus Inoue."
    ys6 "It's IV-C!{w=1.0} Carry over our catchphrase from Junior Year while our reputation is clean."
    "\"Hahahahahahahahahaha...\""
    ai2 "So, what did we miss?"
    hy10 "Nothing official yet. Just the usual friendly banter. Mama said it was the best course of action."
    is4 "I haven't seen you all, save for Miyu, in a while.{w=1.0} Oh! How could I forget? I was present for the exams as well."
    mh8 "Don't bother. {i}*chuckle*{/i}{w=1.0} I trust you've been better since our previous conversation?"
    is4 "Definitely! I'm fit enough to resume my normal activities. Wouldn't want to step over the agreement and extend my vacation, yes? {i}*snicker*{/i}"
    is4 "And I'm sorry for the commotion last week."
    mh8 "Don't beat yourself up. {i}I{/i} should be the one apologizing. Should've known better than to lie."

    "Silence.{w} The four others stared at Miyu, their thoughts a common question."

    hy10 "You mean...?"
    mh8 "Yes..."

    "At this moment, Ichirou joined them.{w} Miyu greeted him coldly, then scouted for eavesdroppers."

    mh8 "She discovered the crime scene. Inoue didn't exactly act friendly when I returned to the Council room. I'll let you fill in the details."
    is4 "{b}{i}*groan*{/i}{/b}"
    iy1 "We've crossed the boundary, it seems. Shouldn't we move on to what we {i}all{/i} came for?"
    ys6 "Then let's not waste any more time."

    "Hikaru and Ichirou sat beside Inoue. The four others either sat under the tree or stood with their back on a pole."
    "All eyes on Inoue."

    ys6 "Let's assume you cannot remember the moment you were abducted by L.C. or whoever. Can you at least describe the events surrounding your captivity?"
    is4 "It's a haze. Nothing is concrete that anything I describe might come off as nonsense."
    iy1 "Just give us anything. We'll work out the details later."

    menu:
        "But which first question is more appropriate?"
        "What state were you in when you've woken up?":
            mh8 "What state were you in when you've first woken up?"
            is4 "It felt as if my head was compressed for weeks. I believe time has passed that long.{w=1.0} When I came to, my feet were chained to a bedpost, restricting my movements."
            st3 "A bed? Was it a prison-like type of bed?"
            is4 "A bit more comfortable if the absence of back pain is any indication."
            is4 "I found a sealed envelope under the pillow.{w} Inside was a CD with the chain lock's key. I used the former on the CD player sitting atop the bedside cabinet."
            mh8 "This L.C. is an old soul, aren't they?"

            $ path_b1 += 1
            $ bonus_b1_i += 1

        "Can you describe the place where you've woken up?":
            iy1 "Can you describe the place where you've woken up?"
            is4 "It was like an abandoned prison cell -- no, a dungeon cell is more accurate. The room was mostly empty, save for a bed, a cabinet, and a CD player."
            is4 "The only opening was a metal door a diagonal away from the bed. It was protected by an electronic lock."
            ys6 "What about this electronic lock? Is it the regular keypad or card reader?"
            is4 "Something else. It was a 36-key piano. Odd choice, but it felt more personalized."
            is4 "My feet were chained to one of the bedposts. The only relevant item I found was an envelope containing a CD and the chain lock's key."
            is4 "I still remember the tune that helped me escape.{w=1.0} It was {i}Au Clair De La Lune.{/i}{w=1.0} I'm not sure if L.C. had made the connection, but I also play the piano."

            $ path_b1 -= 1
            $ bonus_b1_g += 1

    is4 "I inserted the CD and let it play while I examined the surroundings. A little after, I lay on the bed, thinking about how I came to be there."
    is4 "It was a voice recording. L.C. is an affable individual, I must admit.{w=1.0} Monstrous, regardless, because of what he had done to me -- and Kirisaki later on."
    ai2 "Frightening, too! When they first talked to us through the intercom during the mock exams, they were acting all gentlemanlt and such. Things got weirder the longer they talked."
    is4 "Yes. He seems to know me well.{w=1.0} After he was done talking, a lullaby looped infinitely. Glad I recognized it else I wouldn't be able to leave the cell."
    is4 "When the door opened, the void greeted me.{w=1.0} Voices spoke from within the darkness."

    menu:
        "The first moments of consciousness are sufficiently explained. Now, it is time to ask about the disembodied voice... or voices."
        "Hold on. \"He?\"":
            st3 "Hang on. There seems to be a disparity in pronouns, Inoue."
            is4 "I don't understand."
            st3 "Whenever L.C. is mentioned, you refer to {i}him{/i} as male. However, we refer to L.C. neutrally, {i}they{/i}."
            ai2 "Is it because I said \"gentlemanly?\" Let me clarify. I'm not sure about the gender, either."
            is4 "It only applies to the CD recording, however. So, even the gender is unclear at that point.{w=1.0} Past that, let's return to the other voices I heard."
            is4 "{cps=30}It's as if he was all over me.{w=1.0} No. She was at someplace I couldn't see.{w=1.0}{/cps} {cps=25}Their whispers and jeers in my head felt like their mouths touched my ears as if...{/cps}{w=3.0}{nw}"
            is4 "{cps=20}...as if they were in a dimension separate from mine.{/cps}"
            hy10 "Did you check your ears for any receiver-like device, though?"
            is4 "Hikaru, I found nothing odd around my body. There was nothing on me except my glasses."

            $ path_b1 += 1
            $ bonus_b1_i += 2

        "Whose voices?":
            ys6 "Whose voices?"
            is4 "They were threatening me.{w=1.0} It's one of those instances you could say it was all in my head. It felt like it {i}really{/i} was the case."
            ys6 "Did it belong to a male or a female?"
            is4 "I'm not sure. Sometimes, it would be the same voice as in the CD recording. Other times, it would warp to a female. It was witch-like, the second one!"
            mh8 "{cps=15}Witch-like...{/cps}{w=1.0} Did we not experience something of the sort when L.C. revealed their voice to us?"
            iy1 "I remember it distinctly. L.C. sounded like a male as Inoue described in her story.{w=1.0} What about those child hellspawns we heard singing that evil rhyme?"
            is4 "Child hellspawns?{w=1.0} You mean..."
            ai2 "Two children -- a male and a female.{w=1.0} One of them had a tic that went {i}swing, swing, swing.{/i} The other always had this word on one end of his sentences: {i}puku!{/i}"
            is4 "{b}*GASP*{/b}{w=2.0}{nw}"
            is4 "The pool!"
            is4 "{i}{cps=15}Oh... you made her cry...{w=0.5} you bad, bad.{w=0.5} You gonna get slapped in the butt-butt.{w=1.0}{/cps} {cps=10}Swing...{w=0.5} Swing...{w=0.5} Swing...{/cps}{/i}{w=2.0}{nw}"
            hy10 "Inoue-chan? Are you alright?{w=2.0}{nw}"
            is4 "{i}You started it, puku!{/i}{w=2.0}{nw}"
            is4 "And it went straight to Hell from there.{w=1.0} I almost died when I was thrown headfirst into that potpourri of viscera."
            is4 "Never mind about it. I skipped too far ahead."

            $ path_b1 -= 1
            $ bonus_b1_g += 2

    ys6 "And then?"
    is4 "At this point, I started questioning my sanity --{w=0.5} my own reality."
    is4 "There were two doors. The one across I figured would take me forward.{w=1.0} Yet, something stopped me."
    is4 "From beyond the door was another voice.{w=1.0} Unlike the disembodied voices earlier, this one had a corporeal origin. It was angry! It talked to me as if I was a malevolent spirit."
    is4 "And minutes later, I heard...{w=2.0}{nw}"
    unk "{i}Hah...{w=1.0} Hah...{w=1.0} Hahahaha...{w=1.0} Gyahahahahahahahahaha...{/i}{w=1.5}{nw}"

    "{b}*SNAP*{/b}"

    unk "{i}AAAAAAAAAAAAAAAAAAAAHHHHHH!!!{/i}"
    is4 "I thought I died!{w=1.0} My waist felt like the door split it cleanly into two.{w=1.0} {cps=20}Until I saw...{w=0.5} I was fine...{w=0.5} Hehehehe... I don't know.{/cps}"
    iy1 "This is concerning. It is likely your mind has been playing tricks on you.{w=1.0} But to ask how and why wouldn't lead to anything at all!"
    is4 "It wasn't the only time either.{w=1.0} I was blown into a decontamination pool sometime later. With how weak my body became, I thought I would drown."
    is4 "Perhaps I was lucky to have survived. Maybe I didn't survive and you're all part of my imagination.{w=1.0} I don't know.{w=1.0}"
    is4 "I saw Kirisaki after that, but he was already a corpse when I came across him. He was in the room where I almost got split into half!"
    mh8 "Alright, alright. Slow down, please. There's too many weird details to scrutinize.{w=1.0} At the very least, can we clear up the situation with Kyou?"
    hy10 "Maybe he's a {i}walking corpse{/i} when you saw him?"
    mh8 "A zombie?! No way! {i}*chuckle*{/i} Too macabre for L.C.'s own caliber. A spirit is more reasonable."
    is4 "I swear upon it. He was flesh and blood when I encountered him. No way I imagined that."

    menu:
        "It is established that Kyou Kirisaki met his demise by immolation, yet the latest testimony casts doubt onto that. How to respond?"
        "You saw Kirisaki dead? How?":
            hy10 "Okay. You said you saw Kirisaki {i}alive{/i} later on. However, you also mentioned that you saw him {i}dead{/i}. I mean...{w=0.5} how?!"
            is4 "I checked his body -- his uniform, face, hands, everything.{w=1.0} Just like me, he had nothing on him. One of his fingers was black, swollen from being pricked by one of the bonsais in the room."
            hy10 "We own a bonsai. No matter how many times we get pricked, it wouldn't be that bad."
            ys6 "And one of his fingers was black. How does a poisoned bonsai achieve something like that? Are you sure he wasn't burned?"
            is4 "No. The room would have smelled of burnt meat."
            is4 "Moments later, I felt something pulling me towards the large painting on one side of the room. I heard the voice again,{w=1.0} and with it, another sharp pain in my temples."
            is4 "Everything went black and the smell resembled that of a rotting corpse.{w=1.0} When I came to, the surroundings changed -- a haunted, enclosed space much darker than before, and the air felt heavier."
            hy10 "Like how it was from... what's the name?"
            mh8 "I got the reference, Hikaru.{w=1.0} What else changed, Inoue?"
            is4 "The painting transformed from a meadow to a cow, and finally, a hulking monster --{w=1.0} the minotaur!"
            mh8 "Okay?"
            is4 "I dashed out of the room, but it gave chase! I don't want to relive the pain I suffered during that time.{w=1.0} I felt degraded to a worm."

            $ path_b1 += 1
            $ bonus_b1_i += 4

        "Maybe the corpse is a dummy?":
            ai2 "Can we all agree Kirisaki's \"corpse\" was just a dummy to scare Inoue?"
            is4 "It was organic! I checked the body myself.{w=1.0} Made it all the more puzzling to see him alive in the chemistry lab."
            ai2 "A chemistry lab? What happened there?"
            is4 "Kirisaki wasn't himself. When I tried to approach him, he ran away as if he saw {i}something{/i}. No amount of pleading stopped him. He was shouting curses!"
            st3 "Is that a fact?"
            ys6 "We are talking about the same Kirisaki, right? Kyou Kirisaki?"
            is4 "Somehow, I felt hurt, never realizing how out of character he was. {i}*sigh*{/i}"
            is4 "Everything went back to normal once he let me in.{w=1.0} We checked up on each other and discussed a way out of that place."
            is4 "However, the air changed just as we were leaving. Nearly an inch from my face is the tip of an axe.{w=1.0} He,{w=0.5} or {i}it{/i} was planning to kill me!"
            ai2 "Are you sure?"
            is4 "I could sense the bloodlust in his eyes.{w=1.0} There is no mistaking it.{w=1.0} He wasn't himself at all. Believe me!"
            ai2 "It couldn't have been him -- hard to believe if it was. Maybe the Kirisaki you encountered after the corpse was an impostor?"
            is4 "Whatever the case, he lunged at me, aiming at my heart. I pushed him to the shelves, causing various chemicals to spill on his face.{w=1.0} He snapped out of it. It was peculiar..."
            st3 "Was there any acid among the spilled chemicals?"
            is4 "Presumably. The most significant one we found, though neither spilled nor acidic, was liquid chlorine encased in a small ampoule."
            st3 "So, you recognize nothing from the spilled chemicals?"
            is4 "I don't have the time to check. If there was, then such a shame but it matters not!"

            $ path_b1 -= 1
            $ bonus_b1_g += 4

    st3 "Unfortunately, this is where the story muddles. Agreed?"
    mh8 "We can salvage a few points from her story and examine those particular details. Otherwise, it is as you said."
    iy1 "I think what you told us is enough. What I'm interested in is this facility's location. Were you able to glimpse on the surroundings when you escaped?"
    ys6 "It should be somewhere close by.{w=1.0} You have to note, though, that no suspicious vehicles passed through the gate early morning of the 17th."
    ys6 "Considering what activity we were busy with around that timeframe, the suspect has used that to their advantage."
    mh8 "Did someone bother to bring a body bag-sized garbage bag? {i}*chuckle*{/i}"
    ys6 "Then tie it up when the victims are inside. It's too suspect, but there is no other way."
    mh8 "...Unless Inoue can shed light on this."
    is4 "I can do no better."
    unk "She doesn't have to.{w=1.0} We have asked the same question repeatedly with no positive end."
    is4 "{b}*GASP*{/b}"

    "The party turned towards the direction of the voice.{w} It belonged to a petite figure, her hands held behind her."

    hy10 "Whoa! Where did you come from?"
    sr5 "It matters not. What matters now is the lone survivor of L.C.'s crimes.{w=1.0} I figured I should hear the outcome of this conversation."
    mh8 "We're near the end."
    sr5 "Make use of the remaining time, please."

    "She sat on the side closest to Miyu's group, away from the auditorium."

    iy1 "Now, do you remember?"
    is4 "Negative."
    iy1 "Let's focus on the living room.{w=1.0} You heard Kirisaki being brutally murdered inside that room. When you left that room, you said you were attacked."
    is4 "By the minotaur."
    iy1 "I'm not interested in myths. What did the attacker look like?"
    mh8 "It may not be important to you, but the creature itself may hold some significance."
    iy1 "In what way?"
    mh8 "The name of the facility.{w=1.0} The \"manifestation\" of that creature hints at it. If we're lucky, we can ask the authorities to run a search of the place."
    iy1 "Good points.{w=1.0} Let's return to the same question. Once more, who killed Kyou Kirisaki? Was it the same thing that attacked you?"

    "Inoue glanced to her right. Sayo gazed over her shoulder blank-faced."

    iy1 "Hmph."
    st3 "What does that mean, Ichirou? Don't say you haven't changed your mind even after this?"
    iy1 "No. She's trying to cover it up."
    is4 "..."
    ai2 "Stop being a hardball, Ichi. I understand where you're coming from but you stepped over the line."
    iy1 "There is that one possibility. If it can't be proven, then we just press on. No big deal."
    ys6 "Let me reiterate.{w=1.0} Besides the motive, you must have the capacity to commit such horrible acts. And there are a few people here who make the shortlist."
    iy1 "I agree."
    mh8 "Unfortunately for you, I don't."
    iy1 "Prove it otherwise, then!"

    window show
    nvl clear
    narr "Soon, the peaceful conversation escalated to chaos."
    narr "Arguments were thrown and dismantled.{w} Person X must be the killer, Inoue is misremembering, Ichirou's premise is twisted, Miyu and the others are blinded...{w} It is all the same childish bickering."
    narr "All of this unfolded before her eyes.{w} Was she amused?{w=1.0} No one knows.{w=1.0} Entertained?{w=1.0} Perhaps."

    nvl clear
    window hide

    is4 "SHUT UP!!!"
    ".................."
    is4 "Everyone, please listen to me.{w=1.0} Enough of all the speculations and accusations. I will talk."
    is4 "{cps=25}I witnessed it --{w=0.5} the moment of Kirisaki's death.{/cps}"

    "{b}*GASP*{/b}"

    iy1 "Tell us!"
    is4 "{cps=25}The image...{w=1.0} It's still forged deep within my memory.{/cps}{w=1.5} I thought I might have fractured my mind while I was there.{w=3.0}{nw}"
    is4 "With Hiroshi's death, only then I ascertained the truth.{w=1.0} It is a monster with both heads on illusion and reality.{w=3.0}{nw}"
    is4 "{cps=20}It was a nightmare...{/cps}{w=1.0} His screams pleaded that he be salvaged from Hell.{w=3.0}{nw}"
    is4 "{cps=20}And I couldn't do anything...{/cps}{w=2.0} {i}*sniffle*{w=1.0} *SOB*{/i}"

    window show
    nvl clear
    narr "{cps=20}Every sentence...{/cps}{w=1.0} {cps=15}Every word...{/cps}{w=1.0} {cps=20}Inoue slowly,{/cps}{w=0.5} {cps=15}slowly,{/cps}{w=0.5} {cps=10}slowly{/cps}{w=0.5} trailed off into the insanity she acquainted with during her detention."
    narr "Kyou's final moments flashed violently in her mind."
    narr "She fought back her tears.{w=1.0} She needed to be calm.{w=1.0} {cps=25}If not, she would be forever chained in anguish.{/cps}{w=2.0}{nw}"

    nvl clear
    window hide

    is4 "It was me. I killed him.{fast}{w=3.0}{nw}"
    "\"WHAT?! No...!\""
    sr5 "Inoue, are you certain about your claim? Are you not incriminating yourself for Kirisaki's murder?"
    is4 "Don't lecture me. I know what I'm saying.{w=1.0} Besides, among the people here, it is you whom I trust the least."
    sr5 "I figured.{w=1.0} Anyway, for everyone's sake, you must speak the truth and {i}only{/i} the truth."
    is4 "That is the truth!{w=1.0} You --{nw}"
    sr5 "Never mind me! Carry on with your testimony!"
    is4 "..."
    is4 "{b}*EXHALE*{/b} If that's your choice..."
    is4 "Did I say I killed him a while ago?{w=1.0} I mis-phrased that;{w=0.5} rather, I {i}caused{/i} his death."
    is4 "After our fight in the conjuncting chemistry lab, a shelf full of chemicals crashed onto him. He was bathed and soon fell into a stupor."
    is4 "I panicked. The next room happened to be an infirmary, so I dragged him there and propped him up the only bed.{w=1.0} I looked for a bucket to collect water. There was none."
    is4 "Instead, I found a hose which I connected to the nearest faucet."
    is4 "I opened the taps and...{w=1.5} flames rushed out of the faucet and caused an explosion. It almost burned down the entire room!{w=1.0} I was knocked back to the wall while Kirisaki was seared."
    is4 "By the time I extinguished the flames, it was already too late.{w=2.0} He was no longer screaming. Kirisaki was burned to a crisp, his face beyond recognition."
    "....................."
    is4 "{cps=15}I got him killed...{w=0.5} {i}*sniff*{/i}{/cps}{w=1.0} There.{w=0.5} You can end all your petty arguments now."
    is4 "{cps=25}Huh... {i}*sob*{/i}{w=1.0} Uhuhuhuhuhu...{i}*SOB*{/i}{/cps}"
    hy10 "{cps=25}It's alright.{w=1.0} You didn't kill him.{/cps}"
    is4 "{cps=25}It changes nothing, Hikaru. {i}*sniffle*{/i}{w=1.0} He still died while I did nothing...{/cps}"
    hy10 "{cps=25}Wipe your tears. We will seek for justice.{/cps}"
    is4 "{cps=20}Yes...{w=0.5} I'm sure we will. {i}*sniffle*{/i}{/cps}"
    ys6 "People may or may not believe what you said.{w=1.0} Let me share my thoughts --{w=0.5} if they're worth considering."
    is4 "Go on."
    ys6 "As Hikaru said, you're innocent. I concur. You were both instruments and ended up playing as the real culprit orchestrated the crimes to be."
    ys6 "At what extent your mind was warped, we cannot tell. But it dealt a considerable blow to your memory.{w=1.0} You may be aware of some of your actions, but bear in mind the questions you must answer to prove your innocence."
    hy10 "I understand your agreement, but why doubt her still? She told us her story and swallowed her fear in order to do so."
    ys6 "It's far more complicated than merely swallowing, Hikaru.{w=1.0} The only way we can relieve ourselves of doubt is to answer the most important question...{w=4.0}{nw}"
    sr5 "Who is behind all of this?"
    "{cps=10}{b}*grumble* *groan* *hiss*{/b}{/cps}"
    st3 "Inoue, cool down...{w=1.0}{nw}"
    is4 "It was you!{fast}{w=1.0} {b}Sayo Ronoroa!{/b}{fast}{w=1.5}{nw}"
    "{i}*WHOOSH*{/i}{w=1.0} {b}*THUD* *crack*{/b}"

    "Hikaru managed to restrain her but no longer than five seconds. Inoue charged at Sayo and grabbed her collar."

    sr5 "It wasn't me!{w=1.0} Ack!{w=0.5} Let me go!"
    is4 "It's what all of you criminals say, isn't it? Damn the evidence!{w=1.0} Why bother looking for something that no longer exists? You disposed it to cover up your tracks.{w=1.0} Scoundrel!"

    "Akira and Yoshiro clinched an arm each. Inoue's grip on Sayo remained tight."

    sr5 "You don't know what you're talking about. {i}*choke*{/i}{w=1.0} Please! Let me go!"
    
    "{i}*murmur* *murmur* *murmur*{/i}"

    t_nat "What is going on here?!{w=1.0} Ms. Shinozaki!"

    "At last, they were separated. Akira and Yoshiro freed Inoue's arms and stepped away."

    hy10 "Sayo-chan!"
    sr5 "I'm fine... {b}*COUGH* *COUGH*{/b} Hah... I can conceal the mark."
    mh8 "{i}*wince*{/i} My knee...{w=1.0} You alright?"
    st3 "Almost landed on my glasses. {i}*exhale*{/i}"
    t_nat "Inoue and Sayo, you two come with me. We have to discuss the consequences of your actions. The rest of you I will be needing as witnesses."

    "Inoue hung her head, biting her lips upon realizing it. Sayo dusted herself and wore her glasses."

    sr5 "This is madness..."

    "She did not care whether five minutes remain from the lunch period. Ms. Natsumoto led the students to her office, Sayo and Inoue leading the students."
    return

label ch03_05_aftermath:
    scene black with fade
    if path_b1 < 0:
        call ch03_05A_guilty
    elif path_b1 >= 0:
        call ch03_05B_innocent
    return

label ch03_05A_guilty:
    if path_b1 == 0:
        $ path_b1 = -1

    scene black with fade
    "{color=#bd0000}AUGUST 5, 2013 - 1225H{/color}"

    window show
    nvl clear
    narr "The bell had rung. Classes have resumed. Yet the eight remianed inside Ms. Natsumoto's office while Sayo and Inoue were being questioned."
    narr "Inoue gnashed her teeth at the girl across from her. She could not overcome the embarrassment. What will her mother say?"
    narr "Though all six witnesses' accounts are consistent with each other, they remained nervous.{w} Ms. Natsumoto was known to be harsh with her words."
    narr "Ms. Natsumoto laid back on her chair after hearing what she needed."

    nvl clear
    window hide

    t_nat "Alright, kids. You may return to your classrooms now.{w=1.0} Let me just finish our heart-to-heart talk."

    "They complied, leaving the room without speaking. Even outside, they lacked any words."

    t_nat "Now, what do you have to say for yourselves?{w=1.0} Shall this be the last time I'll have you two for assault?"
    sr5 "I apologize for my involvement, ma'am. Throughout our discussion, I never intended to incite any provocation towards Inoue."
    t_nat "Inoue, let me remind you that my patience with you is stretching thin.{w=1.0} You can't quite control yourself and hurt other people during your outburst."
    is4 "It was an honest mistake, ma'am. I gave in to my own fury."
    t_nat "Again, can you handle your emotions just fine?"
    is4 "Yes... I apologize."
    t_nat "Understood. And I will not call your parents for this.{w=1.0} What I want to see before you part ways is you girls making a truce.{w=1.0} Look each other in the eye and shake hands."

    window show
    nvl clear
    narr "Inoue followed the first instruction, giving Sayo a cold glare. In contrast, Sayo gave a genuine smile.{w} They exchanged weak handshakes before dropping their hands."
    narr "With this, Ms. Natsumoto dismissed the two girls.{w} They left the office, Sayo opening the door."
    narr "Inoue zipped past Sayo and left her behind. She rubbed her hand disgustedly as she entered her classroom."
    narr "For Ms. Natsumoto, everything was resolved.{w} For Inoue, however, grudges do not fizzle out that easily."

    nvl clear
    window hide

    "{color=#bd0000}AUGUST 5, 2013 - 1425H{/color}"

    ys6 "Now. Now. Let's not get ahead of ourselves.{w=1.0} We ask you once more, Inoue, are you a hundred percent sure of your statements?"
    is4 "You think I'm off my head, don't you?"
    ys6 "We don't.{w=1.0} If you were to ask my honest opinion, there are a few questionable details in your story. Emmerich would be quick to pick them apart...{w=1.0} {cps=30}unless he already did.{/cps}"
    is4 "Talk to him, then! Why would I disadvantage myself with lies? Things are already complicated as they are."
    ys6 "Exactly what I want to hear. Thank you."

    "His questioning done, Yoshiro stepped aside and allowed her some breathing space."
    "Akira looked to the left.{w} He saw, sitting on the bench outside IV-E, Sayo and Ikuko. Miyu limped back and forth as he voiced his frustrations."

    is4 "Why is he on that girl's side?"
    ai2 "Don't think too much about it. He's probably just getting her side of the story."
    is4 "What lies are she feeding him? How did he find her trustworthy?"
    iy1 "Shouldn't we say the same for you as well? Thinking about it..."
    is4 "Ichi, you shut the f--{nw}"
    ai2 "Inoue!{w=0.5} Ichi!"

    "Akira's concerned eyes tore their faces.{w=1.0} Ichirou shrugged it off, Inoue remaining agitated."

    iy1 "Look. If you were to this to anyone besides us and your family, they're gonna think you did it. Will they understand?{w=1.0} Nine of ten times, they won't."
    iy1 "What you testified is detrimental to your case. Imagine how credible you will be when you say it as it is."
    is4 "Hmmmmmm..."
    ys6 "I'm afraid we have nothing to go on except her story and the initials of our culprit, L.C."
    ai2 "That doesn't include everything that's just happened, though."

    "Ichirou huddled them together, directing them away from the classroom. He continued in a low voice."

    iy1 "I'm sorry, guys. I can't hide Hiroshi's death any longer."
    ai2 "You're going to tell them?! Do you want us to get probed if this elevates to a scandal?"
    iy1 "I can't stand my classmates comparing Hiroshi's sudden disappearance to that of Kyou and Inoue's."
    ai2 "Can't we wait for Inspector E. a little longer?"
    iy1 "I'm not waiting for that damned inspector! His security measures was a dud!{w=1.0} If we ever want to convict L.C. for their crimes, I suggest we do it ourselves."

    "Ichirou looked to the left, catching a glimpse upon Miyu returning to IV-C."

    iy1 "If the fox does not wish to come out of its hole, then we force it to.{w=1.0} On the off-chance we are wrong about our assertions...{w=3.0}{nw}"
    iy1 "{cps=25}...Then we seek the answers another way.{/cps}"
    ys6 "How about we go to the archives and look up anyone who bears L.C.'s initials?"
    is4 "I'm fine with that. When do we go?"
    ys6 "This Saturday -- Freedom Park at ten o' clock."
    iy1 "I don't have any prior engagements on that day. Count me in."
    ai2 "I'm free to go, too, but can't we just search it on the internet?"
    iy1 "Nope. Some pieces of information are only available physically. There is bound to be false information circulating around online."
    iy1 "So, come along unless you want to get left behind."

    "With everything settled, the group dispersed."
    return

label ch03_05B_innocent:
    if path_b1 == 0:
        $ path_b1 = 1

    scene black with fade
    "{color=#5decff}AUGUST 5, 2013 - 1225H{/color}"

    window show
    nvl clear
    narr "The bell had rung. Classes have resumed. Yet the eight remained inside Ms. Natsumoto's office while Sayo and Inoue were being questioned."
    narr "Nobody lied about the events. It was Inoue who struck first and Sayo who chose not to fight back.{w} Had she done otherwise, she would have been imposed a serious penalty and risk her position."
    narr "Miyu girmaced as he rubbed against the tiny bruises on his left arm and knee. He had hit the edge of the stone seat.{w} Sumiko was cleaning his glasses, checking it for any cracks."
    narr "Ms. Natsumoto laid back on her chair and looked at the six students."

    nvl clear
    window hide

    t_nat "Alright, kids. You may return to your classrooms now.{w=1.0} Let me just finish our heart-to-heart talk."

    "They complied, leaving the room without speaking. Even outside, they lacked any words."

    window show
    nvl clear
    narr "While IV-B's teacher had arrived, IV-C was five minutes into their lesson.{w} The teacher was their co-adviser, glaring at them arms crossed."
    narr "Sumiko explained the situation and they were let inside."
    narr "Back at the guidance counselor's office, Ms. Natsumoto had already decided on her course of action."

    nvl clear
    window hide

    t_nat "Inoue, let me remind you that my patience with you is stretching thin.{w=1.0} You can't quite control yourself and hurt other people during your outburst."
    is4 "It was an honest mistake, ma'am. I gave in to my own fury."
    t_nat "Again, can you handle your emotions just fine?"
    is4 "Yes... I apologize."
    t_nat "Understood. And I will not call your parents for this.{w=1.0} What I want to see before you part ways is you girls making a truce.{w=1.0} Look each other in the eye and shake hands."

    window show
    nvl clear
    narr "Sayo took the initiative and extended her right hand. She received a cold glare before Inoue gave in to Ms. Natsumoto's request."
    narr "With this, Ms. Natsumoto dismissed the two girls.{w} They left the office, Sayo opening the door."
    narr "Inoue zipped past Sayo and left her behind. The latter understood her urgency, yet she felt some hint of animosity."
    narr "The aftermath had further drifted them away, opposite of what Sayo had hoped to occur."

    nvl clear
    window hide

    "{color=#5decff}AUGUST 5, 2013 - 1420H{/color}"

    "Sayo buried her face within her hands as Ikuko listened to whatever she had to say."
    "Miyu, despite his injury, paced back and forth in front of IV-E, outraged at the outcome of Inoue's questioning."

    mh8 "Shall we report this to Mrs. Genkai?"
    sr5 "It would make no difference. Doing so implies an abuse of power and would worsen my image."
    mh8 "I understand you need to uphold your role model principle, but get this. She acted like she wasnted to kill you."
    sr5 "I know how she feels. I have forgiven her, Miyu.{w=1.0} She may have wronged me but she did so while her mind was clouded."
    mh8 "She did no better!"
    ikuko "Mi-kun, please calm down. Sayo's having a lot running in her head now."
    mh8 "She's being falsely accused of murder or at least masterminding the kidnappings. That's what started this whole rift in the first place."
    mh8 "I suppose you're aware of the consequences if we let this slide."
    ikuko "I know that."
    mh8 "Then we {i}cannot{/i} let this slide, Ikuko. We already have two victims because of negligence. Worse, one of them met their end inside the Council office!"
    sr5 "That's enough!"
    mh8 "{i}*GASP*{/i}"

    "Her lashing resonated around the walls of the classroom, conjuring a moment of silence and several intrigued eyes to take a gander.{w} Miyu hung his head and stopped in his tracks."

    sr5 "{i}*sigh*{/i} I fully comprehend the situation. I would rather not witness another murder myself."
    mh8 "..."
    sr5 "Do you know the difference betwen your sentiments and mine?"
    mh8 "I do."
    sr5 "I'm the head of the studentry, and protecting it is part of the code I upkeep.{w=1.0} I failed in that, the thought gnawing at me each day."
    sr5 "That makes me no different from Inoue.{w=1.0} She was helpless in preventing Kirisaki's death. I did nothing to ensure Hiroshi's safety."
    sr5 "I never wished misfortune to befall upon anyone, petty or not.{w=1.0} When that voice called us, I asked myself, \"Why?\"{w=2.0} {cps=25}Of all people, why me?{w=1.0} Why {i}you{/i}?{w=1.0} Why {i}them?{/i}{/cps}{w=1.0} Ask yourself, did you ever will for this to happen?"
    mh8 "..."
    mh8 "{cps=15}I'm scared...{/cps}"
    sr5 "Pardon?"
    mh8 "I don't want to die.{w=1.0} Not in the way Kyou and Hiroshi did.{w=0.5} It's messed up -- butchered like animals!"
    ikuko "Me neither.{w=1.0} All I can do now is to assure my parents of my safety. I might never set foot in MSCI again should another one fall."
    mh8 "Tch.{w=1.0} If only Emmerich would hurry up with his investigation and jail that criminal."
    mh8 "I cannot stand watching people point fingers on a hunch. If we are to nab the killer, I suggest we do it now.{w=1.0} We are the most affected, after all."
    sr5 "And also the persons of interest."
    mh8 "That, too."

    "{i}*snap*{/i}"

    ikuko "How about you approach this from another angle?{w=1.0} If we cannot draw any information from ourselves, even with Inoue, then we investigate the next best thing."
    sr5 "That is preferable."
    mh8 "What would the \"next best thing\" be?"
    ikuko "Sayo-chan told me about the similarity in motif between our own murders and those of Sacred Heart Academy. Why don't you start at the root?"
    mh8 "That's brilliant! I see how that would work for us."
    mh8 "Although... there is one glaring problem.{w=1.0} Rika Suzumiya, the closest we have to the main suspect, is one of the victims herself. After her, we have no significant leads."
    sr5 "We have another option.{w=2.0} We can trace the killer's identity through the methods. We might uncover a link."
    mh8 "A link! Interesting...{w=1.0} And we might shoot a second bird in the interim."
    sr5 "That...{w=1.0} we exclude ourselves. Let's focus on our own problems while they are still young."
    mh8 "So, this weekend?"
    sr5 "Sunday. I have already blocked my schedule for Saturday."
    mh8 "That's the Sabbath Day. I don't usually agree to come on that day."
    sr5 "Hm?"
    mh8 "Just this once, then. We no longer have a safe time frame for the month, if you may also recall."
    sr5 "Hehehehehehe. True."

    "Exciting, maybe, given how they marveled at the idea. At the same time, it is all for Sayo's innocence."

    mh8 "Want to come along, Ikuko?"
    ikuko "I would love to, but I have Church on Sunday. You go on ahead. I'll be hearing the results afterwards if you wish."
    mh8 "Then it's settled. {i}*chuckle*{/i}"

    "After exchanging a few more words, Miyu returned to IV-C.{w} He spotted Hikaru eating with Aria. Sumiko had returned from the canteen."

    mh8 "Hikaru, Sumiko, I want to ask you two something."
    hy10 "What is it?"
    mh8 "Sayo is inviting us this Sunday to do some sleuthing at Sacred Heart Village. She said it's the best way to gather information about the current case."
    hy10 "{i}That{/i} far? We have a church gathering late afternoon."
    st3 "Is there any other alternative? I'm okay with anything as long as we're all going."
    mh8 "We can't schedule it this Saturday because Sayo has prior commitments."
    st3 "And we might bump into the {i}other faction{/i} should we decide to go on that day."
    mh8 "Then we find a compromise. It's the last {i}safe{/i} weekend before L.C. makes their move."
    hy10 "I'll let you guys know, then. Let me see if I can convince Mama and Papa about this."

    "And they returned to their respective seats, agreeing to discuss the rest over Facebook."
    return

label ch03_06_investigation1:
    scene black with fade
    "AUGUST 7, 2013 - 0745H"

    window show
    nvl clear
    narr "The police station felt peaceful. The usual clicks of the keyboards and the constant ringing were absent."
    narr "Emmerich, tipsy due to lack of sleep, punched in his time card and walked to his cubicle.{w} Trevors had not arrived yet; they would enjoy a cup of coffee to wear off the grogginess."

    nvl clear
    narr "He tidied his desk and set his laptop up. He supported his head with his wrist and closed his eyes while waiting."
    narr "The folder on top is Kyou Kirisaki's final autopsy report. It had some small deviations but none too significant.{w} He was waiting for Hiroshi Kano's own report, which the coroner estimated to be completed by next week."
    narr "Ah! Before anything on the computer, Emmerich skimmed his notes regarding the latest murder."
    narr "It was done behind closed doors."

    nvl clear
    window hide

    $ current_area = 0 # Office
    $ lock = 0 # Locks on to the current menu
    $ areas = 3 # [Office, Conference Room]
    $ visited = 0 # [Office, Conference Room]
    $ i1_office = 0
    $ i1_conference = 0

    while i1_office < 7 or i1_conference < 15:
        if current_area == 0: # Office
            if not parse_bin(visited, 0):
                window show
                nvl clear
                narr "It had rained that night.{w} The culprit saw their chance to act during the ensuing blackout."
                narr "Had they been too late? Too incompetent to stop the murders?{w} For Emmerich, it is the former -- all planned by a cunning mind."
                narr "The witnesses were rounded up in the conference room while investigation in the crime scene was ongoing."

                nvl clear
                window hide

                centered "{color=#bd0000}--INVESTIGATION START--{/color}"
                "{color=#808080}It is procedural to first examine the body and the surrounding area.{w=2.0} Afterwards, you can interview the witnesses in the next room.{/color}"
                "{color=#808080}In any Investigation, the rule of thumb is to examine every area and talk to all witnesses. Some of your choices can unlock certain options or affect the story. Happy sleuthing!{/color}"
                $ visited += 1

            if not parse_bin(visited,0):
                $ visited += 1
            menu:
                "Examine":
                    menu:
                        "Workstation":
                            $ lock = 1

                            while lock == 1 and (i1_office < 7 or i1_conference < 15):
                                menu:
                                    "Corpse":
                                        "The body occupies one of the workstations, belonging to a certain Akira Ichibana -- auditor of the Student Council."
                                        "The victim is in a sorry state. His face and neck are bound tightly with masking tape. The intent was to kill the victim either by asphyxiation or blood loss."
                                        "Both of his hands lie on the desk. All of his fingers are chopped, the indices spread around the workstation."
                                        "Turning over his hands reveals two numbers etched onto his palms."
                                        "Number {color=#bd0000}7{/color} on the left, number {color=#bd0000}10{/color} on the right. They are carved similar to the ones on Kyou Kirisaki's body."
                                        
                                        if not parse_bin(i1_office,0):
                                            $ i1_office += 1

                                    "Bloody Message":
                                        "There is a message written with the victim's left index finger."
                                        "{color=#bd0000}{i}The mind only stops when the body does,{w=1.0}\nThe roulette's outcome, no doubt, indeed's a loss.{/i}{/color}"
                                        "I must make note of that. It sounds cryptic and irrelevant but it may be of use later on."
                                        
                                        if not parse_bin(i1_office,1):
                                            $ i1_office += 2

                                    "Computer" if parse_bin(i1_conference,2):
                                        "The object of interest here is the flash drive the victim was using before his demise."
                                        "There was nothing, as expected. Even a body search turned up negative results."
                                        "It can be assumed that the suspect had taken the device with them. It must hold more significance than I thought.{w} Perhaps it contained something incriminating?"

                                        if not parse_bin(i1_office,2):
                                            $ i1_office += 4

                                    "<<< BACK":
                                        $ lock = 0
                        
                        "<<< BACK":
                            pass

                "Move":
                    menu:
                        "Conference Room" if parse_bin(areas,1):
                            $ current_area = 1
                        "<<< BACK":
                            pass

        elif current_area == 1: # Conference Room
            if not parse_bin(visited,1):
                $ visited += 2
            menu:
                "Talk":
                    menu:
                        "Sayo Ronoroa":
                            $ lock = 1
                            if not (parse_bin(i1_conference,0) and parse_bin(i1_conference,1)):
                                "The Student Council President's eyes are swollen. Though visibly shaken, she wore a brave face to help with the investigation."
                                p_emm "I'm sorry for your loss, Sayo. This is unfortunate."
                                c_sr5 "Truly.{w=0.5} And in the middle of a storm!{w=1.0} {i}*sigh*{/i} Taking advantage of the outage to strike -- the mark of a monster."
                                p_emm "If I may, I need to ask you some preliminary questions before we invite you to the station."
                                c_sr5 "Ah. The classic \"ask the suspects in the crime scene\" technique, I see.{w=1.0} Very well. I will be glad to help."

                            while lock == 1  and (i1_office < 7 or i1_conference < 15):
                                menu:
                                    "Last seen alive":
                                        p_emm "What happened here? Rather, when did you last see Hiroshi alive?"
                                        c_sr5 "I stayed for a while here until around 6:15 PM, at which I reported to our adviser, Mrs. Genkai."
                                        c_sr5 "Hiroshi said he was working on a project -- not sure what. A little after, the power outage occurred."

                                        if not parse_bin(i1_conference,0):
                                            $ i1_conference += 1

                                    "Power outage":
                                        p_emm "Does the power outage happen often?"
                                        c_sr5 "Not really. During August to October, the frequency on average is about three times.{w=1.0} Either the power is restored immediately or we are told to go home."
                                        c_sr5 "This is the latest I have stayed during an outage."
                                        p_emm "By the way, between the power outage and the discovery of the body, did you enter this office in the interim?"
                                        c_sr5 "I did."

                                        if not parse_bin(i1_conference,1):
                                            $ i1_conference += 2

                                    "Let's discuss the rest later.":
                                        p_emm "Let's discuss the rest later. I feel that we will take forever if I ask every question now."
                                        c_sr5 "Don't worry. Good luck on your investigation, Inspector."

                                        $ lock = 0

                        "Akira Ichibana":
                            $ lock = 1
                            if not (parse_bin(i1_conference,2) and parse_bin(i1_conference,3)):
                                "I recognize him.{w} He is one of Ichirou's chipper friends."
                                "Sadly, that peppiness is overshadowed by his somberness. If I had to guess, he was the first to discover the body."
                                p_emm "Good evening, young sir."
                                c_ai2 "Oh! You're Inspector E, right?{w=1.0} I'm Akira. Akira Ichibana."
                                p_emm "No need to panic. {i}*chuckle*{/i} I'm here. Everything will be alright."
                                c_ai2 "You mean no bogeyman will come at us from the shadows?"
                                p_emm "You still believe in those things?!"
                                p_emm "Ahem!{w=0.5} Excuse my rudeness.{w=1.0} Anyway, I need to ask you a few questions. The victim is sitting on your workstation."
                                c_ai2 "If it would help nab that freak, I'm in!"

                            while lock == 1 and (i1_office < 7 or i1_conference < 15):
                                menu:
                                    "Discovered body":
                                        p_emm "From your behavior, I surmise that you were the nearest to the victim at the moment of discovery."
                                        c_ai2 "Why, yes! You are as sharp as they made you."
                                        p_emm "Thank you. Now, what was the victim doing at your workstation?"
                                        c_ai2 "Working on something. Said his family desktop was busted.{w=1.0} If I may mention, I saw him insert a flash drive into the CPU."
                                        p_emm "Of course, he would. You just told me why."
                                        c_ai2 "No. That flash drive didn't look like his. I don't know."
                                        p_emm "I noticed nothing of the sort but I will double check."
                                        p_emm "Let me remind you, however, that not every new flash drive you see means something bad. It could be that the original device is broken."

                                        if not parse_bin(i1_conference,2):
                                            $ i1_conference += 4

                                    "Power outage":
                                        p_emm "Where were you during the power outage?"
                                        c_ai2 "Doing my business. I was with these three stooges."
                                        p_emm "Past your curfew? Why did you not go home right away?"
                                        c_ai2 "I have LBM...{w=1.0} and I didn't bring some meds."
                                        p_emm "You learned your lesson, big boy.{w=1.0} About those \"three stooges,\" were they with you the whole time?"
                                        c_ai2 "I'm not sure. I called out to them but nobody responded.{w=1.0} The feeling that you're trapped inside that bathroom stall...{w=1.0} It almost drove me insane."
                                        c_ai2 "When I burst out of the stall, they were there the whole time. A prank done in poor taste, I say!"
                                        p_emm "That might have given me an idea."

                                        if not parse_bin(i1_conference,3):
                                            $ i1_conference += 8

                                    "We'll discuss this in depth later.":
                                        p_emm "We'll discuss this in depth later."

                                        $ lock = 0
                        
                        "<<< BACK":
                            pass

                "Move":
                    menu:
                        "Office" if parse_bin(areas,0):
                            $ current_area = 0
                        "<<< BACK":
                            pass

    scene black with fade
    centered "{color=#5decff}--INVESTIGATION COMPLETE--{/color}"

    window show
    nvl clear
    narr "The investigation wrapped up before 8 PM."
    narr "Throughout the previous hour, Emmerich contacted the witnesses' parents to inform that their children would spend the night at the station and why."

    nvl clear
    narr "When they arrived, some of them were already there, bringing dinner for their children."
    narr "Emmerich instructed the parents to keep mum about the murder and assured their children's safety. He asked them to return at seven o' clock in the morning."
    narr "Afterwards, they descended to the underground interrogation room."

    nvl clear
    window hide

    officer "Harold, your cheesecake slice and arabica."
    p_emm "Thanks, Trevors. {i}*siiiiiip*{/i}{w=3.0} I wonder how these kids are doing?"
    officer "Can't answer that. You're closer to them than I am."

    "Trevors shrugged and walked away. Coffee in hand, Emmerich began working on his laptop."
    return

label ch03_07_investigation2:
    if path_b1 < 0:
        call ch03_07A_guilty
    elif path_b1 >= 0:
        call ch03_07B_innocent
    return

label ch03_07A_guilty:
    if path_b1 == 0:
        $ path_b1 = -1

    scene black with fade
    "{color=#bd0000}AUGUST 10, 2013 - 1000H{/color}"

    "At our designated meeting place, two people were already there.{w} Yoshiro was playing with his speed cube; Inoue was texting on her phone."
    "And I thought I would be the last to arrive. Is Akira in a traffic jam again?"

    ys6 "Oh, you're finally here!{w=1.0} Just a moment. Akira is buying some bread."

    "True enough, he approached us with a bag of pastries and munched on a big ensaymada."

    iy1 "That's too much sugar in the morning. Plus, we aren't allowed to make a mess inside the library."
    ai2 "I know, but this is my breakfast.{w=0.5} Woke up before nine. Ahehehehehe."
    iy1 "It's a miracle you arrived before me. And that means you have less time to finish that before we reach our itinerary."
    is4 "So, where is the city library again?"
    ys6 "At the park near my girlfriend's house.{w=1.0} I will lead the way."
    ai2 "Cool! Let's go."

    "He was already on his second pastry.{w=1.0} The pig!"

    window show
    nvl clear
    narr "We discussed our plans for the day.{w} If we are lucky, we would be done before mid-afternoon. There is a fastfood restaurant nearby if we ever get hungry."
    narr "Past the wet market is the house of a famous artist-comedian. He was sitting in front of his store, playing a guitar while greeting passersby. He and our group exchanged smiles and salutes."
    narr "Once we made it out of the street, we were at Kutsutochi North.{w} To the right is my alma mater and its chapel. Across from us is the cultural center designed to be an ancestral home."

    nvl clear
    narr "Westward is our destination, Kutsutochi Public Library."
    narr "It always seemed quiet, not seeing that many patrons even during weekends. Unsurprising given how few students ever go to their school library."
    narr "Akira disposed of the paper bag, wiping his mouth and hands with tissue."

    nvl clear
    window hide

    ai2 "Three pieces to last the day!"
    iy1 "Good. My calculations were correct."

    "We went inside, the musky smell of colonial times wafted the air."
    "The floors were waxed to resemble a mirror, and light reflected well on the varnished wood. Air conditioners are engaged all over the building.{w} It is a big wonder why no one comes to even sleep here."
    "Besides the librarian's desk is the Citizen's Charter and a map of the facility."

    ys6 "Two floors, huh? How do we go about this?"
    iy1 "Why don't we ask the librarian first before anything? Besides we need a guide if we want to accomplish our goal much quicker."

    centered "{color=#bd0000}--INVESTIGATION START--{/color}"

    $ current_area = 0 # Circulation
    $ lock = 0 # Locks on to the current menu
    $ areas = 1 # [Circulation, General Reference*, Periodicals*]
    $ visited = 0 # [Circulation, General Reference, Periodicals]
    $ i2a_circulation = 0
    $ i2a_genreference = 0
    $ i2a_periodicals = 0

    while i2a_genreference not in [24, 25, 26, 28, 29, 30, 31] or i2a_periodicals not in [187, 191, 251, 255]:
        if current_area == 0: # Circulation
            if not parse_bin(visited,0):
                $ visited += 1
            menu:
                "Examine":
                    menu:
                        "Information Desk":
                            $ lock = 1

                            while lock == 1 and (i2a_genreference not in [24, 25, 26, 28, 29, 30, 31] or i2a_periodicals not in [187, 191, 251, 255]):
                                if not (parse_bin(i2a_circulation,0) and parse_bin(i2a_circulation,1)):
                                    "The lady behind the desk is a middle-aged woman. She is busy on some paperworks but set them aside after seeing us approach."
                                    librarian "Good morning.{w=1.0} How may I be of assistance?"

                                menu:
                                    "Operating hours":
                                        iy1 "What are your operating hours?{w=1.0} We might need to drop by here at night -- not today, of course."
                                        librarian "8 AM to 10 PM during weekdays.{w=1.0} On Saturdays, 8 AM to 6 PM."
                                        iy1 "Ah, thank you."
                                        librarian "Is this your first time to visit?"
                                        iy1 "Yes, ma'am."
                                        librarian "I see. Do you want to apply for a library card?{w=1.0} You just need a 1x1 ID Picture and a small fee."
                                        iy1 "I'll think about it, but I have to refuse.{w=1.0} Interesting offer, by the way."

                                        if not parse_bin(i2a_circulation,0):
                                            $ i2a_circulation += 1

                                    "Archives section":
                                        iy1 "Do you have an archives section? We can't find on the map over there."
                                        librarian "We do have a public archives but in the Periodicals section. You can check there."
                                        librarian "If you need assistance retrieving old publications and the like, do not hesitate to come down here."
                                        iy1 "Thank you!"
                                        ys6 "That's on the second floor next to the west staircase.{w=1.0} Shall we go now?"
                                        ai2 "Wait.{w=1.0} Can some of us be left here at the first floor? There are some things I want to check."
                                        ys6 "We can stay afterwards if we have time. Postpone your homework duties until then."
                                        ai2 "No, it's not that.{w=1.0} There are a few specific points in Inoue's story that piqued my curiosity."
                                        is4 "What {i}things{/i} are you talking about, Akira?"
                                        ai2 "Monsters and mazes!{w=1.0} Sci-fi levels of science, chemicals and whatnot!{w=1.0} Conspiracy theories and magic!{w=1.0}"
                                        "........."
                                        iy1 "{cps=10}Okay...{/cps}{w=2.0} Do what you have to --{nw}"
                                        ai2 "Yay! See you guys later!{w=2.0}{nw}"

                                        "He disappeared into the bookshelves, leaving the three of us dumbfounded with his behavior --{w=1.0} excessive peppiness, at that."

                                        is4 "Why did you let him run off like that?!"
                                        ys6 "He knows what he's doing.{w=1.0} And we can text him if ever we find anything."

                                        if not parse_bin(i2a_circulation,1):
                                            $ i2a_circulation += 2
                                            $ areas += 6

                                    "L.C. initials" if parse_bin(i2a_periodicals,0):
                                        if not parse_bin(i2a_circulation,2):
                                            $ i2a_circulation += 4

                                    "Children's section" if parse_bin(i2a_periodicals,5):
                                        if not parse_bin(i2a_circulation,3):
                                            $ i2a_circulation += 8

                                    "<<< BACK":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Talk":
                    menu:
                        "Yoshiro Suzuki":
                            $ lock = 1

                            while lock == 1 and (i2a_genreference not in [24, 25, 26, 28, 29, 30, 31] or i2a_periodicals not in [187, 191, 251, 255]):
                                menu:
                                    "What to look for?":
                                        iy1 "Let's go over our plan once more.{w=1.0} We're here to find out who this L.C. is if such a person exists."
                                        ys6 "Right. We can start by looking at some records related to both Kutsutochi and Sacred Heart Village.{w=1.0} We may also find some publications involving the person if needed."
                                        iy1 "Is that all?"
                                        ys6 "I might have missed something, but that's all for now.{w=1.0} There is a wealthy amount of books and papers to check in this library. Let's spend some extra reading time in case they might help us."
                                        iy1 "Copy."

                                        if not parse_bin(i2a_circulation,4):
                                            $ i2a_circulation += 16

                                    "Night of the murder":
                                        ys6 "Ichi, what happened that night? I don't have a full grasp of the details."

                                        "I told him everything --{w=1.0} why Hiroshi opted to be left behind, the prank we pulled on Akira, who went to the office and when, among other things."

                                        ys6 "That's it?"
                                        iy1 "To the best of my memory."
                                        ys6 "So, that's the basis of your accusation?{w=1.0} Because the last person to be with Hiroshi is Sayo?"
                                        iy1 "No one else has the opportunity. She even admitted as much when Emmerich interviewed her."
                                        iy1 "We were on the other side of the map.{w=1.0} It's impossible for any of us to get there unless we magically teleport to the Council room.{w=1.0} What reason do we have to kill him, anyway?"
                                        ys6 "{cps=15}Really...?{/cps}{w=1.0} I'll see what Akira has to say."
                                        iy1 "What? You don't believe me?"
                                        ys6 "Don't misread it. I just want to know as many angles of the story as possible."

                                        if not parse_bin(i2a_circulation,5):
                                            $ i2a_circulation += 32

                                    "Science Club presidency":
                                        iy1 "Yoshiro,{w=1.0} I've been thinking about this for quite some time. I even consulted with our fellow officers."
                                        ys6 "If this is about the succession of the Sci Club presidency, forget it."
                                        iy1 "More than that. I'm not interested, myself."
                                        ys6 "So, why are we having this discussion?"
                                        iy1 "{cps=20}How should I say this...?{/cps}{w=2.0} By the end of this week, I will resign my position as Secretary."
                                        ys6 "Who will replace you?"
                                        iy1 "Hisashi Odome.{w=1.0} I spoke to him about it a few weeks back."
                                        ys6 "That's rash of you. Why didn't you inform everyone so we can decide on a proper course of action?{w=1.0} Only now you're telling us about this?!"
                                        iy1 "Do you think I have the guts to face our Vice President after that fiasco in the Council room?{w=1.0} What will he say?"
                                        ys6 "That you're a coward who cannot live up to his word.{w=1.0} Even in the darkest of times, we are expected to hold the fort, not desert it."
                                        ys6 "How about you?{w=1.0} Do you think you can hold on to {i}your{/i} fort a little longer?"
                                        iy1 "{b}{i}*grumble*{/i}{/b}"

                                        "The nerve...{w=1.0} and right straight to my face!"

                                        ys6 "End of discussion. Save your prideful outburst for later."

                                        if not parse_bin(i2a_circulation,6):
                                            $ i2a_circulation += 64

                                    "Catch you later.":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Move":
                    menu:
                        "General Reference" if parse_bin(areas,1):
                            $ current_area = 1

                        "Periodicals" if parse_bin(areas,2):
                            $ current_area = 2
                            
                        "<<< BACK":
                            pass

        elif current_area == 1: # General Reference
            if not parse_bin(visited,1):
                window show
                nvl clear
                narr "While Inoue and Yoshiro are at the second floor, I went to the General Reference section to fetch Akira.{w} Texting a silent phone is unreliable; it's better if all four of us are present."
                narr "Akira indulged himself to a biochemistry book.{w} He went undisturbed for five minutes before closing the book and noticing my presence."

                nvl clear
                window hide

                ai2 "Been waiting long?"
                iy1 "I came here to check on you.{w=1.0} Care to share what knowledge you have gained from that?"
                ai2 "Oh, this?{w=0.5} I don't understand it, honestly. {i}*chuckle*{/i}{w=1.0} However, you can check them yourself if you like."

                "He slid a notepad page over the table."
                "It contained call numbers for three of the books he had been reading.{w} These might prove useful even if they may not be all that much."

                iy1 "Cool. The two are waiting upstairs.{w=1.0} You don't want to come with me?"
                ai2 "Text me if you find anything. I'll be sticking around for a while so we can distribute our reach.{w=1.0} I won't mind if you want to strike up a good ol' chat."

                $ visited += 2

            if not parse_bin(visited,1):
                $ visited += 2
            menu:
                "Examine":
                    menu:
                        "Bookshelves":
                            $ lock = 1

                            while lock == 1 and (i2a_genreference not in [24, 25, 26, 28, 29, 30, 31] or i2a_periodicals not in [187, 191, 251, 255]):
                                menu:
                                    "Biochemistry":
                                        if not parse_bin(i2a_genreference,0):
                                            $ i2a_genreference += 1

                                    "Greek Mythology":
                                        if not parse_bin(i2a_genreference,1):
                                            $ i2a_genreference += 2

                                    "Criminal Psychology":
                                        if not parse_bin(i2a_genreference,2):
                                            $ i2a_genreference += 4

                                    "<<< BACK":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Talk":
                    menu:
                        "Akira Ichibana":
                            $ lock = 1

                            while lock == 1 and (i2a_genreference not in [24, 25, 26, 28, 29, 30, 31] or i2a_periodicals not in [187, 191, 251, 255]):
                                menu:
                                    "Sorry for prank":
                                        iy1 "Hey, Akira.{w=1.0} About that prank in the male restroom..."
                                        ai2 "Yeah?"
                                        iy1 "I'm sorry we stepped over the line. I never knew you could turn violent when provoked.{w=1.0} Heck!{w=0.5} You must have exceeded your breaking point."
                                        ai2 "Ahahahahaha... I'm sorry, too."
                                        ai2 "But you gotta understand, Ichi,{w=1.0} the times aren't as colorful as they were. The phantom can strike at any time."
                                        iy1 "Did you know we were calling you when we heard rattling and banging on your stall?{w=1.0} It freaked us out, even more when you gave us no response."
                                        ai2 "You did? I never heard.{w=1.0} Your voice were probably drowned by the rain and the noise I was making. I couldn't keep a straight mind during that moment."

                                        "Did I remember it right?"

                                        ai2 "I was screaming to you guys for help. That's why I was banging the stall door open."
                                        iy1 "We didn't hear you.{w=0.5} At all."

                                        centered "{color=#808080}{cps=20}Weird.{w=1.0} I heard upperclassmen tell ghost stories concerning the restrooms before.{w=1.5} The girls' restroom had Samantha. What about the boys' restroom?{w=2.0}\nA portal to another dimension once you lock yourself inside the stall?{/cps}{/color}"

                                        ai2 "I heard someone recite an incantation that sounded like{w=1.0} {cps=20}{i}Hail Mary, full of grace...{/i}{/cps}{w=0.5} and all.{w=1.0} That was you, right?"
                                        iy1 "Right. That was the point when I stopped with the jokes."
                                        ai2 "How do you explain the rattling afterwards?"
                                        iy1 "That wasn't us! We thought you were making that sound."
                                        ai2 "That was when I was trying to force the stall door open. There was another rattling noise before that."
                                        iy1 "We were waiting at the bench, talking about the supernatural phenomena these past few weeks.{w=1.0} We never set foot in the restroom after that incantation."
                                        ai2 "I overheard your conversation.{w=1.0} It's odd how I didn't hear your voice when you were calling me out."
                                        ai2 "{cps=20}But what confuses me the most is...{w=2.0} how was I able to hear {i}those voices{/i}?{/cps}"

                                        "Excuse me?"

                                        if not parse_bin(i2a_genreference,3):
                                            $ i2a_genreference += 8
                                        
                                    "Voices inside your head" if parse_bin(i2a_genreference,3):
                                        iy1 "Voices?{w=1.0} You mean whispers in your head?"
                                        ai2 "Something like that.{w=1.0} I thought one of you was on the other side."
                                        ai2 "{cps=30}Those voices were giggling,{w=0.5} snickering,{w=0.5}, jeering...{w=1.0}{/cps} {cps=25}They were out to get me.{w=1.0} I readied myself in case I wouldn't make it out.{/cps}"
                                        iy1 "Hold on.{w=0.5} Hold on.{w=0.5} What were the voices saying?"
                                        ai2 "{cps=25}After a series of laughs, they counted.{/cps}{w=1.5} {i}{cps=10}One...{w=1.0} Two...{w=1.0} Three...{w=1.0}{/cps}{/i} {cps=25}And then, {i}bang!{/i}{w=0.5} They forcing the door open. They were breaking it down!{/cps}"
                                        iy1 "Who are {i}they{/i}?{w=3.0}{nw}"
                                        ai2 "{cps=25}To be plunged into the darkness like that...{w=1.0} It distorts your reality in a way only your own nightmares can shape.{w=2.0}{/cps} {cps=20}If you weren't pranking me, as you said,{w=1.0} I thought...{/cps}{w=3.0}{nw}"
                                        ai2 "{cps=15}They got you {i}first{/i}.{w=1.5} And it was my fault...{/cps}"

                                        "Akira curled up and bit his lips, stopping any loud sound that may come through his mouth. He wiped the sweat soaking his forehead and darted his eyes around to look for a bottle of water."
                                        "My conscience tugged at me. What have I done to push him this far?"

                                        ai2 "Don't worry about me. {i}*chuckle*{/i}{w=1.0} I'll get up and drink some water later."
                                        iy1 "You should be thankful that these sniggers remained as such."
                                        ai2 "Yeah. {i}*sigh*{/i}{w=1.0} L.C. and their mind games of death...{w=1.0} You either come out dead or almost-dead. It's as if they want our minds to collapse before our bodies."
                                        iy1 "Couldn't agree more.{w=1.0} It's desensitizing enough to see two savaged corpses in a span of one month. Add that I know these victims personally."

                                        "A needle dropped from the other end."

                                        ai2 "I'm doubting things myself, but I can see where you're coming from with regards to Sayo-chan.{w=1.0} Will you really take Inoue's word as it is -- Kyou's death and all?"
                                        iy1 "Hmmm..."
                                        iy1 "Let's talk about that some other time. I'm not in the right mindset to come up with something meaningful."

                                        if not parse_bin(i2a_genreference,4):
                                            $ i2a_genreference += 16

                                    "Talk to you later.":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Move":
                    menu:
                        "Circulation" if parse_bin(areas,0):
                            $ current_area = 0

                        "Periodicals" if parse_bin(areas,2):
                            $ current_area = 2
                            
                        "<<< BACK":
                            pass

        elif current_area == 2: # Periodicals
            if not parse_bin(visited,2):
                $ visited += 4
            menu:
                "Examine":
                    menu:
                        "Newspapers":
                            $ lock = 1

                            while lock == 1 and (i2a_genreference not in [24, 25, 26, 28, 29, 30, 31] or i2a_periodicals not in [187, 191, 251, 255]):
                                menu:
                                    "Research" if not parse_bin(i2a_periodicals,0):
                                        if not parse_bin(i2a_periodicals,0):
                                            $ i2a_periodicals += 1

                                    "Obituaries" if parse_bin(i2a_circulation,2):
                                        if not parse_bin(i2a_periodicals,1):
                                            $ i2a_periodicals += 2

                                    "Sacred Heart Curse Killings":
                                        if not parse_bin(i2a_periodicals,2):
                                            $ i2a_periodicals += 4

                                    "<<< BACK":
                                        $ lock = 0

                        "Photographs":
                            $ lock = 1

                            while lock == 1 and (i2a_genreference not in [24, 25, 26, 28, 29, 30, 31] or i2a_periodicals not in [187, 191, 251, 255]):
                                menu:
                                    "Old MSCI":
                                        if not parse_bin(i2a_periodicals,3):
                                            $ i2a_periodicals += 8

                                    "Missing child" if parse_bin(i2a_periodicals,1):
                                        if not parse_bin(i2a_periodicals,4):
                                            $ i2a_periodicals += 16

                                    "<<< BACK":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Talk":
                    menu:
                        "Inoue Shinozaki":
                            $ lock = 1

                            while lock == 1 and (i2a_genreference not in [24, 25, 26, 28, 29, 30, 31] or i2a_periodicals not in [187, 191, 251, 255]):
                                menu:
                                    "Nursery rhymes":
                                        if not parse_bin(i2a_periodicals,5):
                                            $ i2a_periodicals += 32

                                    "Au Clair De La Lune" if parse_bin(bonus_b1_g,0):
                                        if not parse_bin(i2a_periodicals,6):
                                            $ i2a_periodicals += 64

                                    "Let Carnegie" if parse_bin(i2a_periodicals,4):
                                        if not parse_bin(i2a_periodicals,7):
                                            $ i2a_periodicals += 128

                                    "I'll be going back to research now.":
                                        $ lock = 0

                        "<<< BACK"
                            pass

                "Move":
                    menu:
                        "Circulation" if parse_bin(areas,0):
                            $ current_area = 0

                        "General Reference" if parse_bin(areas,1):
                            $ current_area = 1
                            
                        "<<< BACK":
                            pass

    scene black with fade
    centered "{color=#5decff}--INVESTIGATION COMPLETE--{/color}"

    return

label ch03_07B_innocent:
    if path_b1 == 0:
        $ path_b1 = 1

    scene black with fade
    "{color=#5decff}AUGUST 11, 2013 - 1000H{/color}"

    $ current_area = 0 # Reception Area
    $ lock = 0 # Locks on to the current menu
    $ areas = 1 # [Reception Area, Office*, Archives*]
    $ visited = 0 # [Reception Area, Office, Archives]
    $ i2b_reception = 0
    $ i2b_office = 0
    $ i2b_archives = 0

    while not parse_bin(i2b_archives,2):
        if current_area == 0: # Reception Area
            if not parse_bin(visited,0):
                $ visited += 1
            menu:
                "Examine":
                    menu:
                        "Reception Desk":
                            $ lock = 1

                            while lock == 1 and (parse_bin(i2b_archives,2)):
                                menu:
                                    "Inspector Emmerich":
                                        if not parse_bin(i2b_reception,0):
                                            $ i2b_reception += 1

                                    "<<< BACK":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Talk":
                    menu:
                        "Sayo Ronoroa":
                            $ lock = 1

                            while lock == 1 and (parse_bin(i2b_archives,2)):
                                menu:
                                    "What to look for?":
                                        if not parse_bin(i2b_reception,1):
                                            $ i2b_reception += 2

                                    "L.C.'s challenge":
                                        if not parse_bin(i2b_reception,2):
                                            $ i2b_reception += 4

                                    "Inoue's memories" if parse_bin(bonus_b1_i,1):
                                        if not parse_bin(i2b_reception,3):
                                            $ i2b_reception += 8

                                    "Let's get back to the investigation.":
                                        $ lock = 0

                    "<<< BACK":
                        pass

                "Move":
                    menu:
                        "Office" if parse_bin(areas,1):
                            $ current_area = 1

                        "Archives" if parse_bin(areas,2):
                            $ current_area = 2
                            
                        "<<< BACK":
                            pass

        elif current_area == 1: # Office
            if not parse_bin(visited,1):
                $ visited += 2
            menu:
                "Talk":
                    menu:
                        "Inspector Emmerich":
                            $ lock = 1

                            while lock == 1 and (parse_bin(i2b_archives,2)):
                                menu:
                                    "Purpose of visit":
                                        if not parse_bin(i2b_office,0):
                                            $ i2b_office += 1

                                    "Hiroshi's case":
                                        if not parse_bin(i2b_office,1):
                                            $ i2b_office += 2

                                    "Cursed killings?":
                                        if not parse_bin(i2b_office,2):
                                            $ i2b_office += 4

                                    "We'll get back to you later, Inspector.":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Move":
                    menu:
                        "Reception Area" if parse_bin(areas,0):
                            $ current_area = 0

                        "Archives" if parse_bin(areas,2):
                            $ current_area = 2
                            
                        "<<< BACK":
                            pass

        elif current_area == 2: # Archives
            if not parse_bin(visited,2):
                $ visited += 4
            menu:
                "Examine":
                    menu:
                        "Old Case Files ({i}MH-0809{/i})":
                            $ lock = 1

                            while lock == 1 and (parse_bin(i2b_archives,2)):
                                menu:
                                    "Fuuko Rikiyama":
                                        call ch03_07B1_rikiyama
                                        "{color=#5decff}AUGUST 11, 2013 - 1330H{/color}"

                                        if not parse_bin(i2b_archives,0):
                                            $ i2b_archives += 1

                                    "Rika Suzumiya" if (parse_bin(i2b_archives,0) and parse_bin(bonus_b1_g,1)):
                                        if not parse_bin(i2b_archives,1):
                                            $ i2b_archives += 2

                                    "<<< BACK":
                                        $ lock = 0

                        "Walkie-talkie":
                            $ lock = 1

                            while lock == 1 and (parse_bin(i2b_archives,2)):
                                menu:
                                    "Contact Sarge":
                                        if not parse_bin(i2b_archives,2):
                                            $ i2b_archives += 4

                                    "<<< BACK":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Talk" if parse_bin(i2b_archives,0):
                    menu:
                        "Sumiko Tokubei":
                            $ lock = 1

                            while lock == 1 and (parse_bin(i2b_archives,2)):
                                menu:
                                    "Ichirou's decision":
                                        if not parse_bin(i2b_archives,3):
                                            $ i2b_archives += 8

                                    "Liquid chlorine" if parse_bin(bonus_b1_g,2):
                                        if not parse_bin(i2b_archives,4):
                                            $ i2b_archives += 16

                                    "Live wires":
                                        if not parse_bin(i2b_archives,5):
                                            $ i2b_archives += 32

                                    "<<< BACK":
                                        $ lock = 0

                        "Hikaru Yamamoto":
                            $ lock = 1

                            while lock == 1 and (parse_bin(i2b_archives,2)):
                                menu:
                                    "Inoue's condition":
                                        if not parse_bin(i2b_archives,6):
                                            $ i2b_archives += 64

                                    "Nursery rhymes":
                                        if not parse_bin(i2b_archives,7):
                                            $ i2b_archives += 128

                                    "<<< BACK":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Move":
                    menu:
                        "Reception Area" if parse_bin(areas,0):
                            $ current_area = 0

                        "Office" if parse_bin(areas,1):
                            $ current_area = 1
                            
                        "<<< BACK":
                            pass

    scene black with fade
    centered "{color=#5decff}--INVESTIGATION COMPLETE--{/color}"

    return

label ch03_07B1_rikiyama:
    scene black with fade
    "{color=#808080}JUNE 28, 2012 - 1830H{/color}"

    return

label ch03_08_facts5:
    if path_b1 < 0:
        call ch03_08A_guilty
    elif path_b1 >= 0:
        call ch03_08B_innocent
    return

label ch03_08A_guilty:
    if path_b1 == 0:
        $ path_b1 = -1

    scene black with fade
    "{color=#bd0000}AUGUST 15, 2013 - 1900H{/color}"

    return

label ch03_08B_innocent:
    if path_b1 == 0:
        $ path_b1 = 1

    scene black with fade
    "{color=#5decff}AUGUST 15, 2013 - 1420H{/color}"

    return

label ch03_09_ministryvisit:
    scene black with fade
    return

label ch03_10_facts6:
    if path_b1 < 0:
        call ch03_10A_guilty
    elif path_b1 >= 0:
        call ch03_10B_innocent
    return

label ch03_10A_guilty:
    if path_b1 == 0:
        $ path_b1 = -1

    scene black with fade
    "{color=#bd0000}AUGUST 23, 2013 - 1930H{/color}"

    return

label ch03_10B_innocent:
    if path_b1 == 0:
        $ path_b1 = 1

    scene black with fade
    "{color=#5decff}AUGUST 26, 2013 - 1150H{/color}"

    return

label ch03_11_ceasefire:
    scene black with fade
    return

label ch03_12_death03:
    scene black with fade
    "{color=#808080}AUGUST 23, 2013 - Time Unknown{/color}"

    return

label ch03_13_epilogue:
    scene black with fade
    return