"""
The initial density is 0.05
a=0  is used to calculate the day
while density<100:
     density=density*2
     a=a+1
When density exceeds 100, a is the number of days calculated



"""


density=0.05
a=0
while density<0.9:
    density*=2
    a+=1
print(f"Cell density does not exceed 0.9 until day {a} and will exceed from day {a+1} onwards")


