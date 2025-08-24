def validate_ip(ip_address):
    if ip_address == "end":
        print("shutting down calculator")
    else:
        ip = ip_address.split(".")

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
            hosts = input("number of hosts per subnet: ")
            subnet_calculator(ip, hosts)
            # print(calculator)


def ip_class(first_octet):
    if int(first_octet) <= 126:
        return f"OOPS! cannot calculate subnet for class-A address"
    elif 127 < int(first_octet) <= 191:
        return f"OOPS! cannot calculate subnet for class-B address"
    else:
        return f"OOPS! cannot calculate subnet for reserved ip-address range"


def subnet_calculator(ip, hosts):
    num_of_hosts = int(hosts)

    first_octet = ip[0]
    second_octet = ip[1]
    third_octet = ip[2]
    # fourth_octet = ip[3]

    if 191 < int(first_octet) < 224:
        host_err = False
        new = 0
        if num_of_hosts <= 2:
            new = 4
        elif num_of_hosts <= 6:
            new = 8
        elif num_of_hosts <= 14:
            new = 16
        elif num_of_hosts <= 30:
            new = 32
        elif num_of_hosts <= 62:
            new = 64
        elif num_of_hosts <= 126:
            new = 128
        elif num_of_hosts <= 254:
            new = 255
        else:
            host_err = True
            print("[ERROR]: cannot resolve number of hosts")

        #printing out subnet value
        if host_err == False:
            subnets = [0]
            for subnet in subnets:
                print(f"subnets: {first_octet}.{second_octet}.{third_octet}.{subnet}")
                new = new + subnet
                if new < 255:
                    subnets.append(new)
                else:
                    break
    else:
        show_class = ip_class(first_octet)
        print(show_class)