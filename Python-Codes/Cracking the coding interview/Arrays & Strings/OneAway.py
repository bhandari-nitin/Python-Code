####################
##### One Away #####
####################

def oneAway(p, q):
    c =  0
    
    if len(p)==len(q)-1:
        #insertion
        for s in p:
            if s not in q:
                return False
            
    elif len(p)==len(q)+1:
        #deletion
        for s in q:
            if s not in p:
                return False
    
    elif len(p)==len(q):
        for r in p:
            if r in q:
                c += 1
        if c != (len(p)-1):
            return False
    else:
        return False
    return True

if __name__ == '__main__':
    print oneAway('pale', 'bake')
    
