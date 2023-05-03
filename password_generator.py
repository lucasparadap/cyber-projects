'''
Write a password generator in Python. 
'''

#Initialization
import random
password = ""
user_strength = input("How strong would you like your password? Choose weak, moderate, or strong? ")

#ascii Libraries depending upon desired strength
ascii_3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
         '1','2','3','4','5','6','7','8','9','0','#','!','$','^','*',':','&','-']
ascii_2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
         '1','2','3','4','5','6','7','8','9','0']
ascii_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         '1','2','3','4','5','6','7','8','9','0']

#Function returns desired strength in standardized format
def strength(user_strength):
    if user_strength.lower() == "weak":
        return "W"
    elif user_strength.lower() == "moderate":
        return "M"
    elif user_strength.lower() == "strong":
        return "S"

desired_strength = strength(user_strength)

#Function takes desired_strength and generates a password corresponding in strength
def password(desired_strength):
    if desired_strength == "W":
         return ''.join(random.choices(ascii_1, k=8))
    elif desired_strength == "M":
        return ''.join(random.choices(ascii_2, k=10))
    elif desired_strength == "S":
        return ''.join(random.choices(ascii_3, k=12))

mypass = (password(desired_strength))

if __name__ == '__main__':
    print(mypass)      
    