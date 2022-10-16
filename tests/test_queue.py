import pytest
from priority_queue import PriorityQueue, QueueIsEmpty

arg_names: list[str] = [
    "initial_data",
    "expected_dump",
    "expected_after_push",
]
arg_values: list[tuple[
    list[float],
    list[float],
    list[float],
]] = [
    ([1, 2, 3], [], [1, 2, 3],),
    ([1, 2, 3, 4], [3], [1, 2, 3, 4]),
    ([4, 3, 2, 1], [1], [4, 3, 2, 1]),
    ([3, 1, 4, 2], [2], [3, 1, 4, 2]),
    ([3, 2, 3, 0], [0], [3, 2, 3, 0]),
]

sorted_names: list[str] = ["sorted_initial_data", "one", "two", "three", "four"]
sorted_values: list[
    tuple[
        list[float],
        list[float],
        list[float],
        list[float],
        list[float]]] = [
    ([1, 2, 3, -1], [1], [2, 1], [3, 2, 1], [3, 2, 1, -1]),
    ([1, 2, 3, 4], [1], [2, 1], [3, 2, 1], [4, 3, 2, 1]),
    ([4, 3, 2, 1], [4], [4, 3], [4, 3, 2], [4, 3, 2, 1]),
    ([3, 1, 4, 2], [3], [3, 1], [4, 3, 1], [4, 3, 2, 1]),
    ([3, 2, 3, 0], [3], [3, 2], [3, 3, 2], [3, 3, 2, 0])
]


@pytest.fixture
def queue() -> PriorityQueue:
    return PriorityQueue()


def test_empty_queue_pop_oldest(queue: PriorityQueue):
    with pytest.raises(QueueIsEmpty):
        queue.pop_oldest()


def test_empty_queue_pop_greatest(queue: PriorityQueue):
    with pytest.raises(QueueIsEmpty):
        queue.pop_greatest()


@pytest.mark.parametrize(arg_names, arg_values)
def test_priority_queue(
        initial_data: list[str],
        expected_dump: list[float],
        expected_after_push: list[float],
        queue: PriorityQueue):
    for item in initial_data:
        queue.push(item)

    assert queue.dump_data() == expected_after_push


@pytest.mark.parametrize(sorted_names, sorted_values)
def test_priority_order(
        sorted_initial_data: list[float],
        one: list[float],
        two: list[float],
        three: list[float],
        four: list[float],
        queue: PriorityQueue):
    for i, item in enumerate(sorted_initial_data):
        queue.push(item)
        if i == 0:
            compare_with = one
        elif i == 1:
            compare_with = two
        elif i == 2:
            compare_with = three
        elif i == 3:
            compare_with = four
        assert queue.get_max_ordered() == compare_with

@pytest.mark.parametrize(arg_names, arg_values)
def test_priorityqueue(
        initial_data: list[str],
        expected_dump: list[str],
        expected_after_push: list[str],
        queue: PriorityQueue):
    for item in initial_data:  # type: float
        queue.push(item)

    queue.pop_oldest()
    queue.pop_greatest()
    queue.pop_oldest()

    assert queue.dump_data() == expected_dump
