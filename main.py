def update_server_config(file_path,key,value): # key value arugumets used to change any config value needed
    with open(file_path,'r') as f:
        lines = f.readlines() # will collect all the data in a list
        print(lines)

    with open(file_path,'w') as f:
        for line in lines:
            if line.strip().startswith(key + "="): # this helps in exact stringmatch
                f.write(key + "=" + value + "\n") # \n for the next line
            else:
                f.write(line) # re-writing everything in the same file


update_server_config('Server.conf',"MAX_CONNECTIONS","1000")

