num =3
print("For login you have only 3 attempts......")
while num>=1:
    password = input('enter password:')
    num = num-1

    if password =='admin123':
        print("password is correct")
        break
    else:
        print(f"Wrong password... \n You have {num} attempts left")
if num==0:
    print("Blocked....")