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
        address_class = ip_class(ip_address)
        print(address_class)


def ip_class(address):
    if int(first_octet) <= 126:
        return f"{address} is a class A ip address; {address}/8"
    elif 127 < int(first_octet) <= 191:
        return f"{address} is a class B ip address; {address}/16"
    elif 191 < int(first_octet) <= 223:
        return f"{address} is a class C ip address; {address}/24"
    else:
        return f"{address} falls in the reserved address range"


ip_address = input("enter ip address here: ")
ip = ip_address.split(".")
first_octet = ip[0]

validate_ip()