''' 
lab 5
'''

#3.1 
alien_color= "yellow"

if alien_color== "green":
    print("you have earned 5 points")
    
#3.2
if alien_color == "green":
    print("you have earned 5 points")
else:
    print("you have earned 10 points")
    
#3.3
favorite_foods = ["burgers", "skittles", "peas"]

if "burgers" in favorite_foods:
    print("I really like burgers")

if "skittles" in favorite_foods:
    print("I really like skittles")
    
if "strawberries" in favorite_foods:
    print("I really like strawberries")
    
#3.4
age = 55

if age <10:
    print("kid")
    
elif age >10 and age <20:
    print("teenager")
    
else:
    print("adult")
    
if age>=65:
    print("elder")