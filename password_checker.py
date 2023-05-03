'''
Python Program to determine how strong a password is.
Will output...

This file imports a sister local file called password_generator.py -- 
It is initialized to run autonomously -- if desired to reference password_generator:
### --- uncomment lines 7 and 8 -- then comment out line 20
'''

# Creates usable ascii list for password strength evaluator
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['#','!','$','^','*',':','&','-']

# Intializes password for script
# password = password_generator.mypass
password = input("Input your passcode: ")
print("\n")

# Separates password into iterable list
pass_chars = []
pass_chars = [i for i in password]

# Func: Is the length weak, moderate, or strong?
def length(password):
    length = ''
    if 8 >= len(password):
        length = 'wL'
    elif 12 > len(password) >= 8:
        length = 'mL'
    else:
        length = 'sL'
    return length

# Func: Is the complexity weak, moderate, or strong? 
def complexity(password):
    complexity = ''
    label_code = []
    for i in pass_chars:
            if i in lower:
                label_code.append("l")
            if i in numbers:
                label_code.append("n")
            if i in upper:
                label_code.append("u")
            if i in symbols:
                label_code.append("s")      
    for x in label_code:
        if 'l' in label_code and'n' in label_code and 'u' in label_code and 's' in label_code:
            complexity = 'sC'
        elif 'l' in label_code and'n' in label_code and 'u' in label_code:
            complexity = 'mC'
        else:
            complexity = 'wC'
    return complexity

# Func: Is the password on the top-10-mil list
def known(password):
    known = ''
    topten = []
    with open ('10-million-password-list-top-1000000.txt') as file:
        topten = [line.strip('\n') for line in file]
    if password in topten:
        known = 'wmK'
    else:
        known = 'sK'
    file.close()
    return known

length = length(password)
complexity = complexity(password)
known = known(password)

# Main function -- used to calculate Password Strength
# There are 5 options for strength:
#       1) Weak -- Change Now (wL + wC + wmK) (3)
#       2) Moderately Weak -- Should Change When Possible (permutations btwn ^ v) (4-5)
#       3) Moderate -- Not weak but not strong, recommend changing if desired (mC + mL + sK) (6)
#       4) Moderately Strong -- Not necessary to change, but could be stronger (permutations btwn ^ v) (7-8)
#       5) Strong -- No need to change (sL + sC + sK) (9)
#
#   w = 1
#   m = 2
#   s = 3
#   wm = 1

# Converts individual metrics to overall integer score
def numeric_init(metric): 
    score = 0
    if metric == 'wL' or metric == 'wC' or metric == 'wmK':
        score += 1
    elif metric == 'mL' or metric == 'mC':
        score += 2
    if metric == 'sL' or metric == 'sC' or metric == 'sK':
        score += 3
    return score


# Converts integer score to verbal score
def cal_strength(password):
    numeric_init(length)
    numeric_init(complexity)
    numeric_init(known)
    score = numeric_init(length) + numeric_init(complexity) + numeric_init(known)   

    if score == 3:
        strength = 'weak'
    elif score == 4 or score == 5:
        strength = 'moderately weak'
    elif score == 6:  
        strength = 'moderate'  
    elif score == 7 or score == 8:
        strength = 'moderately strong'
    elif score == 9:  
        strength = 'strong' 
    return strength


strength = cal_strength(password)

# Provides advice based on strength and offers to create a new password if score is below moderately strong
def advice(strength):
    if strength == 'weak':
        print("Password is considered weak. It is advisable to change it immediately")
    elif strength == 'moderately weak':
        print("Password is considered moderately-weak. It is advisable to change at the soonest possible convenience")
    elif strength == 'moderate':
        print("Password is considered moderate in strength. It is recommended to change when possible, but not an immediate issue")
    elif strength == 'weak':
        print("Password is considered moderately-strong. It is not necessary to change your password, though it could be stronger")
    else:
        print("Password is considered strong. It is not necessary to change it.")

    if strength == 'weak' or strength == 'moderately weak'or strength == 'moderate':
        print("\n")  
        newpass = input('Want the password generator to make you a new password? Type yes or no: ')
        newpass = newpass.lower().strip()
        if newpass == 'yes':
            import password_generator
            print('OK! Your new password is: ' + password_generator.mypass)

    print("\n")    
    print("Thank you for using the password_checker script!")
    print("\n") 

# Runs script
advice(strength)
