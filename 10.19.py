#jdfitzge 1374331
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0,item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        self.print_cost = (self.item_quantity * self.item_price)
        print(('{} {} @ ${} = ${}') .format(self.item_name, self.item_quantity, self.item_price, self.print_cost))

    def print_item_description(self):
        print(self.item_name,end=": ")
        print(self.item_description)

class ShoppingCart:
    def __init__(self,customer_name="none",current_date="January 1, 2016",cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self,item):
        self.cart_items.append(item)

    def remove_item(self,item_name):
        found = False
        for i in self.cart_items:
            if(i.item_name==item_name):
                self.cart_items.remove(i)
                found = True
                break
        if(not found):
            print("Item not found in cart. Nothing removed.")

    def modify_item(self,item,item_quantity=-1,item_price=-1,item_description="none"):
        found = False
        for i in self.cart_items:
            if (i.item_name == item.item_name):
                if(item_price!=-1):
                    i.item_price = item_price
                if(item_quantity!=-1):
                    i.item_quantity = item_quantity
                if(item_description!="none"):
                    i.item_description = item_description
                found = True
                break
        if (not found):
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        number = 0
        for i in self.cart_items:
            number = number + i.item_quantity
        return number

    def get_cost_of_cart(self):
        cost = 0
        for i in self.cart_items:
            cost = cost + (i.item_price*i.item_quantity)
        return cost

    def print_total(self):
        if(self.get_num_items_in_cart() == 0):
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customer_name,end="'s Shopping Cart - ")
            print(self.current_date)
            print("Number of Items:",end=" ")
            print(self.get_num_items_in_cart())
            for i in self.cart_items:
                i.print_item_cost()
            print("Total: $",end="",)
            print(self.get_cost_of_cart())
            print()

    def print_descriptions(self):
        if (self.get_num_items_in_cart()  == 0):
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customer_name, end="'s Shopping Cart - ")
            print(self.current_date)
            print("Item Descriptions")
            for i in self.cart_items:
                i.print_item_description()

def get_input():
    print('MENU')
    print("a - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n")
    print('Choose an option:')
    return input()

def print_menu(cart):
    while(True):
        user_input = get_input()
        if(user_input=='a'):
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = input("Enter the item price:\n")
            quantity = input("Enter the item quantity:\n")
            item = ItemToPurchase(name,int(price),int(quantity),description)
            cart.add_item(item)
        if(user_input=='r'):
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:")
            cart.remove_item(name)
        if(user_input=='c'):
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:")
            quantity = input("Enter the new quantity:")
            Item = ItemToPurchase(name)
            cart.modify_item(Item,int(quantity))
        if(user_input=='i'):
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        if(user_input=='o'):
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        if(user_input=='q'):
            break
        if(user_input != 'a' or 'r' or 'c' or 'i' or 'o' or 'q'):
            print('Choose an option:')
            return

def main():
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print()
    print("Customer name:",end=" ")
    print(name)
    print("Today's date:",date)
    print()
    cart = ShoppingCart(name,date)
    print_menu(cart)

if __name__ == "__main__":
    main()
