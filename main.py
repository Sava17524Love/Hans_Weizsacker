from direct.showbase.ShowBase import ShowBase

#base = ShowBase()
#base.run()

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel('models/Fighter.egg')
        self.model.reparentTo(render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)
        base.camLens.setFov(90)

game = Game()
game.run()