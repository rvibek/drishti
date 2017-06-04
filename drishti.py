from pattern import web
from pattern.web import URL, Element

url = URL('https://docs.google.com/spreadsheets/d/1J2I40hglES63YZHROcOL3oAjDPqiiKLRPE_ikAWsR-Q/pubhtml?gid=1267634591').read()
dom = Element(url)
dom = dom.by_tag('tbody')[0]


#date Get the date from the header
date = dom.by_class('s0')[1].content


#places Read the place from available class='s4' inside <td>
places = []
for ix in dom.by_class('s4'):
       		places.append(ix.content)

try:
       reading_row = [4, 10, 16, 22]
       pol_reading = []

       for row in reading_row:
               	reading = dom.by_tag('tr')[row]
               	reading = reading.by_tag('td')
               	for i in reading:
               		if len(i) >= 1:
               			pol_reading.append(i.content)


       pol_updated_row = [5, 11, 17, 23]
       pol_updated = []

       for row in pol_updated_row:
               	updated = dom.by_tag('tr')[row]
               	updated = updated.by_tag('td')
               	for i in updated:
               		if len(i) >= 1:
               			text = i.content
               			pol_updated.append(text.replace("Last Update at ", ""))

except:
       pass

n=0
quote = '"'
delimit = ","
filepath = "drishti.csv" #folder path
for ix in places:
       	last_reading = quote+str(date)+quote+delimit+quote+str(pol_updated[n])+quote+delimit+quote+places[n]+quote+delimit +str(pol_reading[n])+delimit+"R"
       	n = n+1
       	with open(filepath, 'a') as myfile:
       		myfile.write(last_reading+ "\n")
       	#print last_reading
