import re

url_pattern = r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'
digit_pattern = '\d+'
hashtag_pattern = r'(?:^|\s)[＃#]{1}(\w+)'
user_pattern = r'@(\w+)'

def placeholder(text):
    # Replace URLs
    url_pattern = r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'
    url_repl = ' URL '
    text = re.sub(url_pattern, url_repl, text)
    # Replace digits
    digit_pattern = '\d+'
    digit_repl = ' DIGIT '
    text = re.sub(digit_pattern, digit_repl, text)
    # Replace hashtags
    hashtag_pattern = r'(?:^|\s)[＃#]{1}(\w+)'
    hashtag_repl = ' HASHTAG '
    text = re.sub(hashtag_pattern, hashtag_repl, text)
    # Replace users
    user_pattern = r'@(\w+)'
    user_repl = ' USER '
    text = re.sub(user_pattern, user_repl, text)
    return text