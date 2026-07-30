from binary_tree import BinaryTree, build_tree
from collections import deque
# ==========================================================
# TREE REFERENCE DIAGRAMS
# ==========================================================

# tree1 (Empty)
#
#   None
#

# tree2 (Single Node)
#
#   1
#

# tree3 (Only Left Child)
#
#     1
#    /
#   2
#

# tree4 (Only Right Child)
#
#   1
#    \
#     3
#

# tree5 (Two Children)
#
#     1
#    / \
#   2   3
#

# tree6 (Complete Binary Tree)
#
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#

# tree7 (Left Skewed)
#
#       1
#      /
#     2
#    /
#   3
#  /
# 4
#

# tree8 (Right Skewed)
#
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#

# tree9 (Sparse Tree)
#
#          1
#        /   \
#       2     3
#        \   /
#         5 6
#

# tree10 (Uneven Depth)
#
#            1
#          /   \
#         2     3
#        /     / \
#       4     5   6
#      /
#     8
#

# tree11 (Negative Values)
#
#      -1
#     /  \
#   -2   -3
#

# tree12 (Duplicate Values)
#
#           1
#         /   \
#        1     1
#       / \
#      1   1
#

# tree13 (Mixed Missing Children)
#
#          10
#         /  \
#        5    15
#         \   /
#          7 12
#

# tree14 (Large Balanced Tree)
#
#                    10
#               /          \
#              5            15
#            /   \        /    \
#           2     7      12     20
#          / \   / \    / \    /  \
#         1  3  6  8  11 13  18  25
#

# tree15 (Zig-Zag Tree)
#
#       1
#      /
#     2
#      \
#       3
#      /
#     4
#
# ==========================================================
# TEST CASE DEFINITIONS
# ==========================================================

# 1. Empty Tree
tree1 = None


# 2. Single Node
tree2 = (
    1,
    []
)


# 3. Root with Only Left Child
tree3 = (
    1,
    [
        (2, [])
    ]
)


# 4. Root with Only Right Child
tree4 = (
    1,
    [
        None,
        (3, [])
    ]
)


# 5. Root with Both Children
tree5 = (
    1,
    [
        (2, []),
        (3, [])
    ]
)


# 6. Complete Binary Tree
tree6 = (
    1,
    [
        (
            2,
            [
                (4, []),
                (5, [])
            ]
        ),
        (
            3,
            [
                (6, []),
                (7, [])
            ]
        )
    ]
)


# 7. Left-Skewed Tree
tree7 = (
    1,
    [
        (
            2,
            [
                (
                    3,
                    [
                        (4, [])
                    ]
                )
            ]
        )
    ]
)


# 8. Right-Skewed Tree
tree8 = (
    1,
    [
        None,
        (
            2,
            [
                None,
                (
                    3,
                    [
                        None,
                        (4, [])
                    ]
                )
            ]
        )
    ]
)


# 9. Sparse Tree
tree9 = (
    1,
    [
        (
            2,
            [
                None,
                (5, [])
            ]
        ),
        (
            3,
            [
                (6, []),
                None
            ]
        )
    ]
)


# 10. Uneven Depth Tree
tree10 = (
    1,
    [
        (
            2,
            [
                (
                    4,
                    [
                        (8, [])
                    ]
                )
            ]
        ),
        (
            3,
            [
                (5, []),
                (6, [])
            ]
        )
    ]
)


# 11. Negative Values
tree11 = (
    -1,
    [
        (-2, []),
        (-3, [])
    ]
)


# 12. Duplicate Values
tree12 = (
    1,
    [
        (
            1,
            [
                (1, []),
                (1, [])
            ]
        ),
        (1, [])
    ]
)


# 13. Mixed Missing Children
tree13 = (
    10,
    [
        (
            5,
            [
                None,
                (7, [])
            ]
        ),
        (
            15,
            [
                (12, []),
                None
            ]
        )
    ]
)


# 14. Large Balanced Tree
tree14 = (
    10,
    [
        (
            5,
            [
                (
                    2,
                    [
                        (1, []),
                        (3, [])
                    ]
                ),
                (
                    7,
                    [
                        (6, []),
                        (8, [])
                    ]
                )
            ]
        ),
        (
            15,
            [
                (
                    12,
                    [
                        (11, []),
                        (13, [])
                    ]
                ),
                (
                    20,
                    [
                        (18, []),
                        (25, [])
                    ]
                )
            ]
        )
    ]
)


# 15. Zig-Zag Tree
tree15 = (
    1,
    [
        (
            2,
            [
                None,
                (
                    3,
                    [
                        (4, []),
                        None
                    ]
                )
            ]
        ),
        None
    ]
)


# Run all test cases
test_cases = [
    tree1, tree2, tree3, tree4, tree5,
    tree6, tree7, tree8, tree9, tree10,
    tree11, tree12, tree13, tree14, tree15
]

if __name__=='__main__':
    for i, t in enumerate(test_cases, 1):
        try:
            root = build_tree(t)
            print(f"Test Case {i}: PASS")
        except Exception as e:
            print(f"Test Case {i}: FAIL -> {e}")