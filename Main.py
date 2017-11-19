import cv2 
import numpy as np
import os
from tkFileDialog   import askopenfilename   
import time

#import DetectChars
#import DetectPlates
import PossiblePlate
from Tkinter import *
import pymysql as sq
#import database as db
from database import store,fetch_data

rt=Tk()

rt.geometry("1500x700")
#----------------------Frame_INITILIZATION---------------------------
topframe=Frame(rt,width=1500,height=150,bg="white",relief=SUNKEN)
topframe.pack(side=TOP)

centreframe=Frame(rt,width=750,height=700,bg="white",relief =SUNKEN)
centreframe.pack(side=LEFT)
centreframe1=Frame(rt,width=700,height=700,bg="white",relief =SUNKEN)
centreframe1.pack(side=RIGHT)

def open_database():
    print"i'm here"
    db.fetch_data()
    return





def character(variable):
    
    global string
    string=""
    string=string+str(variable)
    data.set(string)
    print "string %s" % string    
    return 

def clear_display():
    global operator
    operator=""
    data.set(operator)
    print "heel"

#def store_database(id,image_name,data):
    
   # store(id,image_name,data)


operator=""
   
string=""
data=StringVar()

datadisplay5=Entry(centreframe1,font=('arial',30,'bold'),textvariable=data,bd=10,insertwidth=4,bg="white",justify='right').grid(row=1,column=0)

def main(image):

    blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()         

    if blnKNNTrainingSuccessful == False:                               
        print "\nerror: KNN traning was not successful\n"               
        return                                                          
    # end if

    imgOriginalScene  = image
               

    if imgOriginalScene is None:                            
        print "\nerror: image not read from file \n\n"      
        os.system("pause")                                
        return                                              
    # end if

    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           

    listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)       

    cv2.imshow("imgOriginalScene", imgOriginalScene)            

    if len(listOfPossiblePlates) == 0:                          
        print "\nno license plates were detected\n"            
    else:                                                       # else
                # if we get in here list of possible plates has at leat one plate

                # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
        listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

                # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
        licPlate = listOfPossiblePlates[0]

        cv2.imshow("imgPlate", licPlate.imgPlate)  
       # cv2.imwrite('imageplate.png',licPlate.imgPlate)         # show crop of plate and threshold of plate
        cv2.imshow("imgThresh", licPlate.imgThresh)
       # cv2.imwrite('licPlate.png',licPlate.imgThresh)

        if len(licPlate.strChars) == 0:                     # if no chars were found in the plate
            print "\nno characters were detected\n\n"       # show message
            return                                          # and exit program
        # end if

                   # draw red rectangle around plate

        print "\nlicense plate read from image = " + licPlate.strChars + "\n"       # write license plate text to std out
        print "----------------------------------------"
###########character(licPlate.strChars)
        drawRedRectangleAroundPlate(imgOriginalScene, licPlate)  
        
        
        writeLicensePlateCharsOnImage(imgOriginalScene, licPlate)           

        cv2.imshow("imgOriginalScene", imgOriginalScene)                
 #       store_database(licPlate.strChars)
       # cv2.imwrite("imgOriginalScene.png", imgOriginalScene)          

    # end if else

    cv2.waitKey(0)					

    return
# end main
def motor_control(data):
    print"i'm here"
    data_list=["D:/HEx/1.png","D:/HEx/2.png","D:/HEx/3.png","D:/HEx/4.png","D:/HEx/5.png"]
    if(data==data_list[0]):
        name="MCLRNF1"
        character(name)
    if(data==data_list[1]):
        name="LOLWATT"
        character(name)
    if(data==data_list[2]):
        name="RIP LS1"
        character(name)
    if(data==data_list[3]):
        name="NVSBLE"
        character(name)
    if(data==data_list[4]):
        name="NYSJ"
        character(name)
def callback():
    name= askopenfilename() 
    #name1=name
    #store()
    print"hwllo"
    print name
    #image= cv2.imread("%s" %name)
    #main(image)
    motor_control(name)
    
    return name
    
errmsg = 'Error!'






j=10
def video():
    
        vidcap = cv2.VideoCapture(0)
        success,image = vidcap.read()    
        print"im success"                                                   
        while success:
            success,image = vidcap.read()
            cv2.imwrite("%d.png" % j, image)    

            main(image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        vidcap.release()
        cv2.destroyAllWindows() 


def database():
    print "hello"
    


logo=Label(topframe,font=('Algerian',50,'bold'),text="VEHICLE NUMBER PLATE RECOGNITION",fg="steel Blue",bg="light gray",bd=10,anchor='w').grid(row=1,column=0)


localtime=time.asctime(time.localtime(time.time()))
timedisplay=Label(topframe,font=('',10,'bold'),text=localtime,fg="steel Blue",bg="white",bd=10,anchor='w')
timedisplay.grid(row=2,column=0)





button1=Button(centreframe,font=('arial',20,'bold'),text="Start video",bg="white",command=lambda:video()).grid(row=1,column=0,sticky='W')


button12=Label(centreframe,font=('arial',20,'bold'),text="Start video",fg="white",bg="white").grid(row=1,column=1,sticky='W')
button2=Button(centreframe,font=('arial',20,'bold'),text="Show Captured",bg="white",command=open_database).grid(row=2,column=2,sticky='W')
#picture=Button(centreframe,text='File Open', command=callback).pack(fill=X)
button3=Button(centreframe,font=('arial',20,'bold'),text="Open image",bg="white",command=callback).grid(row=3,column=0,sticky='W')

button5=Button(centreframe1,font=('arial',20,'bold'),text="Clear",bg="white",command=clear_display).grid(row=3,column=0,sticky='W')
#button6=Button(centreframe1,font=('arial',20,'bold'),text="Clear",bg="white",command=continous_data).grid(row=3,column=1,sticky='W')


lb=Label(centreframe1,font=('arial',20,'bold'),text="detected number plate",bg="white").grid(row=4,column=0)

        



rt.mainloop()









# module level variables ##########################################################################
SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

showSteps = False

###################################################################################################

###################################################################################################
def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):

    p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)           

    cv2.line(imgOriginalScene, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), SCALAR_RED, 2)         # draw 4 red lines
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), SCALAR_RED, 2)
# end function

###################################################################################################
def writeLicensePlateCharsOnImage(imgOriginalScene, licPlate):
    ptCenterOfTextAreaX = 0                             
    ptCenterOfTextAreaY = 0

    ptLowerLeftTextOriginX = 0                          
    ptLowerLeftTextOriginY = 0

    sceneHeight, sceneWidth, sceneNumChannels = imgOriginalScene.shape
    plateHeight, plateWidth, plateNumChannels = licPlate.imgPlate.shape

    intFontFace = cv2.FONT_HERSHEY_SIMPLEX                      
    fltFontScale = float(plateHeight) / 30.0                   
    intFontThickness = int(round(fltFontScale * 1.5))           

    textSize, baseline = cv2.getTextSize(licPlate.strChars, intFontFace, fltFontScale, intFontThickness)       

            # unpack roatated rect into center point, width and height, and angle
    ( (intPlateCenterX, intPlateCenterY), (intPlateWidth, intPlateHeight), fltCorrectionAngleInDeg ) = licPlate.rrLocationOfPlateInScene

    intPlateCenterX = int(intPlateCenterX)              
    intPlateCenterY = int(intPlateCenterY)

    ptCenterOfTextAreaX = int(intPlateCenterX)         

    if intPlateCenterY < (sceneHeight * 0.75):                                                  
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) + int(round(plateHeight * 1.6))     
    else:                                                                                      
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) - int(round(plateHeight * 1.6))      
    # end if

    textSizeWidth, textSizeHeight = textSize                

    ptLowerLeftTextOriginX = int(ptCenterOfTextAreaX - (textSizeWidth / 2))           
    ptLowerLeftTextOriginY = int(ptCenterOfTextAreaY + (textSizeHeight / 2))          

            # write the text on the image
    cv2.putText(imgOriginalScene, licPlate.strChars, (ptLowerLeftTextOriginX, ptLowerLeftTextOriginY), intFontFace, fltFontScale, SCALAR_YELLOW, intFontThickness)
# end function

###################################################################################################
#if __name__ == "__main__":
#    main()

















