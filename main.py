def count_character(text):
    lowered_text = text.lower()
    words = lowered_text.split(" ")
    result = {" ": len(words) - 1}
    for word in words:
        for char in word:
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1
    return result


def sort_on(dict):
    return dict["num"]


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        result = count_character(file_contents)
        report = []
        for key in result:
            if key.isalpha():
                report.append({"char": key, "num": result[key]})
        report.sort(key=sort_on, reverse=True)
        print(report)


main()
