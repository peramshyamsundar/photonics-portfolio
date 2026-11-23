# on a real chip, you cannot draw every components connect them trough by hand you place them and connect through ports. This is called routing. In this step we will learn how to route components using gdsfactory.
import gdsfactory as gf  # importing gdsfactory library
gf.gpdk.PDK.activate()  # activating generic PDK
c = gf.Component("route_demo")  # creating a component for routing demo
# creating a straight waveguide with length of 20 micrometers
wg = gf.components.straight(length=20)
ref1 = c << wg  # adding the first waveguide to the component
ref2 = c << wg  # adding the second waveguide to the component
# moving the second waveguide to the right of the first waveguide so that they don't overlap
ref2.move((60, 40))
# now we add ports to the waveguides so that we can connect them through routing
# routing the waveguides through their ports using the route_single function. The cross_section parameter specifies the type of waveguide to use for routing.
route = gf.routing.route_single(
    c, ref1.ports["o2"], ref2.ports["o1"], cross_section="strip")
print("Route Length:", route.length)  # printing the length of the route
c.write("gds/step4_route.gds")  # writing the component to a GDS file
