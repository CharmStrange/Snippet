# Albion Markets
# Exceptions : small town markets, Brecilien, hideouts, guild islands

# List
Cities = []

# Dictionary 
# key : {item name, buy price, sell price}
# these are just examples
ITEMS = {
    0 : {'A', 1, 1},
    1 : {'B', 1, 1},
    2 : {'C', 1, 1}
    # Add more items as needed :
}

# Fort Sterling
class FortSterling:
    Bank = []
    Market = []
    
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)
            
    def push_items_bank(self, item_index):
        self.Bank.append(ITEMS[item_index])
    
    def pull_items_bank(self, item_index):
        self.Bank.remove(item_index)
    
    def sell_items_market(self, item_index):
        self.Market.append(ITEMS[item_index])
    
    def buy_items_market(self, item_index):
        self.Market.remove(item_index)
        
    def view_Bank(self):
        print(f"All items in Bank : { len(self.Bank) }")
        for element in self.Bank:
            print(element, end=" ")
        
    def view_Market(self):
        print(f"All items in Market : { len(self.Market) }")
        for element in self.Market:
            print(element, end=" ")
            
    def __del__(self):
        pass


# Lymhurst
class Lymhurst:
    Bank = []
    Market = []
    
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)
    
    def push_items_bank(self, item_index):
        self.Bank.append(ITEMS[item_index])
    
    def pull_items_bank(self, item_index):
        self.Bank.remove(item_index)
    
    def sell_items_market(self, item_index):
        self.Market.append(ITEMS[item_index])
    
    def buy_items_market(self, item_index):
        self.Market.remove(item_index)
        
    def view_Bank(self):
        print(f"All items in Bank : { len(self.Bank) }")
        for element in self.Bank:
            print(element, end=" ")
        
    def view_Market(self):
        print(f"All items in Market : { len(self.Market) }")
        for element in self.Market:
            print(element, end=" ")
            
    def __del__(self):
        pass


# Martlock
class Martlock:
    Bank = []
    Market = []
    
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)

    def push_items_bank(self, item_index):
        self.Bank.append(ITEMS[item_index])
    
    def pull_items_bank(self, item_index):
        self.Bank.remove(item_index)
    
    def sell_items_market(self, item_index):
        self.Market.append(ITEMS[item_index])
    
    def buy_items_market(self, item_index):
        self.Market.remove(item_index)
        
    def view_Bank(self):
        print(f"All items in Bank : { len(self.Bank) }")
        for element in self.Bank:
            print(element, end=" ")
        
    def view_Market(self):
        print(f"All items in Market : { len(self.Market) }")
        for element in self.Market:
            print(element, end=" ")

    def __del__(self):
        pass

# Thetford
class Thetford:
    Bank = []
    Market = []
    
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)

    def push_items_bank(self, item_index):
        self.Bank.append(ITEMS[item_index])
    
    def pull_items_bank(self, item_index):
        self.Bank.remove(item_index)
    
    def sell_items_market(self, item_index):
        self.Market.append(ITEMS[item_index])
    
    def buy_items_market(self, item_index):
        self.Market.remove(item_index)
        
    def view_Bank(self):
        print(f"All items in Bank : { len(self.Bank) }")
        for element in self.Bank:
            print(element, end=" ")
        
    def view_Market(self):
        print(f"All items in Market : { len(self.Market) }")
        for element in self.Market:
            print(element, end=" ")

    def __del__(self):
        pass

# Bridgewatch
class Bridgewatch:
    Bank = []
    Market = []
    
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)

    def push_items_bank(self, item_index):
        self.Bank.append(ITEMS[item_index])
    
    def pull_items_bank(self, item_index):
        self.Bank.remove(item_index)
    
    def sell_items_market(self, item_index):
        self.Market.append(ITEMS[item_index])
    
    def buy_items_market(self, item_index):
        self.Market.remove(item_index)
        
    def view_Bank(self):
        print(f"All items in Bank : { len(self.Bank) }")
        for element in self.Bank:
            print(element, end=" ")
        
    def view_Market(self):
        print(f"All items in Market : { len(self.Market) }")
        for element in self.Market:
            print(element, end=" ")

    def __del__(self):
        pass

# Caerleon
class Caerleon:
    Bank = []
    Market = []
    Black_Market = []
    
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)

    def push_items_bank(self, item_index):
        self.Bank.append(ITEMS[item_index])
    
    def pull_items_bank(self, item_index):
        self.Bank.remove(item_index)
    
    def sell_items_market(self, item_index):
        self.Market.append(ITEMS[item_index])
    
    def buy_items_market(self, item_index):
        self.Market.remove(item_index)
        
    def view_Bank(self):
        print(f"All items in Bank : { len(self.Bank) }")
        for element in self.Bank:
            print(element, end=" ")
        
    def view_Market(self):
        print(f"All items in Market : { len(self.Market) }")
        for element in self.Market:
            print(element, end=" ")
        
    def sell_items_black_market(self, item_index):
        self.Black_Market.append(ITEMS[item_index])
    
    def release_items_black_market(self, item_index):
        self.Black_Market.remove(ITEMS[item_index])
  
    def __del__(self):
        pass
    
def FIND_ITEM(key):
    if ITEMS[key] in ITEMS:
        return ITEMS[key]
    else:
        return None

def MAIN():
    fort_sterling = FortSterling()
    lyumhurst = Lymhurst()
    martlock = Martlock()
    thetford = Thetford()
    bridgewatch = Bridgewatch()
    caerleon = Caerleon()
    
MAIN()
