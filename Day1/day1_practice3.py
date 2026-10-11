field_density=[18.2, 19.1, 17.5, 19.8, 18.9]
maxdry_density=19.5
for fd in field_density:
    percentage_compaction=round((fd/maxdry_density)*100,2)
    if percentage_compaction<95:
        print("Percentage compaction is",percentage_compaction,"% --->>> FAIL")
    else:
        print("Percentage compaction is",percentage_compaction,"% --->>> PASS")
