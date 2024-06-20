def update_server_config(file_path,key,value):
    with open(file_path,'r') as f:
        lines = f.readlines() # will collect all the data in a list
        print(lines)

    with open(file_path,'w') as f:
        for line in lines:
            if line.strip().startswith(key + "="):
                f.write(key + "=" + value + "\n")
            else:
                f.write(line)


update_server_config('Server.conf',"MAX_CONNECTIONS","1000")

