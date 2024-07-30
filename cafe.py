# Menu list 
Menu = ['Espresso','Sandwiches','Pastries','Bagels']

# stock, has quantity for each menu item 
stock = {'Espresso': 5, 'Sandwiches' : 7, 'Bagels': 9, 'Pastries':12 }

# price cost for each menu item
price = {'Bagels':7.00, 'Pastries':9.05, 'Sandwiches':12.50, 'Espresso':15.00} 

total = 0 
for i in Menu:
    total += stock[i] * price[i]
print(total)