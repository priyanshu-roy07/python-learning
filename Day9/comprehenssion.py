#NOTE- compression [expression for item in iterable]
#[ WHAT I WANT  |  FOR EACH ITEM  |  FROM WHERE ]
#expression → what should be added to the list?
#item → what is the loop variable?
#iterable → what are we looping over?


#LIST COMPREHENSION
"""n = []
for i in range(1, 6):
    n.append(2*i)
print(n)"""

#n = [2*i for i in range(1, 6)]
#print(n)

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""even_numbers = []
for i in numbers:
    if i%2 == 0:
        even_numbers.append(i)
print(even_numbers)"""

#even_numbers = [i for i in numbers if i%2==0]
#print(even_numbers)

#odd_squares = [i**2 for i in numbers if i%2!=0]
#print(odd_squares)


#DICTIONARY COMPREHENSSION

#numbers = [1, 2, 3, 4, 5]
#squares = {}

#for i in numbers:
#    squares[i] = i**2
#print(squares)

#squares = {i : i**2 for i in numbers}
#print(squares)


#SET COMPREHENSSION

#numbers = [1, 2, 2, 3, 3, 4, 5]
#set = {i for i in numbers}
#print(set)

