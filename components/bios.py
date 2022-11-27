from . import ram, cpu

class BIOS:
    def __init__(self, devices: dict) -> None:
        self.cpu: cpu.CPU = devices.get("cpu")
        self.ram: ram.RAM = devices.get("ram")
        self.video = devices.get("video")
        self.floppy = devices.get("floppy")
        self.devmap = {
            0x00: self,
            0x01: self.cpu, 
            0x05: self.ram,
            0x10: self.video,
            0x80: self.floppy
        }
    def call(self, devid: int, message):
        device = self.devmap.get(devid)
        if not device:
            return
        if devid == 0:
            self.bios_call(message)
            return
        device.call(self, message)
    def bios_call(self, message):
        pass