import difflib


def main():
    t = user_type()
    test = is_tachycardic(t)
    test_r = similarity(t)
    output(test_r)


def user_type():
    in_user = input('Please type only string: ')
    return in_user


def similarity(n):
    return difflib.SequenceMatcher(None, str(n).lower(), "tachycardic").ratio()


def is_tachycardic(n):
    r = difflib.SequenceMatcher(None, str(n).lower(), "tachycardic").ratio()
    if r > 0.7:
        return True
    else:
        return False


def output(n):
    if n == 1:
        print('exact match  \nsimilarity:{}'.format(round(n, 1)))
    if 0.7 < n < 1:
        print('acceptble error  \nsimilarity:{}'.format(round(n, 1)))
    if n < 0.7:
        print('wrong input  \nsimilarity:{}'.format(round(n, 1)))


if __name__ == "__main__":
    main()
