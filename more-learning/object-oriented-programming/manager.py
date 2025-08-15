from oop import Router
from log import Log

router_one = Router("edge router", "edgerouterpass", "192.168.10.1")
# print(router_one.host_name)
# router_one.router_info()

router_two = Router("core router", "corerouterpass", "192.168.10.2")
# router_two.router_info()

#using clas method to change attribute
router_one.change_hostname("boarder router")
# router_one.router_info()

log_one = Log("interface moved to UP/UP", "gigabit-ethernet0/0", router_one.host_name)
log_one.show_log()