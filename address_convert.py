import sys
import getopt

def normalize_to_hex(address):
	'''fills the missing colons and words, if the address contains zeros'''
	blocks=address.split(':')
	words=[]
	if address.count(":") != 7:
		'''Auslassungen'''
		for i in range(len(blocks)):
			if blocks[i] == "":#ausgelassene Stelle finden
				blocks[i] ="0"
				for j in range (7-address.count(":")):
					blocks.insert(i,"0")
	blocks = [j.zfill(4) for j in blocks]
	for block in blocks:
		words.append(block.strip()[0:2])
		words.append(block.strip()[2:])
	return words



def convert_singlehex(address):
	'''coverts an ipv6 address from a : separated string to a . separated string'''
	hex_octects=[]
	octects=normalize_to_hex(address)
	for octect in octects:
		hex_octects.append(''.join([str(octect),'.']))
	hex_octects=''.join(hex_octects)
	#remove the last dot
	return hex_octects[0:len(hex_octects)-1]


def convert_bin(address):
	'''converts an ipv6 address from a : separated string to a string that represents the address in binary'''
	bin_words=[]
	words=normalize_to_hex(address)
	for word in words:
		bin_words.append(''.join([str(bin(int(word,16))[2:]).zfill(8),'.']))
	bin_words=''.join(bin_words)[::]
	return bin_words[0:len(bin_words)-1]

def convert_decimal(address):
	'''converts an ipv6 address from a colon separated string to a string that represents the address in Decimal'''
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

def get_prefix(address,prefix):
	bin_addr = convert_bin(address)
	return bin_addr[:int(prefix)]

def get_int_identifier(address,prefix):
	bin_addr = convert_bin(address)
	return bin_addr[int(prefix):]

def convert_bin_to_hex(address):
	return hex(int(address))[2:]

def address_info(address,prefix):
	'''examins the address and displays the type of the ipv6 address, link local, eg.'''
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
	print "Praefix in Binary", get_prefix(addr,prefix)
	print "Interface Identifier in Binary", get_int_identifier(addr,prefix)

if __name__ == "__main__":
	main()