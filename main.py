from components import bios, cpu, opcodes, ram, storage

cpu = cpu.CPU()
ram = ram.RAM()
floppycontroller = storage.FloppyController()
floppycontroller.disks.append(storage.FloppyController.Disk("disk.img"))
thebios = bios.BIOS(cpu, ram)

bootdisk: storage.FloppyController.Disk = floppycontroller.disks[0]
thebios.ram.set(0x0, bootdisk.data)

while True:
    input()
    print("A", thebios.cpu.Registers.A)
    print("B", thebios.cpu.Registers.B)
    print("CIR", thebios.cpu.Registers.CurrentInstruction)
    print("0031", ord(thebios.ram.fetch(0x0031, 1)))
    print("TICK")
    thebios.cpu.tick(thebios, opcodes)
    print("A", thebios.cpu.Registers.A)
    print("B", thebios.cpu.Registers.B)
    print("CIR", thebios.cpu.Registers.CurrentInstruction)
    print("0031", ord(thebios.ram.fetch(0x0031, 1)))