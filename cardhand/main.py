from random import randint
class CardHand:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self,element,next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __iter__(self):
        p = self._head
        while p != None:
            original = p._element
            yield original
            p = p._next

    def add_cards(self,r,s):
        p = self._head
        found = 0
        for i in range(self._size):
            if p._element == s:#在链表中寻找花色s
                found += 1
                break
            p = p._next
        if found == 0:#当没有找到花色s时，在手牌末尾加该花色
            point = self._head
            while point._next != None:
                point = point._next#将指针移到链表尾部
            newest = self._Node(s,None)
            point._next = newest
        else:#当手牌中有花色s时，此时p在花色s的第一张牌处
            if r == 1:#加的牌在第一张时
                if p == self._head:
                    newest = self._Node(s,p)
                    self._head = newest#花色位置在最前面时
                else:
                    p = self._head
                    while p._next._element != s:
                        p = p._next#将指针移到位置r处
                    newest = self._Node(s, p._next)
                    p._next = newest
            elif r == 2:#加在花色s的第二张牌处
                newest = self._Node(s, p._next)
                p._next = newest
            else:
                for i in range(r - 2):
                    p = p._next#将指针移到花色s的位置r处
                newest = self._Node(s, p._next)
                p._next = newest
            self._size += 1

    def play(self,s):
        p = self._head
        found = 0
        for i in range(self._size):#寻找花色s
            if p._element == s:
                found += 1
                break
            p = p._next
        if found == 0:#当手牌中没有花色s时
            rand = randint(1,self._size)#利用随机数随机出牌
            p = self._head
            if rand == 1:#如果打手牌第一张牌
                self._head = p._next
                oldvalue = p._element
                p._next = p._element = None
                self._size -= 1
                return oldvalue
            elif rand == 2:#如果打手牌第二张牌
                delete = p._next
                p._next = delete._next
                oldvalue = delete._element
                delete._next = delete._element = None
                self._size -= 1
                return oldvalue
            else:
                for i in range(rand-2):
                    p = p._next#将指针移到删除牌的前一张牌
                delete = p._next
                p._next = delete._next
                oldvalue = delete._element
                delete._next = delete._element = None
                self._size -= 1
                return oldvalue
        else:#手牌中有花色s时，此时p在花色s时的第一张牌处
            count = 0
            first = p
            while p._element == s:
                p = p._next
                count += 1#找出花色s有几张牌
            rand = randint(1,count)
            if rand == 1:#打花色s的第一张牌
                if first == self._head:#当花色s在手牌头时
                    oldvalue = first._element
                    self._head = first._next
                    first._next = first._element = None
                    self._size -= 1
                    return oldvalue
                else:#花色s不在牌头时
                    point = self._head
                    while point._next != first:
                        point = point._next#将指针移到花色s第一张牌前面的一张牌
                    point._next = first._next
                    oldvalue = first._element
                    first._element = first._next = None
                    self._size -= 1
                    return  oldvalue
            elif rand == 2:#打花色s的第二张牌
                delete = first._next
                first._next = delete._next
                oldvalue = delete._element
                delete._next = delete._element = None
                self._size -= 1
                return oldvalue
            else:
                for i in range(rand-2):
                    first = first._next#指针移到打花色s某张牌的前一张牌处
                delete = first._next
                first._next = delete._next
                oldvalue = delete._element
                delete._next = delete._element = None
                self._size -= 1
                return oldvalue

    def all_of_suit(self,s):
        p = self._head
        found = 0
        for i in range(self._size):
            if p._element == s:#找花色s
                found += 1
                break
            p = p._next
        if found == 0:#如果牌中没有花色s，返回None
            return None
        else:
            while p._element == s:
                original = p._element
                yield original
                p = p._next











