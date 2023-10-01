# Problem:
# Write a Python program that takes a list of numbers as input and returns a new list containing only the even numbers from the original list.
#Soltuion 
## My code 
# i_list = int(input("Enter list of number "))
# n_list=[]
# for i in  list(str(i_list)):
#     if int(i)%2==0:
#         n_list.append(i)
    
# print(n_list)
# Better version 
# numbers = input("Enter a list of numbers (space-separated): ").split()
# even_numbers = []

# for num in numbers:
#     if int(num) % 2 == 0:
#         even_numbers.append(int(num))

# print(even_numbers)

###########################################################
# Write a Python program that takes a string as input and prints the reverse of that string.
# def reverse_string(input_string):
#     reversed_string = input_string[::-1]
#     return reversed_string

# # Test the function
# input_str = input("Enter a string: ")
# reversed_str = reverse_string(input_str)
# print("Reversed string:", reversed_str)

# Write a Python program that takes a string as input and checks whether it is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

# str = str(input("Enter word "))

# def ch_p(str):
#     if str == str[::-1]:
#         return print(True)
#     return False


# ch_p(str)


# Intermediate Question:
# Write a Python program that takes a list of strings as input and returns a new list containing only the strings that are palindromes. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

# For example, if the input list is ['radar', 'level', 'hello', 'madam', 'python'], the program should return ['radar', 'level', 'madam'].

# li = str(input("Enter list separeted by , ").lower).split(",")

# def li_p(li):
#     n_l=[ ]
#     for i in li:
#         if i == i[::-1]:
#             n_l.append(i)
#         else:
#             continue
#     return n_l

# li_p(li)

# li = [4, 2, -1, 5, -3, 2, -5, 1]

# def closest_to_zero(numbers):
#     closest_pair = None
#     closest_diff = float('inf')  # Initialize with a large value

#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             curr_sum = numbers[i] + numbers[j]
#             curr_diff = abs(curr_sum)

#             if curr_diff < closest_diff:
#                 closest_diff = curr_diff
#                 closest_pair = (numbers[i], numbers[j])

#     return closest_pair

# # Test the function
# input_list = [4, 2, -1, 5, -3, 2, -5, 1]
# result = closest_to_zero(input_list)
# print("Closest Pair:", result)

# Write a Python program to find the largest element in a list.

# li = ["list",'hello','world','chicken','pig']

# largest= ""
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if len(li[i]) >len(li[j]):
#             largest=li[i]
#         else:
#             largest=li[j]
# print(largest)

# Write a Python program to remove duplicates from a list.


# def remove_duplicates(input_list):
#     unique_list = []
#     for item in input_list:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list

# # Test the function
# my_list = [1, 2, 3, 3, 4, 5, 5, 6]
# result = remove_duplicates(my_list)
# print("List without duplicates:", result)
# Write a Python program to find the index of an element in a list.


# Write a Python program to sort a list in ascending order.
# def bubble_sort(input_list):
#     n = len(input_list)

#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if input_list[j] > input_list[j + 1]:
#                 input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

#     return input_list

# # Test the function
# my_list = [4, 2, 1, 5, 3]
# result = bubble_sort(my_list)
# print("Sorted list:", result)

# Write a Python program to count the number of vowels in a string.
# string = "stiiiiiiring"
# count =0
# for i in range(len(string)):
#     if string[i] in ["i","a","o","u","e"]:
#         count = count +1
    
# print(count)

# Write a Python program to generate a Fibonacci sequence.

# j = 10
# i=2
# list = []
# while i <=j:
#     list.append((i-1)+(i-2))
#     i=i+1

# print(list)

# Write a Python program to remove all occurrences of a specific element from a list.
# li = [4, 2, 1, 5, 3,4,5,6,4,4]
# rm=4
# n_li=[]
# for item in li:
#     if rm != item:
#         n_li.append(item)

# print(n_li)

# Write a Python program to find the common elements between two lists.
# li = [4,2,3,4,6]
# li2=[2,4,5,6,7]
# cli=[]
# for i in li:
#     for j in li2:
#         if i == j:
#             cli.append(i)


# print(cli)



# Write a Python program to check if a string is a pangram.
# string ="The  brown fox jumps over the lazy dog."

# for letter in alphabet:
#     if letter in string:
#         continue
#     else:
#         print(False)
#         break

# Write a Python program to find the first non-repeating character in a string.
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# string ="Hello World"
# n_l=[]
# for i in range(len(string)):
#     if string[i] not in n_l:
#         n_l.append(string[i])
    
# print(n_l)

# Write a Python program to find the mode of a list of numbers.

# def find_mode(numbers):
#     counts = {}
#     max_count = 0
#     modes = []

#     # Count the occurrences of each number in the list
#     for num in numbers:
#         if num in counts:
#             counts[num] += 1
#         else:
#             counts[num] = 1

#         if counts[num] > max_count:
#             max_count = counts[num]

#     # Find the numbers with the highest count (mode)
#     for num, count in counts.items():
#         if count == max_count:
#             modes.append(num)

#     return modes

# # Test the function
# number_list = [1, 2, 3, 2, 4, 3, 2, 5]
# mode_list = find_mode(number_list)
# print("Mode(s) of the list:", mode_list)


# Write a program to check if a given string is a palindrome or not (without using slicing).
# def is_palindrome(string):
#     # Remove spaces and convert to lowercase
#     string = string.replace(" ", "").lower()

#     # Check if the string is a palindrome
#     left = 0
#     right = len(string) - 1
#     print(right,left)
#     while left < right:
#         if string[left] != string[right]:
#             return False
#         left += 1
#         right -= 1
#         print(left,right)

#     return True

# # Test the function
# word = input("Enter a word: ")
# if is_palindrome(word):
#     print(word, "is a palindrome.")
# else:
#     print(word, "is not a palindrome.")

# Write a program to find the maximum difference between two elements in a list.

# list1=[2,3,4,5]
# list2=[2,3,4,8]
# max_diff=0
# for i in list1:
#     for j in list2:
#         if max_diff<i-j:
#             max_diff=i-j

# print(max_diff)

# Write a program to reverse a string without using any built-in functions or slicing.
# string ="Hello World"
# counter =len(string)-1
# new_word=""
# while counter >= 0:
#     new_word = new_word+string[counter]
#     counter-=1

# print(new_word)
# Write a program to merge two sorted lists into a single sorted list.
# list1=[5,3,1,2]
# list2=[9,77,8,9,0]
# list1.extend(list2)

# list1.sort()
# print(list1)

# Write a program to check if two strings are anagrams or not.

# word1 = "listen"
# word2 = "silent"

# # Convert the words to lowercase for case-insensitive comparison
# word1 = word1.lower()
# word2 = word2.lower()

# # Check if the lengths of the words are the same
# if len(word1) != len(word2):
#     print(False)
# else:
#     # Create dictionaries to store character frequencies
#     freq1 = {}
#     freq2 = {}

#     # Count the frequency of characters in word1
#     for char in word1:
#         freq1[char] = freq1.get(char, 0) + 1

#     # Count the frequency of characters in word2
#     for char in word2:
#         freq2[char] = freq2.get(char, 0) + 1

#     # Compare the character frequencies
#     if freq1 == freq2:
#         print(True)
#     else:
#         print(False)
# Write a program to convert a decimal number to binary.
# def decimal_to_binary(decimal):
#     binary = ""

#     while decimal > 0:
#         binary = str(decimal % 2) + binary
#         decimal //= 2

#     return binary

# # Example usage
# decimal_number = 15
# binary_number = decimal_to_binary(decimal_number)
# print("Binary representation of", decimal_number, "is:", binary_number)

# Write a program to find the sum of all even numbers in a list.
# list=[2,1,3,4,5,6,7,8,8,9,90,0,10]
# sum=0
# for i in list:
#     if i %2==0:
#         sum=sum+i

# print(sum)

# Write a program to generate a random password of a given length.
# Special_Characters=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
# Alphabets= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# password=""
# list =[Special_Characters,Alphabets,Numbers]
# while len(password) !=9:
#     index = random.choice([0,1,2])
#     if list[index] == Special_Characters:
#         if password not in Special_Characters:
#             password=password+Special_Characters[random.randint(0,len(Special_Characters)-1)]
#     elif list[index]==Alphabets:
#         password = password+Alphabets[random.randint(0,len(Alphabets)-1)]
#     else:
#         password= password+Numbers[random.randint(0,len(Numbers)-1)]
    
# print(password)
# Write a Python function to find all prime numbers in a given range.
# Numbers=[1,2,3,4,5,6,7,8,9]
# for i in range(0,20):
#     if i >1:
#         for j in Numbers:
#             if i%j==0 and j == 1 or j==i:
#                 print(i,"is prime")
#             else:
#                 print(i,"is not prime")
# Write a Python program to find the second largest number in a list.

# def find_second_largest(numbers):
#     if len(numbers) < 2:
#         return "List should have at least two numbers"

#     largest = max(numbers[0], numbers[1])
#     second_largest = min(numbers[0], numbers[1])

#     for num in numbers[2:]:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest:
#             second_largest = num

#     return second_largest

# # Example usage
# num_list = [5, 9, 3, 8, 2, 7, 10]
# second_largest_num = find_second_largest(num_list)
# print("Second largest number:", second_largest_num)
# Write a Python program to find the most frequent element in a list.

# list = [1,2,2,2]

# c_freq =0
# freq_num=""
# for i in range(len(list)):
#     n_freq=0
#     for j in range(i+1,len(list)):
#         a =list[i]
#         b=list[j]
#         if a==b:
#             n_freq =n_freq+1
#     if n_freq>c_freq:
#         c_freq=n_freq
#         freq_num=list[i]

# print(freq_num)
        
    
#1. Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.

# def max(num1,num2):
#     if num1 > num2:
#         return print(num1)
#     elif num2 > num1:
#         return (print(num2))
#     else:
#         return print("They are equal")
    
# max(19,8)


# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
# def max_of_three(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
            


# max_of_three(4,8,5)

# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".

# def translate(string):
#     string= string.lower()
#     vowel = ["a","e","i","o","u"]
#     new_sting= ""
#     for i in range(len(string)):
#         if string[i] in vowel:
#             new_sting= new_sting + string[i]
#         elif string[i]==" ":
#             new_sting = new_sting + " "
#         else:
#             new_sting = new_sting+ string[i] +"o"+ string[i]
#     return print(new_sting)

# translate("Hello World")

# def reverse(string):
#     right = len(string)
#     re_string = ""
#     for i in range(1,len(string)):
#         re_string= re_string+ string[right-i]
#     return print (re_string)
#     # return print(string [::-1])

# reverse("heelllooo woeled  fjkd cf ")

# Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.

# list1 =["1","2","3","4","a"]
# list2 =["145","83","5","6","afdf"]

# def overlapping(list1,list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return print(True)
#     return print(False)

# overlapping(list1,list2)


#  Write a function max_in_list() that takes a list of numbers and returns the largest one.

# list=["1","2","87","5","6","7"]
# def max_in_list(list):
#     largerest = "0"
#     for i in range(len(list)):
#         if list[i]> largerest:
#             largerest = list[i]
#         else:
#             largerest=largerest
#     return print(largerest)

# max_in_list(list)

# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.

# import sys
# list_words=[]
# for i in range(1,len(sys.argv)):
#     list_words.append(sys.argv[i])
# def map_char_word(list):
#     len_char = []
#     for i in list:
#         len_char.append(len(i))
#     return print(len_char)
# map_char_word(list_words)
    

# Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.


# word_list = ["apple", "banana", "cherry", "datee", "fig"]

# def filter_by(char_n,char_list):
#     new_list =[]
#     for word in char_list :
#         if len(word) > char_n:
#             new_list.append(word )
#     return print(new_list)

# filter_by(5,word_list)
# "99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows:

# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall.

# The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero. Your task here is write a Python program capable of generating all the verses of the song

# songs = """Bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall."""

# vese = 99
# while vese > 0 :
#     print(f"""
#     Bottles of beer on the wall, {vese} bottles of beer.
#     Take one down, pass it around, {vese-1} bottles of beer on the wall.
# """)
#     vese= vese-1

# Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. That is, write a function translate() that takes a list of English words and returns a list of Swedish words.

# s_dict={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
# string= "merry christmas and happy new year"
# string = string.split(" ")
# def greet_translate(dict,string):
#     new_gretting=""
#     for i in string:
#         new_gretting = new_gretting +" "+ dict[i]
#     return print(new_gretting)

# greet_translate(s_dict,string)

