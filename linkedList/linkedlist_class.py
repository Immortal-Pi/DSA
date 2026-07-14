class Node:
    def __init__(self,value):
        self.data=value 
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_head(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return self.head
        else:
            newNode.next=self.head 
            self.head=newNode
            return self.head 
        
    def insert_at_index(self,data,index):
        newNode=Node(data)
        if self.head==None:
            return None 
        if index==0:
            self.head=self.insert_at_head(data)
        temp=self.head 
        count=0
        while temp!=None and count<=index:
            if count==index:
                newNode=Node(data)
                newNode.next=temp.next 
                temp.next=newNode
            temp=temp.next
            count+=1
        return self.head
    
    def insert_at_index_recursive(self,current,data,index):
        if current==None:
            raise IndexError("Index out of range")
        if index==0:
            newNode=Node(data)
            newNode.next=current
            return newNode
        current.next=self.insert_at_index_recursive(current.next,data,index-1)
        return current
    
    def print_LL(self):
        temp=self.head 
        while temp!=None:
            print(temp.data,end='->')
            temp=temp.next


    def get_length(self):
        temp=self.head
        count=0
        while temp!=None:
            count+=1 
            temp=temp.next
        return count 

    # remove 
    # search
    # update 
    def updateNode(self,value,index):
        pass 
        
    def create_LL(self,arr:list):
        tail=None 
        
        for i in range(len(arr)):
            newNode=Node(arr[i])
            if self.head==None:
                self.head=newNode
                tail=newNode
            else:
                tail.next=newNode
                tail=newNode
        return self.head
            



if __name__=='__main__':
    link=LinkedList()
    node=link.create_LL([3,4,2,1,5,6,7,10,22]) 
    node=link.insert_at_index_recursive(node,44,1)
    link.print_LL()


