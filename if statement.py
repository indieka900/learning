#name = 'joseph ali'
#print(name.capitalize())
#last_name = name[7:10]
#reversed_name = name[::2]
#print(first_name)
#print(reversed_name)
#website = "http://youtube.com"
#slice = slice(3,-4)
#print(name[slice])
age = int(input("Enter your old"))
if age>= 20:
    years=int(input("You are an adult"))
    if years>=100:
        print('You are older than expected '+ str(years)+' are many')
elif age<=0:
    print("Still in a womb")
else:
    print('you are still a child')
