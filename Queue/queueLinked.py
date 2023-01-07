import NodeTypes.Node as Ntype

class MyLinkedQueue:

    count: int
    front: Ntype.Node
    back: Ntype.Node

    def __init__(self):
       self.count=0
    

    def Queue(self,input:int=None):
        if (input == None):
            return None
        newnode=Ntype.Node(val=input)

        if (self.count==0):
            self.front=newnode
        else:
            self.back.NextNode=newnode
            newnode.prevNode=self.back
        
        self.back=newnode
        self.count+=1
        return input

    def deQueue(self):
        if (self.count==0 or self.front==None):
            return "stop"

        val = self.front.val

        if (self.count==1):
            self.front=None
            self.back=None
        else:
            self.front=self.front.NextNode
            
        self.count-=1
        return val

    def peek(self):
        return self.front.val   
    
    
