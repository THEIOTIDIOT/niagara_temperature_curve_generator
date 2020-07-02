import csv
import os

filename = '10K Type 2 - AIC.csv'

def getFarenheitCurve(filename):

    farenheitList = []

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            farenheitList.append(row[2])
            
    return farenheitList

def getResistanceCurve(filename):

    resistanceList = []

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            resistanceList.append(row[0])
            
    return resistanceList

def getCelciusCurve(filename):

    celciusList = []

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            celciusList.append(row[1])
            
    return celciusList
    
farenheitList = getFarenheitCurve(filename)
celciusList = getCelciusCurve(filename)
resistanceList = getResistanceCurve(filename)

def generateXmlTempCurve(resistanceCurve, temperatureCurve, tempCurveFilename):
    header = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<thermistor>\n<description>""" + tempCurveFilename + """</description>\n<table>\n"""

    body = ""
    point = ""

    for index in range(len(resistanceCurve)):
        point += "<point ohms=\"" + resistanceCurve[index] + "\""
        point += " farenheight=\"" + temperatureCurve[index] + "\"/>"
        body += point + "\n"
        point = ""
    
    footer = """</table>\n</thermistor>"""

    fileContents = header + body + footer

    xmlFileName = tempCurveFilename + ".xml"

    if os.path.exists(xmlFileName):
        os.remove(xmlFileName)
        with open(xmlFileName, "x") as newFile:
            newFile.write(fileContents)
    else:
        with open(xmlFileName, "x") as newFile:
            newFile.write(fileContents)

    


#print(resistanceList)
generateXmlTempCurve(resistanceList, farenheitList, "testCurve")
