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
    