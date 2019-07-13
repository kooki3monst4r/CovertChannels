
# Requires tweets to be in an array
tweet_array = ['goodmorning.', 'hello!', 'Goodbye.', 'where are you!', 'the end']
tweet_extract = ''
# For loop to extract the last character of each sentence.  This will stop when the character is not a ! or a .
for word in tweet_array:
    if word[-1:] == '.' or  word[-1:] == '!':
        tweet_extract = tweet_extract + word[-1:]
    else:
        break

# definiton for Text to bits
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

# Replace all ! with 1 and all . with 0
tweet_extract_one = (tweet_extract.replace('!', '1'))
tweet_extract_final = tweet_extract_one.replace('.', '0')

# convert binary to text
original_input_file = text_from_bits(tweet_extract_final)

# print out of secret message
print(original_input_file)


