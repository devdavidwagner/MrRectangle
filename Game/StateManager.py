class StateManager():
    def __init__(self):
        super().__init__()

        self.states = ["Menu","Game"]

        self.currentState = self.states[0]


    def updateState(self,state):
        self.currentState = state