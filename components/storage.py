class FloppyController:
    def __init__(self) -> None:
        self.disks = []
    class Disk:
        def __init__(self, file: str) -> None:
            f = open(file, "r")
            self.data = f.read()
            f.close()