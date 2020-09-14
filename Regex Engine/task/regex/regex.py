def checker(word):
    if word[0] == word[-1] or word[0] == "." or word[0] == "|":
        return True
    return False


def checker_string(test):
    input_list = test.split("|")
    regex = input_list[0]
    # print("regex: " + regex)
    word = input_list[1]
    # print("word: " + word)

    if regex.startswith("^"):
        regex = regex[1:]
        starts_with = True
        # print(regex)
    else:
        starts_with = False

    if regex.endswith("$"):
        regex = regex[:-1]
        ends_with = True
        # print(regex)
    else:
        ends_with = False

    if "?" in word:
        # preceding letter should be optional
        pass

    if "*" in word:
        # glob
        pass

    if "+" in word:
        # preceding character occurs once or more
        pass

    if starts_with and ends_with:
        if regex == word:
            # return True, "Starts ends and matches"
            return True
        else:
            return False

    if starts_with:
        if word.startswith(regex):
            return True
        else:
            return False

    if ends_with:
        if word.endswith(regex) or regex == ".":
            # This could use the first checker
            return True
        else:
            return False

    def sub_checker(reg, wor):
        if reg[0] in wor or reg[0] == ".":
            try:
                sub_checker(reg[1:], wor[1:])
            except IndexError:
                return True
                # return True, "Index error"
    if not word and regex:
        # If word is empty and there is a regex return false
        return False
        # return False, "word empty"
    elif word and not regex:
        # If regex is empty and there is a word return true
        return True
        # return True, "regex empty"

    if len(regex) == len(word):
        if test == "|":
            return True
            # return True, "both empty"
        try:
            count = 0
            for counter, value in enumerate(regex):
                if value == word[counter] or value == ".":
                    count += 1
            if count != len(word):
                return False
                # return False, "not all matches"
            else:
                # return True, "all matches"
                return True

        except IndexError:
            return True, "index error"
    elif len(regex) > len(word):
        return False
    else:
        if sub_checker(regex, word):
            # return True, "other"
            return True
    # return True, "last"
    return True


print(checker_string(input()))



# print(checker_string("^apple$|apple"))
# print(checker_string("^apple$|apple pie"))
# print(checker_string("le$|apple"))

# print(checker_string("ple|apple"))
# print(checker_string("ap|apple"))
# print(checker_string(".|apple"))
# print(checker_string("|apple"))
# print(checker_string("apple|apple"))
# print(checker_string("apwle|apple"))
# print(checker_string("peach|apple"))
# print(checker_string("apeach|apple"))
# print(checker_string(".pple|apple"))
