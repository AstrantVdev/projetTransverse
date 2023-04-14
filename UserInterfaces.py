class UserInterface:
    def __init__(self, id):
        self.id = id
        self.buttons = []

    def addButton(self, button):
        self.buttons.append(button)
        return self

    def setButtons(self, buttons):
        self.buttons = buttons
        return self

    def getButtons(self):
        return self.buttons

    def setId(self):
        self.id = id
        return self

    def getId(self):
        return self.id

    def blit(self, screen):
        for b in self.buttons:
            b = b()
            b.blit(screen)
