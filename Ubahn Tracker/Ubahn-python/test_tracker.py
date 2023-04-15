
import requests
import json
import time
import datetime
from tkinter import * 


#print(time.strftime('%H:%M:%S ', time.gmtime(2)))
#print(time.strftime('%H:%M:%S ', time.localtime(1634045760000/1000)))
#print(time.strftime('%M',time.localtime(0)))

master = Tk()
master.title('Ubahn Tracker')
master.geometry("500x600")
master.config(bg="midnight blue")

direction0 = Label(master,font=("Calibri",25),bg="midnight blue",fg="white")
direction1 = Label(master,font=("Calibri",25),bg="midnight blue",fg="white")
direction2 = Label(master,font=("Calibri",25),bg="midnight blue",fg="white")
direction3 = Label(master,font=("Calibri",25),bg="midnight blue",fg="white")
direction4 = Label(master,font=("Calibri",25),bg="midnight blue",fg="white")
direction5 = Label(master,font=("Calibri",25),bg="midnight blue",fg="white")

direction0.grid(row=0,column=0)
direction1.grid(row=1,column=0)
direction2.grid(row=2,column=0)
direction3.grid(row=3,column=0)
direction4.grid(row=4,column=0)
direction5.grid(row=5,column=0)

"""""
time0 = Label(master,font=("Calibri",25),bg="white",fg="black")
time1 = Label(master,font=("Calibri",25),bg="white",fg="black")
time2 = Label(master,font=("Calibri",25),bg="white",fg="black")
time3 = Label(master,font=("Calibri",25),bg="white",fg="black")
time4 = Label(master,font=("Calibri",25),bg="white",fg="black")
time5 = Label(master,font=("Calibri",25),bg="white",fg="black")
"""""

#test = requests.get("https://www.mvg.de/api/fahrinfo/departure/de:09162:520?footway=0")
#info = json.loads(test.content)


#Berechnet die Zeit aus dem Epoch Unix Zeitstempel, von MVG in Millisekunden gegeben? 
def timeconverter(time1): 

        conv_time1 = time.strftime('%M ', time.localtime((time1/1000)-(time.time()+7200)))
        #if int(conv_time1[0]) <= 0: return "00"
        return conv_time1


# Überprüft die Stunden Differenz, gebraucht um Ubahnen die in über einer Stunde kommen zu filter
# Gibt Stunden versetzt an also ist weniger als eine Stunde hier wert 23
def timechecker(time1): 

        conv_time1 = time.strftime('%H', time.localtime((time1/1000)-(time.time()+7200)))
        #if int(conv_time1[0]) <= 0: return "00"
        return conv_time1


#Berechnet die wirkliche Zeit mit eingebautem Delay 
def timeconverter_delay(data): 

        conv_time1 = time.strftime('%M', time.localtime((int(data["departureTime"])/1000)-(time.time()+7200)))
        #if int(conv_time1[0]) <= 0: return "00"
        if data["delay"] == 0:
            return conv_time1
        else : 
            return str(int(conv_time1) + data["delay"])

def delete_label(label):
    label.destroy()

"""""
def label_print(posi):
    match posi:
        case 0:
            direction0.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            return
        case 1:
            direction1.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            return
        case 2:
            direction2.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            return
        case 3:
            direction4.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            return
        case 4:
            direction4.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            return
        case 5:
            direction5.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            return
        
"""""  



def tracking():
    test = requests.get("https://www.mvg.de/api/fahrinfo/departure/de:09162:520?footway=0")
    info = json.loads(test.content)
    position = 0
    for dep in info["departures"]:
        

        if dep["product"] == "UBAHN":
            #print(timechecker(int(dep["departureTime"])))
            if int(timechecker(int(dep["departureTime"]))[0]) != 0:
             
             if int(timeconverter(int(dep["departureTime"]))) < 31:
              if position < 6:       
                    des = dep["destination"]
                    dep_time = timeconverter(int(dep["departureTime"]))

                    
                    match position:
                            case 0:
                                 direction0.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            
                            case 1:
                                direction1.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            
                            case 2:
                                direction2.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            
                            case 3:
                                direction3.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            
                            case 4:
                                direction4.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            
                            case 5:
                                direction5.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
            



                 

                    #direction.config(text="Richtung:  "+des +"\n"+"Verbleibende Zeit: "+dep_time +"Min"+"\n")
                   

                    #print("Richtung: \t\t "+dep["destination"])
                    ###########print("Verbleibende Zeit: \t "+ timeconverter(int(dep["departureTime"]))) Ohne Delay
                    #print("MitVerspätung:   \t"+ timeconverter_delay(dep) + "\n")
                    #print(position)
                    position=position +1 
        

            
        
    master.after(8000,tracking)





tracking()

master.mainloop()























