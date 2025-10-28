input_file = input("Enter input file name: ")
max_qty = -1

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if line == "-1" or not line:  # check if it's empty line or -1
            continue
        part = line.split(" ")
        qty = int(part[2])
        origin = part[0]
        destination = part[1]
        if qty > max_qty:
            max_qty = qty
if max_qty != -1:
    print(f"The largest shipping quantity from {origin} to {destination} is {max_qty}.")
