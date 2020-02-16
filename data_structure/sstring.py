# 正则表达式
import re


def regex():
    string = "ababagsdcblvfzblsz#$%^&1234567abcgabcf"

    # 生成regex,并将regex赋值给pattern
    pattern = re.compile("abc(g|f)")

    # 在目标串中寻找pattern
    # 返回：match对象（第一个匹配的）或 None
    match1_1 = re.search(pattern=pattern, string=string)
    match1_2 = re.search(pattern="abc(g|f)", string=string)
    print("re.search", match1_1, match1_2)

    # 目标串以pattern开头
    # 返回：match对象（第一个匹配的）或 None
    match2_1 = re.match(pattern=pattern, string=string)
    print("re.match", match2_1)

    # 以list形式返回所有匹配的字符串
    # 不包括重叠的
    match4_1 = re.findall(pattern="aba", string="ababa")
    # 若pattern是固定写死的，那么lenlen(list)=匹配个数
    match4_2 = re.findall(pattern="ab", string="abcabcabcabc")
    # 若pattern是有多种可能性的，那么len(list)=不重叠的匹配个数
    match4_3 = re.findall(pattern="ab(a|c)", string="abaaba")
    match4_4 = re.findall(pattern="ab(a|c)", string="abcaba")
    print("re.findall", match4_1, match4_2, match4_3, match4_4)

    # 被两个分隔符包围着的内容输出，作为list中的一个元素；首、尾字符仅被一个分隔符包围
    list3_1 = re.split(";", "1;2;3;4")
    list3_2 = re.split(";", ";1;2;;3;;;4;")
    list3_3 = re.split(";", "1234")
    print("re.split", list3_1, list3_2, list3_3)

    # match对象常用属性和方法
    if match1_1:
        print("=====match对象常用属性和方法=====")
        # 获取目标串 和 正则表达式
        print("match.string: ", match1_1.string, "\nmatch.re: ", match1_1.re)
        # 获得匹配的子串
        print("match.group(): ", match1_1.group())
        print("match.group(): ", match1_1.group(1))
        # 获得匹配子串的 开始index 和 结束index+1,常用开始
        print("match.start(): ", match1_1.start(), "\nmatch.end(): ", match1_1.end())
        # 元组方式返回（开始index, 结束index+1）
        print("match.span(): ", match1_1.span())


if __name__ == "__main__":
    regex()
