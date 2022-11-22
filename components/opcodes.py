from . import bios

def nop(bios: bios.BIOS) -> None:
    pass

def add(bios: bios.BIOS) -> None:
    a = bios.cpu.Registers.A
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    b = ord(bios.ram.fetch(address, 1))
    bios.cpu.Registers.A = a + b

def sub(bios: bios.BIOS) -> None:
    a = bios.cpu.Registers.A
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    b = ord(bios.ram.fetch(address, 1))
    bios.cpu.Registers.A = a - b

codes = {0x00: nop, 0x01: add, 0x02: sub}