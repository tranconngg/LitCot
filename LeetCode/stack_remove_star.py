# sol1
def stack_remove_star(strs):
    st_str=list(strs)
    s=''
    cnt =0
    for _ in range(len(strs)):
        s_pop=st_str.pop()
        if s_pop != '*':
            if cnt < 1:
               s += s_pop
            else:
                cnt -=1
        else:
            cnt +=1
    return s[::-1]
print(stack_remove_star("leet**cod*e"))

# sol2
def stack_remove_star2(strs):
    st = []
    for c in strs:
        if c != "*":
           st.append(c)
        else:
            st.pop()
    return ''.join(st)
print(stack_remove_star("abce****"))