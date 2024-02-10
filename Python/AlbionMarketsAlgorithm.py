# Albion Markets
# Exceptions : small town markets, Brecilien, hideouts, guild islands
#
Cities = []

# Fort Sterling
class FortSterling:
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)
            
    def __del__(self):
        pass


# Lymhurst
class Lymhurst:
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)
            
    def __del__(self):
        pass


# Martlock
class Martlock:
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)

    def __del__(self):
        pass

# Thetford
class Thetford:
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)

    def __del__(self):
        pass

# Bridgewatch
class Bridgewatch:
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)

    def __del__(self):
        pass

# Caerleon
class Caerleon:
    def __init__(self):
        if len(Cities) == 6:
            print("The city already exists.")
        else:
            Cities.append(self)
            
    def __del__(self):
        pass
    
def MAIN():
    fort_sterling = FortSterling()
    lyumhurst = Lymhurst()
    martlock = Martlock()
    thetford = Thetford()
    bridgewatch = Bridgewatch()
    caerleon = Caerleon()

if __name__ == '__main__':
    MAIN()
