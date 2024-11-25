#Graded

def letter_catalog(items,letter='A'):
  pass
  # MULAI KODEMU DI SINI
  letter_catalog=[items for items in items if items.startswith(letter)]
  ''' cara lain :  
  list=[]
  for comp in items:
      if comp[0] == letter:
          list += items
  return list
    '''  
  return letter_catalog

print(letter_catalog(['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries'],letter='A'))
print(letter_catalog(['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries'],letter='B'))
print(letter_catalog(['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries'],letter='C'))

#Graded

def counter_item(items):
  pass
  # MULAI KODEMU DI SINI
  counter_item={x:items.count(x) for x in items}
  ''' cara lain :
      dictbuah={}
      for buah in items:
          dictbuah[buah]= dictbuah.get(buah,0)+1
      return dictbuah'''
  return counter_item

print(counter_item(['Apple','Apple','Apple','Blueberries','Blueberries','Blueberries']))
print(counter_item(['Cherries', 'Blueberries', 'Banana', 'Avocado', 'Blackberries', 'Banana', 'Blueberries', 'Avocado', 'Banana', 'Blackberries']))
print(counter_item(['Avocado', 'Blueberries', 'Cherries', 'Blueberries', 'Banana', 'Apple', 'Banana', 'Blackberries', 'Cherries', 'Cherries']))

#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = dict(zip(fruits,prices))

def total_price(dcounter,fprice):
  pass
  # MULAI KODEMU DI SINI
  total_price=sum((fprice[x]*dcounter[x]) for x in fprice if x in dcounter)  
  return total_price
  
print(total_price(counter_item(chart),fruit_price))
print(total_price({'Cherries': 1, 'Blueberries': 2, 'Banana': 3, 'Avocado': 2, 'Blackberries': 2}, {'Apple': 6, 'Avocado': 5, 'Banana': 3, 'Blackberries': 10, 'Blueberries': 12, 'Cherries': 7, 'Date Fruit': 14, 'Grapes': 15, 'Guava': 8, 'Jackfruit': 7, 'Kiwifruit': 9}))
print(total_price({'Cherries': 4, 'Blackberries': 2, 'Avocado': 2, 'Blueberries': 2}, {'Apple': 6, 'Avocado': 5, 'Banana': 3, 'Blackberries': 10, 'Blueberries': 12, 'Cherries': 7, 'Date Fruit': 14, 'Grapes': 15, 'Guava': 8, 'Jackfruit': 7, 'Kiwifruit': 9}))
print(total_price({'Avocado': 1, 'Blueberries': 2, 'Cherries': 3, 'Banana': 2, 'Apple': 1, 'Blackberries': 1}, {'Apple': 6, 'Avocado': 5, 'Banana': 3, 'Blackberries': 10, 'Blueberries': 12, 'Cherries': 7, 'Date Fruit': 14, 'Grapes': 15, 'Guava': 8, 'Jackfruit': 7, 'Kiwifruit': 9}))

#Graded

def discounted_price(total,discount,minprice=100):
  pass
  # MULAI KODEMU DI SINI
  if total >= minprice:
      total=total-(total*discount)/100
  else :
        total
  return total
  
print(discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100))
print(discounted_price(100,10,100))
print(discounted_price(110,10,80))
print(discounted_price(100,15,120))
print(discounted_price(200,12,100))
print(discounted_price(230,33,100))

#Graded

def print_summary(items,fprice):
  pass
  # MULAI KODEMU DI SINI
  jumlahBuah = counter_item(sorted(items)) #dict
  hargaTotal = total_price(jumlahBuah,fprice) #int
  hargaDiskon = discounted_price(hargaTotal, 10, 100) #int
  for key in fprice:
    if key in items:
        print(jumlahBuah[key],key,':',jumlahBuah[key]*fprice[key])
  print("total : ",hargaTotal)    
  print("discount price : ",str(hargaDiskon),'\n') 
  
print_summary(chart,fruit_price)
print_summary(['Banana', 'Cherries', 'Avocado', 'Blueberries', 'Blackberries', 'Apple', 'Blueberries', 'Banana', 'Blueberries', 'Blueberries'], {'Apple': 6, 'Avocado': 5, 'Banana': 3, 'Blackberries': 10, 'Blueberries': 12, 'Cherries': 7, 'Date Fruit': 14, 'Grapes': 15, 'Guava': 8, 'Jackfruit': 7, 'Kiwifruit': 9})
print_summary(['Apple', 'Banana', 'Cherries', 'Avocado', 'Avocado', 'Cherries', 'Avocado', 'Blackberries', 'Avocado', 'Cherries'], {'Apple': 6, 'Avocado': 5, 'Banana': 3, 'Blackberries': 10, 'Blueberries': 12, 'Cherries': 7, 'Date Fruit': 14, 'Grapes': 15, 'Guava': 8, 'Jackfruit': 7, 'Kiwifruit': 9})
print_summary(['Blueberries', 'Banana', 'Apple', 'Avocado', 'Blackberries', 'Cherries', 'Apple', 'Blackberries', 'Blueberries', 'Blackberries'], {'Apple': 6, 'Avocado': 5, 'Banana': 3, 'Blackberries': 10, 'Blueberries': 12, 'Cherries': 7, 'Date Fruit': 14, 'Grapes': 15, 'Guava': 8, 'Jackfruit': 7, 'Kiwifruit': 9})
print_summary(['Blueberries', 'Blackberries', 'Cherries', 'Blackberries', 'Blackberries', 'Banana', 'Blackberries', 'Banana', 'Blackberries', 'Avocado'], {'Apple': 6, 'Avocado': 5, 'Banana': 3, 'Blackberries': 10, 'Blueberries': 12, 'Cherries': 7, 'Date Fruit': 14, 'Grapes': 15, 'Guava': 8, 'Jackfruit': 7, 'Kiwifruit': 9})
print_summary(['Avocado', 'Avocado', 'Blackberries', 'Blackberries', 'Banana', 'Apple', 'Blueberries', 'Cherries', 'Cherries', 'Cherries'], {'Apple': 6, 'Avocado': 5, 'Banana': 3, 'Blackberries': 10, 'Blueberries': 12, 'Cherries': 7, 'Date Fruit': 14, 'Grapes': 15, 'Guava': 8, 'Jackfruit': 7, 'Kiwifruit': 9})
