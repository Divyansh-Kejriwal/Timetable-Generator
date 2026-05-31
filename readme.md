# Timetable Generator

## Overview

Timetable Generator is a Python-based project that automatically generates school timetables for multiple sections while satisfying scheduling constraints.

The project was developed to reduce the manual effort required in timetable creation and to demonstrate the use of algorithms, data structures, and constraint handling.

## Features Implemented

* Multi-section timetable generation
* Randomized subject allocation
* Teacher assignment based on subject
* Teacher conflict detection
* Teacher conflict resolution
* HTML timetable generation
* Modular code structure using functions

## Project Structure

Timetable-Generator/

├── core/

│ ├── generator.py

│ ├── constraints.py

│ └── html_generator.py

├── data/

│ └── sample_data.json

├── output/

│ └── timetable.html

├── README.md

└── requirements.txt

## Constraints Implemented

1. A subject cannot appear more than the specified limit per day.
2. A teacher cannot teach multiple sections during the same period.
3. Each section receives a complete timetable.

## Future Improvements

* Weekly subject quotas
* Teacher-wise timetable generation
* Class teacher constraints
* Teacher workload balancing
* Fixed periods
* Lab and activity periods
* Database integration
* Web interface

## Technologies Used

* Python
* JSON
* HTML
* Git & GitHub

## Author

Divyansh Kejriwal
