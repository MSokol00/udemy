import re

def censor(input):
    patt = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    result = patt.sub('CENSORED', input)
    return result

if __name__ == '__main__':
    print(censor('I hope you fracking die'))
    print(censor('Frack you!'))