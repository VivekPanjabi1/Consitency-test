import json

def FetchData(url, params={}):
    data = json.loads(url)
    if data == None:
        return []
    try:
        return data["results"]
    except:
        return []

class datamanager:
    def save(self, path, content):
        with open(path, "w") as f:
            f.write(content)
        return 200
