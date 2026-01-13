from decimal import Decimal, ROUND_HALF_UP

def d(x):
    return Decimal(x).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

width = 60

print("-Taxi Calculator-".center(width))
print("--Uber/Bolt net income calculator (Tax 20%, Fleet 5%)--".center(width))
print("-Mert Bahar-".center(width))
print("")
print("")

#INPUTS
uber_gross = Decimal(input("UBER Earnings: "))
uber_cash = Decimal(input("UBER Cash: "))

bolt_gross = Decimal(input("BOLT Earnings: "))
bolt_cash = Decimal(input("BOLT Cash: "))

# TOTAL GROSS
gross_sum = uber_gross + bolt_gross

# TAXES (from gross)
dph = gross_sum * Decimal("0.20")
fleet = gross_sum * Decimal("0.05")

after_tax = gross_sum - (dph + fleet)

# CASH
total_cash = uber_cash + bolt_cash
bank_sum = after_tax - total_cash

# RATIOS
uber_ratio = uber_gross / gross_sum
bolt_ratio = bolt_gross / gross_sum

uber_bank = bank_sum * uber_ratio
bolt_bank = bank_sum * bolt_ratio

# OUTPUT
print("\n--- RESULTS ---")
print(f"UBER amount transferred to bank: {d(uber_bank)} CZK")
print(f"BOLT amount transferred to bank: {d(bolt_bank)} CZK")
print(f"Total amount transferred to bank: {d(bank_sum)} CZK")

input("\nPress ENTER to exit...")