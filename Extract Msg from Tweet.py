
# Requires tweets to be in an array
tweet_array = ['*nuzzles*#12345', 'goodmorning.#12345', 'hello!#12345', 'Goodbye.#12345', 'where are you!#12345', 'the end#12345']
tweet_extract = '0'

# For loop to extract the last character of each sentence.
# The start of the message is identfied with the tweet ending with the '*' character.
# Tweets that end with a . or ! will be added to tweet_extract
# The message will end when the last character of the tweet is not any of the three above characters.


for word in tweet_array:
    if word[-7:-6] == '*':
        f= open('msg.txt', 'a+')
        f.write(' Start msg ')
        f.close()
    elif word[-7:-6] == '.':
        tweet_extract = tweet_extract + '0'
        print(tweet_extract)
    elif word[-7:-6] == '!':
        tweet_extract = tweet_extract + '1'
        print(tweet_extract)
    else:
        break

# definiton for Text to bits
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

# convert binary to text
original_input_file = text_from_bits(tweet_extract)

# Append converted message to our text file
f=open('msg.txt', 'a+')
f.write(original_input_file + ' end msg ')
f.close()

# print out of secret message
print(original_input_file)


