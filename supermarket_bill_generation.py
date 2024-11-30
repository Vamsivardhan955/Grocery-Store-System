# from datetime import  datetime

# name=input("Enter your name :")

# # list of names
# lists='''

# Rice        Rs 20/kg  
# Sugar       Rs 30/kg  
# Salt        Rs 20/kg  
# Oil         Rs 80/liter  
# Wheat Flour Rs 25/kg  
# Milk        Rs 50/liter  
# Eggs        Rs 5/unit  
# Butter      Rs 100/250g  
# Tea         Rs 200/kg  
# Coffee      Rs 400/kg  
# Biscuits    Rs 30/packet  
# Soap        Rs 25/unit  
# Shampoo     Rs 120/bottle  
# Toothpaste  Rs 80/unit  
# Detergent   Rs 50/500g  
# Tomatoes    Rs 30/kg  
# Potatoes    Rs 25/kg  
# Onions      Rs 20/kg  
# Carrots     Rs 40/kg  
# Chillies    Rs 60/kg  

# '''
# #declaration
# price=0
# pricelist=[]
# totalprice=0
# finalprice=0
# ilist=[]
# qlist=[]
# plist=[]

# #rates for items


# items = {
#     'rice': 20,
#     'sugar': 30,
#     'salt': 20,
#     'oil': 80,
#     'wheat_flour': 25,
#     'milk': 50,
#     'eggs': 5,
#     'butter': 100,
#     'tea': 200,
#     'coffee': 400,
#     'biscuits': 30,
#     'soap': 25,
#     'shampoo': 120,
#     'toothpaste': 80,
#     'detergent': 50,
#     'tomatoes': 30,
#     'potatoes': 25,
#     'onions': 20,
#     'carrots': 40,
#     'chillies': 60
# }

# option=int(input("for list of items press 1:"))
# if option==1:
#     print(lists)
# for i in range(len(items)):
#     inp1=int(input("if you want to buy press 1 or 2 for exit:"))
#     if inp1==2:
#         break
#     if inp1==1:
#         item=input("Enter your items:")
#         quantity=int(input("Enter your quality:"))
#         if item in items.keys():
#             price=quantity*(items[item]) 
#             pricelist.append((item,quantity,items,price))
#             totalprice+=price
#             ilist.append(item)
#             qlist.append(quantity)
#             plist.append(price)
#             gst=(totalprice*5)/100
#             finalammount=gst+totalprice
#         else:
#             print("sorry you entered item is not available")
#     else:
#         print("you entered a wrong number")

#     inp=input("can i bill the items yes or no :")
#     if inp=='yes':
#         pass
#         if finalammount!=0:
#             print(25*"=", "Super Makrket",25*"=" )
#             print(25*" ","ALL India")
#             print("Name:",name,30*" " , "Date:",datetime.now())
#             print(75*"-")
#             print("s.no",8*' ',"items",8*" ","Quantity",3*" ","price")
#             for i in range(len(pricelist)):
#                 print(i,8*" ",5*" ",ilist[i],3*" ",qlist[i],8*"" ,plist[i])
#                 print(75*"-")
#                 print(50*" ", 'TotalAmount:','RS',totalprice)
#                 print("gst amount",52*" ",'Rs',gst)
#                 print(50*" ","TotalAmount:",'Rs',totalprice)
#                 print(75*"-")
#                 print(25*" ","Thanks for visiting ")
#                 print(75*"-")






from datetime import datetime

# Get customer name
name = input("Enter your name: ")

# List of available items with prices
items_list = '''
Rice        Rs 20/kg  
Sugar       Rs 30/kg  
Salt        Rs 20/kg  
Oil         Rs 80/liter  
Wheat Flour Rs 25/kg  
Milk        Rs 50/liter  
Eggs        Rs 5/unit  
Butter      Rs 100/250g  
Tea         Rs 200/kg  
Coffee      Rs 400/kg  
Biscuits    Rs 30/packet  
Soap        Rs 25/unit  
Shampoo     Rs 120/bottle  
Toothpaste  Rs 80/unit  
Detergent   Rs 50/500g  
Tomatoes    Rs 30/kg  
Potatoes    Rs 25/kg  
Onions      Rs 20/kg  
Carrots     Rs 40/kg  
Chillies    Rs 60/kg  
'''

# Prices of items
items = {
    'rice': 20,
    'sugar': 30,
    'salt': 20,
    'oil': 80,
    'wheat_flour': 25,
    'milk': 50,
    'eggs': 5,
    'butter': 100,
    'tea': 200,
    'coffee': 400,
    'biscuits': 30,
    'soap': 25,
    'shampoo': 120,
    'toothpaste': 80,
    'detergent': 50,
    'tomatoes': 30,
    'potatoes': 25,
    'onions': 20,
    'carrots': 40,
    'chillies': 60
}

# Initialize variables
pricelist = []
total_price = 0
item_list = []
quantity_list = []
price_list = []

# Display item list
option = int(input("For list of items, press 1: "))
if option == 1:
    print(items_list)

# Shopping loop
while True:
    choice = int(input("If you want to buy, press 1. To exit, press 2: "))
    if choice == 2:
        break
    elif choice == 1:
        item = input("Enter the item: ").lower()
        quantity = int(input("Enter the quantity: "))

        if item in items:
            price = quantity * items[item]
            pricelist.append((item, quantity, items[item], price))
            total_price += price
            item_list.append(item)
            quantity_list.append(quantity)
            price_list.append(price)
        else:
            print("Sorry, the entered item is not available.")
    else:
        print("Invalid input. Please try again.")

# Billing
bill_confirmation = input("Can I bill the items? (yes/no): ").lower()
if bill_confirmation == 'yes' and total_price > 0:
    gst = (total_price * 5) / 100
    final_amount = total_price + gst

    print("\n" + "=" * 30, "Supermarket", "=" * 30)
    print(f"Name: {name}", " " * 30, f"Date: {datetime.now()}")
    print("-" * 75)
    print(f"{'S.No':<10}{'Item':<15}{'Quantity':<10}{'Price':<10}")
    print("-" * 75)

    for i, (item, quantity, rate, price) in enumerate(pricelist):
        print(f"{i + 1:<10}{item:<15}{quantity:<10}{price:<10}")

    print("-" * 75)
    print(f"{'Total Amount:':<55} Rs {total_price}")
    print(f"{'GST (5%):':<55} Rs {gst}")
    print(f"{'Final Amount:':<55} Rs {final_amount}")
    print("-" * 75)
    print(" " * 25, "Thanks for visiting!")
    print("-" * 75)
else:
    print("No items to bill. Thank you!")




