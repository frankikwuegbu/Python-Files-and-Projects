class Log:
    def __init__(self, log_message, interface, device):
        self.log_message = log_message
        self.interface = interface
        self.device = device
    def show_log(self):
        print(f"[{self.device}]: {self.interface} {self.log_message}")
    