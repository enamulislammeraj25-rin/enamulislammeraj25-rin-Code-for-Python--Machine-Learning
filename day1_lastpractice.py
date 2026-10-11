"""
The Scenario:
You are preparing a dataset for a Machine Learning model that predicts Earthquake Liquefaction.
For a soil layer to liquefy during an earthquake, three conditions must ALL be true at the same time:

The soil must be below the water table.

The soil type must be either "Sand" or "Silty Sand". (Clays and Gravels do not liquefy).

The SPT blow count must be loose (less than 20).

Sometimes, the field crew makes a mistake or a sensor breaks, and they write down "-999" for the blow count. This is corrupted data. You cannot let an ML model see corrupted data.

The Raw Data:
The groundwater table for this site is at 3.0 meters deep.

Here is the raw data from the drill rig, provided as a list of dictionaries. Each dictionary is one soil layer:

[
{"layer_id": "L1", "depth": 1.5, "soil_type": "Sand", "blows": 12},
{"layer_id": "L2", "depth": 3.5, "soil_type": "Clay", "blows": 8},
{"layer_id": "L3", "depth": 4.5, "soil_type": "Sand", "blows": 15},
{"layer_id": "L4", "depth": 6.0, "soil_type": "Sand", "blows": 25},
{"layer_id": "L5", "depth": 7.5, "soil_type": "Silty Sand", "blows": -999},
{"layer_id": "L6", "depth": 9.0, "soil_type": "Silty Sand", "blows": 18}
]

The Logic Requirements:

Loop through the list of layers.

First, check if the blow count is exactly -999. If it is, this data is corrupted. Print an error message and do NOT process it further.

If the data is good, check if the layer meets ALL THREE liquefaction rules.
(Hint: You can use the word 'and' to check multiple rules at once, and the word 'or' if it can be one thing or another. Use parentheses to group them nicely if needed).

If it meets all rules, it is a Liquefaction Hazard. If it fails even one rule, it is Safe.

The Output Requirement:
For every layer, print a clear log.
If it is corrupted, print: "Layer [id] -> CORRUPTED DATA. SKIPPING."
If it is a hazard, print: "Layer [id] -> DANGER: Liquefaction Risk!"
If it is safe, print: "Layer [id] -> SAFE."
"""

