'''#write a code for add list members and return the sum of the list
def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total'''
'''#define list and include 10 integer items to the list ,the sum only odd values ..verify is the sum is even or odd..if the sum is even then check the number is perfect number or not and if the number is odd then find the reverse number of that number.
def is_perfect_number(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
def reverse_number(n):
    return int(str(n)[::-1])
numbers = [12, 7, 5, 8, 3, 10, 15, 22, 9, 4]
odd_sum = sum(num for num in numbers if num % 2 != 0)
print("Sum of odd numbers:", odd_sum)
if odd_sum % 2 == 0:
    print("The sum is even.")
    if is_perfect_number(odd_sum):
        print(f"{odd_sum} is a perfect number.")
    else:
        print(f"{odd_sum} is not a perfect number.")
else:
    print("The sum is odd.")
    reversed_sum = reverse_number(odd_sum)
    print("Reversed sum:", reversed_sum)'''
'''#prepare a power supply bill,with unit cost 3.5..total units used by the colony 5000 units ,total houses in the colony 24...without AC the houses are 13,with AC 11...the units used AC houses 200+,and unit for the NON-AC houses below 200...Write code for Approximate for 5000 units,and generate thew bill values for all the houses according to above scenario.
total_units = 5000
total_houses = 24
units_per_house = total_units / total_houses
unit_cost = 3.5
bills = {}
for house_number in range(1, total_houses + 1):
    if house_number <= 11:  # AC houses
        units_used = 200 + (house_number * 10)  # Example increment for AC houses
    else:  # Non-AC houses
        units_used = 150 - (house_number * 5)  # Example decrement for Non-AC houses
    bill_amount = units_used * unit_cost
    bills[f'House {house_number}'] = {
        'Units Used': units_used,
        'Bill Amount': round(bill_amount, 2)
    }
for house, details in bills.items():
    print(f"{house}: Units Used = {details['Units Used']}, Bill Amount = ${details['Bill Amount']}")'''
#A retail store wants to automate its billing process using a python program.As a programmer,you are asked to develop a console-based application that assists the cashier in generating customer bills.the program should accept the customers name,the number of items purchased,and the price of each item.ift should calculate the total bill amount and apply a discount based on the total purchase value(for example,higher discounts for higher bill amounts).the program must also calculate tax on the discounted amount and display the final payable bill clearly.the system should allow the cashier top generate bills for multiple customers until they choose to stop the program.
def calculate_discount(total_amount):
    if total_amount > 500:
        return total_amount * 0.10  # 10% discount
    elif total_amount > 200:
        return total_amount * 0.05  # 5% discount
    else:
        return 0  # No discount
def calculate_tax(amount):
    tax_rate = 0.07  # 7% tax
    return amount * tax_rate
while True:
    customer_name = input("Enter customer name: ")
    num_items = int(input("Enter number of items purchased: "))
    total_amount = 0
    for i in range(num_items):
        item_price = float(input(f"Enter price of item {i + 1}: "))
        total_amount += item_price
    discount = calculate_discount(total_amount)
    discounted_amount = total_amount - discount
    tax = calculate_tax(discounted_amount)
    final_amount = discounted_amount + tax
    print("\n--- Bill Summary ---")
    print(f"Customer Name: {customer_name}")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Amount after Discount: ${discounted_amount:.2f}")
    print(f"Tax: +${tax:.2f}")
    print(f"Final Payable Amount: ${final_amount:.2f}")
    another = input("\nDo you want to generate a bill for another customer? (yes/no): ")
    if another.lower() != 'yes':
        break