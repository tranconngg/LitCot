# # # # # # # # # # # # # # # # # # # def greetings(name, greeting="hello"):
# # # # # # # # # # # # # # # # # # #     print(f"{greeting}, {name}!")
# # # # # # # # # # # # # # # # # # # greetings("Hello")
# # # # # # # # # # # # # # # # # # # greetings("Goobye","Ngủ Ngon")

# # # # # # # # # # # # # # # # # # # def test(*args):
# # # # # # # # # # # # # # # # # # #     for i in args:
# # # # # # # # # # # # # # # # # # #         print(str(i) + " ", end="")
# # # # # # # # # # # # # # # # # # # test(1,2,3,4,5,8,9)
# # # # # # # # # # # # # # # # # # # print("\n")
# # # # # # # # # # # # # # # # # # # def test2(**kwargs):
# # # # # # # # # # # # # # # # # # #         for key, value in kwargs.items():
# # # # # # # # # # # # # # # # # # #              print(f"Quả {key} có giá là {value}")

# # # # # # # # # # # # # # # # # # # test2(Tao=30, Buoi=40, Le=50)      
# # # # # # # # # # # # # # # # # # # print(test2)
# # # # # # # # # # # # # # # # # # from functools import reduce       
# # # # # # # # # # # # # # # # # # words = ["apple", "banana", "cherry", "date"]
# # # # # # # # # # # # # # # # # # tongds = reduce(lambda a,b: a if len(a) > len(b) else b, words)
# # # # # # # # # # # # # # # # # # print(tongds)
# # # # # # # # # # # # # # # # # # # 15
# # # # # # # # # # # # # # # # lowerr = ["Táo", "đào", "lê"]
# # # # # # # # # # # # # # # # Upperr = [item.upper() for item in lowerr]
# # # # # # # # # # # # # # # # print(Upperr)

# # # # # # # # # # # # # # # # sole = [1,3,5,7,9]
# # # # # # # # # # # # # # # # sochan=[int(item) +1 for item in sole]
# # # # # # # # # # # # # # # # print(sochan)

# # # # # # # # # # # # # # # # binhphuong = [int(item)**2 for item in range(11)]
# # # # # # # # # # # # # # # # print(binhphuong)

# # # # # # # # # # # # # # # # matran4x4 = [[i+j for j in range(5)]for i in range(5)]
# # # # # # # # # # # # # # # # print(matran4x4)

# # # # # # # # # # # # # # # from functools import reduce
# # # # # # # # # # # # # # # # sv_dict = {"Nam":10, "Công":9, "Thái": 6, "Hưng":10}
# # # # # # # # # # # # # # # # tb=sum(sv_dict.values())/len(sv_dict)
# # # # # # # # # # # # # # # # # tb = reduce(lambda x,y: (x+y), sv_dict.values())
# # # # # # # # # # # # # # # # # print(tb/len(sv_dict)
# # # # # # # # # # # # # # # # print(tb)
# # # # # # # # # # # # # # # my_dict = {"City":{"Hà Nội": 30, "Lạng Sơn":12, "Hải Phòng":19, "Nghệ An":37}, "Món ăn":{"Hà Nội":"Phở", "Lạng Sơn":"Lợn quay", "Hải Phòng":"Bánh đa cua", "Nghệ An":"Cháo Lươn"}}
# # # # # # # # # # # # # # # City=my_dict.get("City")
# # # # # # # # # # # # # # # Monan =my_dict.get("Món ăn")
# # # # # # # # # # # # # # # print(City)
# # # # # # # # # # # # # # # print(Monan)
# # # # # # # # # # # # # # # for city, number_plate in zip(City.keys(), City.values()):
# # # # # # # # # # # # # # #     specialty = Monan.get(city, "Không có món ăn đặc sản")
# # # # # # # # # # # # # # #     print(f"Thành phố {city} có biển số {number_plate} và món ăn đặc sản là {specialty}.")
# # # # # # # # # # # # # # # # city_tren20 ={key:val for key,val in city_dict.items() if val > 20}

# # # # # # # # # # # # # # # # print(city_tren20)
# # # # # # # # # # # # # # # # try:
# # # # # # # # # # # # # # # #     info_Ls= city_dict.get("Lạng Sn")
# # # # # # # # # # # # # # # #     print(info_Ls)
# # # # # # # # # # # # # # # # except:
# # # # # # # # # # # # # # # #     print("không có tỉnh này")
# # # # # # # # # # # # # # # # for key,val in city_dict.items():
# # # # # # # # # # # # # # # #     if key == "Lạng Sơn":
# # # # # # # # # # # # # # # #         city_dict[key]=120
# # # # # # # # # # # # # # # #         print("Đã thay đổi thành công!")
# # # # # # # # # # # # # # # # print(city_dict)
# # # # # # # # # # # # # # # # # while True:
# # # # # # # # # # # # # # # #     inp =  input("Mời nhập tên thành phố: ")
# # # # # # # # # # # # # # # #     if inp in city_dict:
# # # # # # # # # # # # # # # #         print (city_dict[inp])
# # # # # # # # # # # # # # # #     elif inp == "exit":
# # # # # # # # # # # # # # # #         break
# # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # #         print("Không có thành phố này!", "Mời bạn nhập lại nhé")
    
    
# # # # # # # # # # # # # # import sys

# # # # # # # # # # # # # # # Tạo danh sách bình phương của các số từ 1 đến 1 triệu
# # # # # # # # # # # # # # squares_list = [x * x for x in range(1, 1000001)]

# # # # # # # # # # # # # # # Tạo generator bình phương của các số từ 1 đến 1 triệu
# # # # # # # # # # # # # # squares_gen = (x * x for x in range(1, 1000001))

# # # # # # # # # # # # # # # Kiểm tra kích thước của danh sách và generator
# # # # # # # # # # # # # # print(f"Kích thước của list: {sys.getsizeof(squares_list)} bytes")
# # # # # # # # # # # # # # print(f"Kích thước của generator: {sys.getsizeof(squares_gen)} bytes")
# # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # n_list = [1,2,3,4,5,6,7,8,10,2,4,2,5,6,8,4,3,6,8,6,6,5,3,5,6]
# # # # # # # # # # # # # demnguoc = (x for x in range(1000000, -1, -1))
# # # # # # # # # # # # # for chan in demnguoc:
# # # # # # # # # # # # #     print(chan, end=" ")
# # # # # # # # # # # # # print(f"Kích thước của list: {sys.getsizeof(demnguoc)} byte")
# # # # # # # # # # # # def count_ele(tpl, ele):
# # # # # # # # # # # #     return tpl.count(ele)
# # # # # # # # # # # # tp = (1,2,3,4,5,2,2)
# # # # # # # # # # # # print(count_ele(tp,2))

# # # # # # # # # # # # list_tp=tp
# # # # # # # # # # # # print(list_tp[::-1])
# # # # # # # # # # # l1 = [1,2,3,4]
# # # # # # # # # # # l2 = [3,4,5]
# # # # # # # # # # # def chung(l1,l2):
# # # # # # # # # # #     return list(set(l1) ^ set(l2))
# # # # # # # # # # # print(chung(l1,l2))
# # # # # # # # # # def count_words(s):
# # # # # # # # # #     w_dict={}
# # # # # # # # # #     for char in s:
# # # # # # # # # #         if char in w_dict:
# # # # # # # # # #             w_dict[char]=int(w_dict.get(char)) + 1
# # # # # # # # # #         else:
# # # # # # # # # #             w_dict[char]=1
# # # # # # # # # #     return w_dict
# # # # # # # # # # print(count_words("tranvancong"))

# # # # # # # # # # def sort_byValue(dic):
# # # # # # # # # #     return dict(sorted(dic.items(), key=lambda item:item[1]))

# # # # # # # # # # print(sort_byValue(count_words("tranvancong")))
# # # # # # # # # def paladome(s):
# # # # # # # # #     return s.replace(" ", "_")
# # # # # # # # # print(paladome("tran van cong"))
# # # # # # # # def cal(s):
# # # # # # # #     chucai=sum(c.isalpha() for c in s)
# # # # # # # #     chuso=sum(c.isdigit() for c in s)
# # # # # # # #     ktdb=len(s)-chucai-chuso
# # # # # # # #     return chucai,chuso,ktdb
# # # # # # # # print(cal("Hello123!"))
# # # # # # # import csv
# # # # # # # data=[["GuuChicken","Giảm Giá","https://abcxyz"],["Guu","Giảm Giá","https://abcxkz"]]
# # # # # # # with open("data.csv", 'a', newline='', encoding='utf-8') as file:
# # # # # # #     # for f in file:
# # # # # # #     #     print(f.strip())
# # # # # # #     writer=csv.writer(file)
# # # # # # #     # writer.writerow(["Name","Promotion","store_url"])
# # # # # # #     writer.writerows(data)

# # # # # # def binary_search(a,target):
# # # # # #     left, right = 0, len(a)-1
# # # # # #     mid = left + (left - right)//2
# # # # # #     while left<=right:
# # # # # #         if a[mid]==target:
# # # # # #             return True
# # # # # #         elif a[mid]<target:
# # # # # #             # Nếu giá trị tại arr[mid] nhỏ hơn target,
# # # # # #             # điều này có nghĩa là target không thể nằm ở nửa bên trái của danh sách (bao gồm cả mid),
# # # # # #             # vì danh sách đã được sắp xếp.
# # # # # #             # nên khi thiết lập lại left sẽ bỏ qua mid luôn
# # # # # #             left = mid +1 
# # # # # #         else:
# # # # # #             right = mid -1
# # # # # #     return -1
# # # # # # print(binary_search([1,2,3,4,5,6,7,8,9],0))
# # # # # def selection_sort(a):
# # # # #     for i in range(len(a)):
# # # # #         for j in range(i+1, len(a)):
# # # # #             if a[j]< a[i]:
# # # # #               a[i], a[j]= a[j], a[i]
# # # # #     return a
# # # # # print(selection_sort([1,5,2,7,9,4]))

# # # # def quickSort(arr, low, high):
# # # #    if (low < high):
# # # #        pi = partition(arr, low, high)
# # # #     quickSort(arr, low, pi - 1)
# # # #     quickSort(arr, pi + 1, high)
# # # def insertion_sort(a):
# # #     if len(a) == 0 or 1:
# # #         return a
# # #     for i in range(1,len(a)):
# # #         j = i-1
# # #         for j in range(j,0):
# # #             if a[i]<a[j]:
# # #                 a[j], a[i]=a[i], a[j]
# # #     return a
# # # print(insertion_sort([1,6,2,8,4,5]))


# # def mergeAlternately(word1, word2):
# #         """
# #         :type word1: str
# #         :type word2: str
# #         :rtype: str
# #         """
# #         min_length = min(len(word1),len(word2))
# #         merge =''
# #         for i in range(0,min_length):
# #             merge += word1[i]
# #             merge += word2[i]

# #         merge +=word1[min_length:]
# #         merge +=word2[min_length:]
# #         return merge

# # print(mergeAlternately("abcd","xyz"))
# import string
# solution1
# def gcdOfStrings(str1, str2):
#         """
#         :type str1: str
#         :type str2: str
#         :rtype: str
#         """
#         res=""
#         # if (set(str1) | set(str2)) != len(str1):
#         #     return 
#         if len(str1) >= len(str2):
#             for char in range(len(str2)):
#                 if str1[char] != str2[char]:
#                     return res
#             cnt = str1.count(str2)
#             if cnt == 0:
#                 return res
#             elif cnt >= 2:
#                 return str2
#             else:
#                 if str1.startswith(str2):
#                     return str1[len(str2):]

#         elif len(str1) <len(str2):
#             for char in range(len(str1)):
#                 if str2[char] != str2[char]:
#                     return res
#             cnt = str2.count(str1)
#             if cnt == 0:
#                 return res
#             elif cnt >= 2:
#                 return str1
#             else:
#                 if str2.startswith(str1):
#                     return str2[len(str1):]
# print(gcdOfStrings("ABABAB","ABAB"))
# print(set("abcdef")|set("abc"))
# from math import gcd
# def gcdOfStrings(str1, str2):
#         if str1 + str2 != str2 + str1:
#             return ''
#         n = gcd(len(str1), len(str2))
#         return str1[:n]
# print(gcdOfStrings("ABC","ABCABC"))
# print(gcdOfStrings("ABABAB","ABAB"))

# def flowerPlace(arr, n):
#     if n==0:
#         return True
#     leng = len(arr)
#     for i in range(leng):
#         if arr[i]==0 and (i==0 or arr[i-1]==0) and (i==leng-1 or arr[i+1]==0):
#             arr[i] = 1
#             n -=1
#             if n <=0:
#                 return True
# print(flowerPlace([1,0,1,0,1,0,1],0))
# import string
# # nếu dùng nối chuỗi + sẽ chậm và tốn bộ nhớ vì sau mỗi lần lặp nó sẽ 
# # chép lại toàn bộ dữ liệu cũ và nối với chuỗi mới
# # tránh dùng khi số lượng chuỗi nhiều đặc biệt là trong vòng lặp
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

# # dùng join sẽ tốt hơn 
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
# words = ["Messi", "is", "goat"]
# print(' '.join(words))

# sentence = "I love programming in Python"
# sen_list=sentence.split(" ")
# sen_list = sen_list[::-1]
# print(' '.join(sen_list))
# # print(sentence[::-1])

# def tansuattu(a):
#     dict_a ={}
#     for char in a:
#         if char in dict_a:
#              dict_a[char]+=1
#         else:
#             dict_a[char]=1
#     return dict_a
# print(tansuattu("hello"))
# def doancon_lonnhat(a, k):
#         # if k <= 1:  
#         # return 0

#         product = 1
#         left = 0
#         count = 0
#         list_t=[]

#         for right in range(len(a)):
#             product *= a[right] 

#             while product >= k and left <= right:
#                 product /= a[left]
#                 left += 1
# # xuống tới đây thì đoạn con đã thoả mãn
# #  khi vòng while trên đã xử lý trường hợp k thoả mãn
#             count += right - left + 1
#             for i in range(left,right+1):
#                 list_t.append([a[i:right+1]])

#         return list_t
# print(doancon_lonnhat([10,5,2,6],100))
            
# def subarraysDivByK(nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         left = 0
#         max_length = 0
#         sum = 0
#         list_t =[]
#         for right in range(0,len(nums)):
#             sum += nums[right]
#             while (sum % k != 0) and left <= right:
#                 sum -= nums[left]
#                 left+=1
#             max_length = max_length + (right-left +1)
#             for i in range(left, right+1):
#                 list_t.append([nums[i:right+1]])
#         return list_t

# print(subarraysDivByK([-5,5,3,2],5))
# def reverseWords(s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         s=s.strip()
#         list_s = s.split()
#         return ' '.join(list_s[::-1])
# print(reverseWords("    hello world"))

# ===========SOLUTION 1==================
# def moveZeroes(nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         cnt = 0
#         for i in range(0,len(nums)-2):
#             if nums[i] == 0:
#                 zero = nums.pop(i)
#                 cnt +=1
#         list_zero = [0] * cnt
#         return nums + list_zero

# print(moveZeroes([0,1,0,3,12]))

# ========== solution 2=========
#  def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         right=1
#         left=0
#         for right in range(0,len(nums)):
#             if nums[right] != 0:
#                 nums[left],nums[right]=nums[right],nums[left]
#                 left +=1
            
#         return nums
        
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
# def check_maxsub(a, target):
#     left = 0
#     current_sum = 0
#     max_length = 0

#     for right in range(len(a)):
#         current_sum += a[right]

#         # Khi tổng lớn hơn target, di chuyển left để giảm tổng
#         while current_sum > target:
#             current_sum -= a[left]
#             left += 1
#  abc axbhc

#         # Cập nhật độ dài của dãy con
#         max_length = max(max_length, right - left + 1)

#     return max_length
# print(check_maxsub([1, 2, 3, 4, 5],8))
# set_=list("hello")
# print(set_)
# if "h" in set_:
#         print("có")


# def isSubsequence(s, t):
#     i,j =0,0
#     while j < len(s) and i < len(t):
#             if (s[j]==t[i]):
#                 j+=1
#             i+=1
#     return j == len(s)


# print(isSubsequence("ole","hellol"))
# def maxOperations(nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         nums=sorted(nums)
#         left=0
#         right = len(nums)-1
#         cnt =0
#         while left <right:
#             if nums[left]+nums[right] ==k:
#                 left +=1
#                 right -=1
#                 cnt +=1
#             elif nums[left]+nums[right] <k:
#                 left +=1
#             else:
#                 right -=1
#         return cnt


# print(maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4],2))
# p = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
# def product_of_array_excepted_self(a):
#     tich_left = [1] * len(a)
#     tich_right = [1] * len(a)
#     answer = [1] * len(a)
#     #  hoặc tạo list rỗng rồi sau append cũng được
#     left_tich=1
#     for i in range(len(a)):
#         # lượt đầu tiên i = 0 thì không có phần tử nào đứng trước phần tử i = 0 của mảng nums
#         # nên mảng tich_left sẽ lấy giá trị left_tich ban đầu là 1,
#         # left_tich thứ i là tích của tất cả các phần tử đằng sau phần tử i của mảng nums (tích cộng dồn cho tới phần tử i-1 của mảng nums)

#         # append tích của phần tử tại vòng lặp trước, phần tử i tại tich_left sẽ lưu tích dồn đến i - 1 của nums(vòng lặp trước)
#         tich_left[i]=left_tich

#         # xong rồi mới tính tích cho phần tử tại vòng lặp này rồi sang vòng lặp sau mới append
#         left_tich*=a[i] 
#         # nhân xong để đó qua vòng lặp mới thì mới cho vào mảng,
#         # đảm bảo mảng chứa tích của các phần tử trước i
#     right_tich = 1
#     for i in range(len(a)-1, -1, -1):
#         tich_right[i] = right_tich
#         right_tich *= a[i]
    
#     for i in range(len(a)):
#         # con trỏ để mảng tich_right chạy ngược
#         # k = len(a) - i -1 
#         answer[i] = tich_left[i] * tich_right[i]
#     return answer
# print(product_of_array_excepted_self([1,2,3,4]))

# def increasingTriplet(self, nums):
#         if len(nums) < 3:
#            return False
#         # khởi tạo chúng bằng dương vc
#         min = float('inf')
#         tb = float('inf')
    
#         for num in nums:
#             if num <= min:
#                 min = num
#             elif num <= tb: 
#                 min = num
#             else:
#                 return True

#         return False
# def compress(chars):
#     left, right = 0,0
#     cnt = 0
#     list_chars=[]
#     while right < len(chars):
#         if chars[right] != chars[left]:
#             list_chars.append(chars[left])
#             if cnt >=2:
#                 list_chars.append(cnt)
#             left = right
#             cnt =0
#         if(right == len(chars)-1 and cnt >=1):
#             cnt +=1
#             list_chars.append(chars[right])
#             list_chars.append(cnt)
#         cnt+=1
#         right +=1
#     s="".join(str(item) for item in list_chars)
#     return list(s)
# print(compress("aabbccc"))

# def maxArea(height):
#         left=0
#         right = len(height)-1
#         dientich, chieucao, chieurong= 0,0,0
#         max_dientich=0
#         while left < right:
#             chieucao  = min(height[left], height[right])
#             chieurong = right - left
#             dientich = chieucao * chieurong
#             if dientich > max_dientich:
#                   max_dientich = dientich
#             if height[left] < height[right]:
#                   left += 1
#             else:
#                   right -=1
#         return max_dientich
# print(maxArea([1,8,6,2,5,4,8,3,7]))

# def findMaxAverage(nums, k):
#        left, right = 0,0
#        sum = 0
#        max_tb = -99999999999999
#        while right < len(nums):
#               sum+=nums[right]
#               if right -left +1 == k:
#                     tb = sum / k
#                     if tb > max_tb:
#                            max_tb=tb
#                     sum -= nums[left]
#                     left +=1
#               right +=1
#        return max_tb
# print(findMaxAverage([-1,-2,-3,-4,-6,-8],5))
# def maxVowels(s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         left, right = 0,0
#         max_vowels = 0
#         cnt = 0
#         vowels = ['u','e','o','a','i']
#         while right < len(s):
#                 if s[right] in vowels:
#                         cnt +=1
#                 if right - left +1 == k:
#                         if cnt > max_vowels:
#                                 max_vowels = cnt
#                         if s[left] in vowels:
#                                 cnt -=1
#                         left +=1

#                 right +=1
#         return max_vowels
# print(maxVowels("aeiou",2))
                
# def findDifference(nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[List[int]]
#         """
#         set_s1=set(nums1)
#         set_s2=set(nums2)
#         return [list(set_s1-set_s2),list(set_s2-set_s1)]
# print(findDifference([1,2,3,3],[1,1,2,2]))
        
# def uniqueOccurrences(arr):
#         dict_arr={}
#         for i in range(len(arr)):
#             if arr[i] not in dict_arr:
#                   dict_arr[arr[i]]=1
#             else:
#                 keyy=dict_arr.get(arr[i])
#                 keyy +=1
#                 dict_arr[arr[i]]=keyy

#         val_unique = dict_arr.values()
#         n = len(val_unique)
#         return n == len(set(val_unique))
# print(uniqueOccurrences([1,2]))
        
# sol1
# def stack_remove_star(strs):
#     st_str=list(strs)
#     s=''
#     cnt =0
#     for _ in range(len(strs)):
#         s_pop=st_str.pop()
#         if s_pop != '*':
#             if cnt < 1:
#                s += s_pop
#             else:
#                 cnt -=1
#         else:
#             cnt +=1
#     return s[::-1]
# print(stack_remove_star("leet**cod*e"))

# # sol2
# def stack_remove_star2(strs):
#     st = []
#     for c in strs:
#         if c != "*":
#            st.append(c)
#         else:
#             st.pop()
#     return ''.join(st)
# print(stack_remove_star("abce****"))

# def va_cham_tieu_hanh_tinh(a):
#     st = []
#     for c in a:
#         if len(st) >= 1:
#             check = st[-1]
#         else:
#            check = 99999999999999
#         if c == check or len(st)==0:
#             st.append(c)
#         elif c > check:
#             if abs(c) == abs(check):
#                 st.pop()
#             elif c*check > 0:
#                 st.append(c)
#             else:
#                 st.pop()
#                 st.append(c)
#         elif c < check:
#             if abs(c) == abs(check):
#                 st.pop()
#             elif abs(c) > abs(check):
#                 st.pop()
#             elif c*check >0:
#                 st.append(c)
#     return st
# print(va_cham_tieu_hanh_tinh([10,2,-5]))

# chua tao file

# def largestAltitude(gain):
#       max_prefix=-9999999999
#       prefix = 0
#       for i in range(len(gain)):
#             if prefix >max_prefix:
#                   max_prefix=prefix
#             prefix += gain[i]
            
#       return max_prefix
# print(largestAltitude([-5,1,5,0,-7]))
def pivotIndex(nums):
        sumleft=[0]*len(nums)
        sumright=[0]*len(nums)
        left, right=0,0
        for i in range(len(nums)):
                sumleft[i]=left
                left += nums[i]
        for i in range(len(nums)-1, -1, -1):
                sumright[i]=right
                right += nums[i]
        for i in range(len(sumleft)):
                if sumleft[i] == sumright[i]:
                        return i
        return -1

print(pivotIndex([1,7,3,6,5,6]))
            
