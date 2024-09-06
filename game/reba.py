import random
class basic_reba:
    def __init__(self, name="레바유닛", hp=30, damage=10, mana = 25, gold=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.mana = mana
        self.gold = gold
        print(f"{self.name}: 생성되었습니다")
        print(f"[{self.name}] 체력: {self.hp}, 공격력: {self.damage}, 마나소모량: {self.mana}")

    def attack(self, name):
        print(f"{self.name}: {name} 공격합니다 [공격력 {self.damage}]")

    def damaged(self, name, damage):
        self.hp -= damage
        print(f"{self.name}: {name}에 의해 {damage} 만큼의 공격을 받았습니다")
        if self.hp <= 0:
            print(f"{self.name}: {name}에 의해 처형되었습니다")

    def basic_reba_R(self, name):
        print(f"{self.name}: 딜버프 - 공격력을 3배 강화하여 공격합니다. [마나량: {self.mana} 소모]")
        print(f"{self.name}: {name} 공격합니다 [공격력 {self.damage * 3}]")
        
        


class ranger(basic_reba):
    def __init__(self):
        self.x = random.randint(3, 6)
        super().__init__(name="레인저", hp=60, damage=20, mana=40)
        print(f"[{self.name}] 으로 강화되었습니다.")

    def ranger_R(self, name):
        print(f"{self.name}: [석양이 진다.......] - 공격력을 {self.x}배 강화하여 공격합니다. [마나량: {self.mana} 소모]")
        print(f"{self.name}: {name} 공격합니다 [공격력 {self.damage * self.x}]")





# 선택 가능 버서커 or 스핏파이어 
class weapon_master(basic_reba):
    def __init__(self):
        self.y = random.randint(2,5)
        self.z = random.randint(10,30)
        super().__init__(name = "웨폰마스터" ,  hp =100  , damage = 50 , mana = 50)
        print(f"[{self.name}] 으로 강화되었습니다")
    
    def weapon_monster_R(self, name):
        print(f"{self.name}: [나의 검을 느껴라....] - {self.y} 만큼 연속적으로 {self.z}의 피해를 줍니다. [마나량: {self.name} 소모]")
        print(f"{self.name}: {name} 공격합니다 [공격력 {self.y * self.z}] ")
        






class spitfire(basic_reba):
    def __init__(self):
       super(). __init__(name = "스핏파이어" ,  hp = 100 , damage = 40 , mana = 70)
       print(f"[{self.name}] 으로 강화되었습니다")
    
    def spitfire_R(self, name):
        print(f"{self.name}:[나의 친구들을 소개해쥬지....boy] - 스핏파이어의 친구들이 당신을 돕습니다 {self.hp}: +20 , {self.damage}: + 10 만큼 올립니다")
        print(f"{self.name}: {name} 공격합니다 [공격력 {self.damage + 10}]")
       



class berserker(basic_reba):
    def __init__(self):
        super(). __init__(name = "버서커" , hp = 80 , damage = 60 , mana = 70 )
        print(f"[{self.name}] 으로 강화되었습니다")

    def berserker_R(self,name):
        print(f"{self.name}: [나의 고통, 한껏 꽃피우리라!] - 버서커가 자신의 hp를 소모한 만큼 자신의 데미지를 올립니다")
        self.absorb = input("소모할 hp를 입력해주세요 [20 ~ 70]")
        if 20 <= self.absorb <= 70 and self.hp > self. absorb:
            print(f"{self.name}: {name}  공격합니다 [공격력 {self.absorb + self.damage}] ")
        else:
            print(f"피흡 설정량을 초과하였거나 , hp 가 부족합니다. 현재 hp: {self.hp}")

        