"""
1-Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.

"""
# first=input("Enter Your first name: \n")
# last=input("Enter Your last name:\n")
# print (last +" "+ first)


def reverse(text):
    my_string = ''.join(text[::-1])
    return(my_string)

# print (str(reverse(last))+" "+str(reverse(first)))
  
"""
2-Write a Python program that accepts an integer (n) and computes the value of
n+nn+nnn.
"""
# n=input("Enter a Number:\n")
# print (int(n)+int(n+n)+int(n+n+n))

"""
3- Write a Python program to print the following here document.
Sample string :
"""
"""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""
"""
4- Write a Python program to
 get the volume of a sphere with radius 6.
"""
# import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume

# sphere_volume(6)
       
"""
5- Write a Python program that will accept the base and height of a triangle and compute
the area.
"""       
def triangle_area(base, height):
    area = 0.5 * base * height
    return area

# print(triangle_area(4, 5))  

"""
6- Write a Python program to construct the following pattern, using a nested for loop.
Search about method
end=””
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""


# for i in range(5):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()


# for i in range(4, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

"""
7- Write a Python program that accepts 
a word from the user and reverse it
"""
# word=input("Enter any string\n")
# print(reverse(word))

"""
8- Write a Python program that prints all 
the numbers from 0 to 6 except 3 and 6.
"""
# for i in range(7):
#     if i == 3 or i == 6:
#         continue
#     print(i)


"""
9-Write a Python program to get 
the Fibonacci series between 0 to 50

"""
# a, b = 0, 1
# while b <= 50:
#     print(b, end=' ')
#     a, b = b, a + b

"""
10- Write a Python program that accepts a string
 and calculate the number of digits and
letters.
"""
# def count_digits_letters(string):
#     num_digits = 0
#     num_letters = 0

#     for char in string:
#         if char.isdigit():
#             num_digits += 1
#         elif char.isalpha():
#             num_letters += 1

#     return num_digits, num_letters

# print(count_digits_letters("Hello1234World45"))