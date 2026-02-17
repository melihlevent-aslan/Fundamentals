Python: Ellipsoidal Distance Calculator
This project builds data parsing and mathematical implementation skills.

Step 1: Construct the Mock Data: Create a simple text file (.csv) manually. Format it with headers: PointID, Latitude, Longitude. Add 5 to 10 rows of realistic coordinate data.

Step 2: File I/O setup: Write a Python script to open this file. Read the contents line by line, skipping the header.
Step 3: String Parsing: Split each line by the comma delimiter. Convert the extracted Latitude and Longitude strings into floating-point numbers.

Step 4: The Math Engine: Define a function that takes two sets of coordinates. Implement the Haversine formula inside this function to calculate the great-circle distance.

Step 5: Iteration and Calculation: Store your parsed points in a list of dictionaries or tuples. Loop through the list, taking Point A and Point B, then Point B and Point C, passing them into your math function.
Step 6: Output: Print the resulting distances to the console cleanly (e.g., "Distance 1-2: 45.2 km"), or write them to a new output file.