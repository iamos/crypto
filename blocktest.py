# def foo(a):
# 	for x in range(16):
# 		for offset in range(4):
# 			buff[x] ^= gf_mult(a[4*(x//4)+offset], b[(x//4)+])

def matx(index):
	for offset in range(4):
		print((4*(index//4)+offset));

def maty(index):
	for offset in range(4):
		print( ((4*offset)+(index%4)));

maty(9)