import random
import time

class Player:
    def __init__(self, name, drinking_capacity):
        self.name = name
        self.drinking_capacity = drinking_capacity
        self.drinks = 0

def show_drinks_status(players):
        for p in players:
            print(f"{p.name}은(는) 지금까지 {p.drinks}🍺! 치사량까지 {p.drinking_capacity - p.drinks}")
        print()

def gonggongchilbbang(players):

    current_player = 0
    sequence = ['공', '공', '칠', '빵']
    expected_index = 0

    while True:
        current = players[current_player]
        current.drinks_before = current.drinks
        expected_word = sequence[expected_index]
        
        if current == players[0]:  # 주 플레이어의 차례
            print(f"\n{current.name}의 차례입니다.")
            action = input("'공', '공', '칠', '빵' 중 하나를 입력하세요: ")
            
            if action == expected_word:
                print(f"\n{current.name}: {action}")
                time.sleep(1)
                
                # 다음 플레이어 선택
                print("\n다음 플레이어를 선택하세요:\n")
                for i, player in enumerate(players):
                    if player != current:
                        print(f"{i + 1}. {player.name}\n")
                while True:
                    try:
                        choice = int(input("번호를 입력하세요: ")) - 1
                        if 0 <= choice < len(players) and players[choice] != current:
                            next_player = choice
                            print(f"\n{current.name}이(가) {players[next_player].name}을(를) 지목했습니다.\n")
                            time.sleep(1)
                            if action == '빵':
                                time.sleep(1)
                                left_player = (next_player - 1) % len(players)
                                right_player = (next_player + 1) % len(players)
                                should_eoak = players[0] in [players[left_player], players[right_player]]
                                eoak_choice = input("으악을 외치시겠습니까? (y/n): ").lower()
                                if(eoak_choice == 'y'):
                                    print(f"{players[0].name}: 으악!\n")
                                    if not should_eoak:
                                        print(f"{players[0].name}이(가) 잘못 '으악'을 외쳤습니다. 술을 마십니다!\n")
                                        players[0].drinks += 1
                                        show_drinks_status(players)
                                        return [players[0].name, players[0].drinks]
                                elif eoak_choice == 'n':
                                    print(f"{players[0].name}이(가) '으악'을 외치지 않았습니다.\n")
                                    if should_eoak:
                                        print(f"{players[0].name}이(가) '으악'을 외치지 않아 술을 마십니다!\n")
                                        players[0].drinks += 1
                                        show_drinks_status(players)
                                        return [players[0].name, players[0].drinks]
                                else:
                                    print(f"{players[0].name}이(가) 잘못된 선택을 했습니다. 술을 마십니다!\n")
                                    players[0].drinks += 1
                                    show_drinks_status(players)
                                    return [players[0].name, players[0].drinks]
                                time.sleep(1)
                            current_player = next_player
                            break
                        else:
                            print("올바른 번호를 입력하세요.")
                    except ValueError:
                        print("숫자를 입력하세요.")
            else:
                print(f"{current.name}이(가) 실수했습니다! 술을 마십니다.\n")
                time.sleep(1)
                current.drinks += 1
                show_drinks_status(players)
                current_player = (current_player + 1) % len(players)
                return [current.name, current.drinks]
        else:  # AI 플레이어의 차례
            if random.random() < 0.1:  # 90% 확률로 성공
                print(f"{current.name}: {expected_word}")
                time.sleep(1)
                
                # AI가 다음 플레이어 선택 (자기 자신 제외)
                available_players = [i for i in range(len(players)) if i != current_player]
                next_player = random.choice(available_players)
                print(f"\n{current.name}이(가) {players[next_player].name}을(를) 지목했습니다.\n")
                time.sleep(1)
                if expected_word == '빵':
                    time.sleep(1)
                    left_player = (next_player - 1) % len(players)
                    right_player = (next_player + 1) % len(players)
                    should_eoak = players[0] in [players[left_player], players[right_player]]
                    eoak_choice = input("으악을 외치시겠습니까? (y/n): ").lower()
                    if(eoak_choice == 'y'):
                        print(f"\n{players[0].name}: 으악!\n")
                        if not should_eoak:
                            print(f"{players[0].name}이(가) 잘못 '으악'을 외쳤습니다. 술을 마십니다!\n")
                            players[0].drinks += 1
                            show_drinks_status(players)
                            return [players[0].name, players[0].drinks]
                    elif eoak_choice == 'n':
                        print(f"\n{players[0].name}이(가) '으악'을 외치지 않았습니다.\n")
                        if should_eoak:
                            print(f"{players[0].name}이(가) '으악'을 외치지 않아 술을 마십니다!\n")
                            players[0].drinks += 1
                            show_drinks_status(players)
                            return [players[0].name, players[0].drinks]
                    else:
                        print(f"{players[0].name}이(가) 잘못된 선택을 했습니다. 술을 마십니다!\n")
                        players[0].drinks += 1
                        show_drinks_status(players)
                        return [players[0].name, players[0].drinks]
                    time.sleep(1)
                current_player = next_player
            else:
                print(f"{current.name}이(가) 실수했습니다! 술을 마십니다.\n")
                time.sleep(1)
                current.drinks += 1
                current_player = (current_player + 1) % len(players)
                show_drinks_status(players)
                return [current.name, current.drinks]

        expected_index = (expected_index + 1) % len(sequence)