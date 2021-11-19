from binary_tree import Node, preorder, postorder, inorder, levelorder

def test_preorder():
    tree = Node.from_preorder([4,1,3,7,5,6])
    actual = tree.sequence(preorder)
    assert actual == [4,1,3,7,5,6]

def test_postorder():
    tree = Node.from_preorder([4,1,3,7,5,6])
    actual = tree.sequence(postorder)
    assert actual == [3,1,6,5,7,4]

def test_inorder():
    tree = Node.from_preorder([4,1,3,7,5,6])
    actual = tree.sequence(inorder)
    assert actual == [1,3,4,5,6,7]

def test_levelorder():
    tree = Node.from_preorder([4,1,3,7,5,6])
    actual = tree.sequence(levelorder)
    assert actual == [4,1,7,3,5,6]

def test_count():
    tree = Node.from_preorder([4,1,3,7,5,6])
    actual = tree.count(preorder)
    assert actual == 6

def test_sum():
    tree = Node.from_preorder([4,1,3,7,5,6])
    actual = tree.sum(preorder)
    assert actual == 26

def test_max():
    tree = Node.from_preorder([4,1,3,7,5,6])
    actual = tree.max(preorder)
    assert actual == 7

def test_depth():
    tree = Node.from_preorder([4,1,3,7,5,6])
    actual = tree.depth()
    assert actual == 4

def test_max_cost():
    tree = Node.from_preorder([4,1,3,7,5,6])
    actual = tree.max_cost()
    assert actual == 22

def test_is_balanced_1():
    tree = Node.from_preorder([4,1,3,7,5,6])
    actual = tree.is_balanced()
    assert actual == True

def test_is_balanced_2():
    tree = Node.from_preorder([4,1,3,7,5,6,8,9])
    actual = tree.is_balanced()
    assert actual == False