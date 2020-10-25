# Title: Infix Expression and Postfix Expression
# Time: 2020/10/16
# Author: Vincent

# 后缀表达式的计算
def PostfixExpressionCounter(s):
    nums = []
    for i in s:
        if i not in '+-*/':
            nums.append(int(i))
        else:
            num2 = nums.pop()
            num1 = nums.pop()
        
            if i == '-':
                nums.append(num1-num2)
            elif i == '+':
                nums.append(num1+num2)
            elif i == '/':
                nums.append(num1/num2)
            else:
                nums.append(num1*num2)
                
    if len(nums) == 1:
        return nums[0]
    raise SyntaxError('表达式结构错误！')


# 中缀表达式转为后缀表达式
def infix_to_postfix(s):
    priority = {'(':1, '+':2, '-':2, '*':3, '/':3}
    signal = '()-+*/'
    tmp = [] # 运算符缓存空间
    exp = [] # 表达式
    for x in s:
        
        if x not in signal:
            exp.append(x)
        elif len(tmp) == 0 or x == '(':
            tmp.append(x)
        elif x == ')':
            while len(tmp) > 0 and tmp[-1] != '(':
                exp.append(tmp.pop())
            if len(tmp) == 0:
                raise SyntaxError('不存在对应的"("')
            tmp.pop()
        else:
            while len(tmp) > 0 and priority[tmp[-1]] >= priority[x]:
                exp.append(tmp.pop())
            tmp.append(x)
    while len(tmp) > 0:
        if tmp[-1] == '(':
            raise SyntaxError('存在多余的"("！')
        exp.append(tmp.pop())
            
    return exp
                                  

if __name__ == '__main__':
    # postfix = ['3', '5', '-', '6', '17', '4', '*', '+', '*', '3', '/']
    # print(PostfixExpressionCounter(postfix))
    
    # error = ['3', '5', '-', '6', '17', '4', '*', '+', '*', '3', '4']
    # print(PostfixExpressionCounter(error))
    
    infix = ['(', '3', '-', '5', ')', '*', '(', '6', '+', '17', '*','4', ')', 
             '/', '3']
    print(infix_to_postfix(infix))