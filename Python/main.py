import math

# Ellipsoidal / Haversine Distance Calculator
# Step 4 & 5: The Math Engine and Iteration

def calculate_haversine(lat1, lon1, lat2, lon2):
    # Earth radius in kilometers
    R = 6371.0
    
    # Convert degrees to radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    # Haversine formula
    a = math.sin(delta_phi / 2.0)**2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2.0)**2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return distance

def main():
    print("Distance Calculator Initialized.")
    print("--------------------------------")
    
    parsed_points = []
    
    try:
        with open("points.csv", "r") as file:
            lines = file.readlines()
            for line in lines[1:]:
                clean_line = line.strip()
                if clean_line:
                    parts = clean_line.split(",")
                    parsed_points.append({
                        "id": parts[0],
                        "lat": float(parts[1]),
                        "lon": float(parts[2])
                    })
                    
        print(f"Successfully loaded {len(parsed_points)} points.\n")
        
        # Iteration: Calculate distance between sequential points
        print("--- Sequential Distances ---")
        for i in range(len(parsed_points) - 1):
            pt_a = parsed_points[i]
            pt_b = parsed_points[i+1]
            
            dist = calculate_haversine(pt_a["lat"], pt_a["lon"], pt_b["lat"], pt_b["lon"])
            
            print(f"Distance Point {pt_a['id']} to Point {pt_b['id']}: {dist:.3f} km")
            
    except FileNotFoundError:
        print("Error: points.csv not found.")

if __name__ == "__main__":
    main()