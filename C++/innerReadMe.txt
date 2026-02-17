C++: Point Cloud Filter (CLI)
This is foundational for processing heavy spatial data and preparing for SLAM algorithms. Performance and memory management are key.

Step 1: Data Structures: Define a struct or class named Point3D containing three float or double variables (x, y, z).

Step 2: Input Simulation: Write a function that generates a std::vector of Point3D objects with randomized coordinates, or read them in from a simple text file using std::ifstream.

Step 3: Define Constraints: Create variables defining a 3D bounding box: min_x, max_x, min_y, max_y, min_z, max_z.

Step 4: The Filter Logic: Iterate through your vector of points. For each point, write the conditional logic to check if its x, y, and $z$ values fall strictly within the bounds defined in Step 3.

Step 5: Memory Handling: If a point passes the filter, add it to a new std::vector of "Filtered Points". If you used pointers for dynamic allocation, ensure you are cleaning up memory for the points you discard.

Step 6: Output: Print the total count of original points versus the count of retained points to verify your logic worked.