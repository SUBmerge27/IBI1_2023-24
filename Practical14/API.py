#import libraries
import datetime 
import xml.dom.minidom
import matplotlib.pyplot as plt
import xml.sax
#initialize 3 values to be 0
molecular_function=0
biological_process=0
cellular_components=0

#use DOM API to complete this task
start_time_DOM=datetime.datetime.now() #record start time
DOMTree=xml.dom.minidom.parse("/Users/submerge/IBI1_2023-24/Practical14/go_obo.xml") #parse the file into DOMTree
root_element=DOMTree.documentElement #get the root element
term_elements=root_element.getElementsByTagName("term") #get "term" elements
for term_element in term_elements: #iterate through every "term" element
        if term_element.getElementsByTagName("namespace")[0].firstChild.nodeValue=="molecular_function":
            molecular_function+=1 #Update the corresponding counter based on the value of the namespace
        elif term_element.getElementsByTagName("namespace")[0].firstChild.nodeValue=="biological_process":
            biological_process+=1
        elif term_element.getElementsByTagName("namespace")[0].firstChild.nodeValue=="cellular_component":
            cellular_components+=1
end_time_DOM=datetime.datetime.now() #record ending time
DOM_time=end_time_DOM-start_time_DOM #calculate how much time is used
#printing results
print(f"The number of GO terms within biological_process is {molecular_function} using DOM API")
print(f"The number of GO terms within biological_process is {biological_process} using DOM API")
print(f"The number of GO terms within biological_process is {cellular_components} using DOM API")
print(f"Time taken for SAX API to complete this	task is {DOM_time}")
#plot barcharts
categories=["Molecular function","Biological process","Cellular components"]
data=[molecular_function,biological_process,cellular_components]
plt.bar(categories,data)
plt.show()
plt.clf()

#use SAX API to complete this task
class SAX(xml.sax.ContentHandler): #define a handler
    def __init__(self): 
       self.molecular_function=0 #initialize values or variables to be zero or empty
       self.biological_process=0
       self.cellular_components=0
       self.CurrentData=""
       self.namespace=""
    def startElement(self,tag,attributes): #Begins parsing a new element
        self.CurrentData=tag
    def characters(self,content): #Parse the character data inside the element
        if self.CurrentData=="namespace":
            self.namespace+=content
    def endElement(self,tag): #End parsing an element
        if self.CurrentData=="namespace":
            if self.namespace=="molecular_function":
                self.molecular_function+=1 #Update the corresponding counter based on the value of the namespace
            elif self.namespace=="biological_process":
                self.biological_process+=1
            elif self.namespace=="cellular_component":
                self.cellular_components+=1
            self.CurrentData="" #Reset variable
            self.namespace=""
start_time_SAX=datetime.datetime.now() #record ending time
parser=xml.sax.make_parser() #Create an instance of the SAX parser
parser.setFeature(xml.sax.handler.feature_namespaces,0) #Set a feature to ignore namespaces
handler=SAX() #Instantiate an instance of the SAX_API class, which will act as the parser's content handler
parser.setContentHandler(handler)#Set the parser's content handler to the handler instance you just created
parser.parse("/Users/submerge/IBI1_2023-24/Practical14/go_obo.xml")#parse file
end_time_SAX=datetime.datetime.now()#record ending time
SAX_time=end_time_SAX-start_time_SAX #calculate how much time is used
#print results
print(f"The number of GO terms within molecular_function is {handler.molecular_function} using SAX API")
print(f"The number of GO terms within biological_process is {handler.biological_process} using SAX API")
print(f"The number of GO terms within cellular_components is {handler.cellular_components} using SAX API")
print(f"Time taken for SAX API to complete this	task is {SAX_time}")
#plot bar charts
categories=["Molecular function","Biological process","Cellular component"]
data=[handler.molecular_function,handler.biological_process,handler.cellular_components]
plt.bar(categories,data)
plt.show()
plt.clf()

print("Conclusion: SAX API is faster than DOM API") #summary 

    