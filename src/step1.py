import gdsfactory as gf  # importing gdsfactory module
gf.gpdk.PDK.activate()  # activate the generic PDK
# prediction : length = 50 micrometers
c = gf.Component()  # creating a component
# adding a straight waveguide to the component with specified length
wg = gf.components.straight(length=50)  # making wg with 50 micrometers
c << wg  # adding waveguide to the component
c.write_gds("step1.gds")  # writing the component to a GDS file
