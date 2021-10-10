import pygame
from settings import *

class Rabbit:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.isjump = False
        self.witdh = 50
        self.height = 82
        # Loading Image
        self.walking_img = [pygame.image.load('image/bunny1_walk1.png').convert_alpha(),pygame.image.load('image/bunny1_walk2.png').convert_alpha()]
        self.stand = pygame.image.load('image/bunny1_stand.png').convert_alpha()
        self.stand = pygame.transform.scale(self.stand,(self.witdh,self.height))

        self.walk_l = False
        self.walk_r = False
        self.left = []
        self.right = []
        self.MangeImage()
        self.wc = 0
        self.Get_Rect = pygame.Rect(self.x , self.y, self.witdh, self.height)

    def MangeImage(self):

        # Scale
        for pic in self.walking_img:
            self.img = pygame.transform.scale(pic,(self.witdh,self.height))
            self.right.append(self.img)

        # Flip Images
        for pic in self.right:
            self.left.append(pygame.transform.flip(pic,True,False))
         
    #Animat The Char...
    def animat(self, surface):
        #Draw standing image 
        if self.wc +1 > 30:
            self.wc = 0
        if self.walk_r == False and self.walk_l == False:
            surface.blit(self.stand,(self.Get_Rect.x,self.Get_Rect.y))

        if self.walk_r :
            surface.blit(self.right[self.wc//15], (self.Get_Rect.x,self.Get_Rect.y))
            self.wc +=1 
        if self.walk_l:
            surface.blit(self.left[self.wc//15], (self.Get_Rect.x,self.Get_Rect.y))
            self.wc += 1
    
    def Chack_keys(self):
            
        if self.key[pygame.K_RIGHT]:# Move Right
            self.Get_Rect.x += 6
            self.walk_r = True
            self.walk_l = False
    
        elif self.key[pygame.K_LEFT]: # Move Left
            self.Get_Rect.x -= 6
            self.walk_r = False
            self.walk_l = True

        else:
            # set to the old value
            self.walk_r = False
            self.walk_l = False
            self.wc = 0

         # Part of Jumping and Logic
        if self.key[pygame.K_SPACE]:
            self.isjump = True

    def jump(self):
        # Get keys state 
        self.Chack_keys()
        global v,m,isjump

        if self.isjump:
            self.f = 1/2 * m * v ** 2 # Bower of jumping 
            self.Get_Rect.y -= self.f # jump or fall moation
            v -= 1

            if v < 0:
                m = -1
            if v == -11:
                self.isjump = False
                m = 1
                v = 10
                self.Get_Rect.y += 5

    def run(self):
        # update the game 
        self.key = pygame.key.get_pressed()
        self.Chack_keys()
        self.jump()
        
class Carrot:
    def __init__(self):
    	pass
