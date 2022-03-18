
import cv2
import numpy as np
import threading
import colorsys
from queue import PriorityQueue
import queue
import time
import math


easy_maze = "C:\Python\WORTHY PROJECTS\maze_game\simple_maze.jpg"
hard_maze = "C:\Python\WORTHY PROJECTS\maze_game\Printable-Mazes-for-Adults.png"
imp_maze = "C:\Python\WORTHY PROJECTS\maze_game\imp_maze.jpg"
loop_maze = "C:\Python\WORTHY PROJECTS\maze_game\loop_maze.jpg"
pin_maze = "C:\Python\WORTHY PROJECTS\maze_game\pin_maze.jpg"
small_maze = "C:\Python\WORTHY PROJECTS\maze_game\small_maze.jpg"
diff_maze = "C:\Python\WORTHY PROJECTS\maze_game\diff_maze.jpg"


flag = 0    

class Point:

    counter = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.counter += 1

    def __add__(self, other): #  operator overloading
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    
    def __neg__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)
        

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else: return False
    
    def __lt__(self, other):
        return self.counter < other.counter
    


def h_score(curr_node, goal): #  
    result = abs(goal.x-curr_node.x)**2 + abs(goal.y-curr_node.y)**2
    return math.sqrt(result)

def g_score(s, c): #distance current node to start node
    result = abs(s.x-c.x)**2 + abs(s.y-c.y)**2
    return math.sqrt(result)
    



def A_STAR(start, goal): # where start and goal are of class Point
    global img, h, w
  
    found = False
    const = 10000

    Neighbors = [Point(0,1), Point(-1,0), Point(0,-1), Point(1,0)]   
    
    
    
    CLSD = [[0 for j in range(w)] for i in range(h)]              


    OPEN = PriorityQueue()
    parent = [[Point() for j in range(w)] for i in range(h)]
    
    OPEN.put((h_score(start,goal),h_score(start,goal), start)) # (f(n), g(n), node)
    
    
    
    while not OPEN.empty():
        
        node = OPEN.get()[2]
       
        
        if node == goal:
            found = True
            break

        else:

            for n in Neighbors:

                child = Point(0,0) 
                child = n + node                
                    
                h_child = h_score(child, goal)
                g_child = g_score(start, child)              
                f_child = g_child + h_child
                
                h_curr = h_score(node, goal)
                g_curr = g_score(start, node)   
                f_curr = g_curr + h_curr    
                
                cost = g_curr + h_child    

                     
                    
                if(child.x>=0 and child.x<w and child.y>=0 and child.y<h and CLSD[child.y][child.x]==0 and
                (img[child.y][child.x][0]!=0 or img[child.y][child.x][1]!=0 or img[child.y][child.x][2]!=0)):

                    CLSD[child.y][child.x] = CLSD[node.y][node.x]+1

                    if cost > f_child:
                        
                        OPEN.put((f_child, h_curr, child))
                        parent[child.y][child.x] = node
                        img[child.y][child.x]=list(reversed([i * 255 for i in colorsys.hsv_to_rgb(CLSD[child.y][child.x] / const, 1, 1)]))

                    if cost < f_child and (h_child<f_curr+1):
                        parent[child.y][child.x] = node
                        #CLSD[child.x][child.y] = 0  
                        OPEN.put((cost, h_child, child))

                        img[child.y][child.x]=list(reversed([i * 255 for i in colorsys.hsv_to_rgb(CLSD[child.y][child.x] / const, 1, 1)]))
               
                    

    path = []
    

    if found:
        p = goal
        while p != start:
            path.append(p)
            p = parent[p.y][p.x]
            
        path.append(p)
        path.reverse()

        for p in path:
            print(p.y, p.x)
            img[p.y][p.x] = [150, 150, 150]
        print("Path Found")
    else:
        print("Path Not Found")


def mouse_event(event, pX, pY, flags, param):
    global img, START, END, p, flag

    if event == cv2.EVENT_LBUTTONUP:
        if p == 0:
            cv2.rectangle(img, (pX-rw, pY-rw), (pX+rw, pY+rw),(0,0,255), -1)
            START = Point(pX, pY)
            print("START =", START.x,",", START.y)
            p+=1
        elif p == 1:
            cv2.rectangle(img, (pX-rw, pY-rw), (pX+rw, pY+rw),(0, 200, 50), -1)
            END = Point(pX, pY)
            print("END =", END.x,",",END.y)
            p+=1
    if event==cv2.EVENT_RBUTTONUP:
    	flag=1

def DISPLAY():
    global img
    
    cv2.imshow("Image", img)
    cv2.setMouseCallback('Image', mouse_event)
    run = True
    
    while run:
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        
        if cv2.waitKey(1) & 0xFF == 27:            
            
            break
    

rw = 2
p = 0


START = Point()
END = Point()


img =  cv2.imread(small_maze, cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (700,700),interpolation = cv2.INTER_AREA)
_ , img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
h, w = img.shape[:2]

t  = threading.Thread(target=DISPLAY, args=())
t.daemon = True
t.start()

while p < 2:
    pass





A_STAR(START, END)

cv2.waitKey(0)

