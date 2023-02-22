import pygame as pg

FPS = 60 #сколько FPS

#Инициализируем PyGame
pg.init()

#инициализируем экран
screen = pg.display.set_mode((500, 500))

#--------------------------------------------- Для переменных-------

#-----------------------цвета^^^
back_day_fight = pg.image.load('back_fight_day.png').convert_alpha()
back_day_fight = pg.transform.scale(back_day_fight, (500, 500))

back_night_fight = pg.image.load('back_fight_night.png').convert_alpha()
back_night_fight = pg.transform.scale(back_night_fight, (500, 500))

sun_battle = pg.image.load('sun.png').convert_alpha()
sun_battle = pg.transform.scale(sun_battle, (150, 150))


main_char = pg.image.load('main_char.png').convert_alpha()
main_char = pg.transform.scale(main_char, (150, 150))

main_char_left = pg.image.load('main_char_left.png').convert_alpha()
main_char_left = pg.transform.scale(main_char_left, (150, 150))

armor_for_mch = pg.image.load('armor_mc.png')
armor_for_mch = pg.transform.scale(armor_for_mch, (240,240))

colonna_for_mch = pg.image.load('colonna_f_ar_mc.png')
colonna_for_mch = pg.transform.scale(colonna_for_mch, (130,130))


#-----------------------персонажи^^^

char_x_char = 1
char_y_char = 310
gravitation = 3
jump = 60
flagi = 0
sun_y_battle = 10
y_armor_char =220
down_sun_battle_flag = True
up_sun_battle_flag = False



left_flag = False
right_flag = False


background_night_flag_battle_batle = False
background_battle_flag = False

#-----------------------все остальное^^^

#---------------------------------------------^


clock = pg.time.Clock()
# базовый цикл

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and char_y_char==310:
                char_y_char -= jump

    #гравитация           
    if char_y_char<310:
        #
        char_y_char+=gravitation
        if char_y_char>310:
            char_y_char = 310

    #флаги от солнца
    if sun_y_battle<=10:
        down_sun_battle_flag=True
        up_sun_battle_flag = False
    elif sun_y_battle>265:
        up_sun_battle_flag = True
        down_sun_battle_flag = False
    

    #смена дня и ночи(движения солнца)
    if down_sun_battle_flag:
        sun_y_battle+=0.5
    elif up_sun_battle_flag:
        sun_y_battle-=0.5
    #смена дня и ночи(смена фона)
    
    if 12<sun_y_battle<127.5:
        background_battle_flag= True
        background_night_flag_battle_batle = False
    
    elif 127.5 <=sun_y_battle<=265:
        background_night_flag_battle_batle = True
        background_battle_flag= False

    #смена fona
    if background_battle_flag== True:
        screen.blit(back_day_fight,(0,0)) 
    elif background_night_flag_battle_batle == True:
        screen.blit(back_night_fight,(0,0))              

    

    #заливка главного экрана
    screen.blit(sun_battle,(200,sun_y_battle))
    #платформа
    #screen.blit(platform,(200,240))
    

    #вывод персонажа на экран
    

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
         
    #  --------------------------------
         
 
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
     
    screen.blit(armor_for_mch,(270,220))
    screen.blit(colonna_for_mch,(320, 325))

    
    # обновление экрана
    pg.display.flip()


# Quit pygame
pg.quit()