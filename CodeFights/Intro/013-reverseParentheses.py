def reverseParentheses(ary):
    ary=list(ary)
    while '(' in ary:
        for i in range(len(ary)):
            if ary[i]=='(':
                head=i
            elif ary[i]==')':
                tail= i
                break
        ary[head:tail+1]= ary[tail-1:head:-1]

    return ''.join (i for i in ary)
