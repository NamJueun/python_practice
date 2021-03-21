# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# [게임 이미지]
# 1. 배경: 640 * 480 (세로, 가로) - background.png
# 2. 캐릭터: 70 * 70 - character.png
# 3. 똥: 70 * 70 - enemy.png

import pygame
import random

# 기본 초기화

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경화면, 캐릭터, 똥, 속도)

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\namju\\Desktop\\python\\python_practice\\pygame_basic\\quiz\\background.png")

# 캐릭터
char = pygame.image.load("C:\\Users\\namju\\Desktop\\python\\python_practice\\pygame_basic\\quiz\\\character.png")
char_size = char.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x_pos = (screen_width / 2) - (char_width / 2)
char_y_pos = screen_height - char_height

# 똥
poop = pygame.image.load("C:\\Users\\namju\\Desktop\\python\\python_practice\\pygame_basic\\quiz\\\똥.png")
poop_size = poop.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = 0 
poop_y_pos = 0

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도 
char_speed = 0.2
poop_speed = 5

running = True


while running:
    dt = clock.tick(30)

# 2. 이벤트 처리 (키보드, 마우스 등 )
    for event in pygame.event.get():          
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= char_speed 
            elif event.key == pygame.K_RIGHT:
                to_x += char_speed

        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                to_x = 0

    char_x_pos += to_x * dt

    # 가로 경계값 처리
    if char_x_pos < 0:
        char_x_pos = 0
    elif char_x_pos > screen_width - char_width:
        char_x_pos = screen_width - char_width

    poop_y_pos += poop_speed
    random.randint(0, (screen_width - poop_width))
    ## 충돌체크
    char_rect = char.get_rect()
    char_rect.left = char_x_pos
    char_rect.top = char_y_pos

    poop_rect = poop.get_rect()
    poop_rect.left = poop_x_pos
    poop_rect.top = poop_y_pos
      
    if char_rect.colliderect(poop_rect):
        print("충돌")
        running = False
     
    screen.blit(background,(0,0))
    screen.blit(char, (char_x_pos, char_y_pos))
    screen.blit(poop, (poop_x_pos, poop_y_pos))

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
