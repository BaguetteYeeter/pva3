from components import bios, cpu, opcodes, ram, storage, graphics

cpu = cpu.CPU()
ram = ram.RAM()
devices = {}
devices["cpu"] = cpu
devices["ram"] = ram
video = graphics.VideoController()
devices["video"] = video
floppycontroller = storage.FloppyController()
floppycontroller.disks.append(storage.FloppyController.Disk("disk.img"))
devices["floppy"] = floppycontroller
thebios = bios.BIOS(devices)

bootdisk: storage.FloppyController.Disk = floppycontroller.disks[0]
thebios.ram.set(0x0, bootdisk.data)

#thebios.video.print("Booting", foreground=(170, 170, 170), background=(0, 0, 255))

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