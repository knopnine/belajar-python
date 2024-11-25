# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = dict(zip(fruits,prices))

def counter_item(items):
    pass
    counter_item={x:items.count(x) for x in items}
    return counter_item

def total_price(dcounter,fprice):
    pass
    total_price=sum([fruit_price[x] for x in chart])
    return total_price

def discounted_price(total,discount,minprice):
    pass
    if total >= minprice:
        dprice=total-(total*discount)/100
        return dprice
    else :
        return total

def print_summary(items,fprice):
    pass
    counter_item(chart)
      

print_summary(chart,fruit_price)