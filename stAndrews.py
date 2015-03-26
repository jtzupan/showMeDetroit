import urllib2
import xml.etree.ElementTree as et 
import simplejson as sj


url = 'http://www.saintandrewsdetroit.com/api/TapEvent/GetEventCalendar?venueIds=65585%2C65791&departmentId=8&numberOfEvents=100&eventId=&offerId=0&_=1427327478292'

jsonText = urllib2.urlopen(url)
json = sj.load(jsonText)

stAndrewsDict = {}
for item in json:
    band = item.get('Artists')
    location = item.get('VenueName')
    event = item.get('EventName')
    date = item.get('EventDate')
    buyTix = item.get('BuyTicketUrl')
    genre = item.get('GenreName')
    x = band, location, event, date, buyTix, type
    stAndrewsDict[event] = x

return stAndrewsDict
