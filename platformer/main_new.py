import pygame as pg
import loading_screen as ls

FPS = 60  #сколько FPS

#Инициализируем PyGame
pg.init() 

#название окна
pg.display.set_caption('SnakeSpeare')

#инициализируем экран
screen = pg.display.set_mode((500, 500))

                                                                 

#--------------------------------------------- Для переменных-------

main_char = pg.image.load('main_char.png').convert_alpha()
main_char = pg.transform.scale(main_char, (150, 150))

main_char_left = pg.image.load('main_char_left.png').convert_alpha()
main_char_left = pg.transform.scale(main_char_left, (150, 150))
#-----------------------персонажи^^^

white = 255, 255, 255
#-----------------------цвета^^^
background = pg.image.load('back_ground.png').convert_alpha()
background = pg.transform.scale(background, (500, 500))
#
background_night= pg.image.load('background_night.png').convert_alpha()
background_night= pg.transform.scale(background_night, (500, 500))
#

sun_for_background = pg.image.load('sun.png').convert_alpha()
sun_for_background = pg.transform.scale(sun_for_background, (150, 150))
#
platform = pg.image.load('platform.png').convert_alpha()
platform = pg.transform.scale(platform, (140, 140))

#-----------------------бэкплейс^^^



#-----------------------все остальное^^^
char_x_char = 1
char_y_char = 235
gravitation = 3
jump = 60
flagi = 0
sun_y_char = 10
down_sun_y_flag = True
up_sun_y_flag = False


background_night_flag = False
background_flag = False

#---------------------------------------------

clock = pg.time.Clock()



# базовый цикл
running = True
while running:
    clock.tick(FPS)
    

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and char_y_char==235:
                char_y_char -= jump

    #гравитация           
    if char_y_char<235:
        char_y_char+=gravitation
        if char_y_char>235:
            char_y_char = 235

    #флаги от солнца
    if sun_y_char<=10:
        down_sun_y_flag=True
        up_sun_y_flag = False
    elif sun_y_char>265:
        up_sun_y_flag = True
        down_sun_y_flag = False
    

    #смена дня и ночи(движения солнца)
    if down_sun_y_flag:
        sun_y_char+=0.5
    elif up_sun_y_flag:
        sun_y_char-=0.5
    #смена дня и ночи(смена фона)
    
    if 12<sun_y_char<127.5:
        background_flag = True
        background_night_flag = False
    
    elif 127.5 <=sun_y_char<=265:
        background_night_flag = True
        background_flag = False

    #смена fona
    if background_flag == True:
        screen.blit(background,(0,0)) 
    elif background_night_flag == True:
        screen.blit(background_night,(0,0))              

    

    #заливка главного экрана
    screen.blit(sun_for_background,(200,sun_y_char))
    #платформа
    #screen.blit(platform,(200,240))


    left_flag = False
    right_flag = False


    #управление персонажа
    pk = pg.key.get_pressed()
    

    #-----------------------------
    if pk[pg.K_LEFT]:
        left_flag = True
        flagi=2
        char_x_char-=2


    elif pk[pg.K_RIGHT]:
        right_flag = True
        char_x_char+=2
        flagi=3


    if char_x_char<=-29:
        char_x_char=-30
    elif char_x_char>=401:
        char_x_char=400
    #--------------------------------
        

    #вывод персонажа на экран
    if right_flag:
        screen.blit(main_char, (char_x_char,char_y_char))

        
    elif left_flag:
        screen.blit(main_char_left, (char_x_char,char_y_char))

    elif flagi == 0:
        screen.blit(main_char, (char_x_char,char_y_char))

    else:
        if flagi == 3:
            screen.blit(main_char, (char_x_char,char_y_char))
        elif flagi == 2:
            screen.blit(main_char_left, (char_x_char,char_y_char))


        
            
    
    # обновление экрана
    pg.display.flip()


# Quit pygame
pg.quit()