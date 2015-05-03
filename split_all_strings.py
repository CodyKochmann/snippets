def split_all_strings(input_array, splitter):
    # splits all strings in a list with the splitter and adds them back
    # by: Cody Kochmann
    if isinstance(input_array, basestring):
        # patch to accept input_array in string form
        input_array = [input_array]
    result = []
    for i in input_array:
        for x in i.split(split_char):
            result.append(x)
    return(result)