import pygame  # necessaire pour charger les images et les sons
import random
import math
from pygame.locals import *

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

class Joueur() : # classe pour créer le vaisseau du joueur

    def __init__(self) :
        self.score = 0
        self.vie = 5
        self.upvie()
        self.position =  math.ceil(screen.get_width() /2 -32)
        self.sens = ""
        self.image = pygame.image.load("vaisseau.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (78, 78))
        self.image_rect = self.image.get_rect()
        self.hauteur = math.ceil(screen.get_height() -130)
        self.largeur = math.ceil(screen.get_width() -64)

    def deplacer(self):
        if self.sens=='gauche' and self.position > 0 :
            self.position -= 5
        elif self.sens == "droite" and self.position < self.largeur :
            self.position += 5

    def tirer(self):
        pass

    def marquer(self) :
        self.score += 1

    #def degat(self, amount):
        #if self.vie - amount > amount:
        #    self.vie -= amount
        #else :
        #    self.game.menu_fin()

    def toucherami(self, ami) :
        if -50 < self.hauteur - ami.hauteur < 50 and -50 < self.position - ami.depart < 50 :
            Ami.disparaitre(ami)

    def toucherennemi(self, ennemi) :
        if -50 < self.hauteur - ennemi.hauteur < 50 and -50 < self.position - ennemi.depart < 50 :
            Ennemi.disparaitre(ennemi)

    def touchermeteorite(self, meteorite) :
        if -5 < self.hauteur - meteorite.hauteur < 105 and -5 < self.position - meteorite.depart < 105 :
            Meteorite.disparaitre(meteorite)

    def upvie(self):
        self.barredevie = pygame.image.load(f'barrevie{self.vie}.png').convert_alpha()

class Balle() :

    def __init__(self,joueur):
        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.etat = ""
        self.image = pygame.image.load("balle.png")
        self.depart = joueur.position+33
        self.hauteur = math.ceil(screen.get_height() -110)
        self.joueur = joueur

    def bouger(self):
        if self.etat != 'tiree' :
            self.depart = self.joueur.position+36
        else :
            if self.hauteur > 0 :
                self.hauteur -= 5
            else :
                self.etat = ""
                self.depart = self.joueur.position+36
                self.hauteur = math.ceil(screen.get_height() -135)

    def toucher(self, ennemi) :
        if -5 < self.hauteur - ennemi.hauteur < 105 and -5 < self.depart - ennemi.depart < 105 and self.etat == 'tiree' :
            self.etat = ''
            self.hauteur = math.ceil(screen.get_height() -70)
            return True
        else :
            return False

class Ennemi() :

    NbEnnemis = random.randint(2, 4)

    def __init__(self) :
        self.image = pygame.image.load('invader2.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.depart = random.uniform(35, 1285)
        self.hauteur = -100
        self.vitesse = random.uniform(1, 3)/2

    def avancer(self) :
        self.hauteur += self.vitesse

    def disparaitre(self) :
        self.hauteur = -100
        self.depart = random.randint(35, 1285)
        self.vitesse += 0.02

    

    def espace(self) :
        pass

class Meteorite() :

    NbMeteorite = random.randint(2, 4)

    def __init__(self) :
        self.image = pygame.image.load('meteorite.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.depart = random.uniform(35, 1285)
        self.hauteur = -3000
        self.vitesse = random.uniform(3, 6)
        self.largeur = math.ceil(screen.get_width())

    def avancer(self) :
        self.hauteur += self.vitesse

    def disparaitre(self) :
        self.hauteur = -3000
        self.depart = random.randint(-2000, self.largeur)


class Ami() :

    NbAmis = random.randint(1, 2)

    def __init__(self) :
        self.image = pygame.image.load('invader1.png')
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.depart = random.uniform(35, 1285) 
        self.hauteur = -100
        self.largeur = math.ceil(screen.get_width())
        self.vitesse = random.uniform(3, 5)

    def avancer(self) :
        self.hauteur += self.vitesse

    def disparaitre(self) :
        self.hauteur = -800
        self.depart = random.randint(-500, self.largeur)

    def espace(self) :
        pass

class Texte:
    def __init__(self, texte, size, x, y, color=(255,250,0)) :
        self.texte = texte
        self.size = size
        self.y = y
        self.x = x
        self.color = color
        self.font = pygame.font.Font('retro.ttf', self.size)

        self.update(self.texte)

    def iblit(self,screen):
        screen.blit(self.text, (self.x, self.y))

    def update(self,texte, color=(255, 250, 0)):
        self.text = self.font.render(texte, 1, color)
        self.rect = self.text.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

    def collision(self, mouse_pos) :
        if self.rect.collidepoint(mouse_pos) :
            self.update(self.texte, (0, 0, 0))
            return True
        else :
            self.update(self.texte, (self.color))
            return False

