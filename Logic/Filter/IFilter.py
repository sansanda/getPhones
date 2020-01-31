from abc import ABC, abstractmethod

class IFilter():
    @abstractmethod
    def satisfies(self,laserJob):
        pass
    def getName(self):
        pass

