from tkinter import *
from tkinter import colorchooser
'''

Author : Ezz Elsadaty
Date : 1/1/2023
Email :191900074@ecu.edu.eg

'''

def decToHexa(n):

    # char array to store hexadecimal number
    hexaDeciNum = ['0'] * 100
    # Counter for hexadecimal number array
    i = 0
    while (n != 0):
        # Temporary variable to store remainder
        temp = 0
        # Storing remainder in temp variable.
        temp = n % 16
        # Check if temp < 10
        if (temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        n = int(n / 16)

    hexCode = ""
    if (i == 2):
        hexCode = hexCode + hexaDeciNum[1]
        hexCode = hexCode + hexaDeciNum[0]

    elif (i == 1):
        hexCode = "0"
        hexCode = hexCode + hexaDeciNum[0]

    elif (i == 0):
        hexCode = "00"

    # Return the equivalent
    # hexadecimal color code
    return hexCode

# Function to convert the
# RGB code to Hex color code
def convertRGBtoHex(R, G, B):

    if ((R >= 0 and R <= 255) and
        (G >= 0 and G <= 255) and
            (B >= 0 and B <= 255)):
        hexCode = '#'
        r1 = int(R)
        g1 = int(G)
        b1 = int(B)
        hexCode = hexCode + decToHexa(r1)
        hexCode = hexCode + decToHexa(g1)
        hexCode = hexCode + decToHexa(b1)
        return hexCode

    # The hex color code doesn't exist
    else:
        return "-1"

# Function to Calculate the area
def bilinearinterarea(l1 ,l2 ,w1  ,w2) :
    area1 = l1 * w1
    area2 = l2 * w1
    area3 = l1 * w2
    area4 = l2 * w2
    arrarea = [area1 , area2 , area3 , area4]
    return arrarea


# Function of the Bilinearinterpolation equations
def bilinearinter1(l1 ,l2 ,w1, w2,point1 =[] ,point2 =[] ,point3 =[],point4 =[]) :
    newpoint =[]
    area = bilinearinterarea(l1 ,l2 ,w1  ,w2)
    color_code =[]
    np0= point1[0]*area[3] +point2[0]*area[2]+point3[0]*area[1]+point4[0]*area[0]
    newpoint.append(np0)
    np1= point1[1]*area[3] +point2[1]*area[2]+point3[1]*area[1]+point4[1]*area[0]
    newpoint.append(np1)
    np2= point1[2]*area[3] +point2[2]*area[2]+point3[2]*area[1]+point4[2]*area[0]
    newpoint.append(np2)
    print(newpoint)
    color_code.append(newpoint)
    color_code.append(convertRGBtoHex(np0,np1,np2))
    return color_code


# Clear All things to start again
def delete():
    Text3.delete("1.0","end")
    Text2.delete("1.0","end")
    Text1.delete("1.0","end")
    Text1.insert(END,'B')
    Text2.insert(END,'R')
    Text3.insert(END,'G')
    button5.config(bg='white',text='Expected value')
    button1.config(bg='white',text='Select first color')
    button2.config(bg='white',text='Select Sec color')
    button3.config(bg='white',text='Select Third color')
    button4.config(bg='white',text='Select Fourth color')


# 5 functions to pick the color
def choose_color1():
    color_code = colorchooser.askcolor(title ="Choose color")
    global point1
    point1 = color_code[0]    
    button1.config(bg=color_code[1], text="Color Value :{}".format(color_code[0]))
    print(point1)
    print(color_code)
    return point1

def choose_color2():
    color_code = colorchooser.askcolor(title ="Choose color")
    global point2
    point2 = color_code[0]    
    button2.config(bg=color_code[1], text="Color Value :{}".format(color_code[0]))
    print(point2)
    print(color_code)
    return point2
    

def choose_color3():
    color_code = colorchooser.askcolor(title ="Choose color")
    global point3
    point3 = color_code[0]    
    button3.config(bg=color_code[1], text="Color Value :{}".format(color_code[0]))
    print(point3)
    print(color_code)
    return point3 

def choose_color4():
    color_code = colorchooser.askcolor(title ="Choose color")
    global point4
    point4 = color_code[0]
    button4.config(bg=color_code[1] , text="Color Value :{}".format(color_code[0]))
    print(point4)
    print(color_code)
    return point4 

# Making the new point and print rgb value in the fields
def choose_color5():
    c = bilinearinter1(0.57 ,0.43 ,0.5, 0.5,point1 ,point2,point3,point4)
    print(c)
    Text3.delete("1.0","end")
    Text2.delete("1.0","end")
    Text1.delete("1.0","end")
    Text3.insert(END,int(c[0][0]))
    Text2.insert(END,int(c[0][1]))
    Text1.insert(END,int(c[0][2]))
    # T.insert(END,c[1])
    # x="(%s ,%x ,%d)" %(int(c[0][0]),int(c[0][1]),int(c[0][2])) 
    button5.config(bg=c[1],text='I am the new point')
    

    

root = Tk()
# title of the window
root.title('My Bilinear Func')

# the intializing of the buttons
button1 = Button(root, text = "Select first color",height=10, width=20,command = choose_color1)
button2 = Button(root, text = "Select secound color",height=10, width=20,command = choose_color2)
button3 = Button(root, text = "Select third color",height=10, width=20,command = choose_color3)
button4 = Button(root, text = "Select fourth color",height=10, width=20,command = choose_color4)
button5 = Button(root, text = "Expected value",height=10, width=20,command = choose_color5)

#griding the buttons on the window
button1.grid(row = 0, column = 2)
button2.grid(row = 0, column = 4)
button3.grid(row = 2, column = 2)
button4.grid(row = 2, column = 4)
button5.grid(row = 1,column=3)
#making texts to write the rgb value of the new point
Text1 = Text(root,height=1,width=7)
Text1.grid(row=1,column=2)
Text2 = Text(root,height=1,width=7)
Text2.grid(row=1,column=0)
Text3 = Text(root,height=1,width=7)
Text3.grid(row=1,column=1)
Text1.insert(END,'B')
Text2.insert(END,'R')
Text3.insert(END,'G')
l = Label(root, text = "  ",height=10, width=20)
l.grid(row=0,column=1)
l['background']='#34568B'

b1= Button(root, text= "Delete",command= delete)
b1.grid(row=2,column=5)
root['background']='#34568B'
root.geometry("700x550")
root.mainloop()















# def bilinearinter1(point1 ,point2 ,point3 ,point4 ,l1 ,l2 ,w1  ,w2) :
#     newpoint =[100]
#     area = bilinearinterarea(l1 ,l2 ,w1  ,w2)
#     for i in range(0,3):
#         newpoint[i]= point1[i]*area[3] +point2[i]*area[2]+point3[i]*area[1]+point4[i]*area[0]
#         print(newpoint[i])
#     return newpoint

# def bilinearinterarea(l1 ,l2 ,w1  ,w2) :
#     area1 = l1 * w1
#     area2 = l2 * w1
#     area3 = l1 * w2
#     area4 = l2 * w2
#     arrarea = [area1 , area2 , area3 , area4]
#     return arrarea

# x1 = float(input("please enter the first pieace of width "))
# x2 = float(input("please enter the secound pieace of width "))
# y1 = float(input("please enter the first pieace of Length "))
# y2 = float(input("please enter the secound pieace of Length "))
# point1 =[]
# for i in range(0,3) :
#     z=float(input("enter point 1 : "))
#     point1.append(z)
# point2 =[]
# for i in range(0,3) :
#     z=float(input("enter point 2 : "))
#     point2.append(z)
# point3 =[]
# for i in range(0,3) :
#     z=float(input("enter point 3 : "))
#     point3.append(z)
# point4 =[]
# for i in range(0,3) :
#     z=float(input("enter point 4 : "))
#     point4.append(z)

# c =bilinearinter1(x1 ,x2 ,y1  ,y2,point1 ,point2 ,point3 ,point4)
# print("your new point is : " , c )


