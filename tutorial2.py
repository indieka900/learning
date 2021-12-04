def area(radius):
    area = 22/7 * radius ** 2
    print(area)
area(14)
for letters in "Hello":
    print(letters)
for i in range(20,0,-1):
    print(i,end=' ')
for j in range(10,20):
    if j%2 !=0  and j%3 !=0 and j%5 !=0 and j%7 !=0:
        print(j)
for i in range(5):
    for j in range(i+1):
        print("!",end='')
    print(" ")
def currancy(Ksh):
    dollars = Ksh / 102.2
    Euros = Ksh / 116.3
    Ush = Ksh / 0.55
    Tsh = Ksh / 0.2
    print('In dollars is {:.2f} in Euros is  {:.2f} in Ugandan shilling is {:.2f} in Tanzanian shilling is {:.2f}'.format(dollars,Euros,Ush,Tsh))
currancy(200)
currancy(1872)