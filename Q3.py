#Grocery store billing
count=0
avg=0
tot=0
while True:
    itm_price=int(input("Enter item price: "))
    tot+=itm_price
    if itm_price==0:
        break
    count=count+1
    avg=tot/count
print("The total bill amount is : ", tot)
print("The total item count is  : ", count)
print("The average price of an item is   : ", avg)

