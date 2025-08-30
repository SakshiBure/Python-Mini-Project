#Inputs we Need from user 
#Total Food Ordered for Snacking 
#Electricity units spend
#charge per unit
#Persons living in room/flate
#Outputs 
#Total amt you've to pay is 


rent = int(input("Enter Your Hostel/Flat Rent ="))
food= int(input("Enter the amount of food order = "))
electricity_spend = int(input("Enter the total of Electricity spend ="))
charge_per_unit = int(input("Enter charge per unit = "))
persons =int(input("Enter the no of persons in Room/Flate = "))

total_bill =electricity_spend * charge_per_unit
output=(food +rent +total_bill) /persons
print("Each person will pay:",output)