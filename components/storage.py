class FloppyController:
    def __init__(self) -> None:
        self.disks = []
    class Disk:
        def __init__(self, file: str) -> None:
            f = open(file, "r", encoding="latin-1")
            self.data = f.read()
            f.close()