def play_369_game(players):
    print("! ! 삼 육 구 3 6 9 삼 육 구 3 6 9 ! !")
    num_rounds = 30

    current_player_idx = 0 
    round_number = 1
    players
    while round_number <= num_rounds:
        print("\n==================================================")
        
        player = players[current_player_idx]

        # 내 차례
        if player.computer_flag == False:
            print(f"{player.name}", end="")
            player_input = input("(스페이스로 손뼉 칩니다): ")

            if '3' in str(round_number) or '6' in str(round_number) or '9' in str(round_number):
                if player_input != ' ':
                    player.drinks += 1
                    print(f"{player.name}님이 규칙을 틀렸습니다! 1잔을 마시고 게임 종료!")
                    return players
            else:
                if player_input != str(round_number):
                    player.drinks += 1
                    print(f"{player.name}님이 규칙을 틀렸습니다! 1잔을 마시고 게임 종료!")
                    return players

            if player_input == ' ' and ('3' in str(round_number) or '6' in str(round_number) or '9' in str(round_number)):
                print(f"{player.name}님이 손뼉을 쳤습니다.")
            
        else:
            # 다른 플레이어
            if '3' in str(round_number) or '6' in str(round_number) or '9' in str(round_number):
                print(f"{player.name}: 손뼉") 
            else:
                print(f"{player.name}: {round_number}")
        round_number += 1

        current_player_idx = (current_player_idx + 1) % len(players)

    return players

