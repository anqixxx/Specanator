class app():
    def __init__(self, name):
            self.ssd = 10
            self.ram = 10
            self.gpu = 10
            self.ram = 10
            self.cpu = 10
            self.name = name
    def getssd(self):
        return self.ssd
    def getram(self):
        return self.ram
    def getgpu(self):
        return self.gpu
    def getcpu(self):
        return self.cpu

#minecraft = app("minecraft")
#print( minecraft.getgpu() )
