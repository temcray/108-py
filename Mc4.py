#Calculate the total of a product in the cart list and calculate the average of the product cart.
#product_cart = [100'200'300'400'500]

product_cart = ["100'200'300'400'500"]

def get_total(list):
    total=0
    for product in list:
        sum(total)
    return total

def get_average(total,length):
    return total/length


total = get_total(product_cart)
avg = get_average(total, len(product_cart))

print(f"The total is: {total}")
print(f"The average is: {avg}")