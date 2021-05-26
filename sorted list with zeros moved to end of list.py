#sorted list with zeros moved to end of list in  python
import random
lst=[random.randint(0,20) for item in range(1, 10+1)]
lst.sort()
print("sorted list of random numbers")
print(lst)
lstzro=[item for item in lst if item!=0]+[item for item in lst if item==0]
print("sorted list with zeros moved to end of list ")
print(lstzro)
