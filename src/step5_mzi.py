# creating a Mach-Zehnder Interferometer (MZI) using gdsfactory
import gdsfactory as gf  # importing gdsfactory library
gf.gpdk.PDK.activate()  # activating generic PDK


@gf.cell  # decorator to create a cell
def my_mzi(delta_length: float = 10.0) -> gf.Component:  # function to create a component
    c = gf.Component()  # creating a Mach-Zehnder Interferometer (MZI) using gdsfactory
    mzi = gf.components.mzi(delta_length=delta_length)
    ref1 = c << mzi  # adding the MZI to the component
    c.add_ports(ref1.ports)  # adding the ports of the MZI to the component
    return c  # returning the component


top = gf.Component("mzi_variants")  # creating a component for MZI variants

# MZI variant1 with delta_length of 10 micrometers
mzi_short = my_mzi(delta_length=10)  # creating a component for MZI variant1
ref_a = top << mzi_short  # MZI variant2 with delta_length of 10 micrometers
# MZI variant2 with delta_length of 100 micrometers
mzi_long = my_mzi(delta_length=100)
ref_b = top << mzi_long  # adding the MZI variant2 to the component
ref_b.move((0, 200))  # moving the MZI variant2 up so that they don't overlap
top.write_gds("gds/step5_mzi.gds")  # writing the component to a GDS file

# FSR hand calculation:
lam = 1.55e-6  # wavelength in m
n_g = 4.2         # group index,Si-strip waveguide
for dl_um in [10, 100]:
    fsr = lam**2 / (n_g*dl_um*1e-6)  # FSR in m
    fsr_nm = fsr * 1e9  # converting FSR to nm
    # printing the FSR in nm
    print(f"dl = {dl_um} um -> FSR = {fsr_nm:.1f} nm")
