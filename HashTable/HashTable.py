class HashTable:
    def __init__(self, size):
        self.numBucket = size
        self.hashMap = [[] for i in range(self.numBucket)]
    def __str__(self):
        return str(self.__dict__)
    
    def _hash(self, key):
        return len(key) % self.numBucket

    def set(self, key, value):
        hashKey = self._hash(key)
        keyValuePairs = self.hashMap[hashKey]
        for i in range(len(keyValuePairs)):
            if keyValuePairs[i][0] == key:
                keyValuePairs[i][1] = value
                return None
        keyValuePairs.append([key, value])
        return None

    def get(self, key):
        hashKey = self._hash(key)
        keyValuePairs = self.hashMap[hashKey]
        for i in range(len(keyValuePairs)):
            if keyValuePairs[i][0] == key:
                return keyValuePairs[i][1]
        return -1

    def remove(self, key):
        hashKey = self._hash(key)
        keyValuePairs = self.hashMap[hashKey]
        for i in range(len(keyValuePairs)):
            if keyValuePairs[i][0] == key:
                result = keyValuePairs[i]
                del keyValuePairs[i]
                return result

        return -1 
    
    def key(self):
        result = []
        for i, valueI in enumerate(self.hashMap):
            # print('i: {}, valueI: {}'.format(i, valueI))
            if valueI: 
                for j, valueJ in enumerate(valueI):
                    # print('j: {}, valueI: {}'.format(j, valueJ))
                    result.append(valueJ[0])
        return result



myHashTable = HashTable(5)
myHashTable.set('grapes', 1000)
myHashTable.set('apples', 10)
myHashTable.set('bananas', 11)
print(str(myHashTable))
print(myHashTable.key())
myHashTable.remove('apples')

print(str(myHashTable))
print(myHashTable.get('grapes'))

myHashTable.set('grapes', 5000)
print(myHashTable.get('grapes'))