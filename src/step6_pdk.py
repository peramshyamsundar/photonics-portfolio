# predicting will i find a grading coupler among cells? i think no
import gdsfactory as gf  # importing gdsfactory library
gf.gpdk.PDK.activate()  # activating generic PDK
pdk = gf.get_active_pdk()  # get active PDK
for name, level in pdk.layer_stack.layers.items():  # iterating the levels of the PDK
    # printing the name, thickness, and material of each level in the PDK
    print(name, level.thickness, level.material)
#  print(pdk)  # printing the PDK information
print(pdk.layers)  # printing the layers of the PDK
# printing the cross sections of the PDK
print(list(pdk.cross_sections.keys()))
print(list(pdk.cells.keys())[:20])  # printing the first 20 cells of the PDK
