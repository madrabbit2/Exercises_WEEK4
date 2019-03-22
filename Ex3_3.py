#Ex3_3
#program that asks user to enter cost of a restaurant bill calculates the tip
#at 15% and outputs total cost of the bill as well as the tip

print("input the cost of restaurant bill and this program will output the total cost including your tip at 15%")
restaurant_bill=input("Enter the cost of the restaurant bill: £")
tip=restaurant_bill*15/100
restaurant_bill_total=restaurant_bill+tip
print"total cost = ", restaurant_bill_total
print"cost of tip at 15%: ", tip
