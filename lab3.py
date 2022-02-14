'''
lab 3
list and set
'''
#3.1
str_list = ["a" , "d" , "e" , "b" , "c"]
str_list.sort()
print(str_list)

#3.2
str_list.append("f")
print(str_list)

#3.3
str_list.remove("d")
print(str_list)

#3.4
print(str_list[2])

#3.5, THIS IS WHERE WE STOPPED AS A CLASS. AND I KEPT GOING
my_list = ("a" , "123" , "'123'" , "'b'" , "B" , "'False'" , "False" , "None" , "'None'")
print(len(my_list))

#3.6 my way 
import re
My_sentence = ("This is my third Python lab")
res = len(re.findall(r'\w+', My_sentence))
print("the number of words in this string are :" + str(res))

#3.6 class way 
print( len("this is my third python lab.".split()))

#3.7
num_list = [12, 32, 43, 35]
num_list.sort()
print(num_list[0])
print(num_list[-1])

#3.8
game_board = [ [0,0,0], [0,0,0], [0,0,0]]
print(game_board)
game_board[1][1] = -1
print(game_board)