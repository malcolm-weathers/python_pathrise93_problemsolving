# Given a mathematical expression as a string, return an int computing the
# value of the expression.

# Cheat by just calling eval().
def cheat(expr):
    return eval(expr)

# Given a list of lexemes, i.e. '5', '+', '(', ')',... take anything grouped
# within parentheses and turn into its own nested list. Doesn't check for
# equal number of parentheses.
def parenth(lex):
    if type(lex) != list:
        return
    p_i = p_j = -1
    for i in range(len(lex)):
        if lex[i] == '(':
            p_i = i
            break
    for j in range(len(lex) - 1, i + 1, -1):
        if lex[j] == ')':
            p_j = j
            break

    if p_i != -1:
        slce = lex[p_i + 1:p_j]
        del lex[p_i:p_j + 1]
        lex.insert(p_i, slce)
        parenth(lex)
    else:
        for i in range(len(lex)):
            parenth(lex[i])

# Takes list of lexemes with parentheses turned into nested lists. Evaluates
# and returns the correct value.
def evaluate(lex):
    for i in range(len(lex)):
        if type(lex[i]) == list:
            evaluate(lex[i])
    for i in range(len(lex)):
        if type(lex[i]) == list and len(lex[i]) == 1:
            lex[i] = lex[i][0]

    while '^' in lex:
        p = lex.index('^')
        v = float(lex[p - 1]) ** float(lex[p + 1])
        del lex[p - 1:p + 2]
        lex.insert(p - 1, v)
    while '*' in lex:
        p = lex.index('*')
        v = float(lex[p - 1]) * float(lex[p + 1])
        del lex[p - 1:p + 2]
        lex.insert(p - 1, v)
    while '/' in lex:
        p = lex.index('/')
        v = float(lex[p - 1]) * float(lex[p + 1])
        del lex[p - 1:p + 2]
        lex.insert(p - 1, v)
    while '+' in lex:
        p = lex.index('+')
        v = float(lex[p - 1]) + float(lex[p + 1])
        del lex[p - 1:p + 2]
        lex.insert(p - 1, v)
    while '-' in lex:
        p = lex.index('-')
        v = float(lex[p - 1]) - float(lex[p + 1])
        del lex[p - 1:p + 2]
        lex.insert(p - 1, v)

# Evluate a mathematical expression as a string.
def actual(expr):
    # Turn expression into list of lexemes:
    # 13+(6-5) -> 13 + ( 6 - 5 )
    lex = []
    curr_num = ''
    for i in range(len(expr)):
        if expr[i].isdigit():
            curr_num += expr[i]
        else:
            if curr_num != '':
                lex.append(curr_num)
            lex.append(expr[i])
            curr_num = ''
    if curr_num != '':
        lex.append(curr_num)
    # Turn parentheses into nested lists:
    # 13 + ( 6 - 5 ) -> [13, +, [6, -, 5]]
    parenth(lex)
    # Evaluate:
    # [13, +, [6, -, 5]] -> [13, +, 1] -> [14] -> 14
    evaluate(lex)
    return lex[0]

def main():
    print(cheat('1+(3-(6+5))*2'))
    print(actual('1+(3-(6+5))*2'))

if __name__ == '__main__':
    main()
