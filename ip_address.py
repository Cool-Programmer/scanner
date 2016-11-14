import os


# The url passed is the clean domain name
# In terminal " host google.com "
def get_ip_address(url):
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    return results

print(get_ip_address('facebook.com'))