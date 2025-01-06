import random
import time

def gonggongchilbbang(players):
    current_player = 0
    sequence = ['공', '공', '칠', '빵']
    expected_index = 0

    while True:
        current = players[current_player]
        expected_word = sequence[expected_index]
        
        print(f"\n{current.name}의 차례입니다.")
        
        if not current.computer_flag:  # 주 플레이어의 차례
            action = input("'공', '공', '칠', '빵' 중 하나를 입력하세요: ")
        else:  # AI 플레이어의 차례
            action = expected_word if random.random() < 0.7 else random.choice(sequence)  # 70% 확률로 정확한 단어 선택
            print(f"{current.name}: {action}")
            time.sleep(1)

        if action == expected_word:
            # 다음 플레이어 선택
            if not current.computer_flag:
                print("\n다음 플레이어를 선택하세요:")
                for i, player in enumerate(players):
                    if player != current:
                        print(f"{i + 1}. {player.name}")
                while True:
                    try:
                        choice = int(input("번호를 입력하세요: ")) - 1
                        if 0 <= choice < len(players) and players[choice] != current:
                            next_player = choice
                            break
                        else:
                            print("올바른 번호를 입력하세요.")
                    except ValueError:
                        print("숫자를 입력하세요.")
            else:
                available_players = [i for i in range(len(players)) if i != current_player]
                next_player = random.choice(available_players)
            
            print(f"\n{current.name}이(가) {players[next_player].name}을(를) 지목했습니다.")
            time.sleep(1)

            if action == '빵':
                left_player = (next_player - 1) % len(players)
                right_player = (next_player + 1) % len(players)
                should_eoak = players[-1] in [players[left_player], players[right_player]]
                
                for p in players:
                    if not p.computer_flag:
                        eoak_choice = input(f"{p.name}, 으악을 외치시겠습니까? (y/n): ").lower()
                        if eoak_choice == 'y':
                            print(f"{p.name}: 으악!")
                            if not should_eoak:
                                print(f"{p.name}이(가) 잘못 '으악'을 외쳤습니다. 술을 마십니다!")
                                p.drinks += 1
                                return players
                        elif eoak_choice == 'n':
                            if should_eoak:
                                print(f"{p.name}이(가) '으악'을 외치지 않아 술을 마십니다!")
                                p.drinks += 1
                                return players
                        else:
                            print(f"{p.name}이(가) 잘못된 선택을 했습니다. 술을 마십니다!")
                            p.drinks += 1
                            return players
                        break  # 첫 번째 사람 플레이어만 선택하도록 함
                time.sleep(1)

            current_player = next_player
        else:
            print(f"{current.name}이(가) 실수했습니다! 술을 마십니다.")
            time.sleep(1)
            current.drinks += 1
            return players

        expected_index = (expected_index + 1) % len(sequence)

def print_result(player_list):
    for i in range(len(player_list)):
        print(f'{player_list[i].name}은(는) 지금까지 {player_list[i].drinks}🍺! 치사량까지 {player_list[i].drinking_capacity - player_list[i].drinks}')