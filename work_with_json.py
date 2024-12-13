import json

def readJSONFilfe():
  with open("data.json","rt") as fData:
    data = json.load(fData)
    
    print(data["string"])
    print(data["object"]["a"][1])	
		
def main():
  readJSONFilfe()

if __name__ == "__main__":
  main()
