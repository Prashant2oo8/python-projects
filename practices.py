def check_lines():
    lineNo = 1
    with open("something.txt", "r") as f:
        data = f.readline()
        while data:
            if "language" in data.lower():
                print(f"word found in line number {lineNo}")
                break
            data = f.readline()
            lineNo += 1


check_lines()