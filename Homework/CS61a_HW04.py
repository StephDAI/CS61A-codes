def shuffle(s):
    t1 = iter(s[0:len(s)//2])
    t2 = iter(s[len(s)//2:])
    ans = list()
    for i in range(len(s)//2):
        ans.append(next(t1))
        ans.append(next(t2))
    return ans

# print(shuffle(range(6)))
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print(shuffle(letters))
# print(shuffle(shuffle(letters)))
# print(letters)
def deep_map(f,s):
    for i in range(len(s)):
        if type(s[i]) == list: deep_map(f,s[i])
        else: s[i] = f(s[i])

# six = [1, 2, [3, [4], 5], 6]
# deep_map(lambda x: x * x, six)
# print(six)
# s = [3, [1, [4, [1]]]]
# s1 = s[1]
# s2 = s1[1]
# s3 = s2[1]
# deep_map(lambda x: x + 1, s)
# print(s)
# print(s1 is s[1])
# print(s2 is s1[1])
# print(s3 is s2[1])
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def berry_finder(t):
    if label(t) == 'berry': return True
    t = iter(branches(t))
    for i in t:
        if berry_finder(i) == True: return True
    return False

# scrat = tree('berry')
# print(berry_finder(scrat))
# sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
# print(berry_finder(sproul))
# numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
# print(berry_finder(numbers))
# t = tree(1, [tree('berry',[tree('not berry')])])
# print(berry_finder(t))

def max_path_sum(t):
    if is_leaf(t) : return label(t)
    Max = -1
    for i in branches(t):
        Max = max(Max,max_path_sum(i))
    return Max + label(t)

# t2 = tree(5, [tree(4, [tree(1), tree(9)]), tree(2, [tree(10), tree(3)])])
# print(max_path_sum(t2))