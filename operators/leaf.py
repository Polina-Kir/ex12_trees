"""."""

from default_operator import DefaultOperator
from tree_node import TreeNode


class Leaf(TreeNode):
    """Leaf node."""

    def __init__(self, value):
        """default constructor."""
        super().__init__(value)
        self.__value = value

    @property
    def priority(self):
        """:return the value of the operation."""
        return -1

    @property
    def associativity(self):
        """Nothing fancy here."""
        return True

    @property
    def default_operator(self):
        """Nothing fancy here."""
        return DefaultOperator(lambda x: x, "")

    def apply(self):
        """:return the value."""
        return self.__value

    def __str__(self):
        """:return the mathematical string representation of the tree with least amount of parenthesis."""
        return str(self.__value)
