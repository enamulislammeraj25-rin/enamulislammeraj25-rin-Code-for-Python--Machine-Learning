# 1. VARIABLES (Sticky notes for basic project facts)
water_table_m = 3.0
water_weight = 9.81

# 2. DICTIONARIES (Labeled filing cabinets for our soil layers)
layer_1 = {
    "name": "Dry Sand", 
    "bottom_depth": 3.0, 
    "unit_weight": 17.0
}

layer_2 = {
    "name": "Wet Clay", 
    "bottom_depth": 6.0, 
    "unit_weight": 19.0
}

# 3. LIST (A single column of depths we want to test)
depths_to_check = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

print("--- STARTING BOREHOLE ANALYSIS ---")

# 4. FOR LOOP (The assembly line worker starts moving down the list of depths)
for z in depths_to_check:
    
    # 5. IF/ELSE (Flowchart to decide which soil layer we are currently in)
    if z <= layer_1["bottom_depth"]:
        # If depth 'z' is 3 meters or less, we are in Layer 1
        current_soil = layer_1["name"]
        total_stress = z * layer_1["unit_weight"]
        
    else:
        # Otherwise, we have crossed into Layer 2
        current_soil = layer_2["name"]
        
        # Calculate stress from the full sand layer above
        stress_from_sand = layer_1["bottom_depth"] * layer_1["unit_weight"]
        
        # Calculate stress from just the part of the clay we are standing in
        depth_into_clay = z - layer_1["bottom_depth"]
        stress_from_clay = depth_into_clay * layer_2["unit_weight"]
        
        # Add them together
        total_stress = stress_from_sand + stress_from_clay

    # IF/ELSE (Flowchart to check for water pressure)
    if z <= water_table_m:
        # Above the water table, pressure is zero
        water_pressure = 0.0
    else:
        # Below the water table, calculate the water weight
        depth_under_water = z - water_table_m
        water_pressure = depth_under_water * water_weight
        
    # Final Math
    effective_stress = total_stress - water_pressure
    
    # Print the final answer for this specific depth
    # (The 'round' command just cuts off long decimals so it looks neat)
    print("Depth:", z, "m | Soil:", current_soil, "| Effective Stress:", round(effective_stress, 1), "kPa")

print("--- FINISHED ---")