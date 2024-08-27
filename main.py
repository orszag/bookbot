def main():
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)
    character_count = {}
    #print(file_contents)
    print("REPORT START")
    print(f"Number of words in document: {count_words(file_contents)}")
    character_count = char_count(file_contents)
    for key in character_count:
        print(f"The'{key}' character was found {character_count[key]} times")
    print("REPORT END")

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    return len(words)

def char_count(string):
    chars = {}
    ordered_chars = {}
    sorted_chars = {}
    lowered_string = string.lower()
    for char in lowered_string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    dict_size = len(chars)
    while len(ordered_chars) < dict_size:
        max_count = 0
        key_name = ""
        for key in chars:
            if chars[key] > max_count:
                max_count = chars[key]
                key_name = key
        ordered_chars[key_name] = chars[key_name]
        del chars[key_name]
    for key in ordered_chars:
        if key.isalpha():
            sorted_chars[key] = ordered_chars[key]
    return sorted_chars
    

main()