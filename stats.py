def get_num_words(content: str) -> int:
    list_of_words = content.split()

    return len(list_of_words)

def count_characters(content: str) -> dict[str, int]:
    collection = {}

    for words in content.split():
        for char in words.lower():
            if char in collection:
                collection[char] += 1
            else:
                collection[char] = 1

    return collection

def pretty_list(char_counts: dict[str, int]) -> list:
    new_list = []
    for char, count in char_counts.items():
        new_list.append({
            'char': char,
            'num': count
        })

    new_list.sort(reverse=True, key=lambda x: x['num'])

    return new_list