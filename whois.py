import os


# whois facebook.com
# information about the website, author etc
def get_whois(url):
    print('Scanning whois...')
    command = 'whois ' + url
    process = os.popen(command)
    result = str(process.read())
    return result