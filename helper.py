import re

def FindIndexDuplicate(listVar, strVar):
	indexList = []
	for x in range(len(listVar)):
		try:
			indexInt = listVar.index(strVar, x)
		except ValueError:
			break
		else:
			indexList.append(indexInt)
	return indexList

def ListToString(arglist):
	allstring = ""
	for row in arglist:
		for elem in row:
			allstring += elem
	return allstring

def RemoveDuplicate(listVar):
	"Remove Duplicates in a list"
	result = list(dict.fromkeys(listVar))
	return result

def ChangeUnit(valueStr, scaleStr):
	"Change unit of the values"
	conval = 0.00
	baseval = 0.00
	origval = ''
	expo = ''
	eflag = re.findall("e", valueStr)
	if len(eflag) != 0:
		eindex = valueStr.index("e")
		for elem in range(eindex+1, len(valueStr)):
			expo += valueStr[elem]
		#convert to base value
		for elem in range(eindex):
			origval += valueStr[elem]
		if (expo == "-001"):
			baseval = float(origval) * 0.1
		elif (expo == "-002"):
			baseval = float(origval) * 0.01
		elif (expo == "-003"):
			baseval = float(origval) * 0.001
		elif (expo == "-004"):
			baseval = float(origval) * 0.0001
		elif (expo == "-005"):
			baseval = float(origval) * 0.00001
		elif (expo == "-006"):
			baseval = float(origval) * 0.000001
		elif (expo == "-007"):
			baseval = float(origval) * 0.0000001
		elif (expo == "-008"):
			baseval = float(origval) * 0.00000001
		elif (expo == "-009"):
			baseval = float(origval) * 0.000000001
		elif (expo == "-010"):
			baseval = float(origval) * 0.0000000001
		elif (expo == "-011"):
			baseval = float(origval) * 0.00000000001
		elif (expo == "-012"):
			baseval = float(origval) * 0.000000000001
		#convert to scale
		if int(scaleStr) == 0:
			conval = baseval * 1
		elif int(scaleStr) == 3:
			conval = baseval * 1000
		elif int(scaleStr) == 6:
			conval = baseval * 1000000
		elif int(scaleStr) == 9:
			conval = baseval * 1000000000
		elif int(scaleStr) == 12:
			conval = baseval * 1000000000000
		result = str(conval)
	else:
		result = valueStr
	return(result)





