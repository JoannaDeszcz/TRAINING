# Create warehouse: add products, delete, etc.
import sys
class Warehouse:

    def __init__(self,list_products):
        self.list_products=list_products

    def display_available_products(self):
        print('Available products: ƒn')
        for product in self.list_products:
            print(product)
    
    def add_product(self):
        self.product_name=input('Enter the name of the product you want to add: ')
        if self.product_name not in self.list_products:
            self.list_products.append(self.product_name)
            print(f'The product {self.product_name} has been put into storage.')
        else:
            ('The product {self.product_name} is already in the warehouse.')

    def remove_product(self):
        self.product_name=input('Enter the name of the product you want to delete: ')
        if self.product_name in self.list_products:
            self.list_products.remove(self.product_name)
            print(f'Product {self.product_name} has been removed from stock. ')
        else: 
            print('The product {self.product_name} is not in the warehouse.')

warehouse=Warehouse(['milk','water','eggs'])

print('Welcome to the warehouse!')

while True:

    print('Choose what action you want to perform: \n\n1 - see stock \n2 - add product \n3 - remove product \n4 - exit')
    choice=int(input('\nSelected action: '))

    if choice == 1:
        warehouse.display_available_products()
    elif choice == 2:
        warehouse.add_product()
    elif choice == 3:
        warehouse.remove_product()
    elif choice == 4:
        print('Warehouse completed')
        sys.exit()