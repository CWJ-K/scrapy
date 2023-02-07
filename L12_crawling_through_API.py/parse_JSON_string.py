import json

jsonString = '''
    {
        "arrayOfNums": [{"number":0},{"number":1},{"number":2}],
        "arrayOfFruites": [{"fruit": "apple"},{"fruit":"banana"},{"fruit":"pear"}]
    }
'''

jsonObj = json.loads(jsonString)

print(jsonObj.get('arrayOfNums'))
print(jsonObj.get('arrayOfNums')[1])
print(
    jsonObj.get('arrayOfNums')[1].get('number') +
    jsonObj.get('arrayOfNums')[2].get('number')
)
print(jsonObj.get('arrayOfFruites')[2].get('fruit'))


