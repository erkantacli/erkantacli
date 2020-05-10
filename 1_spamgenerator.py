from random import shuffle

liste = "amazing gorgeous blazing stunning tremendous greatest best fantastic phenomenal \
         delightful amitious outstanding incredible spectacular super cool magical \
         revolutionary beautiful jaw-dropping".upper() .split()
shuffle(liste)

for strophe in range(4):
    for n in range(2):
        for i in range(4):
            print("Spam ", end='')
        print()
   
    print(liste.pop() +" Spam, " + liste.pop() + " Spam")
    print()
