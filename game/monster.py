import random




class monster_0: 
    def __init__(self, name = "0진화 몬스터" , hp = 30 , damage = 10): 
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name}: 생성되었습니다. [체력: {self.hp} , 공격력: {self.damage}]")
    
    def attack(self,name): 
        print(f"{self.name}: {name} 공격합니다 [공격력 {self.damage}]")

    def damaged(self,name,damage):
        self.hp = self.hp - damage
        print(f"{self.name}: {name}에 의해 {damage} 만큼의 공격력을 받았습니다")
        if self.hp <=0: 
            print(f"{self.name}: {name}에 의해 처형되었습니다")
    
class monster_1:
    def __init__(self, name="1진화 몬스터", hp=50, damage=20):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name}: 생성되었습니다. [체력: {self.hp} , 공격력: {self.damage}]")

    def attack(self, name):
        print(f"{self.name}: {name} 공격합니다 [공격력 {self.damage}]")

    def damaged(self, name, damage):
        self.hp = self.hp - damage
        print(f"{self.name}: {name}에 의해 {damage} 만큼의 공격력을 받았습니다")
        if self.hp <= 0:
            print(f"{self.name}: {name}에 의해 처형되었습니다")

class monster_p(monster_0):
    def __init__(self):
        super().__init__(name="Big_dick(1진화 몬스터)", hp=120, damage=20)
        print(f"[{self.name}] 강화되었어요. 쌈뽕할련아 ㅋ")


class monster_chan(monster_0): 
    def __init__(self): 
        super(). __init__(name = "찬순이 냉장고(1보스)" , hp = 140, damage = random.randint(20, 50) )
        print("보스몹 찬순이 냉장고가 나타났습니다. 이 몬스터가 3번 동안 공격을 성공할 시 스킬 공격을 가할 수 있습니다")
    
    
    def attack(self,name): 
        count = 1
        if count<=5:
            print(f"{self.name}: {name} 공격합니다. [공격횟수 {count}],{self.damage}")
            count +=1
        else:
            print(f"스킬 공격[나의 트월킹을 늦껴라~~!]: 가 발동 됩니다 [공격력: {self.damage *2}]")
            count = 0



