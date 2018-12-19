import os

class Lotto:
    def __init__(self, count):
        self.count = count
        self._LottoStats = self.__initLDict()

    def __initLDict(self):
        List = list()
        
        for i in range(6):
            List.append(dict())

            for j in range(1, 46):
                List[i][str(j)] = 0

        if os.path.isfile("Text/Lotto.txt"):
            LottoText = open("Text/Lotto.txt", 'r')

            win_list = LottoText.readlines()

            for i in range(len(win_list)):
        
                CharCount = int(0)
                element = str()
        
                for j in range(len(win_list[i])):
                    if win_list[i][j] != '.' and win_list[i][j] != '\n':
                        element += win_list[i][j]
                    else:
                        List[CharCount][element] += 1
                        CharCount += 1
                        element = ''

                if CharCount == 5:
                    List[CharCount][element] += 1
        return List
