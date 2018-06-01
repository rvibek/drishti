from pattern import web
from pattern.web import URL, Element
import re
from datetime import datetime, date, timedelta


url = URL('https://docs.google.com/spreadsheets/d/1J2I40hglES63YZHROcOL3oAjDPqiiKLRPE_ikAWsR-Q/pubhtml?gid=1267634591').read()
dom = Element(url)
dom = dom.by_tag('tbody')[0]


#date Get the date from the header
today = date = dom.by_class('s0')[1].content


#places Read the place from available class='s4' inside <td>
places = []
for ix in dom.by_class('s4'):
       places.append(ix.content)

reading_row = [4, 10, 16, 22]
pol_reading = []

def cleanhtml(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  cleantext = cleantext.strip("Highest: ")
  return cleantext


def cleandate(txt):
        txt =  txt.split("(")
        txt  = txt[1].strip(")")
        if txt == 'Today':
                return today
        else:
          yesterday = datetime.strptime(today, '%A,%B %d,%Y') - timedelta(days = 1)
          return yesterday.strftime('%A,%B %d,%Y')



def ctime(txt):
        txt = txt.split(" at ")
        txt = txt[1].split("(")
        return txt[0]

higest_val_row = [6, 12, 18]

ahighest =[]
atime = []
adate = []

try:
       for row in higest_val_row:
        updated = dom.by_tag('tr')[row]
        updated = updated.by_tag('td')


        for i in updated:
                if len(i) >= 1:
                        text = i.content
                        text = cleanhtml(text)
                        # print text
                        time = ctime(text)
                        highest = text.split(" ")[0]
                        date = cleandate(text)

                        print highest,time,date
                        ahighest.append(highest)
                        atime.append(time)
                        adate.append(date)


except:
       pass
        # print pol_updated.append(text.replace("Highest: ", ""))
print len(ahighest), len(places), len(adate), len(atime)



quote = '"'
delimit = ","
filepath = "/home/rvibek/git/drishti/drishti.csv" #folder path
# filepath = "drishti.csv"
for i in range(0,len(places)):
  highest_reading = quote+str(adate[i])+quote+delimit+ quote+str(atime[i])+quote+delimit+quote+places[i]+quote+delimit+ahighest[i]+delimit+"H"

  with open(filepath, 'a') as myfile:
          myfile.write(highest_reading+ "\n")
  #print highest_reading
