import difflib


def main():
    test = is_tachycardic()
    test_r = similarity()
    output(test_r)


def user_type():
    in_user = input('Please type only string: ')
    return in_user

    
def is_tachycardic(instring):
    print(instring)


def similarity(instring):
    return difflib.SequenceMatcher(None, str(instring).lower(), 
                                   "tachycardic").ratio


def is_tachycardic(instring):
    r = difflib.SequenceMatcher(None, str(instring).lower(),
                              "tachycardic").ratio()
    if r > 0.7:
        return True
    else:
        return False

   
def output(instring):
    if instring == 1:
        print('exact match \ \nsimilarity:{}%'.format(round(instring, 1)))
    if 0.7 < instring < 1:
        print('exact match \ \nsimilarity:{}%'.format(round(instring, 1)))
    if instring < 0.7:
        print('exact match \ \nsimilarity:{}%'.format(round(instring, 1)))


if __name__ == "__main__":
    main()
