import reba
import monster
import random

def start_game():
    my_gold = 0
    my_mana = 0
    print("게임을 시작하겠습니다\n")
    cn = 0

    while True:
        print(f"현재 골드: {my_gold}\n")
        print(f"현재 마나량: {my_mana}\n")
        monster_battle = create_monster(cn)

        a = input("레바유닛을 생성하시겠습니까? (예, 아니오)\n")
        if a == "예":
            r1, my_gold,my_mana = create_unit(my_gold)
            cn += 1
            if battle(r1, monster_battle,my_mana):
                my_gold += 10
                my_mana += 20
                print(f"현재 골드: {my_gold}\n")
                print(f"현재 마나량: {my_mana}\n")
        elif a == "아니오":
            print("생성한 객체가 없어서 넥서스가 파괴되었습니다\n")
            break

        if not continue_game():
            break



def create_monster(cn):
    p_monster_random = random.randint(1, 11)
    chan_monster_random = random.randint(1,11)
    if cn == 5:
        print("앗 강화된 야생의 몬스터가 생성되었습니다!(p진화)\n")
        if p_monster_random == 1 or p_monster_random == 3 or p_monster_random == 5:
            monster_p_unit = monster.monster_p()
            return monster_p_unit
        else:
            print("앗 강화된 야생의 몬스터가 생성되었습니다!(1진화)\n")
            monster_p_unit = monster.monster_1()
            return monster_p_unit
    elif cn == 7:
        print("아.... 야생의 찬순이 냉장고가 생성되었습니다!")
        if chan_monster_random <=7:
            monster_chan_unit = monster.monster_chan()
            return monster_chan_unit
        else: 
            print("앗 강회된 야생의 몬스터가 생성되었습니다")
            monster_p_unit = monster.monster_p()
            return monster_p_unit
    
    else:
        print("앗 야생의 몬스터가 생성되었습니다!(0진화)\n")
        monster_unit = monster.monster_0()
        return monster_unit



def create_unit(gold):
    if gold < 30:
        r1 = reba.basic_reba()
        mana = 0
        return r1 ,gold, mana
    elif gold >= 30:
        print("확률형 기반 강화를 진행 시킬 수 있습니다.\n 기회는 총 세 번 주어집니다\n 다음 강화 유닛: 레인저\n")
        print("!!!성공 확률: 70 %!!!\n")
        choice_update = input(f"현재 골드가 30골드 이상이 모여있습니다.\n 강화할 경우 내 골드:{gold - 30} \n 강화를 진행 하겠습니까? (예, 아니오)\n")

        if choice_update == "예":
            count = 1
            gold-= 30
            while count < 4:
                possible = random.randint(1, 11)
                if possible <= 3:
                    print("강화 실패!\n")
                    count += 1
                else:
                    print("강화 성공!\n")
                    r1 = reba.ranger()
                    mana = 0
                    return r1, gold , mana
            print("강화 실패의 고통을 느껴라~~!\n")
            mana = 0
            return r1 ,gold , mana
        elif choice_update == "아니오":
                print("기본 유닛을 사용합니다.\n")
                
                return r1, gold, mana
        else:
                print("올바른 입력이 아닙니다.\n")
                return create_unit(gold)
    
    elif gold >= 50:
        print("확률형 기반 강화를 진행 시킬 수 있습니다.\n 기회는 총 다섯 번 주어집니다\n 다음 강화 유닛: 스핏파이어 or 웨폰마스터\n") 
        print("!!!성공 확률 : 50 % !!!")
        choice_update = input(f"현재 골드가 50골드 이상이 모있습니다.\n 강화할 경우 내 골드: {gold - 50}\n 강화를 진행하겠습니까? (예, 아니오)\n")
        
        if choice_update == "예":
            count = 1
            gold-= 50
            while count < 6:
                possible = random.randint(1, 11)
                if possible <= 5:
                    print("강화 실패!\n")
                    count += 1
                else:
                    print("강화 성공!\n")
                    choice_reba = input("두 가지 중 하나로 선택 할 수 있습니다.\n - 번호를 선택하세요 (1.버서커[딜러] , 2.스핏파이어[탱커])\n")
                    if choice_reba == "1":
                        r1 = reba.berserker()
                        mana = 0
                        return r1, gold , mana
                    elif choice_reba == "2":
                        r1 = reba.spitfire()
                        mana = 0
                        return r1, gold , mana
                        
            print("강화 실패의 고통을 느껴라~~!\n")
            mana = 0
            return r1,gold , mana
        elif choice_update == "아니오":
                print("기본 유닛을 사용합니다.\n")
                return r1 ,gold , mana
        else:
                print("올바른 입력이 아닙니다.\n")
                return create_unit(gold)
    
    elif gold >= 100:
        print("확률형 기반 강화를 진행 시킬 수 있습니다.\n 기회는 총 세 번 주어집니다\n 다음 강화 유닛: 웨편마스터\n")
        print("!!!성공 확률: 30 %!!!\n")
        choice_update = input(f"현재 골드가 100골드 이상이 모여있습니다.\n 강화할 경우 내 골드:{gold - 100} \n 강화를 진행 하겠습니까? (예, 아니오)\n")

        if choice_update == "예":
            count = 1
            gold-= 100
            while count < 4:
                possible = random.randint(1, 11)
                if possible <= 7:
                    print("강화 실패!\n")
                    count += 1
                else:
                    print("강화 성공!\n")
                    r1 = reba.ranger()
                    return r1, gold
            print("강화 실패의 고통을 느껴라~~!\n")
            
            return r1 ,gold 
        elif choice_update == "아니오":
                print("기본 유닛을 사용합니다.\n")
                
                return r1, gold
        else:
                print("올바른 입력이 아닙니다.\n")
                return create_unit(gold)
    
    
#스핏파이어 궁 넣어


def battle(r1, monster_unit, my_mana):
    while r1.hp > 0 and monster_unit.hp > 0:
        attack1 = input("상대방을 공격하시겠습니까? (q(공격키), t(마나회복),r(궁키))\n")
        if attack1 == "q":

            rand_attack = random.randint(0, 4)
            if rand_attack < 2:
                r1.attack(monster_unit.name)
                monster_unit.damaged(r1.name, r1.damage)
                if monster_unit.hp <= 0:
                    print("몬스터를 처치했습니다!\n")
                    return True
                monster_unit.attack(r1.name)
                r1.damaged(monster_unit.name, monster_unit.damage)
                if r1.hp <= 0:
                    print("레바 유닛이 죽었습니다.\n")
                    return False
            else:
                print("공격 실패\n")
                monster_unit.attack(r1.name)
                r1.damaged(monster_unit.name, monster_unit.damage)
                if r1.hp <= 0:
                    print("레바 유닛이 죽었습니다.\n")
                    return False
        elif attack1 == "t":
            my_mana += 30
            print("이번 턴은 마나 회복에 집중합니다. [마나 회복량: 30].\n")
            print(f"현재 마나량 {my_mana}\n")
            monster_unit.attack(r1.name)
            r1.damaged(monster_unit.name, monster_unit.damage)
            if r1.hp <= 0:
                print("레바 유닛이 죽었습니다.\n")
                return False
        elif attack1 == "r": #r1.name 을 사용해서 구분 할 수 있도록 변경
            
            if r1.name == "버서커":
                 if my_mana >=70: 
                        my_mana -= 70
                        r1.berserker_R(monster_unit.name)
                        if 20 <= r1.absorb <= 70 and r1.hp > r1.absorb:
                           r1.hp -= r1.absorb
                           monster_unit.damaged(r1.name , r1.absorb + r1.damage)
                           if monster_unit.hp <= 0:
                            print("몬스터를 처치했습니다!\n")
                            return True
                        monster_unit.attack(r1.name)
                        r1.damaged(monster_unit.name, monster_unit.damage)
                        if r1.hp <= 0:
                            print("레바 유닛이 죽었습니다.\n")
                            return False
                        else:
                             print("아무 일도 일어나지 않았습니다!")
            elif r1.name == "레인저":
                if my_mana >= 40:
                        my_mana -= 40
                        r1.ranger_R(monster_unit.name)
                        monster_unit.damaged(r1.name , 20*r1.x)
                        print(f"현재 마나량 : {my_mana}\n")
                        if monster_unit.hp <= 0:
                            print("몬스터를 처치했습니다!\n")
                            return True
                        monster_unit.attack(r1.name)
                        r1.damaged(monster_unit.name, monster_unit.damage)
                        if r1.hp <= 0:
                            print("레바 유닛이 죽었습니다.\n")
                            return False
                else:
                     print(f"현재 마나량이 {my_mana - r1.mana} 부족합니다 [현재 마나량: {my_mana}]\n")        
                 
            elif r1.name == "레바유닛": 
                if my_mana >= 25:
                        my_mana-= 25
                        r1.basic_reba_R(monster_unit.name)
                        monster_unit.damaged(r1.name , 10 * 3 )
                        print(f"현재 마나량: {my_mana}\n")
                        if monster_unit.hp <= 0:
                            print("몬스터를 처치했습니다!\n")
                            return True
                        monster_unit.attack(r1.name)
                        r1.damaged(monster_unit.name, monster_unit.damage)
                        if r1.hp <= 0:
                            print("레바 유닛이 죽었습니다.\n")
                            return False
                else:
                    print(f"현재 마나량이 {my_mana - r1.mana} 부족합니다 [현재 마나량: {my_mana}]\n")
            else: 
                print("누구야 너\n")

            
        else:
            print("제대로 입력해주세요\n")
    return r1.hp > 0



def continue_game():
    quit_game = input("게임을 종료하시려면 1을 누르세요 (계속하시려면 2번을 누르세요)\n")
    if quit_game == "1":
        return False
    elif quit_game == "2":
        return True
    else:
        print("1 또는 2로 입력해주세요.\n")
        return continue_game()


if input("게임을 시작하려면 0을 입력해주세요: \n") == "0":
    start_game()