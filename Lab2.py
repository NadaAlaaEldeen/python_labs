"""
1- Given a list of numbers, create a function that
 returns a list where all similar adjacent
 elements have been reduced to a single element,
You may create a new list or modify the passed in list
"""
def unique(my_arr):
    my_unique_arr=[]
    for element in my_arr:
        if element not in my_unique_arr:
            my_unique_arr.append(element)     
    return my_unique_arr

# my_arr=[1,3,4,5,7,1,2,1,1,3] 
# print(unique(my_arr))    

"""
2-Given 2 strings, a and b, return a string of the form:
(a-front + b-front) + (a-back +b-back)
"""
# def front_back(a, b):
#     a_mid = (len(a) + 1) // 2
#     b_mid = (len(b) + 1) // 2
#     return a[:a_mid] + b[:b_mid] + a[a_mid:] + b[b_mid:]

# a = "abcdef"
# b = "123456"
# result = front_back(a, b)
# print(result)

"""
3- Write a Python function that takes a sequence of numbers and determines
whether all the numbers are different from each other.
E.X. [1,5,7,9] -> True
[2,4,5,5,7,9] -> False
"""
def is_unique(my_arr):
    unique_arr=unique(my_arr) 
    if unique_arr==my_arr: 
      return True
    else:
      return False  
# print(is_unique([1,5,7,9]))
# print(is_unique([2,4,5,5,7,9] ))

"""
4- Given unordered list, sort it using algorithm bubble sort
( read about bubble sort and try to implement it)
"""


def bubble_sort(arr):
    for i in range (0,len(arr)):
       for j in range(0,len(arr)-i-1):
        if arr[j]>arr[j+1]:
         arr[j+1],arr[j]=arr[j],arr[j+1]
    print (arr)

# bubble_sort([6,1,9,2,5,3])

"""
5- Gusses game
● Your game generates a random number and gives only 10 tries for the user to
guess that number.
● Get a user input and compare it with the random number
● Display a hit message to the user in case the use number is smaller or bigger of
the random number
● If the user type number is out of range(100), display a message that is not allowed
and don’t count this as try.
● If user type a number that has been entered before, display a hint message and
don’t count this as try
● In case the user entered a correct number within the 10 tries, display a
congratulations message and let your application guess another random number
with the remain number of tries
● If the user finishes all his tries, display a message to ask him if he wants to play
again or not

"""
import random
def play_guess_game():
    print('Guessing game\n')

    random_number = random.randint(1, 100)
    arr = []
    # print(random_number,arr)
    number = input('Guess the correct number.....\n')
    if not number:
        print('Empty input...\n')
    elif not number.isdigit():
        print("Input is not an integer")
    elif int(number) > 100:
        print('You entered an invalid number...\n')
    elif int(number) == random_number:
        print('Congratulations! You guessed the correct number.\n')
    else:
        trail = 1
        arr.append(int(number))
        while int(number) != random_number and trail < 10 :
            if int(number) > random_number:
                print('You Entered number is bigger than the right num')
            elif int(number) < random_number:
                print('You Entered number is less than the right num')   
            number = input(f'Wrong guess! You have {10-trail} attempts left. Guess another number...\n')
            if not number:
                print('Empty input...\n')
            elif not number.isdigit():
                print("Input is not an integer")
            elif int(number) in arr:
                print('You entered the same guess before...')
            else:
                trail += 1
                arr.append(int(number))
        if trail == 10:
            print(f'You have exhausted all attempts. The correct number was {random_number}.')
        else:
            print(f'Congratulations! You guessed the correct number in {trail} attempt(s).')
            

# play_guess_game()
