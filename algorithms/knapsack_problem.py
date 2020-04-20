'''
背包问题(Knapsack problem)是一种组合优化的NP完全问题。
给定一组物品，每种物品都有自己的重量和价格。
在限定的总重量内，我们如何选择，才能使得物品的总价格最高。
相似问题经常出现在商业、组合数学，计算复杂性理论、密码学和应用数学等领域中。
也可以将背包问题描述为决定性问题，即在总重量不超过W 的前提下，总价值是否能达到V ？它是在1978年由Merkle和Hellman提出的。
'''
import random


class Goods():
    total_count = 0
    type_count = 0

    def __init__(self, weight, price, amount):
        Goods.total_count += amount
        Goods.type_count += 1
        self.name = "type_{0}".format(Goods.type_count)
        self.weight = weight
        self.price = price
        self.amount = amount


def gen_batch_of_goods(amount=None, type_count=None):
    goods_list = []
    if not type_count:
        type_count = random.randint(1, 50)
    for i in range(type_count):
        if not amount:
            amount = random.randint(1, 200)
        goods = Goods(weight=random.randint(1, 10), price=random.randint(1, 200), amount=amount)
        goods_list.append(goods)
    return goods_list


goods_list = gen_batch_of_goods(amount=10000)
for goods in goods_list:
    print("种类名称 重量 价格 个数：", goods.name, goods.weight, goods.price, goods.amount)
print("种类数:", Goods.type_count, "总件数:", Goods.total_count)

'''
number 1
简单背包问题：
n件商品，每件商品有自己的重量
限定的总重量为W，求出所有的组合方案。
'''
WEIGHT_MAX = 100


# 法1 递归法
def func1():
    pass
