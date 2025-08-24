from subnet_calculator import validate_ip

ip_address = ""

while ip_address != "end":
    ip_address = input("enter ip address here: ")
    validate_ip(ip_address)