'''
number 1
括号匹配：所有括号都应该开闭是一对，支持括号嵌套的场景
括号包括[] {} ()
根据问题确定数据结构是关键
'''
# from data_structure.stack import StackPythonList


def bracket_matching(string):
    bracket_stack = StackPythonList()
    bracket_chars = {')': '(', '}': '{', ']': '['}
    for char in string:
        if char in bracket_chars.values():
            bracket_stack.push(char)
        elif char in bracket_chars.keys():
            element = bracket_stack.pop()
            if not element or element != bracket_chars[char]:
                return False
    if not bracket_stack.is_empty():
        return False
    return True


# print(bracket_matching("((4*(5+({6/3}*([2])+6)))"))
'''
number 2 
计算后缀表达式
'''
infix_expression = "(1-2*3+4)+(4*5+6)-2*3+(4*5+6)*7"
prefix_expression = "/ * - 3 5 + 6 + 15 4.4 3"
suffix_expression = "1 2 3 * - 4.0 + 4.0 5.0 * 6.0 + + 2.0 3.0 * - 4.0 5.0 * 6.0 + 7.0 * +"


def calculate(op, left, right):
    if not right or not left:
        return None
    try:
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
    except Exception as e:
        print(e)
        return None


def calculate_suffix_expression(expr):
    op_list = ['+', '-', "*", '/']
    expr = expr.split(" ")
    cal_stack = StackPythonList()
    for element in expr:
        if element in op_list:
            res = calculate(op=element, right=cal_stack.pop(), left=cal_stack.pop())
            if not res:
                return None
            cal_stack.push(res)
        else:
            cal_stack.push(float(element))
    return cal_stack.pop()


print(calculate_suffix_expression(suffix_expression))
'''
number 3 
计算中缀表达式
'''


def to_list(expr):
    op_list = ['+', '-', "*", '/', '(', ')']
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    num = ''
    expression_list = []
    for char in expr:
        if char in op_list:
            if num:
                expression_list.append(float(num))
                num = ""
            expression_list.append(char)
        elif char in num_list:
            num += char
    if num:
        expression_list.append(float(num))
    return expression_list


# 思路完全 等同于 中缀转后缀
def calculate_infix_expression(expr):
    op_list = {'+': 0, '-': 0, "*": 1, '/': 1, '(': 2, ')': 2}
    expr = to_list(expr)
    num_st = StackPythonList()
    op_st = StackPythonList()

    for item in expr:
        if item not in op_list.keys():
            num_st.push(item)
        elif item == ')':
            while not op_st.is_empty():
                op = op_st.pop()
                if op == "(":
                    break
                num_st.push(calculate(op=op, right=num_st.pop(), left=num_st.pop()))
        elif item in op_list:
            top = op_st.read_top_element()
            while top and top != '(' and op_list[item] <= op_list[top]:
                num_st.push(calculate(op=op_st.pop(), right=num_st.pop(), left=num_st.pop()))
                top = op_st.read_top_element()
            op_st.push(item)

    while not op_st.is_empty():
        num_st.push(calculate(op=op_st.pop(), right=num_st.pop(), left=num_st.pop()))
    return num_st.pop()


print(calculate_infix_expression(infix_expression))

'''
number 4
中缀表达式缺点：顺序不直观，需要括号辅助
中缀表达式 转换成 后缀表达式（最适合计算机处理）
条件：仅包括二元运算符 ( ) + - * /
'''


# 思路：遍历中缀表达式时分别会遇到 数字；（ ；+-；*/；）这几种情况。
#      每种情况应该怎么处理？
#      在处理时，会遇到什么样的场景？即判断的时所用的变量可能为空 或 A 或 B
def infix_to_suffix(infix_expr):
    op_list = {'+': 0, '-': 0, "*": 1, '/': 1, '(': 2, ')': 2}
    infix_expr = to_list(infix_expr)
    st = StackPythonList()
    suffix_expr = []

    for item in infix_expr:
        # 1.数字直接输出
        if item not in op_list.keys():
            suffix_expr.append(item)
        # 2.')':需要把之前的运算操作都弹出，直至遇见（
        elif item == ')':
            while not st.is_empty():
                element = st.pop()
                if element == "(":
                    break
                suffix_expr.append(element)
        elif item in op_list:
            top = st.read_top_element()
            # 3.'(':直接push
            #   其他运算符：比较当前运算符和栈顶运算符的优先级
            #             若栈顶 >= 当前：先输出已有运算符,再push；否则直接push
            #             top=( ：直接push
            while top and top != '(' and op_list[item] <= op_list[top]:
                suffix_expr.append(st.pop())
                top = st.read_top_element()
            st.push(item)
    while not st.is_empty():
        suffix_expr.append(st.pop())
    return suffix_expr


print(infix_to_suffix(infix_expression))