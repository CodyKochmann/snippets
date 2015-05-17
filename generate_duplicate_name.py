def generate_duplicate_name(f_name,output_path):
    ## snipet that allows duplicate file generation if need be
    # by: Cody Kochmann
    from os import listdir
    if f_name in listdir(output_path):
      if allow_duplicates == False:
        v_print(f_name+" already downloaded")
        return(False)
      else:
        placeholder_name=2
        while ((str(placeholder_name)+"."+f_name) in listdir(output_path)):
            placeholder_name+=1
        f_name=str(placeholder_name)+"."+f_name