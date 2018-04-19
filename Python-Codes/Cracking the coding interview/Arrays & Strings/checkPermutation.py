##################################################################
########## Check if one string is permutation of another #########
##################################################################

def isPer(s1, s2):
     #sorting two strings
    s1 = s1.strip(' ')
    s2 = s2.strip(' ')

    if len(s1) != len(s2):
        return False
    
    sort1 = []
    sort2 = []
    for x,y in zip(s1,s2):
        sort1.append(ord(x))
        sort2.append(ord(y))
        sort1 = sorted(sort1)
        sort2 = sorted(sort2)
        if sort1 == sort2:
            return True

if __name__  == '__main__':
    print isPer('god', 'dog')
             
             
