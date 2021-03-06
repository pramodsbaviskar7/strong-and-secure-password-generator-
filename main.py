import string
import random

if __name__ == '__main__':
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    pl = input("Enter length of strong password you want\n")
    if(pl.isdigit()):
        pl=int(pl)
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        #print(s)
        random.shuffle(s)

        print("".join(s[0:pl]))
        print("".join(random.sample(s,pl)))
    else:
        print("please enter a integer value")