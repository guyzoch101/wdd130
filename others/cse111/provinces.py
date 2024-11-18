def main():
    provinces_list = read_file("provinces.txt")
    provinces_list.pop(0)
    provinces_list.pop()
    
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"

    print(provinces_list)
    
    count = provinces_list.count("Alberta")
    
    print(f"\nAlberta occurs {count} times in the modified list")
    pass

def read_file(filename):
    text_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    
    return text_list