####################################
###### Palindrome Permutation ######
####################################

def isPalindromePerm(s):
    s = s.lower()
    s = s.strip()
    s = s.replace(' ', '')
    l =[]
    even = []
    odd = []
    for w in s:
        l.append(w)
    d = {x:l.count(x) for x in l}
    print l
    print d.values()
    for v in d.values():
        if v % 2 != 0:
            odd.append(v)
        even.append(v)
    print odd
    print even
    if all(even) and len(odd)==1:
        return True
    elif all(even) and len(odd)==0:
        return True
    return False

if __name__ == '__main__':
    print isPalindromePerm('aabbcc')
    
