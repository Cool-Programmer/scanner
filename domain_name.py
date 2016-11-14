from tld import get_tld


# Get tld (e.g. google.com, from https://www.google.com)
def get_domain_name(url):
    print('Getting the domain name...')
    domain_name = get_tld(url)
    return domain_name