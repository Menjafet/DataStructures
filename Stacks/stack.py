import NodeTypes.Node as Ntype

class MyStack:

    count: int
    head: Ntype.Node

    def __init__(self):
       self.count=0
    

    def push(self,input:int=None):
        if (input == None):
            return None
        if (self.count==0 ):
            head=Ntype.Node(val=input)
        else:
            pass
        
        self.count+=1
        return input

    def pop(self):
        pass        
