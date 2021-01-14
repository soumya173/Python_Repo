# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from LinkedBinaryTree import LinkedBinaryTree

def main():
    lbt = LinkedBinaryTree()
    root = lbt._add_root(5)
    print(f'Root element: {root.element()}')
    lroot = lbt._add_left(root, 6)
    rroot = lbt._add_right(root, 7)
    print(f'Root left element: {lroot.element()}')
    print(f'Root right element: {rroot.element()}')
    llroot = lbt._add_left(lroot, 8)
    rlroot = lbt._add_right(lroot, 9)
    print(f'Root left left element: {llroot.element()}')
    print(f'Root left right element: {rlroot.element()}')
    lrroot = lbt._add_left(rroot, 10)
    rrroot = lbt._add_right(rroot, 11)
    print(f'Root left right element: {lrroot.element()}')
    print(f'Root right right element: {rrroot.element()}')
    print(f'Length: {lbt.__len__()}')
    print(f'Children: {lbt.num_children(rrroot)}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    status = main()
    sys.exit(status)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
