def check_if_link(s,req_http=True):
    # Checks if the input is a link.
    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;=%"
    if req_http and "http" not in s:
        return(False)
    if "://" in s:
        for i in s:
            if i not in allowed_chars:
                return(False)
        return(True)
    return(False)