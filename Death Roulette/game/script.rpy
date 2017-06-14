# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    # narr "Hello, world."

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    narr "Night.{w} The crickets filling in the silence that blankets the area.{w} No one to be seen nor heard as all have went home to rest, ready for the day to come."
    narr "Except it was Saturday, three hours before the Sabbatical Day sets in."
    nvl clear
    narr "The name's Ichirou Yokohama."
    narr "Akira Ichibana."
    narr "Sumiko Tokubei."
    narr "Inoue Shinozaki."
    narr "Sayo Ronoroa."
    nvl clear
    narr "Yoshiro Suzuki."
    narr "Hiroshi Kano."
    narr "Miyu Hirano."
    narr "Kyou Kirisaki."
    narr "Hikaru Yamamoto."
    nvl clear

    # This ends the game.

    return
