import Stacks.stack
import Queue.queue
#
import Queue.queueLinked

class main():

  def __init__(self, dt):
    self.dt= dt
    match dt:
        case 0:
          self.runStack()
        case 1:
          self.runQueue()
        case 2:
          self.runLinkedQueue()

  def runStack(self):
    numbers = [1,2,3,4,5,6,7]
    pila=Stacks.stack.MyStack()
    for x in numbers:
      print(pila.push(x))
    for x in numbers:
      print(pila.pop())

  def runQueue(self):
    numbers = [1,2,3,4,5,6,7]
    cola=Queue.queue.MyQueue()
    for x in numbers:
      print(cola.Queue(x))
    for x in numbers:
      print(cola.deQueue())
  
  def runLinkedQueue(self):
    numbers = [1,2,3,4,5]
    cola=Queue.queueLinked.MyLinkedQueue()
    for x in numbers:
      print(cola.Queue(x))
    
    for x in numbers:
      print(cola.deQueue())
    

# 0=stack
#Test= main(0)
Test= main(2)
