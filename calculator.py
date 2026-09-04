import os

def processData(data, flag=False):
    result = []
    for item in data:
        if item == None:
            continue
        try:
            result.append(item * 2)
        except:
            pass
    return result

class calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b
