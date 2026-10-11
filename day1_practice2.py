blow_count=[11, 48, 15, 38, 18, 62]
for bc in blow_count:
    if bc < 30:
        print("Blow count is in between 0 and 29. Normal Driving")
    elif bc >=30 and bc<50:
        print("Blow count is in between 30 and 49.Hard Driving. Prepare to stop")
    else:
        print("Blow count is greater than or equal to 50. Refusal reached, stop the hammer")