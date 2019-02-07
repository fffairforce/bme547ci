def is_tachycardic(instring):
    print(instring)
    import difflib


def is_tachycardic(instring):
    r=difflib.SequenceMatcher(None, str(instring).lower(), "tachycardic").ratio()
    if r > 0.7:
        return True
    else:
        return False
       
def output(instring):
    if instring == 1:
        print('exact match \ \nsimilarity:{}%'.format(round(instring,1)))
    if 0.7 < instring < 1:
        print('exact match \ \nsimilarity:{}%'.format(round(instring,1)))
    if instring < 0.7:
        print('exact match \ \nsimilarity:{}%'.format(round(instring,1)))
          