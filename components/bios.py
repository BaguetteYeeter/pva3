from . import cpu, ram, graphics

class BIOS:
    def __init__(self, cpu: cpu.CPU, ram: ram.RAM, video: graphics.VideoController) -> None:
        self.cpu = cpu
        self.ram = ram
        self.video = video