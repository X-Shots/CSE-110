with open("hr_system.txt") as lines:
    for line in lines:
        line = line.strip()
        parts = line.split(" ")
        if(parts[2] == "Engineer"):
            print(f"{parts[0]}(ID: {parts[1]}), {parts[2]} - ${((int(parts[3])/24.0) + 1000):.2f}")
        else:
               
            print(f"{parts[0]}(ID: {parts[1]}), {parts[2]} - ${int(parts[3])/24.0:.2f}")
        