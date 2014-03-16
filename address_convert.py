import sys
import getopt

def normalize_to_hex(address):
	blocks=address.split(':')
	octects=[]
	if address.count(":") != 7:
		'''Auslassungen'''
		for i in range(len(blocks)):
			if blocks[i] == "":#ausgelassene Stelle finden
				blocks[i] ="0"
				for j in range (7-address.count(":")):
					blocks.insert(i,"0")
	blocks = [i.zfill(4) for i in blocks]
	for block in blocks:
		octects.append(block[:2])
		octects.append(block[2:])
	return octects

def convert_singlehex(address):
	hex_octects=[]
	octects=normalize_to_hex(address)
	for octect in octects:
		hex_octects.append(''.join([str(octect),'.']))
	hex_octects=''.join(hex_octects)
	#remove the last dot
	return hex_octects[0:len(hex_octects)-1]

def convert_bin(address):
	bin_octects=[]
	octects=normalize_to_hex(address)
	for octect in octects:
		bin_octects.append(str(bin(int(octect,16))[2:]))
	
	bin_octects = [i.zfill(8) for i in bin_octects]
	bin_octects=''.join(bin_octects)[::]
	return bin_octects

def convert_decimal(address):
	dec_octects=[]
	octects=normalize_to_hex(address)
	#add the dots
	for octect in octects:
		dec_octects.append(''.join([str(int(octect,16)),'.']))
	dec_octects=''.join(dec_octects)
	#remove the last dot
	return dec_octects[0:len(dec_octects)-1]

def print_address(address,prefix):
	print "Got this address:",address,"/",prefix

def address_info(address,prefix):
	pass

def main(argv=None):
	addr=""
	prefix=""
	try:
		opts, args = getopt.getopt(sys.argv[1:],"i:p:h")
		for opt,arg in opts:
			if opt == "-i":
				addr= arg
			if opt == "-p":
				prefix= arg
	except getopt.error, msg:
		print msg
		sys.exit(2)
	
	if addr.count(":") > 7:
		print "invalid ipv6 address"
		sys.exit(2)
	print_address(addr,prefix)
	print "in Decimal:",convert_decimal(addr)
	print "in Hex:", convert_singlehex(addr)
	print "in Binary:", convert_bin(addr)
	print address_info(addr,prefix)

if __name__ == "__main__":
	main()