from __future__ import division
from visual import *


##  length units are to be in feet for ease of use in the USA ('Merica!)


##  set camera so that we are looking down onto streets
scene.forward = vector(0,-1,0)

##  set a global dictionary to associate direction names with vectors
##  to access them use directions['north'], directions['south'], etc.
directions = {'north':vector(0,0,-1), 'south':vector(0,0,1), 'east':vector(1,0,0), 'west':vector(-1,0,0)}

##  create a north, south, east, and west compass on map for ease of use
##  NOTE: North is -z, South is +z, East is +x, and West is -x
comp_scale = 4
north_vec = arrow(pos=comp_scale*vector(10,0,10), axis=comp_scale*vector(0,0,-5), color=color.red)
north_text = text(text="North (-z)", pos = north_vec.pos+north_vec.axis, height=1*comp_scale, color=north_vec.color, up=vector(0,0,-1))
south_vec = arrow(pos=north_vec.pos, axis=comp_scale*vector(0,0,5), color=color.white)
south_text = text(text="South (+z)", pos = south_vec.pos+south_vec.axis + vector(0,0,1), height=1*comp_scale, color=south_vec.color, up=vector(0,0,-1))
east_vec = arrow(pos=north_vec.pos, axis=comp_scale*vector(5,0,0), color=color.green)
east_text = text(text="East (-x)", pos = east_vec.pos+east_vec.axis+vector(0,0,-1), height=1*comp_scale, color=east_vec.color, up=vector(0,0,-1))
west_vec = arrow(pos=north_vec.pos, axis=comp_scale*vector(-5,0,0), color=color.blue)
west_text = text(text="West (+x)", pos = west_vec.pos+west_vec.axis+vector(0,0,-1), height=1*comp_scale, color=west_vec.color, up=vector(0,0,-1))

##  create a stoplight class that has member functions to change the color, change the position, etc.
class Stoplight():
    def __init__(self):
        self.base = frame(pos=vector(0,10,0))
        #   NOTE:::  All positions of objects witihin the frame are RELATIVE to the frame's position, not the world position
        case=box(frame=self.base,pos=vector(0,0,0), length=1, width=0.25,height=2, color=color.white)
        self.yellow=sphere(frame=self.base,pos=vector(case.pos.x, case.pos.y, case.pos.z+(case.width/2)), radius=0.25, color=color.yellow)
        self.green=sphere(frame=self.base,pos=vector(case.pos.x, case.pos.y-(2*self.yellow.radius+0.17), case.pos.z+(case.width/2)), radius=0.25, color=color.green)
        self.red=sphere(frame=self.base,pos=vector(case.pos.x, case.pos.y+(2*self.yellow.radius+0.17), case.pos.z+(case.width/2)), radius=0.25, color=color.red)

    def move(self, new_position):
        self.base.pos=new_position

    def green_light(self):
        self.red.visible=false
        self.yellow.visible=false
        self.green.visible=true

    def yellow_light(self):
        self.red.visible=false
        self.yellow.visible=true
        self.green.visible=false

    def red_light(self):
        self.red.visible=true
        self.yellow.visible=false
        self.green.visible=false

        

        
class Road():
    def __init__(self, distance, direction):
        self.base=frame(pos=vector(0,0,0), up=vector(0,1,0), axis=direction)
        self.pave = box(frame=self.base,pos=vector(0,0,0), length=distance, width = 24, height=0.25, color=(0.5,0.5,0.5), axis=vector(1,0,0)) #axis here points along axis of frame
        #lane stripes are 10 feet long and 30 feet spacing between them  (not sure about spacing...)
        stripe_length=10
        stripe_width=1
        stripe_spacing=30
        stripe_list=[]
        stripe_pos_list=[]
        stripe_zpos_list=range(int(-self.pave.length/2),int(self.pave.length/2+stripe_spacing),stripe_spacing)
        for z in stripe_zpos_list:
            stripe_pos_list.append(vector(z,0,0))
        for position in stripe_pos_list:
            stripe_list.append( box( frame=self.base, pos = position, length=stripe_length, width=stripe_width, height=0.3, color=color.yellow, axis=self.pave.axis))

    def change_dir(self, new_dir):
        self.base.axis=new_dir

    def move(self, new_pos):
        self.base.pos = new_pos

class Car():
    def __init__(self, first_pos, v_direction):
        self.body = box(pos=first_pos, length=16, width = 6, height = 5, color = color.cyan, axis = v_direction)
        ##  create velocity vector by using mag * dir
        self.v_mag = 37 # feet/second   ==  25 mph ;  rough speed of standard car
        self.v_hat = v_direction
        self.v = self.v_mag*self.v_hat

    def stopping(self, light):
        dist_to_light = light.self.pos - self.body.pos

    def move(self, delta_position):
        self.body.pos = self.body.pos + delta_position
        


new_light = Stoplight()
new_road = Road(int(5280/25), directions['north'])
key=scene.kb.getkey()
#big.axis=vector(0,1,0)
new_light.move(vector(10,10,0))
new_road.change_dir(vector(1,0,0))
key=scene.kb.getkey()
new_road.move(10*directions['north'])
key=scene.kb.getkey()
new_light.green_light()
key=scene.kb.getkey()
new_light.yellow_light()
key=scene.kb.getkey()
new_light.red_light()
key=scene.kb.getkey()
newer_road = Road(int(5280/25), directions['north'])

new_car = Car(vector(6,0,100), directions['north'])
car2 = Car(vector(100, 0, -16), directions['west'])

t=0
delta_t = 1/60
simtime = 5  #seconds

while t < simtime:
    rate(60)
    deltaR1 = new_car.v*delta_t
    deltaR2 = car2.v*delta_t
    new_car.move(deltaR1)
    car2.move(deltaR2)
    t = t + delta_t

