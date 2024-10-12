def compress(chars):
    left, right = 0,0
    cnt = 0
    list_chars=[]
    while right < len(chars):
        if chars[right] != chars[left]:
            list_chars.append(chars[left])
            if cnt >=2:
                list_chars.append(cnt)
            left = right
            cnt =0
        if(right == len(chars)-1 and cnt >=1):
            cnt +=1
            list_chars.append(chars[right])
            list_chars.append(cnt)
        cnt+=1
        right +=1
    s="".join(str(item) for item in list_chars)
    return list(s)
print(compress("aabbccc"))