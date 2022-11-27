def compile(chunks, finished_program, pointer):
    value = chr(int(chunks[1], base=16))
    finished_program[pointer] = value
    pointer += 1
    if chunks[2] == "$":
        register_sh = chr(int(chunks[3], base=16))
        register_fh = chr(int(chunks[4], base=16))
        finished_program[pointer] = register_fh
        pointer += 1
        finished_program[pointer] = register_sh
        pointer += 1
        return finished_program, pointer