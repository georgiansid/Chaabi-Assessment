mainstream = ["One Punch Man","Attack On Titan","One Piece",
              "Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death Note",
               "Stein's Gate","The Devil is a Part Timer!",
               "One Piece","Attack On Titan"]
def commonNotCommon(mainstream, mustWatch):
    common = set()
    notCommon = set()
    for i in mainstream:
        if i in mustWatch:
            common.add(i)
        else:
            notCommon.add(i)
    for i in mustWatch:
        notCommon.add(i)
    for i in common:
        if i in notCommon:
            notCommon.discard(i)
        else:
            pass
    return list(common), list(notCommon)
print(commonNotCommon(mainstream,must_watch))