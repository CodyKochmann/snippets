def findall(search_field,search):
    # searches a string for a substring and returns an array of indexes
    # by: Cody Kochmann
    tmp_field = search_field.split(search)
    if len(tmp_field) == 1:
        return(False)
    output = []
    tmp_string = ""
    for i in range(len(tmp_field)):
        tmp_string += tmp_field.pop(0)
        output.append(len(tmp_string)+(len(search)*i))
    output.pop(-1)
    return(output)