from linked_list import LinkedList
from pygame.draw import circle
import math

class Frame():
    def __init__(self,screen):
        self.fList = LinkedList()
        self.screen = screen

        for i in range(55):
            self.fList.addNode_L([300+i,300])
        self.x = self.fList.getLastNode().data[0]
        self.y = self.fList.getLastNode().data[1]

        self.counter = 1
    
    def frameUpdate(self):
        lastNode = self.fList.getLastNode()
        self._frameUpdate([self.x,self.y],lastNode)

    def _frameUpdate(self,v,node):
        if node != "NULL":
            a = 0
            self._frameUpdate(node.data,node.prev)
            node.data[0] =v[0] -math.sin(self.counter*3)*self.counter*self.counter*self.counter/4555
            node.data[1] =v[1]-math.cos(self.counter*3)*self.counter*self.counter*self.counter/4555
            self.counter += 0.3
            if self.counter % 2 == 0:
                a = 1
            circle(self.screen,[255,0,0],(node.data[0], node.data[1]),333-self.counter*self.counter,1)
            if node.next != "NULL" and node.prev != "NULL":
                pass
        
    def xy_calc(self,x,y):
        self.x = x
        self.y = y

    
    def VelUpdate(self,vx,vy):
        self.counter = 1
        self.xy_calc(vx,vy)
        self.frameUpdate()
