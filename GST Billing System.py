
name = input("Enter the customer's name: ")
gst_number = input("Enter the customer's GST number: ")
items = []
while True:
    item = input("Enter the item name (or 'done' to finish): ")
    if item == "done":
        break
    price = float(input("Enter the price of the item: "))

    items.append((item, price))
total_cost = sum([item[1] for item in items])

gst_amount = total_cost * 0.18

total_bill = total_cost + gst_amount

print("GST Bill")
print("===============")
print("Customer Name:", name)
print("GST Number:", gst_number)
print("--------------")
print("Item".ljust(20), "Price")
print("--------------")
for item in items:
    print(item[0].ljust(20), item[1])
print("--------------")
print("Total Cost".ljust(20), total_cost)
print("GST Amount".ljust(20), gst_amount)
print("Total Bill".ljust(20), total_bill)
print("===============")
