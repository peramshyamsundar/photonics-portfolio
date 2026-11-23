# photonics-portfolio
Silicon photonics PIC design portfolio: gdsfactory layouts, simulations, notes

## Step 5: Parametric MZI (gdsfactory)
- `my_mzi(delta_length)` — parametric cell built on gdsfactory's generic PDK MZI
- Variants: ΔL = 10 µm and 100 µm → `gds/step5_mzi.gds`
- FSR = λ²/(n_g·ΔL), λ = 1550 nm, n_g ≈ 4.2:
  | ΔL (µm) | FSR (nm) |
  |---|---|
  | 10 | 57.2 |
  | 100 | 5.7 |
- Note: longer ΔL → narrower FSR. Spacing between variants increased to avoid evanescent coupling.