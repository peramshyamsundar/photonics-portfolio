# Question : how many GCs and How many µm apart?
# predictions: 2 GCs and 127µm apart
import gdsfactory as gf  # importing gdsfactory library
gf.gpdk.PDK.activate()  # activating generic PDK
#    pdk = gf.active_pdk()  # get active PDK
# creating a straight waveguide with length of 500 micrometers
wg = gf.components.straight(length=500)
# getting help for the add_fiber_array function
# help(gf.routing.add_fiber_array)
# adding a fiber array to the waveguide component
c = gf.routing.add_fiber_array(component=wg)
c.write_gds("gds/step7_loopback.gds")  # writing the component to a GDS file
c.pprint_ports()  # printing the ports of the component
c.show()  # displaying the component in KLayout viewer
# result : 4 GCs (2 device + 2 alignment loopbacks)
# distance between GCs : 127µm apart(59.5 to 186.5µm,186.5 to 313.5µm,313.5 to 440.5µm)
