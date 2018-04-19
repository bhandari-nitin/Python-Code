################################
###### String Compression ######
################################

def stringCompress(s):
    s = s.lower()
    s = s + " "
    l = ''
    count = 1
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            count = count + 1
        else:
            l = l + str(s[i]) + str(count)
            count = 1 
    return l
        

if __name__ == "__main__":
    print stringCompress('Aabbaada')
