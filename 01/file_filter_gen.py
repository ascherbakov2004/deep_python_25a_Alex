import io


def filter_lines_by_words(file, words_to_find: list[str]) -> str:
    words_to_find = [word.lower() for word in words_to_find]
    for line in file:
        if set(line.lower().split()).intersection(words_to_find):
            yield line


def file_filter_gen(
    file_or_path,
    words_to_find: list[str],
) -> str:
    if not (
        isinstance(words_to_find, list)
        and all(isinstance(word, str) for word in words_to_find)
    ):
        raise ValueError("words_to_find is not a list of strings")

    if isinstance(file_or_path, str):
        with open(file_or_path, "r", encoding="utf-8") as file:
            yield from filter_lines_by_words(file, words_to_find)
    elif isinstance(file_or_path, io.IOBase):
        yield from filter_lines_by_words(file_or_path, words_to_find)
    else:
        raise ValueError("wrong file argument")