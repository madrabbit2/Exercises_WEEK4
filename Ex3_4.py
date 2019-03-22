#Ex 3_4
#program is an update of program addVAT.py
#Chancellor reduced the VAT percent to 15%
#program adVAT.py is: 

# program addVAT.py
# program prompts the user to input an amount (in £), adds VAT at 17.5%,
# then outputs the amount including VAT
# written by P.K., Dec 1, 2004

print "This program will prompt you to input the ex VAT amount (in £), then"
print "output the total amount inclusive of VAT"
print
VATPERCENT = 15

amount = input("Enter the ex VAT amount in £: ")
vat = amount*VATPERCENT/100.0
totalAmount = amount + vat
print
print "The total amount (inclusive of VAT) is £", totalAmount
print
