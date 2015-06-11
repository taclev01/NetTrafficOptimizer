from visual import *

#change the "forward" direction of the camera so as to see the whole scene
scene.forward=(0,-4,-10)

#create user distance between lights; zero seems to work best for aesthetics
light_displacement = 0


#create stoplight composite object using a frame
#can now refer to stoplight object
#NOTE: length = x, width = z, and height = y
stoplight = frame()
casing = box(frame = stoplight, pos=vector(0,0,0), length=1, width=0.5, height=3, color=color.white)
yellowbulb = sphere(frame=stoplight, pos=vector(0,0,0), radius=0.5, color=color.yellow)
greenbulb = sphere(frame=stoplight, pos=vector(0,yellowbulb.pos.y-(2*yellowbulb.radius+light_displacement),0), radius=0.5, color=color.green)
redbulb = sphere(frame=stoplight, pos=vector(0,yellowbulb.pos.y+(2*yellowbulb.radius+light_displacement),0), radius=0.5, color=color.red)

#change position of entire "frame"/stoplight
stoplight.pos=vector(2.5,8,0)

#use visible attribute to make lights "on" or "off"
##redbulb.visible=false will turn the red light off

#############################
#############################
road = frame()
pavement = box(frame = road, pos=vector(0,0,0), length = 10, width=25, height = 0.25, color=(0.5,0.5,0.5))

##  create stripes in z direction using a list
#create an empty array to hold stripe objects
zstripe_list=[]
#create a list of z coordinates to use as positions
#creates 5 stripes centered at z=0
# range( start, stop, step) ;  step is optional and defaults to 1
#zstripe_zlist = range(-10,10,5)
zstripe_zlist = [-10,-5,0,5,10]
zstripe_pos_list=[]

#create list of positions to use for creating stripes in z direction
for z in zstripe_zlist:
    zstripe_pos_list.append(vector(0,0,z))


#create the stripes as objects in the zstripe_list
for position in zstripe_pos_list:
    zstripe_list.append( box(frame=road, pos=position, length=0.5, width=2.5, height=0.3, color=color.yellow))

