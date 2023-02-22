import pygame

def loading_screen():
    FPS = 3
    #Инициализируем PyGame
    pygame.init()

    #loading

    #название окна
    pygame.display.set_caption('SnakeSpeare')


    #инициализируем экран
    screen = pygame.display.set_mode((500, 500))

    #---------------------------loading----------------------

    loading1 = pygame.image.load('load1.png').convert_alpha()
    loading1 = pygame.transform.scale(loading1, (500, 500))
    loading1_flag = True


    loading2 = pygame.image.load('load2.png').convert_alpha()
    loading2 = pygame.transform.scale(loading2, (500, 500))
    loading2_flag = False

    loading3 = pygame.image.load('load3.png').convert_alpha()
    loading3 = pygame.transform.scale(loading3, (500, 500))
    loading3_flag = False

    loading4 = pygame.image.load('load4.png').convert_alpha()
    loading4 = pygame.transform.scale(loading4, (500, 500))
    loading4_flag = False
    #-------------------------------------------------------





    # базовый цикл
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        if loading1_flag == True:
            loading1_flag=False
            loading2_flag=True
        elif loading2_flag == True:
            loading2_flag=False
            loading3_flag=True
        elif loading3_flag == True:
            loading3_flag = False
            loading4_flag = True
        elif loading4_flag == True:
            loading4_flag = False
            loading1_flag = True
        
        if loading1_flag == True:
            screen.blit(loading1,(0,0))
            
        elif loading2_flag == True:
            screen.blit(loading2, (0,0))
        elif loading3_flag == True:
            screen.blit(loading3, (0,0))  
        elif loading4_flag == True:
            screen.blit(loading4, (0,0))     


        # обновление экрана
        pygame.display.update()


    # Quit pygame
    pygame.quit()


loading_screen()