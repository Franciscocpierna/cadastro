from time import sleep
real = "O que e real Como voce define o real Se voce esta falando sobre o que voce pode sentir o que voce pode cheirar o que voce pode saborear e ver o real sao simplesmente sinais eletricos interpretados pelo seu cerebro".split()

natodic = {"A":"Alfa","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"Xray","Y":"Yankee","Z":"Zulu","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","0":"ZERO"}

guardaitem= []




for r in real:
   somaletra=""
   s=0
   if len(r)>1:
    while s <= len(r)-1:
     if r[s].upper() in natodic:
        somaletra=somaletra+natodic[r[s].upper()]
     s=s+1 
    if len(somaletra) > 0:
       guardaitem.append(somaletra)     
   else:
    if r.upper() in natodic:
       guardaitem.append(natodic[r.upper()])            
   
     
print(guardaitem)      
