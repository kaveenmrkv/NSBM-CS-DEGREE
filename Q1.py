#Get the Highest value over 10 days
days=int(input("Enter days count :"))
maximum=0
while days>0:
    sale_amt=float(input("Enter Sale Amount :"))
    days=days-1
    if sale_amt>maximum:
        maximum=sale_amt
    else:
        continue
print("The Maximum Sales amount is : ", maximum)
        
