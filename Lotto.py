import os, random

class Lotto:
    def __init__(self, count):
        self._count = count
        self._LottoStats = self.__initLDict()

        self.LottoList = list()
        for i in range(count):
            self.GenerateLotto()

    #
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

    #
    def __LDictSum(self, Dict, Start, End):
        result = int()
        for i in range(Start, End + 1):
            result += Dict[str(i)]
        
        return result

    #
    def GetLottoListLength(self):
        return len(self.LottoList)
    
    #
    def GenerateLotto(self):
        Lotto = list()

        LastNum  = int(0)
        Prob = int(0)

        for i in range(6):
            Limit = int()
    
            for j in range(LastNum + 1, 46):
                Limit += self._LottoStats[i][str(j)]
    
            Prob = random.randint(1, Limit)
    
            for j in range(LastNum + 1, 46):
                if Prob <= self.__LDictSum(self._LottoStats[i], LastNum + 1, j):
                    Lotto.append(j)
                    LastNum = j
                    break

        self.LottoList.append(Lotto)
        return Lotto
