# -*- coding: utf-8 -*-
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk



key = ''

def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ''

mx = 1
my = 1

def main_proc():
    global mx, my
    if key == 'Up' and maze[my - 1][mx] == 0:
        my = my - 1

    if key == 'Down' and maze[my + 1][mx] == 0:
        my = my + 1

    if key == 'Left' and maze[my][mx - 1] == 0:
        mx = mx - 1

    if key == 'Right' and maze[my][mx + 1] == 0:
        mx = mx + 1

    if key == 'Right' and maze[my][mx + 1] == 3:
        mx = mx + 1

    if maze[my][mx] == 0:
        maze[my][mx] = 2
        canvas.create_rectangle(mx * 80, my * 80, mx * 80 + 80, my * 80 + 80, fill='white', width=0)

    if maze[my][mx] == 3:
        tkinter.messagebox.showinfo('', '미로 탈출!')
      
    canvas.delete('olaf')
    canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag='olaf')
    window.after(95, main_proc)
    
 
    
        
window = tkinter.Tk()
window.title('올라프의_미로찾기')
window.bind('<Key>', key_down)
window.bind('<KeyRelease>', key_up)
canvas = tkinter.Canvas(width=880, height=640, bg='black')
canvas.pack()

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [4, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 3],
    [1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]



for y in range(8):
    for x in range(11):
        if maze[y][x] == 1:
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 80, y * 80 + 80, fill='skyblue')

        if maze[y][x] == 3:
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 80, y * 80 + 80, fill='blue')

        if maze[y][x] == 4:
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 80, y * 80 + 80, fill='indigo')
    
img = (Image.open("olaf.png"))
resized_image = img.resize((80,80), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized_image)
canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag='olaf')

                  

main_proc()
window.mainloop()



