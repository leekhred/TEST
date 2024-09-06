import pygame
import random
from reba import basic_reba, ranger
from monster import monster_0, monster_1, monster_p

# Pygame 초기화
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reba vs Monster")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 한글 폰트 설정
font = pygame.font.SysFont("Malgun Gothic", 20)
# 텍스트 박스 렌더링 함수

def draw_text(text, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def draw_textbox(text, x, y, width, height):
    pygame.draw.rect(screen, white, (x, y, width, height))
    pygame.draw.rect(screen, black, (x, y, width, height), 2)
    lines = text.split('\n')
    line_height = font.size('Tg')[1]
    for i, line in enumerate(lines):
        draw_text(line, black, x + 10, y + 10 + i * line_height)
    pygame.display.update()
# 몬스터 생성 함수
def create_monster(cn):
    p_monster_random = random.randint(1, 11)
    if cn == 5:
        if p_monster_random in [1, 3, 5]:
            monster_p_unit = monster_p()
            return monster_p_unit
        else:
            monster_1_unit = monster_1()
            return monster_1_unit
    else:
        monster_0_unit = monster_0()
        return monster_0_unit

# 유닛 생성 함수
def create_unit(gold):
    if gold < 30:
        draw_textbox("골드가 부족하여 기본 유닛을 생성합니다.", 50, 300, 700, 100)
        pygame.time.wait(2000)
        return basic_reba()
    else:
        draw_textbox("확률형 기반 강화를 진행합니다. 기회는 총 세 번 주어집니다.", 50, 300, 700, 100)
        pygame.time.wait(3000)
        count = 0
        while count < 3:
            possible = random.randint(1, 11)
            if possible > 3:
                draw_textbox("강화 성공! 강화된 유닛을 생성합니다.", 50, 300, 700, 100)
                pygame.time.wait(2000)
                return ranger()
            else:
                count += 1
                draw_textbox(f"강화 실패! 남은 기회: {3 - count}", 50, 300, 700, 100)
                pygame.time.wait(2000)
        draw_textbox("강화 실패! 기본 유닛을 생성합니다.", 50, 300, 700, 100)
        pygame.time.wait(2000)
        return basic_reba()

# 배틀 함수
def battle(player, monster_unit):
    player_turn = True
    while player.hp > 0 and monster_unit.hp > 0:
        screen.fill(black)
        draw_textbox(
            f"플레이어: {player.name}\nHP: {player.hp}\n\n몬스터: {monster_unit.name}\nHP: {monster_unit.hp}",
            50, 50, 700, 200
        )

        if player_turn:
            draw_textbox("당신의 턴입니다! (A)공격 (S)스킬", 50, 300, 700, 100)
            pygame.display.update()

            action = None
            while action is None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            action = 'attack'
                        elif event.key == pygame.K_s:
                            action = 'skill'

            if action == 'attack':
                rand_attack = random.randint(0, 4)
                if rand_attack < 2:  # 공격 성공
                    player.attack(monster_unit.name)
                    monster_unit.damaged(player.name, player.damage)
                    draw_textbox(
                        f"{monster_unit.name}: {player.name}에 의해 {player.damage} 만큼의 공격을 받았습니다!",
                        50, 300, 700, 100
                    )
                else:  # 공격 실패
                    draw_textbox("공격이 실패했습니다!", 50, 300, 700, 100)
            elif action == 'skill':
                player.reba_R(monster_unit.name)
                monster_unit.damaged(player.name, player.damage * 3)
                draw_textbox(
                    f"{monster_unit.name}: {player.name}에 의해 {player.damage * 3} 만큼의 공격을 받았습니다!",
                    50, 300, 700, 100
                )
            player_turn = False
        else:
            monster_unit.attack(player.name)
            player.damaged(monster_unit.name, monster_unit.damage)
            draw_textbox(
                f"{player.name}: {monster_unit.name}에 의해 {monster_unit.damage} 만큼의 공격을 받았습니다!",
                50, 300, 700, 100
            )
            player_turn = True

        pygame.display.update()
        pygame.time.wait(2000)  # 대화창이 일정 시간 동안 표시되도록 대기

        if player.hp <= 0:
            draw_textbox("게임 오버! 당신이 패배했습니다.", 50, 300, 700, 100)
            pygame.display.update()
            pygame.time.wait(2000)
            return False

        if monster_unit.hp <= 0:
            draw_textbox("승리했습니다!", 50, 300, 700, 100)
            pygame.display.update()
            pygame.time.wait(2000)
            return True

        pygame.display.update()

    return player.hp > 0

# 메인 게임 루프
def game_loop():
    clock = pygame.time.Clock()
    my_gold = 0
    cn = 0
    running = True

    while running:
        screen.fill(black)
        draw_textbox(f"현재 골드: {my_gold}", 50, 50, 700, 100)
        pygame.display.update()

        monster_unit = create_monster(cn)
        draw_textbox("레바유닛을 생성하시겠습니까? (Y/N)", 50, 300, 700, 100)
        pygame.display.update()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_input = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        player_unit = create_unit(my_gold)
                        cn += 1
                        if battle(player_unit, monster_unit):
                            my_gold += 10
                        waiting_for_input = False
                    elif event.key == pygame.K_n:
                        draw_textbox("넥서스가 파괴되었습니다. 게임 종료.", 50, 300, 700, 100)
                        pygame.display.update()
                        pygame.time.wait(2000)
                        running = False
                        waiting_for_input = False

        if not running:
            break

        draw_textbox("게임을 계속하시겠습니까? (Y/N)", 50, 300, 540, 100)
        pygame.display.update()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_input = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        waiting_for_input = False
                    elif event.key == pygame.K_n:
                        running = False
                        waiting_for_input = False

    pygame.quit()

# 메인 실행
if __name__ == "__main__":
    game_loop()