"""
Link: https://leetcode.com/problems/design-browser-history/

Used a doubly linked list instead of an dynamic array or stacks.
"""


class HistoryNode:
    def __init__(self, url='homepage', next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.headNode = HistoryNode(homepage)
        self.currentPage = self.headNode

    def visit(self, url: str) -> None:
        newNode = HistoryNode(url=url, prev=self.currentPage)
        self.currentPage.next=newNode
        self.currentPage=newNode

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.currentPage.prev==None:
                return self.currentPage.url
            self.currentPage = self.currentPage.prev
        return self.currentPage.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.currentPage.next==None:
                return self.currentPage.url
            self.currentPage = self.currentPage.next
        return self.currentPage.url    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)