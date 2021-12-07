card= input("Enter the credit card number: ")

while True: 
    val = int(input("Enter the number of digits to show: ")) 
    card = str(card)
    dots=""
    i=16-val
    while i > 0 :
        dots=dots+'*'
        i=i-1
        
    print(dots + card[-val:])