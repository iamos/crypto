import sys # For Taking a console input
#define
ENC = 1
DEC = 0
KEY_ENC = 2
KET_DEC = 3
sbox = [
		0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
		0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
		0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
		0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
		0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
		0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
		0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
		0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
		0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
		0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
		0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
		0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
		0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
		0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
		0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
		0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
	]
isbox = [
		0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
		0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
		0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
		0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
		0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
		0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
		0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
		0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
		0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
		0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
		0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
		0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
		0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
		0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
		0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
		0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
	]

rcon = [
	0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
	0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39,
	0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a,
	0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8,
	0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef,
	0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc,
	0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b,
	0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3,
	0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94,
	0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20,
	0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35,
	0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f,
	0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04,
	0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63,
	0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd,
	0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d
]

def makeBlock(input_string):
	buff = [0] * 16;
	for x in range(16):
		buff[x] = ord(input_string[x]);
	return buff;

def strToHexStr(input_string):
	lens = len(input_string)
	block = [0]*lens
	for x in range(lens):
		block[x] = hex(ord(input_string[x]))[3:]
	return "".join(block)

def bprint(input_block):
	for x in range(len(input_block)//4):
		print(input_block[(4*x):(4*x)+4])

def sprint(input_block):
	for x in range(len(input_block)//4):
		print(chr(input_block[(4*x)]),chr(input_block[(4*x)+1]), chr(input_block[(4*x)+2]), chr(input_block[(4*x)+3]));

def hexprint(input_block):
	for x in range(len(input_block)//4):
		print(hex(input_block[(4*x)])[2:],hex(input_block[(4*x)+1])[2:], hex(input_block[(4*x)+2])[2:], hex(input_block[(4*x)+3])[2:]);

def subBytes(input_block,flag):
	buff = [0] * 16;

	if(flag == ENC):
		for x in range(16):
			buff[x] = sbox[input_block[x]]
	elif(flag == DEC):
		for x in range(16):
			buff[x] = isbox[input_block[x]]
	elif(flag == KEY_ENC):
		word = [0]*4
		for x in range(4):
			word[x] = sbox[input_block[x]]
		return word
	elif(flag == KET_DEC):
		word = [0]*4
		for x in range(4):
			word[x] = isbox[input_block[x]];
		return word
	return buff;

def mixColum(input_block,flag):
	matrix = [2,3,1,1,1,2,3,1,1,1,2,3,3,1,1,2]
	imatrix = [14,11,13,9,9,14,11,13,13,9,14,11,11,13,9,14]
	buff = [0] * 16;
	if (flag == ENC):
		buff = matrixMult(matrix, input_block)
	elif(flag == DEC):
		buff = matrixMult(imatrix,input_block)
	return buff

def matrixMult(A, B):
	buff = [0] * 16;
	for index in range(16):
		for offset in range(4):
			buff[index] ^= gf_mult(A[((4*(index//4))+offset)], B[((4*offset)+(index%4))])
	return buff

def shiftRow(input_block, flag):
	buff = [0] * 16;
	if(flag == ENC):
		for x in range(16):
			buff[x] = input_block[(x//4)*4+((x+(x//4))%4)];
	elif(flag == DEC):
		for x in range(4):
			buff[x] = input_block[x]
		buff[4] = input_block[7]
		buff[5] = input_block[4]
		buff[6] = input_block[5]
		buff[7] = input_block[6]
		buff[8] = input_block[10]
		buff[9] = input_block[11]
		buff[10] = input_block[8]
		buff[11] = input_block[9]
		buff[12] = input_block[13]
		buff[13] = input_block[14]
		buff[14] = input_block[15]
		buff[15] = input_block[12]
	return buff;

def gf_mult(a,b):
	p = 0x00;
	for counter in range(8):
		if b & 1 :
			p^=a;
		hi_bit = a & 0x80
		a <<= 1;
		a &= 0xFF;
		if hi_bit == 0x80:
			a ^=0x1b;
		b >>=1;
	return p;

def addRoundKey(input_block, key_block):
	buff = [0]*16;
	for index in range(16):
		buff[index] = input_block[index]^key_block[index]
	return buff

#def key_xor(a,b):
#	buffer = [0]*4;
#	for i in range(4):
#		buffer[i] = a[i] ^ b
#	return buffer

def keyRotate(word):
	buffer = [0]*4;
	buffer[0] = word[1]
	buffer[1] = word[2]
	buffer[2] = word[3]
	buffer[3] = word[0]
	return buffer

def keyExpansion_256(input_key):
	expansion_key = [0] * 240;
	for i in range(32):
		expansion_key[i] = ord(input_key[i]);
	i = 32
	while(i<240):
		if(i%32 == 0):
			rnd = i//32
			shiftbuffer = [0]*4
			for offset in range(4):
				shiftbuffer[offset] = expansion_key[i-4+offset]
			shiftbuffer = keyRotate(shiftbuffer)
			shiftbuffer = subBytes(shiftbuffer,KEY_ENC)
			shiftbuffer[0] = shiftbuffer[0] ^ rcon[rnd]
			for offset in range(4):
				expansion_key[i+offset] = expansion_key[i-32+offset] ^ shiftbuffer[offset]
			i = i+4
		elif( i%32 == 16):
			subbuffer = [0]*4
			for offset in range(4):
				subbuffer[offset] = expansion_key[i-4+offset]
			subbuffer = subBytes(subbuffer, KEY_ENC)
			for offset in range(4):
				expansion_key[i+offset] = expansion_key[i-32+offset] ^ subbuffer[offset]
			i = i + 4
		else:
			expansion_key[i] = expansion_key[i-4]^expansion_key[i-32];
			i = i+1
	return expansion_key

def aes_module_256(plaintext, key, flag):
	if(len(plaintext)!=16):
		print("Error:Plaintext must be 16 bytes\n len(plaintext):",len(plaintext))
		exit()
	if(len(key)!= 32):
		print("Error: Key must be 32 bytes\nlen(key):",len(key))
		exit()
	expansion_key = keyExpansion_256(key)
	block = makeBlock(plaintext)
	if( flag == ENC):		
		block = addRoundKey(block, expansion_key[0:16])

		for rnd in range(1,14):
			block = subBytes(block,ENC)
			block = shiftRow(block,ENC)
			block = mixColum(block,ENC)
			block = addRoundKey(block, expansion_key[(16*rnd):(16*rnd)+16])

		block = subBytes(block,ENC)
		block = shiftRow(block,ENC)
		block = addRoundKey(block,expansion_key[224:240])

	elif( flag == DEC):
		block = addRoundKey(block, expansion_key[224:240])
		for rnd in range(1,14):
			block = shiftRow(block,DEC)
			block = subBytes(block,DEC)
			block = addRoundKey(block, expansion_key[240-(16*rnd)-16:240-(16*rnd)])
			block = mixColum(block,DEC)

		block = subBytes(block,DEC)
		block = shiftRow(block,DEC)
		block = addRoundKey(block,expansion_key[0:16])
		
	p = [0]*16
	for index in range(16):
		p[index] = chr(block[index])
	return "".join(p)

def blockXor(string1, string2):
	if(len(string1)!=16 and len(string2)!=16):
		print("Error:blockXor( strlen != 16)")
		exit(1)
	buffer = [0]*16
	for x in range(16):
		buffer[x] = chr(ord(string1[x])^ord(string2[x]))
	string = "".join(buffer)
	return string

def nextTweak(input_key):
	nexttweak = [0]*16
	tweak = makeBlock(input_key)

	carry_in = 0
	carry_out = 0

	for j in range(16):
		carry_out = (tweak[j] >> 7) & 1
		nexttweak.append( ( (tweak[j]<<1)+ carry_in) & 0xff)
		carry_in = carry_out

	if carry_out:
		nexttweak[0] ^= 0x87

	temp =[0]*16
	for index in range(16):
		temp[index] = chr(nexttweak[index])
	string = "".join(temp)
	return string

def xts_module(plaintext, key1, T, flag):
	if(len(key1) != 32):
		print("xts_module : Key length Error")
		exit(1)
	if( flag == ENC or flag == DEC):
		PP = blockXor(plaintext,T)
		CC = aes_module_256(PP,key1,flag)
		C = blockXor(CC,T)
	else:
		print("xts_module : Flag Error")
		exit(1)
	return C

def xts_aes(plaintext, key, iv, flag):
	lenp = len(plaintext)
	extra = lenp%16
	num_of_module = 0
	string_buffer = ""

	key1 = key[:32]
	key2 = key[32:]
	tweak = aes_module_256(iv,key2,ENC)

	if(lenp>=16):
		if(lenp%16 == 0):
			num_of_module = lenp//16
		else:
			num_of_module = (lenp//16)+1
	else:
		num_of_module = 1
		print("Error: Size of Plaintext >= 16")
		exit(1)
	if(num_of_module ==1 or num_of_module == 2):
		print("XTS_MODE_1")

		cipher_left_buffer = xts_module(plaintext[(16*(num_of_module-2)):(16*(num_of_module-1))], key1, tweak, flag)
		cipher_right_buffer = cipher_left_buffer[extra:]
		cipher_left_buffer = cipher_left_buffer[:extra]
		temp_string = plaintext[(16*(num_of_module-1)):]+cipher_right_buffer

		tweak = nextTweak(tweak)
		string_buffer+=xts_module(temp_string,key1,tweak,flag)
		string_buffer+=cipher_left_buffer

	else:
		print("XTS_MODE_2")
		for blocks in range(num_of_module-2):
			string_buffer +=xts_module(plaintext[(16*blocks):(16*blocks+16)], key1, tweak, flag)
			tweak = nextTweak(tweak)

		cipher_left_buffer = xts_module(plaintext[(16*(num_of_module-2)):(16*(num_of_module-1))], key1, tweak, flag)
		cipher_right_buffer = cipher_left_buffer[extra:]
		cipher_left_buffer = cipher_left_buffer[:extra]
		temp_string = plaintext[(16*(num_of_module-1)):]+cipher_right_buffer

		tweak = nextTweak(tweak)
		string_buffer+=xts_module(temp_string,key1,tweak,flag)
		string_buffer+=cipher_left_buffer
	return string_buffer

sysinput_flag = sys.argv[1]
if(sysinput_flag == "ENC"):
	#kk = input("Key :")
	#pp = input("Plaintext :")
	#initial_vector = input("i :")
	kk = "D3KJGF9FJSIEIFKGJFIBM39GHKF9GLF9FLDLFKF09HGJWMCBLD0234JDKDZQD390"
	#pp = "GFKGI20SD294JD9FJDK209SWJKODFXCJNKLFDJIGJKDFIGJDJKFL2DL"
	pp = "abcdefghijklmnopqursuvwxyz"
	initial_vector = "SKEFCKVI29DOIFOS"
	#kk = "D3KJGF9FJSIEIFKGJFIBM39GHKF9GLF9FLDLFKF09HGJWMCBLD0234JDKDZQD399"
	#pp = "Information.Security.and.Privacy"
	#initial_vector = "0123456789abcdef"

	print(len(pp))

	asdf = xts_aes(pp,kk,initial_vector,ENC)
	print("\n\n*Encryption Done")
	print("Plaintext         :",pp)
	print("Cipher text       :",asdf)
	print("Cipher text (Hex) :",strToHexStr(asdf))

	fdsa = xts_aes(asdf,kk,initial_vector,DEC)
	print("\n\n*Decryption Done")
	print("Plaintext         :",asdf)
	print("Cipher text       :",fdsa)
	print("Cipher text (Hex) :",strToHexStr(fdsa))

elif( sysinput_flag == "DEC"):
	kk = input("Key :")
	pp = input("Plaintext :")
	initial_vector = input("i :")
	asdf = xts_aes(pp,kk,initial_vector,DEC)
	print("*Decryption Done")
	print("Plaintext         :",pp)
	print("Cipher text       :",asdf)
	print("Cipher text (Hex) :",strToHexStr(asdf))
else:
	print("Usage : python3 aes_256.py [ENC,DEC]")

#kk = D3KJGF9FJSIEIFKGJFIBM39GHKF9GLF9FLDLFKF09HGJWMCBLD0234JDKDZQD390
#SKEFCKVI29DOIFOS