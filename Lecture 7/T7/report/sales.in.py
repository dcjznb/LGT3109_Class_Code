file1 = open("sales.in.txt", "r")
for line in file1:
    line = line.strip()
    if line == "-1":
        break
    customer_info = line.split(", ")
    customer_id = customer_info[0]
    customer_name = customer_info[1]
    product_name = customer_info[2]
    promotion_code = customer_info[3]
    print(
        f"Dear {customer_name}, Thank you for purchasing {product_name}. You can use the following promotion code to receive a 20% discount in your next purchasing.\n\n{promotion_code}\n\nWish you Merry Christmas and Happy New year!\n\nRegards,\nCompany PolyU\n"
    )

file1.close()
