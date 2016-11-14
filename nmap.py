import os


# get nmap via ip(got from ip_address.py) and option
# format nmap -F(?) ip
def get_nmap(options, ip):
    command = 'nmap ' + options + ' ' + ip
    process = os.popen(command)
    result = str(process.read())
    return result