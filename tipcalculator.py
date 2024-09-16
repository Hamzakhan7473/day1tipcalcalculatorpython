#creating a tip calculator 

print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("what was the percentage tip would u like to give ? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
Total_tip_amount = bill * tip_as_percent
total_bill = bill + Total_tip_amount
bill_per_person = total_bill / people 
final_amount  = round(bill_per_person, 2)
print(f"each person should pay: ${final_amount}")