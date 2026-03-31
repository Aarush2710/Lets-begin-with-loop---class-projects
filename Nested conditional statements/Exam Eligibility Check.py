attendence=int(input("Enter your attencence  "))
if attendence >=75 :
    print("You are  eligibele for your exam")
    medical_certificate=input("Do you have a medical certificate ")
    if medical_certificate == "yes" :
        print("You are allow to go for your exam")
    else :
        print("You are not allowed to go for your exam")

    
else :
    print("You are not eligibele for your exam")
   


