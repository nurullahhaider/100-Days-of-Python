# write a program to convert student scores to grades V1
stud_scor= { "John": 82, "Ron": 78, "Hermione": 99, "Dan": 73, "Neville": 62,}
print(stud_scor)
for key in stud_scor:
    print ("key= ",key)
    print ("value= ",stud_scor[key])
    if stud_scor[key]>= 91 :
        print ("Outstanding ")
    elif stud_scor[key]>= 81 and stud_scor[key]<=90 :
        print ("exceeds expectations ")
    elif stud_scor[key]>= 71 and stud_scor[key]<=80 :
        print ("acceptable ")
    else:
        print ("sorry ")
