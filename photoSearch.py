from concurrent.futures import thread
import  pymysql
import tkinter as tk
from PIL import Image,ImageTk
import datetime

TEXTSIZE = 18
TEXTFONT=('Courier',TEXTSIZE)
PAD_Y = 15
PHOTOSIZE =(400,250)

    
def enter_the_license_num():
    global window
    global licenseEntry
    prompt = tk.Label(window, text = '請輸入車牌:')
    prompt.pack()
    licenseEntry = tk.Entry(window, width = 10) 
    licenseEntry.pack()
    button = tk.Button(window, text = 'Enter',  command = show_the_photo()) 
    button.pack()

def show_the_photo():
    global window
    global licenseEntry
    global TkImg
    TkImg = None
    search()
    photo = tk.Label(window, image = TkImg)
    photo.pack()
    photo = tk.Label(window, text = '照片是否正確?')
    yesButton = tk.Button(window, text = '正確', command = enter_the_license_num) 
    noButton = tk.Button(window, text = '錯誤', command = enter_the_license_num) 
    yesButton.pack()
    noButton.pack
       

class photoSearchProgram():
  


    def connect(self):
        try:
            self.connection = pymysql.connect()
            print("successfully connect to database")
        except:
            print("cannot connect to database")

    def close(self):
        self.connection.close()

    def search(self):
        
        command = "SELECT * FROM vehicle_data WHERE license_plate_number = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(command, (self.licenseNum.get(),))
            record = cursor.fetchone()
            self.write_file(record[6],'./img/'+self.licenseNum.get())
            self.enterTimeStr.set(record[1].strftime('進場時間:%Y-%m-%d %H:%M:%S'))
            img = Image.open('./img/'+self.licenseNum.get())
            img = img.resize(PHOTOSIZE)
            return ImageTk.PhotoImage(img)
    
    def write_file(self, data, filename):
    # Convert binary data to proper format and write it on Hard Disk
     with open(filename, 'wb') as file:
            file.write(data)

    def enter_license_plate(self):
        self.noPhotoFrame.pack_forget()
        self.showPhotoFrame.pack_forget()
        self.licenseNum.set('')
        self.enterLicenseFrame.pack()



    def show_license_plate_photo(self):
        self.enterLicenseFrame.pack_forget()
        try:
          img = self.search()
          
          self.photo.config(image = img)
          self.photo.photo_ref = img
          self.showPhotoFrame.pack()
        except:
           self.noPhotoFrame.pack()







    def __init__(self):
            self.connect()
            self.window = tk.Tk()
            self.window.title('photo search terminal')
            self.window.geometry("600x400+250+150")

            self.enterLicenseFrame = tk.Frame(self.window)
            enterPrompt = tk.Label(self.enterLicenseFrame, text = '請輸入車牌:', font=TEXTFONT)
            self.licenseNum = tk.StringVar()
            licenseEntry = tk.Entry(self.enterLicenseFrame, width = 10, font= TEXTFONT, textvariable= self.licenseNum)
            button = tk.Button(self.enterLicenseFrame, text = 'Enter',  command = self.show_license_plate_photo, font=TEXTFONT) 
            enterPrompt.pack(pady=(PAD_Y,PAD_Y))
            licenseEntry.pack(pady=(PAD_Y,PAD_Y))
            button.pack(pady=PAD_Y)
            
            self.showPhotoFrame = tk.Frame(self.window)
            self.photo = tk.Label(self.showPhotoFrame, image = None)
            self.photo.pack(pady=(PAD_Y,PAD_Y))
            self.enterTimeStr = tk.StringVar()
            self.enterTimeStr.set('')
            enterTimePrompt = tk.Label(self.showPhotoFrame, textvariable = self.enterTimeStr , font=TEXTFONT)
            enterTimePrompt.pack(pady=(PAD_Y,PAD_Y))
            button = tk.Button(self.showPhotoFrame, text = 'OK',  command = self.enter_license_plate, font=TEXTFONT) 
            button.pack(pady=(PAD_Y,PAD_Y))

            self.noPhotoFrame = tk.Frame(self.window)
            sorryPrompt = tk.Label(self.noPhotoFrame, text = '找不到您的愛車', font=TEXTFONT)
            button = tk.Button(self.noPhotoFrame, text = 'OK',  command = self.enter_license_plate, font=TEXTFONT)
            sorryPrompt.pack(pady=(PAD_Y,PAD_Y))
            button.pack(pady=(PAD_Y,PAD_Y))


            self.enter_license_plate()
            self.window.mainloop()


app = photoSearchProgram()

