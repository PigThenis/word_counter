def main():
    filename = "peloponnesian_war.txt"

    raw_text = open_file(filename)

    word_list = clean_text(raw_text)

    word_count = count_words(word_list)

    display_count(word_count)


def open_file(filename):
    with open(filename) as raw_file:
        raw = raw_file.read().strip()
        return raw

def clean_text(raw):
    clean_raw = []
    raw_lower = raw.lower()
    clean_string = ""
    for char in raw_lower:
        if char.isalpha() or char.isspace():
            clean_string += char
    word_list = clean_string.split()
    filtered_list = [word for word in word_list if "www" not in word]

    return word_list

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def display_count(word_count):
    print("--- Word Frequency Analysis ---")
    sorted_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for i, (word, count) in enumerate(sorted_count[:10], start=1):
        print(f"{i}. {word}: {count}")

main()


