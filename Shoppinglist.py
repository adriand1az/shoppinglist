class ShoppingList():
  shopping_list = []
  
  def help(self):
    print("What should we pick up out of the store")
    print("""
    Enter 'DONE' to stop adding items
    Enter 'HELP' to see this menu again 
    Enter 'LIST' to see your list
    """)
    
    
  def add_to_list(self,item):
    self.shopping_list.append(item.capitalize())
    print(f"Total Items: {len(self.shopping_list)}")
  
    
  def show_list(self):
    current_item = 1
    for item in self.shopping_list:
      print(f"{current_item}. {item}")
      current_item += 1
          
instance = ShoppingList()
instance.help()
while True:  
    new_item = input("Enter Item: ")
    
    if new_item == "DONE":
      break  
    elif new_item == "HELP":
      instance.help()
      continue    
    elif new_item == "LIST":
      instance.show_list()
      continue
      
    instance.add_to_list(new_item)
    
instance.show_list()
