#password generator
all=['b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y'
     ,'z','0','1','2','3','4','5','6','7','8','9','!','@','$','%','^','&','*','(',')'
     ,'_']

import random
l=input('how long is your password =' )




if l.isnumeric()==False:
 print('plz enter a valid number')
  


a=(int(l))

for i in range(a):

 print(random.choice (all),end='')
