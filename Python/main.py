# Ellipsoidal / Haversine Distance Calculator
# Step 2: File I/O and String Parsing

def main():
    print("Distance Calculator Initialized.")
    print("--------------------------------")
    
    # Store our parsed points
    parsed_points = []
    
    # Open and read the data
    try:
        with open("points.csv", "r") as file:
            # Read all lines
            lines = file.readlines()
            
            # Loop through lines, skipping the first one (header)
            for line in lines[1:]:
                # Clean up the line and split by comma
                clean_line = line.strip()
                if clean_line:  # Make sure it's not an empty line
                    parts = clean_line.split(",")
                    
                    point_id = parts[0]
                    lat = float(parts[1])
                    lon = float(parts[2])
                    
                    # Save as a dictionary for easy access later
                    parsed_points.append({
                        "id": point_id,
                        "lat": lat,
                        "lon": lon
                    })
                    
        print(f"Successfully loaded {len(parsed_points)} points.")
        print(parsed_points[0]) # Print the first point to verify
        
    except FileNotFoundError:
        print("Error: points.csv not found. Make sure it is in the same folder.")

if __name__ == "__main__":
    main()