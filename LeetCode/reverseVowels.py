# nếu dùng nối chuỗi + sẽ chậm và tốn bộ nhớ vì sau mỗi lần lặp nó sẽ 
# chép lại toàn bộ dữ liệu cũ và nối với chuỗi mới
# tránh dùng khi số lượng chuỗi nhiều đặc biệt là trong vòng lặp
def Reveser(s):
    nguyenam =['e','u','a','i','o']
    stack_nguyenam = []
    for i in range(len(s)):
        if s[i].lower() in nguyenam:
            stack_nguyenam.append(s[i])
    new_s =''
    for i in range (len(s)):
        if s[i].lower() in nguyenam:
            new_s += stack_nguyenam.pop()
        else:
            new_s += s[i]
    return new_s
print(Reveser("hello aim"))
print(Reveser("Ronaldo Messi"))

# dùng join sẽ tốt hơn trong trường hợp này, nó tạo list từ s, sau đó hiệu chỉnh các phần tử mong muốn
# cuối cùng là join các phần tử lại thành str
def Reveser(s):
    nguyenam =['e','u','a','i','o']
    stack_nguyenam = []
    for i in range(len(s)):
        if s[i].lower() in nguyenam:
            stack_nguyenam.append(s[i])
    new_s = list(s)
    for i in range (len(s)):
        if s[i].lower() in nguyenam:
            new_s[i] = stack_nguyenam.pop()
    return ''.join(new_s)
print(Reveser("hello aim"))
print(Reveser("Ronaldo Messi"))
