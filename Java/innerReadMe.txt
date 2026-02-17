AVA: Cadastral Object Manager
This project trains strict Object-Oriented principles, mimicking the hierarchical structure of an official real estate cadastre system.

Step 1: The Base Class: Create an abstract class named GeographicObject. Give it private fields like objectID and area, along with standard getter and setter methods. Define an abstract method calculateTax().

Step 2: Derived Classes: Create two new classes, Parcel and Building, that extend GeographicObject.

Step 3: Specific Implementations: Add unique properties to the derived classes (e.g., zoningType for Parcel, numberOfFloors for Building). Implement the calculateTax() method in both classes, using different math for each (e.g., Building tax might multiply area by floors).

Step 4: The Registry Setup: In your main application file, initialize a HashMap where the key is the objectID (String) and the value is a GeographicObject.

Step 5: Instantiation: Create several instances of Parcels and Buildings and put them into your HashMap.

Step 6: Polymorphic Execution: Iterate over the values in your HashMap. Call .calculateTax() on every object. The system should automatically apply the correct math based on whether it is a Parcel or a Building.