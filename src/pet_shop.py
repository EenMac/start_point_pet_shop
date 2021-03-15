# WRITE YOUR FUNCTIONS HERE
# 
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    

def get_pets_sold(pet):    
    return pet["admin"]["pets_sold"]

def increase_pets_sold(pet, sold):
    pet["admin"]["pets_sold"] += sold

def get_stock_count(stock):
     return len(stock["pets"])

def get_pets_by_breed(pet_shop, British_Shorthair):
    emptyList = []
    for pet in pet_shop["pets"]:
        if pet["breed"]==British_Shorthair:
            emptyList.append(pet)  
    return emptyList

def get_pets_by_breed(pets, Dalmation):
    emptyList = []
    for pet in pets["pets"]:
        if pet["breed"] == Dalmation:
            emptyList.append(pet)
    return emptyList        

   
def find_pet_by_name(pet_shop, pet_name):
  for pet in pet_shop["pets"]:
    if pet["name"] == pet_name:
      return pet
  
def find_pet_by_name(pet_shop, Fred):
  for pet in pet_shop["pets"]:
    if pet["name"] == Fred:
      return pet  

def remove_pet_by_name(pet_shop, Arthur):
    pet_shop["pets"].remove(find_pet_by_name(pet_shop, Arthur))

def add_pet_to_stock(pet_shop, new_dict):
    pet_shop["pets"].append(new_dict)

def get_customer_cash(customers):
    for customer in customers:
        return customers["cash"]

def remove_customer_cash(customer, amount):        
    customer["cash"]-= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])    

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)
    return customer["pets"]
