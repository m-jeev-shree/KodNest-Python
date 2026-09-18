#selection statements
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("You got A grade.")
elif marks >= 80:
    print("You got B grade.")
elif marks >= 70:
    print("You got C grade.")
else:
    print("You got D grade.")
#nested-if

free_tonight = input("Are you free tonight? (yes/no): ") == "yes"
friends_avail = input("Are your friends available? (yes/no): ") == "yes"
if free_tonight:
    if friends_avail:
        print("Let's go out for dinner.")
    else:
        print("Let's stay in and watch a movie.")
else:
    print("Let's stay in and watch a movie.")

#match - case statement
day = input("Enter the day of the week: ")
match day:
    case "Monday":
        print("It's the start of the work week.")
    case "Tuesday":
        print("It's the second day of the work week.")
    case "Wednesday":
        print("It's the middle of the work week.")
    case "Thursday":
        print("It's the fourth day of the work week.")
    case "Friday":
        print("It's the last day of the work week.")
    case "Saturday":
        print("It's the weekend!")
    case "Sunday":
        print("It's the weekend!")
    case _:
        print("Invalid day of the week.")

month = int(input("Enter the month (1-12): "))
match month:
    case 3|4|5:
        print("Summer season.")
    case 6|7|8:
        print("Autumn season.")
    case 9|10|11:
        print("Winter season.")
    case 12|1|2:
        print("Spring season.")
    case _:
        print("Invalid month.")