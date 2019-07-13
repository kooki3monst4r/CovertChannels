# Twitter Sender
# Encode a text file to a binary array
# Create an inputfile.txt in same folder as str2bin

# open inputfile
# f = open('inputtxtfile.txt', 'r')

# set contents of text file to variable file_contents
#input_contents = f.read()
input_contents = 'test str'


# Definition to convert text to binary
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


# Convert input file to binary
output_contents = text_to_bits(input_contents)

# Convert binary output to an array
output_array = list(output_contents)

print(output_array)
