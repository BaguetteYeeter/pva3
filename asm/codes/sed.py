def compile(chunks, finished_program, pointer):
    value = chr(int(chunks[1], base=16))
    finished_program[pointer] = value
    pointer += 1
    return finished_program, pointer