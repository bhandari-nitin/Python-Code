import re

def Find(pat, text):
    print 'hi'
    match = re.findall(pat, text)
    if match: print match
    else: print 'not found'

if __name__ == '__main__':
    Find(r'[\w.]+@[\w.]+', 'blah nick.p@gmail.com yatta foo@bar ')
