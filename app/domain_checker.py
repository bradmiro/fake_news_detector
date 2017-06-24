import re

def checker(url):
    """
    :param url: Verify this URL from a loaded list of urls
    :return: True if domain is already flagged, False otherwise.
    """

    url_list = "file_of_url_list"

    url_re = re.compile('(https:\ / \ /|http:\ / \ /|^)(www.|^)([ ^\ /] * )', re.IGNORECASE)

    url_match = url_re.match(url)
\
    with open(url_list) as flagged_urls:
        for line in flagged_urls.readline():
            if url_match.group(1) == line:
                return True

    return False




