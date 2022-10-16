import abc


class AbstractPriorityQueue(abc.ABC):
    @abc.abstractmethod
    def push(self, item: float) -> None:
        """Put an item into the queue"""

    @abc.abstractmethod
    def pop_oldest(self) -> float:
        """Return a queue element using FIFO order and remove it from queue"""

    @abc.abstractmethod
    def pop_greatest(self) -> float:
        """Return the greatest queue element and remove it from queue"""

    @abc.abstractmethod
    def dump_data(self) -> list[float]:
        """Return the list of current queue items ordered by push date"""
