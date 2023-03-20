import socket
import re

#port number and server adress
PORT= 5000
SERVER= socket.gethostbyname(socket.gethostname())
SERVER=""
ADDRESS= (SERVER, PORT)

SocketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket is made using intenet (IP's) and TCP
SocketServer.bind(ADDRESS) #connecting the previous address with the server
SocketServer.listen(5)

print("The Server is Ready to work")

while True:

    ConnectionSoket, Address= SocketServer.accept() #openning one connection for each call
    Sentence= ConnectionSoket.recv(1024).decode() #socket is going to receive data in a buffer size of 1024 bytes at a time.
    print (Address)
    print(Sentence)
    IP= Address[0] #IP is taken from the address
    Port= Address[1] #Port is taken from the address
    URL = Sentence.split()[1] #URL is taken

    if (URL == "/" or URL == "/main.html"): #HTML index file

        #reading HTML file and saving its content in variable
        file = open('main.html')
        filecode = file.read()
        ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
        ConnectionSoket.send("Content-Type: text/html \r\n".encode())
        ConnectionSoket.send("\r\n".encode()) #ready to send data
        ConnectionSoket.send(filecode.encode())
        file.close()
    
    elif (URL.endswith('stylepage.css') or URL.endswith('stylepage.css/')):
        file = open('stylepage.css')
        filecode = file.read()
        ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
        ConnectionSoket.send("Content-Type: text/css \r\n".encode())
        ConnectionSoket.send("\r\n".encode()) #ready to send data
        ConnectionSoket.send(filecode.encode()) #sending css to browser
        file.close()

    elif (URL.endswith('contact.html') or URL.endswith('contact.html/')):
        file = open('contact.html',encoding="utf8")
        filecode = file.read()
        ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
        ConnectionSoket.send("Content-Type: text/html \r\n".encode())
        ConnectionSoket.send("\r\n".encode()) #ready to send data
        ConnectionSoket.send(filecode.encode())
        file.close()
        
    elif (URL.endswith('blueback.jpg') or URL.endswith('blueback.jpg/')): #picture of jpg type

        name = URL.split('/')[1] #image name
        type = URL.split('.')[1] #image extention
        ConnectionSoket.send('HTTP/1.1 200 OK\r\n'.encode())#server response is 200 OK
        ConnectionSoket.send(("Content-Type: image/" + type + "\r\n").encode()) #Type of the data content is jpg image so the browser can translate it
        ConnectionSoket.send("\r\n".encode())#ready to send data
        image_os = open(name, 'rb') #opening image info
        imageInfo = image_os.read() #reading image info
        image_os.close() #closing
        ConnectionSoket.send(imageInfo) #sending data to browser

    elif (URL.endswith('cover.png') or URL.endswith('cover.png/')): #picture of png type

         name = URL.split('/')[1] #image name
         type = URL.split('.')[1] #image extention
         ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
         ConnectionSoket.send(("Content-Type: image/" + type + "\r\n").encode())  #Type of the data content is png image so the browser can translate it
         ConnectionSoket.send("\r\n".encode())#ready to send data
         image_os = open(name, 'rb') #opening image info
         imageInfo = image_os.read() #reading image info
         image_os.close() #closing
         ConnectionSoket.send(imageInfo) #sending data to browser


    elif (URL.endswith('AnalogElectronics.png') or URL.endswith('AnalogElectronics.png/')): #picture of png type

         name = URL.split('/')[1] #image name
         type = URL.split('.')[1] #image extention
         ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
         ConnectionSoket.send(("Content-Type: image/" + type + "\r\n").encode())  #Type of the data content is png image so the browser can translate it
         ConnectionSoket.send("\r\n".encode())#ready to send data
         image_os = open(name, 'rb') #opening image info
         imageInfo = image_os.read() #reading image info
         image_os.close() #closing
         ConnectionSoket.send(imageInfo) #sending data to browser
    
    elif (URL.endswith('database.png') or URL.endswith('database.png/')): #picture of png type

         name = URL.split('/')[1] #image name
         type = URL.split('.')[1] #image extention
         ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
         ConnectionSoket.send(("Content-Type: image/" + type + "\r\n").encode())  #Type of the data content is png image so the browser can translate it
         ConnectionSoket.send("\r\n".encode())#ready to send data
         image_os = open(name, 'rb') #opening image info
         imageInfo = image_os.read() #reading image info
         image_os.close() #closing
         ConnectionSoket.send(imageInfo) #sending data to browser

    elif (URL.endswith('dsp.png') or URL.endswith('dsp.png/')): #picture of png type

         name = URL.split('/')[1] #image name
         type = URL.split('.')[1] #image extention
         ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
         ConnectionSoket.send(("Content-Type: image/" + type + "\r\n").encode())  #Type of the data content is png image so the browser can translate it
         ConnectionSoket.send("\r\n".encode())#ready to send data
         image_os = open(name, 'rb') #opening image info
         imageInfo = image_os.read() #reading image info
         image_os.close() #closing
         ConnectionSoket.send(imageInfo) #sending data to browser

    
    elif (URL.endswith('SortByName') or URL.endswith('SortByName/')): #Sorting file based on phone name and printing using HTML on browser

        ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
        ConnectionSoket.send(("Content-Type: text/html \r\n").encode())#Type of the file content is HTML code so the browser can translate it
        ConnectionSoket.send("\r\n".encode())#ready to send data
        phones_Sorted = [] #creating list
        with open("SmartPhones.txt", 'r') as File: #appending file content into the list
            for line in File:
                phones_Sorted.append(line)
        phones_Sorted.sort() #sorting the list by name
        File.close()
        phones_toString="" #converting the list into string
        for i in range (len(phones_Sorted)):
            phones_toString+= "<p>"+ str(phones_Sorted[i]) + "</p>" + "\n"
         #sending data in HTML, CSS form
        ConnectionSoket.send(("<html>" + "<style> body{background: rgb(186, 222, 234); background: linear-gradient(180deg, rgba(186, 222, 234,1) 0%, rgba(186, 222, 234,1) 100%)} .Div{ border:; background-color: #badeea; text-align: center; } </style>" + "<body>"+ "<h1 style=""text-align:center"">Sorted By Name</h1>" + "<div class=""Div"">" + phones_toString + "</div>" + "</body>" + "</html>").encode())

    elif (URL.endswith('SortByPrice') or URL.endswith('SortByPrice/')): #Sorting file based on phone price and printing using HTML on browser

        ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
        ConnectionSoket.send(("Content-Type: text/html \r\n").encode())#Type of the file content is HTML code so the browser can translate it
        ConnectionSoket.send("\r\n".encode())#ready to send data
        price_list = [] #creating list
        with open('SmartPhones.txt') as File: #appending file content into the list
            for line in File:
                price_list.append(line.split("|")) #getting the prices from the file

        for i in range (len(price_list)): #removing the non numerics from the strings in the list
            price_list[i][1] = re.sub("[^0-9]", "", price_list[i][1])

        for i in range(len(price_list) - 1):  # sorting the numbers in the list using bubble sort
            for j in range(0, len(price_list) - i - 1):
                if (int(price_list[j][1]) > int(price_list[j + 1][1])):
                    temp = price_list[j]
                    price_list[j] = price_list[j + 1]
                    price_list[j + 1] = temp

        for i in range (len(price_list)): #return data into original form but sorted
            price_list[i][1] = " " + price_list[i][1] + "$"

        # converting the list into string and using it in HTML code
        phones_toString=""
        for i in range (len(price_list)):
            phones_toString+= "<p>" + str(price_list[i][0]) + " : " + str(price_list[i][1]) + "</p>"
        #sending data in HTML, CSS form
        ConnectionSoket.send(("<html>" + "<style> body{background: rgb(186, 222, 234); background: linear-gradient(180deg, rgba(186, 222, 234,1) 0%, rgba(186, 222, 234,1) 100%)} .Div{ border:; background-color: #badeea; text-align: center; } </style>" + "<body>"+ "<h1 style=""text-align:center"">Sorted By Price</h1>" + "<div class=""Div"">" + phones_toString + "</div>" + "</body>" + "</html>").encode())
    
    else: #if anything except the above is entered in the URL

        #reading HTML error file and saving its content in variable
        file = open('ERROR.html')
        filecode = file.read()
        file.close()
        ConnectionSoket.send('HTTP/1.1 404 Not Found \r\n'.encode())#server response is 404 Not Found
        ConnectionSoket.send(("Content-Type: text/html \r\n").encode())#Type of the file content is HTML code so the browser can translate it
        ConnectionSoket.send("\r\n".encode())#ready to send data
        ConnectionSoket.send(filecode.encode())#sending data
        ConnectionSoket.send(("<html>" + "<style> body{background: rgb(186,222,234); background: linear-gradient(180deg, rgba(186,222,234,1) 0%, rgba(186,222,234,1) 100%)} .Div { border:; background-color: #badeea; text-align: center; } </style>" + "<body >" + "<div class=""Div"">" + "<p>" + "IP: " + str(IP) + "</p>" + "<p>" + "Port: " + str(Port) + "</p>" + "</div>" +"<body>"+ "</html>").encode())

        ConnectionSoket.close()