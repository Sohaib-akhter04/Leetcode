def check(string):
    stack=[]
    open_list=['(','{','[']
    close_list=[')','}',']']
    for i in string:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos=close_list.index(i)
            if(len(stack)>0 and (open_list[pos]==stack[len(stack)-1])):
                stack.pop()
            else:
                return "UnBalanced"
    if len(stack)==0:
        return "Balanced"
    else:
        return "Unbalanced"




if __name__ == '__main__':
    string = "{[]{()}}"
    print(string,"-", check(string))
 
    string = "[{}{})(]"
    print(string,"-", check(string))
 
    string = "((()"
    print(string,"-",check(string))