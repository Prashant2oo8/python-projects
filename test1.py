def check_line():
    data = True
    lineNo = 1
    with open("newfile.txt", "r") as f:
        while data:
            data = f.readline()
            if not data:
                break
            if ("learning" in data):
                return lineNo
            lineNo += 1
    return -1

print(check_line())