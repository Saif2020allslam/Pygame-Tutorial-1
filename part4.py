import pygame
from settings import *
from Opj import *
pygame.init()


clock = pygame.time.Clock() 
win = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption(Title)

bg = pygame.image.load("image/bg.png").convert_alpha()
bg = pygame.transform.scale(bg,(screen_w, screen_h))
# Ground =>(60,470)
r = Rabbit(60,470)
while run:
    clock.tick(30)
    
    # Chack The Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    r.animat(win)
    r.run()
    # Drawing Part        
    pygame.display.update()
    win.fill((0,0,0))
    win.blit(bg,(0,0))
    
pygame.quit()
