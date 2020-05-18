class People:

    nameList = []
    def __init__ (self, FIO, numOfExperiment, result):
        People.nameList.append(self)
        self.FIO = FIO
        self.numOfExperiment = numOfExperiment
        self.result = result

    def getAll(self):
        return self.FIO, self.numOfExperiment, self.result

    def getFIO(self):
        return self.FIO

    def getNumOfExperiment(self):
        return self.numOfExperiment

    def getResult(self):
        return self.result