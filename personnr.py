__author__ = 'Lucas'

from math import ceil


def validpnr(pnr):
    personNumber = str(pnr)
    if len(personNumber) == 10:
        checkSum = 0
        for pos, number in enumerate(personNumber[0:9]):
            if pos % 2 == 0:
                number = str(int(number) * 2)
            for figure in number:
                checkSum += int(figure)

        if int(ceil(checkSum / float(10) ** (len(str(checkSum)) - 1)) * 10 ** (
            len(str(checkSum)) - 1) - checkSum) == int(personNumber[9]):
            return True
        else:
            return False


def validpnralt2(pnr):
    return len(str(pnr)) == 10 and int(str(pnr)[-1]) == 10 - int(str(
        sum( map(lambda x: sum(map(int, str(x)  ) ), map(lambda x: int(x) * 2, str(pnr)[:9:2]))) +
        sum( map(lambda x: int(x), str(pnr)[1:9:2])))[-1])


def getGender(pnr):
    if len(str(pnr)) != 10:
        return False

    if int(str(pnr)[-2]) % 2 == 0:
        return "female"
    else:
        return "male"


print validpnralt2(9812302512)
