import tweepy


# Logs into api.twitter.com using the app credentials the team created.
# Returns an api for the rest of the program to use
def login():


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
        if status.full_text[-6] == '#':
            encoded_msg_list.insert(0, status.full_text[
                -7])  # Prepend the last character (the sensitive message) into a list
        elif status.full_text[-7] == '#':
            encoded_msg_list.insert(0, status.full_text[
                -8])  # Prepend the last character (the sensitive message) into a list

    # List to hold binary message
    msg_list = []

    # Post process the string. A . is a 0 and a ! is a 1.
    for char in encoded_msg_list:
        if char == ".":
            msg_list.append('0')
        elif char == '!':
            msg_list.append('1')

    # Join the list to an empty string once it's full, to avoid memory allocation to immutable string type
    return ''.join(msg_list)


# Converts binary string to bits
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    if bits.__len__() != 0:
        int_msg = int(bits, 2)
        return int_msg.to_bytes((int_msg.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    else:
        return "No valid message found"

if __name__ == '__main__':
    # Login to api.twitter.com
    api = login()

    # Gets all messages from the hosting account
    msg = get_message(api)

    # Converts the extracted binary message to text
    secret_msg = text_from_bits(msg)
    # print(secret_msg)

    # Append converted message to our text file
    file = open('msg.txt', 'a+')
    file.write(secret_msg + ' EOF \n')
    file.close()
