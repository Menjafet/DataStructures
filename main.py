import Stacks.stack

class main():

  def __init__(self, dt):
    self.dt= dt
    match dt:
        case 0:
          self.runStack()

  def runStack(self):
    numbers = [1,2,3,4,5,6,7]
    estaquitababy=Stacks.stack.MyStack()
    for x in numbers:
      print(estaquitababy.push(x))
    for x in numbers:
      print(estaquitababy.pop())


# 0=stack
staquita= main(0)
