def gen(filepath, words, stops):
    with open(filepath, "r", encoding="UTF-8") as f:
        lines = f.readlines()

    for line in lines:

        line_low = line.lower()

        isFind = False

        for word in words:
            if word.lower() in line_low.split():
                isFind = True

        if isFind:
            for stop in stops:
                if stop.lower() in line_low.split():
                    isFind = False

        if isFind:
            yield line
