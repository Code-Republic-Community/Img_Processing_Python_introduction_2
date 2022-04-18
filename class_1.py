#class computer:
#
#    def __init__(self):
#        self.cpu = None
#        self.ram = None
#        self.disk = None
#
#    def log_me(self):
#        #print(f'cpu-{self.cpu}\nram-{self.ram}\ndisk-{self.disk}')
#        print(f'{self.cpu}\n{self.ram}\n{self.disk}')
#
#
#intel_comp = computer()
#intel_comp.cpu = 'i9'
#intel_comp.ram = 7.8
#computer.log_me(intel_comp)
#
#amd_comp = computer()
#amd_comp.cpu = 'ryzen 5'
#amd_comp.ram = 70
#amd_comp.log_me()

class Point:


  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    print(self.x, self.y, self.z);

m = Point(1, 5, 7)
