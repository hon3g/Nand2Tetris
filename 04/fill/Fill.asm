// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


(START)
    // arr = SCREEN(16384)
    @SCREEN
    D=A
    @arr
    M=D

    // n = 8192
    @8192
    D=A
    @n
    M=D

    // init i=0
    @i
    M=0

    // probe keyboard
    @KBD
    D=M
    @BLOOP
    D;JNE
    @WLOOP
    D;JEQ

(BLOOP)
    // if (i=n) goto START
    @i
    D=M
    @n
    D=D-M
    @START
    D;JEQ

    // RAM[arr+i] = -1
    @arr
    D=M
    @i
    A=D+M
    M=-1

    // i++
    @i
    M=M+1

    @BLOOP
    0;JMP

(WLOOP)
    // if (i=n) goto START
    @i
    D=M
    @n
    D=D-M
    @START
    D;JEQ

    // RAM[arr+i] = 0
    @arr
    D=M
    @i
    A=D+M
    M=0

    // i++
    @i
    M=M+1

    @WLOOP
    0;JMP
