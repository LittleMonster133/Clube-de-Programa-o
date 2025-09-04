import random 

num = random.randint(1, 100)
print (num)


while 1:

    palpite =  input('Digite um número')
    palpite = int(palpite)

    if (palpite <= 0 or palpite > 100):
        print ('número maior')
    
    elif palpite == num:
        print ('você venceu')
     
    elif palpite < num:
        print ('o numero é maior')
    
    elif palpite > num:
        print ('o numero é menor')
