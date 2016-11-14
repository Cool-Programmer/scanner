import os


# The url passed is the clean domain name
# In terminal " host google.com "
def get_ip_address(url):
    print('Getting the ip address...')
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    return results
