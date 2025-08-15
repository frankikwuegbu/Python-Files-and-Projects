# print("hello world")
class Router:
    def __init__(self, host_name, secret, ip_address):
        self.host_name = host_name
        self.secret = secret
        self.ip_address = ip_address
    
    def change_hostname(self, new_hostname):
        self.host_name = new_hostname
    
    def change_secret(self, new_secret):
        self.secret = new_secret

    def router_info(self):
        print(f"host name: {self.host_name}\npassword: *****\nip address: {self.ip_address}")