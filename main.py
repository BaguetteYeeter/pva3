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
    thebios.cpu.tick(thebios)
    print(thebios.cpu.Registers.A)
    print(thebios.cpu.Registers.CurrentInstruction)