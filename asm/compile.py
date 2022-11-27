from codes import nop, add, sub, mul, div, mod, dec, inc, jmp, je, jne, jg, jge, jl, jle, lda, ldb, ldc, ldd, sta, stb, stc, std, sea, seb, sec, sed, equ, reg, call
import sys
import getopt

input_file = "prg.pyasm"
out_file = "disk.img"

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["input=", "output="])
except getopt.GetoptError:
    print("compile.py -i [file] -o [file]")
    sys.exit(2)
for opt, arg in opts:
    if opt == "-h":
        print("compile.py -i [file] -o [file]")
        sys.exit()
    elif opt in ("-i", "--input"):
        input_file = arg
    elif opt in ("-o", "--output"):
        out_file = arg

codes = {"nop": 0x00, "add": 0x01, "sub": 0x02, "mul": 0x03, "div": 0x04, "mod": 0x05, "dec": 0x0e, "inc": 0x0f, "jmp": 0x10, "je": 0x11, "jne": 0x12, "jg": 0x13, "jge": 0x14, "jl": 0x15, "jle": 0x16, "lda": 0xa1, "ldb": 0xa2, "ldc": 0xa3, "ldd": 0xa4, "sta": 0xb1, "stb": 0xb2, "stc": 0xb3, "std": 0xb4, "sea": 0xc1, "seb": 0xc2, "sec": 0xc3, "sed": 0xc4, "reg": 0xaa, "call": 0x41}

finished_program = [chr(0) for i in range(512)]
pointer = 0

f = open(input_file, "r")
asm_program = f.read().splitlines()
f.close()

for line in asm_program:
    if line in ["", " "]:
        continue
    chunks = line.split(" ")
    if chunks[0].lower() in codes:
        finished_program[pointer] = chr(codes[chunks[0].lower()])
        pointer += 1
        exec("finished_program, pointer = "+chunks[0].lower()+".compile(chunks, finished_program, pointer)")
        continue
    else:
        exec("finished_program, pointer = "+chunks[0].lower()+".compile(chunks, finished_program, pointer)")
        continue

f = open(out_file, "w", encoding="latin-1")
f.write("".join(finished_program))
f.close()

"""
for k, v in codes.items():
        if chunks[0].lower() == v:
            finished_program[pointer] = chr(k)
            pointer += 1
            exec("finished_program, pointer = "+v+".compile(chunks, finished_program, pointer)")
            continue
"""