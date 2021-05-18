# gh0u1
# made on May 18, 2021

'''This program implements an XOR cipher in python'''

# XOR uses the same function to decrypt and encrypt
def encryptDecrypt(inpString):

	# Define XOR key
	# Any character value will work
	xorKey = 'P';

	# calculate length of input string
	length = len(inpString);

	# perform XOR operation of key
	# with every caracter in string
	for i in range(length):
	
		inpString = (inpString[:i] +
			chr(ord(inpString[i]) ^ ord(xorKey)) +
					inpString[i + 1:]);
		print(inpString[i], end = "");
	
	return inpString;

# Driver Code
if __name__ == '__main__':
	sampleString = "Going forward with my quantum club I need to make a plan fo what it entails for members and requirements, compile a list of professional speakers who would come talk at NAU, set up the collaborative think journal for the club, set up the discord server, and send out a flyer to CEIAS and Natural Sciences students. I want to name the club Open Source Quantum and it will have 2 general focus areas, one on CS and Communications, and the other oriented to Natural Sciences and quantum applications in places like Chemistry, Physics, Mathematics, and Biology. I think this will be a massive field someday and I am starting the club In hopes the development of early networks of researchers for the field will allow for career opportunities and allow research to be truly collaborative. Quantum Computation makes this possible because of its open source nature in things like Qiskit and Cirq and even Q# to some extent. It is this open-source nature that will allow students to ge involved in this even as undergraduates and allow for great leaps to be made in understanding the theory and informatics of quantum mechanics."; # Plain-text goes here

	# Encrypt the string
	print("Encrypted String: ", end = "");
	sampleString = encryptDecrypt(sampleString);
	print("\n");

	# Decrypt the string
	print("Decrypted String: ", end = "");
	encryptDecrypt(sampleString);
