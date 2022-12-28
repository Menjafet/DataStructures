import Stacks.stack

class main():

  def __init__(self, dt):
    self.dt= dt
    match dt:
        case 0:
          self.runStack()

  def runStack(self):
    numbers = [1,2,3,4,5,6,7]
    for x in numbers:
      print(Stacks.stack.MyStack().push(x))


# 0=stack
staquita= main(0)
