class Cell:

    def __init__(self, row=None, col=None, value=0, is_locked=False) -> None:
        self.row = row
        self.col = col
        self.value = value
        self.is_locked = is_locked

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getValue(self):
        return self.value

    def isLocked(self):
        return self.is_locked

    def setValue(self, value):
        self.value = value

    def setLocked(self, locked):
        self.is_locked = locked
