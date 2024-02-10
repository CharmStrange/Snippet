# Albion Markets
# Exceptions : small town markets, Brecilien, hideouts, guild islands

# List
Cities = []

# Dictionary 
# (ID, ITEM_NAME) : ITEM_PRICE
ITEMS = {
    (0, 'ITEM_NAME_1') : 1,
    (1, 'ITEM_NAME_2') : 1,
    (2, 'ITEM_NAME_3') : 1
    # ...
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
            
    def push_items_bank(item):
        Bank.append(item)
    
    def pull_items_bank(item):
        Bank.remove(item)
    
    def sell_items_market(item):
        Market.append(item)
    
    def buy_items_market(item):
        Market.remove(item)
            
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
    
    def push_items_bank(item):
        Bank.append(item)
    
    def pull_items_bank(item):
        Bank.remove(item)
    
    def sell_items_market(item):
        Market.append(item)
    
    def buy_items_market(item):
        Market.remove(item)
            
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

    def push_items_bank(item):
        Bank.append(item)
    
    def pull_items_bank(item):
        Bank.remove(item)
    
    def sell_items_market(item):
        Market.append(item)
    
    def buy_items_market(item):
        Market.remove(item)

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

    def push_items_bank(item):
        Bank.append(item)
    
    def pull_items_bank(item):
        Bank.remove(item)
    
    def sell_items_market(item):
        Market.append(item)
    
    def buy_items_market(item):
        Market.remove(item)

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

    def push_items_bank(item):
        Bank.append(item)
    
    def pull_items_bank(item):
        Bank.remove(item)
    
    def sell_items_market(item):
        Market.append(item)
    
    def buy_items_market(item):
        Market.remove(item)

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

    def push_items_bank(item):
        Bank.append(item)
    
    def pull_items_bank(item):
        Bank.remove(item)
    
    def sell_items_market(item):
        Market.append(item)
    
    def buy_items_market(item):
        Market.remove(item)
  
    def __del__(self):
        pass
    
def MAIN():
    fort_sterling = FortSterling()
    lyumhurst = Lymhurst()
    martlock = Martlock()
    thetford = Thetford()
    bridgewatch = Bridgewatch()
    caerleon = Caerleon()
    
MAIN()
