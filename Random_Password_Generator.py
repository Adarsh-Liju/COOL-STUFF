import random as r
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
num=[1,2,3,4,5,6,7,8,9]
spe_ch=['!','@','#','$','%','^','&','*','(',')','+']
count=0
pword=""
while(count<3):
    for i in alp,num,spe_ch:
        pa1=str(r.choice(alp))
        pa2=str(r.choice(num))
        pa3=str(r.choice(spe_ch))
        pword=pword+pa1+pa2+pa3
    count=count+1
print("Random Password is : ",pword)
