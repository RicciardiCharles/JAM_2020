from pygame_functions import *
from settings import *
from random import *
import random

def random_cit():
    rd_nb = random.randint(1, 9)
    if rd_nb == 1:
        return "Blanc sans N ça fait Blac, comme quoi sans haine on est tous égaux."
    if rd_nb == 2:
        return "Lorsque la différence sera la norme, alors les hommes vivront en paix."
    if rd_nb == 3:
        return "Nos différences nous rendent uniques."
    if rd_nb == 4:
        return "La différence est un espoir pour l'Humanité."
    if rd_nb == 5:
        return "Si les différences sont particulières, l'intolérance, elle, est générale."
    if rd_nb == 6:
        return "La différence entre possible et impossible réside dans la détermination qui sommeille en toi !"
    if rd_nb == 7:
        return "Le racisme n'est pas une opinion, c'est un délit."
    if rd_nb == 8:
        return "Le mal le plus pernicieux, le plus nocif sur cette Terre est le racisme."
    if rd_nb == 9:
        return "Le racisme, d'où qu'il vienne, est un crime du cœur et de l'esprit. Il abaisse, il salit, il détruit."

def enemy_life(persuasion, life_en):
    store_bar3 = drawRect(1250, 50, 625, 75, (84, 66, 107))
    store_bar4 = drawRect(1450, 150, 425, 75, (84, 66, 107))
    life_baren = drawRect(1270, 60, life_en * 0.95, 55, (222, 60, 75))
    persuasion_bar = drawRect(1470, 160, persuasion * 0.95, 55, (98, 60, 234))

def in_game():
    txt = 0
    pygame.mixer.init()
    f1 = pygame.mixer.Sound("ressources/first_fight.ogg")
    f1.set_volume(0.2)
    f1.play()
    hit_sound = pygame.mixer.Sound("ressources/pse.ogg")
    phit_sound = pygame.mixer.Sound("ressources/pse.ogg")
    fight_sound = pygame.mixer.Sound("ressources/fight.ogg")
    txt2 = 0
    stance = 0
    life = 600
    life_en = 600
    en_lowatk = 0
    en_highatk = 0
    en_middleatk = 0
    life_en2 = 600
    frame_atk = 0
    space_pressed = 0
    first_fight = 0
    second_fight = 0
    wait_stance = 0
    persuasion = 0
    persuasion2 = 0
    rage = 0
    next_anim = 0
    up_guard = 0
    down_guard = 0
    middle_guard = 0
    atk_launched = 0
    atk_hit = 0
    screen = screenSize(1920, 1080)
    x = 250
    pos_enx = 3000
    pos_enx2 = 6000
    setBackgroundImage( ["ressources/wall120.jpg"] )
    road = makeSprite("ressources/road1.jpg")
    addSpriteImage(road, "ressources/road2.jpg")
    addSpriteImage(road, "ressources/road3.jpg")
    addSpriteImage(road, "ressources/road4.jpg")
    addSpriteImage(road, "ressources/road5.jpg")
    fight = makeSprite("ressources/fight.png")
    moveSprite(fight, 720, -50)
    stickman = makeSprite("ressources/anim_walk3.png")
    addSpriteImage(stickman, "ressources/anim_walk2.png")
    addSpriteImage(stickman, "ressources/anim_walk1.png")
    addSpriteImage(stickman, "ressources/highguard.png")
    addSpriteImage(stickman, "ressources/middleguard.png")
    addSpriteImage(stickman, "ressources/lowguard.png")
    addSpriteImage(stickman, "ressources/lowatk1.png")
    addSpriteImage(stickman, "ressources/lowatk2.png")
    addSpriteImage(stickman, "ressources/lowatk3.png")
    addSpriteImage(stickman, "ressources/lowatk4.png")
    addSpriteImage(stickman, "ressources/hightatk1.png")
    addSpriteImage(stickman, "ressources/hightatk2.png")
    addSpriteImage(stickman, "ressources/hightatk3.png")
    addSpriteImage(stickman, "ressources/hightatk4.png")
    addSpriteImage(stickman, "ressources/middleatk1.png")
    addSpriteImage(stickman, "ressources/middleatk2.png")
    addSpriteImage(stickman, "ressources/middleatk3.png")
    addSpriteImage(stickman, "ressources/middleatk4.png")
    enemy_stick = makeSprite("ressources/anim_walkch1.png")
    addSpriteImage(enemy_stick, "ressources/anim_walkch2.png")
    addSpriteImage(enemy_stick, "ressources/anim_walkch3.png")
    addSpriteImage(enemy_stick, "ressources/middleguarden.png")
    addSpriteImage(enemy_stick, "ressources/highguarden.png")
    addSpriteImage(enemy_stick, "ressources/lowguarden.png")
    enemy_stick2 = makeSprite("ressources/walk1en1.png")
    addSpriteImage(enemy_stick2, "ressources/walk2en1.png")
    addSpriteImage(enemy_stick2, "ressources/walk3en1.png")
    addSpriteImage(enemy_stick2, "ressources/highguarden1.png")
    addSpriteImage(enemy_stick2, "ressources/middleguarden1.png")
    addSpriteImage(enemy_stick2, "ressources/lowguarden1.png")
    addSpriteImage(enemy_stick, "ressources/lowatk1en1.png")
    addSpriteImage(enemy_stick2, "ressources/lowatk2en1.png")
    addSpriteImage(enemy_stick2, "ressources/lowatk3en1.png")
    addSpriteImage(enemy_stick2, "ressources/lowatk5en1.png")
    addSpriteImage(enemy_stick2, "ressources/hightatk1en1.png")
    addSpriteImage(enemy_stick2, "ressources/hightatk2en1.png")
    addSpriteImage(enemy_stick2, "ressources/middleatk1en1.png")
    addSpriteImage(enemy_stick2, "ressources/middleatk2en1.png")
    addSpriteImage(enemy_stick2, "ressources/middleatk3en1.png")
    addSpriteImage(enemy_stick2, "ressources/middleatk4en1.png")

    moveSprite(road, 1920, 980, True)
    moveSprite(stickman, 250, 800, True)
    moveSprite(enemy_stick, 3000, 800, True)
    moveSprite(enemy_stick2, 6000, 800, True)
    showSprite(road)
    showSprite(stickman)
    showSprite(enemy_stick)
    showSprite(enemy_stick2)

    nextFrame = clock()

    txt3 = 0
    persuaded = 0
    frame = 0
    frame3 = 0
    in_fight = 0
    in_fight2 = 0
    frameupguard = 3
    en1_middle_stance = 0
    en1_high_stance = 0
    en1_low_stance = 0
    en2_middle_stance = 0
    en2_high_stance = 0
    en2_low_stance = 0
    framemiddleguard = 4
    count_txt1 = 0
    count_txt2 = 0
    framedownguard = 5
    player_hit = 0
    framelowatk = 6
    high_pary1 = 0
    low_pary1 = 0
    middle_parry1 = 0
    en1_framefight1 = 3
    en1_framefight2 = 4
    count_atk2 = 0
    en1_framefight3 = 5
    wait_stance2 = 0
    per_text = 0
    show_hp = 0
    show_hp2 = 0
    framehighatk = 10
    framewait_stance = 0
    player_hithigh = 0
    count_txt3 = 0
    count_txt4 = 0
    count_txt5 = 0
    player_hitmiddle = 0
    player_hitlow = 0
    framewait_stance2 = 0
    framemiddleatk = 14
    count_drawed = 0
    frame2 = 0
    count_enemybar = 0
    pos_road = 1920
    citation = makeLabel("", 40, 50, 250, (98, 60, 234), "Agency FB", "white")


    while True:
        if in_fight2 == 1:
            if life_en2 >= 0:
                life_barneg = drawRect(1875 - (625 - life_en2), 50, 625 - life_en2, 75, (84, 66, 107))
                if persuasion >= 400:
                    persuaded = 1
            else:
                empty = drawRect(1250, 50, 625, 75, (84, 66, 107))
                txt3 = 1
            if show_hp2 == 0:
                store_bar5 = drawRect(1250, 50, 625, 75, (84, 66, 107))
                store_bar6 = drawRect(1450, 150, 425, 75, (84, 66, 107))
                life_baren2 = drawRect(1270, 60, life_en2 * 0.95, 55, (222, 60, 75))
                persuasion_bar2 = drawRect(1470, 160, persuasion * 0.95, 55, (98, 60, 234))
                show_hp2 = 1
            if not x - pos_enx2 >= -150 and x - pos_enx2 <= 150:
                frame3 += 1
                pos_enx2 -= 10
                if frame3 >= 2:
                    frame3 = 0
                changeSpriteImage(enemy_stick2, frame3)
                moveSprite(enemy_stick2, pos_enx2, 800, True)

            if x - pos_enx2 >= -150 and x - pos_enx2 <= 150 and atk_hit == 0:
                if count_atk2 == 0 and wait_stance2 == 0:
                    rand_atk = randint(1, 3)
                    wait_stance2 = 1
                    count_atk2 = 1
                if rand_atk == 1:
                    en2_high_stance = 1
                    if en2_high_stance == 1 and wait_stance2 == 0 and count_atk2 == 1:
                        changeSpriteImage(enemy_stick2, 3)
                        high_pary1 = 1
                        low_pary1 = 0
                        middle_parry1 = 0
                        wait_stance2 = 1
                        count_atk2 = 2
                    elif en2_high_stance == 1 and wait_stance2 == 0 and count_atk2 == 2:
                        changeSpriteImage(enemy_stick2, 10)
                        wait_stance2 = 1
                        count_atk2 = 3
                    elif en2_high_stance == 1 and wait_stance2 == 0 and count_atk2 == 3:
                        changeSpriteImage(enemy_stick2, 11)
                        wait_stance2 = 1
                        count_atk2 = 0
                        en2_high_stance = 0
                        next_anim = 1
                        atk_hit = 1
                if rand_atk == 2:
                    en2_middle_stance = 1
                    if en2_middle_stance == 1 and wait_stance2 == 0 and count_atk2 == 1:
                        changeSpriteImage(enemy_stick2, 4)
                        high_pary1 = 0
                        low_pary1 = 0
                        middle_parry1 = 1
                        wait_stance2 = 1
                        count_atk2 = 2
                    elif en2_middle_stance == 1 and wait_stance2 == 0 and count_atk2 == 2:
                        changeSpriteImage(enemy_stick2, 12)
                        wait_stance2 = 1
                        count_atk2 = 3
                    elif en2_middle_stance == 1 and wait_stance2 == 0 and count_atk2 == 3:
                        changeSpriteImage(enemy_stick2, 13)
                        wait_stance2 = 1
                        count_atk2 = 4
                    elif en2_middle_stance == 1 and wait_stance2 == 0 and count_atk2 == 4:
                        changeSpriteImage(enemy_stick2, 14)
                        wait_stance2 = 1
                        count_atk2 = 0
                        en2_middle_stance = 0
                        next_anim = 1
                        atk_hit = 1
                if rand_atk == 3:
                    en2_low_stance = 1
                    if en2_low_stance == 1 and wait_stance2 == 0 and count_atk2 == 1:
                        changeSpriteImage(enemy_stick2, 5)
                        high_pary1 = 0
                        low_pary1 = 1
                        middle_parry1 = 0
                        wait_stance2 = 1
                        count_atk2 = 2
                    elif en2_low_stance == 1 and wait_stance2 == 0 and count_atk2 == 2:
                        changeSpriteImage(enemy_stick2, 6)
                        wait_stance2 = 1
                        count_atk2 = 3
                    elif en2_low_stance == 1 and wait_stance2 == 0 and count_atk2 == 3:
                        changeSpriteImage(enemy_stick2, 7)
                        wait_stance2 = 1
                        count_atk2 = 4
                    elif en2_low_stance == 1 and wait_stance2 == 0 and count_atk2 == 4:
                        changeSpriteImage(enemy_stick2, 8)
                        wait_stance2 = 1
                        count_atk2 = 5
                    elif en2_low_stance == 1 and wait_stance2 == 0 and count_atk2 == 5:
                        changeSpriteImage(enemy_stick2, 9)
                        wait_stance = 1
                        count_atk2 = 0
                        en2_low_stance = 0
                        next_anim = 1
                        atk_hit = 1
        if wait_stance2 == 1:
            framewait_stance2 += 0.5
            if framewait_stance2 == 2:
                wait_stance2 = 0
                framewait_stance2 = 0
        count_drawed += 1
        if life >= 0:
            life_barnegp = drawRect(675 - (625 - life), 50, 625 - life, 75, (84, 66, 107))
        else:
            emptyp = drawRect(50, 50, 625, 75, (84, 66, 107))
            if count_txt5 == 0:
                killSprite(stickman)
                stance = 0
                labelos7 = makeLabel("Vous êtes mort (aïe)", 40, 400, 400, (84, 66, 107), "Agency FB", "white")
                label_next7 = makeLabel("Appuie sur N pour quitter", 40, 800, 500, (84, 66, 107), "Agency FB", "white")
                showLabel(labelos7)
                showLabel(label_next7)
                count_txt5 = 1
            if keyPressed("n") and count_txt5 == 1:
                pygame.quit()
            
        if show_hp == 0:
            store_bar = drawRect(50, 50, 625, 75, (84, 66, 107))
            store_bar2 = drawRect(50, 150, 425, 75, (84, 66, 107))
            life_bar = drawRect(70, 60, life * 0.95, 55, (222, 60, 75))
            rage_bar = drawRect(70, 160, rage * 0.95, 55, (231, 223, 198))
        if pos_enx == 1200 and first_fight == 0:
            txt = 1
        
        if pos_enx2 <= 1690 and second_fight == 0:
            txt2 = 1
        
        if pos_road <= 0 or pos_road >= 2500:
            pos_road = 1920
        if txt == 1:
            if show_hp == 0:
                store_bar3 = drawRect(1250, 50, 625, 75, (84, 66, 107))
                store_bar4 = drawRect(1450, 150, 425, 75, (84, 66, 107))
                life_baren = drawRect(1270, 60, life_en * 0.95, 55, (222, 60, 75))
                persuasion_bar = drawRect(1470, 160, persuasion * 0.95, 55, (98, 60, 234))
                show_hp = 1
            if first_fight == 0 and count_txt1 == 0:
                labelos = makeLabel("La vie c'est pas facile tous les jours tu sais...", 40, 400, 400, (84, 66, 107), "Agency FB", "white")
                label_next = makeLabel("Appuie sur N pour continuer", 40, 800, 500, (84, 66, 107), "Agency FB", "white")
                showLabel(labelos)
                showLabel(label_next)
                count_txt1 = 1
            if keyPressed("n"):
                first_fight = 1
                txt = 0
        if txt2 == 1:
            if show_hp == 0:
                store_bar3 = drawRect(1250, 50, 625, 75, (84, 66, 107))
                store_bar4 = drawRect(1450, 150, 425, 75, (84, 66, 107))
                life_baren = drawRect(1270, 60, life_en * 0.95, 55, (222, 60, 75))
                persuasion_bar = drawRect(1470, 160, persuasion * 0.95, 55, (98, 60, 234))
                show_hp = 1
            if second_fight == 0 and count_txt2 == 0:
                labelos2 = makeLabel("Alors toi tu va passer un sale quart d'heure", 40, 400, 400, (84, 66, 107), "Agency FB", "white")
                label_next2 = makeLabel("Appuie sur N pour continuer", 40, 800, 500, (84, 66, 107), "Agency FB", "white")
                showLabel(labelos2)
                showLabel(label_next2)
                count_txt2 = 1
            if keyPressed("n") and count_txt2 == 1:
                hideLabel(labelos2)
                hideLabel(label_next2)
                fight_sound.play()
                persuasion = 0
                second_fight = 1
                txt2 = 0
        if txt3 == 1:
            killSprite(enemy_stick2)
            in_fight2 = 0
            stance = 0
            if count_txt3 == 0:
                labelos3 = makeLabel("Félicitations vous avez survécu", 40, 400, 400, (84, 66, 107), "Agency FB", "white")
                label_next3 = makeLabel("Appuie sur N pour quitter", 40, 800, 500, (84, 66, 107), "Agency FB", "white")
                showLabel(labelos3)
                showLabel(label_next3)
                count_txt3 = 1
            if keyPressed("n") and count_txt3 == 1:
                pygame.quit()
        
        if persuaded == 1:
            in_fight2 = 0
            stance = 0
            if count_txt4 == 0:
                labelos4 = makeLabel("Vous êtes un type bien, j'aurais du savoir que la violence n'est pas la solution *lache 1000 balles*", 40, 400, 400, (84, 66, 107), "Agency FB", "white")
                label_next4 = makeLabel("Appuie sur N pour quitter", 40, 800, 500, (84, 66, 107), "Agency FB", "white")
                showLabel(labelos4)
                showLabel(label_next4)
                count_txt4 = 1
            if keyPressed("n") and count_txt4 == 1:
                pygame.quit()

        if first_fight == 1:
            #start 1st dialogue
            if count_txt1 == 1:
                changeLabel(labelos, "Je ne te connais pas mais je vais t'apprendre à te battre si ça te dérange pas")
                count_txt1 = 2
            elif count_txt1 == 2 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "J'ai vu Kung Fu Panda je m'y connais tkt")
                count_txt1 = 3
                wait_stance = 1
            elif count_txt1 == 3 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Pour commencer tu peux parer en utilisant les différentes gardes.")
                count_txt1 = 4
                wait_stance = 1
            elif count_txt1 == 4 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Appuie sur Z ou S sans bouger pour naviguer entre les gardes.")
                count_txt1 = 5
                wait_stance = 1
            elif count_txt1 == 5 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Il y en a 3 différentes: basse, moyenne et haute. Chacune bloque le coup qui lui est associé.")
                count_txt1 = 6
                wait_stance = 1
            elif count_txt1 == 6 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Pour castagner tes opposants appuie sur BARRE ESPACE, l'attaque dépend de ta garde.")
                count_txt1 = 7
                wait_stance = 1
            elif count_txt1 == 7 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Si tu es face à un bon advesaire, il se protègera aussi de tes coups donc fait attention.")
                count_txt1 = 8
                wait_stance = 1
            elif count_txt1 == 8 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Si jamais tu dois te battre, frappe la ou il ne garde pas pour infliger des dégats.")
                count_txt1 = 9
                wait_stance = 1
            elif count_txt1 == 9 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Tu peux t'entrainer sur moi mais j'ai de bon réflexes.")
                count_txt1 = 10
                wait_stance = 1
            elif count_txt1 == 10 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Sinon tu peux continuer à avancer, mais fais attention par ici ça grouille de types louches.")
                count_txt1 = 11
                wait_stance = 1
            elif count_txt1 == 11 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Et si t'es vraiment un type bien, tu les frappes pas et t'essayes de discuter avec eux.")
                count_txt1 = 12
                wait_stance = 1
            elif count_txt1 == 12 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Tu peux faire ça avec la touche P pendant un combat.")
                count_txt1 = 13
                wait_stance = 1
            elif count_txt1 == 13 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Si leur barre de persuasion monte au max, il y a moyen qu'ils soient cools avec toi.")
                count_txt1 = 14
                wait_stance = 1
            elif count_txt1 == 14 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "Sur ce, que la force soit avec toi.")
                count_txt1 = 15
                wait_stance = 1
            elif count_txt1 == 15 and keyPressed("n") and wait_stance == 0:
                changeLabel(labelos, "*Vous obtenez: [Art du combat: Kung Fu (Panda)]*", (98, 60, 234))
                count_txt1 = 16
                wait_stance = 1
            elif count_txt1 == 16 and keyPressed("n") and wait_stance == 0:
                fight_sound.play()
                hideLabel(labelos)
                hideLabel(label_next)
                showSprite(fight)
                count_txt1 = 0
                wait_stance = 1
            #end 1st dialogue
            in_fight = 1
            enemy_life(persuasion, life_en)
        if second_fight == 1:
            hideLabel(labelos2)
            hideLabel(label_next)
            showSprite(fight)
            count_txt2 = 0
            in_fight2 = 1

        if show_hp == 1:
            persuasion_bar = drawRect(1470, 160, persuasion * 0.95, 55, (98, 60, 234))

        if per_text >= 1:
            per_text += 1

        if per_text == 30:
            per_text = 0
            hideLabel(citation)
        if stance == 1:
            if keyPressed("p") and per_text == 0:
                changeLabel(citation, random_cit())
                showLabel(citation)
                per_text += 1
                persuasion += 15
            if (keyPressed("q") or keyPressed("d")) and frame_atk == 0:
                stance = 0
                up_guard = 0
                down_guard = 0
                middle_guard = 0
                space_pressed = 0
                en1_high_stance = 0
                en1_low_stance = 0
                en1_middle_stance = 0
            if keyPressed("z") and up_guard == 0 and down_guard == 0 and middle_guard == 0 and frame_atk == 0 and wait_stance == 0:
                middle_guard = 0
                down_guard = 0
                up_guard = 1
                wait_stance = 1
            elif keyPressed("z") and down_guard == 0 and middle_guard == 1 and frame_atk == 0 and wait_stance == 0:
                down_guard = 0
                up_guard = 1
                middle_guard = 0
                wait_stance = 1
            elif keyPressed("s") and up_guard == 1 and down_guard == 0 and frame_atk == 0 and wait_stance == 0:
                down_guard = 0
                middle_guard = 1
                up_guard = 0
                wait_stance = 1
            elif keyPressed("z") and down_guard == 1 and up_guard == 0 and frame_atk == 0 and wait_stance == 0:
                up_guard = 0
                middle_guard = 1
                down_guard = 0
                wait_stance = 1
            elif keyPressed("s") and middle_guard == 1 and up_guard == 0 and frame_atk == 0 and wait_stance == 0 and stance == 1:
                up_guard = 0
                down_guard = 1
                middle_guard = 0
                wait_stance = 1
            elif keyPressed("s") and middle_guard == 0 and up_guard == 0 and down_guard == 0 and frame_atk == 0 and wait_stance == 0 and stance == 1:
                up_guard = 0
                middle_guard = 0
                down_guard = 1
                wait_stance = 1
            elif wait_stance == 1:
                framewait_stance += 0.5
                if framewait_stance == 2:
                    wait_stance = 0
                    framewait_stance = 0
            if middle_guard == 1:
                if space_pressed == 0:
                    changeSpriteImage(stickman, framemiddleguard)
                if keyPressed("space") and space_pressed == 0 and frame_atk == 0:
                    if first_fight == 1:
                        en1_high_stance = 0
                        en1_low_stance = 0
                        en1_middle_stance = 1
                        if en1_middle_stance == 1:
                            changeSpriteImage(enemy_stick, en1_framefight1)
                    space_pressed = 1
                if space_pressed == 1:
                    frame_atk += 1
                    if frame_atk == 1 and framemiddleatk == 14:
                        changeSpriteImage(stickman, framemiddleatk)
                        framemiddleatk = 15
                    elif framemiddleatk == 15 and frame_atk == 2:
                        changeSpriteImage(stickman, framemiddleatk)
                        framemiddleatk = 16
                    elif framemiddleatk == 16 and frame_atk == 3:
                        changeSpriteImage(stickman, framemiddleatk)
                        framemiddleatk = 17
                    elif (framemiddleatk == 17 or framemiddleatk == 14) and frame_atk == 4:
                        changeSpriteImage(stickman, framemiddleatk)
                        player_hitmiddle = 1
                        framemiddleatk = 14
                    elif frame_atk == 5:
                        space_pressed = 0
                        player_hitmiddle = 0
                        frame_atk = 0
            if up_guard == 1:
                if space_pressed == 0:
                    changeSpriteImage(stickman, frameupguard)
                if keyPressed("space") and space_pressed == 0 and frame_atk == 0:
                    if first_fight == 1:
                        en1_middle_stance = 0
                        en1_low_stance = 0
                        en1_high_stance = 1
                        if en1_high_stance == 1:
                            changeSpriteImage(enemy_stick, en1_framefight2)
                    space_pressed = 1
                if space_pressed == 1:
                    frame_atk += 0.5
                    if frame_atk == 1 and framehighatk == 10:
                        changeSpriteImage(stickman, framehighatk)
                        framehighatk = 11
                    elif (framehighatk == 11 or framehighatk == 10) and frame_atk == 2:
                        changeSpriteImage(stickman, framehighatk)
                        framehighatk = 10
                        player_hithigh = 1
                    elif frame_atk == 3:
                        space_pressed = 0
                        frame_atk = 0
                        player_hithigh = 0
            if down_guard == 1:
                if space_pressed == 0:
                    changeSpriteImage(stickman, framedownguard)
                if keyPressed("space") and space_pressed == 0 and frame_atk == 0:
                    if first_fight == 1:
                        en1_high_stance = 0
                        en1_middle_stance = 0
                        en1_low_stance = 1
                        if en1_low_stance == 1:
                            changeSpriteImage(enemy_stick, en1_framefight3)
                    space_pressed = 1
                if space_pressed == 1:
                    frame_atk += 1
                    if frame_atk == 1 and framelowatk == 6:
                        changeSpriteImage(stickman, framelowatk)
                        framelowatk = 7
                    elif framelowatk == 7 and frame_atk == 2:
                        changeSpriteImage(stickman, framelowatk)
                        framelowatk = 8
                    elif framelowatk == 8 and frame_atk == 3:
                        changeSpriteImage(stickman, framelowatk)
                        framelowatk = 9
                    elif (framelowatk == 9 or framelowatk == 6) and frame_atk == 4:
                        changeSpriteImage(stickman, framelowatk)
                        framelowatk = 6
                        player_hitlow = 1
                    elif frame_atk == 5:
                        space_pressed = 0
                        player_hitlow = 0
                        frame_atk = 0
        
        if x - pos_enx2 >= -150 and x - pos_enx2 <= 150 and atk_hit == 1 and rand_atk == 1 and wait_stance == 0:
            if up_guard == 0 and wait_stance == 0:
                hit_sound.play()
                life -= 75
                wait_stance = 1
            atk_hit = 0
        if x - pos_enx2 >= -150 and x - pos_enx2 <= 150 and atk_hit == 1 and rand_atk == 2 and wait_stance == 0:
            if middle_guard == 0 and wait_stance == 0:
                hit_sound.play()
                life -= 75
                wait_stance = 1
            atk_hit = 0
        if x - pos_enx2 >= -150 and x - pos_enx2 <= 150 and atk_hit == 1 and rand_atk == 3 and wait_stance == 0:
            if down_guard == 0 and wait_stance == 0:
                hit_sound.play()
                life -= 75
                wait_stance = 1
            atk_hit = 0
        
        if x - pos_enx2 >= -150 and x - pos_enx2 <= 150 and player_hithigh == 1 and wait_stance == 0:
            if high_pary1 == 0 and wait_stance == 0:
                phit_sound.play()
                life_en2 -= 75
                wait_stance = 1
        if x - pos_enx2 >= -150 and x - pos_enx2 <= 150 and player_hitmiddle == 1 and wait_stance == 0:
            if middle_parry1 == 0 and wait_stance == 0:
                phit_sound.play()
                life_en2 -= 75
                wait_stance = 1
        if x - pos_enx2 >= -150 and x - pos_enx2 <= 150 and player_hitlow == 1 and wait_stance == 0:
            if low_pary1 == 0 and wait_stance == 0:
                phit_sound.play()
                life_en2 -= 75
                wait_stance = 1

        if keyPressed("d") and txt == 0 and stance == 0 and in_fight == 0 and txt2 == 0 and in_fight2 == 0 and frame_atk == 0:
            stance = 0
            frame2 += 1
            frame3 += 1
            frame += 1
            pos_enx -= 50
            pos_enx2 -= 60
            pos_road -= 50
            changeSpriteImage(stickman, frame)
            changeSpriteImage(enemy_stick, frame2)
            changeSpriteImage(enemy_stick2, frame3)
            if frame == 2:
                frame = 0
                frame2 = 0
                frame3 = 0
            moveSprite(road, pos_road, 980, True)
            moveSprite(stickman, x, 800, True)
            moveSprite(enemy_stick, pos_enx, 800, True)
            moveSprite(enemy_stick2, pos_enx2, 800, True)
            scrollBackground(-5, 0)
        elif keyPressed("d") and txt == 0 and stance == 0 and in_fight == 1 and in_fight2 == 0 and frame_atk == 0:
            stance = 0
            frame += 1
            x += 15
            if x == 1930:
                f1.stop()
                f2 = pygame.mixer.Sound("ressources/menu.ogg")
                f2.play()
                hideSprite(enemy_stick)
                hideSprite(fight)
                first_fight = 2
                loading = makeLabel("Loading ...", 40, 800, 400, (84, 66, 107), "Agency FB", "white")
                showLabel(loading)
                for x in range (count_drawed):
                    clearShapes()
                count_drawed = 0
                x = 250
                in_fight = 0
                hideLabel(loading)
                show_hp = 0
                persuasion = 0
                if first_fight == 2:
                    setBackgroundImage( ["ressources/wall2.jpg"] )
                    changeSpriteImage(road, 2)
            changeSpriteImage(stickman, frame)
            if frame == 2:
                frame = 0
                frame2 = 0
            moveSprite(stickman, x, 800, True)
        elif keyPressed("d") and txt == 0 and stance == 0 and in_fight == 0 and in_fight2 == 1 and frame_atk == 0:
            stance = 0
            frame += 1
            frame3 += 1
            x += 15
            pos_enx2 -= 15
            if x == 1930:
                hideSprite(enemy_stick)
                hideSprite(fight)
                first_fight = 2
                loading = makeLabel("Loading ...", 40, 800, 400, (84, 66, 107), "Agency FB", "white")
                showLabel(loading)
                for x in range (count_drawed):
                    clearShapes()
                count_drawed = 0
                x = 250
                in_fight = 0
                hideLabel(loading)
                if first_fight == 2:
                    setBackgroundImage( ["ressources/wall2.jpg"] )
                    changeSpriteImage(road, 2)
            changeSpriteImage(stickman, frame)
            changeSpriteImage(enemy_stick2, frame3)
            if frame == 2:
                frame = 0
                frame2 = 0
                frame3 = 0
            moveSprite(stickman, x, 800, True)
            moveSprite(enemy_stick2, pos_enx2, 800, True)


        if keyPressed("q") and txt == 0 and stance == 0 and in_fight == 0 and txt2 == 0 and in_fight2 == 0 and frame_atk == 0:
            stance = 0
            frame += 1
            frame2 += 1
            frame3 += 1
            pos_enx += 50
            pos_enx2 += 50
            pos_road += 50
            changeSpriteImage(stickman, frame)
            changeSpriteImage(enemy_stick, frame2)
            changeSpriteImage(enemy_stick2, frame3)
            if frame == 2:
                frame2 = 0
                frame3 = 0
                frame = 0
            moveSprite(road, pos_road, 980, True)
            moveSprite(stickman, x, 800, True)
            moveSprite(enemy_stick, pos_enx, 800, True)
            moveSprite(enemy_stick2, pos_enx2, 800, True)

            scrollBackground(5, 0)
        elif keyPressed("q") and txt == 0 and stance == 0 and in_fight == 1 and frame_atk == 0:
            stance = 0
            frame += 1
            x -= 15
            changeSpriteImage(stickman, frame)
            if frame == 2:
                frame = 0
                frame2 = 0
            moveSprite(stickman, x, 800, True)
        elif keyPressed("q") and txt == 0 and stance == 0 and in_fight2 == 1 and frame_atk == 0:
            stance = 0
            frame += 1
            frame3 += 1
            x -= 15
            pos_enx2 += 10
            changeSpriteImage(stickman, frame)
            changeSpriteImage(enemy_stick2, frame3)
            if frame == 2:
                frame = 0
                frame2 = 0
                frame3 = 0
            moveSprite(stickman, x, 800, True)
            moveSprite(enemy_stick2, pos_enx2, 800, True)
        elif txt == 0 and stance == 0:
            stance = 1
        if x <= 0:
            x += 30
            moveSprite(stickman, x, 800, True)
            scrollBackground(-10, 0)
        if pos_enx2 <= 0:
            pos_enx2 += 30
            moveSprite(enemy_stick2, pos_enx2, 800, True)
            scrollBackground(-10, 0)
        if x >= 1920:
            x -= 30
            moveSprite(stickman, x, 800, True)
            scrollBackground(10, 0)

        tick(15)

    endWait()
