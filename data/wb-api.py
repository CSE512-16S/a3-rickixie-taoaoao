import requests
import pandas
import json
import pandas as pd
#https://searchcode.com/codesearch/view/86732471/
#define countries/income level
#Countries code ---
#1. Low Income: LIC
#2. Middle Income: MIC
#3. Lower Middle Income = LMC
#4. Upper Middle Income = UMC
#5. Low & Middle Income = LMY --nope
#6. High Income = HIC
country_string = "LIC;MIC;LMC;UMC;HIC"

#define indicators
indicator_string = "SE.SCH.LIFE.FE"

#define source: Gender Statistics is 14
source = "14"

#define year
startYr = "2005"
endYr = "2014"

#define request url
#http://api.worldbank.org/countries/lic;mic;lmc;umc;lmy;hic/indicators/SP.ADO.TFRT;SH.STA.BRTC.ZS?source=14&date=1965:2014&per_page=50&format=json
url = "http://api.worldbank.org/countries/LIC;MIC;LMC;UMC;HIC/indicators/SE.SCH.LIFE.FE;SE.SCH.LIFE.MA?source=14&date=2005:2014&per_page=600&format=json"
# url = "http://api.worldbank.org/countries/%(country_stringP)s/indicators/%(indicator_stringP)s?source=%(sourceP)s&date=%(startYrP)s:%(endYrP)s&per_page=50&format=json"%{"country_stringP":country_string, "indicator_stringP" = indicator_string, "sourceP" = source, "startYrP"=startYr, "endYrP"=endYr}

response = requests.get(url)
data = json.loads(response.text)[1]
data1=json.dumps(data)
# data

file_name = "wb_%(indicatorstring)s.json"%{"indicatorstring":indicator_string}
wb_file = open(file_name,"w")
wb_file.write(data1)
wb_file.close()

# [
#   {"key":"clothing, beauty, & fashion",
#    "values":
#      [{"year":"2004", "n":141, "date":"2004-01-01"},{"year":"2005", "n":203, "date":"2005-01-01"},...]
#   },
#   {"key":"computers & internet",
#    "values":
#      [{"year":"2004", "n":2489, "date":"2004-01-01"},{"year":"2005", "n":2200, "date":"2005-01-01"},...]
#   },
#   ...
# ]

	# data3
	# {
	#     "indicator": {
	#       "id": "SP.ADO.TFRT",
	#       "value": "Adolescent fertility rate (births per 1,000 women ages 15-19)"
	#     },
	#     "country": {
	#       "id": "XD",//<---eliminate this
	#       "value": "High income"
	#     },
	#     "value": "19.8044573782575",
	#     "decimal": "0",//<---eliminate this
	#     "date": "2014"
	#   },

	# data1
	# 	[{"indicator": {
	# 		"id": "SP.ADO.TFRT",
	# 	      "value": "Adolescent fertility rate (births per 1,000 women ages 15-19)"
	# 	    },
	# 	"valueByIncomeLevel":
	# 		[{"country":"High income", 
	# 			"value":
	# 			[{"date":"2014", "value":19.8044573782575},{"date":"2015", "value":19.8044573782575}]
	# 		},
	# 		{"country":"Middle High income", 
	# 			"value":
	# 			[{"date":"2014", "value":19.8044573782575},{"date":"2015", "value":19.8044573782575}]
	# 			}
	# 		]
	# 	}]
	





# var indicators = [] #all indicators


# var indicators_keys = [] #store keys of all indicators_IncomeLevel

# var indicators_IncomeLevel = []
# var indicator_allValue = []

# for indicator in data:
# 	if indicator['id'] in indicator_allValue.keys == false: #if the indicator is new
# 		#create the indicator dictionary
# 		new_indicator = {}
# 		new_indicator['indicator']={}
# 		new_indicator.indicator = {"indicator_Id": indicator['id'], "indicator_Name":indicator['value']}
# 		# new_indicator['indicator_Name'] = indicator['value']
# 		new_indicator['incomeLevel'] = {} #create a new list item to store time series of all income level
# 		indicator_allValue.append(new_indicator) #create a new list item and store in the allValue
# 		# indicator.append(indicator['id']) #mark the indicator as added
# 		indicator_IncomeLevelCheck = indicator['id']+indicator['country']['id']
# 			if indicator_IncomeLevelCheck in indicators_IncomeLevel == false: #if income level is not in the indicator
# 				new_indicator_IncomeLevel = {}
# 				new_indicator_IncomeLevel['incomeLevel_Short'] = indicator['country']['id']
# 				new_indicator_IncomeLevel['incomeLevel_Name'] = indicator['country']['value']
# 	else:


# def GetIndicator (f, seq):
# 	for indicator in seq:
# 		if f(indicator):
# 			return indicator


# def checkIndicatorIncomeLevel (indicator):
# 		result = GetIndicator(indicator, indicator_allValue)
# 		if result is not None:
# 			result
		



# def find_element(children_list,name):
#     """
#     Find element in children list
#     if exists or return none
#     """
#     for i in children_list:
#         if i["name"] == name:
#             return i
#     #If not found return None
#     return None

# def add_node(path,value,nest):
#     """
#     The path is a list.  Each element is a name that corresponds 
#     to a level in the final nested dictionary.  
#     """

#     #Get first name from path
#     this_name = path.pop(0)

#     #Does the element exist already?
#     element = find_element(nest["children"], this_name)

#     #If the element exists, we can use it, otherwise we need to create a new one
#     if element:

#         if len(path)>0:
#             add_node(path,value, element)

#     #Else it does not exist so create it and return its children
#     else:

#         if len(path) == 0:
#             nest["children"].append({"name": this_name, "value": value})
#         else:
#             #Add new element
#             nest["children"].append({"name": this_name, "children":[]})

#             #Get added element 
#             element = nest["children"][-1]

#             #Still elements of path left so recurse
#             add_node(path,value, element)

# df = pd.read_json(data)
# d = {"name": "root",
# "children": []}

# levels = ["l1","l2", "l3"]
# for row in df.iterrows():
#     r = row[1]
#     path = list(r[levels])
#     value = r["val"]
#     add_node(path,value,d)
# # print json.dumps(d, sort_keys=False, indent=2)