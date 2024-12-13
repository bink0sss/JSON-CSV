import json

def readJSONFilfe():
  with open("data.json","rt") as fData:
    data = json.load(fData)
    
    print(data["string"])
    print(data["object"]["a"][1])	
		
def fromJSONStringToObject():
  x = '{"k1": 1, "k2": "abc"}'
  
  y = json.loads(x)
  print(y["k2"])
	
def fromObjectToJSONString():
  x = {
    "k1": 1,
    "k2": "abc"
		}
  y = json.dumps(x)
  print(y)
  print(type(y))
def fromJSONToCSV():
  with open("12.json","rt") as fData:
    data = json.load(fData)
    print(data[object]["timeServer"])
def main():
  #readJSONFilfe()
  #fromJSONStringToObject()
  #fromObjectToJSONString()
  fromJSONToCSV()
if __name__ == "__main__":
  main()
