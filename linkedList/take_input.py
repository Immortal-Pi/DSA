class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

def print_LL(head:Node):
    temp=head
    while temp!=None:
        print(temp.data,end='->')
        temp=temp.next


def take_input_with_no_tail():
    value=int(input("enter the value of Node:- "))
    head=None 

    while value!=-1:
        new_Node=Node(value)
        if head==None:
            head=new_Node
        else:
            temp=head
            while temp.next!=None:
                # print(temp.data)
                temp=temp.next
            temp.next=new_Node
            
        value=int(input("enter the value of Node:- "))
        
        # head.next=new_Node
    return head 

def take_input_with_tail():
    value=int(input("enter the value of Node:- "))
    head=None 
    tail=None

    while value!=-1:
        new_Node=Node(value)
        if head==None:
            head=new_Node
            tail=new_Node
        else:
            tail.next=new_Node
            tail=new_Node

            
        value=int(input("enter the value of Node:- "))
        
    return head 

def get_length(head:Node):
    count=0
    temp=head
    while temp!=None:
        count+=1
        temp=temp.next
    return count 

def get_length_recursive(head:Node):
    if head==None:
        return 0 
    return 1+ get_length_recursive(head.next)

# newhe=take_input_with_no_tail()
newhe=take_input_with_tail()
print_LL(newhe)
print(f'\nlength:{get_length_recursive(newhe)}')
    

        