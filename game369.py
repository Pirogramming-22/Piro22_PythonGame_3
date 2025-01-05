import random

class Player:
    def __init__(self, name, drinking_capacity):
        self.name = name
        self.drinking_capacity = drinking_capacity
        self.drinks = 0

def play_369_game(players):
    print("! ! 삼 육 구 3 6 9 삼 육 구 3 6 9 ! !")
    num_rounds = 30

    current_player_idx = 0
    round_number = 1
    total_players = len(players)

    while round_number <= num_rounds:
        print("\n===========================")
        
        for i in range(len(players)):
            player = players[i]
            
            # 내 차례 
            if player == players[current_player_idx]:
                print(f"{player.name}: ", end="")
                player_input = input(f"{round_number}를 말하세요 (스페이스로 손뼉 칩니다): ")

                if '3' in str(round_number) or '6' in str(round_number) or '9' in str(round_number):
                    if player_input != ' ':
                        player.drink(1)
                        print(f"{player.name}님이 규칙을 틀렸습니다! 1잔을 마시고 게임 종료!")
                        return
                else:
                    if player_input != str(round_number):
                        player.drink(1)
                        print(f"{player.name}님이 규칙을 틀렸습니다! 1잔을 마시고 게임 종료!")
                        return

                if player_input == ' ' and ('3' in str(round_number) or '6' in str(round_number) or '9' in str(round_number)):
                    print(f"{player.name}님이 손뼉을 쳤습니다.")
                
                round_number += 1
                if players[current_player_idx].is_dead():
                    print(f"{players[current_player_idx].name}님이 치사량에 도달했습니다! 게임 종료!")
                    return
                
            else:
                # 다른 플레이어
                if '3' in str(round_number) or '6' in str(round_number) or '9' in str(round_number):
                    print(f"{player.name}: 손뼉")
                else:
                    print(f"{player.name}: {round_number}")
                round_number += 1
                if players[current_player_idx].is_dead():
                    print(f"{players[current_player_idx].name}님이 치사량에 도달했습니다! 게임 종료!")
                    return
                current_player_idx = (current_player_idx + 1) % len(players)

