import pygame
from gl import *


pygame.init()
screen = pygame.display.set_mode((1000,500), pygame.DOUBLEBUF | pygame.HWACCEL) #, pygame.FULLSCREEN)
screen.set_alpha(None)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

def updateFPS():
    fps = str(int(clock.get_fps()))
    fps = font.render(fps, 1, pygame.Color("white"))
    return fps

# def mouse_control(angle):
#     if pygame.mouse.get_focused():
#         difference = pygame.mouse.get_pos()[0] - 250
#         pygame.mouse.set_pos([750, 250])
#         angle += difference * 0.004
#         angle %= math.pi * 2
#         return angle

r = Raycaster(screen)
r.load_map('map2.txt')

isRunning = True
while isRunning:

    r.movement()

    r.coin_collide()

    screen.fill(pygame.Color("gray")) #Fondo

    #Techo
    screen.fill(pygame.Color("saddlebrown"), (int(r.width / 2), 0, int(r.width / 2),int(r.height / 2)))
    
    #Piso
    screen.fill(pygame.Color("dimgray"), (int(r.width / 2), int(r.height / 2), int(r.width / 2),int(r.height / 2)))

    r.render()
    
    # FPS
    screen.fill(pygame.Color("black"), (0,0,30,30))
    screen.blit(updateFPS(), (0,0))
    clock.tick(30)  
    
    pygame.display.update()

pygame.quit()
