import requests

def trace(*args):
  """Used for debug output"""
  print (*args)  # Comment out this line to remove debug output
  pass

"""# This base URL works, but doesn't return anything too interesting
# After running this script, read https://www.boredapi.com/ and
# figure out how to change it to get back a filtered activity.
# The filter is up to you: number of people, category, price, etc.
# Tip: try testing the API URLs directly in a browser first
URL = "https://www.boredapi.com/api/activity"

# Get data from the web site and put it into Python collections
trace ("Calling", URL)
response = requests.get(URL) # Get data from the URL
response.raise_for_status()  # Throw an exception if the request failed
data = response.json()       # Parse the response into JSON

# See what the raw data looks like
trace ("\nText returned:", response.text)"""

activities = ["recreational", "educational", "relaxation", "social", "cooking"]
print ("Available activities:", activities)
type = input("What type of activity would you like to do? ")
while type not in activities:
  type = input("Try again: ")


URL = "https://www.boredapi.com/api/activity?type=" + type 
trace ("Calling", URL)
response = requests.get(URL) # Get data from the URL
response.raise_for_status()  # Throw an exception if the request failed
data = response.json()       # Parse the response into JSON

# See what the raw data looks like
trace ("\n You should: ", data["activity"])


