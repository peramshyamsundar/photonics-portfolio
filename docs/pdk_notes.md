# PDK notes - gdsfactory generic PDK(nov 2026 )

A pdk is process design kit, where in chip design a PDK is set of files,models, and rules provided by a foundary so designers can design ICs(integrated circuits)for a specific manufacturing process

for gdsfactory genric pdk 
1. **Layer stack ** : Si core 0.22µm on a 3µm SiO₂ BOX; rib slab = 220 nm − etch depth
2. Cross-sections: strip, rib, nitride, gsg (RF)
3. Cells: grating_coupler_te, mmi1x2, ring_single, mzm
4. Design rules: not in the generic PDK (only a 1 nm grid); real foundries ship a DRC deck
5. Models: empty in the generic PDK; foundries provide S-parameter models