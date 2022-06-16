import random

def predict(num):
    c=0
    s=0
    for i in range(num):
        x=random.uniform(-1, 1)
        y=random.uniform(-1, 1)
        if x**2 + y**2 <=1:
            c+=1
        s+=1
    pi_est = 4*c/s
    return pi_est

