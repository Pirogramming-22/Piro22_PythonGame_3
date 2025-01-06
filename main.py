import game007, guessing_number, subway, game369, apt2,random, re, random, time

class Player:
    def __init__(self, name, drinking_capacity, computer_flag = True, game_starter = False):
        self.name = name
        self.drinking_capacity = drinking_capacity
        self.drinks = 0
        self.computer_flag = computer_flag
        self.game_starter = game_starter

    ''''@classmethod
    def create_player(cls, name, drinking_capacity, computer_flag, game_starter):
        return cls(name, drinking_capacity, computer_flag, game_starter)'''

def start_game():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("ALCOHOL GAME")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("안주먹을 시간이 없어요~ 마시면서 배우는 술게임!")
    while True:
        play = input("게임을 진행할까요?(y/n): ")
        if play == "Y" or play == "y":
            break
#start logo 띄우는 함수
def input_user_name():
    user_name = input("📢오늘 씬나게 놀아볼 당신의 이름은?? >_O ")
    return user_name
#player 이름 입력 함수
def select_capacity(user):
        print("~~~~~~~~~~~~~~~🍻 소주 기준 당신의 주량은? 🍻~~~~~~~~~~~~~~~~")
        print("1. 소주 반병 (2잔)")
        print("2. 소주 반병에서 한병 (4잔)")
        print("3. 소주 한병에서 한병 반 (6잔)")
        print("4. 소주 한병 반에서 두병 (8잔)")
        print("5. 소주 두병 이상 (10잔)")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while True:
            try :
                capacity = int(input(f"{user}님의 치사량(주량)은 얼마만큼인가요? (1~5를 선택해주세요): "))
                if re.fullmatch(r"[0-9]", str(capacity)) and capacity <=5 and capacity >= 1:
                    if capacity == 1:
                        return 2
                    elif capacity == 2:
                        return 4
                    elif capacity == 3:
                        return 6
                    elif capacity == 4:
                        return 8
                    elif capacity == 5:
                        return 10
            except ValueError:
                print('잘못 입력하셨습니다. 다시 입력해주세요.')
#주량 선택 함수
def invite_game(player_name_choice, current_player_name):
    num = 0
    record = [current_player_name]
    participants = []
    while True:
        try :
            num = int(input("함께 취할 친구들은 얼마나 필요하신가요?(3명까지 초대 가능합니다 😁 "))
            if re.fullmatch(r"[0-9]", str(num)) and num <=3 and num>=1:
                break
        except ValueError:
            print('잘못 입력하셨습니다. 다시 입력해주세요.')

    for i in range(num):
        while True:
            name_index = random.randint(0, len(player_name_choice) - 1)
            cap_pivot = random.choice([2, 4, 6, 8, 10])

        # 중복되지 않은 이름 선택
            if player_name_choice[name_index] not in record:
                record.append(player_name_choice[name_index])
                participants.append(Player(player_name_choice[name_index], cap_pivot, True, False))
                break  # 루프 종료

    for cp in participants:
        print(f'오늘 함께 취할 친구는 {cp.name}입니다! (치사량 : {cp.drinking_capacity})')
    return participants
#플레이어 생성 및 명수 선택 함수
def execute_game(player_list):
    print_result(player_list)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~🍻 오늘의 술 게임 🍻~~~~~~~~~~~~~~~~~~~~~~")
    print("               1. 공공칠빵 게임")
    print("               2. 숫자 맞추기 게임")
    print("               3. 아파트 게임")
    print("               4. 369 게임")
    print("               5. 지하철 게임")
    #print("               exit. 게임 종료")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for player in player_list:
        if player.game_starter==True and player.computer_flag == False:
            while True:
                choice_num = int(input(f'{player.name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임> : '))
                if choice_num <= 5 and re.fullmatch(r"[0-9]", str(choice_num)):
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(f'{player.name} 님이 게임을 선택하셨습니다!😁')
                    return choice_num
                else:
                    print('잘못 입력하셨습니다.')
                    continue
        elif player.game_starter==True:
            continue_flag = input("술게임 진행 중! 다른 사람의 턴입니다. 그만하고 싶으면 \"exit\"를, 계속하고 싶으면 아무키나 입력해 주세요! : ")
            if continue_flag == "exit":
                return "exit"
            choice_num = random.randint(1, 5)
            print(f'{player.name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임> : {choice_num}')
            return choice_num
#게임 선택 함수
def print_result(player_list):
    for i in range(len(player_list)):
        print(f'{player_list[i].name}은(는) 지금까지 {player_list[i].drinks}🍺! 치사량까지 {player_list[i].drinking_capacity - player_list[i].drinks}')
#게임 끝난 후 결과 인쇄 함수
def game_over(player):
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
#게임 종료 로고 띄우는 함수
def main():
    player_name_choice = ["건욱", "예원", "태린", "현진", "유지"]
    start_game()
    time.sleep(1)
    user_name = input_user_name()
    time.sleep(1)
    capcity = select_capacity(user_name)
    main_user = Player(user_name, capcity, False, True)
    time.sleep(1)
    players = invite_game(player_name_choice, main_user.name)
    players.append(main_user)
    
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in players:
            if i.drinks >= i.drinking_capacity:
                print_result(players)
                time.sleep(1)
                game_over(i)
                return 0
        choice = execute_game(players)
        if choice == "exit":
            game_over(main_user)
            break
        if choice == 1:
            players = game007.gonggongchilbbang(players)
        elif choice == 2:
            players = guessing_number.multiplayer_guess_game(players)
        elif choice == 3:
            players = apt2.apt(players)
        elif choice == 4:
            players = game369.play_369_game(players)
        elif choice == 5:
            players = subway.subway(players)
           # 기존 코드 수정
    try:
        origin_index = next(i for i, player in enumerate(players) if player.game_starter)
        origin_selector = players[origin_index]
    except StopIteration:
        # game_starter가 True인 플레이어가 없을 때 처리
        print("Error: No player is marked as game starter. Setting the first player as the starter.")
        players[0].game_starter = True
        origin_selector = players[0]
    
    while True:
        sindex = random.randint(1, len(players)-1)
        if origin_selector.name != players[sindex].name:
            origin_selector.game_starter = False
            players[sindex].game_starter = True
            break
        
if __name__ == "__main__":
    main()