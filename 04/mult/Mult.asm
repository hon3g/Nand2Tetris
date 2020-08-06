// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// for (i=0, i<R0, i++): R2 = R2 + R1

    @R2
    M=0     // initialize product to 0

    @R0
    D=M
    @n
    M=D   // n = R0

    @R1
    D=M
    @END
    D;JEQ   // goto END if R1=0

(LOOP)
    @n
    D=M
    @END
    D;JEQ   // goto END if n=0

    @R1
    D=M
    @R2
    M=M+D   // R2 = R2+R1

    @n
    M=M-1   // n = n-1

    @LOOP
    0;JMP

(END)
    @END
    0;JMP
