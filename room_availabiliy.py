rooms = {"101": "yes", "102": "no", "103": "yes"}
for number,ans in rooms.items():
    if ans =="no":
        continue
    else:
        print(f"Room no:",number," is Available......")
