import time, os, random, json, threading

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1  

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.is_full():
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:

            self.front = (self.front + 1) % self.size
        return data
      
    def show_all(self):
      print(self.queue)
    
def rhythm_text(text, width):
  for i in range(len(text) + width):
    os.system("cls" if os.name == "nt" else "clear")
    print(" " * (width - i) + text[:i])
    time.sleep(0.01)  # 속도 조절

def time_up():
  raise SystemExit

'''def set_loser(player_list, loser):
  start_index = next(i for i, player in enumerate(player_list) if player.game_starter)
  origin_loser = player_list[start_index]
  if origin_loser.name == loser.name:
    return
  else:
    origin_loser.game_starter = False
    loser.game_starter = True'''
    
def subway(player_list):
  line_list =["1호선","2호선","3호선","4호선","5호선","6호선","7호선","8호선","9호선","GTX-A","경강선","경의선","경춘선","공항철도","김포도시철도","서해선","수인분당선","신림선","신분당선","용인경전철","우이신설경전철","의정부경전철","인천2호선","인천선"]
  repeat_flag = True
  line_decision = None
  cq = CircularQueue(len(player_list))
  record = []
  
  print("""
                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣷⡄⠀⢀⣴⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⣿⣿⣿⡟⠀⠰⣿⣿⣿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠛⠏⠀⠀⠀⠙⠻⠛⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣾⣷⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣷⣿⣾⣾⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⠈⠈⠈⠈⠈⠁⠉⠈⠈⠈⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣾⣷⣿⣾⣾⣷⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡁⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⠂⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⣦⣀⠀⡀⢀⠀⡀⡀⡀⡀⡀⡀⡀⢠⣗⢀⠀⡀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣠⣴⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⡟⠋⢀⣀⣀⡀⠙⢻⣿⣿⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣿⣿⣿⠟⠉⣀⣠⣀⡀⠙⢿⣿⣿⣿⣿⣿⠅⠀⠀⠀
⠀                      ⠀⠀⠨⣿⣿⣿⣿⣿⠁⣸⣿⣿⣿⣿⣦⠐⣻⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⡟⠀⣼⣿⣿⣿⣿⣆⠘⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠨⣿⣿⣿⣿⣿⠀⠺⣿⣿⣿⣿⠏⠀⣾⣿⣷⣶⣷⣶⣾⣶⣶⣷⣶⣾⣾⣿⣿⣯⠀⢻⣿⣿⣿⣿⠇⢀⣿⣿⣿⣿⣿⠅⠀⠀⠀
                      ⠀⠀⠀⠀⢿⣿⣿⣿⣿⣷⣀⠈⠋⠉⢁⣠⣾⣿⣿⣭⣭⣫⣝⣭⣫⣫⣙⣙⣍⣻⣿⣿⣿⣧⣀⠈⠋⠙⢀⢤⣿⣿⣿⣿⣿⡯⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀
⠀                      ⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⠟⠈⠀⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁⠈⠈⠀⠻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⠿⠾⠶⠷⠷⠾⠶⠷⠾⠶⠷⠾⠶⠷⠾⠶⠷⠾⠶⠷⠾⠾⠾⠾⠾⠿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⡿⡁⢀⠀⡀⢀⠀⡀⢀⠀⡀⢀⠀⡀⢀⠀⡀⢀⠀⡀⢀⠀⡀⢀⠀⡀⢀⠀⡈⣿⣿⣿⣿⣿⣿⣂⠀⠀⠀⠀
                      ⠀⠀⢀⣼⣿⣿⣿⣿⣿⠟⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠙⠻⣿⣿⣿⣿⣿⣧⠀⠀⠀
                      ⠀⢀⣾⣿⣿⣿⣿⣿⣯⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣦⣿⣿⣿⣿⣿⣿⣷⡀⠀
                      ⣠⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣄



                _______. __    __  .______   ____    __    ____  ___   ____    ____ 
                /       ||  |  |  | |   _  \  \   \  /  \  /   / /   \  \   \  /   / 
               |   (----`|  |  |  | |  |_)  |  \   \/    \/   / /  ^  \  \   \/   /  
                \   \    |  |  |  | |   _  <    \            / /  /_\  \  \_    _/   
            .----)   |   |  `--'  | |  |_)  |    \    /\    / /  _____  \   |  |     
            |_______/     \______/  |______/      \__/  \__/ /__/     \__\  |__|     

                          _______      ___      .___  ___.  _______ 
                         /  _____|    /   \     |   \/   | |   ____|
                        |  |  __     /  ^  \    |  \  /  | |  |__   
                        |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
                        |  |__| |  /  _____  \  |  |  |  | |  |____ 
                         \______| /__/     \__\ |__|  |__| |_______|
                                                                    

                        """)
  time.sleep(1)

  while(repeat_flag):
    text = "지하철~ 지하철~ 지하철~ 지하철~ 지하철~ 지하철~"
    width = 60  # 출력창 너비
    rhythm_text(text, width)
    text = "몇호선~ 몇호선~ 몇호선~ 몇호선~"
    rhythm_text(text, width)
    
    for i in player_list:
      if i.game_starter:
        if i.computer_flag:
          line_decision = line_list[random.randint(1,24)]
          text = f'{line_decision}~ {line_decision}~ {line_decision}~ {line_decision}~'
          rhythm_text(text, width)
          repeat_flag=False
        else:
          line_decision = input('어떤 노선으로 게임을 진행하시겠습니까? ')

          if line_decision not in line_list:
            rhythm_text("X신 샷 아 X신 샷 X신 샷은 BGM이 없어요~", 60)
            print(f'{i.name}이(가) 술을 마셨다')
            time.sleep(1)
            i.drinks += 1
            if i.drinks >= i.drinking_capacity:
              return player_list
          else:
            text = f'{line_decision}~ {line_decision}~ {line_decision}~ {line_decision}~'
            rhythm_text(text, width)
            repeat_flag=False
  
  with open('./서울시 지하철역 정보 검색 (역명).json',"r", encoding="utf-8") as sd:
    data = json.load(sd)
  
  start_index = next(i for i, player in enumerate(player_list) if player.game_starter)
  
  for i in range(len(player_list)):
    cq.enqueue(player_list[(start_index + i) % len(player_list)])
  
  
  while True:
    current_speaker = cq.dequeue()
    if current_speaker.computer_flag:
      skip_flag = False
      station_decision = random.randint(0,794)
      
      for index, station in enumerate(data["DATA"]):
        if index == station_decision:
          time.sleep(1)
          print(f'{current_speaker.name} : {station["station_nm"]}')
          if station["line_num"] == line_decision and station["line_num"] not in record:
            record.append(station["line_num"])
            skip_flag = True
      
      if skip_flag:
        continue
      
      print(f'아 누가 술을 마셔 {current_speaker.name}이(가) 술을 마셔 👏 원샷~!')
      current_speaker.drinks += 1
            #set_loser(player_list,current_speaker)
      return player_list

    else:
      station_decision = input('역의 이름을 입력하시오.').strip()
      skip_flag = False

      for index, station in enumerate(data["DATA"]):
        if station["station_nm"] == station_decision and station_decision not in record:
          if station["line_num"] == line_decision:
            record.append(station_decision)
            skip_flag = True

      if skip_flag:
        continue
      
      print(f'아 누가 술을 마셔 {current_speaker.name}이(가) 술을 마셔 👏 원샷~!')
      current_speaker.drinks += 1
      #set_loser(player_list,current_speaker)
      return player_list
    cq.enqueue(current_speaker)