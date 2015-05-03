def extract_links(url):
    # extracts all links from a URL and returns them as a list
    # by: Cody Kochmann
    def grep(link):
        from urllib2 import urlopen
        response = urlopen(link)
        return(response.read())

    def check_if_link(s,req_http=True):
        # Checks at the input is a legitimate link.
        allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;=%"
        if req_http and "http" not in s:
            return(False)
        if "://" in s:
            for i in s:
                if i not in allowed_chars:
                    return(False)
            return(True)
        return(False)
    
    collected_links = []
    link_being_built = ""
    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&()*+,;=%"
    collected_html= grep(url)
    for i in collected_html:
        if i in allowed_chars:
            link_being_built+=i
        else:
            if link_being_built not in collected_links:
                if check_if_link(link_being_built):
                    collected_links.append(link_being_built)
            link_being_built=""
    return(collected_links)