is_leap_year = False
   
input_year = int(input())

if ((input_year // 100) % 4) != 0:
    is_leap_year = True
    print(input_year, "- not a leap year")
    exit()
if (input_year % 4) == 0:
    is_leap_year = True
    print(input_year, "- leap year")
elif (input_year % 400) == 0:
    is_leap_year = True
    print(input_year, "- leap year")

else:
    is_leap_year = False
    print(input_year, "- not a leap year")
