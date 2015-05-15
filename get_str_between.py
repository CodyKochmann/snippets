def get_str_between(s, before, after):
    # gets a substring between two strings in a string in python
    # by: Cody Kochmann
    unique="~~~~the~obvious~way~to~do~it~~~~"
    return(s.replace(before, unique).replace(after, unique).split(unique)[1])