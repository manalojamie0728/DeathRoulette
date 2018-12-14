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
    
    #call ch03_01_prologue1
    #call ch03_02_prologue2
    #call ch03_03_extrareview # REMOVED; UNNECESSARY
    #call ch03_04_decision1
    #call ch03_05_aftermath
    #call ch03_06_investigation1
    #call ch03_07_investigation2 # SKIP FOR NOW; NEED NEW SPRITES
    #call ch03_08_facts5
    #call ch03_09_ministryvisit
    #call ch03_10_facts6
    call ch03_11_ceasefire
    call ch03_12_death03
    call ch03_13_epilogue
    call credits
    return

label ch03_01_prologue1:
    scene black with fade
    "AUGUST 4, 2013 - 0545H"
    scene bg intersection night with fade

    window show
    nvl clear
    narr "In about five minutes, the sun shall grace the horizon once more."
    narr "In about five minutes, the jeepney shall reach the gate of its destination -- the premier university of the country, the National State University."
    narr "In about five minutes, all this three year-long anticipation shall reach its climax."

    scene black with fade
    nvl clear
    narr "The infamous NSUEE (National State University Entrance Exam) has seen tens of thousands of students annually vying for a slot.{w=1.0} Sadly, never have there been a passing rate exceeding one-fifth. Virtually, even a hundred is impossible."
    narr "Nevertheless, it is left to the student's own mileage whether the privilege, should it be granted, is truly worth it.{w=1.0} What lies ahead is a journey that relies on wits, perseverance, and a good heart, not some stroke of luck."
    narr "Past the low hum of the transport's motor are the sounds of nature.{w=1.0} Crickets perform their crescendo before sunrise. At night, they shall do it again. Leaves rustle as they are kissed by the soothing breeze."

    nvl clear
    window hide

    scene bg academicoval with fade
    driver "Engineering!"

    window show
    nvl clear
    narr "I, along with a few others, signaled to stop."
    narr "While my companions immediately headed left towards the College of Engineering, I walked straight ahead.{w} My test center, according to my examination permit, is the College of Law. Two blocks away according to the map."
    narr "The road was nearly empty, devoid of even the usual joggers and bikers on the the inner half the oval. Dubbed the \"Academic Oval\" by NSU denizens, most of the major colleges and institutions are placed around its arc."

    scene bg collegeoflaw with dissolve
    nvl clear
    narr "I arrived at the Law building at around six, nearly the same time as the breaking of dawn.{w} There were already two long queues from the entrance, the right of which I joined."
    narr "The exterior is rather sophisticated.{w} The front pillars and overall architecture resembled that of an actual courthouse --{w=1.0} or at least, the Supreme Court."
    narr "Still, those budding lawyers have quite a home for the next six to seven years. Close to actuality, in fact."

    scene bg collegeoflaw interior with dissolve
    nvl clear
    narr "At 6:15 AM, the marshals and faculty members inspected our permits and guided us to our testing rooms.{w=1.0} An addendum -- these marbled floors are cleanly polished."

    scene bg collegeoflaw classroom with dissolve
    narr "We were escorted to Courtroom No. 4 -- I mean, Lecture Hall No. 4.{w} It was a relatively small room for twenty students. The benches resemble those from a courtroom.{w=1.0} The professor, complete with raised podium, is the judge."
    narr "The aesthetics of this place is impressive. One has to wonder if court will be in session within a few minutes.{w=1.0} It feels as if the twenty of us are participants of a trial, audience or defendants."
    narr "I hope it stays as that. I would prefer being on the witness stand should the time come. Better yet, never set foot in a courthouse ever!"

    window hide
    show eliza serious at Three2 with Dissolve(0.5)
    window show
    nvl clear
    narr "At 6:30 AM, the proctor arrived.{w=1.0} In hand, she had our test booklets and answer sheets. Hanging from her wrist is a timepiece."

    show eliza seriousleft at Three1 with Dissolve(0.2)
    narr "She walked through the left aisle, distributing the test materials while we brought out our snacks and stationery."

    nvl clear
    window hide

    show eliza serioustalk at Three2 with Dissolve(0.2)
    proctor "Please keep your belongings inside your bags. Turn off your cellphones and gadgets, and keep your test permit and school ID in front.{w=1.0} I will inspect the former to check if you're in the correct room."
    proctor "We will start at exactly seven o' clock. Please provide the necessary details in the front part of your answer sheets."
    hide eliza with Dissolve(0.2)

    window show
    nvl clear
    narr "Like what we did during the review sessions, I filled out the form in fifteen minutes.{w=1.0} The proctor was busy going around the room inspecting our permits."
    show eliza serioustalk at Three2 with Dissolve(0.2)
    narr "She reappeared in front, giving out the next instructions and house rules.{w} The conditions are exactly the same as they were presented during the review sessions. That is to be expected from an event modeled after the actual NSUEE."
    show eliza seriousleft at Three2 with Dissolve(0.2)
    narr "At seven, the proctor received the signal and turned to the calendar-like timekeeper on the whiteboard."

    nvl clear
    window hide

    show eliza serious at Three2 with Dissolve(0.2)
    proctor "The first part is Language. You have 60 items to answer in 60 minutes."
    proctor "You are not permitted to proceed to the next section without my instruction.{w=1.0} Instead, you may review your answers or eat, whichever you prefer."
    show eliza smile at Three2 with Dissolve(0.2)
    proctor "Keep the rules in mind and good luck!"
    hide eliza with Dissolve(0.2)

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

    show eliza serious at Three2 with Dissolve(0.2)
    proctor "Okay! You may begin the second section, Mathematics. 60 items to answer in 75 minutes.{w=1.0} Use the scratch papers provided and approach me if you need an extra piece."
    show eliza seriousleft at Three2 with Dissolve(0.2)
    proctor "Take note that you may not return to the previous section. You may only finish shading your answers."
    show eliza serioustalk at Three2 with Dissolve(0.2)
    proctor "Proceed."
    hide eliza with Dissolve(0.2)

    window show
    nvl clear
    narr "I can do Mental Math just fine, but just to be sure, I wrote every question's solution in fine print.{w=1.0} The former, coupled with overconfidence, may be the source of said mistakes."
    narr "What impacted me the most is one of the last Logic questions -- the kind that would initiate a good conversation."

    nvl clear
    narr "It is worded as follows:"
    narr "{i}Diego and Juan are sent to the principal's office due to a scuffle between them. Pedro arrived as a witness. The following are their statements:{/i}"
    narr "{i}Pedro: Diego is not lying.\nDiego: All of us are telling the truth.\nJuan: Any one of us is lying.{/i}"
    narr "{i}Who is telling the truth?{/i}"

    nvl clear
    narr "It took a good five minutes before I arrived at answer.{w=1.0} I contemplated upon this question the most while eating the second sandwich. It was, I decided, the best question of the entire test by far."
    narr "As a disclaimer -- to this day, I still have not confirmed what the answer was. Perhaps others have the same or a different idea as mine?"
    narr "When the time ran out, the proctor did not ask us to continue to the next section. Instead..."

    nvl clear
    window hide

    show eliza smiletalk at Three2 with Dissolve(0.2)
    proctor "Okay, since you've been sitting there for two hours straight, please stand up. We will perform some stretching exercises."
    show eliza smiletalk2 at Three2 with Dissolve(0.2)
    proctor "Stretch your arms forward, palms outward...{w=3.0} Arms upward...{w=3.0} Turn your neck to the left...{w=3.0} To the right...{w=3.0} Circular motion...{w=3.0} Inhale...{w=2.0} Exhale...{w=2.0} Inhale...{w=2.0} Exhale...{w=2.0}"
    show eliza smile at Three2 with Dissolve(0.2)
    proctor "Thank you. Enjoy the rest of the fifteen-minute break.{w=1.0} Those who wish to go to the restroom, you may do so."
    hide eliza with Dissolve(0.2)

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

    show eliza serioustalk at Three2 with Dissolve(0.2)
    proctor "We now move on to the final section, Reading Comprehension. You have 40 items to answer within 45 minutes."
    show eliza serious at Three2 with Dissolve(0.2)
    proctor "Good luck!"
    hide eliza with Dissolve(0.2)

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
    scene bg conferenceroom with fade
    show miyu smile at Three3 with Dissolve(0.2)
    show inoue smilepose at Three1 with Dissolve(0.2)

    window show
    nvl clear
    narr "Our club adviser, Mrs. Aibara, invited Inoue and I to the Student Council conference room.{w=1.0} We discussed my last responsibilities as acting president before returning the power to Inoue."
    narr "It was brief, and all throughout, Inoue was her jolly self."

    nvl clear
    window hide

    t_aib "By the end of this week, Mi-kun, you can resume your duties and let Inoue-chan handle her job.{w=1.0} I bet she still needs to rest a little longer. {i}*giggle*{/i}"
    show miyu smiletalk at Three3 with Dissolve(0.2)
    mh8 "As a matter of fact, ma'am, she can rest until the following week, no more extensions.{w} We have planned to secure her responsibilities until then."
    show inoue happyopen at Three1 with Dissolve(0.2)
    is4 "You've done enough, Miyu. Let me shoulder my one-month absence.{w} Besides, it's time the Math Club has seen its original President in action, eh? {i}*snicker*{/i}"
    t_aib "I'll leave you kids to wrap up any loose threads in our discussion as well as any plans you might have. Goodbye, children."

    "She was a gentle lady, mother-like even. Except at the beginning when she asked about Inoue's condition, she smiled for the entire meeting."
    show miyu smile at Three3 with Dissolve(0.2)
    show inoue schemingclosed at Three1 with Dissolve(0.2)
    "Back to business."

    show inoue schemingopen at Three1 with Dissolve(0.2)
    is4 "So, what are these things I'm hearing about you, hm?"
    show miyu worried at Three3 with Dissolve(0.2)
    mh8 "What do you mean? Did I do anything wrong?"
    show inoue smilepose at Three1 with Dissolve(0.2)
    is4 "Hmmmmm... Not quite wrong, per se. But I heard you've been doing {i}very{/i} naughty things while I was gone.{w=1.0} It feels good to be in the throne, right?"
    show miyu worried blush at Three3 with Dissolve(0.2)
    mh8 "You {i}could{/i} say that, but whatever the heck that means.{w=1.0} Of course, I've been doing --{nw}"
    show inoue schemingclosed at Three1 with Dissolve(0.2)
    is4 "Tsk.{w=0.5} I knew it!{w=1.0} Tsk.{w=0.5} Tsk.{w=0.5} Tsk."
    show miyu nervous blushleft at Three3 with Dissolve(0.2)
    mh8 "Come on...{w=0.5} Let me explain myself!"
    is4 "I can ask Mrs. Aibara to return to my old post now, Mi-kun. I am {i}so{/i} disappointed in you. {i}*snicker* *snicker*{/i}"

    "I don't know whether Inoue is serious or not, but I'm not sure if I should feel guilty or relieved either."

    show miyu embarrassed at Three3 with Dissolve(0.2)
    mh8 "{cps=15}Ku.{w=0.5} Kikikikikiki...{/cps}{w=1.0} Teeheeheeheeheeheeheeheehee..."
    show inoue serious at Three1 with Dissolve(0.2)
    is4 "Why are you laughing?"
    mh8 "Don't you see it? Heeheeheeheeheehee!{w=1.0} I'm happy."
    show inoue talk at Three1 with Dissolve(0.2)
    is4 "Eh?"
    show miyu smiletalk at Three3 with Dissolve(0.2)
    mh8 "Welcome back."

    show miyu smile at Three3 with Dissolve(0.2)
    "Silence."
    show inoue blank at Three1 with Dissolve(0.2)
    "I swept the shoes from her feet and wore them instead.{w} Like a child she was a minute ago, it is now I who was becoming more childish."
    show inoue smile at Three1 with Dissolve(0.5)
    "Slowly, her smile revealed her true nature."

    is4 "{cps=20}Thank you, Mi-kun.{/cps}{w=1.0} I'm glad to be."

    "It was a genuine smile, a great relief to witness after bearing that heavy Cross.{w} She glanced at the office door."

    show inoue dullsurprise at Three1 with Dissolve(0.2)
    is4 "I don't remember the office door being closed this early."
    show miyu bored at Three3 with Dissolve(0.2)
    mh8 "That's probably because Sayo didn't come in today."
    show inoue talk at Three1 with Dissolve(0.2)
    is4 "It's Monday. Doesn't she have paperworks to do?"

    "She looked around the room.{w} Her eyes stopped at the stack of papers on the drawer near the whiteboard."

    show inoue worried at Three1 with Dissolve(0.2)
    is4 "Are those our official documents? Shouldn't they be inside the office drawer?"
    show miyu pissedclosed at Three3 with Dissolve(0.2)
    mh8 "For quick reference. I must have forgotten to put them away.{w=1.0} The month has been hectic, you know?"
    show inoue talk at Three1 with Dissolve(0.2)
    is4 "I understand.{w} In that case, let me put these away and --{w=1.5}{nw}"
    show miyu pissed at Three2 with Dissolve(0.2)
    mh8 "I'll do it."
    show inoue surprised at Three1
    hide miyu with Dissolve(0.2)

    "I zipped past her, scooped up the documents, and disappeared into the office. These were all done in under a minute.{w=1.0} She watched inquisitively."

    show inoue talk at Three2 with Dissolve(0.2)
    show miyu worried at Three3 with Dissolve(0.2)
    is4 "You work faster than usual --{w=0.5} {cps=20}too fast, if I may note.{/cps}{w=1.0} What's the deal?"
    show miyu surprised at Three3 with Dissolve(0.2)
    mh8 "Ahehehehehehehe...{w=0.5} {cps=15}You see, I'm inspired.{/cps}"
    show inoue surprised at Three2 with Dissolve(0.2)
    is4 "Ah! I forgot!{w=1.0}{nw}"
    show inoue smile at Three2 with Dissolve(0.2)
    is4 "Ah! I forgot!{fast} Belated happy birthday!"
    show miyu embarrassed at Three3 with Dissolve(0.2)
    mh8 "Thank you! {i}*chuckle*{/i}"
    show miyu smile at Three3 with Dissolve(0.2)
    mh8 "{cps=20}If we have nothing further to discuss, then I should take my leave.{/cps}"
    show inoue happyclosed at Three2 with Dissolve(0.2)
    is4 "Go ahead. I'll stay here for a little longer."
    show miyu smiletalk at Three1 with Dissolve(0.2)
    mh8 "Okay. Remember to turn the lights off and close the door when you leave. You wouldn't want Mrs. Genkai to be mad at us."
    show inoue happyopen at Three2 with Dissolve(0.2)
    is4 "I {i}know{/i}. Run along and enjoy the rest of the day, Mi-kun!"
    hide miyu with Dissolve(0.2)
    show inoue dullsurprise at Three2 with Dissolve(0.5)
    show inoue seriousleft at Three2 with Dissolve(0.5)
    hide inoue with Dissolve(0.2)

    scene bg msci with dissolve
    "I wore my backpack and left the room."
    show miyu focusedpose at Three2 with Dissolve(0.2)
    "Instead of leaving the campus and travelling to Sanae's house, I stayed and sat on the front desk bench.{w} My head feels light, heart racing, my mind in anticipation of the worst outcome."
    "{cps=25}Inoue is going to find out.{/cps}{w=1.0} {cps=20}She is not supposed to...{w=0.5} She is not supposed to...{/cps}{w=1.0}{nw}"

    show ikuko talk at Three3 with Dissolve(0.2)
    ikuko "You alright, Miyu?"

    show miyu talk at Three2 with Dissolve(0.2)
    "That's right!{w=0.5} Ikuko knows what happened in that room."

    show miyu worried at Three2 with Dissolve(0.2)
    mh8 "Ikuko, she's still inside. I don't know far her curiosity will take her, but please, you must stall her."
    show ikuko worried at Three3 with Dissolve(0.2)
    ikuko "Did you slip up?!"
    show miyu serious at Three2 with Dissolve(0.2)
    mh8 "Yes...{w=0.5} No.{w=0.5} I lied to buy some time. She might have picked up, but I'm not sure. She'll understand you more than me.{w=1.0} {i}*sigh*{/i} If she sees what's inside that office..."
    show ikuko blank at Three3 with Dissolve(0.2)
    ikuko "Alright. I'll go there now. Just stay calm.{w=0.5} If anything happens, get in touch with Sayo."
    show miyu worried at Three2 with Dissolve(0.2)
    mh8 "{cps=15}Look normal.{/cps}"
    hide ikuko with Dissolve(0.2)

    "She paid no more attention as she dashed to the Council Room."
    "My mind was conflicted.{w=1.0} Should I go ahead and visit Sanae, or do I stay and watch what happens next?"
    "That reminds me!{w} I forgot to visit Ms. Natsumoto earlier. The guidance counselor's room is adjacent to the Council room. Should anything untoward happen, I will be able to hear it."
    hide miyu with Dissolve(0.2)

    scene bg guidancecounselor office with dissolve
    "{i}*knock* *knock* *knock*{/i}"

    t_nat "Come in!"

    "I greeted Ms. Natsumoto with a smile, although it cracked almost instantly.{w} She sensed my body shaking and urged me to have a seat."

    t_nat "Is there anything you need, son?"

    show miyu pissedclosed at Three1 with Dissolve(0.2)
    "I nodded, allowing my body to sink into a chair in front of her desk. I closed my eyes and stopped my teeth from clattering."

    show miyu pissedclosedpose at Three1 with Dissolve(0.2)
    mh8 "{i}*EXHALE*{/i}{w=1.5} I think I messed up."
    t_nat "Please elaborate."
    show miyu pissedleftpose at Three1 with Dissolve(0.2)
    mh8 "It's Inoue.{w=0.5} She's still not stable even after undergoing intense therapy for a few weeks, right?"
    t_nat "I wouldn't call her {i}unstable{/i} but the trauma is still fresh in her mind.{w=1.0} If she comes across anything that would trigger those unpleasant memories, she would suffer a nervous breakdown."
    t_nat "You met her today?"
    mh8 "Earlier. We were having a club-related discussion in the Council room.{w=0.5} And she's still there as we speak."

    "I have said nothing more, yet her eyes turned wary. She caught on to the implications and wore an authoritative expression."

    t_nat "{cps=20}Mi-kun...{w=0.5} Did you tip her off about the {i}restricted area{/i}?{/cps}"
    show miyu pissedpose at Three1 with Dissolve(0.2)
    mh8 "I didn't mean to. I haven't said anything.{w=1.0} Inoue's a bright girl; she'll catch on eventually.{w} The thought unsettles me. There's no telling what happens in the next few moments."

    show miyu worried at Three1 with Dissolve(0.2)
    "Ms. Natsumoto tapped my hand and pointed at the window.{w=0.5} Ikuko was standing there, a quick gesture to her neck before scurrying away."
    "Whatever it meant, it was foreboding to {i}the inevitable moment{/i}."
    show miyu pissed at Three1 with Dissolve(0.5)
    show miyu pissedclosed at Three1 with Dissolve(0.5)
    "Damn."

    show miyu proudclosed at Three1 with Dissolve(0.2)
    mh8 "{cps=15}Well, ma'am...{/cps}{w=2.0} Boom!{w=1.0}{nw}"
    hide miyu

    scene bg blood2 with vpunch
    play sound sfx_girlscream
    is4 "AAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHH!!!"

    "That was the prompt! I excused myself and rushed to the Council room."
    scene bg conferenceroom dark with dissolve
    show inoue creepy worriedtalkleft at Eight7 with Dissolve(0.2)
    show miyu worried at Three1 with Dissolve(0.2)
    "The door to the offices was open.{w} Inoue,{w=0.5} cowering on the floor in front of the file cabinet, wrapped her hands around her neck,{w=0.5} choking,{w=0.5} averting her eyes from the scene."

    r_is4 "{i}*SOB*{/i}{w=0.5} {cps=15}This can't be...{w=0.5} Even here...?{/cps}{w=0.5} {i}*SOB*{/i}"
    show miyu talk at Three2 with Dissolve(0.2)
    f_mh8 "{cps=10}Inoue...{/cps}{w=0.5}{nw}"
    show inoue creepy angryscream at Eight6 with hpunch
    r_is4 "Don't touch me!"
    hide inoue
    hide miyu with vpunch
    
    "{b}*THUD*{/b}"

    show inoue creepy angry at Three2 with Dissolve(1.0)
    c_mh8 "Calm down. It's me!"
    show inoue creepy angrytalk at Three2 with Dissolve(0.2)
    r_is4 "{cps=10}Haa...{w=0.5} Haa...{w=0.5} Haa...{w=0.5} Haa...{/cps}"
    r_is4 "{cps=25}Mi-kun...{w=1.0} What the hell is this?!{w=0.5} Why is there a corpse in one of the workstations?{/cps}"
    c_mh8 "Inoue..."
    show inoue creepy angryscream at Three2 with hpunch
    r_is4 "You didn't tell me! You were hiding this from me,{w=0.5} you and Ikuko!{w=1.0} He followed us here, huh?{w=0.5} When?{w=1.0} When?!"
    c_mh8 "{b}GULK!{/b}"
    show inoue creepy angryscream at Three2 with hpunch
    r_is4 "Answer me!"
    c_mh8 "{cps=15}I can't breathe. Let go...{/cps}"
    hide inoue

    scene bg conferenceroom with hpunch
    show inoue noglass pissed at Three2 with Dissolve(0.5)
    "I forced myself out of her grip.{w=1.0} Inoue, while still outraged from her discovery, sat on the wall and composed herself."

    f_mh8 "{b}*COUGH*{w=0.5} *COUGH*{w=0.5}{/b} That's right. L.C. terrorized us here while you were away. Some of us even thought they were going after you next."
    show inoue noglass serious at Three2 with Dissolve(0.2)
    c_is4 "If not me, then who? Who did he take?"
    show inoue noglass sad at Three2 with Dissolve(0.2)
    f_mh8 "..."
    show inoue noglass worried at Three2 with Dissolve(0.2)
    c_is4 "{cps=20}Don't tell me it's...{/cps}{w=2.0}{nw}"
    f_mh8 "Yes, Inoue.{w=1.0} {cps=20}Hiroshi is dead.{/cps}"
    show inoue noglass cry at Three2 with Dissolve(0.2)
    c_is4 "{cps=10}But...{/cps}{w=0.5}{nw}"

    show inoue noglass sadcry at Three3 with vpunch
    "{b}*THUD*{/b}"

    show inoue noglass sadcry2 at Three3 with Dissolve(0.2)
    c_is4 "It's all my fault. I should have stopped my brother from handing it to him."
    show inoue noglass smilecry at Three3 with Dissolve(0.2)
    d_is4 "That's it. It must be the reason why he went after Hiroshi.{w=1.0} I'm useless. I'm a fool...{w=1.0} No. {i}He{/i} is the fool. The Devil chose him."
    show inoue noglass laughcry at Three3 with Dissolve(0.2)
    r_is4 "{cps=15}May the Devil take the fool.{/cps}{w=1.0} Heh...{w=0.5} Hehehehehehehehehehe..."

    window show
    nvl clear
    narr "I could not bear seeing her like that any longer."

    scene black with fade
    narr "Ms. Natsumoto checked on us after hearing the noises from her office.{w} I left Inoue in her care after explaining the situation. She understood."
    narr "Don't do anything rash, Inoue. Don't make the same mistake he did."

    nvl clear
    window hide

    scene bg collegeoflaw classroom
    show eliza serioustalk at Three2 with Dissolve(0.2)
    proctor "Five minutes left."
    hide eliza with Dissolve(0.2)

    window show
    nvl clear
    narr "And I was on the last passage with five questions remaining."
    narr "The intensity at which your heart races, the vigor of blood pumping up to your head, the excitement that causes the eyes to move up and down...{w=0.5} The enemy is always time."
    narr "It is a double-edged sword, jogging the memory to remember better or worse. With high stakes on the line, it is everything or nothing."

    nvl clear
    window hide

    show eliza serious at Three2 with Dissolve(0.2)
    proctor "Time's up!"
    show eliza seriousleft at Three2 with Dissolve(0.2)
    proctor "Please finish shading your answers. After one minute, I will collect your test materials so you may leave."

    show eliza serious at Three3 with Dissolve(0.2)
    "We complied and closed our booklets after a minute passed."
    show eliza serious at Three2 with Dissolve(1.0)
    show eliza seriousleft at Three1 with Dissolve(1.0)
    "The proctor went over to our seats and collected the materials. She also scanned our IDs."

    show eliza smiletalk at Three1 with Dissolve(0.2)
    proctor "Say, hi, to the teachers for me. I'm also from MSCI."
    show eliza smileleft at Three1 with Dissolve(0.2)
    mh8 "Eh? Oh, okay."
    hide eliza with Dissolve(0.2)

    "Wow! I never expected an alumna would be my proctor.{w=1.0} At the latest, she would be from Batch '04, if her youthful appearance is anything to go by."
    "Nevertheless, she went on with her duty.{w=1.0} We waited for her to finish collecting papers before leaving."
    "The clock read 11:45; the sky was white.{w=0.5} A relief."

    scene bg intersection with dissolve
    "I walked back to the College of Engineering jeepney stop and pondered upon a few things."

    scene bg blood with fade
    "First, we cannot hide Hiroshi's demise any longer -- two weeks have passed since that dreadful evening.{w} Tomorrow, we meet with Inoue and get her side of the story. She has already agreed and we would share the details of the heinous crime in exchange."
    
    scene bg conferenceroom dark with fade
    show sayo smileclosedpose at Three2 with Dissolve(0.5) 
    "Second, why Sayo?{w} It takes one meticulous pair of eyes to disprove {i}that{/i} notion. Why would she take the mantle of a near-omnipotent criminal mastermind only to indict herself early on? It does not add up."
    show sayo creepy smirkpose at Three2 with Dissolve(1.0)
    "The next step is rather obvious, is it not?"
    hide sayo with Dissolve(0.2)
    call opening

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
    scene bg classroom1 with fade
    show miyu focusedpose at Three2 with Dissolve(0.2)

    window show
    nvl clear
    narr "With over half an hour remaining, some students have done away with their meal and are doing their usual business."
    narr "Among them is Miyu. Oftentimes, he would glance at his watch, and mumble to himself, \"Is she done yet?\""
    narr "Beyond the window, he spotted Inoue sitting underneath a large tree.{w=1.0} She was accompanied by Hikaru and Yoshiro, the three having a conversation."
    show miyu bored at Three1 with Dissolve(0.2)
    narr "Just as he stepped out of the door, a hand tapped him from behind."

    nvl clear
    window hide

    show sumiko seriousleft at Three2 with Dissolve(0.2)
    st3 "Let's go.{w=1.0} I don't want to miss what she has to say either."
    show miyu naughty talk at Three1 with Dissolve(0.2)
    mh8 "Alright.{w} But I wonder if Sayo is on her way?"
    show sumiko serioustalk at Three2 with Dissolve(0.2)
    st3 "She'll come from either IV-E or the Student Council office. Paperworks or personal routine, I'd wager."
    show miyu bored at Three1 with Dissolve(0.2)
    mh8 "Which makes me wish she takes long.{w} We need to get as much information as we can before the situation turns dire. Inoue's bound to explode once she sees her."
    show sumiko seriousleft at Three2 with Dissolve(0.2)
    st3 "I agree."
    hide miyu with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)

    scene bg school outside with dissolve
    show hikaru smile at Eight1 with Dissolve(0.2)
    show inoue blank at Eight2 with Dissolve(0.2)
    show yoshiro surprised2 at Eight3 with Dissolve(0.2)
    show miyu smile at Eight5 with Dissolve(0.2)
    show sumiko surprised2 at Eight6 with Dissolve(0.2)
    "The two boys approached the tree.{w} Hikaru waved at them, catching Inoue and Yoshiro's attention."
    show akira smileleft at Eight8 with Dissolve(0.2)
    "The two boys approached the tree.{w} Hikaru waved at them, catching Inoue and Yoshiro's attention.{fast} Akira, coming from the canteen's direction, trailed closed behind. He disposed his mango shake on the way."
    hide akira with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    hide inoue with Dissolve(0.2)

    show hikaru smirk at Three1 with Dissolve(0.2)
    show yoshiro smile at Three3 with Dissolve(0.2)
    hy10 "Aren't we IV-C folks so diligent? Five plus Inoue."
    show yoshiro smirkclosed at Three3 with Dissolve(0.2)
    ys6 "It's IV-C!{w=1.0} Carry over our catchphrase from Junior Year while our reputation is clean."
    "\"Hahahahahahahahahaha...\""
    hide yoshiro with Dissolve(0.2)
    show akira proud2 at Three3 with Dissolve(0.2)
    ai2 "So, what did we miss?"
    show hikaru smile at Three1 with Dissolve(0.2)
    hy10 "Nothing official yet. Just the usual friendly banter. Mama said it was the best course of action."
    show inoue surprised at Three2 with Dissolve(0.2)
    is4 "I haven't seen you all, save for Miyu, in a while.{w=1.0} Oh! How could I forget? I was present for the exams as well."
    hide akira with Dissolve(0.2)
    show miyu proudclosed at Three3 with Dissolve(0.2)
    show inoue smile at Three2 with Dissolve(0.2)
    mh8 "Don't bother. {i}*chuckle*{/i}{w=1.0} I trust you've been better since our previous conversation?"
    show inoue smile at Three2 with Dissolve(0.2)
    is4 "Definitely! I'm fit enough to resume my normal activities. Wouldn't want to step over the agreement and extend my vacation, yes? {i}*snicker*{/i}"
    show inoue sighclosed at Three2 with Dissolve(0.2)
    is4 "And I'm sorry for the commotion last week."
    show hikaru serious at Three1 with Dissolve(0.2)
    show miyu pissed at Three3 with Dissolve(0.2)
    mh8 "Don't beat yourself up. {i}I{/i} should be the one apologizing. Should've known better than to lie."

    "Silence.{w} The four others stared at Miyu, their thoughts a common question."

    show hikaru serioustalkleft at Three1 with Dissolve(0.2)
    hy10 "You mean...?"
    mh8 "Yes..."

    hide hikaru with Dissolve(0.2)
    hide inoue with Dissolve(0.2)
    show ichirou focus at Eight1 with Dissolve(0.2)
    "At this moment, Ichirou joined them.{w} Miyu greeted him coldly, then scouted for eavesdroppers."

    show ichirou focus at Three1 with Dissolve(0.2)
    show inoue sighclosed at Three2 with Dissolve(0.2)
    show miyu pissedleftpose at Three3 with Dissolve(0.2)
    mh8 "She discovered the crime scene. Inoue didn't exactly act friendly when I returned to the Council room. I'll let you fill in the details."
    show inoue sigh at Three2 with Dissolve(0.2)
    is4 "{b}{i}*groan*{/i}{/b}"
    show ichirou serious at Three1 with Dissolve(0.2)
    iy1 "We've crossed the boundary, it seems. Shouldn't we move on to what we {i}all{/i} came for?"
    hide miyu with Dissolve(0.2)
    show yoshiro serious2 at Three3 with Dissolve(0.2)
    ys6 "Then let's not waste any more time."
    hide yoshiro with Dissolve(0.2)
    hide ichirou with Dissolve(0.2)
    show inoue noglass sad at Three2 with Dissolve(0.2)

    "Hikaru and Ichirou sat beside Inoue. The four others either sat under the tree or stood with their back on a pole."
    "All eyes on Inoue."

    show yoshiro talkleft at Eight7 with Dissolve(0.2)
    ys6 "Let's assume you cannot remember the moment you were abducted by L.C. or whoever. Can you at least describe the events surrounding your captivity?"
    show inoue noglass sadleft at Three2 with Dissolve(0.2)
    is4 "It's a haze. Nothing is concrete that anything I describe might come off as nonsense."
    show ichirou confused at Three3 with Dissolve(0.2)
    iy1 "Just give us anything. We'll work out the details later."
    hide yoshiro with Dissolve(0.2)
    show ichirou serious at Three3 with Dissolve(0.2)
    show miyu pissedclosedpose at Three1 with Dissolve(0.2)

    menu:
        "But which first question is more appropriate?"
        "What state were you in when you've woken up?":
            show miyu pissedpose at Three1 with Dissolve(0.2)
            mh8 "What state were you in when you've first woken up?"
            hide inoue
            hide ichirou
            hide miyu

            scene white with dissolve
            scene bg emptycell with dissolve
            is4 "It felt as if my head was compressed for weeks. I believe time has passed that long.{w=1.0} When I came to, my feet were chained to a bedpost, restricting my movements."
            st3 "A bed? Was it a prison-like type of bed?"
            is4 "A bit more comfortable if the absence of back pain is any indication."

            scene bg envelopefour with dissolve
            is4 "I found a sealed envelope under the pillow.{w} Inside was a CD with the chain lock's key. I used the former on the CD player sitting atop the bedside cabinet."
            mh8 "This L.C. is an old soul, aren't they?"

            $ path_b1 += 1
            $ bonus_b1_i += 1

        "Can you describe the place where you've woken up?":
            show ichirou serious at Three3 with Dissolve(0.2)
            iy1 "Can you describe the place where you've woken up?"
            hide inoue
            hide miyu
            hide ichirou

            scene white with dissolve
            scene bg emptycell2 with dissolve
            is4 "It was like an abandoned prison cell -- no, a dungeon cell is more accurate. The room was mostly empty, save for a bed, a cabinet, and a CD player."
            is4 "The only opening was a metal door a diagonal away from the bed. It was protected by an electronic lock."
            ys6 "What about this electronic lock? Is it the regular keypad or card reader?"
            is4 "Something else. It was a 36-key piano. Odd choice, but it felt more personalized."

            scene bg envelopefour with dissolve
            is4 "My feet were chained to one of the bedposts. The only relevant item I found was an envelope containing a CD and the chain lock's key."
            is4 "I still remember the tune that helped me escape.{w=1.0} It was {i}Au Clair De La Lune.{/i}{w=1.0} I'm not sure if L.C. had made the connection, but I also play the piano."

            $ path_b1 -= 1
            $ bonus_b1_g += 1

    scene bg school outside with fade
    show inoue noglass worried at Three2 with Dissolve(0.2)
    is4 "I inserted the CD and let it play while I examined the surroundings. A little after, I lay on the bed, thinking about how I came to be there."
    is4 "It was a voice recording. L.C. is an affable individual, I must admit.{w=1.0} Monstrous, regardless, because of what he had done to me -- and Kirisaki later on."
    show akira worriedleft at Three3 with Dissolve(0.2)
    ai2 "Frightening, too! When they first talked to us through the intercom during the mock exams, they were acting all gentlemanly and such. Things got weirder the longer they talked."
    show inoue noglass serious at Three2 with Dissolve(0.2)
    is4 "Yes. He seems to know me well.{w=1.0} After he was done talking, a lullaby looped infinitely. Glad I recognized it else I wouldn't be able to leave the cell."
    hide akira
    hide inoue

    scene bg darkhallway with fade
    is4 "When the door opened, the void greeted me.{w=1.0} Voices spoke from within the darkness."

    menu:
        "The first moments of consciousness are sufficiently explained. Now, it is time to ask about the disembodied voice... or voices."
        "Hold on. \"He?\"":
            scene bg school outside with fade
            show inoue noglass sadleft at Three2 with Dissolve(0.2)
            show sumiko surprisedtalk at Three1 with Dissolve(0.2)
            st3 "Hang on. There seems to be a disparity in pronouns, Inoue."
            show inoue noglass serious2 at Three2 with Dissolve(0.2)
            is4 "I don't understand."
            show sumiko seriousleft at Three1 with Dissolve(0.2)
            st3 "Whenever L.C. is mentioned, you refer to {i}him{/i} as male. However, we refer to L.C. neutrally, {i}they{/i}."
            show akira surprised2 at Three3 with Dissolve(0.2)
            ai2 "Is it because I said \"gentlemanly?\" Let me clarify. I'm not sure about the gender, either."
            show inoue noglass sadleft at Three2 with Dissolve(0.2)
            is4 "It only applies to the CD recording, however. So, even the gender is unclear at that point.{w=1.0} Past that, let's return to the other voices I heard."
            hide sumiko with Dissolve(0.1)
            hide akira with Dissolve(0.1)
            show inoue noglass worried at Three2 with Dissolve(0.2)
            is4 "{cps=30}It's as if he was all over me.{w=1.0} No. She was at someplace I couldn't see.{w=1.0}{/cps} {cps=25}Their whispers and jeers in my head felt like their mouths touched my ears as if...{/cps}{w=3.0}{nw}"
            is4 "{cps=20}...as if they were in a dimension separate from mine.{/cps}"
            show hikaru worried at Three1 with Dissolve(0.2)
            hy10 "Did you check your ears for any receiver-like device, though?"
            show inoue noglass sad at Three2 with Dissolve(0.2)
            is4 "Hikaru, I found nothing odd around my body. There was nothing on me except my glasses."
            hide hikaru with Dissolve(0.2)

            $ path_b1 += 1
            $ bonus_b1_i += 2

        "Whose voices?":
            ys6 "Whose voices?"
            is4 "They were threatening me.{w=1.0} It's one of those instances you could say it was all in my head. It felt like it {i}really{/i} was the case."
            ys6 "Did it belong to a male or a female?"
            is4 "I'm not sure. Sometimes, it would be the same voice as in the CD recording. Other times, it would warp to a female. It was witch-like, the second one!"

            scene bg school outside with fade
            show inoue noglass sadleft at Three2 with Dissolve(0.2)
            show miyu focusedpose at Three1 with Dissolve(0.2)
            mh8 "{cps=15}Witch-like...{/cps}{w=1.0} Did we not experience something of the sort when L.C. revealed their voice to us?"
            show ichirou worried at Three3 with Dissolve(0.2)
            iy1 "I remember it distinctly. L.C. sounded like a male as Inoue described in her story.{w=1.0} What about those child hellspawns we heard singing that evil rhyme?"
            show inoue noglass pissed at Three2 with Dissolve(0.2)
            is4 "Child hellspawns?{w=1.0} You mean..."
            hide ichirou with Dissolve(0.2)
            show akira surprised at Three3 with Dissolve(0.2)
            ai2 "Two children -- a male and a female.{w=1.0} One of them had a tic that went {i}swing, swing, swing.{/i} The other always had this word on one end of his sentences: {i}puku!{/i}"
            show inoue noglass worried at Three2 with Dissolve(0.2)
            show akira surprised2 at Three3
            show miyu talk at Three1
            is4 "{b}*GASP*{/b}{w=2.0}{nw}"
            hide inoue
            hide miyu
            hide akira

            scene red with dissolve
            scene bg pool nightmare with dissolve
            is4 "The pool!"
            is4 "{i}{cps=15}Oh... you made her cry...{w=0.5} you bad, bad.{w=0.5} You gonna get slapped in the butt-butt.{w=1.0}{/cps} {cps=10}Swing...{w=0.5} Swing...{w=0.5} Swing...{/cps}{/i}{w=2.0}{nw}"
            hy10 "Inoue-chan? Are you alright?{w=2.0}{nw}"
            is4 "{i}You started it, puku!{/i}{w=2.0}{nw}"

            scene bg underwater nightmare with dissolve
            is4 "And it went straight to Hell from there.{w=1.0} I almost died when I was thrown headfirst into that potpourri of viscera."

            scene bg school outside with fade
            show inoue noglass pissed at Three2 with Dissolve(0.2)
            is4 "Never mind about it. I skipped too far ahead."

            $ path_b1 -= 1
            $ bonus_b1_g += 2

    show yoshiro worried at Three3 with Dissolve(0.2)
    ys6 "And then?"
    hide yoshiro
    hide inoue

    scene bg darkhallway with fade
    is4 "At this point, I started questioning my sanity --{w=0.5} my own reality."
    is4 "There were two doors. The one across I figured would take me forward.{w=1.0} Yet, something stopped me."
    is4 "From beyond the door was another voice.{w=1.0} Unlike the disembodied voices earlier, this one had a corporeal origin. It was angry! It talked to me as if I was a malevolent spirit."
    is4 "And minutes later, I heard...{w=2.0}{nw}"
    unk "{i}Hah...{w=1.0} Hah...{w=1.0} Hahahaha...{w=1.0} Gyahahahahahahahahaha...{/i}{w=1.5}{nw}"

    scene bg blood
    "{b}*SNAP*{/b}"

    unk "{i}AAAAAAAAAAAAAAAAAAAAHHHHHH!!!{/i}"

    scene bg blood2
    is4 "I thought I died!{w=1.0} My waist felt like the door split it cleanly into two.{w=1.0} {cps=20}Until I saw...{w=0.5} I was fine...{w=0.5} Hehehehe... I don't know.{/cps}"
    iy1 "This is concerning. It is likely your mind has been playing tricks on you.{w=1.0} But to ask how and why wouldn't lead to anything at all!"

    scene bg underwater with fade
    is4 "It wasn't the only time either.{w=1.0} I was blown into a decontamination pool sometime later. With how weak my body became, I thought I would drown."

    scene bg underwater nightmare with dissolve
    is4 "Perhaps I was lucky to have survived. Maybe I didn't survive and you're all part of my imagination.{w=1.0} I don't know.{w=1.0}"
    is4 "I saw Kirisaki after that, but he was already a corpse when I came across him. He was in the room where I almost got split into half!"

    scene bg school outside
    show inoue noglass sadleft at Three2 with Dissolve(0.2)
    show miyu worried at Three1 with Dissolve(0.2)
    mh8 "Alright, alright. Slow down, please. There's too many weird details to scrutinize.{w=1.0} At the very least, can we clear up the situation with Kyou?"
    show hikaru angry at Eight1 with Dissolve(0.2)
    hy10 "Maybe he's a {i}walking corpse{/i} when you saw him?"
    show miyu naughty smirk at Three1 with Dissolve(0.2)
    mh8 "A zombie?! No way! {i}*chuckle*{/i} Too macabre for L.C.'s own caliber. A spirit is more reasonable."
    show hikaru serious at Eight1 with Dissolve(0.2)
    show inoue noglass serious2 at Three2 with Dissolve(0.2)
    is4 "I swear upon it. He was flesh and blood when I encountered him. No way I imagined that."
    hide miyu with Dissolve(0.2)
    show hikaru serious at Three1 with Dissolve(0.2)

    menu:
        "It is established that Kyou Kirisaki met his demise by immolation, yet the latest testimony casts doubt onto that. How to respond?"
        "You saw Kirisaki dead? How?":
            show hikaru angry at Three1 with Dissolve(0.2)
            hy10 "Okay. You said you saw Kirisaki {i}alive{/i} later on. However, you also mentioned that you saw him {i}dead{/i}. I mean...{w=0.5} how?!"
            show inoue noglass serious at Three2 with Dissolve(0.2)
            is4 "I checked his body -- his uniform, face, hands, everything.{w=1.0} Just like me, he had nothing on him. One of his fingers was black, swollen from being pricked by one of the bonsais in the room."
            show hikaru seriousleft at Three1 with Dissolve(0.2)
            hy10 "We own a bonsai. No matter how many times we get pricked, it wouldn't be that bad."
            show yoshiro surprised2 at Three3 with Dissolve(0.2)
            ys6 "And one of his fingers was black. How does a poisoned bonsai achieve something like that? Are you sure he wasn't burned?"
            is4 "No. The room would have smelled of burnt meat."
            hide inoue
            hide hikaru
            hide yoshiro

            scene bg cowpainting with fade
            is4 "Moments later, I felt something pulling me towards the large painting on one side of the room. I heard the voice again,{w=1.0} and with it, another sharp pain in my temples."

            scene black with fade
            is4 "Everything went black and the smell resembled that of a rotting corpse.{w=1.0}{nw}"

            scene bg darkhallway3 nightmare with fade
            is4 "Everything went black and the smell resembled that of a rotting corpse.{fast} When I came to, the surroundings changed -- a haunted, enclosed space much darker than before, and the air felt heavier."
            hy10 "Like how it was from... what's the name?"
            mh8 "I got the reference, Hikaru.{w=1.0} What else changed, Inoue?"

            scene bg meadow with dissolve
            is4 "The painting transformed from a meadow{w=1.0}{nw}"

            scene bg cowpainting with dissolve
            is4 "The painting transformed from a meadow{fast} to a cow,{w=1.0}{nw}"

            scene bg minotaur with dissolve
            is4 "The painting transformed from a meadow to a cow,{fast} and finally, a hulking monster --{w=1.0} the minotaur!"

            scene bg school outside with fade
            show inoue noglass sadleft at Three2 with Dissolve(0.2)
            show miyu pissedclosedpose at Three1 with Dissolve(0.2)
            mh8 "Okay?"
            show inoue noglass worried at Three2 with Dissolve(0.2)
            is4 "I dashed out of the room, but it gave chase! I don't want to relive the pain I suffered during that time.{w=1.0} I felt degraded to a worm."
            hide miyu with Dissolve(0.2)

            $ path_b1 += 1
            $ bonus_b1_i += 4

        "Maybe the corpse is a dummy?":
            show akira annoyed at Three3 with Dissolve(0.2)
            ai2 "Can we all agree Kirisaki's \"corpse\" was just a dummy to scare Inoue?"
            show inoue noglass angry at Three2 with Dissolve(0.2)
            is4 "It was organic! I checked the body myself.{w=1.0} Made it all the more puzzling to see him alive in the chemistry lab."
            show akira surprised2 at Three3 with Dissolve(0.2)
            ai2 "A chemistry lab? What happened there?"
            hide inoue
            hide akira
            hide hikaru

            scene bg darkhallway3 nightmare with fade
            is4 "Kirisaki wasn't himself. When I tried to approach him, he ran away as if he saw {i}something{/i}. No amount of pleading stopped him. He was shouting curses!"
            st3 "Is that a fact?"
            ys6 "We {i}are{/i} talking about the same Kirisaki, right? Kyou Kirisaki?"
            is4 "Somehow, I felt hurt, never realizing how out of character he was. {i}*sigh*{/i}"
            is4 "Everything went back to normal once he let me in.{w=1.0} We checked up on each other and discussed a way out of that place."

            scene bg chemistrylab with fade
            is4 "However, the air changed just as we were leaving. Nearly an inch from my face is the tip of an axe.{w=1.0} He,{w=0.5} or {i}it{/i} was planning to kill me!"
            ai2 "Are you sure?"
            is4 "I could sense the bloodlust in his eyes.{w=1.0} There is no mistaking it.{w=1.0} He wasn't himself at all. Believe me!"
            ai2 "It couldn't have been him -- hard to believe if it was. Maybe the Kirisaki you encountered after the corpse was an impostor?"
            is4 "Whatever the case, he lunged at me, aiming at my heart. I pushed him to the shelves, causing various chemicals to spill on his face.{w=1.0} He snapped out of it. It was peculiar..."
            st3 "Was there any acid among the spilled chemicals?"
            is4 "Presumably. The most significant one we found, though neither spilled nor acidic, was liquid chlorine encased in a small ampoule."

            scene bg school outside with fade
            show inoue noglass sadleft at Three2 with Dissolve(0.2)
            show sumiko serioustalk at Three1 with Dissolve(0.2)
            st3 "So, you recognize nothing from the spilled chemicals?"
            show inoue noglass pissed at Three2 with Dissolve(0.2)
            is4 "I don't have the time to check. If there was, then it's such a shame. But it doesn't matter, anyway!"

            $ path_b1 -= 1
            $ bonus_b1_g += 4

    show sumiko sighclosed at Three1 with Dissolve(0.2)
    st3 "Unfortunately, this is where the story muddles. Agreed?"
    show miyu proudclosed at Eight1 with Dissolve(0.2)
    mh8 "We can salvage a few points from her story and examine those particular details. Otherwise, it is as you said."
    show ichirou serioustalkleft at Three3 with Dissolve(0.2)
    iy1 "I think what you told us is enough. What I'm interested in is this facility's location. Were you able to glimpse on the surroundings when you escaped?"
    show yoshiro talkleft at Eight8 with Dissolve(0.2)
    ys6 "It should be somewhere close by.{w=1.0} You have to note, though, that no suspicious vehicles passed through the gate early morning of the 17th."
    show yoshiro serious at Eight8 with Dissolve(0.2)
    ys6 "Considering what activity we were busy with around that timeframe, the suspect has used that to their advantage."
    show ichirou serious at Three3 with Dissolve(0.2)
    show miyu naughty smirk at Eight1 with Dissolve(0.2)
    mh8 "Did someone bother to bring a body bag-sized garbage bag? {i}*chuckle*{/i}"
    show yoshiro serious2 at Eight8 with Dissolve(0.2)
    ys6 "Then tie it up when the victims are inside. It's too suspect, but there is no other way."
    show miyu bored at Eight1 with Dissolve(0.2)
    mh8 "...Unless Inoue can shed some light onto this."
    show inoue noglass serious2 at Three2 with Dissolve(0.2)
    is4 "I can do no better."
    hide inoue
    hide miyu
    hide sumiko
    hide yoshiro
    hide ichirou

    scene black
    unk "She doesn't have to.{w=1.0} We have asked the same question repeatedly with no positive end."
    is4 "{b}*GASP*{/b}"

    scene bg school outside
    "The party turned towards the direction of the voice."
    show sayo seriousnormal at Three2 with Dissolve(0.5)
    "The party turned towards the direction of the voice.{fast} It belonged to a petite figure, her hands held behind her."

    hy10 "Whoa! Where did you come from?"
    show sayo serioustalkleft at Three2 with Dissolve(0.2)
    sr5 "It matters not. What matters now is the lone survivor of L.C.'s crimes.{w=1.0} I figured I should hear the outcome of this conversation."
    mh8 "We're near the end."
    show sayo seriousclosed at Three2 with Dissolve(0.2)
    sr5 "Make use of the remaining time, please."
    hide sayo with Dissolve(0.2)

    "She sat on the side closest to Miyu's group, away from the auditorium."

    show inoue seriousleft at Three2 with Dissolve(0.2)
    show ichirou confused at Three3 with Dissolve(0.2)
    iy1 "Now, do you remember?"
    show inoue serioustalk at Three2 with Dissolve(0.2)
    is4 "Negative."
    show ichirou serioustalkleft at Three3 with Dissolve(0.2)
    iy1 "Let's focus on the living room.{w=1.0} You heard Kirisaki being brutally murdered inside that room. When you left that room, you said you were attacked."
    show inoue serious at Three2 with Dissolve(0.2)
    is4 "By the minotaur."
    show ichirou serioustalk at Three3 with Dissolve(0.2)
    iy1 "I'm not interested in myths. What did the attacker actually look like?"
    show miyu pissedleftpose at Three1 with Dissolve(0.2)
    mh8 "It may not be important to you, but the creature itself may hold some significance."
    show ichirou serious at Three3 with Dissolve(0.2)
    iy1 "In what way?"
    show miyu pissedclosedpose at Three1 with Dissolve(0.2)
    mh8 "The name of the facility.{w=1.0} The \"manifestation\" of that creature hints at it. If we're lucky, we can ask the authorities to run a search of the place."
    show ichirou confused at Three3 with Dissolve(0.2)
    iy1 "Good points.{w=1.0}{nw}"
    show ichirou focus at Three3 with Dissolve(0.2)
    iy1 "Good points.{fast} Let's return to the same question.{w=1.0} Once more, who killed Kyou Kirisaki? Was it the same thing that attacked you?"

    show inoue seriousleft at Three2 with Dissolve(0.2)
    show sayo seriousserious at Eight1 with Dissolve(0.2)
    "Inoue glanced to her right. Sayo gazed over her shoulder blank-faced."
    hide sayo with Dissolve(0.2)

    show ichirou focusleft at Three3 with Dissolve(0.2)
    iy1 "Hmph."
    hide miyu with Dissolve(0.2)
    show sumiko angry at Three1 with Dissolve(0.2)
    st3 "What does that mean, Ichirou? Don't say you haven't changed your mind even after this?"
    iy1 "No. She's trying to cover it up."
    show inoue seriouspose at Three2 with Dissolve(0.2)
    is4 "..."
    show akira worried at Eight7 with Dissolve(0.2)
    ai2 "Stop being a hardball, Ichi. I understand where you're coming from but you stepped over the line."
    show ichirou surprised at Three3 with Dissolve(0.2)
    iy1 "There is that one possibility. If it can't be proven, then we just press on. No big deal."
    hide akira with Dissolve(0.2)
    show yoshiro serious at Eight7 with Dissolve(0.2)
    ys6 "Let me reiterate.{w=1.0} Besides the motive, you must have the capacity to commit such horrible acts. And there are a few people here who make the shortlist."
    show ichirou focus at Three3 with Dissolve(0.2)
    iy1 "I agree."
    hide sumiko with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    show miyu bored at Three1 with Dissolve(0.2)
    mh8 "Unfortunately for you, I don't."
    show ichirou happy2 at Three3
    iy1 "Prove it otherwise, then!"
    hide miyu
    hide ichirou
    hide inoue

    window show
    nvl clear
    narr "Soon, the peaceful conversation escalated to chaos."
    narr "Arguments were thrown and dismantled.{w} Person X must be the killer, Inoue is misremembering, Ichirou's premise is twisted, Miyu and the others are blinded...{w} It is all the same childish bickering."
    narr "All of this unfolded before her eyes.{w} Was she amused?{w=1.0} No one knows.{w=1.0} Entertained?{w=1.0} Perhaps."

    nvl clear
    window hide

    show inoue serioustalk2 at Three2
    is4 "SHUT UP!!!"
    hide inoue with Dissolve(0.2)
    show miyu worried at Three3 with Dissolve(0.2)
    show sumiko surprised2 at Three2 with Dissolve(0.2)
    show hikaru worried at Three1 with Dissolve(0.2)
    ".................."
    hide hikaru with Dissolve(0.1)
    hide sumiko with Dissolve(0.1)
    hide miyu with Dissolve(0.1)
    show ichirou worried at Three1 with Dissolve(0.2)
    show yoshiro angry at Three2 with Dissolve(0.2)
    show akira worried at Three3 with Dissolve(0.2)
    "................."
    hide akira with Dissolve(0.1)
    hide yoshiro with Dissolve(0.1)
    hide ichirou with Dissolve(0.1)
    show sayo blankfaceclosedpose at Three1 with Dissolve(0.2)
    show inoue serioustalk at Three3 with Dissolve(0.2)
    is4 "Everyone, please listen to me.{w=1.0} Enough of all the speculations and accusations. I will talk."
    hide sayo with Dissolve(0.2)
    show inoue worried at Three2 with Dissolve(0.5)
    is4 "{cps=25}I witnessed it --{w=0.5} the moment of Kirisaki's death.{/cps}"

    "{b}*GASP*{/b}"

    iy1 "Tell us!"
    hide inoue with Dissolve(0.2)

    scene bg clinic with fade
    is4 "{cps=25}The image...{w=1.0} It's still forged deep within my memory.{/cps}{w=1.5} I thought I might have fractured my mind while I was there.{w=3.0}{nw}"

    scene bg whiteroom with dissolve
    is4 "With Hiroshi's death, only then I ascertained the truth.{w=1.0} It is a monster with both heads on illusion and reality.{w=3.0}{nw}"

    scene bg whiteroom nightmare with dissolve
    is4 "{cps=20}It was a nightmare...{/cps}{w=1.0} His screams pleaded that he be salvaged from Hell.{w=3.0}{nw}"

    scene bg abyss with dissolve
    is4 "{cps=20}And I couldn't do anything...{/cps}{w=2.0} {i}*sniffle*{w=1.0} *SOB*{/i}"

    window show
    nvl clear
    narr "{cps=20}Every sentence...{/cps}{w=1.0} {cps=15}Every word...{/cps}{w=1.0} {cps=20}Inoue slowly,{/cps}{w=0.5} {cps=15}slowly,{/cps}{w=0.5} {cps=10}slowly{/cps}{w=0.5} trailed off into the insanity she acquainted with during her detention."
    narr "Kyou's final moments flashed violently in her mind."
    narr "She fought back her tears.{w=1.0} She needed to be calm.{w=1.0} {cps=25}If not, she would be forever chained in anguish.{/cps}{w=2.0}{nw}"

    nvl clear
    window hide

    scene bg school outside with fade
    show inoue noglass worried at Three2 with Dissolve(0.2)
    is4 "It was me. I killed him.{fast}{w=3.0}{nw}"
    "\"WHAT?! No...!\""
    show inoue noglass worried at Three3 with Dissolve(0.2)
    show sayo normaltalk at Three1 with Dissolve(0.2)
    sr5 "Inoue, are you certain about your claim? Are you not incriminating yourself for Kirisaki's murder?"
    show inoue noglass serious at Three3 with Dissolve(0.2)
    is4 "Don't lecture me. I know what I'm saying.{w=1.0} Besides, among the people here, it is you whom I trust the least."
    show sayo seriousnormal at Three1 with Dissolve(0.2)
    sr5 "I figured.{w=1.0} Anyway, for everyone's sake, you must speak the truth and {i}only{/i} the truth."
    show inoue noglass angry at Three3 with Dissolve(0.2)
    is4 "That is the truth!{w=1.0} You --{nw}"
    show sayo serioustalk2 at Three1
    sr5 "Never mind me! Carry on with your testimony!"
    show inoue noglass serious2 at Three3 with Dissolve(0.2)
    is4 "..."
    show inoue noglass pissed at Three3 with Dissolve(0.2)
    is4 "{b}*EXHALE*{/b} If you insist..."
    hide inoue
    hide sayo

    scene white with dissolve
    scene bg chemistrylab with dissolve
    is4 "Did I say I killed him a while ago?{w=1.0} I mis-phrased that;{w=0.5} rather, I {i}caused{/i} his death."
    show kyou angrytalk at Three1 with Dissolve(0.2)
    show inoue noglass angry at Three3 with Dissolve(0.2)
    is4 "After our fight in the conjuncting chemistry lab, a shelf full of chemicals crashed onto him. He was bathed and soon fell into a stupor."
    hide kyou with Dissolve(0.2)
    hide inoue with Dissolve(0.2)

    scene bg clinic with dissolve
    show inoue noglass worried at Three3 with Dissolve(0.2)
    is4 "I panicked. The next room happened to be an infirmary, so I dragged him there and propped him up the only bed.{w=1.0} I looked for a bucket to collect water. There was none."
    show inoue noglass sadleft at Three1 with Dissolve(0.2)
    is4 "Instead, I found a hose which I connected to the nearest faucet."
    show inoue noglass sadleft at Three2 with Dissolve(0.2)
    is4 "I opened the taps and...{w=1.5}{nw}"
    hide inoue

    scene bg fire with vpunch
    is4 "I opened the taps and...{fast} flames rushed out of the faucet and caused an explosion. It almost burned down the entire room!{w=1.0} I was knocked back to the wall while Kirisaki was seared."
    is4 "By the time I extinguished the flames, it was already too late.{w=2.0} He was no longer screaming. Kirisaki was burned to a crisp, his face beyond recognition."

    scene bg school outside with fade
    show inoue noglass sadcry2 at Three2 with Dissolve(0.2)
    "....................."
    show inoue noglass sadcry at Three2 with Dissolve(0.2)
    is4 "{cps=15}I got him killed...{w=0.5} {i}*sniff*{/i}{/cps}{w=1.0} There.{w=0.5} You can end all your petty arguments now."
    hide inoue with Dissolve(0.2)
    show sumiko seriousleft at Three1 with Dissolve(0.2)
    show hikaru worried at Three2 with Dissolve(0.2)
    show yoshiro worriedleft at Three3 with Dissolve(0.2)
    is4 "{cps=25}Huh... {i}*sob*{/i}{w=1.0} Uhuhuhuhuhu...{i}*SOB*{/i}{/cps}"
    hide sumiko with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    show inoue noglass sadcry2 at Three2 with Dissolve(0.2)
    show hikaru worried2 at Three1 with Dissolve(0.2)
    hy10 "{cps=25}It's alright.{w=1.0} You didn't kill him.{/cps}"
    show inoue noglass sadcry at Three2 with Dissolve(0.2)
    is4 "{cps=25}It changes nothing, Hikaru. {i}*sniffle*{/i}{w=1.0} He still died while I did nothing...{/cps}"
    show hikaru worriedclosed at Three1 with Dissolve(0.2)
    hy10 "{cps=25}Wipe your tears. We will seek for justice.{/cps}"
    show inoue noglass sadleft at Three2 with Dissolve(0.2)
    is4 "{cps=20}Yes...{w=0.5} I'm sure we will. {i}*sniffle*{/i}{/cps}"
    show yoshiro worriedleft at Three3 with Dissolve(0.2)
    ys6 "People may or may not believe what you said.{w=2.0} Let me share my thoughts --{w=0.5} if they're worth considering."
    show inoue noglass talk at Three2 with Dissolve(0.2)
    is4 "Go on."
    show yoshiro talkleft at Three3 with Dissolve(0.2)
    ys6 "As Hikaru said, you're innocent. I concur. You were both instruments and ended up playing as the real culprit orchestrated the crimes to be."
    show yoshiro worried at Three3 with Dissolve(0.2)
    ys6 "At what extent your mind was warped, we cannot tell. But it dealt a considerable blow to your memory.{w=1.0} You may be aware of some of your actions, but bear in mind the questions you must answer to prove your innocence."
    show inoue noglass serious2 at Three2 with Dissolve(0.2)
    show hikaru serious at Three1 with Dissolve(0.2)
    hy10 "I understand where you're coming from, but why doubt her still? She told us her story and swallowed her fear in order to do so."
    show yoshiro talkleft at Three3 with Dissolve(0.2)
    ys6 "It's far more complicated than merely swallowing, Hikaru.{w=1.0} The only way we can relieve ourselves of doubt is to answer the most important question...{w=4.0}{nw}"
    show sayo normaltalkleftpose at Eight1 with Dissolve(0.2)
    sr5 "Who is behind all of this?"
    hide sayo
    hide hikaru
    hide yoshiro
    hide inoue
    scene bg school outside dark with dissolve
    show inoue noglass pissed at Three2 with Dissolve(0.5)
    "{cps=10}{b}*grumble* *groan* *hiss*{/b}{/cps}"
    st3 "Inoue, cool down...{w=1.0}{nw}"
    show inoue creepy smile3 at Three2
    is4 "It was you!{fast}{w=1.0} {b}Sayo Ronoroa!{/b}{fast}{w=1.5}{nw}"
    hide inoue with vpunch
    "{i}*WHOOSH*{/i}{w=1.0} {b}*THUD* *crack*{/b}"

    "Hikaru managed to restrain her but no longer than five seconds. Inoue charged at Sayo and grabbed her collar."

    show sayo worriedtalk at Three2
    show inoue creepy serious at Eight5 with hpunch
    sr5 "It wasn't me!{w=1.0} Ack!{w=0.5} Let me go!"
    show inoue creepy smile3 at Eight5 with hpunch
    is4 "It's what all of you criminals say, isn't it? Damn the evidence!{w=1.0} Why bother looking for something that no longer exists? You disposed it to cover up your tracks.{w=1.0} Scoundrel!"

    "Akira and Yoshiro clinched an arm each. Inoue's grip on Sayo remained tight."

    show sayo worriedtalkcry at Three2
    show inoue creepy serious at Eight5 with hpunch
    sr5 "You don't know what you're talking about. {i}*choke*{/i}{w=1.0} Please! Let me go!"
    
    "{i}*murmur* *murmur* *murmur*{/i}"

    t_nat "What is going on here?!{w=1.0}{nw}"
    scene bg school outside
    show sayo worriedtalkcry at Three2
    show inoue noglass worried at Eight5
    t_nat "What is going on here?!{fast} Ms. Shinozaki!"
    hide inoue with Dissolve(0.2)
    show sayo worriedtalkclosed at Three2 with vpunch

    "At last, they were separated. Akira and Yoshiro freed Inoue's arms and stepped away."

    show hikaru worriedtalk at Eight3 with Dissolve(0.2)
    hy10 "Sayo-chan!"
    show sayo worriedtalk at Three2 with Dissolve(0.2)
    sr5 "I'm fine... {b}*COUGH* *COUGH*{/b} Hah... I can conceal the mark."
    hide hikaru with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    show miyu worried at Three1 with Dissolve(0.2)
    mh8 "{i}*wince*{/i} My knee...{w=1.0} You alright?"
    show sumiko sighclosed at Three3 with Dissolve(0.2)
    st3 "Almost landed on my glasses. {i}*exhale*{/i}"
    hide miyu with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)
    t_nat "Inoue and Sayo, you two come with me. We have to discuss the consequences of your actions. The rest of you I will be needing as witnesses."

    "Inoue hung her head, biting her lips upon realizing it. Sayo dusted herself and wiped her glasses."

    show sayo worried at Three3 with Dissolve(0.2)
    show hikaru worried at Three2 with Dissolve(0.2)
    sr5 "This is madness..."
    hide sayo with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)

    "She did not care whether five minutes remained for lunch. Ms. Natsumoto led the students to her office, Sayo and Inoue leading the students."
    return

label ch03_05_aftermath:
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
    scene bg guidancecounselor office with fade

    show sayo blankface at Three1 with Dissolve(0.2)
    show inoue seriousleft at Three3 with Dissolve(0.2)
    window show
    nvl clear
    narr "The bell had rung. Classes have resumed. Yet the six others remained inside Ms. Natsumoto's office while she questioned Sayo and Inoue."
    narr "Inoue gnashed her teeth at the girl across from her. She could not overcome the embarrassment. What will her mother say?"
    narr "Though all six witnesses' accounts are consistent with each other, they remained nervous.{w} Ms. Natsumoto was known to be harsh with her words."
    narr "Ms. Natsumoto laid back on her chair after hearing what she needed."

    nvl clear
    window hide

    t_nat "Alright, kids. You may return to your classrooms now.{w=1.0} Let me just finish our heart-to-heart talk."

    "They complied, leaving the room without speaking. Even outside, they lacked any words."

    t_nat "Now, what do you have to say for yourselves?{w=1.0} Shall this be the last time I'll have you two for assault?"
    show sayo normaltalk at Three1 with Dissolve(0.2)
    sr5 "I apologize, ma'am. Throughout our discussion, I never intended to incite any provocation towards Inoue."
    show sayo blankface at Three1 with Dissolve(0.2)
    t_nat "Inoue, let me remind you that my patience with you is stretching thin.{w=1.0} You can't quite control yourself and hurt other people during your outburst."
    show inoue sighclosed at Three3 with Dissolve(0.2)
    is4 "It was an honest mistake, ma'am. I gave in to my own fury."
    t_nat "Again, can you handle your emotions just fine?"
    show inoue sigh at Three3 with Dissolve(0.2)
    is4 "{cps=20}Yes... I apologize.{/cps}"
    t_nat "Understood. And I will not call your parents for this.{w=1.0} What I want to see before you part ways is you girls making a truce.{w=1.0} Look each other in the eye and shake hands."

    show inoue seriousleft at Three3 with Dissolve(0.2)
    show sayo smileopen at Three1 with Dissolve(0.2)
    window show
    nvl clear
    narr "Inoue followed the first instruction, giving Sayo a cold glare. In contrast, Sayo gave a genuine smile.{w} They exchanged weak handshakes before dropping their hands."
    narr "With this, Ms. Natsumoto dismissed the two girls."
    window hide
    hide inoue with Dissolve(0.5)
    hide sayo with Dissolve(0.5)
    
    scene bg msci with dissolve
    show sayo seriousserious at Three3 with Dissolve(0.2)
    show inoue seriousleft at Three1 with Dissolve(0.2)
    window show
    narr "They left the office, Sayo opening the door."
    
    show inoue serious at Eight8 with Dissolve(0.2)
    show sayo normaltalk at Three3 with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    hide inoue
    scene bg classroom1 with dissolve
    show inoue seriouspose at Three3 with Dissolve(0.5)
    narr "Inoue zipped past Sayo and left her behind. She rubbed her hand disgustedly as she entered her classroom."
    narr "For Ms. Natsumoto, everything was resolved.{w} For Inoue, however, grudges do not fizzle out that easily."

    nvl clear
    window hide
    hide inoue with Dissolve(0.2)

    scene bg msci with fade
    "{color=#bd0000}AUGUST 5, 2013 - 1425H{/color}"

    show yoshiro worried at Three1 with Dissolve(0.2)
    show inoue blank at Three3 with Dissolve(0.2)
    ys6 "Now. Now. Let's not get ahead of ourselves.{w=1.0} We ask you once more, Inoue, are you a hundred percent sure of your statements?"
    show inoue serious at Three3 with Dissolve(0.2)
    is4 "You think I'm off my head, don't you?"
    show yoshiro talkleft at Three1 with Dissolve(0.2)
    ys6 "We don't.{w=1.0} If you were to ask my honest opinion, there are a few questionable details in your story. Emmerich would be quick to pick them apart...{w=1.0}{nw}"
    show yoshiro smirk at Three1 with Dissolve(0.2)
    ys6 "We don't.{w=1.0} If you were to ask my honest opinion, there are a few questionable details in your story. Emmerich would be quick to pick them apart...{fast} {cps=30}unless he already did.{/cps}"
    show inoue serioustalk2 at Three3 with Dissolve(0.2)
    is4 "Talk to him, then! Why would I disadvantage myself with lies? Things are already complicated as they are."
    show yoshiro smile at Three1 with Dissolve(0.2)
    ys6 "Exactly what I want to hear. Thank you."
    hide yoshiro with Dissolve(0.2)

    show inoue sighclosed at Three3 with Dissolve(0.2)
    "His questioning done, Yoshiro stepped aside and allowed her some breathing space."
    "Akira looked to the left.{w} He saw, sitting on the bench outside IV-E, Sayo and Ikuko. Miyu limped back and forth as he voiced his frustrations."

    show inoue worried at Three3 with Dissolve(0.2)
    is4 "Why is he on that girl's side?"
    show akira happy at Three2 with Dissolve(0.2)
    ai2 "Don't think too much about it. He's probably getting her side of the story, that's all."
    show inoue talk at Three3 with Dissolve(0.2)
    is4 "What lies are she feeding him? How did he find her trustworthy?"
    show ichirou serioustalkleft at Three1 with Dissolve(0.2)
    iy1 "Shouldn't we say the same for you as well? Thinking about it..."
    show inoue serioustalk at Three3 with Dissolve(0.2)
    is4 "Ichi, you shut the f--{w=1.0}{nw}"
    show akira angry at Three2
    show ichirou focus at Three1
    show inoue serious at Three3
    ai2 "Inoue!{w=0.5} Ichi!"

    show akira serious at Three2 with Dissolve(0.2)
    show ichirou focusleft at Three1 with Dissolve(0.2)
    show inoue seriousleft at Three3 with Dissolve(0.2)
    "Akira's eyes tore through their faces.{w=1.0} Ichirou shrugged it off, Inoue remaining agitated."

    show ichirou serioustalk at Three1 with Dissolve(0.2)
    iy1 "Look. If you were to share this to anyone besides us and your family, they're gonna think you did it. Will they understand?{w=1.0} Nine of ten times, they won't."
    iy1 "What you testified is actually detrimental to your case. Imagine how credible you will be when you say it as it is."
    is4 "Hmmmmmm..."
    hide ichirou with Dissolve(0.2)
    show yoshiro worried at Three1 with Dissolve(0.2)
    ys6 "I'm afraid we have nothing to go on except her story and the initials of our culprit, L.C."
    show akira surprised2 at Three2 with Dissolve(0.2)
    ai2 "That doesn't include everything that's just happened, though."
    hide inoue with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    hide akira with Dissolve(0.2)

    scene bg school outside with dissolve
    "Ichirou huddled them together, directing them away from the classroom. He continued in a low voice."

    show ichirou confused at Three2 with Dissolve(0.2)
    iy1 "I'm sorry, guys. I can't hide Hiroshi's death any longer."
    show akira worried at Three1 with Dissolve(0.2)
    ai2 "You're going to tell them?! Do you want us to get probed if this elevates to a scandal?"
    show ichirou worried at Three2 with Dissolve(0.2)
    iy1 "I can't stand my classmates comparing Hiroshi's sudden disappearance to that of Kyou and Inoue's."
    ai2 "Can't we wait for Inspector E. a little longer?"
    show ichirou serioustalk at Three2 with Dissolve(0.2)
    iy1 "I'm not waiting for that damned gumshoe! His security measures was a dud!{w=1.0} If we ever want to convict L.C. for their crimes, I suggest we do it ourselves."

    show ichirou focusleft at Three2 with Dissolve(0.2)
    "Ichirou looked to the left, catching a glimpse upon Miyu returning to IV-C."

    iy1 "If the fox does not wish to come out of its hole, then we force it to.{w=1.0} On the off-chance we are wrong about our assertions...{w=3.0}{nw}"
    show ichirou focus at Three2 with Dissolve(0.2)
    iy1 "{cps=25}...Then we seek the answers another way.{/cps}"
    show yoshiro surprised2 at Three3 with Dissolve(0.2)
    ys6 "How about we go to the archives and look up anyone who bears L.C.'s initials?"
    show inoue smile at Eight8 with Dissolve(0.2)
    is4 "I'm fine with that. When do we go?"
    show yoshiro serious at Three3 with Dissolve(0.2)
    ys6 "This Saturday -- Freedom Park at ten o' clock."
    show ichirou smile at Three2 with Dissolve(0.2)
    iy1 "I don't have any prior engagements on that day. Count me in."
    show akira surprised at Three1 with Dissolve(0.2)
    ai2 "I'm free to go, too, but can't we just search it on the internet?"
    show ichirou confused at Three2 with Dissolve(0.2)
    iy1 "Nope. Some pieces of information are only available physically. There is bound to be false information circulating around online."
    show ichirou proud at Three2 with Dissolve(0.2)
    iy1 "So, come along unless you want to get left behind."
    hide ichirou with Dissolve(0.2)
    hide akira with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)
    hide inoue with Dissolve(0.2)

    "With everything settled, the group dispersed."
    return

label ch03_05B_innocent:
    if path_b1 == 0:
        $ path_b1 = 1

    scene black with fade
    "{color=#5decff}AUGUST 5, 2013 - 1225H{/color}"
    scene bg guidancecounselor office with fade

    show sayo blankface at Three1 with Dissolve(0.2)
    show inoue seriousleft at Three3 with Dissolve(0.2)
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

    scene bg classroom1 with dissolve
    show sumiko seriousleft at Three3 with Dissolve(0.2)
    show hikaru surprised at Three2 with Dissolve(0.2)
    show miyu pissedclosed at Three1 with Dissolve(0.2)
    window show
    nvl clear
    narr "While IV-B's teacher had arrived, IV-C was five minutes into their lesson.{w} The teacher was their co-adviser, glaring at them arms crossed."
    show sumiko serioustalk at Three3 with Dissolve(0.2)
    narr "Sumiko explained the situation and they were let inside."
    hide sumiko with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)
    hide miyu with Dissolve(0.2)
    
    scene bg guidancecounselor office with dissolve
    show sayo blankface at Three1 with Dissolve(0.2)
    show inoue seriousleft at Three3 with Dissolve(0.2)
    narr "Back at the guidance counselor's office, Ms. Natsumoto had already decided on her course of action."

    nvl clear
    window hide

    t_nat "Inoue, let me remind you that my patience with you is stretching thin.{w=1.0} You can't quite control yourself and hurt other people during your outburst."
    show inoue sighclosed at Three3 with Dissolve(0.2)
    is4 "It was an honest mistake, ma'am. I gave in to my own fury."
    t_nat "Again, can you handle your emotions just fine?"
    show inoue sigh at Three3 with Dissolve(0.2)
    is4 "{cps=20}Yes... I apologize.{/cps}"
    t_nat "Understood. And I will not call your parents for this.{w=1.0} What I want to see before you part ways is you girls making a truce.{w=1.0} Look each other in the eye and shake hands."

    show sayo smileopen at Three1 with Dissolve(0.5)
    show inoue seriousleft at Three3 with Dissolve(0.5)
    window show
    nvl clear
    narr "Sayo took the initiative and extended her right hand. She received a cold glare before Inoue gave in to Ms. Natsumoto's request."
    narr "With this, Ms. Natsumoto dismissed the two girls."
    window hide
    hide inoue with Dissolve(0.5)
    hide sayo with Dissolve(0.5)
    
    scene bg msci with dissolve
    show sayo seriousserious at Three3 with Dissolve(0.2)
    show inoue seriousleft at Three1 with Dissolve(0.2)
    window show
    narr "They left the office, Sayo opening the door."
    
    show inoue serious at Eight8 with Dissolve(0.2)
    show sayo normaltalk at Three3 with Dissolve(0.2)
    hide inoue with Dissolve(0.2)
    narr "Inoue zipped past Sayo and left her behind. The latter understood her urgency, yet she felt some hint of animosity."
    
    show sayo seriousnormal at Three3 with Dissolve(0.2)
    narr "The aftermath had further drifted them away, opposite of what Sayo had hoped to occur."

    nvl clear
    window hide
    hide sayo with Dissolve(0.2)

    scene bg msci with fade
    "{color=#5decff}AUGUST 5, 2013 - 1420H{/color}"

    show sayo seriousclosedpose at Eight6 with Dissolve(0.2)
    show ikuko blank at Eight7 with Dissolve(0.2)
    "Sayo buried her face within her hands as Ikuko listened to whatever she had to say."
    show miyu confused at Three1 with Dissolve(0.5)
    show miyu confused at Three2 with Dissolve(0.5)
    "Miyu, despite his injury, paced back and forth in front of IV-E, outraged at the outcome of Inoue's questioning."

    show miyu talk at Three1 with Dissolve(0.5)
    mh8 "Shall we report this to Mrs. Genkai?"
    show sayo serioustalkpose at Eight6 with Dissolve(0.2)
    sr5 "It would make no difference. Doing so implies an abuse of power and would worsen my image."
    show miyu serious at Three1 with Dissolve(0.2)
    mh8 "I understand your need to uphold your role model principle, but get this. She acted like she wanted to kill you."
    show sayo normaltalkpose at Eight6 with Dissolve(0.2)
    sr5 "I know how she feels. I have forgiven her, Miyu.{w=1.0} She may have wronged me but she did so while her mind was clouded."
    show miyu happytalk at Three1 with Dissolve(0.2)
    mh8 "She did no better!"
    show ikuko worried at Eight7 with Dissolve(0.2)
    ikuko "Mi-kun, please calm down. Sayo's having a lot running in her head now."
    show miyu serious at Three1 with Dissolve(0.2)
    mh8 "She's being falsely accused of murder or, at least, masterminding the kidnappings. That's what started this whole rift in the first place."
    show miyu bored at Three1 with Dissolve(0.2)
    show sayo seriousclosedpose at Eight6 with Dissolve(0.2)
    mh8 "I suppose you're aware of the consequences if we let this slide."
    show ikuko blank at Eight7 with Dissolve(0.2)
    ikuko "We know that."
    show miyu talk at Three1 with Dissolve(0.2)
    mh8 "Then we {i}cannot{/i} let this slide, Ikuko. We already have two victims because of negligence. Worse, one of them met their end inside the Council office!"
    show sayo serioustalk2 at Eight6 with Dissolve(0.2)
    sr5 "That's enough!"

    show miyu worried at Three1 with Dissolve(0.2)
    "Her lashing resonated around the walls of the classroom, conjuring a moment of silence and several intrigued eyes to take a gander.{w} Miyu hung his head and stopped in his tracks."

    show sayo worried at Eight6 with Dissolve(0.2)
    sr5 "{i}*sigh*{/i} I fully comprehend the situation. I would rather not witness another murder myself."
    mh8 "..."
    show sayo worriedtalk at Eight6 with Dissolve(0.2)
    sr5 "Do you know the difference between your sentiments and mine?"
    show miyu bored at Three1 with Dissolve(0.2)
    mh8 "I do."
    show sayo worriedtalkclosed at Eight6 with Dissolve(0.2)
    sr5 "I'm the head of the studentry, and protecting it is part of the code I upkeep.{w=1.0} I failed in that, the thought gnawing at me each day."
    show sayo worriedtalk at Eight6 with Dissolve(0.2)
    sr5 "That makes me no different from Inoue.{w=1.0} She was helpless in preventing Kirisaki's death. I did next to nothing to ensure Hiroshi's safety."
    show sayo upset at Eight6 with Dissolve(0.2)
    sr5 "I never wished misfortune to befall upon anyone, petty or not.{w=1.0} When that voice called us, I asked myself, \"Why?\"{w=2.0} {cps=25}Of all people, why me?{w=1.0} Why {i}you{/i}?{w=1.0} Why {i}them?{/i}{/cps}{w=1.0} Ask yourself, did you ever will for this to happen?"
    mh8 "..."
    show miyu worried at Three1 with Dissolve(0.2)
    mh8 "{cps=15}I'm scared...{/cps}"
    show sayo seriousserious at Eight6 with Dissolve(0.2)
    sr5 "Pardon?"
    show miyu talk at Three1 with Dissolve(0.2)
    mh8 "I don't want to die.{w=1.0} Not in the way Kyou and Hiroshi did.{w=0.5} It's messed up -- butchered like animals!"
    show ikuko talk at Eight7 with Dissolve(0.2)
    ikuko "Me neither.{w=1.0} All I can do now is to assure my parents of my safety. I might never set foot in MSCI again should another one fall."
    show ikuko blank at Eight7 with Dissolve(0.2)
    show miyu pissed at Three1 with Dissolve(0.2)
    mh8 "Tch.{w=1.0} If only Emmerich would hurry up with his investigation and jail that criminal."
    mh8 "I cannot stand watching people point fingers on a hunch. If we are to nab the killer, I suggest we do it now.{w=1.0} We are the most affected, after all."
    show sayo serioustalkleft at Eight6 with Dissolve(0.2)
    sr5 "And also the persons of interest."
    mh8 "That, too."

    show sayo normaltalk at Eight6 with Dissolve(0.2)
    show miyu talk at Three1 with Dissolve(0.2)
    "{i}*snap*{/i}"

    show ikuko smile at Eight7 with Dissolve(0.2)
    ikuko "How about you approach this from another angle?{w=1.0} If we cannot draw any information from ourselves, even with Inoue, then we investigate the next best thing."
    show sayo smiletalk at Eight6 with Dissolve(0.2)
    sr5 "That is preferable."
    show miyu smile at Three1 with Dissolve(0.2)
    mh8 "What would the \"next best thing\" be?"
    ikuko "Sayo-chan told me about the similarity in motif between our own murders and those of Sacred Heart Academy. Why don't you start at the root?"
    show miyu smiletalk at Three1 with Dissolve(0.2)
    mh8 "That's brilliant! I see how that would work for us."
    show miyu talk at Three1 with Dissolve(0.2)
    mh8 "Although... there is one glaring problem.{w=1.0} Rika Suzumiya, the closest we have to the main suspect, is one of the victims herself. After her, we have no significant leads."
    show sayo normaltalkleft at Eight6 with Dissolve(0.2)
    sr5 "We have another option.{w=2.0} We can trace the killer's identity through the methods. We might uncover a link."
    show miyu surprised at Three1 with Dissolve(0.2)
    mh8 "A link! Interesting...{w=1.0} And we might shoot a second bird in the interim."
    show sayo blankface at Eight6 with Dissolve(0.2)
    sr5 "That...{w=1.0} we exclude ourselves. Let's focus on our own problems while they are still young."
    show miyu smile at Three1 with Dissolve(0.2)
    mh8 "So, this weekend?"
    sr5 "Sunday. I have already blocked my schedule for Saturday."
    show miyu worried at Three1 with Dissolve(0.2)
    mh8 "That's the Sabbath Day. I don't usually agree to come on that day."
    show sayo worried at Eight6 with Dissolve(0.2)
    sr5 "Hm?"
    show miyu smile at Three1 with Dissolve(0.2)
    mh8 "Just this once, then. We no longer have a safe time frame for the month, if you may also recall."
    show sayo smiletalk at Eight6 with Dissolve(0.2)
    sr5 "Hehehehehehe. True."

    show sayo smileopen at Eight6 with Dissolve(0.2)
    "Exciting, maybe, given how they marveled at the idea. At the same time, it is all for Sayo's innocence."

    show miyu smiletalk at Three1 with Dissolve(0.2)
    mh8 "Want to come along, Ikuko?"
    show ikuko blank at Eight7 with Dissolve(0.2)
    ikuko "I would love to, but I have Church on Sunday. You go on ahead. I'll be hearing the results afterwards if you wish."
    show miyu proudclosed at Three1 with Dissolve(0.2)
    mh8 "Then it's settled. {i}*chuckle*{/i}"
    hide ikuko with Dissolve(0.2)
    hide sayo with Dissolve(0.2)
    hide miyu with Dissolve(0.2)

    scene bg classroom2 with dissolve
    "After exchanging a few more words, Miyu returned to IV-C.{w} He spotted Hikaru eating with Aria. Sumiko had returned from the canteen."

    show miyu talk at Three2 with Dissolve(0.2)
    show hikaru smile at Three3 with Dissolve(0.2)
    show sumiko serious at Three1 with Dissolve(0.2)
    mh8 "Hikaru, Sumiko, I want to ask you two something."
    show hikaru surprised2 at Three3 with Dissolve(0.2)
    hy10 "What is it?"
    show miyu serious at Three2 with Dissolve(0.2)
    mh8 "Sayo is inviting us this Sunday to do some sleuthing at Sacred Heart Village. She said it's the best way to gather information about our case."
    show hikaru surprisedtalk at Three3 with Dissolve(0.2)
    hy10 "{i}That{/i} far? We have a church gathering late afternoon."
    show sumiko surprisedtalk at Three1 with Dissolve(0.2)
    st3 "Is there any other alternative? I'm okay with anything as long as we're all going."
    show miyu surprised at Three2 with Dissolve(0.2)
    mh8 "We can't schedule it this Saturday because Sayo has prior commitments."
    show sumiko seriousleft at Three1 with Dissolve(0.2)
    st3 "And we might bump into the {i}other faction{/i} should we decide to go on that day."
    show miyu confused at Three2 with Dissolve(0.2)
    mh8 "Then we find a compromise. It's the last {i}safe{/i} weekend before L.C. makes their move."
    show hikaru thinkingleft at Three3 with Dissolve(0.2)
    hy10 "I'll let you guys know, then. Let me see if I can convince Mama and Papa about this."
    hide sumiko with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)
    hide miyu with Dissolve(0.2)

    "And they returned to their respective seats, agreeing to discuss the rest over Facebook."
    return

label ch03_06_investigation1:
    scene black with fade
    "AUGUST 7, 2013 - 0745H"
    scene bg policedepartment office with fade

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

    scene black with fade
    $ current_area = 0 # Office
    $ lock = 0 # Locks on to the current menu
    $ areas = 3 # [Office, Conference Room]
    $ visited = 0 # [Office, Conference Room]
    $ i1_office = 0
    $ i1_conference = 0

    while i1_office < 7 or i1_conference < 15:
        if current_area == 0: # Office
            if not parse_bin(visited, 0):
                scene bg msci night rain with fade
                window show
                nvl clear
                narr "It had rained that night.{w} The culprit saw their chance to act during the ensuing blackout."
                narr "Had they been too late? Too incompetent to stop the murders?{w} For Emmerich, it is the former -- all planned by a cunning mind."
                narr "The witnesses were rounded up in the conference room while investigation in the crime scene was ongoing."

                nvl clear
                window hide

                scene black with fade
                centered "{color=#bd0000}--INVESTIGATION START--{/color}"

                scene bg facultyroom with fade
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
                                        scene bg blood2 with dissolve
                                        "The body occupies one of the workstations, belonging to a certain Akira Ichibana -- auditor of the Student Council."
                                        "The victim is in a sorry state. His face and neck are bound tightly with masking tape. The intent was to kill the victim either by asphyxiation or blood loss."
                                        "Both of his hands lie on the desk. All of his fingers are chopped, the indices spread around the workstation."
                                        "Turning over his hands reveals two numbers etched onto his palms."
                                        "Number {color=#bd0000}7{/color} on the left, number {color=#bd0000}10{/color} on the right. They are carved similar to the ones on Kyou Kirisaki's body."
                                        scene bg facultyroom with dissolve
                                        
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
                            scene bg conferenceroom with fade
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
                            show sayo worried at Three3 with Dissolve(0.2)
                            $ lock = 1
                            if not (parse_bin(i1_conference,0) and parse_bin(i1_conference,1)):
                                "The Student Council President's eyes are swollen. Though visibly shaken, she wore a brave face to help with the investigation."
                                p_emm "I'm sorry for your loss, Sayo. This is unfortunate."
                                show sayo worriedtalkclosed at Three3 with Dissolve(0.2)
                                c_sr5 "Truly.{w=0.5} And in the middle of a storm!{w=1.0} {i}*sigh*{/i} Taking advantage of the outage to strike -- the mark of a monster."
                                p_emm "If I may, I need to ask you some preliminary questions before we invite you to the station."
                                show sayo smileopen at Three3 with Dissolve(0.2)
                                c_sr5 "Ah. The classic \"ask the suspects in the crime scene\" technique, I see.{w=1.0} Very well. I will be glad to help."

                            while lock == 1  and (i1_office < 7 or i1_conference < 15):
                                menu:
                                    "Last seen alive":
                                        p_emm "What happened here? Rather, when did you last see Hiroshi alive?"
                                        show sayo normaltalk at Three3 with Dissolve(0.2)
                                        c_sr5 "I stayed for a while here until around 6:15 PM, at which I reported to our adviser, Mrs. Genkai."
                                        show sayo normaltalkleft at Three3 with Dissolve(0.2)
                                        c_sr5 "Hiroshi said he was working on a project -- not sure what. A little after, the power outage occurred."

                                        if not parse_bin(i1_conference,0):
                                            $ i1_conference += 1

                                    "Power outage":
                                        p_emm "Does the power outage happen often?"
                                        show sayo blankface at Three3 with Dissolve(0.2)
                                        c_sr5 "Not really. During August to October, the frequency on average is about three times.{w=1.0} Either the power is restored immediately or we are told to go home."
                                        show sayo blankfacepose at Three3 with Dissolve(0.2)
                                        c_sr5 "This is the latest I have stayed during an outage."
                                        p_emm "By the way, between the power outage and the discovery of the body, did you enter this office in the interim?"
                                        show sayo normaltalkpose at Three3 with Dissolve(0.2)
                                        c_sr5 "I did."

                                        if not parse_bin(i1_conference,1):
                                            $ i1_conference += 2

                                    "Let's discuss the rest later.":
                                        p_emm "Let's discuss the rest later. I feel that we will take forever if I ask every question now."
                                        show sayo smileopen at Three3 with Dissolve(0.2)
                                        c_sr5 "Don't worry. Good luck on your investigation, Inspector."

                                        hide sayo with Dissolve(0.2)
                                        $ lock = 0

                        "Akira Ichibana":
                            show akira worriedleft at Three1 with Dissolve(0.2)
                            $ lock = 1
                            if not (parse_bin(i1_conference,2) and parse_bin(i1_conference,3)):
                                "I recognize him.{w} He is one of Ichirou's chipper friends."
                                "Sadly, that peppiness is overshadowed by his somberness. If I had to guess, he was the first to discover the body."
                                p_emm "Good evening, young sir."
                                show akira proud2 at Three1 with Dissolve(0.2)
                                c_ai2 "Oh! You're Inspector E, right?{w=1.0} I'm Akira. Akira Ichibana."
                                p_emm "No need to panic. {i}*chuckle*{/i} I'm here. Everything will be alright."
                                show akira worried at Three1 with Dissolve(0.2)
                                c_ai2 "You mean no bogeyman will come at us from the shadows?"
                                p_emm "You still believe in those things?!"
                                p_emm "Ahem!{w=0.5} Excuse my rudeness.{w=1.0} Anyway, I need to ask you a few questions. The victim is sitting on your workstation."
                                show akira proud at Three1 with Dissolve(0.2)
                                c_ai2 "If it would help nab that freak, I'm in!"

                            while lock == 1 and (i1_office < 7 or i1_conference < 15):
                                menu:
                                    "Discovered body":
                                        p_emm "From your behavior, I surmise that you were the nearest to the victim at the moment of discovery."
                                        show akira happy at Three1 with Dissolve(0.2)
                                        c_ai2 "Why, yes! You are as sharp as they made you."
                                        p_emm "Thank you. Now, what was the victim doing at your workstation?"
                                        show akira surprised at Three1 with Dissolve(0.2)
                                        c_ai2 "Working on something. Said his family desktop was busted.{w=1.0} If I may mention, I saw him insert a flash drive into the CPU."
                                        p_emm "Of course, he would. You just told me why."
                                        show akira surprised2 at Three1 with Dissolve(0.2)
                                        c_ai2 "No. That flash drive didn't look like his. I don't know."
                                        p_emm "I noticed nothing of the sort but I will double check."
                                        show akira worried at Three1 with Dissolve(0.2)
                                        p_emm "Let me remind you, however, that not every new flash drive you see means something bad. It could be that the original device is broken."

                                        if not parse_bin(i1_conference,2):
                                            $ i1_conference += 4

                                    "Power outage":
                                        p_emm "Where were you during the power outage?"
                                        show akira surprised at Three1 with Dissolve(0.2)
                                        c_ai2 "Doing my business. I was with these three stooges."
                                        p_emm "Past your curfew? Why did you not go home right away?"
                                        show akira fangblush at Three1 with Dissolve(0.2)
                                        c_ai2 "I have LBM...{w=1.0} and I didn't bring some meds."
                                        p_emm "You learned your lesson, big boy.{w=1.0} About those \"three stooges,\" were they with you the whole time?"
                                        show akira worriedleft at Three1 with Dissolve(0.2)
                                        c_ai2 "I'm not sure. I called out to them but nobody responded.{w=1.0} The feeling that you're trapped inside that bathroom stall...{w=1.0} It almost drove me insane."
                                        show akira worried at Three1 with Dissolve(0.2)
                                        c_ai2 "When I burst out of the stall, they were there the whole time. A prank done in poor taste, I say!"
                                        p_emm "That might have given me an idea."

                                        if not parse_bin(i1_conference,3):
                                            $ i1_conference += 8

                                    "We'll discuss this in depth later.":
                                        p_emm "We'll discuss this in depth later."

                                        hide akira with Dissolve(0.2)
                                        $ lock = 0
                        
                        "<<< BACK":
                            pass

                "Move":
                    menu:
                        "Office" if parse_bin(areas,0):
                            scene bg facultyroom with fade
                            $ current_area = 0
                        "<<< BACK":
                            pass

    hide sayo with Dissolve(0.2)
    hide akira with Dissolve(0.2)
    scene black with fade
    centered "{color=#5decff}--INVESTIGATION COMPLETE--{/color}"
    scene bg policedepartment lobby with fade

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

    scene bg policedepartment office with fade
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
    scene bg freedompark with fade

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

    scene bg park2 with dissolve
    narr "Once we made it out of the street, we were at Kutsutochi North.{w} To the right is my alma mater and its chapel. Across from us is the cultural center designed to be an ancestral home."

    nvl clear
    narr "Westward is our destination, Kutsutochi Public Library."
    narr "It always seemed quiet, not seeing that many patrons even during weekends. Unsurprising given how few students ever go to their school library."
    narr "Akira disposed of the paper bag, wiping his mouth and hands with tissue."

    nvl clear
    window hide

    ai2 "Three pieces to last the day!"
    iy1 "Good. My calculations were correct."

    scene bg library circulation with dissolve
    "We went inside, the musky smell of colonial times wafted the air."
    "The floors were waxed to resemble a mirror, and light reflected well on the varnished wood. Air conditioners are engaged all over the building.{w} It is a big wonder why no one comes to even sleep here."
    "Besides the librarian's desk is the Citizen's Charter and a map of the facility."

    ys6 "Two floors, huh? How do we go about this?"
    iy1 "Why don't we ask the librarian first before anything? Besides we need a guide if we want to accomplish our goal much quicker."

    scene black with fade
    centered "{color=#bd0000}--INVESTIGATION START--{/color}"
    scene bg library circulation with fade

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
                                            "A different librarian is behind the desk. The other lady headed out for lunch.{w} It doesn't change things that much, though."

                                            iy1 "Good morning. I need some assistance with my research.{w=1.0} I want to look up someone with the initials \"L.C.\" Limited to Kutsutochi, please."
                                            librarian "Wait just a moment, sir."

                                            "{i}*click* *click* *clack* *clack* *clack* *clack* *clack* *clack* *clack* *clack* *clack* *clack*{/i}"
                                            "With that decterity, she could have been a secretary or clerk in the past. Maybe she {i}is{/i} the clerk here?"

                                            librarian "Do you have a pen and paper? I'll list the names here."
                                            iy1 "Oh. I, uh...{w=1.0}{nw}"
                                            ai2 "Here."
                                            iy1 "Eh? Where did you come from?"
                                            ai2 "I saw you coming down here so I followed. Figured you might need some pen and paper."
                                            iy1 "That's very resourceful of you."
                                            librarian "Here you go, sir."

                                            "The list has ten names with pertinent information -- age, status, and whatnot. Three of them are marked with {i}dec.{/i}"

                                            librarian "All of them you can find in the Directory, second floor in the Periodicals section. I've marked the ones who are deceased so you can find them in the obituary."
                                            iy1 "This is great help.{w=1.0} Thanks, ma'am!"
                                            ai2 "Lead the way, Ichi. I think you need more hands upstairs."
                                            iy1 "Okay. Let's go."

                                            $ lock = 0
                                            scene bg library periodicals with fade
                                            $ current_area = 2

                                            ai2 "We got the goods."
                                            ys6 "Hey! You're here.{w=1.0} How did your research go?"
                                            ai2 "I didn't find anything related to the case. Still, I found a few interesting concepts that we may use to help with our investigation."
                                            ys6 "I see. You're gonna stay here and help?"
                                            ai2 "Absolutely! It's so lonely down there."
                                            iy1 "You take the list, Akira. I'll look up the deceased names in the newspapers."

                                        else:
                                            ai2 "Ichi, we already have the list of names. Let's find out more about these people so we can move forward."

                                        if not parse_bin(i2a_circulation,2):
                                            $ i2a_circulation += 4

                                    "Children's section" if parse_bin(i2a_periodicals,5):
                                        if not parse_bin(i2a_circulation,3):
                                            "Same old lady. Looks grumpier than when we first inquired to her.{w=1.0} Although, she did say she would help if we ask."

                                            iy1 "Excuse me. Where is the Children's Section?"

                                            "The librarian didn't answer immediately.{w} She eyed me from head to toe while I stood petrified and awkward."

                                            librarian "Proceed to the East Wing.{w=1.0} Are you planning on borrowing a book there?"
                                            iy1 "I don't have a library card."
                                            librarian "Then why do you need to go there?"
                                            iy1 "I am looking for a book.{w=1.0} I...{w=1.0} want to read it here."
                                            librarian "By the looks of it, son, you are too old to be reading there.{w=1.0} If it is a children's book you need, you can borrow {i}if{/i} you have a library card."
                                            iy1 "But I don't have an ID Picture with me, ma'am."
                                            librarian "So, what do you suggest we do?"
                                            iy1 "I only need it for one hour at most. I can surrender my School ID if you like."

                                            "She stared at my ID,{w=1.0} moments before dialing the Children's Section's librarian."

                                            librarian "What is the name of the book, son?"
                                            iy1 "Any nursery rhyme collection.{w=1.0} Mother Goose, preferably."

                                            "She relayed the information to her fellow librarian."
                                            "Within a minute, the younger librarian from before appeared with the book in hand. I exchanged it with my ID and an hour."

                                            librarian "One hour, Mr. Yokohama. Any longer than that, you will incur a penalty."

                                            "I gave her my word and left there as soon as I could."

                                            scene bg library periodicals with fade
                                            "Inoue was waiting for me outside the Periodicals section."
                                            
                                            is4 "Is that Mother Goose? {i}*giggle*{/i} What do you need that for?{w=1.0} Let me guess.{w=0.5} You're tired of this adult job, huh?"
                                            iy1 "Quit it."

                                            "We peeked inside the Table of Contents.{w} Among those listed were {i}Star Light, Star Bright{/i}, {i}Ten Little Indians{/i}, and fifty other rhymes."
                                            "I had Inoue read the book herself."

                                            iy1 "Now, do any of these ring a bell?"

                                            "She took no longer than one minute scanning each rhyme. This she did with a mocking grin plastered on her face."

                                            is4 "{cps=30}Ring a ring o' roses...{/cps}"

                                            "Her hand stopped. Her eyes went wild upon reading the words on each verse."

                                            is4 "{cps=20}Ring around the rosie...{w=1.0} Pocket full of posies...{/cps}{w=1.5}{nw}"

                                            "{b}*THUD*{/b}"

                                            ys6 "What's going on here?"
                                            iy1 "I didn't mean to!"

                                            "The light was leaving Inoue's eyes.{w=1.0} It was a sign.{w=1.0} {cps=15}Churn.{w=0.5} Lower.{w=0.5} Lower.{/cps}{w=1.5}{nw}"
                                            "Akira crouched down and picked up the book."

                                            ai2 "Is this...{w=1.5}{nw}"
                                            is4 "{cps=20}A'tishoo! {i}{b}*hiss*{/b}{/i}{w=1.0} A'tishoo! {i}{b}*hiss*{/b}{/i}{w=1.5} We all...{w=0.5} fall{w=0.5} down...{w=0.5}{/cps}"
                                            is4 "{cps=20}Hehehehehehehe... Hehehehehehehehe...{/cps}"
                                            ys6 "Hey! Snap out of it!"
                                            is4 "{i}*suck*{/i}{w=0.5} Hpf!{w=0.5} {b}*COUGH* *COUGH*{/b}{w=1.0} {i}*INHALE*{/i}"

                                            "We were lucky.{w=1.0} Blood returned to her lips."
                                            "Yoshiro and I assisted her to a chair and allowed her to breathe."

                                            ai2 "{cps=30}So, this was the song meant for Kyou...{w=1.0} How morbid and sick of a mind that L.C. has.{/cps}"

                                            "Indeed.{w} To quote a famous tragedy in history and to reintroduce it in the most sadistic way...{w} Only a monster would dare to do that.{w=1.0} A monster!"
                                            "We left Inoue and continued with our search."

                                            $ current_area = 2
                                        
                                        else:
                                            "I already have the book...{w=1.0} and I already upset a grown woman with it. Achievement unlocked!"

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
                                        iy1 "Do you think I have the guts to face our Vice President after that debacle in the Council room?{w=1.0} What will he say?"
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

                "Move" if areas > 1:
                    menu:
                        "General Reference" if parse_bin(areas,1):
                            scene bg library genreference with fade
                            $ current_area = 1

                        "Periodicals" if parse_bin(areas,2):
                            scene bg library periodicals with fade
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
            menu:
                "Examine":
                    menu:
                        "Bookshelves":
                            $ lock = 1

                            while lock == 1 and (i2a_genreference not in [24, 25, 26, 28, 29, 30, 31] or i2a_periodicals not in [187, 191, 251, 255]):
                                if not (parse_bin(i2a_genreference,0) and parse_bin(i2a_genreference,1) and parse_bin(i2a_genreference,2)):
                                    window show
                                    nvl clear
                                    narr "The library has at least thirty bookshelves on this section alone. There are more on the second floor, perhaps fifteen to twenty.{w} It is coupled with the seating capacity of a hundred, from individual booths to tables for six."
                                    narr "Oh, what to choose? These books may not be immediately relevant to our case, but a little knowledge is always welcome."
                                    narr "What should one look for when you ask the three essential questions of mystery --{w=1.0} the whodunnit, the whydunnit, and the howdunnit?"

                                    nvl clear
                                    window hide

                                menu:
                                    "Biochemistry":
                                        window show
                                        nvl clear
                                        narr "We must look into the possibility that Inoue and Kirisaki were poisoned -- or drugged, as it shows. Why would she pay special attention to the ampoule of liquid chlorine?"
                                        narr "The biochemistry book can help us.{w} I'm not a fan of these -- tiny font in a thick book filled with three-pass readings."
                                        narr "Chlorine...{w=1.0} Chlorine...{w=1.0} Ah! Here it is."

                                        # INCOMPLETE

                                        nvl clear
                                        window hide

                                        if not parse_bin(i2a_genreference,0):
                                            $ i2a_genreference += 1

                                    "Greek Mythology":
                                        window show
                                        nvl clear
                                        narr "It's a good thing Inoue lived to tell the tale. Otherwise, we would be depraved of one potentially vital piece of information -- the \"Labyrinth.\" L.C. included its iconic monster as a nod."
                                        narr "The earliest account of the Labyrinth is from the story of Theseus and Ariadne."

                                        nvl clear
                                        narr "King Minos of Crete had built one in order to contain the creature, a half-human and half-bull child of his wife Pasiphea."
                                        narr "The God of the Sea Poseidon, who aided him into power, had him promise to sacrifice a bull after his coronation. Minos sacrificed an inferior one instead, and thus his wife was cursed to fall in love with the first bull and let it horn her."
                                        narr "The creature had a savage nature. Minos ordered the architect Daedalus to build and design the eponymous Labyrinth."
                                        
                                        nvl clear
                                        narr "Minos decreed that every nine years, seven young men and seven young women be sacrificed to the creature. Among those was Minos' son, who failed to slay the creature."
                                        narr "In the third wave of sacrifices, Theseus joined the fourteen youths to slay the monster."
                                        narr "Minos' daughter Ariadne fell in love with Theseus and offered to assist him. Using Daedalus' thread, Theseus managed to navigate to the center of the Labyrinth and put the Minotaur to rest."

                                        nvl clear
                                        narr "The maze-like structure is a source of fascination among mathematicians and philosophers."
                                        narr "There are four layers to the overall structure: The first is the 113 teeth (the middle number of a 15-magic square) around the Labyrinth, which is the second layer; the third layer is Solomon's Seal and the fourth is the six-petaled rosette."
                                        narr "The Labyrinth itself consists of 11 concentric circles, a six-petaled flower at the center. To reach the heart, one must enter from the West, walking through a 261.50 meter long corridor, and end at the East. The long walk represents the journey to the inner self."

                                        nvl clear
                                        narr "There are several more details concerning the Labyrinth and its monster, but it would be impossible to retain everything."
                                        narr "There are a few more books to check out."

                                        nvl clear
                                        window hide

                                        if not parse_bin(i2a_genreference,1):
                                            $ i2a_genreference += 2

                                    "Criminal Psychology":
                                        window show
                                        nvl clear
                                        narr "L.C. is a psychopath -- no objections warranted.{w} The way they managed to abduct Inoue and Kirisaki, as well as managing to take out Hiroshi behind closed doors..."
                                        narr "If I were to base it on my own hypothesis, L.C. is a female. But are they really? The only thread we can follow with this is the opportunity with respect to Hiroshi's murder."
                                        narr "On the off-chance we may be mistaken about L.C.'s identity, maybe looking into some guidelines and statistics won't hurt."

                                        nvl clear
                                        narr "There is a large disparity between male and female serial killers. It would be difficult to name one from the latter group.{w} Jack The Ripper,{w=0.5} Zodiac Killer,{w=0.5} John Wayne Gacy...{w=0.5} all identified as male."
                                        narr "Psychopaths are capable of charm, manipulation, and pathological lying. Some are not necessarily mentally ill and are capable of rational decision-making. They possess an above average-level of intelligence, yet they show little remorse when the repercussions of their deeds are harmful."
                                        narr "How does L.C. manage to skirt between reality and fantasy?"
                                        narr "The ability to tap into one's subconscious and to use their fears against them is a mark of an extraordinary individual.{w} Maybe projecting demons is another critical skill. I would consult a book on exorcism, but such information is prohibited."

                                        nvl clear
                                        narr "If anything, their own fault is another one's responsibility. To have a heart entrenched in violent fantasies is pitiful (why that word?). But what's the cause?{w} Abuse, neglect, and rejection from the world. These form mental scars that permanently linger within the psychopath's mind."
                                        narr "A male serial killer would choose a stranger as their target.{w} They would stalk and continually pursue those who fit his chosen characteristics -- ones that remind him of a despicable enemy that he cannot eliminate because of an emotional hold."
                                        narr "A female serial killer would choose anyone in her vicinity, oftentimes tied to her occupation.{w} Instead of aggression, she chooses subtle methods and utilizes traps -- a black widow devouring her mate for dinner."

                                        scene bg eyesdark with fade
                                        nvl clear
                                        narr "Given all of these, who has the potential to be a psychopath?{w=2.0}{nw}"
                                        narr "{cps=10}Sayo?{/cps}{w=1.5}{nw}"
                                        narr "{cps=10}Miyu?{/cps}{w=1.5}{nw}"
                                        narr "{cps=10}Inoue?{/cps}{w=1.5}{nw}"
                                        narr "{cps=10}Hikaru?{/cps}{w=1.5}{nw}"
                                        narr "{cps=10}...Me?{/cps}"

                                        nvl clear
                                        window hide

                                        scene bg library genreference with dissolve

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
                            scene bg library circulation with fade
                            $ current_area = 0

                        "Periodicals" if parse_bin(areas,2):
                            scene bg library periodicals with fade
                            $ current_area = 2
                            
                        "<<< BACK":
                            pass

        elif current_area == 2: # Periodicals
            if not parse_bin(visited,2):
                "A college student left the room we were about to enter."
                "At least we would have it to ourselves, giving us more leeway in discussing things."

                iy1 "Where the heck do we start? Look at all those thick piles newsprint to wade through."
                is4 "We can divide these among ourselves.{w=1.0} There are also photographs to look at here."
                ys6 "Is Akira still downstairs?"
                iy1 "Doing his own research to \"help\" with the investigation."
                ys6 "At least we have someone downstairs. Let's concern ourselves with what we have now."

                $ visited += 4
            menu:
                "Examine":
                    menu:
                        "Newspapers":
                            $ lock = 1

                            while lock == 1 and (i2a_genreference not in [24, 25, 26, 28, 29, 30, 31] or i2a_periodicals not in [187, 191, 251, 255]):
                                menu:
                                    "Research" if not parse_bin(i2a_circulation,2):
                                        if not parse_bin(i2a_periodicals,0):
                                            "The newspapers dated as early as 1996, the year when Kutsutochi was established as a Capital Region city.{w} Earlier than that, it was part of the same province as Sacred Heart Village."
                                            "The first is an article detailing the inaugurual of Kutsutochi's inclusion in the Capital Region, 1975."
                                            "The next significant event is a sanitation drive by the City Government, completed in the second quarter of 1999."
                                            "Skipping to the contemporaries, we have MSCI winning the interhigh debate led by Sayo Ronoroa.{w} Wish I could make the front page after winning the Math Challenge this January before graduation. That would be awesome."
                                            "And then more news and updates,{w} {cps=25}elections, fires, crimes, anti-drug campaigns, medical missions...{/cps} {cps=15}more news... even more mundane news...{/cps}"

                                            iy1 "Ugggggghhh... This is going nowhere real quick.{w=1.0} Thirty minutes have passed without a useful result."
                                            is4 "Are you browsing the {i}correct{/i} articles? Maybe you're cherry-picking what to read, Ichirou?"
                                            iy1 "I'm serious. Without so much as a reference point, we'll reach closing time without ever finding what we need."
                                            is4 "Do something about it.{w=1.0} Why don't you go down and ask the librarian for help?"
                                            iy1 "Good idea."
                                        
                                        else:
                                            "Just as I was about to grab another newspaper, Inoue swiped her hand on the print before mine."

                                            is4 "Ichi, don't waste any more time rifling through these articles.{w=1.0} Remember what the librarian said? Go down and talk to her."
                                            iy1 "Alright. I'm going."
                                            is4 "Do it again. I'll swipe my hand over your cheeks, you hear?"
                                            iy1 "I hear you."

                                        if not parse_bin(i2a_periodicals,0):
                                            $ i2a_periodicals += 1

                                    "Obituaries" if parse_bin(i2a_circulation,2):
                                        "While Akira busied himself doing background information on those alive with L.C.'s initials, I continued my search.{w} This time, I only needed to check three newspapers."
                                        "The first two are minimalistic in-passing announcements."
                                        "One is Lester Coolidge, died on November 21, 2005.{w} Second is a certain Lelouch Calvin, died on April 1, 2007...{w=1.0} {cps=10}no joke.{/cps}"
                                        "The third is eye-catching.{w} Under the picture of a seven-year old girl is the following description:"
                                        "{i}Let Carnegie -- born on February 29, 2000 -- has joined our Lord on this day, June 1, 2007. May her soul rest in peace. She is survived by her two sisters, E and E.{/i}"
                                        "She's an orphan? That's surprising."

                                        window show
                                        nvl clear
                                        narr "Since she was the only one whose manner of death was specified in the list, I searched the rest of the newspaper for a related article."
                                        narr "It was located at the bottom of the fourth page."

                                        nvl clear
                                        narr "{i}{b}Seven Year Old Victim of Hit-and-Run, Critical{/b}{/i}"
                                        narr "{i}{b}KUTSUTOCHI{/b} -- Not two months have passed, but misfortune had befallen upon a young girl once again.{w=2.0} Let Carnegie, aged seven, is in critical condition after becoming a victim of a hit-and-run incident yesterday morning.{w=2.0} She is currently being treated at Virgin Mother Medical Center.{/i}"
                                        narr "{i}Witnesses state that a red Montero -- apparently not noticing the poor child -- had hit her.{w=2.0} Its plate number, LCS-879, is registered to Ms. Carol Volante, the aerial acrobat who has finished second in the 2006 World Aerial Queens Tourney in Australia.{w=2.0} She is currently being reached for commentary.{/i}"
                                        narr "{i}(Jungo Kazuya -- 05/31/07){/i}"

                                        nvl clear
                                        narr "It's frightening to die in the early hours of the morning. It's not as comforting to know that she joined her parents in Heaven."
                                        narr "And that name..."
                                        narr "It was eight months ago. Carol Volante's plane crashed during her farewell performance.{w} Her engine croaked in the middle of her signature stunt."
                                        narr "Once it was revealed that the engine was rigged, an investigation took place and the authorities arrested one suspect.{w} The trial was the most sensational part of the entire case, prompting a media blackout the day following the verdict."

                                        nvl clear
                                        window hide

                                        "But that's not important.{w} We still haven't found anything or anyone resembling L.C. at all."

                                        iy1 "How is your search turning up?"
                                        ai2 "Only one of them is a male --{w=0.5} a rich bachelor currently residing in the United States.{w=1.0} The six females?{w=1.0} No criminal record as far as legalities are concerned."
                                        iy1 "I'm curious as to how you were able to dig up {i}that{/i} kind of information."
                                        ai2 "I have a cousin who is a Sergeant in the police force.{w=0.5} No, not the old geezer with Inspector E. My old buddy who comes to play NBA every Sunday."
                                        iy1 "We should be more wary of you, then.{w=1.0} Hmmmmmm..."

                                        "There are plenty more to check here. It's our luck that no one has joined us yet.{w} Maybe some of the patrons are having their lunch? It's fifteen minutes past twelve, after all."

                                        ai2 "I'm hungry..."
                                        iy1 "It's just a little over noon. We can have our lunch break at two or so.{w=1.0} {i}*sigh*{/i} {cps=25}I'm craving for that fried chicken and its crispylicious skin.{/cps}"
                                        is4 "Look!{w=1.0} This might ring a bell. Come here."

                                        "Inoue is holding a dusted photograph covered in plastic. I have seen the subject recently."

                                        if not parse_bin(i2a_periodicals,1):
                                            $ i2a_periodicals += 2

                                    "Sacred Heart Curse Killings":
                                        "There is another article here. This time, covering the last victim of the Sacred Heart Curse Killings."
                                        "It is still fresh in my memory, but the specific details I cannot recall."

                                        window show
                                        nvl clear
                                        narr "{i}{b}Tenth Mysterious Ritual Victim Surfaces{/b}{/i}"
                                        narr "{i}{b}SACRED HEART VILLAGE{/b} -- In a series of alleged curse killings starting two years ago, the body count has already reached ten as of yesterday morning.{w=2.0} Graduating HS student, Kugimiya \"Lienel\" Oizumi, sixteen, has been found dead by her mother at around 6 AM.{/i}"
                                        narr "{i}She was found hanging on her room's ceiling fan, her head literally sliced in half.{w=2.0} Her parents stated that they can no longer support their only child through college. This may have been a factor in her suspected suicide. Her friends believe otherwise.{/i}"
                                        narr "{i}Whether or not her case involves foul play is yet to be determined by the case's investigative team.{w=2.0} Neighbors reported no suspicious activity on the night of Oizumi's death.{/i}"
                                        narr "{i}Those who survived her wonder if everything is truly over.{/i}"
                                        narr "{i}(Akane Yuuichi -- 03/29/2013){/i}"

                                        nvl clear
                                        window hide

                                        "What follows is a short interview involving our alumna, Ikari Suzumoto."
                                        "While she -- to quote herself -- \"started\" this curse killing phenomenon, she is innocent of all charges.{w} The entire series of incidents must have alienated her in their village."
                                        "Regardless, there is nothing new to learn here. We have already discussed this two months ago."

                                        if not parse_bin(i2a_periodicals,2):
                                            $ i2a_periodicals += 4

                                    "<<< BACK":
                                        $ lock = 0

                        "Photographs":
                            $ lock = 1

                            while lock == 1 and (i2a_genreference not in [24, 25, 26, 28, 29, 30, 31] or i2a_periodicals not in [187, 191, 251, 255]):
                                menu:
                                    "Old MSCI":
                                        "This is an old photo of Maria St. Claire Institute. It is the graduating class of '04, the last batch before the name change in 2001."
                                        "Two of the teachers in these five photos -- Mrs. Kaida and Mrs. Ritsuko -- are currently advising in Fourth Year. Respectively, they advised IV-E and IV-C.{w} That's three cycles ago. It's impressive they're still on deck."
                                        "Their batch even has one pair of twins just like us!{w} In the individual class photos, one of the sisters belongs to Mrs. Kaida's class, the other in Mrs. Ritsuko's."
                                        "Other than that, there is nothing more to add. They just showed the MSCI of the past, no hexes and witches involved."

                                        if not parse_bin(i2a_periodicals,3):
                                            $ i2a_periodicals += 8

                                    "Missing child" if parse_bin(i2a_periodicals,1):
                                        "Inoue handed me the photo."
                                        "I recognize the subject. There are some text printed above below it."

                                        scene bg missingposter with dissolve

                                        "The same seven-year old girl -- Let Carnegie.{w} Things are getting weirder down the rabbit hole."

                                        iy1 "She was also a hit-and-run victim sometime after she was found, I read."
                                        is4 "Oh? How unlucky is she...{w=1.0} Rather, how irresponsible her parents must be to let these happen?"
                                        iy1 "They're dead, Inoue. Show some respect."

                                        scene bg library periodicals with dissolve
                                        "Still... What the hell did we just uncover?"

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
                                        if not parse_bin(i2a_circulation,3):
                                            iy1 "You were there at the time of Kyou's murder, right?"
                                            is4 "I'll never forget that."
                                            iy1 "Then you must also know what rhyme played while he was being immolated, too."
                                            is4 "A rhyme?{w=1.0} You mean nursery rhyme?{w=1.0} I can't remember. That part of my memory is still a haze."
                                            iy1 "It's part of L.C.'s M.O.{w=1.0} If we can pinpoint the exact rhyme, it might lead us somewhere."
                                            is4 "Sorry, Ichi. I don't know.{w=1.0} However, if you can hum the tune or show the lyrics to me, you might be able to jog my memory."

                                            "While that is another problem to set aside, there is one more question I have been meaning to ask."

                                            iy1 "Do you have a favorite nursery rhyme?"
                                            is4 "{cps=10}Hmmmmm...{/cps}{w=1.0} It's {i}Star Light, Star Bright.{/i}{w=1.0} Unpleasant given the present circumstances, but pleasant when I connect it to my childhood memories.{w=1.0} I remember it being played on {i}Barney{/i}."
                                            iy1 "Pft...{w=0.5} Pffffft...!{w=1.0} {cps=15}I love you...{w=0.5} You love me...{/cps}{w=1.5}{nw}"
                                            is4 "Yeah, shut up! Nobody watches that stuff anymore."
                                            iy1 "So, in case you die hearing that, then we know who the suspect is in advance?"
                                            is4 "Definitely!"

                                            "Someone here agrees with me even without a name drop.{w=2.0}{nw}"

                                            is4 "Though, I'll kill you first before you plan on killing me, buster!"
                                            iy1 "Whoa! That's too far over the line!{w=1.0} Easy... {i}*chuckle*{/i}"

                                        else:
                                            is4 "{i}*EXHALE*{/i}"
                                            iy1 "Are you sure you don't need medical assistance?"
                                            is4 "No need.{w=1.0} Give me some breathing space, will you?{w=1.0} If you have nothing new or important to say, please save it for another day."

                                            "We already know what nursery rhyme triggered her unpleasant memories. It is unadvisable to show it for a second time, else she chews my head off."

                                        if not parse_bin(i2a_periodicals,5):
                                            $ i2a_periodicals += 32

                                    "Au Clair De La Lune" if parse_bin(bonus_b1_g,0):
                                        iy1 "I'm impressed with how you applied your piano lessons to escape your cell.{w=1.0} To keep a French song in mind that's not {i}Frere Jacques{/i}? That's quite a feat."
                                        is4 "Hm.{w=0.5} Thank you.{w=1.0} If you would grab a chair and listen to my story, please."

                                        "There are no chairs to grab.{w} Instead, we sat across each other on one of the reading tables at the side."
                                        "Her fingers entwined under her chin with elbows touching the wood."

                                        scene bg livingroom with fade
                                        window show
                                        nvl clear
                                        narr "When I was two, my mother bought me a 16-key piano.{w} My parents loved to play during family gatherings, always bringing me along and letting me press random keys until I felt bubbles steaming out my head."
                                        narr "While my parents were away and my nanny asleep, I snuck up to our family piano and opened the music book.{w} Three-year old me understood the notes a bit and played them according to height. I didn't know where Base-C was at the time."
                                        narr "My nanny caught me and saved me from an otherwise terrible fall. Gave me a good scolding and told Mama and Papa later on.{w} They were mad when they found out, but ultimately decided to accentuate the positives."
                                        narr "I started to receive formal lessons at four.{w} The first song I mastered was,{w=0.5} indeed,{w=0.5} {i}Au Clair De La Lune{/i}. The lyrics are beautiful; so is the tune."

                                        nvl clear
                                        window hide

                                        scene bg library periodicals with fade
                                        is4 "Which makes L.C.'s knowledge of it rather bizarre. I never told anyone about it!"
                                        iy1 "It's a coincidence."
                                        is4 "It very well may be, but imagine if Kirisaki and I switched places.{w=1.0} It might kill our chances even more."
                                        is4 "So, it's not just a coincidence. He knows even the most obscure details of our lives.{w=1.0} Most of the things I saw were connected to me in some way, but that piano lock puzzle stands out."
                                        iy1 "Remind me to keep a mouth zipper ready and to never indulge in some dark secrets."

                                        if not parse_bin(i2a_periodicals,6):
                                            $ i2a_periodicals += 64

                                    "Let Carnegie" if parse_bin(i2a_periodicals,4):
                                        is4 "Alright. I went too far with that unlucky child comment.{w=1.0} I had no knowledge, or perhaps my moral compass is still misaligned."
                                        iy1 "Mhm?"
                                        is4 "Tell me more about the hit-and-run.{w=1.0} This Let Carnegie, what about her?"
                                        iy1 "That's all I can tell you. If you want more, let me fetch the article for a moment."

                                        "I took the dog-eared newspaper with said article and handed it to Inoue. She spent a few minutes over it."

                                        is4 "Ms. Volante's car had another driver during the incident. It was borrowed by one of her nieces for a joyride.{w=1.0} She even took responsibility and paid for the child's medical expenses."
                                        iy1 "Even burial?"
                                        is4 "None I can confirm."

                                        "Really?{w} I thought there is another side to the story --{w=2.0} that Ms. Volante's payment is actually hush money?"

                                        is4 "Last I've heard of Let's sisters was that they moved to Sacred Heart Village to start anew, though they continued attending classes in NSU."
                                        is4 "The first few months were difficult. One of them had to file for a Leave of Absence and underwent counseling following the tragedy."
                                        iy1 "NSU, huh?{w=1.0} What are their degree programs?"
                                        is4 "One of them graduated BS Nursing.{w=1.0} The other I'm unsure about."
                                        iy1 "How do you know that?"
                                        is4 "One of the nurses in the hospital I was confined in is a friend of hers.{w=1.0} When she found out I am an MSCI student, she mentioned it and asked if I plan to study in NSU."
                                        iy1 "Whatever happened to bedside manners?"
                                        is4 "Exactly.{w=1.0} Why that overwhelming trust to someone you barely know?"
                                        iy1 "Anything else?"
                                        is4 "I didn't bother asking any more. Tossed the topic aside as gossip."

                                        "Understandable.{w} Although the nurse was being nice, that does not entitle her to spill secrets about her friend's personal life. It's a mark of a traitor."

                                        if not parse_bin(i2a_periodicals,7):
                                            $ i2a_periodicals += 128

                                    "I'll be going back to research now.":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Move":
                    menu:
                        "Circulation" if parse_bin(areas,0):
                            scene bg library circulation with fade
                            $ current_area = 0

                        "General Reference" if parse_bin(areas,1):
                            scene bg library genreference with fade
                            $ current_area = 1
                            
                        "<<< BACK":
                            pass

    scene black with fade
    centered "{color=#5decff}--INVESTIGATION COMPLETE--{/color}"
    scene bg library circulation with fade

    window show
    nvl clear
    narr "We convened at the circulation section to discuss our findings."
    narr "It was already two o' clock, way past lunch time.{w} At least the restaurant will not be as congested."
    narr "Much to my embarrassment, I exchanged the Mother Goose Rhymes for my ID. This will be one hell of a story at dinnertime."

    nvl clear
    window hide

    ai2 "From what we gathered, it seems L.C. is not from Kutsutochi.{w=1.0} {cps=30}At least, not in the way we think.{/cps}"
    ys6 "That's true.{w=1.0} The closest lead we have is the sisters of Let Carnegie."
    ys6 "But who are they?{w=1.0} The papers never mentioned their names."
    ai2 "Still...{w=1.0} there is a possibility..."
    iy1 "..."
    ai2 "...of L.C. orchestrating the crimes outside Kutsutochi.{w=1.0} Come on, guys! You thought I would mention a deceased child somehow rising from the dead and started the cursed killings to ward off boredom?"
    iy1 "You mean that rich bachelor overseas? What does he have to do with us or those in Sacred Heart Academy?"
    ai2 "I'm not sure. We don't have enough information."
    is4 "It's a shame we aren't allowed to take snapshots. Ichirou and I found some photographs wourth referencing later on."
    ys6 "Like the ones showcasing the younger versions of our advisers? {i}*chuckle*{/i}{w=1.0} Might be a handy tactic to get on their good side later on.s"

    "It won't be easy to make Mrs. Ritsuko speak, though.{w} If Presidential Powers permit -- damn, Sumiko is rubbing off on me -- she might spill some juicy information."
    "Drop the idea.{w} She's either going to reprimand me for merely asking, or she's going to tell valueless gossip just to spite me."
    "{i}*GROWL*{/i}"

    ai2 "Uggggghhh... The three pieces of bread have done their job."
    iy1 "Let's go grab some chicken at the bee's. Our brains need some nourishing first."
    ai2 "So, let's go!"
    iy1 "Even now?"
    librarian "Shhhhhhhh!"
    ys6 "Pardon us, ma'am."
    ai2 "Come on, slowpokes! Pick up the pace!"

    "At the end of the day, it is always food, isn't it?"
    return

label ch03_07B_innocent:
    if path_b1 == 0:
        $ path_b1 = 1

    scene black with fade
    "{color=#5decff}AUGUST 11, 2013 - 1000H{/color}"
    scene bg school gate with fade

    window show
    nvl clear
    narr "Sometime after I proposed to Hikaru and Sumiko that the four of us meet today, Sayo found a compromise."
    narr "We decided to postpone the trip to Sacred Heart Village to a later date.{w} Instead, we agreed to pay the CRPD a visit and consult Emmerich about the case. He would be waiting for us at around lunchtime."
    narr "Luckily, our itinerary is near the church where the Yamamotos are congregating, confirming our trip even further."
    narr "Thus, the four of us met in front of MSCI.{w} We commuted together."

    scene bg intersection with dissolve
    nvl clear
    narr "You are obligated to squeeze your nostrils and mouth with your hand.{w} Even if the Clean Air Act is in effect, there exist drivers whose vehicles remain belching black smoke. How is this so?{w} A thick wad of oil."
    narr "There are barely any congestions since it's Sunday.{w} Try waiting at a stop on weekdays and see if your patience runs thin. Don't bother asking how many people traffic jams have inconvenienced during rush hours."
    narr "And then there is the faulty transit.{w} It used to be good...{w=1.0} ten years ago (though I was out of the country, so I'm not certain). When a breakdown happens, kiss that diligence award goodbye."
    narr "Thankfully, the third mishap was not a problem.{w} The CRPD was just one station away from where we boarded."

    scene bg policedepartment outside with dissolve
    nvl clear
    narr "At quarter to eleven, we were walking towards the civilian entrance of the building."
    narr "The CRPD is shown on camera whenever a politician or high-profile criminal is awaiting trial{w=1.0} or when the police force themselves are facing an issue."
    narr "The actual police department looks grandiose, the front garden's floral design carefully maintained."

    scene bg policedepartment lobby with dissolve
    narr "Once inside, expectations of simpleness are, to one's own mileage, subverted.{w} The floors are regularly waxed, the chestnut colors pleasing to the eyes. It's like LAPD."

    nvl clear
    window hide

    hy10 "Wow! I haven't been in places like this. Sadly, it doesn't look like anything what Hollywood shows."
    mh8 "Seriously? This isn't LAPD. {i}*chuckles*{/i}{w=1.0} And this also houses a police academy. Who would want prestige over practical use, anyway?"
    hy10 "Yeah, but point is, this interior looks aesthetic."
    sr5 "If you two are done talking, then we should proceed with our appointment.{w=1.0} We may be too early, but the clock is ticking."
    st3 "Alright. Let's do whatever we came here for."

    scene black with fade
    centered "{color=#bd0000}--INVESTIGATION START--{/color}"
    scene bg policedepartment lobby with fade

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

                            while lock == 1 and not (parse_bin(i2b_archives,2)):
                                if not parse_bin(i2b_reception,0):
                                    "The receptionist is working on his computer. He has an aluminum-wrapped box beside the mouse.{w} We have arrived well before the officers take a break."
                                    "He seems nice, if that grumpy demeanor betrays expectations."

                                    sr5 "Good morning, officer. We are students from Maria St. Claire Institute."
                                    officer "Good morning, kids.{w=1.0} We usually don't receive high school students as visitors, so this is quite surprising. Unless you want to be a cadet in the future, that is. {i}*chuckle*{/i}"
                                    officer "How may I be of service?"

                                menu:
                                    "Inspector Emmerich":
                                        sr5 "We are here on an appointment."
                                        officer "You know, I seem to recognize your voice, ma'am. Did you call here last month?"
                                        sr5 "That is correct. I am Sayo Ronoroa."
                                        officer "Pleasure to meet you.{w=1.0} I take it you have a meeting with Inspector Emmerich?"
                                        sr5 "Exactly. Is he busy?"
                                        officer "He should be finished with his meeting right about now. I have orders to let you in should you arrive before noon."
                                        officer "Just go upstairs to the second floor and head into the east wing offices.{w=1.0} You'll find Harold there."
                                        mh8 "Thank you. Don't we get a visitor's pass?"
                                        officer "Sharp mind!{w=1.0} Your School IDs, please.{w=2.0} Thank you."

                                        "Four IDs in exchange for four Visitor's passes. We were instructed to wear them inside the premises and to return them once we are done."

                                        mh8 "Okay. Let's just hope Inspector E. is really free to talk to now."

                                        if not parse_bin(i2b_reception,0):
                                            $ i2b_reception += 1
                                            $ areas += 2

                                    "<<< BACK":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Talk":
                    menu:
                        "Sayo Ronoroa":
                            $ lock = 1

                            while lock == 1 and not (parse_bin(i2b_archives,2)):
                                menu:
                                    "What to look for?":
                                        st3 "So... what are we here for, again?"
                                        mh8 "You forgot already?!{w=1.5} To meet with Inspector E. and ask him about the Sacred Heart Curse Killings. He was involved in that case, remember?"
                                        sr5 "It wouldn't suffice if we merely listen to his story. We are here to dig up the facts ourselves.{w=2.0} I have a feeling we can uncover a hidden link between Sacred Heart and MSCI that may also lead us to L.C."
                                        mh8 "But what do we look for, exactly?"
                                        sr5 "I'm more concerned about how this Curse Killing trend started one year ago.{w=1.0} If Emmerich can grant us access to the case files somehow, we might have exclusive details on our hands soon."
                                        mh8 "And to ask about Hiroshi's autopsy report, if that's possible."
                                        sr5 "It's illegal to outsource these kinds of documents to civilians, Miyu.{w=1.0} Besides, I bet those contain jargons only medical practitioners and law enforcement officers can decode."
                                        mh8 "Then we look for the \"next best thing,\" right?"
                                        sr5 "We are expecting notes. Heaps of notes, if we have that much time."
                                        st3 "I brought a scratch notebook with me."
                                        mh8 "And I thought I'm the only \"Always Prepared\" guy in our group...{w=1.0} and I'm not even a Boy Scout!"

                                        if not parse_bin(i2b_reception,1):
                                            $ i2b_reception += 2

                                    "L.C.'s challenge":
                                        mh8 "Sayo, I'm not trying to be offensive here, but consider this scenario."
                                        mh8 "Say you didn't win the SC Presidency. Would Ayumi be L.C.'s primary target instead?"
                                        sr5 "No."
                                        mh8 "Why so?"
                                        sr5 "As one of the Ten Little Indians, maybe.{w=1.0} Primary target, it's hard to say.{w=1.0} Maybe the lineup would be different.{w=1.0} Maybe it would be the same sans one of us."
                                        mh8 "And who would that be?"
                                        sr5 "Hopefully, me, but it's already established otherwise."
                                        mh8 "I interpreted L.C.'s challenge as such.{w=1.0} You are the Student Council President, even going so far as to emphasize that bit."
                                        sr5 "If anything, I am sure my position is trivial to the motive. It would take months of planning to pull it off successfully."
                                        sr5 "{cps=30}And so far,{w=0.5} the results are positive.{/cps}"
                                        mh8 "Hmmmmm...{w=2.0} Why the need to capitalize on a sensational case? Doesn't that convey how much of a bastard the supposed gentleman is?"
                                        sr5 "Your language, please."
                                        mh8 "Sorry."
                                        sr5 "It's what L.C. wants us to think.{w=1.0} They even pinned their identity on me by circumstance. What do I know about fickle-minded freks? You don't get to see those everyday."
                                        sr5 "I'm not entitled to anything, either.{w=2.0} I'm just another player in a deadly game."

                                        if not parse_bin(i2b_reception,2):
                                            $ i2b_reception += 4

                                    "Inoue's memories" if parse_bin(bonus_b1_i,1):
                                        mh8 "Sayo-chan, do you remember when you talked to me the day before Inoue was rescued?"
                                        sr5 "All of it."
                                        mh8 "To be accused of a threatening prank call is one thing. To be assaulted is another.{w=1.0} Do they, Inoue or the Shinozakis in general, have anything against you?"
                                        sr5 "For what? They'll gain nothing from harassing me.{w=1.0} Keep in mind, even I doubt Inoue's credibility despite the harrowing experiences she suffered."
                                        mh8 "Is it because of the supernatural details? We can explain them."
                                        sr5 "You arrived before me, Mi-kun. Come on. Use that \"particular set of skills\" of yours."

                                        centered "{color=#808080}{cps=25}There are two major changes to Inoue's demeanor during that time.{w=3.0}\nThe first is when I, Sumiko, and Akira arrived.{w=2.0}\nThe second -- more significant than the first -- is when Sayo popped up out of nowhere.{/cps}{/color}"

                                        mh8 "She made little sense as her own story went along, even less as more spectators arrived at the scene."
                                        mh8 "L.C.'s voice she described as masculine.{w=1.0} Why would she accuse you, a female?"
                                        sr5 "I can't say the same theory I have with L.C.'s voice during the mock exams. Keep in mind that {i}we never heard L.C. speak outside of that{/i}."
                                        mh8 "Isn't that a given? Why we're split up in the first place?"
                                        sr5 "Is it because,{w=0.5} perhaps,{w=0.5} of words we are not aware were spoken?{w=1.0} Or events that happened outside our knowledge?"
                                        sr5 "Do you remember one reason why a magic trick is effective?{w=1.0} How did L.C. manipulate us to our disadvantage?"

                                        "My eyes fell upon my arm."

                                        scene bg school fields evening with fade
                                        "She gave that short lecture while we were playing UNO.{w} Sayo deliberately set herself up to get a ketchup{w=1.0} and pass it to someone else."

                                        sr5 "The effectiveness of a magic trick lies on several key factors, such as dexterity and distraction.{w=1.5} In a game like this, the first is more important. If the second is employed more often, the effect is weakened.{w=4.0}{nw}"
                                        sr5 "You ask,{w=1.0} how did it work?{w=3.0}{nw}"
                                        sr5 "All of us decided to guard the current player as he makes his move to avoid being the top hand should a declaration happen.{w=5.0}{nw}"
                                        sr5 "When it did happen, from then on, you started to watch the {i}player{/i} instead of the {i}hand{/i}."
                                        sr5 "Ironically, a blind spot is made. You all fell for a simple sleight-of-hand you could have spotted easily."

                                        scene bg policedepartment lobby with fade
                                        "I just realized something."

                                        mh8 "{cps=30}Sayo-chan,{w=1.0} are you a good poker player or are you a magician?{/cps}"

                                        "She winked and placed a finger on her lips."

                                        sr5 "A magician doesn't reveal her secrets.{w=1.0} It is part of the creed. {i}*giggle*{/i}"
                                        sr5 "And if you're willing to play poker with me, let me know."
                                        mh8 "Maybe in chess I have a better chance against you."
                                        sr5 "Your choice.{w=1.0} When all of this is over, I'll be willing to teach you."
                                        sr5 "{cps=20}I'll be waiting...{/cps}"

                                        "Why not during?"

                                        if not parse_bin(i2b_reception,3):
                                            $ i2b_reception += 8

                                    "Let's get back to the investigation.":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Move" if areas > 1:
                    menu:
                        "Office" if parse_bin(areas,1):
                            scene bg policedepartment office with fade
                            $ current_area = 1

                        "Archives" if parse_bin(areas,2):
                            if parse_bin(visited,2):
                                scene bg policedepartment study with fade
                            $ current_area = 2
                            
                        "<<< BACK":
                            pass

        elif current_area == 1: # Office
            if not parse_bin(visited,1):
                "After passing through the next inspection, we walked up the stairs in the succeeding corridor."
                "From the landing, a glass door can be seen. Beside it is a signage that reads:"
                "{i}Office 2A - A to F{/i}"
                "This is the place.{w=1.0} We swiped our Visitor's ID into the electronic card reader."
                "The entire office space is mellow, aside from a few phone rings and whispers from the workers."
                "One of the junior officers emerged from the right.{w=1.0} When he saw us, he stopped and turned to yell."

                officer "Hey, Harold! You got some visitors here."

                "I recognize him. He's one of the investigators on Inspector Emmerich's team."

                officer "Follow me, kids."

                "He led us through the maze of cubicles,{w=1.0} ending at the one where Emmerich and his superior are conversing."

                p_emm "Good morning!{w=1.0} I didn't expect you to arrive before noon."

                "The senior officer extended his hand."

                p_dei "Ms. Ronoroa and your friends, it seems?{w=1.0} What business do you have with this rookie?"
                sr5 "Matters that concern us most, Sergeant."
                p_dei "Well, it is unusual for witnesses to approach us on their own.{w=1.0} {i}We{/i} come to them. {i}*chuckle*{/i}"
                p_emm "They wished to know more about the ongoing investigation, Sarge, as well as details about MH-0809."
                st3 "MH-0809?{w=1.0} Is that the series of murders at Sacred Heart Village?"
                p_dei "Indeed.{w=1.0} But let me tell you something, sonny.{w=1.5} We're not obligated to give away information to those not tied with the case,{w=0.5} especially one as sensitive as that."
                st3 "We understand. Do we sign a Non-Disclosure Agreement?"
                p_dei "Not without my approval.{w=1.0} If you like, you can go up to Sacred Heart Village and ask the locals themselves. Good luck with making them talk, though."
                mh8 "Well, that's a shame.{w=1.0} In that case, we --{nw}"
                p_dei "If,{w=0.5} however,{w=0.5} you can establish a connection MSCI and SHA's murder cases, then I can grant you {i}temporary privileges{/i} effective only today."
                mh8 "That would do, Sarge. Thank you."
                p_dei "I'll be staying awhile here, if you don't mind. Go ahead and entertain your guests, Harold."

                "He walked to the side and lounged around one of the chairs, whistling the tune of a noir mystery film."

                p_emm "He was the lead investigator of that case. Gotten tired of dealing with people over it."
                hy10 "This is your first case, Inspector? That's a pretty big leap from your previous one."
                p_emm "Sure is. I can thank two people for convincing me to pursue this job:{w=1.0} Sarge and one other person."
                p_dei "Awwwww... Blush. You're gonna hate this job soon enough, Harold! {i}*chuckle*{/i}"
                hy10 "Who is this other person?"
                p_emm "Someone the same age as you. Calls herself \"Little Miss Detective.\""
                hy10 "This isn't a de-aged woman? You mean a child or a teenager helped you out? Must be a prodigy!"
                p_emm "She's a nuisance.{w=1.0} {i}Was{/i} a nuisance, after all she's done.{w=1.5} Can't really blame her for helping out with the case, though especially if your best friend is involved."
                p_emm "But enough sob stories. You'll know more about it one of these days.{w=1.0} What do you want to know?"

                $ visited += 2

            if i2b_office == 7 and not parse_bin(areas,2):
                p_dei "The thing in the hands!{w=1.0} Harold, you remember those?"
                p_emm "It's not that important, Sarge. We already cleared Ms. Suzumoto of the charges against her."

                "Now, that is a curious detail.{w} It reminds me of a certain {color=#bd0000}{i}thing{/i}{/color} that may help us move forward."

                mh8 "A symbol?{w=1.5} A name?{w=1.5} {cps=15}A {color=#bd0000}{i}pair of numbers{/i}{/color}?{/cps}"

                "{i}*SNAP*{/i}"

                p_dei "Bingo!{w=1.0} Gold star for you, young lad."

                "The four of us looked each other in the eye, altogether realizing what that confirmation meant."

                sr5 "One of the night guards found Ikari-san in the middle of a ritual. On her palms were a pair of numbers carved not unlike those on Kyou and Hiroshi's hands."
                p_emm "But the victims had no traces of such carvings."
                sr5 "That's true.{w=0.5} However, the circumstances surrounding the ritual and The Correspondent's coverage of her reveal a significant connection:{w=1.5} Why were the Sacred Heart Curse Killings referred to as such?"
                mh8 "Maybe Ikari Suzumoto conjured up a malevolent spirit that went on to terrorize Sacred Heart Academy, ten of its students the victims."
                mh8 "It came as a spirit, only gaining a corporeal form whenever the time to kill each victim is nearing; hence, why no suspect was ever found."
                p_emm "Seriously?!{w=1.0} That's the best explanation you can come up with?"
                mh8 "From a supernatural perspective, yes."
                sr5 "There is one more thing you might have overlooked.{w=1.0} The series of crimes took place in a span of ten months -- one victim each on the latter half."
                hy10 "The letters we received are proof, assuming they are from the culprit themselves.{w=1.0} One of these said something along the lines of, {i}Every month is divided into two halves, the latter where the amusement is.{/i}"
                st3 "Kyou Kirisaki was killed sometime between the 16th and the 25th;{w=0.5} Hiroshi Kano on the 19th.{w=1.0} It is consistent with what the letter said."
                mh8 "If nothing convinces you further, we don't know what will. I'd rather we grope in the dark together rather than watch eight more people die until the end of the school year."
                mh8 "And you wouldn't want that to happen, would you, Inspector?"
                p_emm "..."

                "{i}*tap*{w=0.5} *tap*{w=0.5} *tap*{w=0.5} *tap*{/i}{w=2.0}{nw}"

                p_emm "Sarge...{w=1.5}{nw}"

                "{i}*tap*{w=0.5} *tap*{w=0.5} *tap*{w=0.5} {b}*tap*{/b}{/i}{w=2.0}{nw}"

                p_dei "You got spunk, kiddo.{w=1.0} A civilian wouldn't dare bend the rules against a cop just to meet his own ends."
                p_dei "But I'll let it slide this time. {i}*chuckle*{/i}{w=1.0} It is just like the olden days, Harold --{w=0.5} the type of things that make the Holidays exciting."
                p_emm "I agree, sir. The four of them gives off an unusual aura. Combined, they could match {i}her{/i} influence and competence."
                p_dei "Alright! You earned your one-time ticket.{w=1.0} Follow me down to the Archives when you're ready. Emmerich, hold the fort while I'm gone."
                p_emm "Roger that."
                p_emm "Be sure to come back afterwards, kids.{w=1.0} I have something to show you.{w=0.5} Just give me time to prepare it."
                sr5 "Thank you, Inspector."
                p_dei "Shall we?"

                $ areas += 4

            menu:
                "Talk":
                    menu:
                        "Inspector Emmerich":
                            $ lock = 1

                            while lock == 1 and not (parse_bin(i2b_archives,2)):
                                menu:
                                    "Purpose of visit":
                                        sr5 "I discussed this with you over the phone, Inspector. Have you readied the case files as requested?"
                                        p_emm "You've heard the Sergeant. I can't just let you down without his blessing.{w=1.0} And policies.{w=0.5} These are sensitive information we would be potentially releasing to outsiders."
                                        mh8 "However, if we are to press for information about our current case, will that be valid? Even if we're suspects, Inspector?"
                                        p_emm "{i}Persons of interest,{/i} Miyu. There is nothing against any of you--{w=2.0} including you, Sayo."
                                        sr5 "I figured."
                                        st3 "Hmmmmm...{w=1.0} Is there something you're not telling us?"
                                        sr5 "No need to worry. It's dubious evidence against me by Inoue's family."
                                        p_emm "We have laws regarding use of such evidence. That doesn't mean we'll junk it, in case it may become significant later on."
                                        mh8 "In any case, that's good to hear. What we should look for is circumstantial yet solid evidence.{w=1.0} It's 2013. There are a lot of voice modulating apps available."
                                        hy10 "So, L.C. might have used one themselves?"
                                        mh8 "Don't they all when people want to mask their own voices?"
                                        p_emm "That's one of the angles we're looking into. It has little impact as of now, I'm afraid."

                                        if not parse_bin(i2b_office,0):
                                            $ i2b_office += 1

                                        if i2b_office == 7 and not parse_bin(areas,2):
                                            $ lock = 0

                                    "Hiroshi's case":
                                        mh8 "How did your weekend investigations go?"
                                        p_emm "You won't like what we surmised after interviewing all the night watchmen at MSCI.{w=1.0} It's more or less confirmed --{w=1.5} {cps=25}the \"phantom\" is in your midst.{/cps}"
                                        mh8 "Did you find traces of L.C. inside and around the crime scene?"
                                        p_emm "If any of you is the culprit, let me congratulate you for doing a clean job!"
                                        hy10 "Hey! I was nowhere near the campus during the time."
                                        p_emm "I'm kidding!"
                                        p_emm "You know this already. The only way we can confirm who entered that office is gone thanks to the power outage."
                                        mh8 "How about the murder weapon?"
                                        p_emm "By school policy, you are not allowed to bring a deadly weapon with you. The cuts on his fingers are too clean to have been made with school supplies."
                                        mh8 "Then that makes a cutter insufficient. The blade is too brittle to surge through a bone.{w=1.0} If it was used, then Hiroshi's throat should have been slit."
                                        p_emm "Correct.{w=1.0} What {i}was{/i} used is this."

                                        "From his drawer, he produced a paring knife labeled inside a plastic bag."

                                        mh8 "There are blood patches between the blade and the handle. Not so clean of a job, if you ask me.{w=1.0} What about fingerprints?"
                                        p_emm "The suspect was using a glove. It had been disposed as well."
                                        mh8 "Hmmmmm..."
                                        p_emm "Can you think of anyone with a motive?"
                                        sr5 "Even if I had the perfect chance, I don't. That's not an admission of guilt, though."

                                        "We responded similarly. None of us hated Hiroshi so much as to give him a brutal end."

                                        if not parse_bin(i2b_office,1):
                                            $ i2b_office += 2

                                        if i2b_office == 7 and not parse_bin(areas,2):
                                            $ lock = 0

                                    "Cursed killings?":
                                        mh8 "If you must know, Inspector, I'm a fan of crime procedurals and supernatural occurrences."
                                        p_emm "That's good to hear!{w=1.0} The latter I'm not so sure about..."
                                        mh8 "There is this conspiracy touting the Sacred Heart Village murders as \"Curse Killings.\"{w=1.5} I'm curious. Was there a theme the killer was following or was it truly the case?"

                                        "Emmerich turned to his superior.{w=1.0} He raised his hands in response, unsure of what to answer.{w=1.0} However, he had this to say."

                                        p_dei "More than half of the deaths are impossible."
                                        p_dei "The murders are said to be related to Ms. Ikari Suzumoto in some way.{w=2.0} But it's just hearsay. The locals always blame it on ghosts when there's a loon going around picking off students from the same high school."
                                        p_emm "It means while all the methods of murder are possible, which I can attest to, some of the murders are not possible given each circumstance.{w=1.5} {cps=25}Did we miss anything?{/cps}"

                                        "{cps=20}That was not helpful.{w=1.0} At all.{/cps}"

                                        if not parse_bin(i2b_office,2):
                                            $ i2b_office += 4

                                        if i2b_office == 7 and not parse_bin(areas,2):
                                            $ lock = 0

                                    "We'll get back to you later, Inspector.":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Move":
                    menu:
                        "Reception Area" if parse_bin(areas,0):
                            scene bg policedepartment lobby with fade
                            $ current_area = 0

                        "Archives" if parse_bin(areas,2):
                            if parse_bin(visited,2):
                                scene bg policedepartment study with fade
                            $ current_area = 2
                            
                        "<<< BACK":
                            pass

        elif current_area == 2: # Archives
            if not parse_bin(visited,2):
                scene bg elevator with fade
                p_dei "Tell me somethin'.{w=0.5} What are you hoping to take away from this?"
                sr5 "We desire to understand the nature of these mysterious phenomena.{w=1.0} It is rare for a serial killer to operate in this country, even weirder when the M.O. crosses into the supernatural."
                p_dei "Too many eyes watching the streets, that is.{w=1.0} Gotta admit, I had the same thoughts as you. But I held it in since it sounded too ridiculous to be true."

                window show
                nvl clear
                narr "Floor B1."
                narr "The elevator doors opened to a familiar hallway.{w} To the left are the interrogation rooms. To the right a few more doors farther down is a door labeled, \"Archives.\""
                narr "Sarge scanned his ID on the reader and let us inside."

                scene bg policedepartment study with dissolve
                nvl clear
                narr "The room resembled a library, the bookshelves filled with compilations of old cases and a few legal books."
                narr "The first area we were in is a reading room, two long tables with six chairs each.{w} The small door across leads into the archives proper. The locked door on the right leads into the Evidence Room."
                narr "Sarge opened the air conditioner and disappeared into the shelves.{w} He returned with a thick book -- coded {i}MH-0809{/i}, Volume 1 (Rikiyama to Shibuya)."

                nvl clear
                window hide

                p_dei "This is a long read, kids.{w=1.0} {i}*EXHALE*{/i} I suggest you focus on one or two victims for now. If you can skim this all in one sitting, why not?"
                mh8 "Thank you, Sarge. We can handle things from here."
                p_dei "Okay. Handle the pages carefully now."
                p_dei "When you're done or if you have any questions, use that walkie-talkie over there and give me a call. I'll leave my frequency with one of you."

                "He scribbled on his notepad and tore the page, handing it over to Sayo."
                "{i}*BUZZ* *BUZZ*{/i}"

                sr5 "Testing broadcast. One, two, three. Over."
                p_dei "Message received. Out."
                p_dei "You sure you kids don't wanna stop by the canteen? It's almost lunchtime."
                mh8 "No need, sir. We already ate before coming here."
                p_dei "Sure, huh? You aren't allowed to eat crackers here.{w=1.0} Remember the guy at the reception?{w=0.5} He's your guardian angel for this afternoon."

                "He turned to the CCTV camera mounted on one of the corners and gave a goofy salute before walking to the door."

                p_dei "See you in a few hours, kids.{w=1.0} Wish you luck!"

                "And he left us alone. Just the four of us and one thick book of photocopied reports."

                $ areas -= 2
                $ visited += 4

            menu:
                "Examine":
                    menu:
                        "Old Case Files ({i}MH-0809{/i})":
                            $ lock = 1

                            while lock == 1 and not (parse_bin(i2b_archives,2)):
                                menu:
                                    "Fuuko Rikiyama":
                                        if not parse_bin(i2b_archives,0):
                                            window show
                                            nvl clear
                                            narr "There are plenty of starting points in this book -- the first to the fifth victim."
                                            narr "However, for maximum comprehension, we decided to start with Fuuko Rikiyama."
                                            narr "Fuuko Rikiyama -- Female; died on June 28, 2012 at the age of 15. Attached to the page following the victim's personal details is an article from The Correspondent."

                                            nvl clear
                                            narr "{i}{b}Fire at Sacred Heart Academy: Accident or Arson?{/b}{/i}"
                                            narr "{i}{b}SACRED HEART VILLAGE{/b} -- A fire broke out yesterday evening at the Sacred Heart Academy, reaching second alarm before officials declared \"Fire Out.\"{/i}"
                                            narr "{i}The few staff members who were there were already packing up when the fire alarm sounded at 7:00 PM. Nearby villagers have contacted emergency services shortly afterwards.{/i}"
                                            narr "{i}Investigators traced the cause to faulty electrical wiring, originating from a broken power box inside the second floor computer laboratory. Though ready to label the incident as an accident, authorities were shocked to find a dead body hidden in one of the vents.{/i}"

                                            nvl clear
                                            narr "{i}The victim was a Fourth Year student named Fuuko Rikiyama, cause of death yet to be determined. The Regional Police District has decided to withhold details surrounding the victim's death until further information is confirmed.{/i}"
                                            narr "{i}So now, the question remains. Was the fire at Sacred Heart Academy a simple electrical mishap, or was it an antecedent to the victim's death as some have speculated?{/i}"
                                            narr "{i}(Akane Yuuichi -- 06/29/12){/i}"

                                            nvl clear
                                            window hide

                                            mh8 "Burns cut deeper than knives or strangulation if the fire is used as a cover-up. Usually, most of these cases are determined to be foul play."
                                            sr5 "A fire...{w=1.0} I forgot such an event occurred. Fuuko Rikiyama's murder overshadowed it."

                                            window show
                                            nvl clear
                                            narr "The following pages contained reports and photographs of the crime scene. Among these is the autopsy report hinted at in the article."
                                            narr "What stumped the good old Sergeant?{w} A corpse hidden from view is a dead giveaway."
                                            narr "The questions vastly outnumber the answers in this mystery.{w} If only someone has an accurate account of the events {i}before the fire{/i}."

                                            nvl clear
                                            window hide

                                            call ch03_07B1_rikiyama

                                            scene bg policedepartment study with fade
                                            "{color=#5decff}AUGUST 11, 2013 - 1330H{/color}"

                                            "Stunned.{w=1.5} I stopped myself from saying any more."

                                            sr5 "Most of the evidence supports your theory, Miyu. However, there are a lot of contestable points we picked up."
                                            mh8 "I know. A few details I mentioned just clicked into the story as I went along."
                                            hy10 "Oh! I get it.{w=1.0} Some parts of Inoue's story are there."
                                            mh8 "{cps=25}Waking up dazed and stupefied,{w=1.0} seeing one other person in the room.{w=1.0} What follows is the kiss of death...{/cps}{w=1.5} {cps=15}and fire...{/cps}"
                                            mh8 "The strangulation.{w=1.0} The reports imply Rikiyama's injury was self-inflicted. What she experienced mirrors that of Inoue -- more than half of it, at least."
                                            hy10 "She didn't mention anything of the sort. You might be mixing up the details."
                                            mh8 "But {i}I{/i} saw it. It was when she discovered the crime scene.{w=1.0} She was clutching her neck as if someone had just choked her unconscious."

                                            "{i}*tap* *tap* *tap*{/i}"

                                            st3 "What you just said before that strangulation bit. Is that solidification of her self-incrimination?"
                                            mh8 "Only if the killer's side is considered.{w=1.0} The strangulation itself parallels that of the victim.{w=2.0} If she {i}was{/i} the killer, then that means we found a loophole in Yoshiro's logic."
                                            sr5 "To perform a crime so grand, one must have the motive, the resources, and the mental capacity.{w=1.0} There is your problem. Inoue has no valid motive."
                                            sr5 "If she didn't have one for Kyou...{w=1.0} {cps=15}then...{/cps}{w=2.0} {cps=25}that means she did it to pin the blame on me?{/cps}{w=1.5} {cps=2.0}That makes no sense...{/cps}"
                                            hy10 "No one has an answer. Don't know what Inoue has been up to outside of our casual meetings."
                                            st3 "In any case, this should be enough for now. Let me just note every bullet point from this case file and from Miyu's theory."

                                            "After another fifteen minutes, he finished. Sayo went to the bookshelves and returned the case file."
                                            "It's almost two o' clock. Sarge should already be finished with his meal."

                                        else:
                                            "What we have right now should be enough. Let us study the remaining victims sometime in the future."

                                        if not parse_bin(i2b_archives,0):
                                            $ i2b_archives += 1

                                    "Rika Suzumiya" if (parse_bin(i2b_archives,0) and parse_bin(bonus_b1_g,1)):
                                        if not parse_bin(i2b_archives,1):
                                            scene bg policedepartment archives with fade
                                            "I followed Sayo to the case file archives. Our eyes met just as she turned to leave."

                                            sr5 "Have you contacted the Sergeant yet?"
                                            mh8 "No. There's something else that crossed my mind.{w=1.0} If you don't mind giving the case files another look..."
                                            sr5 "What is it about?"
                                            mh8 "Inoue's life was endangered even before encountering Kirisaki.{w=1.0} She mentioned something about hearing voices before being thrown headfirst into a pool."
                                            sr5 "Point being?"
                                            mh8 "Do you think with the similarity we established earlier with Rikiyama's case, we can connect that event to another Sacred Heart victim?"
                                            sr5 "Hang on. Let me get the second volume."

                                            "The second volume of MH-0809 was slightly thicker by a few pages. This one contained reports about the sixth to tenth victims."

                                            sr5 "This is the one."
                                            mh8 "Rika Suzumiya; Female, aged 16 at time of death.{w=1.0} Dead on arrival when paramedics tried to save her."
                                            mh8 "One can consider this girl careless allowing herself alone at sea.{w=1.0} Dead men tell no tales. Pardon."
                                            sr5 "That's the major difference.{w=0.5} Inoue was in an enclosed space where the depth is measurable. Suzumiya was at the beach."
                                            sr5 "To be fair, both were helpless against...{w=1.0} something."
                                            mh8 "She must be a swimmer. That {i}something{/i} should be powerful enough to hold her down if that was the case."
                                            sr5 "No evidence indicating that."
                                            mh8 "About that deal with Domina Shibuya, what do the papers say?"
                                            sr5 "The opinion surrounding Suzumiya's death was and is still divided, especially since she was the prime suspect of Shibuya's murder.{w=1.0} Some say it was conscience; others, revenge."
                                            mh8 "But she was alone on her yacht and far from the shore.{w=1.0} The only way she could be \"attacked\" is through indirect means --{w=1.5} drugs."
                                            sr5 "Agreed, yet the autopsy reports reveal otherwise.{w=1.0} The immediate surroundings should have been contaminated with drugs. No reports about that either."
                                            mh8 "Inoue should have been subjected to the same ordeal, body conditions and all."
                                            sr5 "Although, she isn't a swimmer. I would not put it past her if she was flailing around struggling for air in that pool."
                                            mh8 "I see..."
                                            sr5 "Are we done here?"

                                            scene bg policedepartment study with fade
                                            "I nodded and returned the case files to the shelf, after which we returned to the reading room."

                                        else:
                                            sr5 "Mi-kun, where are you going?"
                                            mh8 "Something else has crossed my mind.{w=0.5} I --"
                                            hy10 "We don't have much time. I'll be running late for our congregation."
                                            sr5 "Let's contact the Sergeant now if you don't have any more queries. We don't want to keep Hikaru waiting."
                                            mh8 "Did I miss anything else?"

                                        if not parse_bin(i2b_archives,1):
                                            $ i2b_archives += 2

                                    "<<< BACK":
                                        $ lock = 0

                        "Walkie-talkie":
                            $ lock = 1

                            while lock == 1 and not (parse_bin(i2b_archives,2)):
                                menu:
                                    "Contact Sarge":
                                        if not (parse_bin(i2b_archives,0) or parse_bin(i2b_archives,5)):
                                            "I held the frequency close to my face as I configured the portable radio."
                                            "{i}*BUZZ* *BUZZ*{/i}"

                                            mh8 "Sarge?"
                                            p_dei "{color=#808080}Oi! {i}*munch*{w=0.25} *munch*{w=0.25} *munch*{w=0.5}{/i} Need something?{/color}"
                                            mh8 "Am I not a disturbance? You seem to be enjoying a meal."
                                            p_dei "{color=#808080}Ahahahahahaha!{w=1.0} Go on. Ask away.{/color}"
                                            mh8 "Alright.{w=1.0} About the...{w=0.5}{nw}"
                                            p_emm "{color=#808080}{i}Sarge, if it's nothing urgent, let's repsect our food. We can deal with that later.{/i}{/color}"
                                            p_dei "{color=#808080}Right you are, Harold!{i}*chuckle*{/i}{w=1.0} Sorry about that, kid. Talk to you later.{/color}"
                                            mh8 "Thank you, sir."

                                            "That was awkward."

                                        elif (parse_bin(i2b_archives,0) and not parse_bin(i2b_archives,5)):
                                            "The Sergeant should be done with his meal since more than an hour has already passed."
                                            "There is something amiss, however -- one more detail I need to clarify. It's best if I ask one of my companions before I forget about it later."

                                        else:
                                            "With all four of us gathered in the room, we contacted the Sergeant.{w} It took him five minutes to come down and meet with us."

                                            p_dei "Ready to head back to the surface?"
                                            "\"Yes, sir!\""
                                            p_dei "Alright! Since you kids behaved good, the young rookie has some souvenir for you.{w=1.0} Take my lead."

                                            "A souvenir? What could that be?"
                                            "The Sergeant voiced his approval when he learned that Sayo returned the book to its designated place, stating that a few fellow officers would do the same."

                                            scene bg policedepartment office with dissolve
                                            "We returned to the office less than three minutes later.{w} Emmerich is in his cubicle, working on his laptop."

                                            p_dei "Hey, Harold. Your four stooges are here."
                                            hy10 "Nyuk!{w=0.25} Nyuk!{w=0.25} Nyuk!"
                                            "\"HAHAHAHAHAHAHAHAHAHAHAHAHA!!!\""

                                            "He opened the brown envelope next to his laptop and handed a freshly-printed autopsy report to us."

                                            p_emm "We have just received that this morning.{w} Consider that an exclusive scoop before the rest of the world knows about it."

                                            scene bg brownenvelope with dissolve
                                            window show
                                            nvl clear
                                            narr "The details match perfectly on two things:{w=1.0} what Ichirou and I witnessed at the hospital, and what Inoue said towards the end of her testimony."
                                            narr "While it clarified ambiguous areas such as the \"dummy Kyou\" corpse, it opened more questions.{w} What exactly happened before Inoue and Kyou met at the chemistry lab?"
                                            narr "There is one line that caught everyone's attention."
                                            narr "{i}Traces of FDX-A found within the victim's bloodstream. Stimulant likely been ingested twenty-four hours before death. Amount less than 0.01 mL per milliliter of blood.{/i}"

                                            nvl clear
                                            window hide

                                            scene bg policedepartment office with dissolve
                                            st3 "{cps=15}{i}FDX-A{/i}...{/cps}{w=2.0} I have never heard of that."
                                            p_emm "It is a rare chemical that can be formulated from a flower extract. Said plant is indigenous to this country.{w=1.0} Sounds like a lethal poison, but it is more than that."
                                            p_emm "Make of it however it is presented.{w=1.0} We are still in the process of {i}collecting intel{/i} about the chemical.{w=1.0} For now, let's concern ourselves with the basic stuff, shall we?"

                                            "Sayo and Hikaru took pictures of the autopsy report, handing it back to Emmerich when they were done."

                                            if parse_bin(bonus_b1_g,2):
                                                sr5 "If you don't mind, Inspector, shall we ask another question?"
                                                p_emm "Shoot."
                                                sr5 "We talked to Inoue about the details of her abduction and mentioned something about an ampoule containing liquid chlorine.{w=1.0} Were you able to find anything of the sort?"
                                                p_emm "Negative. Dr. Shinozaki confirmed as much."
                                                mh8 "What about Kirisaki? Is there anything else other than what was mentioned in that report?"
                                                p_emm "Also negative."
                                                hy10 "You know, it's strange that she would make a special note of it if it's a mundane object."
                                                mh8 "That's because she almost drowned in a pool.{w=1.0} It's possible she took note of something else while searching for evidence, but that's the only chemical she remembers."
                                                p_emm "She did not bring anything out, however. Shame, but a thoughtful effort, nonetheless."
                                                st3 "This is just a shot, but were there any traces of liquid chlorine or {i}FDX-A{/i} inside Hiroshi's body?"
                                                p_emm "That we would have to wait until the end of this week."

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

                            while lock == 1 and not (parse_bin(i2b_archives,2)):
                                menu:
                                    "Ichirou's decision":
                                        "I wonder if it's alright to interrupt him. Sumiko seems to be in his usual thinking state."

                                        st3 "Did he make the right decision?{w=0.5} Did I make mine?{w=1.0} Given how everything has played out...{w=2.0}{nw}"
                                        st3 "Hm?{w=0.5} What do you want?"
                                        mh8 "Is it about Ichirou?"
                                        st3 "Until now, I can't remove his words from my mind. I never thought how much he could influence others to take his words as gospel."
                                        mh8 "And rally them against the Student Council President even without evidence.{w=1.0} We're lucky that the meeting's details haven't leaked out to the open."
                                        st3 "IV-B is doing excellently with their hush job.{w=1.0} Our class I can say the same."
                                        mh8 "Eventually, the rest of the batch will know about it and play their parts.{w=1.0} Do you think they'll cooperate?"
                                        st3 "Not to cast distrust on our batchmates,{w=0.5} but in a group of two-hundred, there is {i}always{/i} that one snitch who blows the whistle."
                                        st3 "If that happens, then all eyes are on us.{w=1.0} I'm not going to say any more."

                                        if not parse_bin(i2b_archives,3):
                                            $ i2b_archives += 8

                                    "Liquid chlorine" if parse_bin(bonus_b1_g,2):
                                        mh8 "Liquid chlorine is something that's used as a swimming pool cleaner, right?"
                                        st3 "Correct."
                                        mh8 "Did you notice the discrepancy? Why would such a harmless substance be kept in a small vial when it can be stored in a larger container?"
                                        st3 "Not necessarily {i}harmless{/i}, but what you're suggesting is indeed questionable."
                                        mh8 "Yes. There was a decontamination pool in the facility Inoue and Kyou were held in.{w=1.0} Still though,{w=0.5} why in an ampoule?"
                                        st3 "I forgot the specifics. Let's ask the Inspector later."
                                        mh8 "I thought this is your area of expertise?"
                                        st3 "It's a bit complicated to recall the tiniest details about chlorine, especially if we're finding a toxic component within that element."
                                        mh8 "Fair enough."

                                        if not parse_bin(i2b_archives,4):
                                            $ i2b_archives += 16

                                    "Live wires":
                                        mh8 "From what the news articles were telling us, Rikiyama was found hanging with a live wire.{w=1.0} In that case, wouldn't the culprit be electrocuted as well?"
                                        st3 "Your theory oddly made more sense than that.{w=1.0} If the perpetrator was wearing insulated gloves, then that fills in the hole."
                                        mh8 "The murder could have ended there, but Rikiyama {i}was{/i} hanged.{w=1.0} How would that work?"
                                        st3 "Wires are too thin to support a human body. Body weight is enough more than enough to break them.{w=1.0} You would need several rolls of {i}thick wire{/i} to counteract the force."
                                        mh8 "Which can be conveniently found inside that computer lab and, if they have one, the adjacent storage room."
                                        st3 "Even then, handling them that way poses a dangerous risk to both the victim and the attacker.{w=1.0} There would have been two corpses instead of one if Rikiyama was hanged right before the wires are connected to the power box."

                                        if not parse_bin(i2b_archives,5):
                                            $ i2b_archives += 32

                                    "<<< BACK":
                                        $ lock = 0

                        "Hikaru Yamamoto":
                            $ lock = 1

                            while lock == 1 and not (parse_bin(i2b_archives,2)):
                                menu:
                                    "Inoue's condition":
                                        hy10 "Mi-kun, did you really mean what you said earlier?"
                                        mh8 "About what?"
                                        hy10 "Inoue.{w=1.0} Do you believe she killed Kirisaki?"
                                        mh8 "Unintentional at best, if her words are to be believed.{w=1.0} How can you be so sure about it, however? All the plausible scenarios I've thought of have unfortunate end results."
                                        hy10 "You must keep in mind she survived a series of harrowing ordeals.{w=1.0} Give her time and maybe she'll have a clearer outline of events."
                                        mh8 "How long?{w=0.5} When she finally dies?"
                                        hy10 "I'm not saying that!"
                                        mh8 "Look.{w=0.5} I can forgive Inoue for all the unwarranted outbursts because of her triggers.{w=1.0} I do not understand why she is so adamant in convicting Sayo of kidnapping and murder."
                                        hy10 "Maybe Sayo-chan really did kill Kirisaki -- and possibly, Hiroshi?"
                                        mh8 "Not you too, Hikaru?"
                                        hy10 "If that upsets you, why don't you stop asking the wrong questions? You act as if you can make sensible decisions most of the time. Live up to that, if you please."

                                        if not parse_bin(i2b_archives,6):
                                            $ i2b_archives += 64

                                    "Nursery rhymes":
                                        mh8 "{cps=15}Hmmmmmm...{/cps}"
                                        mh8 "Hey, Hikaru.{w=0.5} Do you have any favorite nursery rhyme?"

                                        "Yes, I'm bored. I can't think of any other topic to pass the time while she is returning the book.{w=1.0} Come to think of it.{w=0.5} She's taking longer than expected."

                                        hy10 "{cps=20}{i}Twinkle,{w=0.5} Twinkle,{w=0.5} little{w=0.25} star;{w=1.0} How I wonder what you are?{/i}{/cps}{w=1.5}{nw}"
                                        mh8 "{cps=20}{i}Up above the world so high;{w=0.5} Like a diamond in the sky...{/i}{/cps}"
                                        hy10 "That's my favorite. It was Mama's lullaby to me.{w=0.5} What's yours?"
                                        mh8 "Mine is this."
                                        mh8 "{cps=25}{i}Jack and Jill went up the hill to fetch a pail of waaaaater...{/i}{/cps}{w=1.5}{nw}"
                                        hy10 "{cps=25}{i}Jack fell down and broke his crown and Jill came tumbling aaaaafter...{/i}{/cps}"
                                        mh8 "..."
                                        hy10 "..."
                                        hy10 "Why'd you ask?"
                                        mh8 "Nothing."

                                        "{cps=15}{i}*whistle* *whistle* *whistle*{/i}{/cps}"
                                        "Sayo's still inside, huh?{w=1.0} {cps=15}Oh well...{/cps}"

                                        if not parse_bin(i2b_archives,7):
                                            $ i2b_archives += 128

                                    "<<< BACK":
                                        $ lock = 0

                        "<<< BACK":
                            pass

                "Move":
                    menu:
                        "Reception Area" if parse_bin(areas,0):
                            scene bg policedepartment lobby with fade
                            $ current_area = 0

                        "Office" if parse_bin(areas,1):
                            scene bg policedepartment office with fade
                            $ current_area = 1
                            
                        "<<< BACK":
                            pass

    scene black with fade
    centered "{color=#5decff}--INVESTIGATION COMPLETE--{/color}"
    scene bg policedepartment office with fade

    "{i}*RING* *RING*{/i}"
    hy10 "It's Papa.{w=0.5} Excuse me for a moment.{w=1.0}{nw}"
    hy10 "Hello...?"
    mh8 "{cps=25}And none too soon.{/cps}"
    p_emm "I appreciate you guys coming here to do some investigative work. It's not a standard pasttime, but you have to do what you need to do."
    p_dei "And you didn't cross the vigilante line.{w=1.0} Gold star for each of you!"
    mh8 "We appreciate it. {i}*chuckle*{/i}"
    p_emm "I've taken note of what you said earlier, Miyu.{w=1.0} Finish your studies and maybe consider joining the force to pursue your detective dream."
    mh8 "I have five more years to consider that.{w=1.0} Plus, I'm not even sure if I {i}do{/i} want to be an investigator like you and Sarge."
    p_emm "Speaking of, I had a conversation with {i}her{/i} over lunch. She's helping us with the case as a \"guest character,\" so to speak.{w=1.0} I'll introduce you to {i}her{/i} soon."
    mh8 "We'll look forward to it,{w=1.0} and I hope it won't be long.{w=1.5} {cps=20}If we can stay alive until then, that is...{/cps}"
    sr5 "Like what I've said, Inspector, I shall search for the truth as long as my actions are bounded by the Law.{w=1.0} The three of us follow that same principle."
    sr5 "{cps=25}That,{w=1.0} and I need to clear my name.{/cps}"
    p_emm "That has always been our end goal:{w=1.0} to convict the guilty and to let the innocents roam free."
    p_emm "Please understand that we cannot ascertain your innocence at this point.{w=1.0} You and your friends are equally likely to be a suspect, and possibly, the mastermind."

    "She grinned and nodded silently."

    mh8 "At what cost?"
    st3 "Let's not think about that now, Miyu. We still have a few more days before the game starts."
    mh8 "{cps=20}Right... {i}Where the amusement is...{/i}{/cps}"
    sr5 "We shall be taking our leave, Inspector. Our friend is scheduled to attend Church with her family this late afternoon."
    p_dei "Then we shan't hold you any longer!"

    scene bg policedepartment lobby with fade
    "Emmerich and the Sarge exchanged handshakes with us. They accompanied us outside the office where Hikaru is."

    hy10 "Alright, Pa. We'll be going downstairs now.{w=1.0} Bye."

    "{i}*BEEP*{/i}"

    "Likewise, they exchanged handshakes with her.{w} A few more farewells and thanks later, we parted ways."

    scene bg policedepartment outside with fade
    "We returned to the reception desk, collected our IDs, and went outside the building. Sure enough, Hikaru's parents are waiting at the parking lot nearby."

    hy10 "There they are. Thanks again, guys!"

    "Hikaru greeted her parents and went inside the car."
    "We walked towards the civilians' exit as the Yamamotos drove away in the opposite direction from Kutsutochi."
    "And now, we wait."

    return

label ch03_07B1_rikiyama:
    scene black with fade
    "{color=#808080}JUNE 28, 2012 - 1830H{/color}"
    scene bg sha computerlab with fade

    teacher "Fuuko, we have a policy against using the lab for personal use. Plus, you should be heading home already."
    rikiyama "I know, sir. Just this once!{w=1.0} It will be in preparation for the Foundation Day next week."
    rikiyama "{cps=30}And we have prepared a special segment {i}just for you.{/i} *giggle* *giggle*{/cps}"
    teacher "Hmph.{w=0.5} Just{w=0.25} {i}this{/i}{w=0.25} once."
    rikiyama "Yay! Thank you so much!"
    teacher "But!{w=0.5} I am only giving you until eight o' clock.{w=1.0} Do we have an understanding, Ms. Rikiyama?"
    rikiyama "Yes, sirree!"
    teacher "And if I catch you on Facebook or Twitter, I'll send you home early."
    rikiyama "Yes, sirree!"
    teacher "Before I leave, do you need anything else?"
    rikiyama "Nothing more. I'm sure everything I need is installed."
    teacher "Good. I'll be in a meeting with the other lab instructors.{w=1.0} Turn off the lights and the PC when you leave. The password is under the keyboard in case you need it."

    window show
    nvl clear
    narr "She was left alone in the lab, her teacher marking the door with a fat red chalk before disappearing."
    narr "The only sounds that can be heard are the whirring of the air conditioner and the CPU she was using. It would take fifteen minutes before the room turns into frostbite condition."
    narr "Outside, a guard roamed the empty hallways, locking the classrooms and checking for any stray students.{w} He peeked into the computer lab where he confirmed Rikiyama was alone before continuing his rounds."

    nvl clear
    narr "She was busy working on their class poster, her progress nearly done with only retouches left to do.{w} Why did she not leave the job to one of her classmates? Maybe she was the only available member of their Creatives Committee."
    narr "Rikiyama is also a talented artist, frequently commended by her peers for her efficiency."
    narr "Although...{w=1.0} it is true that she was one of the \"headaches\", stepping over the boundaries as she wished."

    nvl clear
    narr "After fifteen minutes, Rikiyama felt the pressure on her pelvis as her skin registered the air's coolness.{w} She activated Sleep Mode and left for the washroom."

    scene bg sha corridor night with dissolve
    narr "The corridors were dark, the moon serving as the only light source."
    narr "{i}*step*{w=0.5} *step*{w=0.5} *step*{/i}"
    narr "If she had to turn her neck, she avoided the classrooms. There were {i}unnerving things{/i} inside those.{w} Things derived from the academy's old folk tales, where staring through the door glass allows one to see into the parallel dimension and get swallowed within should they play the curious cat."
    narr "She laughed and mocked herself for believing in such stories when she was younger.{w} Ghosts do not exist. The sheer ridiculousness is the reason why campfire stories and cheesy B-Horror movies exist."

    nvl clear
    window hide

    scene black
    centered "{i}{b}*SLAM*{fast}{w=1.0} *rattle rattle*{/b}{/i}{w=2.0}\n\n{cps=15}{i}murmur... murmur... murmur...{/i}{/cps}"

    rikiyama "{cps=20}Classic Mr. Guard M.O...{/cps}{w=1.5} Always living out these myths to amuse themselves. {i}*giggle*{/i} Bored schmucks."

    scene bg sha womensrestroom with dissolve
    window show
    nvl clear
    narr "She sat down on the toilet and went on with her business."
    narr "The door opened.{w=1.0} Stilletto steps on tiles passing by her stall.{w=1.5} The other door closed.{w=1.0} Locked."
    narr "Just a teacher.{w=1.0} Ignore her."

    nvl clear
    narr "Rikiyama washed her hands and glanced at the other stalls through the reflection.{w} The doors were all open, including the one the teacher used. She dismissed her thoughts and set off for the computer lab."
    narr "{cps=10}{i}*INHALE*{w=1.5} {b}*EXHALE*{/b}{/i}{/cps}"
    narr "Look to the left.{w=1.0} To the right.{w=1.0} Walk faster.{w=1.0} Breathe."

    scene bg sha corridor with dissolve
    nvl clear
    narr "The corridor became a winter box when she stepped out. Rikiyama rubbed her arms vigorously and buried her hands under them. The leaves rustled as the wind blew stronger."

    scene bg sha computerlab with dissolve
    narr "She reached the lab -- knob the same temperature when she touched it -- and went straight to her terminal. She input the PC's password and continued with her work."
    narr "{cps=20}The artwork was vandalized.{/cps}{w=2.0}{nw}"
    narr "{cps=15}Her face was smudged.{/cps}"

    nvl clear
    window hide

    rikiyama "{cps=20}What the...?{/cps}{w=0.5}{nw}"

    scene white
    "{i}*THUD*{/i}"

    rikiyama "MFFF!"

    window show
    nvl clear
    narr "A hand muffled her screams."
    narr "Rikiyama flailed, desperate to break free from whatever was restraining her.{w} She managed to kick it.{w=1.0} Step on its foot.{w=1.0} It grimaced.{w=1.0} She broke free."
    narr "She {i}would have{/i} had her hair be shorter than present. The unknown assailant pulled it, almost tearing it away from her scalp."

    scene red
    narr "{b}*CRASH*{/b}{w=2.0} {i}*fizzle* *spark* *spark*{/i}"

    scene black with fade
    narr "Rikiyama's head smahed the computer monitor.{w} She fell unconscious from the blow, unaware of what happened in the next ten minutes."

    nvl clear
    narr "{i}{b}*spark* *spark* *spark*{/b}{/i}"
    narr "Those sounds along with the pungent smell jolted her awake.{w} Dazed and numb, she struggled to look at her attacker, features obscured by the blur."

    nvl clear
    window hide

    scene black
    centered "{color=#808080}{i}{cps=25}This will hurt,{w=0.5} but this won't be long.{/cps}{w=1.5} {cps=15}Don't you worry...{/cps}{/i}{/color}"

    window show
    nvl clear
    narr "Seconds passed."
    narr "She felt an unusual pressure on her neck.{w} It was odd since she did not bring a scarf to school.{w=1.0} No, it was too narrow to be a scarf and too rough on her fingers."

    window hide
    scene bg sha computerlab with fade
    window show
    narr "No. Her neck was tightly wrapped with wires!{w=2.0} It was long enough to span from her neck...{w=1.0} up to the broken ceiling above...{w=1.0} to the power box where the shadow was standing."

    nvl clear
    window hide

    rikiyama "{cps=20}Let me go...{w=1.0} I won't...{w=0.5} tell anybody.{w=1.0} Promise... {i}*SOB*{/i}{/cps}"

    centered "{cps=20}{i}{color=#808080}I won't either.{/color}{w=1.5} {color=#bd0000}Stay still.{/color}{/i}{/cps}{w=2.0}{nw}"
    centered "{color=#bd0000}{b}*ZAP*{w=0.5} *HUM*{w=0.5} *SPARK* {i}*SPARK* *SPARK*{/i}{/b}{/color}"

    scene blood
    rikiyama "HRRRRRRRRNNNNGGGHHH..."
    scene blood2 with fade

    window show
    nvl clear
    narr "Rikiyama's screams stayed within her head.{w} Electricity surged throughout her body and severed her nerves until the pain was no more. Her senses were reduced to a buzz and a blur."
    narr "Before the next minute, she expired. The shadow vanished and left the power snaking through her lifeless body.{w} The room plunged into darkness, sparks flashing until they disappeared."
    narr "And from the darkness emerged an ember."

    nvl clear
    window hide

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
    scene bg smallstreet night with fade

    window show
    nvl clear
    narr "Thunder.{w=1.0} The sky flashed, revealing the rain clouds in the violet sky."
    narr "The hour marked the last outpour of students from all over the city. It is when a few shops in the wet market are closing for inventory; when the youngsters are at home enjoying their last meal before bedtime."
    narr "For Ichirou Yokohama, it was an unusual time to leave campus.{w} Mrs. Ritsuko had left early and he had stayed, hoping to have a word with her."
    narr "She never returned.{w=1.0} Ichirou headed home, exasperated for not taking the initiative that morning."

    nvl clear
    narr "The tricycle stopped in front of their street. He paid the fare and walked towards their gate.{w} Though poorly lit, the street felt lively, neighbors chatting over a smoke or a pack of chips."
    narr "He locked the gate. Only when he was near did he notice that the front door was ajar.{w=2.0} Most unusual.{w=1.0} He and his sisters were always told to close the door every six o' clock."
    narr "He brought out his umbrella and lengthened it to a cubit. Using this, he prodded the door open."
    narr "{cps=15}{i}*creeeeeeeeeaaaaaaaak*{/i}{/cps}"

    scene black with dissolve
    narr "{cps=30}The first two steps on the marble floor,{w=1.5} the softening voices of the neighbors,{w=1.5} and the deathly silence of the entire household. His abode felt hostile.{/cps}"
    narr "{cps=25}Is the unwelcome presence himself?{w=2.0} Or is there someone else?{/cps}"

    nvl clear
    window hide

    f_iy1 "Hello?{w=1.0} I'm home!"

    window show
    nvl clear
    narr "{cps=20}Home.{w=0.25} {i}Home.{/i}{w=0.25} {i}home...{/i}{w=0.5} It is a most unusual night.{/cps}"
    narr "{cps=30}He placed his backback down, arms facing towards the mini coffee table.{w=1.0} With a flashlight, he found the switch.{/cps}"
    narr "{cps=20}But it did nothing.{/cps}"
    narr "{cps=25}The temperature increased.{w=1.0} Ichirou's uniform was soaked.{w=1.0} Whoever was with him had deactivated the breaker.{w=1.0} He turned his attention to --{nw}{/cps}"

    nvl clear
    narr "{b}{i}*SLAM*{/i}{/b}{fast}{w=2.0}{nw}"
    narr "A quick turn!{fast}{w=1.5} His instincts told him to run!{fast}{w=2.0} But there he froze, thoughts conflicting on his course of action.{w=1.0} The beam caught a glimpse of a shadow.{w=1.0} It moved swift enough to evade his sights."
    narr "{cps=20}{color=#bd0000}{i}Hehehehehehehehe...{w=1.5} Kyekyekyekyekyekyekye...{/i}{/cps}{/cps}"
    narr "{cps=30}He was doomed.{w=1.0} He had been duped.{w=1.0} His heart could burst at any moment now.{w=1.5}{/cps} {cps=25}The air felt heavier.{w=1.0}{/cps} {cps=20}He was being watched...{/cps}{w=0.5}{nw}"

    nvl clear
    narr "{b}*THUNDER*{/b}{fast}{w=2.0}{nw}"
    narr "{cps=15}He ran...{/cps}{w=0.5} {cps=20}ran as fast as he could.{/cps}{w=0.5} {cps=25}Past the kitchen and out to the laundry area.{/cps}{w=0.5} {cps=30}The lid he forced open with his hand and held the switch.{/cps}{w=0.5} Raise it!{fast}{w=2.0}{nw}"
    narr "{i}*spark*{/i}"

    scene bg livingroom2
    narr "{cps=20}And the entire house lit up and hummed.{/cps}{w=1.0} {cps=15}He looked inside.{/cps}{w=1.0}{nw}"

    nvl clear
    window hide

    scene bg diningroom
    "\"SURPRISE!!!\""

    "How silly. Today is his sixteenth birthday. The Yokohamas had been hiding all along!{w} He laughed at the utter ridiculousness of the situation and received intimacy as compensation."

    iy1 "You got me good there. I thought someone was going to jump at me from the dark and silence me.{w=1.0} Surprise, indeed! Hahahahaha!"
    ms_yok "We had to up the ante, Ichi. You always say we're getting more predictable."
    mr_yok "Treat this as a reward for being Top 1 Overall for the First Quarter.{w=1.0} Keep that up, son, and you will graduate a Valedictorian with Highest Honors, maybe!"
    iy1 "Awww...{w=1.0} I'm touched."
    iy1 "But, wait. This isn't something we'd think of when planning a surprise. There has to be a third party involved.{w=1.0} Who helped with this, hm?"
    mr_yok "Have a look."

    scene bg livingroom2 with dissolve
    "His eyes followed his Papa's hand."
    show akira proud at Three2 with Dissolve(0.2)
    "His eyes followed his Papa's hand.{fast} A smug face occupied one of the couches."

    show akira proud2 at Three2 with Dissolve(0.2)
    ai2 "Yo."
    show akira fang at Three2 with Dissolve(0.2)
    iy1 "Oh, you little devil... {i}*chuckle*{/i}"
    hide akira with Dissolve(0.2)

    scene bg diningroom with dissolve
    show akira smirk at Three1 with Dissolve(0.2)
    show ichirou happyblush at Three2 with Dissolve(0.2)
    window show
    nvl clear
    narr "They spent the next hour giving gifts and eating dinner."
    narr "The usual menu consists of the following:{w=1.0} a pan of spaghetti, a large basket of pancit canton, two bowls of fruit salad, thirty pieces of spring rolls, and a pot of menudo."
    narr "Over the table, they talked about the day's events, what Ichirou's plans are for the future, and how his school life is going.{w} There were, of course, {i}taboo{/i} topics they avoided to not spoil the night."

    nvl clear
    window hide

    show ichirou happy at Three2 with Dissolve(0.2)
    iy1 "Ma, Pa, please excuse us. Akira and I will discuss something in private."
    mr_yok "Bring a cup of fruit salad with you. Here."
    show akira smile at Three1 with Dissolve(0.2)
    ai2 "Thank you."
    hide akira with Dissolve(0.2)
    hide ichirou with Dissolve(0.2)

    scene bg livingroom2 with dissolve
    show akira smile at Three1 with Dissolve(0.2)
    show ichirou smile at Three3 with Dissolve(0.2)
    "They took their own cups with them.{w} Once Ichirou assured that they were beyond earshot, he began speaking."

    show ichirou confused at Three3 with Dissolve(0.2)
    iy1 "You're one I least expected to visit. Don't your parents know about this."
    show akira smirk at Three1 with Dissolve(0.2)
    ai2 "Oh. Hehehehe...{w=1.0} About that..."
    show ichirou serious at Three3 with Dissolve(0.2)
    iy1 "It's a dangerous time to be out this late at night. Even more when you consider the kind of danger we're both in."
    show akira happy at Three1 with Dissolve(0.2)
    ai2 "The roads to our village are safe. I can guarantee that.{w=1.0} The time when you should start worrying about is midnight."
    show ichirou surprised at Three3 with Dissolve(0.2)
    iy1 "What about it?{w=2.0} Oh."
    show ichirou smile at Three3 with Dissolve(0.2)
    iy1 "Tomorrow is the sixteenth.{w=1.0} No matter.{w=0.5} We have duly prepared for that.{w=1.0} When I blew the candles, I wished that none of us be harmed -- at least until the end of the month."
    show akira surprised2 at Three1 with Dissolve(0.2)
    ai2 "You just blew it, silly."
    show ichirou embarrassed at Three3 with Dissolve(0.2)
    iy1 "Did I?{w=1.0} Sorry!"
    show ichirou happy2 at Three3 with Dissolve(0.2)
    show akira smirk at Three1 with Dissolve(0.2)
    "\"Hehehehehehehehehehehe!\""
    show ichirou surprised at Three3 with Dissolve(0.2)
    iy1 "Do you still remember what we talked about in the library?{w=1.0} You asked me a question about Innoue's credibility. I thought over it during the Sunday Mass."
    show akira bored at Three1 with Dissolve(0.2)
    show ichirou focus at Three3 with Dissolve(0.2)
    iy1 "Honestly, I'm not sure if we can trust Inoue."
    show akira boredtalk at Three1 with Dissolve(0.2)
    ai2 "I'm glad you feel the same, too. I thought you'd be hard-headed enough to believe everything she says."
    show ichirou serioustalk at Three3 with Dissolve(0.2)
    iy1 "So, then what? That doesn't change the fact that she admitted her hand in Kirisaki's death.{w=1.0} The rest? We cannot be sure of until her memories are restored."
    show akira serious at Three1 with Dissolve(0.2)
    ai2 "What about that moment that got our butts into Ms. Natsumoto's office? You don't buy that?"
    show ichirou proud at Three3 with Dissolve(0.2)
    iy1 "Buy it? Heh.{w=0.5} Even if she asks me a penny, I won't give it to her.{w=1.0} Oh yes, \"It was you,{w=1.0} Sayo Ronoroa!\"{w=1.0} She said that because..."
    show akira annoyedclosed at Three1 with Dissolve(0.2)
    ai2 "..."
    show ichirou surprised at Three3 with Dissolve(0.2)
    iy1 "Ahem.{w=0.5} ...Because she gatecrashed our peaceful interview...{w=1.0} and at the opportune moment!{w=1.0} Had she arrived any earlier, Inoue's statements would have sounded more jumbled up."
    show akira surprised at Three1 with Dissolve(0.2)
    ai2 "You're so transparent, Ichi. {i}*sigh*{/i}{w=1.0} You pulled that one out of your socks."
    show ichirou focusleft at Three3 with Dissolve(0.2)
    iy1 "Hmph.{w=0.5} Fine. I did.{w=1.0} What does it change? Not my feelings about the entire situation, that's one."
    show akira annoyed at Three1 with Dissolve(0.2)
    ai2 "The only change I'm seeing is that we have a potential enemy in our midst."
    ai2 "I'm not saying Inoue is bound to run amok and bash some of our heads when we least expect it. I'm saying we should keep a watchful eye on her."
    ai2 "Yoshiro already has the message, I figure."
    show ichirou serioustalkleft at Three3 with Dissolve(0.2)
    iy1 "Too bad, he still has an ounce of trust for both of his former classmates. Can't say I'll be taking that at face value."
    show akira bored at Three1 with Dissolve(0.2)
    ai2 "It is what's fair, Ichi.{w=1.0} That doesn't mean it changes his mind instantly, you know."
    show ichirou focusleft at Three3 with Dissolve(0.2)
    iy1 "I know."

    if parse_bin(bonus_b1_i,1):
        show ichirou worried at Three3 with Dissolve(0.2)
        show akira smile at Three1 with Dissolve(0.2)
        "{i}*SNAP*{/i}"

        ms_yok "What is it, children?"
        show akira fangblush at Three1 with Dissolve(0.2)
        ai2 "{cps=20}Uh...{w=0.5} Ah...{w=1.0}{/cps} Nothing, auntie. Just wanted to break the ice.{w=1.0} Carry on. {i}*chuckle*{/i}"
        mr_yok "If you say so, boys. Hohohohohoh..."
        show ichirou confused at Three3 with Dissolve(0.2)
        iy1 "Right.{w=1.0} What do you have in mind?"
        show akira boredtalk at Three1 with Dissolve(0.2)
        ai2 "From what we know so far, we can consider Inoue as a suspect."
        show ichirou serious at Three3 with Dissolve(0.2)
        iy1 "I can't deny that."
        show akira bored at Three1 with Dissolve(0.2)
        ai2 "She's my not my pick, though. How about you, Ichi?{w=1.0} Other than the three of us, who do you got as L.C.?"
        show ichirou focusleft at Three3 with Dissolve(0.2)
        iy1 "{cps=20}It would be...{w=1.5} Hmmmmmmmmm...{/cps}{w=3.0}{nw}"
        show ichirou serioustalk at Three3 with Dissolve(0.2)
        iy1 "I maintain.{w=1.0} Sayo is still L.C. for me."
        show akira surprised at Three1 with Dissolve(0.2)
        ai2 "{i}Other{/i} than her?"
        show ichirou focus at Three3 with Dissolve(0.2)
        iy1 "Dammit, Akira. Stop making this more difficult than it is. You said to pick someone other than the three of us."
        show akira surprised2 at Three1 with Dissolve(0.2)
        ai2 "What if she isn't?{w=1.0} What if her statements have some merit after all?"
        show ichirou surprised at Three3 with Dissolve(0.2)
        iy1 "{b}{i}*groan*{/i}{/b} If you aren't satisfied, then I'm going with Hikaru."
        show akira bored at Three1 with Dissolve(0.2)
        ai2 "Mine is Sumiko."
        show ichirou serious at Three3 with Dissolve(0.2)
        iy1 "{cps=15}...............{/cps}"
        show ichirou proud at Three3 with Dissolve(0.2)
        iy1 "Excuse me."
        hide ichirou with Dissolve(0.2)

        "Ichirou stood up to get them both a glass of water."
        "Akira leaned to check on him;{w=1.0} he was holding it in."

        show ichirou proud at Three3 with Dissolve(0.2)
        iy1 "Okay... {i}*exhale* *snicker* *snicker*{/i}{w=1.0} As much as I'm bitter about Sumiko, there is {i}zero chance{/i} he is the mastermind.{w=1.0} Hikaru?{w=0.5} Laughable."
        show akira proud2 at Three1 with Dissolve(0.2)
        ai2 "I can guarantee my innocence if you want me to remove the constraints."
        show ichirou confused at Three3 with Dissolve(0.2)
        iy1 "Can you prove that you're not? That is the question."
        show akira surprised at Three1 with Dissolve(0.2)
        ai2 "The irony is you can't either if you always base it on the evidence."
        show ichirou smile at Three3 with Dissolve(0.2)
        iy1 "Oh, please.{w=1.0} You're just waiting for me to say L.C. is Let Carnegie, aren't you?{w=1.0} {cps=10}Hmph!{w=0.5} As if!{/cps}"
        show akira worriedleft at Three1 with Dissolve(0.2)
        ai2 "I don't remember ever calling L.C. a {i}fair lady.{/i}"

        "{i}*tap* *tap* *tap*{/i}"

        show ichirou serioustalkleft at Three3 with Dissolve(0.2)
        iy1 "Inoue is an acceptable alternative.{w=1.0} While she barely fits into every liability parameter Yoshiro had laid down, there exists a possibility that she's telling a hokey story."
        iy1 "Their -- Inoue and Kyou's -- abduction she could have set up, given that they have two of their three classroom keys."
        show akira bored at Three1 with Dissolve(0.2)
        ai2 "I understand Inoue as she's the Vice President of IV-A, but why Kyou?"
        show ichirou worried at Three3 with Dissolve(0.2)
        iy1 "Because he is usually the first to arrive just like you. You're not a class officer either yet you have one of the keys."
        show akira boredtalk at Three1 with Dissolve(0.2)
        ai2 "Hikaru has it that morning. I surrendered it to Sumiko to pass it on to her."
        show ichirou serious at Three3 with Dissolve(0.2)
        iy1 "Same idea.{w=1.0} And if you might ask, it doesn't always follow that L.C. {i}acts alone.{/i} Everything that has happened seems to have some sort of external or supernatural influence."
        show akira bored at Three1 with Dissolve(0.2)
        ai2 "Let's leave it at that."

    hide akira with Dissolve(0.2)
    hide ichirou with Dissolve(0.2)
    scene bg smallstreet night with dissolve
    "Before half past eight, Akira exchanged farewells with the Yokohamas and left the house. He closed the gate on the way out."

    show akira proud at Three3 with Dissolve(0.2)
    neighbor "Evening, buddy.{w=1.0} Better stay alert when you get home. Ichi's mentioned about some weird stuff goin' on lately."
    show akira proudclosed at Three3 with Dissolve(0.2)
    ai2 "Huh. That guy can't keep his mouth shut, can he?{w=1.0} What do you know about it?"
    neighbor "Ehhhhhh... Nothin' outside the news. Only thing he told me -- and I noticed, too -- is that whatever's been goin' on, it's been keeping him on edge."
    show akira serious at Three3 with Dissolve(0.2)
    ai2 "Nothing more?"
    neighbor "Nothin'. Swear. {i}*chuckle*{/i}"
    neighbor "Before you leave, I wanna to perform a {i}routine check{/i} -- safety measures, we call it.{w=1.0} Can you give him a holler?"
    show akira surprised2 at Three3 with Dissolve(0.2)
    ai2 "Hey, Ichirou Yokohama!{w=1.5} Good night!"
    u_iy1 "{i}You don't need to yell that loud!{/i}"

    show akira smile at Three3 with Dissolve(0.2)
    "From behind the curtain of his bedroom window, a silhouette of a hand waving twice appeared."

    neighbor "Fair enough.{w=1.0} Take care on the road and good night!"
    hide akira with Dissolve(0.2)

    scene bg bedroom2 night with dissolve
    window show
    nvl clear
    narr "Lights off. The buzzing sound of the fan the only sound audible."
    narr "Ichirou surfed the net with his smartphone to drowse himself. He periodically glanced at the upper right of the screen to check the clock."
    narr "His notes from the meeting were open. Using this, he read news articles that he thought could cover the remaining gray areas he had in mind."
    narr "{b}{i}*ding*{w=2.0} *ding*{w=2.0} *ding*{/i}{/b}"
    narr "The mechanical clock in the living room sounded twelve times.{w} Ichirou recited his prayers and fell into a slumber."

    nvl clear
    window hide

    scene bg apartment night with dissolve
    "Somewhere else, there are nocturnals gleefully playing under the moonlight.{w} Giggles, rattles and candy pops --{w=1.0} the little devils cared not for the rules of this world."

    scene bg tvstatic with dissolve
    unk "{cps=25}Tee hee hee...{w=0.5} It is time.{w=1.0} {b}{i}*yawn*{/i}{/b}{w=2.0} Have you gotten a good night's sleep?{/cps}"
    unk "{cps=15}Puku.{w=1.5} I did not let the bedbugs bite.{/cps}"

    "Rain fell.{w} Its intensity meant it would last until the next hour. No chances for a class suspension."

    unk "{cps=25}Swing,{w=0.5} swing,{w=0.5} swing...{w=1.0} What should we play?{w=1.0} Who wants to be our playmate?{w=1.0} They need to be fun.{/cps}"
    unk "{cps=15}Who will it be, I wonder...{w=1.0} puku?{/cps}"

    "Using the light coming from the static-filled TV, it trotted to a huge chunk of wood on the other end of the room. Its delicate hands caressed the rough and splintered surface."
    "It was a perfect circle of ten sectors -- two of those torn away."

    unk "{cps=25}Ah, yes...{w=1.0} Swing,{w=0.5} swing,{w=0.5} swing...{w=1.0} With just a little spin, we shall let fate decide our new playmate.{/cps}"
    unk "{cps=25}Three...{w=0.5} two...{w=0.5} one!{/cps}{w=1.0}{nw}"

    "{i}*click*{w=1.0} *WHIRRRRRRRRRRRRRRRR*{/i}"

    unk "{cps=15}Puku.{w=1.0} What should we sing?{w=0.5} What should we sing?{/cps}"

    scene bg abyss with dissolve
    "It stopped."
    "The hands pulled the third tooth out and held it close for both to scrutinize what's written on it."
    "{cps=20}One smiled.{w=1.0} The other widened its eyes.{/cps}"

    scene black with fade
    unk "{cps=25}Swing,{w=0.5} swing,{w=0.5} swing...{w=2.0} Interesting...{/cps}"
    unk "{cps=15}Puku,{w=1.0} best wishes to you...{/cps}"
    "{cps=20}\"Hehehehehehehehehe...{w=1.0} Kukukukuhahahahahahahaha...{w=1.0} Kyekyekyekyehihihihihi...\"{/cps}"

    scene bg blood with fade
    "{i}*drip* *drip* *drip* *drip*{/i}"

    "It has come."
    return

label ch03_08B_innocent:
    if path_b1 == 0:
        $ path_b1 = 1

    scene black with fade
    "{color=#5decff}AUGUST 15, 2013 - 1420H{/color}"
    scene bg classroom1 morning with fade

    window show
    nvl clear
    narr "The students were unusually quiet.{w} What is to be expected when one already learns of a gruesome crime happening within the closest proximity{w=2.0} -- and behind closed doors?"
    narr "There was, however, one notable break in monotony for IV-C. Wednesday's first period is Calculus, handled by the witty Sasuke Uendo."
    narr "Since the start of July, he had been introducing nuggets of useful advice before the week's lesson.{w} He touted each one a \"Thought for the Week.\" He required his students to jot them down for future reference."

    nvl clear
    narr "For this week, he wrote the following on the board:"
    narr "{i}Truth hurts.{w=2.0} It bites!{/i}"
    narr "Which he followed with...{w=2.0}{nw}"

    nvl clear
    window hide

    t_uen "Pretty straightforward!"
    t_uen "Undoubtedly, every one here adheres to their own code. Otherwise, what is the point in living if we live an aimless and baseless life?{w=1.0} One is one,{w=1.0} zero is nothing,{w=1.0} I am me,{w=1.0} you are you."
    t_uen "While we can read this positively, I would like to point out its {i}harsher{/i} side.{w=1.5} Depending on how loving your parents are -- usually, your mother -- you will always hear pleasant adjectives fed into your ears.{w=1.0} Prince Charming, Darling Princess, and the like."
    t_uen "That is until someone smacks you in the face with something like...{w=1.5}{nw}"
    t_uen "You're ugly!{fast}"

    "A finger right between the eyes...{w=1.0} and reddening shameful cheeks."

    student "Me?!{w=1.0} Ow!"
    t_uen "See?{w=0.5} It bites! UGH!"
    "\"HAHAHAHAHAHAHAHAHAHAHAHAHAHA!!!\""
    t_uen "No offense meant, chap.{w=1.0} Forget about what I said, Prince Phillip."
    t_uen "{i}That{/i} is an exaggerated example.{w=1.0} It's what keeps the world a colorful place.{w=1.0} It's a necessary evil.{w=1.0} If everything that's been fed to us is \"real,\" we would become a sausage machine of cynics."
    t_uen "It doesn't excuse us to constantly feed ourselves with lies.{w=1.0} The deeper you are in your fantasy world when you're snapped back to reality, the more painful it will be."
    t_uen "If I say, \"all of you are great,\" will you believe me?"

    "Forty-two shaking heads."

    t_uen "Oh, come on! All of you must be great at something.{w=1.0} For example,{w=0.5} {i}sleeping{/i}."

    scene bg classroom2 morning
    "{b}{i}*snap*{/i}{/b}"

    student "{cps=20}Eh? Wha-what?{/cps}"
    ai2 "Sleepyhead! He's talking to you."
    "\"AHAHAHAHAHAHAHAHAHAHAHA!!!\" \"What a dork!\""
    t_uen "Please keep your head up while I'm speaking, mister. Thank you very much! {i}*chuckle*{/i}"

    scene bg classroom1 morning with dissolve
    t_uen "Point is, all of you are great at something no matter how positive or negative. What those are depends on your genuineness."
    t_uen "{cps=25}And if I ask you,{/cps}{w=2.0} \"What is the derivative of 4 x-squared y-cubed with respect to x,\" will you give me a straight answer?"
    student "{i}*grooooooooan*{/i}{w=1.5} Must you ruin the moment, sir?"
    t_uen "Right you are!{w=1.0} Let's discuss how derivates work, shall we?"

    "For that one moment, there was temporary reprieve."
    "After the class ended, everything returned to how it was -- one seatwork after another."

    scene bg msci with fade
    "The following afternoon, the front desk guard walked over to IV-E and gave the door three knocks."

    scene bg classroom1 with dissolve
    guard "Ms. Sayo Ronoroa!{w=1.0} Are you here?"
    show sayo smileopen at Three2 with Dissolve(0.2)
    sr5 "I am. What do you have for me?"
    guard "Got an envelope from Mr. Inspector here. Said it was to be given directly to the addressee.{w=1.5} Confidential stuff, eh?"
    show sayo smiletalk at Three2 with Dissolve(0.2)
    sr5 "Absolutely.{w=1.0} Thank you, Onifuchi-san."

    show sayo blankface at Three2 with Dissolve(0.2)
    "Exactly as the guard described and time-stamped 1:25 PM. It contained a set of photocopied reports like the ones they examined last Sunday."

    show ayumi serious at Three3 with Dissolve(0.2)
    ayumi "What's that?"
    show sayo normaltalk at Three2 with Dissolve(0.2)
    sr5 "It's confidential."
    show ayumi seriousleft at Three1 with Dissolve(0.2)
    ayumi "Okay. I will be going along now."
    hide ayumi with Dissolve(0.2)
    hide sayo with Dissolve(0.2)

    scene bg msci with dissolve
    show hikaru smile at Three3 with Dissolve(0.2)
    "Ayumi ran into Hikaru and Aria as she went into the canteen. Sayo approached the two when they neared the classroom."

    show sayo smiletalk at Three1 with Dissolve(0.2)
    sr5 "Hello, you two."
    show hikaru talk at Three3 with Dissolve(0.2)
    hy10 "Hey, Sayo-chan. What are we --{w=0.5}{nw}"
    show sayo normaltalkleft at Three1 with Dissolve(0.2)
    sr5 "Pardon me, Aria. May I borrow Hikaru for a moment?"
    show hikaru surprisedtalk at Three3 with Dissolve(0.2)
    hy10 "Whoa! That's a weird way to ask permission."
    show sayo smileopen2 at Three1 with Dissolve(0.2)
    sr5 "Please?"

    show hikaru surprised2 at Three3 with Dissolve(0.2)
    "She tapped at the sender's name.{w} Aria, understanding what it meant, told Hikaru to meet back at IV-C afterwards and left."

    show sayo blankface at Three1 with Dissolve(0.2)
    sr5 "Follow me to the fields."
    show hikaru surprised2 at Three3 with Dissolve(0.2)
    hy10 "Why not to the Student Council office?"
    show sayo seriousnormalleft at Three1 with Dissolve(0.2)
    sr5 "No official reason to use it now."
    show hikaru thinkingleft at Three3 with Dissolve(0.2)
    hy10 "Let's fetch Miyu and Sumiko first."
    show sayo serioustalkleft at Three1 with Dissolve(0.2)
    sr5 "Not now."
    show hikaru angry at Three3 with Dissolve(0.2)
    hy10 "Why? They have been waiting for this."
    show sayo serioustalk2 at Three1 with Dissolve(0.2)
    sr5 "In due time, Hikaru. We don't have time to have a prolonged discussion.{w=1.0} I'd say we keep it until we examine the documents thoroughly."
    hide sayo with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)

    scene bg school fields with dissolve
    "Although Sayo's response was puzzling, Hikaru went along with her to the auditorium."
    show sayo seriousnormalleft at Three3 with Dissolve(0.2)
    show hikaru serious at Three1 with Dissolve(0.2)
    "They sat facing each other.{w=1.0} After ensuring no other students were nearby, Sayo took the papers out and handed them to Hikaru."

    show sayo seriousnormal at Three3 with Dissolve(0.2)
    sr5 "Inspector Emmerich delivered this after lunch break. Good of old Onifuchi to hand this to me just as break time started."
    show hikaru surprised2 at Three1 with Dissolve(0.2)
    hy10 "He followed through, huh?{w=1.0} But some details are subject to change with this version."
    show sayo normaltalk at Three3 with Dissolve(0.2)
    sr5 "Better to have an initial report than to wait for the final analysis after a few more weeks. Besides, we have less than ten hours to prepare for L.C.'s coming."

    "With the limited time given to them, they skimmed to the most important parts of the report."
    hide sayo with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)

    scene bg brownenvelope with dissolve
    window show
    nvl clear
    narr "In summary,"
    narr "{i}Hiroshi Kano -- aged 15 at time of death\nDate: 19th of July, 2013{/i}"
    narr "{i}Cause of Death: Asphyxiation due to shock from excessive blood loss\nEstimated Time of Death: 1800H-1900H, skin still warm to the touch{/i}"
    narr "{i}All of the patient’s indices have been severed by a medium-sized blade, most likely a pair of office scissors or a kitchen knife. Small bruises found around victim’s neck. Attempted strangulation possible before being bound. Pieces of scotch tape found around the mouth, the wrists, and the neck.{/i}"
    narr "{i}Moderate amounts of melatonin found within bloodstream; no signs of drug overdose. Hence, no definite relation in regards to cause of death. Further analysis in progress.{/i}"

    nvl clear
    window hide

    scene bg school fields with dissolve
    show sayo worriedtalk at Three3 with Dissolve(0.2)
    show hikaru surprised at Three1 with Dissolve(0.2)
    sr5 "{cps=15}Melatonin...{/cps}{w=2.0} Sleep medicine?{w=1.0} I didn't know Hiroshi had insomnia or anything of the kind!"
    show hikaru thinkingleft at Three1 with Dissolve(0.2)
    hy10 "Me neither.{w=1.0} I mean, he doesn't even look that problematic. He never seemed to suffer from narcolepsy when we were classmates."
    show sayo normaltalkleft at Three3 with Dissolve(0.2)
    sr5 "That was two years ago. How much could he have changed since then?{w=1.0} Besides, isn't he too young to be taking such medication?"
    show hikaru surprised2 at Three1 with Dissolve(0.2)
    hy10 "Sumiko can tell us later about Junior Year."
    show hikaru serioustalkleft at Three1 with Dissolve(0.2)
    hy10 "{cps=30}Still, this makes me curious.{w=1.0} This implies {i}something{/i}.{/cps}"

    show hikaru serious at Three1 with Dissolve(0.2)
    show sayo worried at Three3 with Dissolve(0.2)
    "The two stared into each other's eyes, signaling not to utter the word."
    "With one more possible angle in their grasp, it is but a small victory. Is there, however, any truth to it?"

    show sayo blankfacepose at Three3 with Dissolve(0.2)
    sr5 "I hope he wasn't overworking himself while he was still alive.{w=1.0} Do you remember how he surprised us by becoming one of the Top 5 students last year?"
    show hikaru talk at Three1 with Dissolve(0.2)
    hy10 "After a slump and disqualification from the First Quarter, it is! I even congratulated him personally."
    show hikaru thinkingclosed at Three1 with Dissolve(0.2)
    hy10 "Getting back to the report, though.{w=1.0} How would a pair of scissors chop a finger, let alone ten of them?"

    show sayo blankfaceclosedpose at Three3 with Dissolve(0.2)
    centered "{color=#808080}{cps=20}The pink book states that blades and other deadly weapons are prohibited inside the school.{w=1.0} Cutters and scissors can only be brought if required by the teacher.{w=0.5} Therefore, all knives are out of the question.{w=3.0}\n\nHowever, consider the crime scene.{w=1.0} There are plenty of supplies inside the Student Council office, some of which may be potential instruments to the crime. Yet, no weapon was found.{w=2.0}\n\nIf so,{w=0.5} then maybe...{/cps}{/color}"

    show sayo normaltalkleftpose at Three3 with Dissolve(0.2)
    sr5 "The crime scene is in an office space. If you are creative enough, you have a lot of weapons at your disposal."
    show hikaru thinkingleft at Three1 with Dissolve(0.2)
    hy10 "Just like those series of flash games where you whack your boss or someone you hate?"
    show sayo normaltalkpose at Three3 with Dissolve(0.2)
    sr5 "Exactly.{w=1.0} And I'll admit this right now.{w=1.0} We don't keep an inventory of our supplies except for two instances: the beginning and the end of the school year."
    show sayo serioustalkpose at Three3 with Dissolve(0.2)
    sr5 "In fact, we have no idea how many of each item we currently have regardless of restocks or disposals. Even if we did, it makes me wonder how a bladed weapon disappeared from a single-entryway room."
    show hikaru serioustalkleft at Three1 with Dissolve(0.2)
    hy10 "So then..."
    show sayo seriousnormalleftpose at Three3 with Dissolve(0.2)
    sr5 "However!{w=1.0} Recall that Emmerich and his team finished their investigation of the office and found no murder weapon. Why?"
    show hikaru serioustalkclosed at Three1 with Dissolve(0.2)
    hy10 "Right. I see why."
    show hikaru worried at Three1 with Dissolve(0.2)
    hy10 "What do we do now?"
    show sayo seriousclosedpose at Three3 with Dissolve(0.2)
    sr5 "No other choice.{w=1.0} We must wait for L.C. to make their move. There's no merit to random accusations without solid evidence. It would make us no different from {i}them{/i}."
    show hikaru worriedclosed at Three1 with Dissolve(0.2)
    hy10 "..."
    show hikaru seriousleft at Three1 with Dissolve(0.2)
    hy10 "I heard Ichirou conducted their own investigation as well.{w=1.0} Do you think it would be best if we sit down and talk our differences over?"
    show sayo blankfacepose at Three3 with Dissolve(0.2)
    sr5 "I would love to. But how should we approach it?{w=1.0} For sure, Inoue despises me because of what happened to her and what she witnessed then."
    show hikaru serious at Three1 with Dissolve(0.2)
    hy10 "If not Inoue-chan, then we start with the root cause?"
    show sayo smileclosedpose at Three3 with Dissolve(0.2)
    sr5 "Possible.{w=1.0} Miyu can snap him out of his own delusion. Ichirou's recklessness has caused an irreparable strife between us, and Inoue only made things worse."
    sr5 "They are neighbors, yes?"
    show hikaru seriousleft at Three1 with Dissolve(0.2)
    hy10 "Yes. Ichi told me they live two streets from each other."
    show sayo smirkpose at Three3 with Dissolve(0.2)
    sr5 "He has more than enough time. It's up to him when the right time is."
    show hikaru worriedtalk at Three1 with Dissolve(0.2)
    hy10 "Are you sure you're alright, Sayo-chan?"
    show sayo creepy smirkpose at Three3 with Dissolve(0.2)
    sr5 "..."

    "{cps=25}Swaying her feet back and forth...{w=1.0} Back and forth...{w=1.0}{/cps} {cps=20}Back and forth...{/cps}{w=1.0} Sayo watched the leaves being carried away by the wind.{w=1.5} The gray skies signified an oncoming downpour."
    "{cps=20}Tongue,{w=0.5} lips,{w=0.5} tongue,{w=0.5} lips,{w=0.5}{/cps} Sayo clicked her tongue to the steady beat of the song from her childhood."
    "{cps=20}A, B, C, D, E, F, G...{w=1.5} Now I know my ABC,{w=1.0} next time please sing with me.{/cps}"

    show sayo creepy smirkpose2 at Three3 with Dissolve(0.2)
    sr5 "{cps=25}Less than a minute left.{/cps}{w=1.0} {cps=15}Tick tock,{w=0.5} Tick tock,{w=0.5} Tick tock...{/cps}"
    show hikaru worried at Three1 with Dissolve(0.2)
    hy10 "{cps=30}You're scaring me...{/cps}"
    show sayo creepy smirkpose at Three3 with Dissolve(0.2)
    sr5 "..."

    "{i}*RIIIIIIIIIIIIIIIIIINNNGGG*{/i}"

    show sayo smileclosed at Three3 with Dissolve(0.2)
    "Sayo stood up, motioning Hikaru to come along."

    show sayo smirknormal at Three3 with Dissolve(0.2)
    sr5 "It's time."
    show hikaru worried2 at Three1 with Dissolve(0.2)
    hy10 "Yes.{w=1.0} It is."
    hide sayo with Dissolve(0.2)
    hide hikaru with Dissolve(0.2)

    scene bg msci with dissolve
    show sayo smileclosed at Three3 with Dissolve(0.2)
    show hikaru worried2 at Three1 with Dissolve(0.2)
    "The two walked back to their classrooms, passing by the bust in the middle of the quadrangle.{w} Before they separated, Hikaru glanced at Sayo one last time."
    show sayo smirkpose at Three3 with Dissolve(0.2)
    "{cps=20}Grinning with her teeth visible...{/cps}{w=2.0}{nw}"
    show sayo happyclosed at Three3 with Dissolve(0.2)
    show hikaru surprised at Three1
    "And she winked playfully."
    show hikaru smile at Three1 with Dissolve(0.5)
    hide sayo with Dissolve(0.2)
    hide hikaru with Dissolve(1.0)
    return

label ch03_09_ministryvisit:
    scene black with fade
    "AUGUST 16, 2013 - 1700H"
    scene bg msci evening with fade

    window show
    nvl clear
    narr "On Monday morning, the principal announced that they would have a flag retreat this evening.{w} The bell rang, all students stopping no matter what their progress in cleaning was."
    narr "The students, their respective class presidents taking charge, arranged themselves at the quadrangle.{w} The Boy Scouts prepared the equipment and positioned themselves next to the country and school flagpoles."
    narr "The Student Council went up to the second floor, Sayo leading the studentry in singing the hymns. Silence fell once more as soon as those were done."
    narr "Waiting...{w=2.0} What could Mrs. Sokoguchi be planning to tell them now?"

    nvl clear
    narr "A minute passed, and it was not the principal who appeared before them."
    narr "It was Mrs. Ichimiya, a grim expression she wore.{w} Where was she?{w=1.0} The question nagged at their curiosity."

    nvl clear
    window hide

    t_ich "Good afternoon.{w=1.0} I regret to inform all of you that our beloved principal cannot join us. She has some {i}pressing matters{/i} to take care of."
    t_ich "That is not the problem, though. What we are to discuss this afternoon concerns {i}all of you{/i}.{w=1.5} I believe I am not in the position to indulge you in the details. There is someone here who is more qualified to do so."

    "She looked behind her in contempt.{w=1.0} Perhaps her emotion resonated to her audience whom were now picking up similar signals."

    f_mh8 "What's up with Mrs. Ichimiya? She looks uncharacteristically stern."
    f_st3 "It is as we feared. We have been paid a visit."
    f_mh8 "Visit?{w=1.0} By whom?"
    t_ich "Let us all welcome,{w=0.5} from the Kutsutochi Ministry of Education,{w=0.5} Ms. Saotomi Khai."

    "The students gave her a lukewarm applause, the weakest of which came from the Seniors."
    "Minister Khai received the microphone and placed it in front of her lips.{w} She took a gander down at the students, locking sights with as many as she could."

    minister "I am seeing some sour faces here to my right. You are Fourth Year students, yes?{w=1.0} Please behave according to your rank. The oldest of the pack influence the younger inexperienced ones."
    minister "If my father was still serving as the principal, he would not tolerate your showing of disrespect.{w=1.0} Commit that to memory.{w=1.0} {i}Claro?{/i}"

    "The Seniors affirmed in unison.{w} This satisfied the Minister's ears, yet her expression remained tact."

    minister "Then it's a pleasant afternoon to everyone.{w=2.0} I will not waste any more time sugarcoating my purpose here. You are all intelligent enough to work that out."

    "In this stage, the audience felt like Egyptians, Minister Khai as the cruel pharaoh. Towering over them is a harbinger of pestilence, the Moses whom nobody admires."

    minister "Maria St. Claire Institute shall be placed under probation.{w=1.0} This means that any outside activity you are planning to do -- including graduation -- must have our approval."
    minister "The cause is straightforward.{w=1.0} Whatever happened during the previous month may dramatically affect the entry rate for the following academic year."

    "{cps=10}Last...{w=1.5} month...?{/cps}"

    minister "As minister, I shall {i}not{/i} allow another innocent life to be taken under such incompetent supervision!{w=1.0} You let this happen within your yard, you take full responsibility."
    minister "How do you plan on explaining this to your parents?"

    "She is not stopping.{w=1.0} Her mouth keep on grinding out words.{w=1.0} The noise from the lower batches was worsening."

    unk "Shut the hell up already, you wretch..."
    minister "Is that right,{w=1.0} {cps=20}Mrs. Genkai and Mrs. Ritsuko?{/cps}{w=2.0} You kept Hiroshi Kano's death in the Student Council office a secret?"
    student "{cps=15}{i}What...?{w=1.0} You mean...{/i}{/cps}{w=2.0} No.{w=0.5} No.{w=0.5} No!"

    "They had run out of time.{w=1.0} Everyone knew that the murderer is still on the loose and is likely among their numbers.{w} Her question incited chaos, one that the Minister bothered not to quell."

    minister "Worry not. It is all taken care of.{w=1.0} We understand the effects of being ostracized for the unfortunate crimes. But that does not guarantee anything, does it not?"

    "If only one was there to witness the wincing faces of the Seniors and the teachers, some tearing up in silent fury. It fueled the hearts especially of those who made an effort to help close the case."

    minister "Thank you for having me, for I shall take my leave."

    "She placed her microphone on the table next to the sound system.{w} In front of nine hundred stunned teenagers, she walked to the principal's office without giving a damn."
    "For all those at the quadrangle, they felt soaked in her venom."

    scene bg guidancecounselor room with fade
    "AUGUST 16, 2013 - 1730H"

    window show
    nvl clear
    narr "What must they do? Everyone was at a loss."
    narr "Mrs. Ichimiya emerged from the principal's office and went straight to the Guidance Counselor's office.{w} Seated around the coffee table past the waiting area were Sayo, Ayumi, and Ms. Natsumoto."

    nvl clear
    window hide    

    show ayumi seriousleft at Three2 with Dissolve(0.2)
    show sayo seriousclosedpose at Three1 with Dissolve(0.2)
    t_ich "What a nuisance! Saotomi wants us to attend a whole-day meeting about {i}it{/i} tomorrow.{w=1.0} {i}*groan*{/i} How were they able to involve themselves in this?!"
    t_nat "Like a fly that keeps coming no matter how many times you swat it.{w=1.5} Have a seat, Sasha."

    "She sat on the chair across Ms. Natsumoto and poured herself a cup of green tea."

    t_ich "You two, aren't you supposed to be going home already?{w=1.0} Ayumi, what about the classroom?"
    show ayumi serious at Three2 with Dissolve(0.2)
    ayumi "Already done and locked up before the flag retreat."

    "{i}*rattle*{/i}"

    t_ich "Very efficient.{w=2.0} And what about you, Sayo-chan?"
    show sayo normaltalkpose at Three1 with Dissolve(0.2)
    f_sr5 "I stopped by to ask some advice from Ms. Natsumoto.{w=1.0} With all of this reaching the Ministry, the Student Council would be in the center of all scandals. It is difficult to think otherwise."
    t_ich "But it's more than that, I know, child.{w=1.0} How are you and Inoue getting along?"
    show sayo blankfacepose at Three1 with Dissolve(0.2)
    f_sr5 "We never spoke to each other after our scuffle.{w=1.0} Now that she is here, I am seeing more of my own detractors surface. They actually believe I orchestrated the abductions, whatever reason they find."
    t_nat "How about your peers -- fellow Council members and friends?"
    show sayo seriousnormalleftpose at Three1 with Dissolve(0.2)
    f_sr5 "The former, though I sense some awkwardness, I can manage.{w=1.0} The latter, in contrast..."
    t_nat "Say no more. It might stress you further."
    t_ich "Let's have a heart-to-heart with the entire class on Monday. I need to know who leaked that information to her."
    show ayumi  at Three2 with Dissolve(0.2)
    ayumi "I cannot guarantee IV-E's innocence, ma'am. Yet, I do remember giving strict orders not to snitch out the details of Hiroshi's death."
    t_ich "IV-E or not, this tells us that {i}someone{/i} did not comply. Or they did, but made the unfortunate mistake of confiding to their parents.{w=1.0} I made my son promise to keep it between ourselves."
    t_nat "Did anybody else know?"
    t_ich "None to my knowledge. My son understands how serious the consequences are.{w=1.0} {i}*chuckle*{/i} He's always my rantbox on our lovely Minister's nastiness during Board Meetings -- always ballooning the issue."
    show sayo seriousnormalpose at Three1 with Dissolve(0.2)
    f_sr5 "Not to accuse anybody, but if the whistleblower is not from IV-E, then where do we look?{w=1.5} IV-D is neutral according to Odome.{w=1.0} IV-C has integrity. I'd be shocked if they came from there.{w=1.0} IV-B, the same."
    show ayumi smile at Three2 with Dissolve(0.2)
    ayumi "Even though Ichirou's upset with you?"
    show sayo serioustalkpose at Three1 with Dissolve(0.2)
    f_sr5 "Ayumi...!"
    t_ich "Hold on. What is this now?"
    show sayo seriousclosedpose at Three1 with Dissolve(0.2)
    f_sr5 "Hmmmm... {i}*exhale*{/i}"
    show sayo seriousnormal at Three1 with Dissolve(0.2)
    f_sr5 "Ayumi meant that Ichirou's upset with me because I \"allowed\" Hiroshi's death to happen. Had I asked him to leave before meeting with Mrs. Genkai, he would probably still be alive today."
    t_ich "Probably? Whatever does that mean?"
    show sayo worriedtalkclosed at Three1 with Dissolve(0.2)
    f_sr5 "Please take it for what it is, ma'am.{w=1.0} Now's not the time to explain everything."

    "Ms. Natsumoto placed her empty teacup down and brought a pitcher of water to the table."

    t_nat "You shouldn't stoop down to Inoue's level -- if you think she did it, that is."
    show sayo worried at Three1 with Dissolve(0.2)
    f_sr5 "Definitely not!{w=1.0} No evidence is worse than illegal evidence to back up your pointer fingers."
    t_ich "Even so, there is also no definite proof you did not do it,{w=0.5} what with lack of witnesses and all. You weren't entirely under Ikuko's watch, too."

    "True. Sayo acknowledged this fair point."
    "Ms. Natsumoto looked at the clock, the minute hand close to twelve."

    t_nat "It's getting late. You two should wrap up your visit.{w=1.0} I'll be expecting an influx of students next week -- from Freshmen, especially."
    t_ich "I'll be speaking with Mrs. Genkai about the meeting tomorrow."
    t_nat "And you girls,{w=0.5} what are your plans from this point onwards?"
    show ayumi serious at Three2 with Dissolve(0.2)
    ayumi "Interrogation time tonight just to be extra sure.{w=0.5} Moral support, too.{w=1.0} And Sayo, it's better if you join in. Chat starts at 9 PM."
    show sayo blankface at Three1 with Dissolve(0.2)
    f_sr5 "You do that.{w=1.0} I might need time to reflect, so do not disturb me unless there is an urgent question. Make that clear at the group chat."
    show ayumi seriousclosed at Three2 with Dissolve(0.2)
    ayumi "Copy."

    "{i}*BEEEEEEEEEEEEEEEEEP*{/i}"
    "That was the guard's whistle.{w} Volleyball time is over. Pack up and leave, folks.{w} Doubt it anyone would find the urge to play after the bomb drop under an hour ago."
    hide sayo with Dissolve(0.2)
    hide ayumi with Dissolve(0.2)
    "Sayo and Ayumi opened the door a little after Yoshiro and Akira passed by. The latter pair were already beyond earshot."

    scene bg msci evening with fade
    show akira pe sigh at Three1 with Dissolve(0.2)
    show yoshiro pe blankleft at Three3 with Dissolve(0.2)
    f_ai2 "I knew it! I figured there was something wrong with Ichirou's plan as soon as that reptile showed up."
    f_ys6 "To his credit, though, it was a necessary evil.{w=1.0} Less impactful repercussions than waiting it out in the long run. I just can't believe how this blew up."
    show akira pe worried at Three1 with Dissolve(0.2)
    f_ai2 "How am I gonna explain this to my parents?{w=1.0} Man, that just killed all my plans for this weekend!"
    show yoshiro pe smile at Three3 with Dissolve(0.2)
    f_ys6 "Then wait for the storm to calm and remain low profile in the meantime.{w=1.0} Don't believe for one second the media isn't going to be involved soon."
    show akira pe worriedleft at Three1 with Dissolve(0.2)
    f_ai2 "I'm already tired of this.{w=1.0} Can't L.C. cancel their stupid game and allow us space to sort things out?"
    show yoshiro pe smiletalk at Three3 with Dissolve(0.2)
    f_ys6 "It's all planned out. They anticipated and willed for the media's involvement from the beginning. Isn't it the norm for psychopathic killers?"
    f_ys6 "Sayo --{w=0.5} or whoever L.C. is --{w=0.5} must have a deep-rooted hatred against us for orchestrating a conundrum this grave."
    show akira pe serious at Three1 with Dissolve(0.2)
    f_ai2 "So does the person who alerted Minister Khai. Probed, my behind."
    show yoshiro pe smirk at Three3 with Dissolve(0.2)
    f_ys6 "Hmph. Hehehehehehehe. It's a compromise of our privacy.{w=1.0} And I think I know who caused this."
    hide akira with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)

    scene bg freedompark night with dissolve
    "Akira, surprised at that last statement, waited until they were nearing Freedom Park to ask."

    show akira pe confused at Three1 with Dissolve(0.2)
    show yoshiro pe smile at Three3 with Dissolve(0.2)
    f_ai2 "I have someone in mind, too.{w=1.0} From IV-C?"
    show yoshiro pe smirk at Three3 with Dissolve(0.2)
    f_ys6 "Where else? {i}*snicker*{/i}{w=1.0} Her mother can't restrain her tongue, can she? That is the problem when you are best buddies with those in the seat of power.{w=1.0} You delude yourself in being a hero."
    show akira pe serious at Three1 with Dissolve(0.2)
    f_ai2 "She never changed. Always thinking about herself more than her child and the school.{w=1.0} I wonder how far her disgruntled attitude will take her."
    f_ys6 "Heh. For all I know, she's rolling on her belly like a rabid dog."
    show akira pe happy at Three1 with Dissolve(0.2)
    f_ai2 "That's nasty! Hahahahahahahahaha!"

    window show
    nvl clear
    narr "Their laugh echoed across the park. It would be detrimental to their health if they didn't.{w} After all, they were still hard-pressed in their quest to unmask the true culprit."
    narr "Ichirou already named one, but they could not produce solid evidence against her. If she was, how could she have done it?"
    narr "{cps=25}Or...{w=1.0} is there someone else they missed?{/cps}"

    nvl clear
    window hide

    show akira pe bored at Three1 with Dissolve(0.2)
    show yoshiro pe blankleft at Three3 with Dissolve(0.2)
    f_ys6 "Honestly, I have no idea who L.C. is yet. I'm not sure how long we'll take before we substantiate Ichirou's claim regarding Sayo's alternate identity -- if it is hers."
    show akira pe boredtalk at Three1 with Dissolve(0.2)
    f_ai2 "If not her, then my guess is Inoue."
    f_ys6 "Because she confessed to Kirisaki's murder?{w=1.0} Please remember her state of mind when she said that."
    show akira pe bored at Three1 with Dissolve(0.2)
    f_ai2 "Oh."
    show yoshiro pe smiletalk at Three3 with Dissolve(0.2)
    f_ys6 "If anything, only Inoue is in jive with Ichirou's accusation.{w=1.0} I only swing where the balance is heavier. Better to be safe than sorry in naming someone."
    f_ys6 "For now, we have some pieces we can work with. Should L.C. decide to show themselves before the 30th, we'll be ready."
    show akira pe confused at Three1 with Dissolve(0.2)
    f_ai2 "But the thing is, one of us has their own safety guaranteed in case Inoue's letter is telling the truth."
    show yoshiro pe smile at Three3 with Dissolve(0.2)
    f_ys6 "{cps=25}Indeed.{w=0.5} They could be anyone.{w=1.0} You, me, or any of the other six...{/cps}"
    hide akira with Dissolve(0.2)
    hide yoshiro with Dissolve(0.2)

    "{cps=15}Who is L.C.?{/cps}"
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
    scene bg livingroom2 with fade

    window show
    nvl clear
    narr "Home --{w=2.0} alone."
    narr "Mom and Pops needed to visit grandma in the hospital. Sis' is at her classmate's house working on some video project in Health Education.{w} That means I have the house to myself until early morning tomorrow."
    narr "Lucky they even thought of cooking tinola. My nose has been runny for three days. And the cold nights are not helping either."

    nvl clear
    narr "I skipped the TV. Nothing newsworthy this late.{w} The first thirty to forty-five minutes are alright, but beyond that is a plethora of worthless showbiz drama and internet memes."
    narr "The living room is silent. Not even the outside chatter is audible.{w} There is only the clicking of the laptop keys and the whirring of the electric fan."
    narr "Let's not make an already bad week even worse.{w} Man, she just had to butt in at the best moment, huh?"

    nvl clear
    window hide

    "{b}{i}*ding* *dong*{/i}{/b}"
    "Tsk! Sis' {i}always{/i} forgets things!"

    scene bg smallstreet night with dissolve
    "Keys in hand, I open the front door to find...{w=2.5}{nw}"
    show miyu bored at Three2 with Dissolve(0.2)
    "{cps=25}...someone else with a neutral expression.{/cps}{w=1.5} Honestly, I don't have time for this.{w=1.0} I already know where this is going."

    show miyu serious at Three2 with Dissolve(0.2)
    f_mh8 "Ichi,{w=0.5} don't close the door on me.{w=1.0} I'm not here to fight. I want to have a civil discussion."
    f_iy1 "About what?{w=1.0} You want to say sorry?{w=0.5} You're going to persuade me to change my mind?{w=1.0} Forget it, buddy. Good night."
    show miyu pissed at Three2 with Dissolve(0.2)
    f_mh8 "This is very important.{w=1.0} If only you would listen, we can straighten things out{w=0.5} and work out a reasonable solution to the bigger problem --{w=1.5} {i}our{/i} problem."

    "The neighbors hushed.{w=1.0} They feasted their eyes on this little scene between us and possibly composing some sort of story to pass around."
    "{i}*rattle* *creak*{/i}"

    f_iy1 "I'll consider.{w=1.0} Come inside or you'll cause a fuss. I don't want to be the sole audience of Mom's homily when she gets home."
    show miyu proudclosed at Three2 with Dissolve(0.2)
    f_mh8 "Thank you."
    hide miyu with Dissolve(0.2)

    scene bg livingroom2 with dissolve
    "He stepped inside and waited as I locked the gate.{w} I invited him in, getting a pitcher of cold water and two glasses for the both of us. He drank without inspection."

    show miyu naughty smile at Three2 with Dissolve(0.2)
    f_iy1 "You haven't dressed. That's unusual of you."
    f_mh8 "I didn't feel the need to. I'll only switch to my casuals once I'm ready to sleep."
    f_iy1 "Still, the sweat accumulated all day does chip damage to your immune system."
    f_iy1 "{i}{b}*COUGH*{/b} *COUGH* *sniff*{/i}"
    show miyu naughty talk at Three2 with Dissolve(0.2)
    f_mh8 "Case in point -- you."
    hide miyu with Dissolve(0.2)

    scene bg diningroom with dissolve
    "I excused myself to get a Lagundi tablet and dissolved it in my drink. I refilled both of our glasses and placed the pitcher on the dining table."

    scene bg livingroom2 with dissolve
    show miyu smile at Three2 with Dissolve(0.2)
    f_iy1 "What do you hope to get from this, Miyu? A truce?"
    f_mh8 "If you want to.{w=1.0} But you can't be convinced to agree to my terms. That's a well-known fact."
    f_iy1 "Tch. {i}*snicker*{/i} That hit the spot."
    show miyu pissedclosedpose at Three2 with Dissolve(0.2)
    f_mh8 "Let me make one thing clear.{w=1.0} I came here of my own accord."
    show miyu pissedpose at Three2 with Dissolve(0.2)
    f_mh8 "It's true that I spearhead the people maintaining Sayo's innocence, for I have my own reasons to believe as such.{w=1.5} What about you?"

    "Shrug.{w=1.0} It is the very question I dreaded discussing."

    show miyu naughty focuspose at Three2 with Dissolve(0.2)
    f_mh8 "When you made that dramatic act nearly a month ago, I was impressed by your bravado.{w=1.0} Foolish,{w=0.5} but very brave.{w=1.0} You might have good reasons to hold onto your belief.{w=1.0} Tell me. Why incriminate her?"
    f_iy1 "Don't be daft, Miyu. Of the six witnesses there, th--{w=1.0} the four of us were far away from the crime scene.{w=1.5} Did you stop to think that she might not have been under Ikuko or Mrs. Genkai's watch the whole time?"
    show miyu naughty focuspose2 at Three2 with Dissolve(0.2)
    f_mh8 "Or vice versa for Ikuko, though I genuinely believe she's innocent.{w=2.0} Why reason out like that? Is it more convenient?"
    f_iy1 "Oh, not just convenient. It's all over the place!"
    show miyu pissedpose at Three2 with Dissolve(0.2)
    f_mh8 "Why? Answer this one goddamn question first and I might start believing your word.{w=1.0} Motive. What has Kirisaki and Hiroshi done to her? Trigger her temper?"
    f_mh8 "Ichi, you know her longer than I do.{w=1.0} But why does it seem like we've been seeing {i}two different Sayos{/i} especially when this whole mess began?"
    f_iy1 "Listen to yourself. How much do {i}you{/i} really know the girl?"
    f_iy1 "If I had to make a guess, it would be a generic one.{w=1.0} Maybe power?"
    show miyu pissedleftpose at Three2 with Dissolve(0.2)
    f_mh8 "On what end? She's already the studentry representative and is among the best students of our batch."
    f_iy1 "To ensure her seat at the valedictorian's throne come graduation day."
    show miyu pissedclosedpose at Three2 with Dissolve(0.2)
    f_mh8 "I liked it better before you said that. {i}*sigh*{/i}{w=1.0} If that's the case, then why didn't she kill {i}you{/i} first, Mr. Top 1 Overall? I sense a logic error somewhere."

    centered "{color=#808080}{cps=25}{i}Unbelievable.{w=0.5} This is real.{w=1.0} I am hearing myself spout out these unjustified thoughts.{w=1.0} It is all hatred.{w=2.0}\nWhen was the last time I heard a \"good job\" from anyone?{w=1.0} Very recently, I'm sure.{/i}{/cps}{/color}"

    show miyu naughty closepose at Three2 with Dissolve(0.2)
    f_mh8 "Your mind is clouded.{w=1.0} It seems one month isn't enough to rehabilitate it."
    f_iy1 "I get your point. No need to hammer it in ad infinitum."
    show miyu naughty closepose2 at Three2 with Dissolve(0.2)
    f_mh8 "Yes, but it is a remedy against ego strokes.{w=1.0} Epistemology is the heart of the scientific method. Under its umbrella, egoism is nowhere to be found."

    "{cps=20}Is that right...?{/cps}"

    show miyu naughty smile at Three2 with Dissolve(0.2)
    f_mh8 "Now, is it clear who is acting more off the rails here?"
    f_iy1 "Hmmmmmmmm...{w=2.0} Whatever."

    if parse_bin(bonus_b1_i,2):
        show miyu naughty talk at Three2 with Dissolve(0.2)
        f_mh8 "If you look at it from a certain perspective, one may think that everything Inoue experienced was just a fever dream."

        "That is interesting.{w} It explains the more absurd and fantastical details of her story.{w=1.5} Blood-pulsed walls, monsters, and reanimated corpses, pfeh! That's something you would read out of a Clive Barker story."

        f_iy1 "So, only the major beats were true.{w=1.0} There is the actual abduction, Kyou being burned to a crisp, the nursery rhyme, and the disposal."
        f_iy1 "The burnt corpse we found being taken into the hospital is confirmed to be Kyou, the damage as described in Inoue's story.{w=2.0} And her mental state?{w=1.0} The aftermath of a traumatic event."
        show miyu bored at Three2 with Dissolve(0.2)
        f_mh8 "True.{w=1.0} What about the events in the facility's living room?"
        f_iy1 "That's where the morphing painting can be found.{w=1.0} A monster broke free and strangled Inoue to near-death.{w=0.5} Prior to that she saw Kyou's corpse."
        f_mh8 "Did we miss anything?"
        f_iy1 "None that I can remember."
        show miyu pissed at Three2 with Dissolve(0.2)
        f_mh8 "Paintings like that don't exist.{w=1.0} Last time we both saw something of the like was in a Harry Potter movie."
        show miyu naughty talk at Three2 with Dissolve(0.2)
        f_mh8 "{cps=25}That gives me an idea, though...{/cps}"
        f_iy1 "What is that?"
        show miyu naughty smile at Three2 with Dissolve(0.2)
        f_mh8 "L.C., as far as we know, is a bodiless entity. Are they one or many?{w=1.5} The one who spoke at the mock examinations was different from what was described in Inoue's story."
        f_mh8 "What is consistent are two things:{w=1.0} the presence of two child-like sadists accompanying them,{w=0.5} and the merciless toying they do with one of his potential victims."
        f_iy1 "It's still a bit different from what we encountered that night.{w=1.0} {i}*COUGH* *sniff*{/i}"
        show miyu bored at Three2 with Dissolve(0.2)
        f_mh8 "From height and voice alone, {i}that thing{/i} is not Sayo."
        hide miyu with Dissolve(0.2)

        scene bg village night with dissolve
        show silhouette at Three2 with Dissolve(0.2)
        "{i}Condolence!{w=1.5} And I'm sorry to see your friend go...{/i}"
        hide silhouette

        scene bg livingroom2 with dissolve
        show miyu bored at Three2 with Dissolve(0.2)
        f_iy1 "The volume was not higher than a loud whisper where you can still hear the crickets sing.{w=1.0} \"Condolence,\" they said."
        show miyu pissedclosedpose at Three2 with Dissolve(0.2)
        f_mh8 "Can you describe them for me? I only saw their back."

        centered "{color=#808080}{cps=25}{i}What's the point of describing a silhouette?! I couldn't even distinguish anything aside from the road under the faint moonlight.{/i}{/cps}{/color}"

        show miyu proudclosed at Three2 with Dissolve(0.2)
        f_mh8 "I figured."
        f_iy1 "I haven't said anything."
        show miyu naughty smile at Three2 with Dissolve(0.2)
        f_mh8 "Even nothing implies something.{w=1.0} Everything is crucial when we're all fumbling in the dark."
        show miyu naughty smirk at Three2 with Dissolve(0.2)
        f_mh8 "{cps=20}So predictable...{/cps}"
        f_iy1 "{i}*sniff*{/i}"
        show miyu naughty smile at Three2 with Dissolve(0.2)
        f_mh8 "How about I share my side so you can think more clearly."
        hide miyu with Dissolve(0.2)

        scene bg diningroom with dissolve
        "I excused myself to get a liter of Coke from the fridge -- despite my condition.{w=1.0} So what if I have a cold? No one's here to object."

        scene bg livingroom2 with dissolve
        show miyu pissedclosed at Three2 with Dissolve(0.2)
        "I poured ourselves three quarters of a glass each.{w} He didn't drink immediately.{w=1.0} So did I."

        show miyu pissed at Three2 with Dissolve(0.2)
        f_mh8 "Black.{w=2.0} I remember it clearly.{w=1.0} When it phased through me, everything plunged into darkness.{w=1.0} My blood sapped,{w=1.0} body numbened,{w=1.0} ears ringing."

        "He took his glass and gave it a slight shake, peering inside instead of downing it."

        show miyu naughty talk at Three2 with Dissolve(0.2)
        f_mh8 "If you hadn't shouted, I wouldn't have snapped back to reality."
        f_iy1 "But I never saw you lying on the side of the road. You can see a few feet off the road."
        show miyu naughty smile at Three2 with Dissolve(0.2)
        f_mh8 "Because I landed somewhere beyond those few feet.{w=1.0} Could be in a pocket dimension for all I know."

        "Which coincides with my own point. I must have focused too much on the perp to see anything else."

        show miyu pissedclosedpose at Three2 with Dissolve(0.2)
        f_mh8 "If we can't find a solid explanation -- other than what you suggested earlier -- for Inoue's predicament,{w=1.0} then what I experienced might be a stepping stone."
        f_mh8 "As I mentioned, I could have been transported in an alternate dimension separate from our own.{w=1.0} Even though it was brief, I can still remember walking down an endless tunnel."
        f_iy1 "But they did suffer through that Hell, right?"
        show miyu pissedleftpose at Three2 with Dissolve(0.2)
        f_mh8 "And managed to return dead or broken.{w=1.0} Unless we prove the facility's existence and pinpoint its location, what I said is our only explanation."
        f_iy1 "You came back in one piece. That's a hole in your theory."
        show miyu naughty focuspose2 at Three2 with Dissolve(0.2)
        f_mh8 "It was thanks to you. Communication from the outside world works wonders. {i}*chuckle*{/i}"
        f_mh8 "If L.C. plays by his rules, then it's natural that you, me, and Inoue be spared.{w=1.0} They had already had a victim in Kyou Kirisaki. Why kill more than necessary at the time?"
        show miyu naughty closepose at Three2 with Dissolve(0.2)
        f_mh8 "Law of Diminishing Returns, Ichi.{w=1.0} That's what keeps the game {i}fun{/i} and {i}exciting{/i}."
        f_iy1 "Economics aside,{w=0.5} you're saying that L.C. is some sort of an alchemist who uses magic as part of their M.O.?"
        show miyu embarrassed at Three2 with Dissolve(0.2)
        f_mh8 "AHAHAHAHAHAHAHAHAHAHAHA!!!"
        show miyu proudclosed at Three2 with Dissolve(0.2)
        f_mh8 "{cps=25}Ah... You're hopeless, Ichi.{w=1.0} Roped in like a gullible fish.{/cps}"
        f_iy1 "Then what? A magician?"
        show miyu naughty smirk at Three2 with Dissolve(0.2)
        f_mh8 "And an actor.{w=1.0} Remember,{w=0.5} we can't be certain."

        "He took a sip of Coke while retaining that malicious smirk.{w} Now, I dislike him even more."

    elif parse_bin(bonus_b1_g,2):
        show miyu bored at Three2 with Dissolve(0.2)
        f_mh8 "Enough of these two girls for now.{w=1.0} Let's talk about you.{w=1.0} There has to be a reason for you lashing out at the conference room."
        show miyu naughty focuspose2 at Three2 with Dissolve(0.2)
        f_mh8 "Tell me. What did you see?"
        f_iy1 "The same thing you all did. The eighth letter stated it clearly:{w=1.0} one of us is L.C.{w=1.0} It wasn't written in intelligible handwriting; rather, in type font."
        f_mh8 "Mhm."
        show miyu naughty focuspose at Three2 with Dissolve(0.2)
        f_mh8 "Now, consider this.{w=1.5} It is true that Kyou died of third-degree burns -- you and I can attest to that.{w=1.0} But when?{w=1.0} Was it as Inoue said to have taken place,{w=0.5} or {i}sometime before{/i}?"
        f_iy1 "What do you mean? Does it even matter?"
        show miyu pissedleftpose at Three2 with Dissolve(0.2)
        f_mh8 "Inoue has taken responsibility for his death.{w=1.0} It matters, definitely, if we want to clear her name.{w=2.0} Think back to the details and you'll find a lot of problems becoming apparent."
        hide miyu with Dissolve(0.2)

        "I got ourselves two glasses and a liter bottle of Coke.{w} He looked at me strangely.{w} Heck, I'll have myself a glass of soda even if I have a cold. It helps me to think."
        "Related to the question, that instance would be..."

        scene white with dissolve
        scene bg school outside with dissolve
        show inoue noglass worried at Three2 with Dissolve(0.2)
        show sumiko seriousleft at Three1 with Dissolve(0.2)
        c_is4 "Kirisaki wasn't himself. When I tried to approach him, he ran away as if he saw {i}something{/i}."
        show inoue noglass sadleft at Three2 with Dissolve(0.2)
        c_is4 "I could sense the bloodlust in his eyes.{w=1.0} There is no mistaking it.{w=1.0} He wasn't himself at all. Believe me!"
        show akira boredtalk at Three3 with Dissolve(0.2)
        f_ai2 "It couldn't have been him -- hard to believe if it was. Maybe the Kirisaki you encountered after the corpse was an impostor?"
        hide inoue
        hide sumiko
        hide akira

        scene bg school outside dark with dissolve
        centered "{color=#808080}{cps=25}{i}Was he alluding to this idea?{w=1.0} My doubts about her before Sayo came along were true?{w=2.0}\nIf so, then that explains her ill temper and her superhuman strength when she knocked Miyu and Sumiko aside after she snapped.{/i}{/cps}{/color}{w=4.0}{nw}"

        scene bg underwater with dissolve
        centered "{color=#808080}{cps=25}{i}What if Inoue drowned in that pool?{w=1.0} What if the Inoue we're seeing now is nothing more than a clone?{w=1.0} Its sentience is being controlled.{w=1.0} But is that...{/i}{/cps}{/color}{w=3.0}{nw}"

        scene bg livingroom2 with dissolve
        show miyu pissedleftpose at Three2 with Dissolve(0.2)
        f_iy1 "Is that certain? Why aren't seeing copies of Hiroshi and Kyou if Copy-Inoue is dwelling among us?"
        show miyu pissedpose at Three2 with Dissolve(0.2)
        f_mh8 "You mean \"skinwalking\" as her?"
        f_iy1 "Something like that?"
        show miyu naughty closepose at Three2 with Dissolve(0.2)
        f_mh8 "Like I'd know what sort of research is being held at that mysterious facility. Have we already reached that epoch where we can transfer and upload a sentience to a body?"
        f_iy1 "Or she's being possessed?{w=2.0} But that doesn't make sense. The three of us were with Inoue the whole day one weekend.{w=1.0} She seems pretty normal."
        f_mh8 "Which also means she wasn't triggered."
        f_iy1 "{cps=30}No.{w=1.0} But she was {i}very{/i} close to snapping.{/cps}"

        "I left it as that. Like he cares about the details of our trip, nor I do with their own investigation."

        show miyu pissedclosedpose at Three2 with Dissolve(0.2)
        f_mh8 "One more thing...{w=1.0} related to something the eight of us received the weekend after Hiroshi's murder."
        f_iy1 "I only remember mine and Inoue's.{w=1.0} The others are either too cryptic or innate that one wouldn't bother reading them."
        show miyu naughty closepose at Three2 with Dissolve(0.2)
        f_mh8 "I'm pertaining to the eighth letter, so you won't have to worry about recalling the others."
        f_iy1 "Why? Are you going to retract your claim that all the letters are telling the truth?{w=1.0} If there is a hidden message when you piece all eight together, I would love to know! {i}*COUGH* *sniff*{/i}"
        show miyu naughty focuspose at Three2 with Dissolve(0.2)
        f_mh8 "{cps=25}No, Ichi...{w=1.0} The rules stand by themselves just fine.{/cps}"
        f_iy1 "Spit it out. What about that damn eighth letter?"
        show miyu naughty focuspose2 at Three2 with Dissolve(0.2)
        f_mh8 "Before I state the major problem in its contents, I need you to recall one particular statement L.C. made when they spoke to us through the intercom."
        f_iy1 "Clue?"
        show miyu naughty closepose2 at Three2 with Dissolve(0.2)
        f_mh8 "L.C. is {i}supposedly{/i} a gentleman, isn't he?{w=1.0} A good sport?"
        f_iy1 "L.C. promised to {i}play fair{/i}."
        show miyu naughty closepose at Three2 with Dissolve(0.2)
        f_mh8 "{cps=20}Play fair...{/cps}{w=1.0} Do you think sending a message whose purpose is to divide ourselves --{w=1.0} which {i}you{/i} caused --{w=1.0} is playing fair?"
        f_iy1 "Think, Miyu!{w=1.0} When have you ever heard of a killer-in-a-group story where everyone stays united until just before the reveal?{w=1.0} {i}*COUGH*{/i}{w=0.5} It has always been the intended way."
        f_iy1 "Even if the letter's contents were different --{w=1.0} presenting us with a choice to solve the crimes and catch the criminal indivdually or collectively --{w=1.0} it all comes down to the illusion of choice."
        show miyu naughty talk at Three2 with Dissolve(0.2)
        f_mh8 "You have an excellent point there.{w=1.0} But have you considered if the letter presents us with the illusion of the {i}absence{/i} of choice?"
        f_iy1 "Huh?!"
        show miyu proudclosed at Three2 with Dissolve(0.2)
        f_mh8 "Playing fair can mean leaving your Game Master role and abiding by the rules you set to your own subjects.{w=2.0} It can also mean watching the game unfold from your throne and not bother interrupting."
        f_mh8 "And you reacted harshly without even stopping to consider that. {i}*sigh*{/i}"
        f_iy1 "Enough already! You're starting to sound like Mom.{w=1.0} {i}*groan*{/i} My head..."

        show miyu naughty smile at Three2 with Dissolve(0.2)
        "He slowly fell back to the sofa, crossing his arms and planting his feet on the ground.{w} He sipped a bit of Coke while keeping his eyes on me."

    "I took a sip from my glass.{w} The soda has already lost some of its --{nw}"
    hide miyu

    scene white with vpunch
    c_iy1 "{b}*COUGH*{w=1.0} *COUGH*{w=1.0} *COUGH*{/b}"
    f_mh8 "Ahem!{w=0.5} Ahem!{w=0.5} Ahem!{w=1.0} Drinking Coke when you have a cold -- what a brilliant idea!"

    scene bg livingroom2 with dissolve
    show miyu naughty smile at Three2 with Dissolve(0.2)
    "I grabbed two plys of tissue from the box on the table, wiping my mouth and the tears on my eyes."

    c_iy1 "Shut up.{w=0.5} Stop acting like you didn't do the same."
    show miyu naughty blush at Three2 with Dissolve(0.2)
    f_mh8 "Hehehehehehe. You got me."

    "I took another sip, this time increasing the amount to an entire glass. It didn't cause a second coughing fit.{w=1.5} Still, a glass of water is still the standard dose. Somebody here is concerned for my well-being."

    f_iy1 "{i}*EXHALE*{/i}{w=1.0} Alright.{w=0.5} I've heard enough of your arguments.{w=1.0} Know this, however, will not mean an immediate change in my opinion. I still maintain Sayo's guilt."
    show miyu pissedclosed at Three2 with Dissolve(0.2)
    f_mh8 "What can I do? Change by words do not take effect instantaneously.{w=1.0} Understand that I came here as a visitor and a diplomat."
    f_iy1 "You've realized.{w=1.0} Now, would you --{nw}"
    hide miyu

    scene black
    centered "{color=#bd0000}{cps=25}{i}Your heart is an unbreakable stone...{w=1.5}\nA narrow-minded fool you are just like she was...{/i}{/cps}{/color}"

    scene bg livingroom2
    show miyu serious at Three2
    f_mh8 "Would I what?{w=0.5} Leave?{w=1.0} I'm about to do just that."
    c_iy1 "{cps=20}I mean... uuuhhh... Did you hear?{/cps}"
    show miyu talk at Three2 with Dissolve(0.2)
    f_mh8 "Hear what?"
    hide miyu

    centered "{color=#bd0000}{cps=25}{i}When will you acknowledge the truth?{w=1.0}\nUntil when will you run away from it?{w=1.0} Forever?{w=1.5}\nYou shall not live forever... Humbug...{/i}{/cps}{/color}"

    scene bg abyss with dissolve
    "My fingers picked up a sign of fever from my neck. My temples ached and my throat gradually became sore.{w} I rested my head on the couch looking up to the ceiling."

    f_mh8 "You shouldn't have drunken Coke in your state. You're having a bad fever, Ichirou."
    d_iy1 "{cps=20}Thanks... Captain...{/cps}"
    f_mh8 "Do you need help before I leave you? Comforters, check-up, anything?"

    centered "{color=#bd0000}{cps=25}{i}Kukukukukuku...{w=1.0} Kyekyekyekyekye...{w=1.0}\nGahahahahahahahahaha!{w=1.0}\nAHAHAHAHAHAHAHAHAHAHAHA!!!{/i}{/cps}{/color}"

    "My vision switched back and forth between clarity and bluriness. I almost knocked the Coke bottle in my confusion."

    f_mh8 "Hey! Are you sure you'll be fine tonight?"
    d_iy1 "I'll be.{w=1.0} Just go."

    "I searched my pocket for the gate and house keys and threw them to the table."

    scene red with dissolve
    unk "{cps=25}{i}Swing, swing, swing...{w=1.5} Looky what we have here.{w=1.0} We have a playmate! Two of them, in fact.{/i}{/cps}"
    unk "{cps=15}{i}Puku.{w=1.0} One of them looks no good.{w=1.0} The other one I prefer.{/i}{/cps}"

    "Damn it..."

    f_mh8 "{cps=20}Ichi,{w=1.0} I can ring up your --{/cps}{nw}"
    r_iy1 "Just see yourself out, Mi-kun! You shouldn't be here!"
    f_mh8 "What are you saying?! I can't leave you like this!"
    r_iy1 "You're going to get killed.{w=1.0} Just listen to me. They're already here..."
    
    scene black with fade
    f_mh8 "Then why are you driving me away?"
    r_iy1 "JUST GO!!!"

    window show
    nvl clear
    narr "In my bouts of fever, I can barely recall anything that happens for the next few hours. If they are conneccted to household routines, then that makes them exceptions."
    narr "I shut the gate and our front door, turned the lights and all appliances off, and threw myself to bed. Creak...{w} The rest I can't remember."
    narr "I hope they go away.{w} Leave us alone, please..."

    nvl clear
    window hide

    return

label ch03_10B_innocent:
    if path_b1 == 0:
        $ path_b1 = 1

    scene black with fade
    "{color=#5decff}AUGUST 26, 2013 - 1150H{/color}"
    scene bg classroom2 with fade

    window show
    nvl clear
    narr "Lunch -- not at the office, but here at my homeroom. It is better if I have companions around rather than spending half the time alone in that place."
    narr "Ever since the day Minister Khai showed up, all the students are on edge.{w} The poor children didn't need to find out about that gruesome incident. They are too young to understand."
    narr "The probation being the worst penalty might have been luck, but it is still an unpleasant bureaucrat who handed it down to us.{w} We'd rather have the media out of this."
    narr "I took my journal and finished the afternoon's entry."

    scene bg book with fade
    nvl clear
    narr "{i}August 26, 2013{/i}"
    narr "{i}What fruits have our investigations borne?{/i}"
    narr "{i}I would sound pessimistic if I said, \"Nothing.\" That is far from the truth.{/i}"
    narr "{i}Based on evidence alone (and Miyu's theory), Fuuko Rikiyama's murder is a sufficient baseline for subsequent analyses. Those who came after her may no longer be necessary, but will remain relevant. The methods are definitely similar to L.C.'s own, but the motives are still blurry.{/i}"

    nvl clear
    narr "{i}As the days pass, thoughts about myself begin to manifest, some of which birthed from recent events. Do I truly know myself by heart? If any was to ask themselves that, it would be a \"no.\"{/i}"
    narr "{i}Human ideals are dynamic, their motivations ever-changing. Those who believe otherwise have not yet seen much, or have seen it all. The third is of those who remain a shell -- a circle in a spherical universe. Why do they? Manipulation or a misguided dogma, perhaps?{/i}"
    narr "{i}But why? Why do people let themselves be deluded? I don't understand. They have the pieces and the ability to form the answers to their questions, yet no significant effort is made.{/i}"
    narr "{i}On the other hand, even those who are aware of their actions trudge to their end goal in vain. I admit I am part of these people. That weekend was an exercise in futility. Oh, we did make progress, but we are ultimately at a standstill.{/i}"
    narr "{i}So long as we are divided like this, we will never seek our desired answers.{/i}"

    nvl clear
    narr "{i}Am I L.C.?{/i}"
    narr "{i}I do not buy whatever that proposition implies. No. I would never spearhead such acts of inhumanity. Only a ruthless monster would even dare to concoct such a diabolical plan.{/i}"
    narr "{i}That is the truth I believe in, and so does my family and friends who know me well. We do not need to be lawyers to present arguments to determine the verdict regarding my guilt or innocence. We are scientists whose conclusions depend on evidence, not words or spiteful emotions.{/i}"
    narr "{i}I say this if I were Henry Jekyll. Of course, he would defend himself like that -- most true criminals would. The difference is that everyone knows he can summon Hyde if he wills it. I have no \"Hyde\" one might speak of.{/i}"
    narr "{i}Maybe... Just maybe... Ichirou is seeing a Hyde, after all.{/i}"

    nvl clear
    narr "{i}Let us take that into consideration. Then that means I did murder a defenseless person in the dark. That means I own an unidentified complex where I perform heinous experiments.{/i}"
    narr "{i}Now, if I accept those implications and confess to the police, would they believe me? Nay. Let the evidence speak for themselves. The lead detective is not an idiot himself.{/i}"
    narr "{i}I stand by my own words: I am not L.C. Never will I endanger our future -- mine and MSCI's -- over some petty grudge or some other twisted fulfillment.{/i}"
    narr "{i}Whatever accusations they made against me, I shall see the end of them.{/i}"
    narr "{i}Whoever L.C. is, I pray they surrender and stop this madness as soon as possible. It is utterly pointless to uphold this charade.{/i}"

    nvl clear
    narr "{i}Assuming none of us has fallen victim yet, we still have the entire week to catch the culprit.{/i}"
    narr "{i}I intend to settle our differences now, lest we be consumed by our own pride and folly. It would be difficult to remedy if we let the tumor balloon and become incurable. Godspeed.{/i}"
    narr "{i}'Til I ramble again,{w=1.0}\nSayo Ronoroa{/i}"

    nvl clear
    window hide

    scene bg classroom2 with fade
    show ikuko smile at Three2 with Dissolve(0.2)
    "I bound the journal and found Ikuko by my side. She had just finished her lunch and was reading her New Testament with Psalms and Proverbs."

    show ikuko talk at Three2 with Dissolve(0.2)
    ikuko "Proverbs 16:18 says, \"Pride goes before destruction, a haughty spirit before a fall.\""
    show ikuko smile at Three2 with Dissolve(0.2)
    ikuko "It may not be the best greeting I can offer you this afternoon. I still hope it serves you well for the oncoming days."
    f_sr5 "It seems you have read from my heart. I have the same sentiments as that verse.{w=1.0} Those astray will soon realize their mistake and help solve this conundrum. But for how long, I cannot say."
    ikuko "I'm sure the Heavens favor you.{w=1.0} Whatever the outcome, we can only hope the best for everyone."
    f_sr5 "You're in the right track.{w=1.0} {i}*sigh*{/i} I can't thank you enough for staying through all these trying times."
    f_sr5 "Even I cannot distinguish the truth from the lies, what with the lack of knowledge serving as the biggest obstacle in doing so."
    show ikuko worried at Three2 with Dissolve(0.2)
    ikuko "Hmmmmmm...{w=2.0} It pains me to say this, Sayo-chan.{w=1.0} I dread the day when you drown in the lies conjured up by those against you and those \"lies\" turn out to be the truth."
    f_sr5 "No, no. {i}*chuckle*{/i}{w=1.0} These things ought to remain as theories."
    show ikuko blank at Three2 with Dissolve(0.2)
    ikuko "You would never kill?"
    f_sr5 "Not for petty reasons.{w=1.0} If it would be a means to bring an end to this, then I shall gladly stain my hands in blood. Otherwise, what interest is there to behold?"
    show ikuko worried at Three2 with Dissolve(0.2)
    ikuko "Are you sure?!{w=1.0} I thought you told me otherwise?"
    f_sr5 "{cps=25}Not for {i}petty reasons{/i}.{/cps}"
    f_sr5 "{cps=20}Trust me.{/cps}"

    show ikuko blank at Three2
    "{b}{i}*knock* *knock*{/i}{/b}"
    hide ikuko with Dissolve(0.2)

    scene bg classroom1 with dissolve
    show hikaru surprised2 at Three2 with Dissolve(0.2)
    "Someone is at the door.{w} Hikaru looked towards the direction of my seat, flashing a handwave to beckon me over."
    hide hikaru with Dissolve(0.5)

    scene bg msci with dissolve
    "I bid Ikuko farewell and followed Hikaru outside. Sumiko was waiting at the bench."

    show hikaru surprised2 at Three1 with Dissolve(0.2)
    show sumiko surprised2 at Three3 with Dissolve(0.2)
    f_sr5 "Where's Miyu?"
    show hikaru worried at Three1 with Dissolve(0.2)
    show sumiko seriousleft at Three3 with Dissolve(0.2)
    f_hy10 "{cps=20}Ummmmmm...{/cps}"
    f_sr5 "Is something the matter?"
    show hikaru worriedtalk at Three1 with Dissolve(0.2)
    f_hy10 "He won't be joining us.{w=1.0} Instead, he left us with this."

    show hikaru worriedclosed at Three1 with Dissolve(0.2)
    centered "{i}Next phase. I have done my part.\n\n-- Miyu (08/23/2013){/i}"

    f_sr5 "I see.{w=1.0} Come along, you two."
    hide hikaru with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)

    scene bg school fields with dissolve
    show hikaru worried at Three1 with Dissolve(0.2)
    show sumiko serious at Three3 with Dissolve(0.2)
    "We sat on the auditorium steps facing the field. Though the ground felt warm, we need not worry as the clouds are concealing the Sun."

    f_sr5 "Let's go over what we know so far.{w=2.0} We can link Kyou and Hiroshi's deaths with a few common elements."
    show sumiko serioustalk at Three3 with Dissolve(0.2)
    f_st3 "Killed in their sleep,{w=0.5} or rather,{w=0.5} in a trance-like state."
    f_sr5 "And?"
    show sumiko seriousleft at Three3 with Dissolve(0.2)
    f_st3 "Both of their corpses have traces of drugs, administered a long time before their deaths.{w=1.0} Although, I wouldn't say the level consent is the same."
    f_st3 "Hiroshi, for instance, suffered from narcolepsy, or was it insomnia?{w=1.0} He started bringing sleeping pills to school after his First Quarter disqualification. I even asked him about it during one of our 7-11 sessions."
    f_st3 "Kirisaki?{w=2.0} No, I don't think so.{w=1.0} We've pulled all-nighters before whenever we did group assignments and often had difficulty sleeping, but we never took sleeping pills."
    f_sr5 "I agree. I sometimes catch him sleeping during breaks but always alert during class."
    show hikaru serioustalkleft at Three1 with Dissolve(0.2)
    f_hy10 "So, our conclusions are correct. There are only a few questions left to answer and we're all set."
    show sumiko surprisedtalk at Three3 with Dissolve(0.2)
    f_st3 "If you didn't know already, Ichirou's group did the same thing as us. Akira told me just recently."

    show hikaru seriousleft at Three1 with Dissolve(0.2)
    "So I have heard, but did not bother."

    show sumiko surprised2 at Three3 with Dissolve(0.2)
    f_sr5 "Fill me in. Hikaru mentioned this before but I don't know the exact details."
    show sumiko surprisedtalk at Three3 with Dissolve(0.2)
    f_st3 "He said they went to Kutsutochi North to research about key people and points of interest related to the case.{w=1.0} Not sure how far they went, but he said they discovered some questionable threads...{w=1.5} {i}at least{/i}."
    f_sr5 "Did he specify what those are?"
    show sumiko surprised at Three3 with Dissolve(0.2)
    f_st3 "No. He clammed up on me before I was able to get anything.{w=1.0} Maybe it's because I lashed out on him before."
    f_sr5 "{cps=25}That's unfortunate...{w=1.5} No.{w=1.0} {i}Quite{/i} fortunate, actually.{/cps}"

    "Oh, yes. It has been over a month.{w=1.0} The way Sumiko was disgusted and lashed out at the three boys' disposition...{w=1.0} {i}That{/i} was genuinely terrifying."

    show hikaru serious at Three1 with Dissolve(0.2)
    f_hy10 "I think we should stop this.{w=1.0} It's obvious to me you didn't do it. L.C.'s watching us from afar, doubling over thinking that this is just a silly game."
    f_sr5 "And the only way to stop this silly game is to force itself to do so.{w=1.0} How can it be done? Ask yourselves."

    show hikaru smirk at Three1 with Dissolve(0.2)
    show sumiko angry at Three3 with Dissolve(0.2)
    "Sumiko and Hikaru looked at each other, the latter winking with a sly smile."

    show hikaru smile at Three1 with Dissolve(0.2)
    f_hy10 "So, we'll follow through with my suggestion?"
    f_sr5 "I'm ready. Let's sort this out with the other group, shall we?"
    show sumiko serioustalk at Three3 with Dissolve(0.2)
    f_st3 "With that hard-head? {b}*groan*{/b}{w=1.0} Absolutely not!"
    show hikaru worried2 at Three1 with Dissolve(0.2)
    f_hy10 "Sayo-chan, about what you said regarding Inoue's grudge...{w=1.0} I felt it, too."
    show sumiko seriousleft at Three3 with Dissolve(0.2)
    f_st3 "When she made a ruckus after accusing you as the culprit, her strength became inhuman. It's not a mere grudge or defense mechanism. She truly believes you did it!"
    show sumiko serious at Three3 with Dissolve(0.2)
    f_st3 "If they find out you had that idea, it's likely they will refuse to listen."
    f_sr5 "Ichirou and Inoue, yes. That's expected.{w=1.0} Who you {i}can{/i} convince are the two {i}other boys{/i}. You see each other everyday."
    f_sr5 "Sumiko, you told us Akira reached to you regarding their own investigation. You do realize what that means, yes? I'm sure he will listen if you reason out properly.{w=1.0} Yoshiro, especially so."
    f_sr5 "As for me...{w=3.0}{nw}"
    hide hikaru with Dissolve(0.1)
    hide sumiko with Dissolve(0.1)

    scene bg msci with dissolve
    show inoue seriousleft at Three3 with Dissolve(0.5)
    show inoue seriousleft at Three2 with Dissolve(0.5)
    "There she is."
    show inoue seriousleft at Three1 with Dissolve(0.5)
    "In the distance, Inoue is walking back to IV-A, a small packet of biscuits in hand.{w} She looked disgruntled, not willing to greet any passersby."
    hide inoue with Dissolve(1.0)

    scene bg school fields with dissolve
    show hikaru serious at Three1 with Dissolve(0.2)
    show sumiko serious at Three3 with Dissolve(0.2)
    f_sr5 "We must take our chances.{w=1.5} If we dawdle, then L.C. will get the jump on us and further complicate the situation.{w=1.0} I'm not sure if I can cope with another loss. The casualties are too much."
    show hikaru angry at Three1 with Dissolve(0.2)
    f_hy10 "When do we?"
    f_sr5 "Second break, today. Same spot.{w=1.0} Try your best to convince them in case they show any resistance. It's better while the {i}biggest obstacle{/i} is out of the way."
    show sumiko smile at Three3 with Dissolve(0.2)
    f_st3 "Noted.{w=1.0} We'll see you later."
    show hikaru smile at Three1 with Dissolve(0.2)
    f_sr5 "Thank you.{w=1.0} Let's head back and enjoy the rest of the break."
    hide hikaru with Dissolve(0.2)
    hide sumiko with Dissolve(0.2)
    
    return

label ch03_11_ceasefire:
    scene black with fade
    "AUGUST 26, 2013 - 1420H"
    scene bg classroom1 with fade

    window show
    nvl clear
    narr "Mr. Uendo, after reciting a prayer of thanksgiving, left IV-A and headed to the mens' faculty room."
    narr "Inoue refused her classmates' invitation to eat at the canteen, settling down on the biscuits she bought earlier.{w} Her mind wandered, first reading the posters on the sides of the board before settling down on {i}The Mark of Athena{/i}. She held the paper bookmark with her right thumb."
    narr "Her mind recalled the sweetest memories since the beginning of the year:{w=1.0} the first Club and Organization Day,{w=1.0} the gathering at the auditorium,{w=1.0} the times Emmerich did not visit at the hospital,{w=1.0} and the game nights with her brother after release."
    narr "The unpleasant ones soon followed:{w=1.0} her troubling periods of mental breakdown,{w=1.0} the isolation during her recovery,{w=1.0} and the repressed memories of her ordeal."

    nvl clear
    narr "She could still hear the voice."
    narr "{color=#808080}{cps=25}{i}Leave it all behind --{w=1.0} it is nothing.{w=2.0} What interest is there to behold?{/i}{/cps}{/color}"
    narr "At the doorway, she stood.{w} They stared into each other's eyes. Inoue averted her own."

    nvl clear
    window hide

    f_sr5 "You haven't forgiven me still, have you?"

    "No response."

    f_sr5 "Come on. Let's have a friendly chat outside."

    "Inoue rose from hear seat and approached Sayo."

    f_is4 "We've already made up. Why waste your time coming here?"
    f_sr5 "Because I have to.{w=1.5} I'm going to waste my own to time so I can talk to you.{w=1.0} I'm going to waste my time so I can see everyone together.{w=1.0} Most of all,{w=0.5} I'm going to waste my time so we can reach the end of this!"
    f_sr5 "If you have no qualms, then come with me."
    f_is4 "Where?"
    f_sr5 "To the bonding place.{w=1.0} They're waiting for us."

    scene bg msci with dissolve
    "Inoue watched Sayo cross the small street, the latter uncaring if Inoue followed or not.{w} She returned to IV-A."
    "But as Sayo turned to check at the small stairs, Inoue was already closing in some ten feet away."

    scene bg school fields with dissolve
    "They joined the four others in the square, now forming a circle. Sayo and Inoue sat between Hikaru and Yoshiro. Opposite them is Sumiko and Akira."

    f_is4 "This is everyone?"
    f_sr5 "I know it doesn't fit the definition of \"everyone,\" but the matter at hand concerns us more."
    f_is4 "Why {i}just{/i} us?! Where is Ichirou and Miyu?"
    f_ys6 "Inoue, save the questions for later.{w=1.0} There is a reason why things are they are right now."

    "Inoue looked at the others befuddled.{w} She crossed her arms, observing how the conversation will flow."
    "She had to make sure.{w=1.0} {cps=25}Something feels off.{/cps}"

    f_sr5 "First of all, I want to thank everyone for your time.{w=2.0} The last time we gathered, it went turbulent. I hope the outdoors would enable us to decide with more positive minds."
    f_sr5 "We've been thinking about this for two whole weeks now. I'm sure you were also shaken when the {i}unexpected{/i} turned up two Fridays ago.{w=1.5} From there, we have thought about what more we can do.{w=1.0} At this point, \"nothing more.\""
    f_sr5 "Therefore, we propose that we end this pointless feud and combine our efforts to prevent L.C. from taking another life; at the same time, inch closer to exposing their true identity."
    f_is4 "You're one to talk.{w=1.0} Why don't you address the accusations against you first?{w=1.5} Treat that as a request from one of the survivors."
    f_sr5 "..."
    f_is4 "Can you prove the claims wrong straight to my face?"
    f_sr5 "What is there to prove if the evidence never existed in the first place?"
    f_is4 "Hmph."
    f_sr5 "Sumiko, take charge."
    f_st3 "Alright. That is all we're asking for.{w=1.0} What are your thoughts --{w=1.0} Yoshiro,{w=0.5} Akira,{w=0.5} Inoue?"

    centered "{color=#808080}{cps=20}{i}What is this now? They have waited this long to make a proposition?{w=1.0} If Ichirou was here, he would have responded negatively without further discussion.{w=2.0}\nBut is that not a boon? After all, we already have something to work with.{w=1.5}\nIt is worth considering if our efforts would become more meaningful as a result.{/i}{/cps}{/color}"

    f_ys6 "Let me remind everyone that we all maintain divisive beliefs regarding the main culprit's identity.{w=1.0} As a result, we scoured for evidence ourselves to prove our own claims since the police is of little help."
    f_st3 "Yet we cannot discredit their efforts.{w=1.0} It is because of them we have information about the crimes almost at the same degree as they do."
    f_ys6 "Add that we are equally likely to be suspects as potential victims.{w=1.0} I'm taking a shot at the moon right now and claim that L.C. doesn't have complete knowledge of the puzzle pieces."
    f_ai2 "Is this referring to us or the info related to the case?"
    f_ys6 "Both, in some aspects.{w=1.0} Despite the numerous motifs they use in connection with the Sacred Heart Curse Killings, I doubt they understand the story behind it."
    f_hy10 "What about it? Is there something else we don't know?"
    f_ys6 "Precisely.{w=1.0} It's the same problem we've been trying to piece together but couldn't figure out how.{w=1.0} If, by any chance, it can make the process easier, then we're open to drop the barrier."
    f_is4 "I object!"
    f_ys6 "It is the most reasonable action. There is no other way. {i}*sigh*{/i}{w=1.0} It's better than to let him decide for us."
    f_is4 "Tsk."
    f_is4 "{cps=20}Fine. Do as you wish...{/cps}"
    f_st3 "How about you, Akira?"
    
    centered "{color=#808080}{cps=20}{i}I admit.{w=0.5} This is turning out better than I thought it would.{w=1.0} One man for himself, it seems. More freedom to think without the pressure of the autocrat's influence.{w=2.0}\nDid I just think that? Wow!{w=1.5}\nAnyway, casting my doubts aside would ease the situation. It's about time we work together guilt-free.{w=1.0} Oh, boy! This makes for an exciting adventure!{/i}{/cps}{/color}"

    f_st3 "Mr. Ichibana, your decision please."
    f_ai2 "Alright, Pres.{w=1.0} My decision.{w=0.5} Ummmmm..."
    f_st3 "Heh. Told you. That's the sign."
    f_is4 "You're agreeing to this, too?"
    f_ai2 "Hear me out first."
    f_ai2 "I believe in the goodwill of everyone here.{w=1.0} If Yoshiro thinks that we're all likely to be guilty, and the two others hold Sayo responsible...{w=3.0}{nw}"
    f_is4 "Because it's true!{w=2.0}{nw}"
    f_hy10 "Shut up!"

    "Silence."
    "All eyes -- especially Inoue's -- were on Hikaru.{w=1.0} She gave the heckler a menacing glare."
    "Blood rushed up to Inoue's temples and her fists shook.{w=1.0} This time, however, her stomach dropped.{w} She mellowed down without assistance and kept mum for a good chunk of the conversation."

    f_hy10 "Please, don't be rude and let him finish.{w=1.0} Await your turn."
    f_ai2 "{cps=25}Okay... Ahehehehehe...{w=1.0} I beg to differ...{/cps}"
    f_ys6 "Meaning?"
    f_ai2 "My opinion differs from yours.{w=1.5} I don't think any of us are capable of committing crimes of that degree."
    f_st3 "It was obvious from the get-go. You were {i}that{/i} easy to read."
    f_ys6 "It's not a secret to us, either. Be glad we cut you some slack even if it seemed unacceptable."
    f_ai2 "Ah, I see I need to brush up on my acting skills, then. {i}*chuckle*{/i}"
    f_ai2 "Still, that's the long and short of it. There's no way we can catch L.C. in our current state.{w=2.0} Sure, we have Inoue for the myths{w=1.0} and Yoshiro as the protégé --{w=1.5}{nw}"
    f_ys6 "I never agreed to be Emmerich's understudy if that's what you mean."
    f_ai2 "Uh. I change that to puzzle whiz kid. Sorry."
    f_ai2 "From my own research, I determined that we still lack the brainpower with the people we have.{w=2.0} How about those complicated bits of chemistry,{w=1.0} the supernatural stuff,{w=1.0} and those bits that require some level of psychoanalysis?"
    f_ys6 "And Hikaru for the nursery rhymes. In fact, maybe Aria can help us out."
    f_hy10 "Good idea.{w=1.0} I'll be sure to tell her."
    f_st3 "But why would anyone here even bother with psychoanalysis? Do we have someone who has {i}that{/i} as an interest?"
    f_ai2 "Oh, we do!"
    f_sr5 "..."
    f_ai2 "I rest my case."
    f_st3 "What about your decision, Inoue?"
    
    scene black with fade
    centered "{color=#808080}{cps=20}{i}Who cares? My own vote is meaningless. Down five to one without Ichirou here to back me up! If he was here, he would render this discussion meaningless.{w=2.0}\nAkira is such a tool. He only found the courage to speak up without Ichirou around.{w=1.0} Yoshiro has his own mind, following whatever is the \"most appropriate.\" He would not risk being the black sheep.{/i}{/cps}{/color}"

    f_st3 "Hello?"

    centered "{color=#808080}{cps=20}{i}Who do I truly hold responsible?{w=1.0} I can answer that.{w=1.5}\nIf I say, \"no,\" there better be a damn good reason. Whether I can trust them or not depends entirely on my own belief.{w=1.5}\nIt is what I experienced. I cannot be mistaken.{/i}{/cps}{/color}"

    f_hy10 "Inoue, it's your turn.{w=1.0} Are you alright?"

    centered "{color=#808080}{cps=20}{i}Why are these two still with her?{w=2.0}\nI'm not sure why Mi-kun would sit this out. Would he be not here to support her?{w=1.0} Then again, where is he?{w=1.5}\nI need some answers.{/i}{/cps}{/color}"

    scene bg school fields with fade
    c_is4 "Pass."
    f_st3 "Then we will present our sides first. Shall we?"
    f_sr5 "We all hold the same opinion and have decided on this after a long period of consideration.{w=1.5} It is best if we drop these so-called loyalties and work together as a whole."
    f_hy10 "I've made my loyalties known to Sayo based on one principle:{w=1.0} to seek out the truth.{w=1.5} I know you're all sick of hearing that phrase but we want to succeed in pursuing that goal."
    f_hy10 "If she is guilty, then I'm sorry I made a horrible mistake.{w=1.5} If not -- which I believe to be the case -- then we have no problem.{w=1.0} All I'm asking is that we stop pointing fingers without sufficient proof."
    f_st3 "Make it a five.{w=1.0} After all, I'm tired of having awkward interactions in the classroom whenever I'm in charge. I can't stand puppy dog eyes, you know?"
    f_ai2 "True. I think our other classmates know what's up."
    f_st3 "A select few, probably. But no one seems to mind so far."
    f_sr5 "It's good to know that all of us have made an effort to investigate even with our limitations.{w=1.0} I'm more than interested to know what you dug up."
    f_ys6 "Same sentiments.{w=2.0}{nw}"
    f_is4 "If I may!"

    "Finally.{w=1.0} The oddball has spoken up."

    f_is4 "I have considered all your opinions carefully. In fact, that gives me enough room to justify my decision.{w=2.0} You would forgive me if I do not share the same sentiments as all of you."

    "Sayo, Sumiko, and Hikaru glanced at each other. Akira and Yoshiro shook their heads in dismay.{w} Inoue kept one hand hidden from view."

    f_is4 "Hikaru said it best. We all want to seek the truth, and all claims must be accompanied with a solid proof.{w=1.0} If you are so interested in our findings, Sayp, I suggest you start with mine."
    f_sr5 "Alright.{w=0.5} Bring it out."
    f_is4 "I hope you'll all understand why I cannot agree to this readily."

    "She revealed her hand and uncovered a folded piece of paper. It was thoroughly crumpled and slightly dusty.{w} She threw it at the middle for Sayo to pick up."

    f_hy10 "{cps=20}Hold on. Is that...?{/cps}"

    "There was a streak of red on of the edges.{w} When she noticed it, the others followed and became unsettled."
    "Sayo unfolded the paper, confirming the color of the words{w=1.0} and something more.{w} She pressed her nose to the ink and recognized the faint hint of copper.{w} It was already a few days dry."
    "Her expression darkened as she read the words out."

    scene black with fade
    centered "{color=#bd0000}{cps=15}{i}Baa,{w=0.25} Baa,{w=0.25} black sheep,{w=0.5} have you any wool?{w=1.0}\nYes{w=0.25} sir,{w=0.25} yes{w=0.25} sir,{w=0.5} three bags full!{w=1.0}\nTwo for the master, and one for the dame...{w=1.0}\nNone for the little boy who cried down the lane...{w=1.0}\n\n Signed:{w=2.0} 1-2{/i}{/cps}{/color}"

    scene bg school fields with fade
    f_sr5 "{cps=25}When did you get this?{/cps}"
    f_is4 "{cps=25}This morning.{/cps}"

    "{cps=20}Then it means...{/cps}{w=2.0}{nw}"

    scene black
    "{i}*RIIIIIIIIIIIIIIINNNGGG*{/i}"
    return

label ch03_12_death03:
    scene black with fade
    "{color=#808080}AUGUST 23, 2013 - Time Unknown{/color}"

    window show
    nvl clear
    narr "{cps=10}Uggghhh...{/cps}"
    narr "I felt my neck with the back of my hand. Estimate a forty, as I forgot to take a paracetamol before dozing off."
    narr "It stings.{w} That's the usual situation whenever I wake up in the middle of a sleep cycle, made even worse by the fever.{w} On the contrary, this is the first case where my entire body sans my head and hands feel numb."
    narr "It's the weather.{w=1.5} That is all.{w=1.5} Add my foolhardy decisions.{w=1.0} Blame them for everything."
    narr "{cps=20}Stop keeping me awake.{/cps}"

    nvl clear
    window hide

    centered "{i}{cps=15}It is useless to deny it.{w=2.0} You cannot escape...{/cps}{/i}"

    window show
    nvl clear
    narr "There goes my dream voicebox,{w=1.0} malfunctioning since the early evening."
    narr "Come to think of it, it's the last thing I remember.{w} My mind was overflowed with questions.{w} {cps=25}Did I lock the gate?{w=2.0} Did I clean up after Miyu's visit?{w=2.0} Did I turn off the lights downstairs?{w=2.5}{/cps}{nw}"
    narr "{cps=15}Did I...?{/cps}{w=3.0}{nw}"
    narr "Somehow, I don't have the will to check. It keeps telling me everything is alright. Why should I worry?{w} Inside or outside, everything is peaceful.{w=1.5} Safe.{w=1.0} Yes. Don't tie the brain with these thoughts. It is the weekend, after all."

    nvl clear
    window hide

    centered "{i}{cps=20}Among a hundred sheep, one has led itself astray.{w=2.0}\nSome may wonder,{w=1.0} does the shepherd bother to look for it while leaving the others?{w=1.5} The answer is, \"Yes! He does!\"{/cps}{/i}{w=4.0}{nw}"
    centered "{i}{cps=20}Although,{w=1.0} it seems that{w=3.0}{/cps} {color=#bd0000}the master did not make it after all...{/color}{/i}"

    window show
    nvl clear
    narr "What?! No...{w=2.0}{nw}"
    narr "This cannot be.{w=2.0}{nw}"
    narr "The dream ended minutes ago.{w=1.0} Rather, I cannot recall any dream.{w=1.5} I had none!{w=2.0}{nw}"
    narr "But then there are these voices.{w=2.0}{nw}"
    narr "My mind is making it up.{w=1.5}{nw}"

    nvl clear
    window hide

    scene bg bedroom2 nightmare
    "{b}{i}*BUZZ*{/i}{/b}"

    window show
    nvl clear
    narr "A rough slice was enough for a good jolt. My heart rushed to deliver blood throughout my entire body."
    narr "Only then I knew why I didn't have the strength to act upon my instincts' calls."
    narr "I am in my room, alright.{w} The chattering outside sounded nothing but murmurs. I could always hear people wandering about until one in the morning."
    narr "Yet, I am not lying in bed.{w} I am sitting on my computer chair, my head propped up with a small pillow above the wood."

    nvl clear
    narr "My left thumb and index fingers feel warm. I held my hand close to my face so I can check.{w} Bile rose up my esophagus as I formed a fist."
    narr "Blood trickled from the tips.{w=1.5} Scratch marks from what seems to be from a razor appeared on the skin.{w=1.5} Worse, the nails have been sliced in half.{w=2.0} The sensation only kicked in!"
    narr "Aside from my limbs and my head, everything else is bound with thick rolls of fabric. The tightness could crush my ribcage and shorten my breath."
    narr "I feel lightheaded, likely from the shock of seeing and receiving such a wound."
    narr "I pray that this be a dream.{w} The pain...{w=2.0} I can't stand it any longer."

    nvl clear
    window hide

    unk "{cps=20}You are awake.{w=2.0} Much earlier than scheduled.{/cps}"

    "I looked all over for the voice.{w} It hid itself within the shadows.{w} Its presence can be felt, yet it chooses to remain unknown."
    "{i}*step*{w=0.5} *step*{w=0.5} *step*{w=0.5} *step*{/i}"
    "The sounds came from my right.{w} I turned and saw the intruder, the upper half of the body concealed.{w} It was the one who sliced my fingers, the small trail of blood traced to its position."
    "Its tone was mellow and cold, similar to that of what I've heard no long ago."
    "{cps=15}Could it be...?{/cps}"

    unk "Pardon me, my friend.{w=1.0} It seems I have handled things too roughly.{w=1.5} Oh, bother.{w=0.5} We can apply some antiseptic and band-aids later. For now, we need to talk."

    "{i}You bastard!{w=1.0} You...{w=1.0} You tricked me.{w=0.5} Cheater!{w=0.5} Murderer!{w=0.5} What have you done to me?{w=1.0} Wy are you doing this?{/i}"
    unk "Questions{w=0.5} upon questions{w=0.5} upon questions...{w=1.5} It only becomes more complicated the longer this entire farce drags on.{w=0.5} And for good reason.{w=1.5} Plucking out sheep like you is the best form of entertainment,{w=0.5} picking out those who treat their words as gospel."
    unk "{cps=20}My, my, aren't you sweetheart and a hard nut to crack?{w=2.0} How does it feel to be reminded of humanity?{w=1.0} Harsh,{w=0.5} incomparable to the amount of pain others have suffered.{w=1.0} It is only minute.{w=1.0} Suck it up and be a man.{/cps}"

    "{i}*step*{w=0.5} *step*{w=0.5} *step*{w=0.5} *step*{/i}"
    "Another set of footsteps from the other side.{w} The feet sounded heavier, if not occasionally pattering on the wood to mimic a child."
    "{cps=15}A...{w=1.0} {i}child{/i}?!{/cps}"
    "That's not right. It was only a thought.{w} The two intruders had a more teenage-like build. One has a bulge in his pelvis; the other shorter and well-endowed at the front."
    "Who are these people?!{w=1.0} Certainly not from my family!"

    "{i}Just take what you want and leave.{w=1.0} I won't tell a soul.{w=0.5} Promise!{w=1.0} Leave me be!{/i}"
    "\"{i}Kukukukukukukukuku...{w=1.0} Kyekyekyekyehahahahahahaha!{/i}\""

    "And one of them hopped in front of me.{w=2.0} She leaned forward, making herself known."

    u_sr5 "Hello."

    "{cps=15}I was...{w=1.0} I was...{w=2.0} No...{w=1.0} But she didn't...{/cps}"

    "{i}Sayo...?{w=3.0} What the hell did you do to me?!{w=1.0} And this lackey of yours! Who is he?{/i}"
    unk "One of two things.{w=2.0} For one,{w=1.0} your worst rival.{w=1.5} Second, I am the person whom you loathe so much that you wouldn't dare look at my face.{w=1.0} Take a gander, pitiful creature."

    "I recognize that voice."
    "He joined her, sporting a similar Cheshire Cat-like grin as her."

    u_mh8 "Did I promise not to day that?{w=1.0} {i}*snicker* *snicker*{/i} Sorry..."

    "Two of them?{w=1.5} And you're telling me one of them is L.C.?! They are equally as bonkers as the other!{w=1.0} This renders that idea meaningless."
    "What does it mean?"

    f_is4 "I'm not sure. Sometimes, it would be the {i}same voice as in the CD recording{/i}. Other times, it would warp to a {i}female{/i}. It was witch-like, the second one!"

    "{cps=20}The only way that would make sense is if...{/cps}{w=3.0}{nw}"
    "{cps=15}...there are {i}two{/i} L.C.s in the first place.{/cps}{w=2.0}{nw}"
    "Wait!{w=0.5} That's not right.{w=1.0} That violates everything we know so far. It makes no sense! {color=#bd0000}Arrrrrrrggghhh!!!{/color}"

    u_mh8 "I'm appalled to watch you tear you hair out in spite of your \"disabling\" injury. How fascinating, indeed..."
    u_sr5 "{cps=20}Are you happy now? {i}*giggle*{/i} It seems you were right all along. Who would have known? Will they know?{w=2.0} I'm sure they'll be stoked to learn this revelation.{w=1.0} Imagine their heads rolling in disbelief!{/cps}"
    u_mh8 "In short...{w=1.0} Game over.{w=1.5} Tsk. {i}*giggle* *giggle*{/i}{w=2.0} Look at him. Moping like he lost badly in a game of tag,{w=1.0} or he got red-flagged and bannned from playing volleyball!{w=1.0} Oooooh... The horror!"
    r_iy1 "Damn you...{w=1.0} Damn you both...{w=1.0} Curses!{w=0.5} L.C., why you...{w=1.5} {i}*hic*{w=0.5} *gulp*{w=2.0} *gasp* *hic*{/i}"

    "No more.{w=1.0} No farther.{w=2.0} These two are far beyond reasoning.{w=1.0} They're nothing more than shells."

    u_mh8 "He's sad.{w=1.0} Why don't we sing a song?"
    u_sr5 "{cps=20}What will it be?{w=2.0} Oh! {b}*clap*{/b} I know just the thing. Glad my memory is ever reliable.{/cps}"

    "She whispered something into his ear.{w} What that song is, like I care."
    "{b}{i}*clap*{w=1.0} *clap*{w=1.0} *clap*{w=1.0} *clap*{/i}{/b}"

    "{cps=15}{i}Baa,{w=0.25} Baa,{w=0.25} black sheep,{w=0.5} have you any wool?{w=1.0}\n{color=#bd0000}Yes{w=0.25} sir,{w=0.25} yes{w=0.25} sir,{w=0.5} three bags full!{/color}{w=1.5}{/i}{/cps}{nw}"
    "{cps=15}{i}Two for the master, and one for the dame...{w=1.0}\n{color=#bd0000}None for the little boy who cried down the lane!{/color}{w=1.0}{/i}{/cps}"
    r_iy1 "Kekekekekekeke...{w=1.0} Ahehehehehehehehehe...{w=1.0} GAHAHAHAHAHAHAHAHAHAHAHAHAHA!!!"
    u_sr5 "{cps=20}Look at him. He's happy!{w=1.0} Why don't we give him a reward?{/cps}"
    u_mh8 "You do the honors.{w=1.5} Besides, I already did my part to wake him up."

    "They passed the razor around.{w} My hands were turned over, palms down."
    scene red
    "{b}{i}*BUUUUUUUUUUUUUZZZ*{/i}{/b}"

    scene bg blood with dissolve
    r_iy1 "Gulk! Ngggggggggggggg!!!"

    "Excruciation as they scraped the skin off to form two numbers --{w=2.0} {color=#bd0000}1{/color} and {color=#bd0000}2{/color} on the left and right hands, respectively."

    scene bg bedroom2 nightmare with dissolve
    u_sr5 "{cps=20}This is not the time to be frowning, you know.{w=2.0} We just learned what happened to the little boy down the lane.{w=1.0} For that, we shall punish you.{/cps}"

    scene red
    "{b}{i}*BUZZ*{/i}{/b}"

    scene bg bedroom2 nightmare with dissolve
    "{cps=25}The other thumb joined its distant siblings, only this time the whole nail was decapitated. The entire digit was sprayed red after a few seconds.{/cps}"
    "{cps=15}No more smiles.{w=1.0} Eyes and soul withdrawn.{w=1.5} There is only darkness.{/cps}"

    u_sr5 "{cps=20}That's a shame.{/cps}"

    "{b}*GULK*{/b}"

    u_sr5 "{color=#bd0000}{cps=20}Sayonara.{w=1.0} Have a nice dream.{/cps}{/color}"

    scene bg blood2
    centered "{color=#bd0000}{b}{i}*GRIIIIIIIIIIIIIIIIIIIIIIIND*{/i}{/b}{/color}"

    scene bg bedroom2 night
    window show
    nvl clear
    narr "And thus, he awoke from the dream.{w} This he could remember, the colors and sensations so vivid.{w=1.5} This he could never miss."
    narr "{b}*THUD*{/b}{fast}"
    narr "{cps=10}Help...{w=1.0} Help...{/cps}"

    scene bg abyss with dissolve
    nvl clear
    narr "{color=#808080}{i}Hey, Ichi! Your holler!{/i}{/color}"
    narr "His body was feeble.{w=1.0} He lifted it so he can be saved.{w} Because of the pain, he managed no more than a hand wave...{w=1.0} only once, in fact. Once was enough to be acknowledged/"

    scene white with dissolve
    narr "He did not hear the response that followed.{w} He crashed to the ground, eyes slowly being sapped of life."
    narr "His sleep felt more peaceful than before."

    nvl clear
    window hide

    return

label ch03_13_epilogue:
    scene black with fade
    centered "{i}{b}A surreal vision of a horrific end, or a dying dream?{w}\nEither one or the other, what does it all mean?{/i}{/b}"

    centered "{b}***END OF AUGUST CHAPTER***\n\n{i}TO BE CONTINUED...{/i}{/b}"
    return