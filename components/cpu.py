from . import opcodes
from . import bios

class CPU:
    def __init__(self) -> None:
        self.name = "BDD Phantom 100"
        self.model_number = "BDDPH100100"
        self.serial_number = "BPHA100001AAAA"
    class Registers:
        CurrentInstruction = 0
        A = 0 # Accumulator
        B = 0 # Base
        C = 0 # Counter
        D = 0 # Data
    def tick(self, bios: bios.BIOS):
        data = ord(bios.ram.fetch(self.Registers.CurrentInstruction, 1))
        self.Registers.CurrentInstruction += 1
        try:
            instruction = opcodes.codes[data]
        except Exception:
            instruction = opcodes.nop
        instruction(bios)