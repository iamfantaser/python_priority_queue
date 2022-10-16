from .abstract import AbstractPriorityQueue
from .exceptions import QueueIsEmpty
# import operator


class PriorityQueue(AbstractPriorityQueue):
    def __init__(self):
        self.fifo = None
        self.max = None
        self.count = 0

    class Node:
        def __init__(self, p, val, n):
            self.num = val
            self.next = n
            self.prev = p
            self.order_prev = self
            self.order_next = self

        def push_in_order(self, item, count):
            ptr = self
            index = 0
            while item.num <= ptr.num and index < count - 1:
                ptr = ptr.order_next
                index += 1
            item.order_next = ptr
            item.order_prev = ptr.order_prev
            ptr.order_prev = item
            item.order_prev.order_next = item
            if item.num > self.num:
                return item
            return self

        @staticmethod
        def push(item, dest):
            item.prev = dest.prev
            item.next = dest
            dest.prev = item
            item.prev.next = item

        def _cut(self):
            if self.next:
                self.next.prev = self.prev
            if self.prev:
                self.prev.next = self.next
            return self

        def _cut_ordered(self):
            if self.order_next:
                self.order_next.order_prev = self.order_prev
            if self.order_prev:
                self.order_prev.order_next = self.order_next
            return self

    def push(self, item) -> None:
        if (type(item) is float or type(item) is int) is not True:
            raise ValueError("Wrong type")
        n = self.Node(None, item, None)
        if self.fifo is None:
            self.fifo = n
            self.fifo.next = n
            self.fifo.prev = n
            self.count += 1
        else:
            self.Node.push(n, self.fifo)
            self.count += 1

        if self.max is None:
            self.max = n
        else:
            if self.count == 2:
                n.order_next = self.max
                n.order_prev = self.max
                self.max.order_next = n
                self.max.order_prev = n
                if self.max.num < n.num:
                    self.max = n
            else:
                self.max = self.max.push_in_order(n, self.count)

    def pop_oldest(self):
        if self.fifo is None:
            raise QueueIsEmpty("This is the end...")
        old = self.fifo._cut()
        old._cut_ordered()
        if old == self.max:
            self.max = self.max.order_next
        self.count -= 1
        self.fifo = old.next
        return old.num

    def pop_greatest(self):
        if self.max is None:
            raise QueueIsEmpty('This is the end...')
        great = self.max.num
        fifo = self.max._cut()
        self.max._cut_ordered()
        self.count -= 1
        if fifo == self.fifo:
            self.fifo = fifo.next
        self.max = self.max.order_next
        return great

    def dump_data(self):
        arr = []
        ptr = self.fifo
        for ind in range(self.count):
            arr.append(ptr.num)
            ptr = ptr.next
        return arr

    def get_max_ordered(self):
        arr = []
        ptr = self.max
        for ind in range(self.count):
            arr.append(ptr.num)
            ptr = ptr.order_next
        return arr

#Custom_test
# def test_output(
#         op_1,
#         op_2,
#         initial,
#         message
# ):
#     print('Initial data:', initial)
#     print(message, end='')
#     if operator.eq(op_1, op_2):
#         print(': OK')
#         print()
#         print()
#         return 1
#     else:
#         print(': KO')
#         print(op_1)
#         print()
#         print(op_2)
#         print()
#         #raise ValueError("Ooops...")
#         return -1
#
# if __name__ == "__main__":
#
#     total_ok = 0
#     total_ko = 0
#
#     initial_data = (
#         [1, 2, 3],
#         [1, 2, 3, 4],
#         [4, 3, 2, 1],
#         [3, 1, 4, 2],
#         #  [3, 2, 3, 0],
#     )
#     initial_data_mod = (
#         [1, 2, 3, -1],
#         [1, 2, 3, 4],
#         [4, 3, 2, 1],
#         [3, 1, 4, 2],
#         [3, 2, 3, 0],
#     )
#
#     data = [
#         ([1], [2, 1], [3, 2, 1], [3, 2, 1, -1]),
#         ([1], [2, 1], [3, 2, 1], [4, 3, 2, 1]),
#         ([4], [4, 3], [4, 3, 2], [4, 3, 2, 1]),
#         ([3], [3, 1], [4, 3, 1], [4, 3, 2, 1]),
#         ([3], [3, 2], [3, 3, 2], [3, 3, 2, 0])
#     ]
#
#     for x, row in enumerate(initial_data):
#         q = PriorityQueue()
#         for i, num in enumerate(row):
#             q.push(num)
#             cmp = q.get_max_ordered()
#             cmp2 = data[x][i]
#             if test_output(
#                 cmp,
#                 cmp2,
#                 initial_data[x],
#                 f"Test: {x+1} : {i+1}",
#             ) > 0:
#                 total_ok += 1
#             else:
#                 total_ko += 1
#
#     expected_dump = ([], [3], [1], [2])
#
#     for in1, expected in enumerate(expected_dump):
#         q = PriorityQueue()
#         for num in initial_data[in1]:
#             q.push(num)
#         old = q.pop_oldest()
#         great = q.pop_greatest()
#         old_1 = q.pop_oldest()
#
#         op = q.dump_data()
#         op1 = expected
#         if test_output(
#             op,
#             op1,
#             initial_data[in1],
#             f"Test fifo sequence: {in1 + 1} ",
#         ) > 0:
#             total_ok += 1
#         else:
#             total_ko += 1
#
#     data_fifo_cut = [
#         ([2, 3, -1], [3, -1], [-1], []),
#         ([2, 3, 4], [3, 4], [4], []),
#         ([3, 2, 1], [2, 1], [1], []),
#         ([1, 4, 2], [4, 2], [2], []),
#         ([2, 3, 0], [3, 0], [0], [])
#     ]
#     data_fusion_fifo_cut = [
#         ([3, 2, -1], [3, -1], [-1], []),
#         ([4, 3, 2], [4, 3], [4], []),
#         ([3, 2, 1], [2, 1], [1], []),
#         ([4, 2, 1], [4, 2], [2], []),
#         ([3, 2, 0], [3, 0], [0], [])
#     ]
#
#     data_fusion_ordered_cut = [
#         ([1, 2, -1], [1, -1], [-1], []),
#         ([1, 2, 3], [1, 2], [1], []),
#         ([3, 2, 1], [2, 1], [1], []),
#         ([3, 1, 2], [1, 2], [1], []),
#         ([2, 3, 0], [2, 0], [0], [])
#     ]
#     data_ordered_cut = [
#         ([2, 1, -1], [1, -1], [-1], []),
#         ([3, 2, 1], [2, 1], [1], []),
#         ([3, 2, 1], [2, 1], [1], []),
#         ([3, 2, 1], [2, 1], [1], []),
#         ([3, 2, 0], [2, 0], [0], [])
#     ]
#
#     try:
#         for in1, row in enumerate(data_fifo_cut):
#             q = PriorityQueue()
#             for num in initial_data_mod[in1]:
#                 q.push(num)
#             for in2, arr in enumerate(row):
#                 print(q.pop_oldest())
#                 cmp = q.dump_data()
#                 cmp1 = arr
#                 if test_output(
#                     cmp,
#                     cmp1,
#                     initial_data_mod[in1],
#                     f"Test fifo sequence: {in1 + 1} : {in2 + 1} ",
#                 ) > 0:
#                     total_ok += 1
#                 else:
#                     total_ko += 1
#
#                 cmp2 = q.get_max_ordered()
#                 cmp4 = data_fusion_fifo_cut[in1][in2]
#                 if test_output(
#                     cmp2,
#                     cmp4,
#                     initial_data_mod[in1],
#                     f"Test fifo pop and ordered state sequence: {in1 + 1} : {in2 + 1} ",
#                 ) > 0:
#                     total_ok += 1
#                 else:
#                     total_ko += 1
#
#         for in1, row in enumerate(data_ordered_cut):
#             q = PriorityQueue()
#             for num in initial_data_mod[in1]:
#                 q.push(num)
#             for in2, arr in enumerate(row):
#                 q.pop_greatest()
#                 cmp = q.get_max_ordered()
#                 cmp1 = arr
#                 if test_output(
#                     cmp,
#                     cmp1,
#                     initial_data_mod[in1],
#                     f"Test ordered pop and ordered sequence: {in1 + 1} : {in2 + 1} "
#                 ) > 0:
#                     total_ok += 1
#                 else:
#                     total_ko += 1
#
#                 cmp2 = q.dump_data()
#                 cmp3 = data_fusion_ordered_cut[in1][in2]
#                 if test_output(
#                     cmp2,
#                     cmp3,
#                     initial_data_mod[in1],
#                     f"Test ordered pop and fifo state sequence: {in1 + 1} : {in2 + 1} :",
#                 ) > 0:
#                     total_ok += 1
#                 else:
#                     total_ko += 1
#             print('Total_ok :', total_ok, "\nTotal_ko : ", total_ko)
#     except ValueError as err:
#         print(err, 'Total_ok: ', total_ok)
