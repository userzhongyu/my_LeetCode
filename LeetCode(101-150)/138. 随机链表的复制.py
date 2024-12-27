"""
# Definition for a Node.

"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dic = {}
        h = head
        p = Node(head.val, None, None)
        q = p
        dic[head] = q
        # 复制 next 指针，创建映射
        while h.next:
            cur = Node(h.next.val, None, None)
            dic[h.next] = cur
            q.next = cur
            q = q.next
            h = h.next
        q = p
        h = head
        # 根据 旧节点的 random 将新节点链接上新创建的节点
        while q:
            if h.random:
                q.random = dic[h.random]
            q = q.next
            h = h.next
        return p

# 输入输出处理
def build_list(data):
    """根据输入格式 [[val, random_index], ...] 创建链表"""
    if not data:
        return None
    nodes = [Node(val) for val, _ in data]
    for i, (_, random_index) in enumerate(data):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    return nodes[0]


def serialize_list(head):
    """将链表转化为 [[val, random_index], ...] 格式"""
    if not head:
        return []
    node_to_index = {}
    nodes = []
    current = head
    index = 0
    while current:
        node_to_index[current] = index
        nodes.append([current.val, None])
        current = current.next
        index += 1
    current = head
    index = 0
    while current:
        if current.random:
            nodes[index][1] = node_to_index[current.random]
        current = current.next
        index += 1
    return nodes

def main():
    input_data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    input_data = []
    original_head = build_list(input_data)

    # 运行复制函数
    solution = Solution()
    copied_head = solution.copyRandomList(original_head)

    # 输出
    output_data = serialize_list(copied_head)
    print("Output:", output_data)

if __name__ == '__main__':
    main()
