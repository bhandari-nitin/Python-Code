################################
######## isStringUnique ########
################################

def isUnique(s):
    letter = {}
    # Assuming string is ASCII
    if len(s) > 128:            
        return False
    for l in s:
        if l in letter:         # This loop iterates over keys in dictionary
            return False
        letter[l]=True
    return True

# main fuction calling isUnique

if __name__ == '__main__':
    print isUnique('Nitin')
        
