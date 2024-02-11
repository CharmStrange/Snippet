# Albion Markets
# Exceptions : small town markets, Brecilien, hideouts, guild islands

# List
Cities = []

# Dictionary 
# (ID, ITEM_NAME) : ITEM_PRICE
# (ID, ITEM_NAME) : ITEM_PRICE
ITEMS = {
    (0, 'T4_Bag') : 1000,
    (1, 'T4_Sword') : 1500,
    (2, 'T4_Armor') : 2000,
    (3, 'T4_Shield') : 1800,
    (4, 'T4_Helmet') : 1200,
    (5, 'T4_Boots') : 1300,
    (6, 'T4_Axe') : 1600,
    (7, 'T4_Bow') : 1700,
    (8, 'T4_Staff') : 1900,
    (9, 'T4_Hammer') : 1750,
    (10, 'T4_Mace') : 1650,
    (11, 'T4_Dagger') : 1400,
    (12, 'T4_Cape') : 1100,
    (13, 'T4_Robe') : 1550,
    (14, 'T4_Tome') : 1450,
    (15, 'T4_Fishing Rod') : 2100,
    (16, 'T4_Hammer') : 2200,
    (17, 'T4_Sickle') : 2300,
    # These are just examples.
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
        
    def sell_items_black_market(item):
        Black_Market.append(item)
    
    def release_items_black_market(item):
        Black_Market.remove(item)
  
    def __del__(self):
        pass
    
def FIND_ITEM(Id, Name):
    if ITEMS[Id, Name] in ITEMS:
        return ITEMS[Id, Name]
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
