#square formation
'''import turtle

def square():
    my_turtle  = turtle.Turtle()
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    #hello

square()'''

#to give individual value of the variable 'data'
'''data = "XBOX 60| 150 | New "
product = data[:data.index('|')]

print(product)'''

#for finding another | after the first |
'''print(data.index("|", 10))
print(data[13])

cost = data[1+data.find("|"): data.find("|", 10)]
print(cost)'''
'''groceries = ['pineapple', 'corn', 'pad',]
for i in groceries:
    print('I want to buy ', i)
print(groceries[1][3])'''
'''spliting = "I-want-to-split-this"
print(spliting.split("t"))'''
#for split or breaking values of a string
'''detail = data.split('|')
print(detail)
product = detail[0]
price = detail[1]
condition = detail[-1] 
print(product)
print(price)
print(condition)'''
#for appending/adding numbers
'''numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
print(list(range(10)))'''


#for circle_ square
'''import turtle


my_turtle = turtle.Turtle()
my_turtle.speed(-5)

def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)
for n in range(100):
    square(100, 90)
    my_turtle.right(10)

'''

#code for printing and reversing numbers into a list
'''numbers = list()

numbers.append(1)
for number in range(2, 21):
        numbers.append(number)
        reverse_numbers =numbers[::-1]

print(reverse_numbers)'''

#making and accessing profiles using dictionaries
'''profile = {
        'hikma': {
                "number": "08054657825",
                "gmail": "hikma@gmail.com",
                "hobbies": ['singing', 'reading', 'exploring', 'having fun']
        },

        'kauthar': {
                "number": "080336677889",
                "gmail": "kauthar@gmail.com",
                "hobbies": "browsing, playing, eating, having fun"
        }
}
print(profile['hikma']['hobbies'][-1])'''

#True or False
'''if False:
        print("hello")
elif True:
       print("slice")
else: print("stupid")'''

#calculating pay based on hours of work
'''hours = float(input("Hours:"))
Rate = float(input("Rate:"))
pay = hours* Rate
if hours>=40:
        pay += pay* 0.25
elif hours <= 10:
        pay-= pay * 0.10
print( "the total pay is ", pay, " naira.")'''

'''twenties = 1
thirties = 5
count  = 0
for number in range(twenties, thirties):
        count += number
        print(count)
'''
#function that adds all numbers in a list and returns them.
'''def sum_list(my_list):
    count = 0
    for number in my_list:
        count = count + number

    return count
   


assert sum_list([1, 2, 3]) ==6'''

#while loop for deceding numbers from 100 to 0 and blastoff
'''x= 100
while x>= 0:
    print(x)
    if x == 0:
            print("blastoff!!")
    x -= 1'''
        
#function that sums up the two numbers in its argument
'''def sum_two(number_1, number_2):
        return number_1 + number_2
        

print(sum_two(100, -2))'''

#function that squres a number
'''def square_number(number):
        return number**2
print(square_number(4))'''

# function for even numbers 
'''def is_even(number):
        if number% 2 == 0:
               return True
        else:
              return False

is_even(474637)'''

#another funtion even numbers
'''def is_even(number):
        return number % 2== 0

print(is_even(56))
'''
#function to check the length if a string
'''def string_length(my_string):
        return len(my_string)
or 
def string_length(my_string):
        count = 0
        for i in my_string:
                count += 1
        return count
print(string_length("hello me and you"))'''

#function to return the last letter of a string
'''def last_letter(my_string):
    return my_string[-1]

print(last_letter("hello there you"))'''

#larger number
'''def bigger_guy(num1, num2):
        if num1 > num2:
                return num1
        else:
                return num2

print(bigger_guy("g", "g"))'''

#biggest number 
'''def biggest_guy(num1, num2, num3):
        if num1> num2 and num1> num3:
                return num1
        elif num2> num1 and num2> num3:
                return num2
        elif num3> num1 and num3> num2:
                return num3

print(biggest_guy(1, 2, 3))

or 
#using function bugger_guy
def biggest_guy(num1, num2, num3)
        return bigger_guy(bigger_guy(num1, num2), num3)'''

#function using dict to check info
'''def race_position(choice):
    return  {"Usain": 1, "Hikmah": 2, "Qazi": 3}[choice]
            
print(race_position("Usain"))'''


#rock, paper, scssors code (though I don't understand some shit here)
'''import random


human_choice = ''
computer_choice = ''
HUMAN_SCORE = 0
COMPUTER_SCORE = 0

def choice_to_number(choice):
        return {"rock": 0, "paper": 1, "scissors": 2}[choice]
def number_to_choice(number):
        return {0: "rock", 1: "paper", 2:"scissors"}[number]
def random_computer_choice():
        return random.choice(["rock", "paper", "scissors"])
def choice_result(human_choice, computer_choice):
        global COMPUTER_SCORE
        global HUMAN_SCORE

        human_number = choice_to_number(human_choice)
        computer_number = choice_to_number(computer_choice)

        if (human_number - computer_number) % 3 == 1:
                COMPUTER_SCORE = COMPUTER_SCORE +1
        elif human_number == computer_number:
                print("tie")
        else:
                HUMAN_SCORE = HUMAN_SCORE + 1 '''



#squaring a list
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
square_number = []
for number in numbers:
        square_number.append(number** 2)

print(square_number)'''

'''max_count = 0
for number in [1, 34, 444323, 45445, 4567]:
        if number > max_count:
                max_count = number
                print("before :", number, max_count)
 
        print(number)'''


'''import pytz
import panda
import requests
import bs4'''

#calendar function 
'''import calendar
import datetime
import time
import pytz
hour_delta = datetime.timedelta(hours= 10)
datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone("Africa/Lagos"))
print(datetime_pacific)'''
'''for tz in pytz.all_timezones:
        print(tz)'''


'''today = datetime.date.today()#today's date
birthday = datetime.date(1997, 7, 15)
tdelta =datetime.timedelta(days = 10)
print(today.strftime('%B, %d, %Y'))#shows the date the written month, not numerical, %B=month, %d=day, %Y=year'''
'''print(today + tdelta)#adds 10 days to the current date
print(today.month)#today's month
time = datetime.time(7,2,20,15)#shows the timein hr,min,sec & microsec
print(time)
#datetime.date(Y, M, D)
#datetime.time(h,m,s,ms)
#datetime.datetime(Y,M,D,h,m,s,ms)
datetime.datetime.now()#unlike datetime.datetime(), this doesnt require argument to know the current'''
'''print(time.localtime())#for check int location tiime'''
'''print(calendar.weekheader(3)) #=days of the week, 3= len of their names
print(calendar.firstweekday()) #=in python, the 1st weekday is monday so = 0
print(calendar.month(2020,3, w=3, l=2)) #= 2020= year, 3= months, w=3 = width of the weekday name, l= len of space btw lines
print(calendar.monthcalendar(2020, 3))#matrix 2020= year, 3= month
print(calendar.calendar(2020, w= 3, l=2, c= 11, m= 3))


day_of_the_week = calendar.weekday(2020, 3, 17)
print(day_of_the_week)
#code for showing the friday of the month
count = 0
friday = 6
for frid in calendar.month(2020, 3):
        if calendar.weekday(2020, 3, 6)== 4:
                print('Today ', friday,"th of march" ' is a Friday')
                friday += 7
                count+= 7
                if count == 28:
                        break

is_leap = calendar.isleap(2020)#for checking if it is a leap year(True or False)
print(is_leap)

is_a_leap_year = calendar.leapdays(2000, 2020)# for checking the numbers for no of leap years in ranging btw, so =5
'''



#shorter for loop
'''names= [1,2,3,4]
print([person for person in names])'''

'''movie_and_rating = { "acotar": 9, "clickd": 6, "i owe you one": 3, "shopaholic":2}
l= []
for movie in movie_and_rating:
    if movie_and_rating[movie] > 5:
        l.append(movie)
print(l)


print([movie for movie in movie_and_rating if movie_and_rating[movie]>5])'''
#regular expression
'''import re
text= "a random string"
pattern= re.compile("[fraf]")#=a , ie the first match
result = pattern.search(text)
print(result)


text= "a random string"
pattern= re.compile("[a-zA-Z0-9]+")#=random, + one or than
result = pattern.search(text)
print(result)

import re
text= " hikmayousuph@gmail.com a random string. kauthar@gmail.com is my sis email"
pattern= re.compile("[a-zA-Z0-9,-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")#for email address
result = pattern.search(text)
print(result)


text= " hikmayousuph@gmail.com a random string. kauthar@gmail.com is my sis email"
pattern= re.compile("[a-zA-Z0-9,-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")#for email address
result = pattern.findall(text)#unlike compile, findall finds more than one 
print(result)'''


#counter module for counting a string occurence in form of a dict
'''import collections
from collections import Counter
c = Counter("djcbsjddhuhnxndueudh")
print(c)'''
 
#zip function
'''list1 = [1,2,3,4,5]
list2 = ['one','two', 'three', 'four', 'five']'''

'''zipped = list(zip(list1, list2))#can be tuple(zip()), dict(), and list()
print(zipped)'''
'''unzipped = list( zip(*zipped))#* for unzipping
print(unzipped)'''

'''for (l1, l2) in zip(list1, list2):
    print(l1), print(l2)'''

'''items = ['Apple', 'Banana','Orange']
counts = [3, 6, 4]
prices = [0.99, 0.25, 0.50]
#e.g I brought 3 appples at 0.99, I brought 6 banana at 0.25
sentences = []
for (item, count, price) in zip(items, counts, prices):
	sentence = 'I brought ' + str(count) + ' ' +item.lower()+ 's at ' + str(price)
	sentences.append(sentence)

print(sentences)'''

#palindrome
'''word = input("enter a word:")
if word ==word[::-1]:
    print("it is a palindrome")
else:
	print("not a palindrome")'''

#sets
#they are a dictionary with only keys
'''my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set)
my_list = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6]
print(set(my_list))#will show only one occurence of the list of values'''

#list comprehension
#more concise and shorter than if and for loop
'''a_list = [letter for letter in 'word']
print(a_list)
lst = [x**2 for x in range(1, 11)]
print(lst)
even = [number for number in range(11) if number%2 ==0]
print(even)

