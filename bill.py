print("Welcome to the Tip Calculator!")
Bill=input("What was the total bill? $")
tip=input("What percentage tip would you like to give? 10, 12, or 15? ")
people=input("How many people to split the bill? ")
tip_as_percent=int(tip)/100
total_tip=tip_as_percent*float(Bill)
total_bill=float(Bill)+total_tip
bill_per_person=total_bill/int(people)
final_amount="{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

