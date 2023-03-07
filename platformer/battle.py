import pygame as pg

FPS = 60 #сколько FPS

#Инициализируем PyGame
pg.init()

#инициализируем экран
screen = pg.display.set_mode((500, 500))

#--------------------------------------------- Для переменных-------

#-----------------------цвета^^^
day_1layer = pg.image.load("day_1layer.png").convert_alpha()
day_1layer = pg.transform.scale(day_1layer, (500,500))

day_2layer = pg.image.load("day_2layer.png").convert_alpha()
day_2layer = pg.transform.scale(day_2layer, (500,500))

night_1layer = pg.image.load("night_1layer.png").convert_alpha()
night_1layer = pg.transform.scale(night_1layer, (500,500))

night_2layer = pg.image.load("night_2layer.png").convert_alpha()
night_2layer = pg.transform.scale(night_2layer, (500,500))

#--------------
sun_battle = pg.image.load('sun.png').convert_alpha()
sun_battle = pg.transform.scale(sun_battle, (150, 150))


main_char = pg.image.load('main_char.png').convert_alpha()
main_char = pg.transform.scale(main_char, (150, 150))

main_char_left = pg.image.load('main_char_left.png').convert_alpha()
main_char_left = pg.transform.scale(main_char_left, (150, 150))

armor_for_mch = pg.image.load('armor_mc.png').convert_alpha()
armor_for_mch = pg.transform.scale(armor_for_mch, (240,240))

colonna_for_mch = pg.image.load('colonna_f_ar_mc.png').convert_alpha()
colonna_for_mch = pg.transform.scale(colonna_for_mch, (130,130))

pet_mch_left = pg.image.load('down_pet_left.png').convert_alpha()
pet_mch_left = pg.transform.scale(pet_mch_left, (100,100))

pet_mch_right = pg.image.load('down_right_pet.png').convert_alpha()
pet_mch_right = pg.transform.scale(pet_mch_right, (100,100))


#-----------------------персонажи^^^

char_x_char = 1
char_y_char = 310


gravitation = 3

jump = 60


flagi = 0
sun_y_battle = 10
y_armor_char = 220

#180 для нижнего    

armor_x = 269
armor_y = 220

down_sun_y_flag = True
up_sun_y_flag = False

#
left_character_flag = False
right_character_flag = True

#день и ночь флаги
day_flag = True
night_flag = False


#Оружие вверх и вниз
armor_y_up_flag = False
armor_y_down_flag = False

#движение оружия вправо и влево
armor_x_left_flag = False
armor_x_right_flag = True

f_down_right = False
f_down_left = False
f_up_right = True
f_up_left_ = False 



#-----------------------все остальное^^^

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
        down_sun_y_flag=True
        up_sun_y_flag = False
    elif sun_y_battle>265:
        up_sun_y_flag = True
        down_sun_y_flag = False
    

    #смена дня и ночи(движения солнца)
    if down_sun_y_flag:
        sun_y_battle+=0.5
    elif up_sun_y_flag:
        sun_y_battle-=0.5

    if 11<sun_y_battle<100:
        day_flag = True
        night_flag = False
    elif 100<=sun_y_battle<=265:
        night_flag = True
        day_flag = False

    if night_flag == False and day_flag == True:
        screen.blit(day_2layer,(0,0))
    elif night_flag == True and day_flag == False:
        screen.blit(night_2layer,(0,0))

    screen.blit(sun_battle,(300,sun_y_battle))
    
    if night_flag == False and day_flag == True:
        screen.blit(day_1layer,(0,0))
    elif night_flag == True and day_flag == False:
        screen.blit(night_1layer,(0,0))
    

    left_character_flag = False
    right_character_flag = False 


    #управление персонажа
    pk = pg.key.get_pressed()

    #низ или верх (флаги)


#------------------------------
    if pk[pg.K_DOWN] and pk[pg.K_RIGHT]:
        f_down_right = True
        f_down_left = False
        f_up_right = False
        f_up_left_ = False 
        char_x_char+=2



    elif pk[pg.K_DOWN] and pk[pg.K_LEFT]:
        f_down_right = False
        f_down_left = True
        f_up_right = False
        f_up_left_ = False
        char_x_char-=2

    elif pk[pg.K_LEFT]:
        f_down_right = False
        f_down_left = False
        f_up_right = False
        f_up_left_ = True
        char_x_char-=2

    elif pk[pg.K_RIGHT]:
        f_down_right = False
        f_down_left = False
        f_up_right = True
        f_up_left_ = False 
        char_x_char+=2


#-----------------------------------

    #стенки против персонажа
    if char_x_char<=-29:
            char_x_char=-30
    elif char_x_char>=401:
            char_x_char=400


    if f_up_right == True or f_up_left_ == True:
        if char_x_char>=235:
            char_x_char = 235


    if f_up_right == True:
        screen.blit(main_char,(char_x_char,char_y_char))

    elif f_up_left_ == True:
        screen.blit(main_char_left,(char_x_char,char_y_char))
    
    elif f_down_left == True:
        screen.blit(pet_mch_left,(char_x_char,char_y_char+6))

    elif f_down_right == True:
        screen.blit(pet_mch_right,(char_x_char,char_y_char))



    #движения оружия 
    #движения вправо и влево
    if armor_x_right_flag == False and armor_x_left_flag == False:
        armor_x-=1 
    
    elif armor_x<=260:
        armor_x_right_flag = True
        armor_x_left_flag = False
    elif armor_x>=278:
        armor_x_left_flag = True
        armor_x_right_flag = False

    if armor_x_right_flag == True:
        armor_x+=1
    elif armor_x_left_flag == True:
        armor_x-=1

    #-------------------------------

    #движения вверх и вниз    
    if armor_y>=220:
        armor_y_up_flag = True
        armor_y_down_flag = False
    
    elif armor_y<=180: 
        armor_y_down_flag = True 
        armor_y_up_flag = False
    

    if armor_y_down_flag == False and armor_y_up_flag == False:
        armor_y-=1
    elif armor_y_up_flag == True:
        armor_y-=1
    elif armor_y_down_flag == True:
        armor_y+=1

    
    

    screen.blit(armor_for_mch,(armor_x,armor_y))


    screen.blit(colonna_for_mch,(320, 325))
    print(char_x_char)
    
    # обновление экрана
    pg.display.flip()         

# Quit pygame
pg.quit()