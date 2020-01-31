class Publisher:
    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print(f'Failed to add: {observer}')

    def removeObserver(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print(f'Failed to remove: {observer}')

    def notify(self, object):
        [o.notify(object) for o in self.observers]