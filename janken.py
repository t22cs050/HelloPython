import random
#11/15 プッシュ確認

class Player:
    # プレイヤークラスのコンストラクタ
    # 引数： name プレイヤーの名前
    def __init__(self, name):
        self._name = name
        self._wincount = 0
        
    # じゃんけんの手を出す関数：
    # 0, 1, 2 をランダムに出力する
    def show_hand(self):
        return random.randrange(3)


playerInput = input("0:グー,1:チョキ,2:パー  :")

enemyInput = random.randint(0, 2)

result = "あなたの⼿︓"

if (playerInput == "0"):
    result += "グー v.s. 相手の⼿︓"
    if (enemyInput == 0):
        result += "グー -> あいこ"
    elif (enemyInput == 1):
        result += "チョキ -> 相手の負け"
    elif (enemyInput == 2):
        result += "パー -> 相手の勝ち"
    print(result)
     
elif (playerInput == "1"):
    result += "チョキ v.s. 相手の⼿︓"
    if (enemyInput == 0):
        result += "グー -> 相手の勝ち"
    elif (enemyInput == 1):
        result += "チョキ -> あいこ"
    elif (enemyInput == 2):
        result += "パー -> 相手の負け"
    print(result)

elif (playerInput == "2"):
    result += "パー v.s. 相手の⼿︓"
    if (enemyInput == 0):
        result += "グー -> 相手の負け"
    elif (enemyInput == 1):
        result += "チョキ -> 相手の勝ち"
    elif (enemyInput == 2):
        result += "パー -> あいこ"
    print(result)

else:
    print("エラー！")