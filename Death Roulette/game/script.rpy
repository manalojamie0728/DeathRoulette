# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# PRIMARY
define narr = nvl_narrator

# -- General/Safe
define iy1 = Character("Ichirou", color="#ffffff")
define ai2 = Character("Akira", color="#ffffff")
define st3 = Character("Sumiko", color="#ffffff")
define is4 = Character("Inoue", color="#ffffff")
define sr5 = Character("Sayo", color="#ffffff")
define ys6 = Character("Yoshiro", color="#ffffff")
define hk7 = Character("Hiroshi", color="#ffffff")
define mh8 = Character("Miyu", color="#ffffff")
define kk9 = Character("Kyou", color="#ffffff")
define hy10 = Character("Hikaru", color="#ffffff")

# -- Fine/Sane
define f_iy1 = Character("Ichirou", color="#08a000")
define f_ai2 = Character("Akira", color="#08a000")
define f_st3 = Character("Sumiko", color="#08a000")
define f_is4 = Character("Inoue", color="#08a000")
define f_sr5 = Character("Sayo", color="#08a000")
define f_ys6 = Character("Yoshiro", color="#08a000")
define f_hk7 = Character("Hiroshi", color="#08a000")
define f_mh8 = Character("Miyu", color="#08a000")
define f_kk9 = Character("Kyou", color="#08a000")
define f_hy10 = Character("Hikaru", color="#08a000")

# -- Caution/Sane
define c_iy1 = Character("Ichirou", color="#eaff00")
define c_ai2 = Character("Akira", color="#eaff00")
define c_st3 = Character("Sumiko", color="#eaff00")
define c_is4 = Character("Inoue", color="#eaff00")
define c_sr5 = Character("Sayo", color="#eaff00")
define c_ys6 = Character("Yoshiro", color="#eaff00")
define c_hk7 = Character("Hiroshi", color="#eaff00")
define c_mh8 = Character("Miyu", color="#eaff00")
define c_kk9 = Character("Kyou", color="#eaff00")
define c_hy10 = Character("Hikaru", color="#eaff00")

# -- Danger/Sane
define d_iy1 = Character("Ichirou", color="#e78d00")
define d_ai2 = Character("Akira", color="#e78d00")
define d_st3 = Character("Sumiko", color="#e78d00")
define d_is4 = Character("Inoue", color="#e78d00")
define d_sr5 = Character("Sayo", color="#e78d00")
define d_ys6 = Character("Yoshiro", color="#e78d00")
define d_hk7 = Character("Hiroshi", color="#e78d00")
define d_mh8 = Character("Miyu", color="#e78d00")
define d_kk9 = Character("Kyou", color="#e78d00")
define d_hy10 = Character("Hikaru", color="#e78d00")

# -- Critical/Insane
define r_iy1 = Character("Ichirou", color="#bd0000")
define r_ai2 = Character("Akira", color="#bd0000")
define r_st3 = Character("Sumiko", color="#bd0000")
define r_is4 = Character("Inoue", color="#bd0000")
define r_sr5 = Character("Sayo", color="#bd0000")
define r_ys6 = Character("Yoshiro", color="#bd0000")
define r_hk7 = Character("Hiroshi", color="#bd0000")
define r_mh8 = Character("Miyu", color="#bd0000")
define r_kk9 = Character("Kyou", color="#bd0000")
define r_hy10 = Character("Hikaru", color="#bd0000")

# -- Dead/Unknown
define u_iy1 = Character("Ichirou", color="#808080")
define u_ai2 = Character("Akira", color="#808080")
define u_st3 = Character("Sumiko", color="#808080")
define u_is4 = Character("Inoue", color="#808080")
define u_sr5 = Character("Sayo", color="#808080")
define u_ys6 = Character("Yoshiro", color="#808080")
define u_hk7 = Character("Hiroshi", color="#808080")
define u_mh8 = Character("Miyu", color="#808080")
define u_kk9 = Character("Kyou", color="#808080")
define u_hy10 = Character("Hikaru", color="#808080")

# -- NVL
define n_iy1 = Character("Ichirou", kind=nvl)
define n_ai2 = Character("Akira", kind=nvl)
define n_st3 = Character("Sumiko", kind=nvl)
define n_is4 = Character("Inoue", kind=nvl)
define n_sr5 = Character("Sayo", kind=nvl)
define n_ys6 = Character("Yoshiro", kind=nvl)
define n_hk7 = Character("Hiroshi", kind=nvl)
define n_mh8 = Character("Miyu", kind=nvl)
define n_kk9 = Character("Kyou", kind=nvl)
define n_hy10 = Character("Hikaru", kind=nvl)

# SECONDARY
define tomonori = Character("Tomonori", color="#ffffff")
define ikuko = Character("Ikuko", color="#ffffff")
define sanae = Character("Sanae", color="#ffffff")
define ayumi = Character("Ayumi", color="#ffffff")
define t_gen = Character("Mrs. Genkai", color="#ffffff")
define t_har = Character("Ms. Harada", color="#ffffff")
define t_rit = Character("Mrs. Ritsuko", color="#ffffff")
define t_kan = Character("Mrs. Kanako", color="#ffffff")
define t_kai = Character("Mrs. Kaida", color="#ffffff")
define t_ich = Character("Mrs. Ichimiya", color="#ffffff")
define prin = Character("Mrs. Sokoguchi", color="#ffffff")
define ms_shi = Character("Mrs. Shinozaki", color="#ffffff")
define mr_shi = Character("Mr. Shinozaki", color="#ffffff")
define ms_kir = Character("Mrs. Kirisaki", color="#ffffff")
define p_serg = Character("Sergeant", color="#ffffff") # Same Character as Deitch
define p_insp = Character("Inspector", color="#ffffff") # Same Character as Emmerich
define p_emm = Character("Insp. Emmerich", color="#ffffff")
define p_dei = Character("Sgt. Deitch", color="#ffffff")

# MISC
define guard = Character("Guard", color="#ffffff")
define nurse = Character("Nurse", color="#ffffff")
define student = Character("Student", color="#ffffff")
define officer = Character("Officer", color="#ffffff")
define proctor = Character ("Proctor", color="#ffffff")
define c_vp = Character("Vice President", color="#ffffff")
define c_sec = Character("Secretary", color="#ffffff")
define c_4r = Character("Fourth-Year Rep", color="#ffffff")
define neighbor = Character("Neighbor", color="#ffffff")
define sanae_bro = Character("Sanae's Brother", color="#ffffff")
define ms_yos = Character("Mrs. Yoshida", color="#ffffff")
define unk = Character("???", color="#808080")

init:
    $ LS = Position(xpos=0.2, xanchor=0.2, ypos=0.55, yanchor=0.5, yoffset=100)
    $ RS = Position(xpos=0.75, xanchor=0.8, ypos=0.55, yanchor=0.5, yoffset=100)
    $ Three1 = Position(xpos=0.25, xanchor=0.25, ypos=0.55, yanchor=0.5, yoffset=100)
    $ Three2 = Position(xpos=0.5, xanchor=0.5, ypos=0.55, yanchor=0.5, yoffset=100)
    $ Three3 = Position(xpos=0.75, xanchor=0.75, ypos=0.55, yanchor=0.5, yoffset=100)
    $ EightM = Position(xpos=-0.1, xanchor=-0.1, ypos=0.55, yanchor=0.5, yoffset=100)
    $ Eight1 = Position(xpos=0.0, xanchor=0.0, ypos=0.55, yanchor=0.5, yoffset=100)
    $ Eight2 = Position(xpos=0.14, xanchor=0.14, ypos=0.55, yanchor=0.5, yoffset=100)
    $ Eight3 = Position(xpos=0.29, xanchor=0.29, ypos=0.55, yanchor=0.5, yoffset=100)
    $ Eight4 = Position(xpos=0.43, xanchor=0.43, ypos=0.55, yanchor=0.5, yoffset=100)
    $ Eight5 = Position(xpos=0.56, xanchor=0.56, ypos=0.55, yanchor=0.5, yoffset=100)
    $ Eight6 = Position(xpos=0.71, xanchor=0.71, ypos=0.55, yanchor=0.5, yoffset=100)
    $ Eight7 = Position(xpos=0.86, xanchor=0.86, ypos=0.55, yanchor=0.5, yoffset=100)
    $ Eight8 = Position(xpos=1.0, xanchor=1.0, ypos=0.55, yanchor=0.5, yoffset=100)
    transform slide_left:
        zoom 2.0
        xpos 0.9 xanchor 0.9 ypos 0.85 yanchor 0.5
        linear 35.0 xpos 0.0
        pause 2.0
        linear 5.0 alpha 0.0
    transform slide_right:
        zoom 2.0
        xpos 0.1 xanchor 0.1 ypos 0.85 yanchor 0.5
        linear 35.0 xpos 1.0
        pause 2.0
        linear 5.0 alpha 0.0

# The game starts here.
init python:
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    config.debug_sound = True
    
    # Writing, Programming, Background, Sprites, GUI, Music
    credits = ('STORY', 'Jamie D.W.'), ('GUI', 'Jamie D.W.'), ('SPRITES', 'Made Using: IICharacterAlpha (nantoka.main.jp), 2011-2013'), ('BACKGROUNDS', 'mugenjohncel'), ('BACKGROUNDS', 'konnett'), ('BACKGROUNDS', 'Google Images'), ('BACKGROUNDS', 'Processed By: Jamie D.W.'), ('SOUND EFFECTS', 'https://freesound.org'), ('OTHER SOUND EFFECTS', '')
    credits += ('Eric Matyas (SFX)\nwww.soundimage.org', 'Street Ambience 5'), ('Eric Matyas (SFX)\nwww.soundimage.org', 'UI_Quirky18')
    credits += ('MUSIC', 'Licensed under CC Attr. 3.0 and 4.0')
    credits += ('Eric Matyas (Music)\nwww.soundimage.org', 'Calmer Times'), ('Eric Matyas (Music)\nwww.soundimage.org', 'Hazy Disorientation'), ('Eric Matyas (Music)\nwww.soundimage.org', 'On Things to Come'), ('Eric Matyas (Music)\nwww.soundimage.org', 'The Ant Hill Gang Goes West')
    credits += ('Kevin MacLeod (Music)\nincompetech.com', 'Autumn Day'), ('Kevin MacLeod (Music)\nincompetech.com', 'Awkward Meeting'), ('Kevin MacLeod (Music)\nincompetech.com', 'Corruption'), ('Kevin MacLeod (Music)\nincompetech.com', 'Controlled Chaos'), ('Kevin MacLeod (Music)\nincompetech.com', 'Decline'), ('Kevin MacLeod (Music)\nincompetech.com', 'Echoes of Time')
    credits += ('Kevin MacLeod (Music)\nincompetech.com', 'Ghost Story'), ('Kevin MacLeod (Music)\nincompetech.com', 'Merry Go'), ('Kevin MacLeod (Music)\nincompetech.com', 'Night of Chaos'), ('Kevin MacLeod (Music)\nincompetech.com', 'Porch Swing Days'), ('Kevin MacLeod (Music)\nincompetech.com', 'Road To Hell'), ('Kevin MacLeod (Music)\nincompetech.com', 'Satiate')
    credits += ('Kevin MacLeod (Music)\nincompetech.com', 'Two Together'), ('Kevin MacLeod (Music)\nincompetech.com', 'Undaunted'), ('Kevin MacLeod (Music)\nincompetech.com', 'Vulcan')
    credits += ('Robert Austin (Music)', 'Chloe\'s Lullaby'), ('Marc Steene and Wray Burgess', 'Ring Around The Rosie (Slender Elementary Version)'), ('Marioverehrer (Original: Claude Debussy)', 'Au Clair De La Lune - Synthesia')
    credits += ('COPYRIGHTED MUSIC', ''), ('Eiko Shimamiya', 'Chikai (Higurashi No Naku Koro Ni Chikai)'), ('tia koudelika (Original: Eiko Shimamiya)', 'Why or Why Not - Cover (Higurashi No Naku Koro Ni)'), ('Mao Hamamoto', 'Chapter1 MainBGM PSP-Original BGM11 (Corpse Party: Blood Covered Repeated Fear)')
    credits += ('SPECIAL THANKS TO', 'Lizeth Baldelomar - Stay Awesome! ;)')
    credits += ('COPYRIGHT, 2017', 'Jamie D.W.')
    credits_s = "{size=50}CREDITS\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=35}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=40}" + renpy.version() #Don't forget to set this to your Ren'py version

init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image opening = Text("{size=60}A GAME BY\nJamie D.W.", text_align=0.5)
    image opening2 = Text("{size=60}A REN\'PY VISUAL NOVEL", text_align=0.5)
    image opening3 = Text("{size=60}JAMIE D.W.\nPRESENTS", text_align=0.5)
    image opening4 = Text("{size=20}Chikai - Eiko Shimamiya\nHigurashi No Naku Koro Ni Chikai OST\nCopyright, 2009", text_align=0.5)
    image opening5 = Text("{size=40}STORY\n{size=30}Jamie D.W.", text_align=0.5)
    image opening6 = Text("{size=40}GRAPHICS DESIGN\n{size=30}Jamie D.W.", text_align=0.5)
    image opening7 = Text("{size=40}SPRITES DESIGN\n{size=30}Jamie D.W.\nUsing: IICharacterAlpha (nantoko.main.jp), 2011-2013", text_align=0.5)
    image opening8 = Text("{size=40}BACKGROUNDS\n{size=30}mugenjohncel\nkonnett", text_align=0.5)
    image opening9 = Text("{size=40}MUSIC AND SFX\n{size=30}Eric Matyas\nKevin MacLeod\nRobert Austin", text_align=0.5)
    image opening10 = Text("{size=40}FEATURING SONGS FROM\n{size=30}Higurashi No Naku Koro Ni\nCorpse Party: Blood Covered Repeated Fear", text_align=0.5)
    image opening11 = Text("{size=40}DIRECTED BY\n{size=30}Jamie D.W.", text_align=0.5)
    image openingname1 = Text("{size=40}Sayo Ronoroa", text_align=0.5)
    image openingname2 = Text("{size=40}Hikaru Yamamoto", text_align=0.5)
    image openingname3 = Text("{size=40}Kyou Kirisaki", text_align=0.5)
    image openingname4 = Text("{size=40}Inoue Shinozaki", text_align=0.5)
    image openingname5 = Text("{size=40}Miyu Hirano", text_align=0.5)
    image openingname6 = Text("{size=40}Ichirou Yokohama", text_align=0.5)
    image openingname7 = Text("{size=40}Sumiko Tokubei", text_align=0.5)
    image openingname8 = Text("{size=40}Akira Ichibana", text_align=0.5)
    image openingname9 = Text("{size=40}Yoshiro Suzuki", text_align=0.5)
    image openingname10 = Text("{size=40}Hiroshi Kano", text_align=0.5)
    image splash1 = Text("{size=60}{color=#f00}WARNING{/color}", text_align=0.5)
    image splash2 = Text("{size=50}{color=#f00}The following contains acts of violence and other content that may be disturbing to some players.\nPlay at your own risk.{/color}", text_align=0.5)
    image theend = Text("{size=80}CREATED BY:\nJamie D.W.", text_align=0.5)
    image thanks = Text("{size=80}DEATH ROULETTE\nSEE YOU NEXT TIME!", text_align=0.5)

label start:
    stop music
    scene black with fade

    #call ch01_june from _call_ch01_june
    call ch02_july
    #call ch03_august
    #call ch04_september
    #call ch05_october
    #call ch06_november
    #call ch07_december
    #call ch08_january
    #call ch09_february
    #call ch10_march
    return

label before_main_menu:
    scene black with dissolve
    show opening:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with Pause(5)
    scene bg splashscreen with dissolve
    show splash1:
        yanchor 0.2 ypos 0.2
        xanchor 0.5 xpos 0.5
    show splash2:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with Pause(10)
    scene black with fade
    return

label opening:
    play music guest_chikai noloop
    scene black with dissolve
    show opening2:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with Pause(5)
    hide opening2
    show opening3:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with Pause(3.75)
    hide opening3
    scene op title1 with Pause(4)
    scene op title2 with Pause(4)
    scene red with dissolve
    show opening4:
        yanchor 1.0 ypos 1.0
        xanchor 0.0 xpos 0.0
    with Pause(6)
    hide opening4
    scene bg street rain with dissolve
    show opening5:
        yanchor 0.8 ypos 0.8
        xanchor 0.8 xpos 0.8
    with Pause(4)
    hide opening5
    scene bg village night
    show opening6:
        yanchor 0.9 ypos 0.9
        xanchor 0.1 xpos 0.1
    with Pause(4)
    hide opening6
    scene bg msci night
    show opening7:
        yanchor 0.9 ypos 0.9
        xanchor 0.1 xpos 0.1
    with Pause(3)
    hide opening7
    scene bg underwater with dissolve
    scene bg underwater
    show opening8:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with Pause(4)
    hide opening8
    scene bg underwater nightmare with dissolve
    scene bg underwater nightmare
    show opening9:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with Pause(3.25)
    hide opening9
    scene bg blood with Pause(3.75)
    scene bg blood2 with Pause(4.5)
    scene black with dissolve
    scene black with Pause(1.5)
    scene bg msci nightmare
    scene black with dissolve
    scene bg msci nightmare
    scene black with dissolve
    scene bg msci nightmare with dissolve
    show openingname1:
        yanchor 0.8 ypos 0.8
        xanchor 0.7 xpos 0.7
    show op sayo at slide_right("Sayo") with Pause(1.0)
    hide openingname1 with Dissolve(0.25)
    hide op sayo with Dissolve(0.25)
    
    show openingname2:
        yanchor 0.8 ypos 0.8
        xanchor 0.3 xpos 0.3
    show op hikaru at slide_left("Hikaru") with Pause(1.0)
    hide openingname2 with Dissolve(0.25)
    hide op hikaru with Dissolve(0.25)

    show openingname3:
        yanchor 0.8 ypos 0.8
        xanchor 0.7 xpos 0.7
    show op kyou at slide_right("Kyou") with Pause(1.0)
    hide openingname3 with Dissolve(0.25)
    hide op kyou with Dissolve(0.25)
    
    show openingname4:
        yanchor 0.8 ypos 0.8
        xanchor 0.3 xpos 0.3
    show op inoue at slide_left("Inoue") with Pause(1.0)
    hide openingname4 with Dissolve(0.25)
    hide op inoue with Dissolve(0.25)
    
    show openingname5:
        yanchor 0.8 ypos 0.8
        xanchor 0.7 xpos 0.7
    show op miyu at slide_right("Miyu") with Pause(1.0)
    hide openingname5 with Dissolve(0.25)
    hide op miyu with Dissolve(0.25)
    
    show openingname6:
        yanchor 0.8 ypos 0.8
        xanchor 0.3 xpos 0.3
    show op ichirou at slide_left("Ichirou") with Pause(1.0)
    hide openingname6 with Dissolve(0.25)
    hide op ichirou with Dissolve(0.25)
    
    show openingname7:
        yanchor 0.8 ypos 0.8
        xanchor 0.7 xpos 0.7
    show op sumiko at slide_right("Sumiko") with Pause(1.0)
    hide openingname7 with Dissolve(0.25)
    hide op sumiko with Dissolve(0.25)
    
    show openingname8:
        yanchor 0.8 ypos 0.8
        xanchor 0.3 xpos 0.3
    show op akira at slide_left("Akira") with Pause(1.0)
    hide openingname8 with Dissolve(0.25)
    hide op akira with Dissolve(0.25)
    
    show openingname9:
        yanchor 0.8 ypos 0.8
        xanchor 0.7 xpos 0.7
    show op yoshiro at slide_right("Yoshiro") with Pause(1.0)
    hide openingname9 with Dissolve(0.25)
    hide op yoshiro with Dissolve(0.25)
    
    show openingname10:
        yanchor 0.8 ypos 0.8
        xanchor 0.3 xpos 0.3
    show op hiroshi at slide_left("Hiroshi") with Pause(1.0)
    hide openingname10 with Dissolve(0.25)
    hide op hiroshi with Dissolve(0.25)

    scene bg msci with dissolve
    scene bg msci with Pause(2.5)
    scene bg school gate with Pause(3.0)
    scene bg tvstatic with dissolve
    scene bg tvstatic with Pause(3.5)
    scene black with dissolve
    scene black with Pause(2.0)
    scene bg abyss with dissolve
    scene bg abyss with Pause(3.0)
    scene op roulette with dissolve
    scene op roulette 
    show opening10:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with Pause(4.0)
    hide opening10
    scene bg darkhallway3 with dissolve
    scene bg darkhallway3
    show opening11:
        yanchor 0.6 ypos 0.6
        xanchor 0.5 xpos 0.5
    with Pause(1.5)
    hide opening11
    scene bg darkhallway3 nightmare
    show opening11:
        yanchor 0.6 ypos 0.6
        xanchor 0.5 xpos 0.5
    with Pause(1.5)
    hide opening11
    scene black with dissolve

    stop music fadeout 1.0
    return

label credits:
    $ credits_speed = 300 #scrolling speed in seconds
    play music guest_whyorwhynot
    scene black with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    scene bg msci night with dissolve
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    scene black with dissolve
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return