class Empty(Exception):
    """Error attempting to access am element from an empty container"""
    pass

class UrlStack:
    def __init__(self):
        self.data = []
        self.forwardpage = []

    def __len__(self):
        """return the numbers of pages in the URL stack"""

        return len(self.data)

    def push(self,page):
        """add the page to the stack when getting into next page"""

        self.data.append(page)

    def is_empty(self):
        "if the stack is empty,return true"

        return len(self.data) == 0

    def Back(self,page):
        """get back to the last page users have viewed and remove it from the stack"""

        if self.is_empty():
            raise Empty
        lastpage = self.data.pop()
        self.forwardpage.append(page)
        return lastpage

    def lastview(self):
        """return the last page users have viewed but not remove it"""

        if self.is_empty():
            raise Empty
        return self.data[-1]

    def forward(self,page):
        """forward"""

        if len(self.forwardpage) == 0:
            raise Empty
        forward = self.forwardpage.pop()
        self.push(page)
        return forward

def main():
    print("1.get back to the last page you have viewed\n2.return the last page you have viewed\n3.forward to the next page\n4.store the page\n5.break")
    choice = int(input("please input your choice"))
    stack = UrlStack()
    while True:
        if choice == 1:
            print(stack.Back(input("please input the current page")))
        if choice == 2:
            print(stack.lastview())
        if choice == 3:
            print(stack.forward(input("please input the current page")))
        if choice == 4:
            stack.push(input("please input the last page after getting into a new page"))
        if choice == 5:
            break
        choice = int(input("please input your choice"))
if __name__ == '__main__':
    main()