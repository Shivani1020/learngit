class Flight:
    def __init__(self,engine):
        self.engine = engine

    def startengine(self):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print("AirBus engine starting")

class BoingEngine:
    def start(self):
        print("Boing engine starting")

ae = AirbusEngine()
f = Flight(ae)
f.startengine()

be = BoingEngine()
f2 = Flight(be)
f2.startengine()