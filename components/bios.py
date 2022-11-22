from . import cpu, ram

class BIOS:
    def __init__(self, cpu: cpu.CPU, ram: ram.RAM) -> None:
        self.cpu = cpu
        self.ram = ram