gender = 'male'
age = 62
r_status = 'unmarried'
if r_status== 'unmarried':
    if gender == 'male' and age>40:
        print("You are selected!!")
    elif gender=='female' and age<30:
        print("You are selected")
else:
    print("Rejected")
