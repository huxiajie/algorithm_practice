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


# pattern = "abababca"
# string = "ababbcababababca"

# string = "qwertyuiopqwertyuioqwertyuiopqwertyuioppqwertyuiopqwertyuiopqwertyuiopqwertyuiopa"
pattern = "qwertyuiopqwertyuiopa"

# pnext = create_pnext(pattern)
# print(pnext)
# res = string_match_kmp(pattern=pattern, string=string, pnext=pnext)
# res2 = string_match_naive(pattern=pattern, string=string)
# print(res, res2)
