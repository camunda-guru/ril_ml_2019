# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:16:55 2018

@author: Balasubramaniam
"""

from xml.dom import minidom
#create DOM object
doc=minidom.Document()
#rootnode
rootElement=doc.createElement("Claims")
doc.appendChild(rootElement)

file =open("claimdata.csv","r")

for line in file:   
    temp=line.split(",")
    if(temp[0] !="ClaimId"):
        #claim
        node=doc.createElement("Claim")
        #node.setAttribute('ClaimId','12345')
        rootElement.appendChild(node)
        #claim id Node
        childNode=doc.createElement("ClaimId")
        textNode = doc.createTextNode(temp[0])
        childNode.appendChild(textNode)
        node.appendChild(childNode)
        
        #PolicyNo Node
        childNode=doc.createElement("PolicyNo")
        textNode = doc.createTextNode(temp[1])
        childNode.appendChild(textNode)
        node.appendChild(childNode)
        
        #Claim Amount
        childNode=doc.createElement("ClaimAmount")
        textNode = doc.createTextNode(temp[2])
        childNode.appendChild(textNode)
        node.appendChild(childNode)
        #Status
        childNode=doc.createElement("Status")
        textNode = doc.createTextNode(temp[3])
        childNode.appendChild(textNode)
        node.appendChild(childNode)
    
    
#indentation
xml_str = doc.toprettyxml(indent="  ")
with open("allstate_claims.xml", "w") as f:
    f.write(xml_str)

