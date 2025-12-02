class SmartHomeSystem:    
    def __init__(self, *args):
        self.devices = {}

        if len(args) == 0:
            return
            
        if len(args) == 1 and isinstance(args[0], dict):
            self.devices = args[0].copy()
            return

        if len(args) == 2 and all(isinstance(arg, str) for arg in args):
            self.devices = {args[0]: args[1]}
            return
            
        raise ValueError("Invalid initialization arguments. Use either: no args, dict, or two strings")

    def add_device(self, device_name, device_type):
        pass
        
    def control_device(self, device_name, action):
        pass
        
    def __str__(self):
        return "\n".join(f"{name}:{status}" for name, status in self.devices.items())