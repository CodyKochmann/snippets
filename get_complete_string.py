def get_complete_string(s,start,end):
    # returns a substring starting with start and ending with end
    # By: Cody Kochmann
    unique="~~~~the~obvious~way~to~do~it~~~~"
    return(start+s.replace(start, unique).replace(end, unique).split(unique)[1]+end)