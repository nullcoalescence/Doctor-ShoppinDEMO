"""
Game engine
"""

import json

class Engine:

    def __init__():
        print()

    def loadScenario(filePath):
        # Load file into JSON
        scenarioFile = open(filePath)
        jsonFormat = json.load(scenarioFile)

        # Iterate through each item in the file
        for item in jsonFormat["commands"]:
            print(str(item.keys()))

            
            commandType = item.keys()
            if commandType == "message":
                print("message")
            elif commandType == "delay":
                print("delay")
            elif commandType == "choices":
                print("choices")
            elif commandType == "results":
                print("resuilts")
            elif commandType == "loadScenario":
                print("load scenario")
            else:
                raise Exception("Invalid command in json file (" + filePath + "): " + commandType)
                
        

    if __name__ == "__main__":
        loadScenario("json/scenario1.json")