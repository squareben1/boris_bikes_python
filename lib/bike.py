class Bike:

    def __init__(self,model):
        self.model = model
        self.working = True

    def report_broken(self):
        self.working = False
        return self.working
