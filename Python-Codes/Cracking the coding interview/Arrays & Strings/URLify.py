##################
##### URLify #####
##################

def urlIfy(s):
    s = s.strip(' ')
    return s.replace(' ', '%20')

if __name__ == '__main__':
    print urlIfy('Nitin Bhandari')
