import gdsfactory as gf  # importing gdsfactory library
gf.gpdk.PDK.activate()  # activating generic PDK
# Waveguide length prediction: 50 micrometers,prediction:o1(0,0)180degree,o2(50,0)0degree,width = 0.5 micrometers(dont need to pridict)
c = gf.Component()  # creating a component
# creating a straight waveguide with length of 50 micrometers
wg = gf.components.straight(length=50)
c << wg  # adding the waveguide to the component
wg.pprint_ports()  # printing the ports of the waveguide
