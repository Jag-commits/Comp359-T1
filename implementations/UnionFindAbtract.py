# This is an abstract base class in Python for our unionfinds
# I can already see we prefer different naming styles, this will enforce a common one.
# Any subclass MUST implement these methods.
# This ensures it works with the rest of the code.

#PLEASE read https://peps.python.org/pep-0008/
#it will save all a bunch of head space (:

from abc import ABC, abstractmethod


class Template(ABC):
    """Template for Union-Find implementations. Any subclass MUST implement these methods. This ensures it works with the rest of the code."""

    @abstractmethod
    def find(self, p: int) -> int:
        """Return the root for set p. If 2 elements have the same root they belong to the same set
        
        Example: uf.find(1) returns the root of the set containing 1
        """
        raise NotImplementedError

    @abstractmethod
    def connected(self, p: int, q: int) -> bool:
        """Return True when p and q are in the same set.
        
        Example: uf.connected(1, 2) returns True if 1 and 2 are in the same set, False otherwise
        """
        raise NotImplementedError

    @abstractmethod
    def union(self, p: int, q: int) -> None:
        """Merge the sets containing p and q.
        
        Example: uf.union(1, 2) merges the sets containing 1 and 2
        """
        raise NotImplementedError
