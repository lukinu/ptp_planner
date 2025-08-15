import json
import csv
import zipfile

BRAND = 'http://infinet.ru/kml'
HEAD = '<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:projectdata="' + BRAND + '"><Document id="1t-UlJIsJjQEInqy4VwWc-mk-s5xufjVo"><name>New Project</name><open>1</open><ExtendedData><projectdata:json>'
TAIL = '</projectdata:json></ExtendedData></Document></kml>'
sitesArray = []
linksArray = []

with open('links.csv', newline='') as csvfile:
    links_lst = csv.reader(csvfile, delimiter=',')
    link = 
    linksArray.append(link)
    # for row in links_lst:
        # print(', '.join(row))

jstring = json.loads('{"appVersion":"f4eb57c","appVersionFull":"f4eb57c","linksArray":[{"terrainType":"AVERAGE","climateType":"NORMAL","frequencies":{"start":4850,"end":6050},"band":5450,"transmissionType":"SINGLE_CARRIER","bandwidth":10,"goal":{"type":"DISTANCE","value":30000},"txPowerLimit":"Infinity","temperature":293.15,"totalAirPressure":1013.2499968000001,"humidity":60,"startSite":{"id":782582,"name":"ÇİM-NAK","location":{"latitude":40.7797151668,"longitude":29.5982600517},"antennaHeight":17,"deviceProductKey":"Quanta 5#Q5-23","antennaPartNumber":null,"rfCablePartNumber":null,"relocationLocked":false,"interference":"-Infinity","temperature":293.1499938964844,"powerLimit":null},"endSite":{"id":782581,"name":"kamera diregi","location":{"latitude":40.7905567792,"longitude":29.5967539525},"antennaHeight":15,"deviceProductKey":"Quanta 5#Q5-23","antennaPartNumber":null,"rfCablePartNumber":null,"relocationLocked":false,"interference":"-Infinity","temperature":293.1499938964844,"powerLimit":null}}],"sitesArray":[{"id":782582,"name":"ÇİM-NAK","location":{"latitude":40.7797151668,"longitude":29.5982600517},"antennaHeight":17,"deviceProductKey":"Quanta 5#Q5-23","antennaPartNumber":null,"rfCablePartNumber":null,"relocationLocked":false,"interference":"-Infinity","temperature":293.1499938964844,"powerLimit":null},{"id":782581,"name":"kamera diregi","location":{"latitude":40.7905567792,"longitude":29.5967539525},"antennaHeight":15,"deviceProductKey":"Quanta 5#Q5-23","antennaPartNumber":null,"rfCablePartNumber":null,"relocationLocked":false,"interference":"-Infinity","temperature":293.1499938964844,"powerLimit":null}],"obstaclesArray":[],"project":{"id":78620,"name":"Burkina-Faso","type":"PTP","regulation":"WORLDWIDE","unitSystem":"METRIC","settings":{"ptmp":{"visible":true}},"updatedDatetime":"2025-05-02T09:22:54.718996Z","eirpInfo":{"otherLimit":50,"freqLimits":[]},"createNew":0}}')
print(json.dumps(jstring, indent=4))

with open("file.kml", "w") as f:
    f.write(HEAD + TAIL)

# f = open("file.kml","r")
# print(f.read())