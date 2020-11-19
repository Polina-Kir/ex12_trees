"""."""

from abc import abstractmethod
from tree_node import TreeNode


class Operator(TreeNode):
    """Custom operation wrapper."""

    def __init__(self, *args):
        """Store the given arguments somehow."""
        super().__init__(*args[0])
        self.__value = args[0]  # usually tuple of 2 elements

    def apply(self):
        """Make use of the *args to compute the value of the given subtree. Recursion is your friend."""
        params = [x.apply() for x in self.__value]
        types = tuple(type(x) for x in params)
        if self.actions.get(types):
            return self.actions[types](*params)
        else:
            return self.default_operator(*params)

    def class_str(self):
        """:return class string representation of the object."""
        return "Add(Leaf(5), Leaf(6))"

    @property
    def associativity(self):
        """abstract method witch should be overridden to return a boolean when the node is not associative."""
        return False

    @property
    @abstractmethod
    def default_operator(self):
        """abstract method which should be overridden to return the default_operator object."""
        pass

    @property
    @abstractmethod
    def priority(self):
        """
        abstract method witch should be overridden to return priority of the node.

        Boolean whether the operation is associative or not.

        For example addition is associative but subtraction is not.
        Override this property for operations where the given operation is not associative.

        Visit: https://en.wikipedia.org/wiki/Order_of_operations
        """
        pass

    @property
    @abstractmethod
    def actions(self):
        """
        All custom implemented actions on different data structures.

        For example set - int does not exist, but we can implement it.
        :return a dictionary of functions where key is accepted parameters and value is a function which takes the
        aforementioned parameters as inputs and computes a value with them.
        """
        pass

    def __str__(self):
        """:return the mathematical string representation of the tree with least amount of parenthesis."""
        operator_as_string = f" {self.default_operator.__str__()} "
        string_values = [x.__str__() for x in self.__value]
        return operator_as_string.join(string_values)
