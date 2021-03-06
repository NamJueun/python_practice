# collision: 충돌 처리

import pygame
from pygame.constants import K_LEFT

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")  # 게인 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기 (움직이지 않음)
background = pygame.image.load(
    "C:\\Users\\namju\\Desktop\\python\\python_practice\\pygame_basic\\background.png")

# 캐릭터 (스프라이트) 불러오기 (움직임)
character = pygame.image.load(
    "C:\\Users\\namju\\Desktop\\python\\python_practice\\pygame_basic\\character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터 가로 크기
character_height = character_size[1]  # 캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width /
                                        2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
# 화면 세로크기 가장 아래에 해당하는 곳에 위치 (세로)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
character_speed = 0.6

# 적 enemy 캐릭터 생성

enemy = pygame.image.load(
    "C:\\Users\\namju\\Desktop\\python\\python_practice\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]  # 캐릭터 가로 크기
enemy_height = enemy_size[1]  # 캐릭터 세로 크기
# 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
# 화면 세로크기 가장 아래에 해당하는 곳에 위치 (세로)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)


# 이벤트 루프 : 종료되지 않도록 대기
running = True  # 게임이 진행중인가 확인
while running:  # True니까 계속 돔
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정, dt -> delta
    #print("fps: " + str(clock.get_fps()))
    #캐릭터가 1초 동안 100 만큼 이동을 해야함
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동해야하나 ? 10만큼. 10 * 10 = 100
    # 20 fps : 1초 동안에 20번 동작 -> 1번에 몇 만큼 이동해야하나 ? 20만큼. 20 * 5 = 100

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가.
            running = False  # 게임 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키보드 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed  # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.type == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                to_x = 0
            elif event.type == pygame.K_UP or event.type == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:  # 화면 벗어나면
        character_x_pos = 0  # 왼쪽 끝에 둠
    elif character_x_pos > screen_width - character_width:  # 화면크기 보다 커지면
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()  # 캐릭터의 rect 정보 업데이트
    character_rect.left = character_x_pos  # 왼쪽
    character_rect.top = character_y_pos  # 위쪽

    enemy_rect = enemy.get_rect()  # 캐릭터의 rect 정보 업데이트
    enemy_rect.left = enemy_x_pos  # 왼쪽
    enemy_rect.top = enemy_y_pos  # 위쪽

    # 충돌 체크
    if character_rect.colliderect(enemy_rect): # 충돌 여부 확인하는 함수 
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

    pygame.display.update()  # 게임 화면을 다시 그리기 (반드시)

# pygame 종료
pygame.quit()
