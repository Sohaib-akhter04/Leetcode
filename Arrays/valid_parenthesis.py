def check_parenthesis(string):
    stack=[]
    open_bracket=['(','{','[']
    close_bracket=[')','}',']']
    for i in string:
        if i in open_bracket:
            stack.append(i)
        elif i in close_bracket:
            pos=close_bracket.index(i)
            if (len(stack)>0 and open_bracket[pos]==stack[len(stack)-1]):
                stack.pop()
            else:
                return "unbalanced"

    if len(stack)==0:
        return "balanced"
    else:
        return "unbalanced"

if __name__=='__main__':
    string = "{[]{()}}"
    print(check_parenthesis(string))