def script_path(include_name=False):
    # returns the full path of the script containing this snippet
    # by: Cody Kochmann
    from os import path
    full_path = path.realpath(__file__)
    if include_name:
        return(full_path)
    else:
        full_path = "/".join( full_path.split("/")[0:-1] ) + "/"
        return(full_path)