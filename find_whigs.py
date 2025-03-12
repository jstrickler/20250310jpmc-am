FILE_PATH = "DATA/presidents.txt"

with open(FILE_PATH) as presidents_in:
    for raw_line in presidents_in:
        if "Whig" in raw_line:
            print(raw_line.rstrip())