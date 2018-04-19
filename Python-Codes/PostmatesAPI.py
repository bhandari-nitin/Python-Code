#  #######
#  # ### #
#  ### # #
#      # #
#      ###        Hungry LLC 
#                 Drafted 1/28/2018.
#      ###        Nitin Bhandari


###################################################
##### Creating a delivery using postmates API #####
###################################################

# This API is responsible for creating a delivery if they operate in specified delivery and pick up addresses
# Postmate's API Link: https://postmates.com/developer/docs

import requests
import json

###################################################
############# HyperSetting and Params #############
###################################################

Customer_ID = cus_LWbgu5VCiVkTrk
Signature_Secret = 9b3df0fd-6f42-4449-8045-3105f3860859
Sandbox_Key = 8947f7d6-2c09-472f-b983-0e810e869d13     # sandbox key to simulate test deliveries

#############################################
############# Support Functions #############
#############################################

# Postmates API docs says to see if the pick up and delivery zones are in serviceable areas, use 'Get quote endpoint'
# This method is reposible for verifying the delivery and pickup address is serviceable and gets the delivery Quote
def getDeliveryQuote():
	get_quote_url = https://api.postmates.com/v1/customers/cus_LWbgu5VCiVkTrk/delivery_quotes
	rep = request.post(url=get_quote_url)


def createDelivery():
#This method is resposible for creating a delivery

