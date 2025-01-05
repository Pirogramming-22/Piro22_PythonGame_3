import random
import time

'''class Player:
    def __init__(self, name, drinking_capacity, computer_flag):
        self.name = name
        self.drinking_capacity = drinking_capacity
        self.drinks = 0
        self.computer_flag = computer_flag'''


def multiplayer_guess_game(players):
    print("소주🍶 뚜껑 숫자 맞추기 게임에 오신 것을 환영합니다!")

    # 문제 내는 사람 랜덤 선택
    setter = random.choice(players)
    print(f"{setter.name}이(가) 문제를 냅니다.")

    # 문제 번호 1~50 사이 랜덤 생성
    number_to_guess = random.randint(1, 50)
    print(f"문제가 설정되었습니다. (1~50 사이의 숫자)")

    # 문제 내는 사람 제외
    players = [player for player in players if player != setter]
    print(f"게임 참가자: {', '.join(player.name for player in players)}")

    turn = 0
    lower_bound = 1
    upper_bound = 50

    while True:
        current_player = players[turn % len(players)]
        print(f"{current_player.name}의 차례입니다.")

        if not current_player.computer_flag:
            guess = int(input(f"숫자를 입력하세요 (범위: {lower_bound} ~ {upper_bound}): "))
        else:
            guess = random.randint(lower_bound, upper_bound)
            time.sleep(2)  # 2초 텀 추가
            print(f"{current_player.name}의 추측: {guess}")

        current_player.drinks += 1

        if guess == number_to_guess:
            if not current_player.computer_flag:
                print(f"축하합니다! {current_player.name}이(가) {current_player.drinks}번 만에 정답을 맞췄습니다!")
                return players
            else:
                print(f"{current_player.name}이(가) {current_player.drinks}번 만에 정답을 맞췄습니다. 다음엔 더 잘하세요!")
                return players
            break
        elif guess < number_to_guess:
            print("너무 낮습니다!")
            lower_bound = max(lower_bound, guess + 1)
        else:
            print("너무 높습니다!")
            upper_bound = min(upper_bound, guess - 1)

        turn += 1

'''if __name__ == "__main__":
    
    # 테스트용 플레이어 생성
    players = [
        Player("예원", 5, False),  # 사용자
        Player("a", 4, True),
        Player("b", 3, True),
        Player("c", 6, True)
    ]

    multiplayer_guess_game(players)'''
