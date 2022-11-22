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

def mul(bios: bios.BIOS) -> None:
    a = bios.cpu.Registers.A
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    b = ord(bios.ram.fetch(address, 1))
    bios.cpu.Registers.A = a * b

def div(bios: bios.BIOS) -> None:
    a = bios.cpu.Registers.A
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    b = ord(bios.ram.fetch(address, 1))
    bios.cpu.Registers.A = int(a / b)

def mod(bios: bios.BIOS) -> None:
    a = bios.cpu.Registers.A
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    b = ord(bios.ram.fetch(address, 1))
    bios.cpu.Registers.A = int(a % b)

def dec(bios: bios.BIOS) -> None:
    bios.cpu.Registers.A -= 1

def inc(bios: bios.BIOS) -> None:
    bios.cpu.Registers.A += 1

def jmp(bios: bios.BIOS) -> None:
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    bios.cpu.Registers.CurrentInstruction = address

def je(bios: bios.BIOS) -> None:
    if bios.cpu.Registers.A == bios.cpu.Registers.B:
        jmp(bios)
    else:
        bios.cpu.Registers.CurrentInstruction += 2

def jne(bios: bios.BIOS) -> None:
    if bios.cpu.Registers.A != bios.cpu.Registers.B:
        jmp(bios)
    else:
        bios.cpu.Registers.CurrentInstruction += 2

def jg(bios: bios.BIOS) -> None:
    if bios.cpu.Registers.A > bios.cpu.Registers.B:
        jmp(bios)
    else:
        bios.cpu.Registers.CurrentInstruction += 2

def jge(bios: bios.BIOS) -> None:
    if bios.cpu.Registers.A >= bios.cpu.Registers.B:
        jmp(bios)
    else:
        bios.cpu.Registers.CurrentInstruction += 2

def jl(bios: bios.BIOS) -> None:
    if bios.cpu.Registers.A < bios.cpu.Registers.B:
        jmp(bios)
    else: 
        bios.cpu.Registers.CurrentInstruction += 2

def jle(bios: bios.BIOS) -> None:
    if bios.cpu.Registers.A <= bios.cpu.Registers.B:
        jmp(bios)
    else:
        bios.cpu.Registers.CurrentInstruction += 2

def lda(bios: bios.BIOS) -> None:
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    data = ord(bios.ram.fetch(address, 1))
    bios.cpu.Registers.A = data

def ldb(bios: bios.BIOS) -> None:
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    data = ord(bios.ram.fetch(address, 1))
    bios.cpu.Registers.B = data

def ldc(bios: bios.BIOS) -> None:
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    data = ord(bios.ram.fetch(address, 1))
    bios.cpu.Registers.C = data

def ldd(bios: bios.BIOS) -> None:
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    data = ord(bios.ram.fetch(address, 1))
    bios.cpu.Registers.D = data

def sta(bios: bios.BIOS) -> None:
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    bios.ram.set(address, chr(bios.cpu.Registers.A))

def stb(bios: bios.BIOS) -> None:
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    bios.ram.set(address, chr(bios.cpu.Registers.B))

def stc(bios: bios.BIOS) -> None:
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    bios.ram.set(address, chr(bios.cpu.Registers.C))

def std(bios: bios.BIOS) -> None:
    address = bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 2)
    bios.cpu.Registers.CurrentInstruction += 2
    address = ord(address[0]) + (ord(address[1]) * 0x100)
    bios.ram.set(address, chr(bios.cpu.Registers.D))

def sea(bios: bios.BIOS) -> None:
    data = ord(bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 1))
    bios.cpu.Registers.CurrentInstruction += 1
    bios.cpu.Registers.A = data

def seb(bios: bios.BIOS) -> None:
    data = ord(bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 1))
    bios.cpu.Registers.CurrentInstruction += 1
    bios.cpu.Registers.B = data

def sec(bios: bios.BIOS) -> None:
    data = ord(bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 1))
    bios.cpu.Registers.CurrentInstruction += 1
    bios.cpu.Registers.C = data

def sed(bios: bios.BIOS) -> None:
    data = ord(bios.ram.fetch(bios.cpu.Registers.CurrentInstruction, 1))
    bios.cpu.Registers.CurrentInstruction += 1
    bios.cpu.Registers.D = data

codes = {0x00: nop, 0x01: add, 0x02: sub, 0x03: mul, 0x04: div, 0x05: mod, 0x0e: dec, 0x0f: inc, 0x10: jmp, 0x11: je, 0x12: jne, 0x13: jg, 0x14: jge, 0x15: jl, 0x16: jle, 0xa1: lda, 0xa2: ldb, 0xa3: ldc, 0xa4: ldd, 0xb1: sta, 0xb2: stb, 0xb3: stc, 0xb4: std, 0xc1: sea, 0xc2: seb, 0xc3: sec, 0xc4: sed}