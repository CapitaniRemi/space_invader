import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application
import math
from pygame.locals import *

pygame.init()
# création de la fenêtre
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#pygame.display.set_icon('abricot.png')
pygame.display.set_caption("Space Invaders")
# chargement de l'image de fond
fond = pygame.image.load('background.jpg')
#musique
musique = pygame.mixer.music.load('musique_menu.mp3')
pygame.mixer.music.play(-1)

# creation du joueur
player = space.Joueur()
# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"
#creation du score
score = space.Score = 0
# creation des ennemis
listeEnnemis = []
for indice in range (space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
#création des amis
listeAmis = []
for indice2 in range (space.Ami.NbAmis) :
    vaisseau_ami = space.Ami()
    listeAmis.append(vaisseau_ami)
#creation des météorites
listeMeteorite = []
for indice3 in range(space.Meteorite.NbMeteorite) :
    meteorites = space.Meteorite()
    listeMeteorite.append(meteorites)

def regles() :
    pygame.init()
    texte1 = space.Texte('Mouvements :', 80, 20, 40)
    texte2 = space.Texte('Flèche droite et flèche gauche pour se diriger', 80, 20, 100)
    texte3 = space.Texte('Explications :', 80, 20, 160)
    texte4 = space.Texte('Chaque ennemi touché vaut 1 point, ', 80, 20, 220)
    texte5 = space.Texte('mais chaque ennemi laissé passer fait perdre 1 point', 80, 20, 280)
    texte6 = space.Texte('Un vaisseau ami touché fait perdre 5 points', 80, 20, 340)
    texte7 = space.Texte('mais chaque vaisseau laissé passer rapporte 1 points' ,80, 20, 400)
    retour = space.Texte('Retour', 50, 30, 30)
    quitter = space.Texte('Quitter', 50, 150, 30)
    regles = True
    while regles :
        screen.blit(fond, (0, 0))
        texte1.iblit(screen)
        texte2.iblit(screen)
        texte3.iblit(screen)
        texte4.iblit(screen)
        texte5.iblit(screen)
        texte6.iblit(screen)
        texte7.iblit(screen)
        retour.iblit(screen)
        quitter.iblit(screen)
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()

                  # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT:  # si l'événement est le clic sur la fermeture de la fenêtre
                running = False  # running est sur False
                sys.exit()  # pour fermer correctement
            if retour.collision((x, y)) and pygame.MOUSEBUTTONUP == event.type:
                menu()

            if quitter.collision((x,y)) and pygame.MOUSEBUTTONUP == event.type:
                pygame.quit()
        pygame.display.update()

def menu_fin() :

    pygame.init()
    pygame.display.set_caption("Une autre partie ?")
    image_gameover1 = pygame.image.load('game_over1.png').convert_alpha()
    image_gameover2 = pygame.image.load('game_over2.png').convert_alpha()
    rejouer = space.Texte('Rejouer ?', 90, 100, 100)
    quitter = space.Texte('Quitter', 90, 500, 100)
    menu = space.Texte('Menu', 90, 900, 100)
    menu_fin = True
    while menu_fin :
        screen.blit(fond,(0,0))
        rejouer.iblit(screen)
        menu.iblit(screen)
        quitter.iblit(screen)
        screen.blit(image_gameover1, (550, 100 ))
        screen.blit(image_gameover2, (400, 300))

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()

                  # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT:  # si l'événement est le clic sur la fermeture de la fenêtre
                running = False  # running est sur False
                sys.exit()  # pour fermer correctement
            if rejouer.collision((x, y)) and pygame.MOUSEBUTTONUP == event.type:
                jeu()

            if quitter.collision((x,y)) and pygame.MOUSEBUTTONUP == event.type:
                pygame.quit()

            if menu.collision((x, y)) and pygame.MOUSEBUTTONUP == event.type :
                menu()

        for ami in listeAmis :
            ami.avancer()
            screen.blit(ami.image, [ami.depart, ami.hauteur]) #appel de la fonction qui dessine les amis
            if ami.hauteur > 1080 :
                ami.disparaitre()

        pygame.display.update()

def menu_gagnee() :

    pygame.init()
    pygame.display.set_caption("Bien joué !")
    image_gameover1 = pygame.image.load('game_over1.png').convert_alpha()
    rejouer = space.Texte('Rejouer ?', 90, 100, 70)
    quitter = space.Texte('Quitter', 90, 500, 70)
    menutexte = space.Texte('Menu', 90, 900, 70)
    bienjoue = space.Texte('Bien joué !' ,120, 200, 400)
    menu_gagnee = True
    while menu_gagnee :
        screen.blit(fond,(0,0))
        rejouer.iblit(screen)
        quitter.iblit(screen)
        menutexte.iblit(screen)
        bienjoue.iblit(screen)
        screen.blit(image_gameover1, (800, 110 ))

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()

            # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT:  # si l'événement est le clic sur la fermeture de la fenêtre
                running = False  # running est sur False
                sys.exit()  # pour fermer correctement

            if rejouer.collision((x, y)) and pygame.MOUSEBUTTONUP == event.type:
                jeu()

            if quitter.collision((x,y)) and pygame.MOUSEBUTTONUP == event.type:
                pygame.quit()

            if menutexte.collision((x, y)) and pygame.MOUSEBUTTONUP == event.type:
                menu()

        for ami in listeAmis :
            ami.avancer()
            screen.blit(ami.image, [ami.depart, ami.hauteur]) #appel de la fonction qui dessine les amis
            if ami.hauteur > 1080 :
                ami.disparaitre()

        pygame.display.update()


### BOUCLE DE JEU  ###

def jeu() :
    pygame.init() # lancement des modules inclus dans pygame
    score = space.Texte(f'Score : {player.score}', 45, 45, 35)
    upvie = space.Joueur()
    #laser = pygame.mixer.Sound('laser.mp3')
    #explosion = pygame.mixer.Sound('explosion.mp3')

    running = True # variable pour laisser la fenêtre ouverte
    while running : # boucle infinie pour laisser la fenêtre ouverte
        # dessin du fond
        screen.blit(fond,(0,0))

        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            #si le score est nul, afficher le menu 'game over'
            if player.score < 0 :
                player.score = 0
                menu_fin()

            #si le score est égal à 100, afficher le menu 'gagné'
            if player.score > 100 :
                player.score = 0
                menu_gagnee()

            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False

           # gestion du clavier
            if event.type == KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
                if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                    player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                    player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_SPACE : # espace pour tirer
                    player.tirer()
                    tir.etat = "tiree"
                    #laser.play()
            else : player.sens =""

        ### Actualisation de la scene ###
        # Gestions des collisions
        for ennemi in listeEnnemis:
            if tir.toucher(ennemi):
                ennemi.disparaitre()
                #explosion.play()
                player.marquer()
                score.update(f"Score: {player.score}")

            if player.toucherennemi(ennemi) :
                ennemi.disparaitre()
                player.vie = player.vie - 1
                if player.vie > 0 :
                    player.upvie()
                else :
                    menu_fin()


        for ami in listeAmis :
            if tir.toucher(ami) :
                ami.disparaitre()
                #explosion.play()
                player.score -= 5
                score.update(f"Score: {player.score}")

            if player.toucherami(ami) :
                ami.disparaitre()
                player.vie = player.vie - 1
                if player.vie > 0 :
                    player.upvie()
                else :
                    menu_fin()


        for meteorite in listeMeteorite :
            if tir.toucher(meteorite) :
                meteorite.disparaitre()
                #explosion.play()

            if player.touchermeteorite(meteorite) :
                meteorite.disparaitre()
                player.vie = player.vie - 1
                if player.vie > 0 :
                    player.upvie()
                else :
                    menu_fin()


        # placement des objets
        # le joueur
        player.deplacer()
        screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
        # la balle
        tir.bouger()
        screen.blit(player.image,[player.position, player.hauteur]) # appel de la fonction qui dessine la balle
        # les ennemis
        for ennemi in listeEnnemis:
            ennemi.avancer()
            screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine les ennemis
            if ennemi.hauteur > 1080 :
                player.score -= 2
                score.update(f"Score: {player.score}")
                ennemi.disparaitre()

        #les amis
        for ami in listeAmis :
            ami.avancer()
            screen.blit(ami.image, [ami.depart, ami.hauteur]) #appel de la fonction qui dessine les amis
            if ami.hauteur > 1080 :
                player.score += 1
                score.update(f"Score: {player.score}")
                ami.disparaitre()

        for meteorite in listeMeteorite :
            meteorite.avancer()
            screen.blit(meteorite.image, [meteorite.depart, meteorite.hauteur])
            if meteorite.hauteur > 1080 :
                meteorite.disparaitre()

        #affichage score et vie
        score.iblit(screen)
        #screen.blit(upvie.image, (30, 100))
        pygame.display.update() # pour ajouter tout changement à l'écran

def menu() :

    pygame.init()
    image_menu = pygame.image.load('logo.png')
    image_menu = pygame.transform.scale(image_menu, (500, 400))

    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    largeur = math.ceil(screen.get_width()/2)
    pygame.display.set_caption("Menu")
    # chargement de l'image de fond
    jouer = space.Texte('Jouer', 100, 1017, 200)
    regle = space.Texte('Règles', 100, 980, 300)
    quitter = space.Texte('Quitter', 100, 950, 400)
    menu = True
    while menu : # boucle infinie pour laisser la fenêtre ouverte
        # dessin du fond
        screen.blit(fond,(0,0))
        jouer.iblit(screen)
        regle.iblit(screen)
        quitter.iblit(screen)
        screen.blit(image_menu, (100, 160 ))
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()

                  # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT:  # si l'événement est le clic sur la fermeture de la fenêtre
                running = False  # running est sur False
                sys.exit()  # pour fermer correctement
            if jouer.collision((x, y)) and pygame.MOUSEBUTTONUP == event.type:
                jeu()

            if regle.collision((x, y)) and pygame.MOUSEBUTTONUP == event.type :
                regles()

            if quitter.collision((x,y)) and pygame.MOUSEBUTTONUP == event.type:
                pygame.quit()

        for ami in listeAmis :
            ami.avancer()
            screen.blit(ami.image, [ami.depart, ami.hauteur]) #appel de la fonction qui dessine les amis
            if ami.hauteur > 1080 :
                ami.disparaitre()

        pygame.display.update()  # pour ajouter tout changement à l'écran

menu()