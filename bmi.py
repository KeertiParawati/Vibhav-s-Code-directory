height = int (input("please enter your height in cm"))     
weight = int (input("please enter your weight in kg"))
bmi = weight/(height / 100)**2 
if bmi < 18.5:
    print ("you are underweight") 
elif bmi < 25:
    print ("you are normal weight eight") 
elif bmi < 30:    
    print ("you are overweight ")
else:            
    print ("you are obese")