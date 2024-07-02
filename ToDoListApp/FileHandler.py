def write_to_file(data_to_save):
    f = open("saved_data.txt", "w")
    for line in data_to_save:
        f.write(line + "\n")
    f.close()

def read_from_file():
    f = open("saved_data.txt", "r")
    return [line.strip() for line in f]