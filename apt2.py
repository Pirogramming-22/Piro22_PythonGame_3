import random
import time

'''class Player:
    def __init__(self, name, drinking_capacity, computer_flag, game_starter):
        self.name = name
        self.drinking_capacity = drinking_capacity
        self.drinks = 0
        self.computer_flag = computer_flag
        self.game_starter = game_starter 

def show_drinks_status(players):
    for p in players:
        print(f"{p.name}은(는) 지금까지 {p.drinks}🍺! 치사량까지 {p.drinking_capacity - p.drinks}")
    print()'''

def apt(players):
    print("\n🏡 아파트~아파트~아파트~ (feat.APT) 🏡\n")

    # 모든 참여자 손 리스트
    hands = []
    for player in players:
        hands.append(f"{player.name}의 왼손 ✋")
        hands.append(f"{player.name}의 오른손 🤚")

    random.shuffle(hands)  # 손의 순서 섞기
    print("🧑‍🤞 모두 손 올려! 자, 아파트 게임을 시작합니다! 🧑‍🤞\n")

    while True:
        # 술래 선택
        current_leader = random.choice(players)
        print(f"🏆 이번 라운드의 술래는 {current_leader.name}입니다! 🎊\n")

        # 층수 선택 (손 개수 이하의 층수 선택)
        max_floors = len(hands)
        chosen_floor = random.randint(1, max_floors)
        print(f"📢몇층? {current_leader.name}: {chosen_floor}층!🚀 \n")
        time.sleep(1)

        # 층수 카운트 진행
        print("🤚 자자 손 움직이지 말고 가만히 있어!~~ 아래부터 층 세는중... 🤚\n")
        for i, hand in enumerate(hands):
            print(f"{i + 1}층: {hand} 🎶")
            time.sleep(0.5)

        # 선택된 층에 해당하는 손의 주인이 다음 술래로 결정
        new_leader_hand = hands[chosen_floor - 1]
        new_leader_name = new_leader_hand.split("의 ")[0]  # 손 주인
        new_leader = next(player for player in players if player.name == new_leader_name)

        # 술 마시기
        print(f"\n❓ {chosen_floor}층 누구야?!! 🕵️‍♂️")
        print(f"👇 {chosen_floor}층의 손은 {new_leader_hand}입니다! 🖐️")
        print(f"🍺 누가 술을 마셔~ {new_leader_name}이가 마셔! 원~샷! 🍻🍻🍻\n")
        new_leader.drinks += 1
        time.sleep(1)

        # 현재 상태 출력
        #show_drinks_status(players)
        return players 
        # 치사량 도달 여부 확인
        '''if new_leader.drinks >= new_leader.drinking_capacity:
            print(f"\n💔 {new_leader.name}이(가) 치사량에 도달했습니다! 게임 종료! 💔")
            break'''

# 테스트용:
'''if __name__ == "__main__":
    players = [
        Player("건욱", random.choice([2, 4, 6, 8, 10]), True, False),
        Player("예원", random.choice([2, 4, 6, 8, 10]), True, False),
        Player("태린", random.choice([2, 4, 6, 8, 10]), True, False),
        Player("현진", random.choice([2, 4, 6, 8, 10]), True, False),
        Player("유지", random.choice([2, 4, 6, 8, 10]), True, False)
    ]

    apt(players)'''
