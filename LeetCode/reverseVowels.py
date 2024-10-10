# nếu dùng nối chuỗi + sẽ chậm và tốn bộ nhớ vì sau mỗi lần lặp nó sẽ 
# chép lại toàn bộ dữ liệu cũ và nối với chuỗi mới
# tránh dùng khi số lượng chuỗi nhiều đặc biệt là trong vòng lặp
# def Reveser(s):
#     nguyenam =['e','u','a','i','o']
#     stack_nguyenam = []
#     for i in range(len(s)):
#         if s[i].lower() in nguyenam:
#             stack_nguyenam.append(s[i])
#     new_s =''
#     for i in range (len(s)):
#         if s[i].lower() in nguyenam:
#             new_s += stack_nguyenam.pop()
#         else:
#             new_s += s[i]
#     return new_s
# print(Reveser("hello aim"))
# print(Reveser("Ronaldo Messi"))

# # dùng join sẽ tốt hơn trong trường hợp này, nó tạo list từ s, sau đó hiệu chỉnh các phần tử mong muốn
# # cuối cùng là join các phần tử lại thành str
# def Reveser(s):
#     nguyenam =['e','u','a','i','o']
#     stack_nguyenam = []
#     for i in range(len(s)):
#         if s[i].lower() in nguyenam:
#             stack_nguyenam.append(s[i])
#     new_s = list(s)
#     for i in range (len(s)):
#         if s[i].lower() in nguyenam:
#             new_s[i] = stack_nguyenam.pop()
#     return ''.join(new_s)
# print(Reveser("hello aim"))
# print(Reveser("Ronaldo Messi"))
# ===================== Hai con trỏ =====================
# Tìm tất cả các cặp số trong mảng có tổng bằng một giá trị
# Cho một mảng đã được sắp xếp(tự xắp xếp ê), tìm hai số trong mảng có tổng bằng một giá trị cụ thể

# def find_num(a, target):
#     left = 0
#     right = len(a)-1
#     a=sorted(a)
#     list_cap =[]
#     while left < right:
#         if a[left] + a[right] == target:
#             list_cap.append([a[left],a[right]])
#             left+=1
#         elif a[left] + a[right] < target:
#             left +=1
#         else:
#             right -=1

#     conver_tople=map(lambda x:tuple(x),list_cap)
#     return set(conver_tople)
# print(find_num([1,5,2,6,4,0,0,3,6,2,5,8,4],10))
# check palindrome
# def check_palindrome(a):
#     left = 0
#     right = len(a)-1
#     while left < right:
#         if a[left] != a[right]:
#             return False
#         else:
#             left +=1
#             right -=1
#     return True

# print(check_palindrome("123454321"))
# check độ dài chuỗi con nhỏ hơn hoặc bằng một giá trị
def check_maxsub(a, target):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(a)):
        current_sum += a[right]

        # Khi tổng lớn hơn target, di chuyển left để giảm tổng
        while current_sum > target:
            current_sum -= a[left]
            left += 1

        # Cập nhật độ dài của dãy con
        max_length = max(max_length, right - left + 1)

    return max_length
print(check_maxsub([1, 2, 3, 4, 5],8))