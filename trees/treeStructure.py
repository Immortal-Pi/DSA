from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.child=[]

    def add_children(self,node):
        self.child.append(node)


def print_level_wise(root):
    if root is None:
        print("Empty tree")
        return

    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        children_values = []

        for child in current_node.child:
            children_values.append(str(child.data))
            queue.append(child)

        print(f"{current_node.data}: {', '.join(children_values)}")


def build_trees(data):
    """ 
    data format:
    (node_value,[child1,child2,....])
    """
    value,children_data=data
    root=TreeNode(value)
    for child in children_data:
        child_node=build_trees(child)
        root.child.append(child_node)
    return root

tree1_data=(1,[
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

    for name, tree_data in test_cases.items():
        print(f"\nTesting: {name}")

        if tree_data is None:
            root = None
        else:
            root = build_trees(tree_data)

        print_level_wise(root)