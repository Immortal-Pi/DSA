from collections import deque
class BinaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None 
        self.right=None 


def build_tree(treeStructure):
    if treeStructure==None:
        return None 
    key,value=treeStructure
    # print(key,value[1])

    root=BinaryTree(key)
    if len(value)>=1:
        root.left=build_tree(value[0])

    if len(value)>=2:
        root.right=build_tree(value[1])
    return root


def print_tree(root):
    if root==None:
        return root 

    print(root.val,end=':')
    if root.left!=None:
        print(f'L->{root.left.val}',end=',')
    else:
        print(f'None',end=',')
    if root.right!=None:
        print(f'R->{root.right.val}',end=',')
    else:
        print(f'None',end=',')
    print('\n')
    print_tree(root.left)
    print_tree(root.right)

def print_tree_BT(root):
    if root==None:
        return root
    queue=deque([root])
    while queue:
        top=queue.popleft()
        print(f'{top.val}',end=':')
        if top.left:
            print(f'L->{top.left.val}',end=',')
            queue.append(top.left)
        else:
            print(f'L-> None',end=',')
        if top.right:
            print(f'R->{top.right.val}',end=',')
            queue.append(top.right)
        else:
            print(f'R-> None',end=',')
        print('\n')
    

tree1_struture=(1,[
    (2,[
        (4,[]),
        (5,[])
        ]),
    (3,[
        (6,[])
    ])
])

if __name__=='__main__':
    tree1=build_tree(tree1_struture)
    print_tree(tree1)