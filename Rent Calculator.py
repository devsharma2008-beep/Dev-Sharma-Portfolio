#Rent Calculator

#Inputs we need from the user 
#Total rent
#Total food ordered for snacks
#Electricity Bill
#Persons living in room/flat

#Output
#Total amount you've to pay is

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the total amount of food ordered = "))
electricity_bill = int(input("Enter the total amount of electricity bill = "))
persons = int(input("Enter the number of persons living in room/flat = "))

output = (rent + food + electricity_bill)//persons

print("Each person will pay = ", output)