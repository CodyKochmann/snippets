def current_dir(): 
    # returns a unix current directory
    # By: Cody Kochmann
    from os import path
    return(path.dirname(path.realpath(__file__)))