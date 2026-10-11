"""
-------------------------------------------------------PRACTICE PROBLEM---------------------------------------------------
Write a Python script using the 5 basic tools. Follow these steps exactly:

The Dictionary:
Create a dictionary named project_info. Inside it, store two labels:
"Project_Name": "River Bridge"
"Borehole_ID": "BH-04"

The List:
Create a list named blow_counts that holds these 5 numbers: [4, 15, 25, 8, 32]

The For Loop:
Write a for loop that tells the computer to look at every single number in your blow_counts list, one by one.

The If/Else Flowchart:
Inside your for loop, write an if/elif/else flowchart with these rules:

If the blow count is less than 10, print: "Danger: Soft soil found!"

Else If (elif) the blow count is between 10 and 30, print: "Good: Medium soil."

Else (which covers anything higher), print: "Excellent: Hard soil."

"""



project_info={
    "Project_Name": "River Bridge",
    "Borehole_ID": "BH-04"
}

blow_counts=[4,15,25,8,32]

for z in blow_counts:
    if z<10:
        print("Danger: Soft soil")
    elif(z>=10 and z<=30):
        print("Good: Medium soil")
    else:
        print("Excellent: Hard soil")

