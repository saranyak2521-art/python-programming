name = input("Enter customer name: ")
mobile = input("Enter mobile number: ")
cost = float(input("Enter cost of purchase: "))

discount = 0.1 * cost if cost > 1000 else 0.05 * cost
total = cost - discount

print("Customer Name:", name)
print("Mobile Number:", mobile)
print("Purchase Cost:", cost)
print("Discount:", discount)
print("Total Amount to be paid:", total)
