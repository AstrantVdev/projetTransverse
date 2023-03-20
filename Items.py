class Inventory:

    def __init__(self):
        self.maxSlot = 0
        self.slots = [] #[item, number of items]

    def setMaxSlot(self, maxSlot):
        self.maxSlot = maxSlot
        return self

    def getMaxSlot(self):
        return self.maxSlot

    def addItem(self, item, n):
        len = len(self.slots)
        if len < self.maxSlot:
            self.slots[len] = [item, n]
            return True

        return False

    def removeItemsBySlot(self, slot, n):
        self.slots[slot][1] -= n

        if self.slots[slot][1] <= 0:
            self.removeSlot(slot)

    def removeItemById(self, id, n):
        o = 0
        for i in self.slots:
            if i[0].id == id:
                self.removeItemsBySlot(o, n)
                break
            o += 1

    def removeAllItemsInSlot(self, slot):
        i = slot
        while i < len(self.slots):
            self.slots[i] = self.slots[i + 1]
            i += 1

    def getSlots(self):
        return self.slots


class Item:

    def __init__(self, id):
        self.id = id
        self.maxStack = 1
        self.frame = 0

    def exe(self):
        print(self.name + "executed !")
