def download_file(url, output_path="./", verbose=False, allow_duplicates=False, f_name=''):
    # downloads a given url to the output_path with duplicate checking options
    # by: Cody Kochmann
    from urllib2 import urlopen
    from os import listdir
    def v_print(s):
        if(verbose):
            print(s)
    if f_name == '':
      f_name = url.split('/')[-1]
    if f_name in listdir(output_path):
      if allow_duplicates == False:
        v_print(f_name+" already downloaded")
        return(False)
      else:
        placeholder_name=2
        while ((str(placeholder_name)+"."+f_name) in listdir(output_path)):
            placeholder_name+=1
        f_name=str(placeholder_name)+"."+f_name
    v_print("downloading: "+f_name)
    response = urlopen(url)
    data = response.read()
    with open(output_path+f_name, "w") as f:
        f.write(data)
    v_print("finished: "+f_name)