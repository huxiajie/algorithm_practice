'''
number 1
匹配字符串
考虑两个问题：1.如果相等怎么办  2.如果不相等怎么办
'''


# 法1：朴素串匹配:返回第一个匹配的下标
# 最坏的情况：只有p[-1]不相等，O(s*p),效率过低
def string_match_naive(pattern, string):
    m = len(pattern)
    n = len(string)
    i, j = 0, 0
    count = 0
    while i < m and j < n:
        count += 1
        if pattern[i] == string[j]:
            i, j = i + 1, j + 1
        else:
            i, j = 0, j - i + 1
    print("朴素算法：", count, len(string))
    if i == m:
        return j - i
    else:
        return -1


# todo 法2：KMP串匹配:记录信息，加以分析，做到不回溯 O(n)x
# http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/
# 问题的关键在于：每次匹配失败后，是有一些有用信息的，抓住这些信息，就可以找到下个开始匹配的正确位置，跳过一些无用字母
# 关有用信息就是：proper prefix & proper suffix
# 对与朴素算法的最差情况特别有效：
# string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz1"
# pattern = "abcdefghijklmnopqrstuvwxyz1"

def string_match_kmp(pattern, string, pnext):
    m, i = len(pattern), 0
    n, j = len(string), 0
    count = 0
    while i < m and j < n:
        count += 1
        if pattern[i] == string[j]:
            i, j = i + 1, j + 1
        elif pnext[i] == -1:
            j = j + 1
        else:
            i = pnext[i]
    print("kmp算法：", count, len(string))
    if i == m:
        return j - i
    else:
        return -1


# O(n)生成部分匹配表的方法也是kmp
# string 是pattern，pattern也是pattern 实时写入
def create_pnext(pattern):
    count = 0
    pnext = [None] * len(pattern)
    pnext[0] = -1
    # j指向的是pattern串的下表
    i, j = 0, -1
    while i < len(pattern) - 1:
        count += 1
        if j == -1 or pattern[i] == pattern[j]:
            i, j = i + 1, j + 1
            pnext[i] = j
        else:
            j = pnext[j]
    print(count, len(pattern))
    return pnext


if __name__ == "__main__":
    pattern = "abababca"
    string = "ababbcababababca"

    # string = "qwertyuiopqwertyuioqwertyuiopqwertyuioppqwertyuiopqwertyuiopqwertyuiopqwertyuiopa"
    # pattern = "qwertyuiopqwertyuiopa"

    pnext = create_pnext(pattern)
    print(pnext)
    res = string_match_kmp(pattern=pattern, string=string, pnext=pnext)
    res2 = string_match_naive(pattern=pattern, string=string)
    print(res, res2)
