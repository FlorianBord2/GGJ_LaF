import sys, pygame
from citi_fct import brain
from random import randrange

pygame.init()
pygame.font.init()

def print_text(text, taille, color, pos):
    myfont = pygame.font.SysFont('Comic Sans MS', taille)
    textsurface = myfont.render(text, False, color)
    screen.blit(textsurface, pos)
    return textsurface

def print_random(fake, citi, r):
    if r == 0:
        print_text(fake, 42, (0,0,0),(237,234))
        print_text(citi, 42, (0,0,0), (208,380))
    else:
        print_text(fake, 42, (0,0,0),(208,380))
        print_text(citi, 42, (0,0,0), (237,234))

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                if sign_up_rect.collidepoint(pos):
                    return 'up'
                elif sign_down_rect.collidepoint(pos):
                    return 'down'
                elif restart_rect.collidepoint(pos):
                    return 'reset'
                elif start_rect.collidepoint(pos):
                    return 'start'
                return


size = width, height = 800, 800
speed = [2, 2]
black = 0, 0, 100
white = 255, 255, 255

screen = pygame.display.set_mode(size)
#restart
restart = pygame.image.load("restart.png").convert_alpha()
restart_rect = restart.get_rect()
restart_rect.y = 550
restart_rect.x = 40
#start
start = pygame.image.load("start.png").convert_alpha()
start_rect = start.get_rect()
start_rect.x = 550
start_rect.y = 550
#Panneaux
sign_up = pygame.image.load("sign.png").convert_alpha()
sign_down = pygame.image.load("sign.png").convert_alpha()
sign_up_rect = sign_up.get_rect()
sign_up_rect.center = (400,250)
sign_down_rect = sign_down.get_rect()
sign_down_rect.center = (400,400)

MODE = 'creation'

br = brain()
br.load_cities_data()

up_citi = br.get_random_citie()
down_citi = br.get_random_citie()

while 1:
    screen.fill(black)
    screen.blit(sign_up, sign_up_rect)
    screen.blit(pygame.transform.flip(sign_down, True, False), sign_down_rect)
    screen.blit(restart, restart_rect)
    screen.blit(start, start_rect)

    
   
    print_text('Remember the right path !', 42, (255,255,255),(200,20))
    
    if MODE == "creation":

        print_text(up_citi, 42, (0,0,0),(237,234))
        print_text(down_citi, 42, (0,0,0), (208,380))

        print_text(('Your path is ' + str(len(br.path)) + ' long ! Best score :' + str(br.bscore)), 42, (0,0,0), (200, 100))
        pygame.display.flip()
        user_inpout = wait()
        if user_inpout == 'up':
            br.add_path(up_citi)
            up_citi = br.get_random_citie()
            down_citi = br.get_random_citie()
        elif user_inpout == 'down':
            br.add_path(down_citi)
            up_citi = br.get_random_citie()
            down_citi = br.get_random_citie()
        elif user_inpout == 'reset':
            br.score = 0
            br.path = []
        elif user_inpout == 'start':
            MODE = 'run'
            i = 0
        print(br.path)
    
    elif MODE == 'run':

        print_text(('Score : '+ str(br.score) + '/' + str(len(br.path)) + ' Best score :' + str(br.bscore)), 42, (0,0,0), (200, 100))
        fake_citi = br.get_random_citie()
        print(i, br.path[i])
        citi = br.path[i]
        r = randrange(2)
        print_random(fake_citi, citi, r)
        pygame.display.flip()
        user_inpout = wait()
        print(user_inpout, r)
        if user_inpout == 'up' and r == 1:
            br.score = br.score + 1
            print('Correct')
        elif user_inpout == 'down' and r == 0:
            br.score = br.score + 1
            print('Correct')
        else:
            print('ERREUR')
            br.score = 0
            br.path = []
            MODE = 'creation'
        i = i + 1
        if i == len(br.path):
            screen.fill(black)
            print_text('Remember the right path !', 42, (255,255,255),(200,20))
            print_text(('Félicitation ! Vous avez attien le score de ' + str(br.score) + ' !'),50,(0,0,0),(30,400))
            screen.blit(restart, restart_rect)
            pygame.display.flip()
            wait()
            MODE = 'creation'
            br.path=[]
            if (br.bscore < br.score):
                br.bscore = br.score
            br.score = 0

