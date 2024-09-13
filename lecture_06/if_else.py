# if, else, elif
# if
## if condition(TRUE or FALSE):
##     (executed only if condition == TRUE)
##     code block

age = int(input("How old are you?: "))
if age >= 18:
    print("You are an adult!")
# print('end of the demo')

# if..else
## if condition:
##     code block (condition == TRUE)
## else:
##     code block (condition == FALSE)

if age >= 18:
    print("You are an adult!")
else:
    print("You are too young. Grow up a little bit!")

# if..elif..else
## if condition_1:
##     code block (condition == TRUE)
## elif condition_2:
##     code block (condition == TRUE)
## ....
## ....
## elif condition_n:
##     code block (condition == TRUE)
## else:
##     code block (condition == FALSE)

if age < 18:
    print("You are a child!")
elif 18 <= age < 35:
    print("You are youth!")
else:
    print("You are an adult!")

# and
is_student = True

if 18 <= age < 35 and is_student:
    print("Young student")
elif 18 <= age < 35 and not is_student:
    print("Young but not a student")

# or
has_experience = False

if age >= 25 or has_experience:
    print("You are an adult or you have an experience")
else:
    print("You are not an adult and you don't have experience")

# mixed 'and', 'or'

if (age >= 18 and is_student) or (has_experience and age < 30):
    print("You are either an adult student or have experience and are under 30.")
else:
    print("You don't meet any of the specified conditions.")

if (age >= 18 or is_student) and (has_experience or age < 30):
    print("You are either an adult student or have experience and are under 30.")
else:
    print("You don't meet any of the specified conditions.")

### NESTED IF
if age >= 18:
    if age < 30:
        if is_student:
            print("Adult student")
        elif has_experience:
            print("You have experience")
else:
    print("Yuo don't meet any of the specified conditions")
