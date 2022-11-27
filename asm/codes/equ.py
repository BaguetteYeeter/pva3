def compile(chunks, finished_program, pointer):
    register_sh = chr(int(chunks[2], base=16))
    register_fh = chr(int(chunks[3], base=16))
    value = chr(int(chunks[4], base=16))
    finished_program[ord(register_fh) + (ord(register_sh) * 0x100)] = value
    return finished_program, pointer