import random,time
if __name__=="__main__":
    flag=1
    money=0
    round_count=1
    rules = {
        1:[1,2,3,4,5,6],
        2:[1,2,3,4,5],
        3:[1,2,3,4],
        4:[1,2,3],
        5:[1,2],
        6:[1]
    }
    price = [0.88,1.88,3.88,8.88,12.88,28.88]
    print("*****开始游戏*****")
    time.sleep(2)
    while flag==1:
        print("【第{0}轮】".format(round_count))
        round_count +=1
        dice1=random.randint(1,6)
        print("骰子1：",dice1)
        time.sleep(1)
        dice2 = random.randint(1, 6)
        print("骰子2：", dice2)
        time.sleep(1)
        money = money - 2.99
        if dice2 in rules[dice1]:
            money = money + price[dice1-1]
            print("恭喜恭喜，获奖 {0} 元，净赚 {1} 元".format(price[dice1-1], float('%.3f'%money)))
        else:
            print("很遗憾，没有中奖哦! ，净赚 {0} 元".format(float('%.3f'%money)))
        flag=int(input("再来一轮吗？1：yes  2:no\n"))
    print("*****结束游戏*****")