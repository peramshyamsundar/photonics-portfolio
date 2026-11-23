# Euler or Circular bend? which has bigger footprint? Let's find out by creating both and printing their footprints.
import gdsfactory as gf  # importing gdsfactory library
gf.gpdk.PDK.activate()  # activating generic PDK
# creating a circular bend with radius of 10 micrometers
circ = gf.components.bend_circular(radius=10)
# creating an Euler bend with radius of 10 micrometers and p=0.5 p is the parameter that controls the shape of the Euler bend(smoothness)
euler = gf.components.bend_euler(radius=10, p=0.5)
print("Circular bend ports:")
circ.pprint_ports()  # printing the ports of the circular bends
print("Euler bend ports:")
euler.pprint_ports()  # printing the ports of the Euler bends

# now measuring footprint
# printing the bounding box of the circular bend
print("circular bbox:", circ.dbbox())
# printing the bounding box of the euler bend
print("euler bbox:", euler.dbbox())
c = gf.Component()  # creating a component
ref1 = c << circ  # adding the circular bend to the component
ref2 = c << euler  # adding the euler bend to the component
# moving the euler bend to the right of circular bend so that they don't overlap
ref2.move((30, 0))
# writing the component to a GDS file
c.write_gds("gds/step3_bends.gds")
