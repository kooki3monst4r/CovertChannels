import tweepy
import time
import random

# Twitter credentials
consumer_key = 'XXXX'
consumer_secret = 'XXXX'
access_token = 'XXXX'
access_token_secret = 'XXXX'

# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    """Definition to convert text to binary"""
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


if __name__ == '__main__':
    # API is the main tweepy class we're going to use to interact with twitter
    api = tweepy.API(auth)

    # The start message and end message will indicate to the decoder the beginning and end of a new encoded
    # transmission. This isn't fully used in this version, but is built in for future use.
    startmsg = "A drop from the moon dropped and disappeared into a room into my heart *nuzzles*"
    endmsg = "So tell me, what’s it like living in a constant haze of stupidity?"

    # The . at the end indicates to the decoder this is a 0
    message0 = ["We each need to find our own inspiration. Sometimes, it is not easy.",
                "Giving up is what kills people.",
                "The world is not perfect, but it is there for us trying the best it can.",
                "If you win, you live. If you lose, you die. If you don’t fight, you can’t win.",
                "No matter how deep the night, it always turns to day, eventually.",
                "A castle that vanishes at the first gust of wind is worthless.",
                "A skyscraper built within your mind will never fall down.",
                "How can you move forward when you keep regretting the past.",
                "If you don’t like your destiny, don’t accept it. Instead, have the courage to change it.",
                "The circumstances of one’s birth are irrelevant, but it is what you do with the gift of life.",
                "It takes an Idiot do something cool, that’s why it is cool.",
                "I don’t have any goals for the future. So long as I can get out of my home and far away, I don’t care.",
                "I don’t just want to die: I want to die happy.",
                "Having happy and beautiful memories won’t always bring you salvation.",
                "I do not need a Heaven. However, if I must go to Heaven then please, God, do not divide Heaven in two.",
                "We are neither beasts nor slaves! We are human.",
                "I had more than enough time to notice, so why? Why didn’t I use my deadly, destructive strength.",
                "You did the best you could. The both of you did the best you could.",
                "I have always wanted to apologize to you. I endured and lived on just for that.",
                "They were weak. That’s why they died. We were weak too. That’s why we couldn’t save them.",
                "I don’t want to become a witch.",
                "If I had faith then I would blame all the bad things on God. Then I would be sure it wasn’t my fault.",
                "Don’t go. Don’t go. Please don’t go. Please don’t leave me behind."]

    # The ! at the end indicates to the decoder this is a 1
    message1 = ["I know as much of games as hugs and puppies, and care for them even less!",
                "Don’t talk, it makes you sound stupid!",
                "You try to sound like you think through things, when in fact you’re not thinking at all!",
                "I can’t accept this. I value our friendship and all we’ve been through but… I don’t like you that way!",
                "It’s sad when your friends leave you alone but it’s fun when you leave them and watch anime alone!",
                "Since you left, what is left for me is only loneliness!",
                "You are not interested in others, but you hate loneliness!",
                "The worst part about being strong is that no one asks if you are okay!",
                "I hate loneliness but it loves me!",
                "I don’t run from you, I walk away slowly, and it kills me, ’cause you don’t care enough to stop me!",
                "I run in the rain, so that nobody can see my tears!",
                "I’m tired if trying, sick of crying, I know I’ve been smiling, but inside I’m dying!",
                "I think I’d do better on my own, no friends, no fights. Just me, alone!",
                "People, who can’t throw something important away, can never hope to change anything!",
                "If you have time to think of a beautiful end, then live beautifully until the end!",
                "I won’t live my life by another person’s script!",
                "Forgetting is like a wound. The wound may heal but it has already left a scar!",
                "Even if life is painful and tough, people should appreciate what it means to be alive at all!",
                "You’re thinking in Japanese! If you must think, do it in German!",
                "Stop making me repeat myself! It’s bad for my health!",
                "Don’t tell me he wants to conquer the world? Can’t he come up with something more original!",
                "And what’s the real lesson? Don’t leave things in the fridge!",
                "I can’t talk about it! It’s so horrible! They were– they were– the milk! Oh God, the milk!",
                "Survivability takes priority!",
                "Man fears the darkness, and so he scrapes away at the edges of it with fire!",
                "The boy’s screams excited me far more than yours!",
                "A drop from the moon dropped and disappeared into a room into my heart!",
                "I just love the smell of C4 in the morning!",
                "I don’t care about no artificial humans!",
                "Ranma, please. I like you just the way you are. Please don’t fight anymore. I’m begging you!"]

    # Twitter will not allow you to post the same tweet twice, so we use these hashtags to add randomness to it and
    # reduce the likelihood of a collision.
    hashtags = ["#olive",
                "#nadir",
                "#legal",
                "#maqui",
                "#unbid",
                "#bohea",
                "#squad",
                "#curst",
                "#tapas",
                "#sadbo",
                "#hunks",
                "#bigbo",
                "#light",
                "#bleak",
                "#alive",
                "#brave",
                "#worse",
                "#false",
                "#worst",
                "#angry",
                "#loved",
                "#naive",
                "#awful",
                "#loyal",
                "#tense",
                "#aware",
                "#toxic",
                "#burnt",
                "#sworn",
                "#leafy"]

    # Open Message File
    f = open('message.txt', 'r')

    # Read in the contents on the sensitive message
    input_contents = f.read()
    # input_contents = ''
    print(input_contents)

    # Convert message to binary
    output_contents = text_to_bits(input_contents)
    print(output_contents)

    # Convert binary output to an array
    binary_msg = list(output_contents)
    print(binary_msg)

    # Determines a random quote based on the 0 or 1 of the text file.
    #    start message: "*"
    #    end message: "?"
    #    0: "."
    #    1: "1"
    quote = ''
    api.update_status(startmsg + random.choice(hashtags))  # This sends the start tweet to twitter
    time.sleep(60) # Wait 60 seconds before sending another tweet

    for i in range(len(binary_msg)):
        if binary_msg[i] == '1':
            quote = random.choice(message1) + random.choice(hashtags)
            print(quote)
        elif binary_msg[i] == '0':
            quote = random.choice(message0) + random.choice(hashtags)
            print(quote)

        # This catches if we have a collision and try to post the same message twice. If we do, we will resend with a
        # different message and different hashtag that's not in the other list.
        try:
            api.update_status(quote)
        except:
            if binary_msg[i] == '1':
                quote = random.choice(message1) + '#death'
            elif binary_msg[i] == '0':
                quote = random.choice(message0) + '#death'
            api.update_status(quote)
        # Twitter thinks we're a bot if we send messages every 60 seconds, so this changes it to send it randomly
        # between 1 and 5 minutes
        n = random.randint(60, 300)
        time.sleep(n)
    api.update_status(endmsg + random.choice(hashtags))  # This sends the end message tweet to twitter
