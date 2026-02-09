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
'''#A retail store wants to automate its billing process using a python program.As a programmer,you are asked to develop a console-based application that assists the cashier in generating customer bills.the program should accept the customers name,the number of items purchased,and the price of each item.ift should calculate the total bill amount and apply a discount based on the total purchase value(for example,higher discounts for higher bill amounts).the program must also calculate tax on the discounted amount and display the final payable bill clearly.the system should allow the cashier top generate bills for multiple customers until they choose to stop the program.
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
        break'''
'''#a city traffic department wants to build a python based syatem to monitor vechile speed and automatically identify traffic rules vilolations .you are required to develop a console based program that accepts a vehicle number ,the type of vehicle (two-wheeler,car,or heavy vehicle), and the recorded speed based on predefined speed limits for each vehicle limits for each vehicle type the progarm should determine wheather the vehicle is within the permitted speed or has violated the speed or has violated speed limit. if violated occurs the program should calculate the fine amount according to the level of overspeending and display a detailed violation report the syatem should continue procesing vehicle records until the operater choosesto termenate program.
def get_speed_limit(vehicle_type):
    speed_limits = {
        'two-wheeler': 40,
        'car': 60,
        'heavy vehicle': 50
    }
    return speed_limits.get(vehicle_type.lower(), 0)
def calculate_fine(overspeed):
    if overspeed <= 10:
        return 100
    elif overspeed <= 20:
        return 200
    else:
        return 500
while True:
    vehicle_number = input("Enter vehicle number: ")
    vehicle_type = input("Enter vehicle type (two-wheeler/car/heavy vehicle): ")
    recorded_speed = int(input("Enter recorded speed (km/h): "))
    speed_limit = get_speed_limit(vehicle_type)
    if speed_limit == 0:
        print("Invalid vehicle type. Please try again.")
        continue
    if recorded_speed <= speed_limit:
        print(f"Vehicle {vehicle_number} is within the speed limit of {speed_limit} km/h.")
    else:
        overspeed = recorded_speed - speed_limit
        fine = calculate_fine(overspeed)
        print(f"Vehicle {vehicle_number} has violated the speed limit by {overspeed} km/h.")
        print(f"Fine amount: ${fine}")
    another = input("Do you want to process another vehicle record? (yes/no): ")
    if another.lower() != 'yes':
        break
    '''
'''#A hospital wants to implement a python based patient appointment system to reduce waiting times and improve patient experience.you are required to develop a console based application that allows patients to book appointments with doctors.the program should accept patient details such as name,age,and contact information.it should also allow patients to select a doctor from a predefined list and choose an available time slot.the program must check for scheduling conflicts and ensure that no double bookings occur.once an appointment is successfully booked the system should generate a confirmation message with all relevant details.the program should continue to accept new appointment requests until the operator chooses to terminate the program.
doctors = {
    'Dr. Smith': ['10:00 AM', '11:00 AM', '02:00 PM'],
    'Dr. Johnson': ['09:00 AM', '01:00 PM', '03:00 PM'],
    'Dr. Lee': ['10:30 AM', '12:00 PM', '04:00 PM']
}
appointments = {}
while True:
    patient_name = input("Enter patient name: ")
    patient_age = input("Enter patient age: ")
    patient_contact = input("Enter patient contact information: ")
    print("\nAvailable Doctors:")
    for i, doctor in enumerate(doctors.keys(), start=1):
        print(f"{i}. {doctor}")
    doctor_choice = int(input("Select a doctor by number: ")) - 1
    selected_doctor = list(doctors.keys())[doctor_choice]
    print(f"\nAvailable Time Slots for {selected_doctor}:")
    available_slots = [slot for slot in doctors[selected_doctor] if (selected_doctor, slot) not in appointments]
    for i, slot in enumerate(available_slots, start=1):
        print(f"{i}. {slot}")
    slot_choice = int(input("Select a time slot by number: ")) - 1
    selected_slot = available_slots[slot_choice]
    appointments[(selected_doctor, selected_slot)] = {
        'Patient Name': patient_name,
        'Age': patient_age,
        'Contact': patient_contact
    }
    print("\n--- Appointment Confirmation ---")
    print(f"Patient Name: {patient_name}")
    print(f"Doctor: {selected_doctor}")
    print(f"Time Slot: {selected_slot}")
    another = input("\nDo you want to book another appointment? (yes/no): ")
    if another.lower() != 'yes':
        break'''
'''#A bank wants to introduce a python-based loan eligibility evaluation system to handle a wide range od real-world customer profiles and reduce manual processing time.you are required to develop a console-based application that accepts customer details such as name,age,income,credit score,and existing debts.the program should evaluate the loan eligibility based on predefined criteria such as minimum income,credit score thresholds,and debt-to-income ratios.if the customer is eligible,the program should calculate the maximum loan amount they can avail based on their financial profile.the system should generate a detailed eligibility report for each customer and continue processing new applications until the operator chooses to terminate the program.
def calculate_debt_to_income_ratio(debts, income):
    if income == 0:
        return float('inf')
    return debts / income
def evaluate_loan_eligibility(age, income, credit_score, debts):
    min_income = 30000
    min_credit_score = 600
    max_debt_to_income_ratio = 0.4
    if age < 18 or age > 65:
        return False, 0
    if income < min_income or credit_score < min_credit_score:
        return False, 0
    dti_ratio = calculate_debt_to_income_ratio(debts, income)
    if dti_ratio > max_debt_to_income_ratio:
        return False, 0
    max_loan_amount = income * 5 - debts
    return True, max_loan_amount
while True:
    customer_name = input("Enter customer name: ")
    customer_age = int(input("Enter customer age: "))
    customer_income = float(input("Enter customer income: "))
    customer_credit_score = int(input("Enter customer credit score: "))
    customer_debts = float(input("Enter existing debts: "))
    eligible, max_loan = evaluate_loan_eligibility(customer_age, customer_income, customer_credit_score, customer_debts)
    print("\n--- Loan Eligibility Report ---")
    print(f"Customer Name: {customer_name}")
    if eligible:
        print("Status: Eligible for Loan")
        print(f"Maximum Loan Amount: ${max_loan:.2f}")
    else:
        print("Status: Not Eligible for Loan")
    another = input("\nDo you want to process another application? (yes/no): ")
    if another.lower() != 'yes':
        break'''
'''
# A supermarket wants to automate its monthly sales analysis system using a python program to help the manager understand product-wise and day-wise sales performance.you are required to develop a console-based application that uses multiple loops to process sales data.the program should first ask for the number of days in month and then,for each day,ask for the number of products sold that day.for each product,the program should accept the product name,quantity sold,and price per unit.the program must calculate the total sales for each product and the overall sales for each day.at the end of the month,the system should generate a comprehensive sales report showing total sales per product,total sales per day,and the grand total sales for the month.the program should continue to accept new month's data until the operator chooses to terminate the program.
while True:
    num_days = int(input("Enter number of days in the month: "))
    monthly_product_sales = {}
    daily_sales_totals = []
    for day in range(1, num_days + 1):
        print(f"\nDay {day}:")
        num_products = int(input("Enter number of products sold today: "))
        daily_total = 0
        for _ in range(num_products):
            product_name = input("Enter product name: ")
            quantity_sold = int(input("Enter quantity sold: "))
            price_per_unit = float(input("Enter price per unit: "))
            total_sales = quantity_sold * price_per_unit
            daily_total += total_sales
            if product_name in monthly_product_sales:
                monthly_product_sales[product_name] += total_sales
            else:
                monthly_product_sales[product_name] = total_sales
        daily_sales_totals.append(daily_total)
        print(f"Total sales for Day {day}: ${daily_total:.2f}")
    grand_total = sum(daily_sales_totals)
    print("\n--- Monthly Sales Report ---")
    print("Total Sales per Product:")
    for product, total in monthly_product_sales.items():
        print(f"{product}: ${total:.2f}")
    print("\nTotal Sales per Day:")
    for day, total in enumerate(daily_sales_totals, start=1):
        print(f"Day {day}: ${total:.2f}")
    print(f"\nGrand Total Sales for the Month: ${grand_total:.2f}")
    another_month = input("\nDo you want to enter data for another month? (yes/no): ")
    if another_month.lower() != 'yes':
        break
'''
'''#A apartment complex wants to automate its Resident Maintenance Billing and Service Management System using Python to avoid manual bookkeeping errors and to track monthly maintenance payments efficiently. You are required to design an object-oriented Python application that models real-world entities using classes and constructors. The system should contain a class named Resident where the constructor initializes resident details such as flat number, resident name, apartment type (1BHK, 2BHK, or 3BHK), number of family members, parking slots, water usage units, electricity usage units, and whether additional facilities such as gym and swimming pool are subscribed. Another class named MaintenanceCalculator should compute monthly maintenance charges based on apartment type base maintenance cost, per-unit water charge, electricity charge slabs, parking charges, and facility subscription fees. A third class named ApartmentManagement should maintain multiple resident records generate bills, store payment status, and produce monthly reports. The program must calculate the total bill using multiple conditions such as higher water usage leading to higher rates, electricity slab-wise billing, and discounts for senior citizens or early payments. The system should also allow marking a bill as paid or unpaid and generate a warning list for pending payments. At the end of the execution, the program should display individual bills and a summary report showing total revenue collected, number of unpaid residents ,and highest bill amount.
class Resident:
    def __init__(self, flat_number, resident_name, apartment_type, family_members, parking_slots, water_units, electricity_units, gym_subscribed, pool_subscribed):
        self.flat_number = flat_number
        self.resident_name = resident_name
        self.apartment_type = apartment_type
        self.family_members = family_members
        self.parking_slots = parking_slots
        self.water_units = water_units
        self.electricity_units = electricity_units
        self.gym_subscribed = gym_subscribed
        self.pool_subscribed = pool_subscribed
class MaintenanceCalculator:
    def __init__(self):
        self.base_costs = {'1BHK': 1000, '2BHK': 1500, '3BHK': 2000}
        self.water_charge_per_unit = 5
        self.electricity_slabs = [(100, 2), (200, 3), (float('inf'), 5)]
        self.parking_charge_per_slot = 200
        self.gym_fee = 300
        self.pool_fee = 500
    def calculate_bill(self, resident):
        base_cost = self.base_costs.get(resident.apartment_type, 0)
        water_charge = resident.water_units * self.water_charge_per_unit
        electricity_charge = sum(min(resident.electricity_units, slab[0]) * slab[1] for slab in self.electricity_slabs)
        parking_charge = resident.parking_slots * self.parking_charge_per_slot
        gym_fee = self.gym_fee if resident.gym_subscribed else 0
        pool_fee = self.pool_fee if resident.pool_subscribed else 0
        total_bill = base_cost + water_charge + electricity_charge + parking_charge + gym_fee + pool_fee
        return total_bill
class ApartmentManagement:
    def __init__(self):
        self.residents = []
        self.payments = {}
    def add_resident(self, resident):
        self.residents.append(resident)
    def generate_bills(self):
        calculator = MaintenanceCalculator()
        for resident in self.residents:
            bill_amount = calculator.calculate_bill(resident)
            self.payments[resident.flat_number] = {'Resident Name': resident.resident_name, 'Bill Amount': bill_amount, 'Paid': False}
    def mark_payment(self, flat_number):
        if flat_number in self.payments:
            self.payments[flat_number]['Paid'] = True
    def generate_report(self):
        total_revenue = sum(payment['Bill Amount'] for payment in self.payments.values() if payment['Paid'])
        unpaid_residents = [payment['Resident Name'] for payment in self.payments.values() if not payment['Paid']]
        highest_bill = max(payment['Bill Amount'] for payment in self.payments.values())
        print("\n--- Monthly Maintenance Report ---")
        print(f"Total Revenue Collected: ${total_revenue:.2f}")
        print(f"Number of Unpaid Residents: {len(unpaid_residents)}")
        print(f"Highest Bill Amount: ${highest_bill:.2f}")
# Example usage
management = ApartmentManagement()
resident1 = Resident(101, "Alice", "2BHK", 4, 1, 50, 150, True, False)
resident2 = Resident(102, "Bob", "3BHK", 5, 2, 80, 250, False, True)
management.add_resident(resident1)
management.add_resident(resident2)
management.generate_bills()
management.mark_payment(101)  # Mark Alice's bill as paid
management.generate_report()'''
