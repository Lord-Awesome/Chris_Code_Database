from collections import deque
from startShow import startShow

def acceptRequest(request):
    if type(request) != type({}):
        print("BAD REQUEST: ", request)
        raise TypeError("Request was not a dict!")
    else:
        #call chris's function here
        # print("Recieved this request: ", request)
        startShow(request)

class RequestStack:
    def __init__(self):
        self.stack = deque()
        self.show_names = deque()

    def print(self):
        response = ''
        for x in self.shows:
            response += x
        return response

    def add(self, request, request_name):
        if(type(request) != type({})):
            print('Error in adding', request, 'as it is not a dict')
        self.stack.append(request)
        self.show_names.append(request_name)

    def getNextRequest(self):
        # print(self.stack)
        if(len(self.stack)):
            self.show_names.popleft()
            return self.stack.popleft()
        else:
            return ''

    def getIndex(self, show):
        try:
            return self.show_names.index(show)
        except:
            return -1

    def currentLength(self):
        return len(self.stack)