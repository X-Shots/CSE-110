speed = int(input("Whats your speed bozo"))

if speed > 55:
    print("SLOW DOWN LOSER")
elif speed > 30:
    print("NICE JOB GOOF BALL")
else:
    print("SPEED UP GRANNEY")



speed = int("Whats your speed bozo")
truck = input("ARE YOU A TRCUKER?(type 'yes' if yes")
if truck.lower() == "yes".lower():
    truck = True
else:
    truck = False
    
if (truck and speed > 40) or (not truck and speed > 50):
    print("SLOW DOWN LOSER")
elif(speed > 30 ):
    print("NICE JOB DUMMY")
else:
    print("SPEED UP GRANNY")
    