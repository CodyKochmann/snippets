def ensure_dir(dir_name,parent_dir,verbose=False): 
    # ensures there is a directory of that name in that path
    # by: Cody Kochmann
    # ex: trash_dir=ensure_dir("trash", script_dir)
    def v_log(s):
        if(verbose):
            print(s)
    from os import listdir, path, mkdir
    dir_name=dir_name.replace("/", "")
    if parent_dir[-1] != "/":
        parent_dir+="/"
    new_dir = parent_dir+dir_name
    v_log(new_dir)
    if path.isdir(new_dir) == False:
        mkdir(new_dir)
    else:
        v_log("%s already exists" % (dir_name))
    return(new_dir+"/")