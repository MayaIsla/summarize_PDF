import time

log_path = "C:/log.txt"
cap_path = "C:/cap.txt"
dup_path = "C:/remove_dup.txt"
fin_path = "C:/FINAL.txt"

delete_list = ["N/A"]

def cap_text():
    with open(log_path, 'r') as data:
        with open(cap_path, 'a') as out:
            for line in data:
                out.write(line.lower())

def remove_duplicates():
    lines_seen = set() # holds lines already seen
    outfile = open(dup_path, "w")
    for line in open(cap_path, "r"):
        if line not in lines_seen: # not a duplicate
            lines_seen.add(line)
    outfile.writelines(sorted(lines_seen))
    outfile.close()

def remove_NA():
    with open(cap_path) as fin, open(fin_path, "w+") as fout:
        for line in fin:
            for word in fin:
                for word in delete_list:
                    line = line.replace(word, " ")
                fout.write(line)
    

def remove_duplicates_alt():
    with open(cap_path) as result:
        uniqlines = set(result.readlines())
        with open(dup_path, 'w') as rmdup:
            rmdup.writelines(set(uniqlines))

def remove_dup():
    lines_seen = set()
    with open(cap_path, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i not in lines_seen:
                f.write(i)
                lines_seen.add(i)

    
 
 
def main():
    print("Capitalizing Text..")
    cap_text()
    time.sleep(5)
    print("Removing Duplicates..")
    remove_dup()
    print("Removing 'N/A'")
    remove_NA()
    print("Done.")

    

if __name__ == '__main__':
    main()
