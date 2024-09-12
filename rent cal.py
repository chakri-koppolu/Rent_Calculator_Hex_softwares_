total_rent = int (input("Enter the total rent =" ))
food = int(input("Enter the total food charges =" ))
water = int(input("Enter the total water charges =" ))
elec_Charges = int(input("Enter the total elcetricity charges" ))
person = int(input("Enter the number of persxon living in room = "))
total_Amount = (total_rent + food + water + elec_Charges)//person
print("Each person will pay =", total_Amount)