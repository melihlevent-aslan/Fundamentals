# Fundamentals: The Search-Free Manifesto

This repository is a dedicated training ground for mastering the core syntax and logic of the languages essential for **Geodetic Engineering, MSR, and Data Management**. 

**The Goal:** Write every line of code without opening a search engine. 
**The Rule:** If I don't know the syntax, I must struggle with the compiler/interpreter until I remember or logically deduce it. No StackOverflow, no documentation—just logic.

---

## Python: The Data Scientist’s Swiss Army Knife
**Focus:** Data structures, Math logic, and File I/O.

### Project: Ellipsoidal Distance Calculator
Create a script that reads a `.csv` file containing Point IDs and their Geographic Coordinates (Lat, Lon) and outputs the 2D Euclidean or Great-Circle distance between consecutive points.

* **Core Concepts:** `math` module, `csv` library, List comprehensions, Functions.
* **Geodetic Twist:** Implement the **Haversine formula** or a basic 7-parameter transformation logic.
* **Success Metric:** Run the script and verify the distances match a manual calculation.

---

## JavaScript (HTML/CSS): The Digital Twin Interface
**Focus:** DOM manipulation and UI/UX for spatial data.

### Project: Live Coordinate Dashboard
Build a single-page web app where a user clicks on a "Map Area" (a styled `div`) and the site displays the pixel coordinates relative to the container in real-time. Include a "Save Point" button that logs coordinates to a list below.

* **Core Concepts:** Event Listeners (`click`, `mousemove`), Template Literals, CSS Flexbox/Grid.
* **Geodetic Twist:** Add a toggle to "transform" these pixel coordinates into a mock local grid system (e.g., $X = pixel * scale + offset$).

---

## C++: The Engine of SLAM & Robotics
**Focus:** Memory management, Pointers, and Performance.

### Project: Point Cloud Bounding Box Filter (CLI)
Write a command-line tool that takes a simulated stream (or array) of $(x, y, z)$ coordinates and filters out any points that fall outside a specific "Bounding Box" volume defined by the user.

* **Core Concepts:** `std::vector`, Structs, File Streams (`fstream`), Pointers.
* **Geodetic Twist:** This is the precursor to your **MSR-02 (SLAM)** and **Digital Twin** work. Focus on processing speed.

---

## JAVA: The Backbone of Land Management (ALKIS)
**Focus:** Object-Oriented Programming (OOP) and Type Safety.

### Project: Cadastral Object Manager
Design a system to manage "Parcels" of land. Create a base class `GeographicObject` and inherited classes like `Parcel`, `Building`, and `BoundaryLine`. Each should have methods to calculate "Tax Value" based on area and usage.

* **Core Concepts:** Encapsulation (Private/Public), Inheritance, Interfaces, HashMaps.
* **Geodetic Twist:** Mirror the logic of **ALKIS (Official Real Estate Cadastre Information System)**. Essential for your 2032 ÖbVI goal.

---

## Field-Specific Requirements

To bridge the gap between "Coder" and "Engineer," these fundamentals must be mastered:

| Skill | Why it's needed | Recommended Language |
| :--- | :--- | :--- |
| **Matrix Algebra** | Least Squares Adjustment | Python (NumPy logic) / C++ |
| **SQL / PostGIS** | Managing Cadastral Databases | PostgreSQL |
| **ROS2 Basics** | Sensor Fusion (Lidar/GNSS) | C++ / Python |
| **Regex** | Parsing raw NMEA strings | Python |

---

## Execution Strategy

1.  **Phase 1 (Pseudocode):** Define the logic on paper/whiteboard first.
2.  **Phase 2 (Dark Mode):** Code the logic with **zero** internet tabs open.
3.  **Phase 3 (Debugging):** Use compiler error messages as your only guide.
4.  **Phase 4 (Refactor):** Only after the code works, check documentation to see "The Pro Way" and optimize.

> "Health in mind, health in body." — *Mustafa Kemal Atatürk*

---
© 2026 | Geodetic Engineering Student | University of Bonn
