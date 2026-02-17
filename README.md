# Fundamentals: The Search-Free Manifesto

This repository is a dedicated training ground for mastering the core syntax and logic of the languages essential for Geodetic Engineering, Mobile Sensing and Robotics (MSR), and Data Management.

**The Goal:** Write every line of code without opening a search engine. 
**The Rule:** If I don't know the syntax, I must struggle with the compiler/interpreter until I remember or logically deduce it.

---

## Python: The Data Scientist's Swiss Army Knife
**Focus:** Data structures, File I/O, and Geodetic transformations.

### Project: Ellipsoidal Distance Calculator
Create a script that reads a `.csv` file containing Point IDs and their Geographic Coordinates (Lat, Lon) and outputs the 2D Euclidean or Great-Circle distance between consecutive points.

* **Core Concepts:** `math` module, `csv` library, List comprehensions, Functions.
* **Geodetic Twist:** Implement a simplified version of the Haversine formula or a 7-parameter transformation logic.

---

## JavaScript (HTML/CSS): The Digital Twin Interface
**Focus:** DOM manipulation, Asynchronous events, and UI/UX for spatial data.

### Project: Live Coordinate Dashboard
Build a single-page web app that allows a user to click on a "Map Area" (a styled `div`) and displays the pixel coordinates relative to the container in real-time. Include a "Save Point" button that logs coordinates to a list.
* **Core Concepts:** Event Listeners (`click`, `mousemove`), Template Literals, CSS Flexbox/Grid.
* **Geodetic Twist:** Add a toggle to "transform" these pixel coordinates into a mock local grid system (e.g., $X = pixel \cdot scale + offset$).

---

## C++: The Engine of SLAM & Robotics
**Focus:** Memory management, Pointers, and Performance.

### Project: Point Cloud Filter (CLI)
Write a command-line tool that takes a simulated stream of $(x, y, z)$ coordinates and filters out any points that fall outside a specific "Bounding Box" volume.
* **Core Concepts:** `std::vector`, Structs/Classes, File Streams (`fstream`), Pointers for memory efficiency.
* **Geodetic Twist:** This is the precursor to MSR and Digital Twin work. Focus on processing speed.

---

## JAVA: The Backbone of Land Management
**Focus:** Object-Oriented Programming (OOP), Inheritance, and Type Safety.

### Project: Cadastral Object Manager
Design a system to manage "Parcels" of land. Create a base class `GeographicObject` and inherited classes like `Parcel`, `Building`, and `BoundaryLine`. Each should have methods to calculate "Tax Value" based on area.
* **Core Concepts:** Encapsulation (Private/Public), Inheritance, Interfaces, HashMaps.
* **Geodetic Twist:** Mirror the logic of official real estate cadastre information systems (like ALKIS) for land management.

---

## SQL: The Core of Spatial Databases
**Focus:** Relational schemas, Queries, Joins, and Aggregations.

### Project: Property Registry Setup
Write the raw SQL scripts to initialize a relational database containing tables for `Owners`, `Parcels`, and `Coordinates`. Write queries to find all parcels owned by a specific person and calculate the total area they own.
* **Core Concepts:** `CREATE TABLE`, `Primary/Foreign Keys`, `INNER JOIN`, `GROUP BY`.
* **Geodetic Twist:** Store coordinate bounds and use basic SQL math to estimate parcel area before moving to true PostGIS extensions.

---

## Data Management: The ETL Pipeline
**Focus:** Extract, Transform, Load (ETL) principles, Data Cleaning, and Integrity.

### Project: GNSS Sensor Data Pipeline
Create a script (in Python or C++) that ingests a messy, raw text file of simulated NMEA sentences from a GNSS receiver. The script must parse the strings, filter out lines with low satellite counts, format the valid timestamps and coordinates, and load them directly into your SQL database.
* **Core Concepts:** String parsing, Regex (Regular Expressions), Error handling (try/catch), Database connection execution.
* **Geodetic Twist:** Handling real-world sensor noise and transforming it into structured, queryable data for analysis.

---

## Execution Strategy
1. **Phase 1:** Identify the logic (Pseudocode).
2. **Phase 2:** Code the logic (No Internet).
3. **Phase 3:** Debug via error messages only.
4. **Phase 4:** Only after completion, check documentation to see how to optimize.

> "Health in mind, health in body." — Mustafa Kemal Atatürk

---
Melih Levent Aslan | M.Sc. Geodetic Engineering Student, University of Bonn
