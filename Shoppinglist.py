shopping_list = []

def help():
  print("What should we pick up out of the store")
  print("""
  Enter 'DONE' to stop adding items
  Enter 'HELP' to see this menu again 
  Enter 'LIST' to see your list
  """)
  
  
def add_to_list(item):
  shopping_list.append(item.capitalize())
  print(f"Total Items: {len(shopping_list)}")

  
def show_list():
  current_item = 1
  for item in shopping_list:
    print(f"{current_item}. {item}")
    current_item += 1
        
help()     
while True:  
  new_item = input("Enter Item: ")
  
  if new_item == "DONE":
    break  
  elif new_item == "HELP":
    help()
    continue    
  elif new_item == "LIST":
    show_list()
    continue
    
  add_to_list(new_item)
  
show_list()
