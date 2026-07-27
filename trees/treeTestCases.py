from collections import deque 
class TreeNode:
    def __init__(self,value):
        self.val=value
        self.child=[]

def build_tree(tree_data):

    value,children=tree_data
    root=TreeNode(value)
    for child1 in children:
        # print(child1)
        child_node=build_tree(child1)
        root.child.append(child_node)
    return root


def print_tree(root):
    queue=deque([root])
    while queue:
        print('\n')
        top=queue.popleft()
        print(top.val,end=':')
        
        for i in top.child:
            queue.append(i)
            print(i.val,end=',')



tree1_data=(1,[
    (2,[]),
    (3,[(5,[]),(6,[
                (7,[
                    (20,[])
                ]),
                (8,[]),
            ])]),
    (4,[(11,[]),(12,[])])
])

tree2_data=(1,[
        (2,[]),
        (3,[
            (5,[]),
            (6,[])
        ]),
        (4,[]),
        (7,[
            (9,[
                (23,[(2,[]),(3,[])])
            ]),
            (44,[
                (45,[(6,[]),(7,[])])
            ]),
        ])
    ])
    # tree1=build_trees(tree1_data)

    # 1. Empty tree
tree_empty = None


# 2. Single-node tree
tree_single = (
    1,
    []
)


# 3. Root with multiple leaf children
tree_flat = (
    1,
    [
        (2, []),
        (3, []),
        (4, []),
        (5, [])
    ]
)


# 4. Linear tree: every node has one child
tree_linear = (
    1,
    [
        (2, [
            (3, [
                (4, [
                    (5, [])
                ])
            ])
        ])
    ]
)


# 5. Balanced tree
tree_balanced = (
    1,
    [
        (2, [
            (4, []),
            (5, [])
        ]),
        (3, [
            (6, []),
            (7, [])
        ])
    ]
)


# 6. Unbalanced tree
tree_unbalanced = (
    1,
    [
        (2, []),
        (3, [
            (4, [
                (5, [
                    (6, [])
                ])
            ])
        ])
    ]
)


# 7. Generic tree with different numbers of children
tree_generic = (
    10,
    [
        (20, [
            (50, []),
            (60, [])
        ]),
        (30, []),
        (40, [
            (70, []),
            (80, []),
            (90, [])
        ])
    ]
)


# 8. Tree containing duplicate values
tree_duplicates = (
    1,
    [
        (2, [
            (3, []),
            (2, [])
        ]),
        (1, [
            (3, []),
            (1, [])
        ])
    ]
)


# 9. Tree containing zero and negative values
tree_negative = (
    0,
    [
        (-10, [
            (-20, []),
            (5, [])
        ]),
        (10, [
            (-5, []),
            (20, [])
        ])
    ]
)


# 10. Larger multi-level tree
tree_large = (
    1,
    [
        (2, [
            (5, []),
            (6, [
                (11, []),
                (12, [])
            ])
        ]),
        (3, [
            (7, [
                (13, [])
            ])
        ]),
        (4, [
            (8, []),
            (9, [
                (14, []),
                (15, [
                    (16, [])
                ])
            ]),
            (10, [])
        ])
    ]
    ) 
test_cases = {
    "tree2":tree2_data,
    "complex_tree":tree1_data,
    "empty": tree_empty,
    "single": tree_single,
    "flat": tree_flat,
    "linear": tree_linear,
    "balanced": tree_balanced,
    "unbalanced": tree_unbalanced,
    "generic": tree_generic,
    "duplicates": tree_duplicates,
    "negative": tree_negative,
    "large": tree_large
    }

if __name__=='__main__':
    # tree1=build_tree(tree1_data)
    # print_tree(tree1)
    pass