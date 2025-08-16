ip_address = input("enter ip address here: ")
ip = ip_address.split(".")

def validate_ip():
    count = 0
    octet_error = False

    #validating value of each octet
    for octet in ip:
        if int(octet) <= 255:
            count += 1
        else:
            octet_error = True
            print("[ERROR] invalid ip format. Octet value cannot be greater than 255")
            break
    
    #validating that ip address has four groups of numbers
    if count != 4 and octet_error == False:
        print("[ERROR] invalid ip format. Four octets expected")
    elif count == 4 and octet_error == False:
        print("valid ip")

validate_ip()