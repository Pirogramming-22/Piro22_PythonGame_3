from game007 import Player, gonggongchilbbang
from guessing_number import Player, multiplayer_guess_game
import random

drinking_capacity = [2, 4, 6, 8, 10]

main_character = input("오늘 거하게 취해볼 당신의 이름은? : ")
main_player = [Player(main_character, random.choice(drinking_capacity), False)] 

number_of_player = int(input("함께 취할 친구들은 얼마나 필요하신가요? (사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : "))

player_list = [
    Player("건욱", random.choice(drinking_capacity), True),
    Player("예원", random.choice(drinking_capacity), True),
    Player("태린", random.choice(drinking_capacity), True),
    Player("현진", random.choice(drinking_capacity), True),
    Player("유지", random.choice(drinking_capacity), True)
]

main_player_filter = [p for p in player_list if p.name != main_character]

selected_player = random.sample(main_player_filter, number_of_player)

for player in selected_player:
    print(f"오늘 함께 취할 친구는 {player.name}입니다! (치사량 : {player.drinking_capacity})")

while True:
    # 종료 조건: 치사량 초과한 플레이어가 있을 경우 루프 종료
    if any(p.drinks >= p.drinking_capacity for p in main_player + selected_player):
        break

    # 게임 메뉴 표시
    print("\n🍺 ~~~ Alcohol GAME Menu ~~~ 🍺")
    print("1. 공공칠빵 게임")
    print("2. 숫자 맞추기 게임")
    print("exit. 게임 종료")
    choice = input("원하는 게임 번호를 선택하세요: ")

    if choice == '1':
        print("\n🍺 공공칠빵 게임을 시작합니다! 🍺")
        gonggongchilbbang(main_player + selected_player)
    elif choice == '2':
        print("\n🍺 숫자 맞추기 게임을 시작합니다! 🍺")
        multiplayer_guess_game(main_player + selected_player)
    elif choice.lower() == 'exit':
        print("\n🍺 게임을 종료합니다. 다음에 또 만나요! 🍺")
        break
    else:
        print("\n❌ 잘못된 입력입니다. 다시 선택해주세요! ❌")

# 게임 종료 후 플레이어 상태 확인
for player in main_player + selected_player:
    if player.drinks >= player.drinking_capacity:
        print("""
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
                ⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
                ⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
                ⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
                ⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
                ⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
                ⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
                ⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
                ⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
                ⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
                ⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
                ⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        """)
        print(f"\n{player.name}이(가) 전사했습니다... 꿈나라에서는 편히...ZZZ\n")
        print("🍺 다음에 술마시면 또 불러주세요~ 안녕! 🍺")
