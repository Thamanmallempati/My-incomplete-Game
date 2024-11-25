import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()

size = pygame.display.Info()
x = size.current_w
y = size.current_h -50

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Simple Buttons")

WHITE = (255, 255, 255)
GRAY = (170, 170, 170)

font = pygame.font.Font(None, 40)

def text(context,colour,xpos,ypos):
    msg = font.render(context,True,colour)
    screen.blit(msg,(xpos,ypos))

# play_btn = pygame.image.load("download__2_-removebg-preview.png")
bc_image = pygame.image.load("download (3).jpg")
bc_image = pygame.transform.scale(bc_image,(x,y))
op_image = pygame.image.load("game-buttons-wood-stone-gamer-interface_107791-10116.jpg")

op_x = 1830
op_y = 10

op_rect = op_image.get_rect(topright=(op_x,op_y))

def game():
    running = True
    play = False
    sett = False

    while running:
        while play:
            # Assets
            Road = pygame.image.load("Pista.jpg")
            Road = pygame.transform.scale(Road, (x, y))

            font_style = pygame.font.SysFont(None, 30)

            def message(msg, color):
                msg = font_style.render(msg, True, color)
                screen.blit(msg, (x / 4, y / 2.1))

            def score(msg, colour):
                msg = font_style.render("Score:" + str(msg), True, colour)
                screen.blit(msg, (10, 10))

            car_w, car_h = 200, 200
            car_speed = 10

            White = (255, 255, 255)
            Red = (255, 0, 0)

            maincar = pygame.image.load("car_6-removebg-preview.png")
            maincar = pygame.transform.scale(maincar, (car_w, car_h))
            car1 = pygame.image.load("car_1-removebg-preview.png")
            car1 = pygame.transform.scale(car1, (car_w, car_h))
            car2 = pygame.image.load("car_2-removebg-preview.png")
            car2 = pygame.transform.scale(car2, (car_w, car_h))
            car3 = pygame.image.load("car_3-removebg-preview.png")
            car3 = pygame.transform.scale(car3, (car_w, car_h))
            car4 = pygame.image.load("car_4-removebg-preview.png")
            car4 = pygame.transform.scale(car4, (car_w, car_h))
            car5 = pygame.image.load("car_5-removebg-preview.png")
            car5 = pygame.transform.scale(car5, (car_w, car_h))

            cars = []

            def mul_cars():
                while True:
                    car_type = random.choice([car1, car2, car3, car4])
                    car_x = random.randint(0, x - car_w)
                    car_y = -60
                    overlap = False
                    for car in cars:
                        if (car_x in range(car['x'] - car_w, car['x'] + car_w) and
                                car_y in range(car['y'] - car_h, car['y'] + car_h)):
                            overlap = True
                            break
                    if not overlap:
                        return {'type': car_type, 'x': car_x, 'y': car_y}

            red = (255, 0, 0)

            def game():
                Score = 0
                maincar_w, maincar_h = 200, 200
                maincar_x = (x - maincar_w) // 2
                maincar_y = y - maincar_h - 10
                maincar_s = 20

                bg_y1 = 0
                bg_y2 = -y

                game_close = False
                game_running = True

                while game_running:
                    while game_close == True:
                        screen.fill(White)
                        message("You lost! Press Q to quit and P to play again", Red)
                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                    pygame.quit()
                                if event.key == pygame.K_p:
                                    game_running = True

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                maincar_x -= maincar_s
                            if event.key == pygame.K_RIGHT:
                                maincar_x += maincar_s
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            if op_rect.collidepoint(mouse_x, mouse_y):
                                running = True
                                play = False

                    # creation of new cars
                    if random.random() < 0.015:
                        cars.append(mul_cars())

                    for car in cars:
                        car['y'] += car_speed

                        if car['y'] > y:
                            cars.remove(car)
                            Score += 1

                    bg_y1 += 0.5
                    bg_y2 += 0.5
                    if bg_y1 >= y:
                        bg_y1 = -y
                    if bg_y2 >= y:
                        bg_y2 = -y

                    screen.blit(Road, (0, bg_y1))
                    screen.blit(Road, (0, bg_y2))
                    screen.blit(op_image,(op_rect.topright))

                    screen.blit(maincar, (maincar_x, maincar_y))

                    for car in cars:
                        if car['type'] == car1:
                            screen.blit(car1, (car['x'], car['y']))
                        if car['type'] == car2:
                            screen.blit(car2, (car['x'], car['y']))
                        if car['type'] == car3:
                            screen.blit(car3, (car['x'], car['y']))
                        if car['type'] == car4:
                            screen.blit(car4, (car['x'], car['y']))
                        if car['type'] == car5:
                            screen.blit(car5, (car['x'], car['y']))

                    maincar_rect = pygame.Rect(maincar_x, maincar_y, car_w, car_h)
                    for car in cars:
                        car_rect = pygame.Rect(car['x'], car['y'], car_w, car_h)
                        if maincar_rect.colliderect(car_rect):
                            game_close = True

                    score(Score, Red)

                    pygame.display.update()
                    clock.tick(30)

            game()

        while sett:
            screen.fill(GRAY)
            pygame.display.update()


        # while home:
        screen.blit(bc_image,(0,0))

        play_btn = pygame.Rect(300,250,150,50)
        set_btn = pygame.Rect(300,350,150,50)
        # screen.blit(play_btn,(250,200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if play_btn.collidepoint(mouse_x,mouse_y):
                    play = True
                if set_btn.collidepoint(mouse_x,mouse_y):
                    sett =True

            pygame.draw.rect(screen,WHITE,play_btn,5)
            pygame.draw.rect(screen,WHITE,set_btn,5)
            text("Play",WHITE,347,260)
            text("Settings",WHITE,320,360)

            pygame.display.flip()

game()