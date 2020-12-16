"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
At most 3 * 104 calls will be made to get and put.
"""


class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None


class LRUCache():

    def _remove_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

    def _remove_node(self, node):
        prev = node.prev
        nex = node.next

        prev.next = nex
        nex.prev = prev

    def _add_node(self, node):
        #         node.next = self.head.next
        #         node.prev = self.head

        #         self.head.next = node
        #         self.head.next.prev = node
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node):
        self._remove_node(node)

        self._add_node(node)

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if node is None:
            return -1
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.cache.get(key, None)
        if node is not None:
            node.value = value
            self._move_to_head(node)
        else:
            newNode = DLinkedNode()
            newNode.value = value
            newNode.key = key
            self.cache[key] = newNode
            self.size += 1
            self._add_node(newNode)

            if self.size > self.capacity:
                tail = self._remove_tail()
                del self.cache[tail.key]
                self.size -= 1
