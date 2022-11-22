import array

class RAM:
    def __init__(self) -> None:
        self.memory = array.array('u', chr(0)*65535)
    def fetch(self, addr: int, len: int) -> str:
        data = ""
        for i in range(0, len):
            try:
                value = self.memory[addr+i]
            except Exception:
                return 0
            data += value
        return data
    def set(self, addr: int, val: str) -> None:
        for i in range(0, len(val)):
            self.memory[addr+i] = val[i]
