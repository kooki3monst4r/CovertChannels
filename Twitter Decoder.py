import tweepy


def login():
    # Twitter credentials


    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # api is the main tweepy class we're going to use to make this work
    api = tweepy.API(auth)

    # Check to make sure we can authenticate before we begin.
    # Prevents ya boi from trying to do this without an internet connection
    try:
        api.verify_credentials()
        print("I'm in...")
    except:
        print("You didn't say the magic word!")

    return api


# Method reaches out to Twitter, pulls down new messages, and returns a string with them in it
def get_message(api):
    # List to hold the extracted message. Using a list rather than a string because a string is immutable.
    # Not good practice to continually modify an immutable
    encoded_msg_list = []

    # Go through each message in the timeline we're posting the tweets to
    for status in tweepy.Cursor(api.user_timeline, screen_name='@DailyDoseOfSad1', tweet_mode="extended").items():
        # print(status.full_text)
        encoded_msg_list.insert(0, status.full_text[-7])  # Prepend the last character (the sensitive message) into a list

    # Join the list to an empty string once it's full, to avoid memory allocation to immutable string type

    # List to hold binary message
    msg_list = []

    # Post process the string. A . is a 0 and a ! is a 1.
    for char in encoded_msg_list:
        if char == ".":
            msg_list.append('0')
        elif char == '!':
            msg_list.append('1')

    msg = ''.join(msg_list)

    return msg


# Converts binary string to bits
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


if __name__ == '__main__':
    api = login()

    msg = get_message(api)

    # convert binary to text
    original_input_file = text_from_bits(msg)

    # Append converted message to our text file
    f = open('msg.txt', 'a+')
    f.write(original_input_file + ' end msg ')
    f.close()

    # print out of secret message
    print(original_input_file)

