💻 Real-Time CLI System Monitor

Overview

The Real-Time CLI System Monitor is a Python utility built to replicate the core functionality of system monitoring tools like Linux's top or Windows' Task Manager. It provides a constantly updated, command-line view of the system's overall resource utilization (CPU, Memory, Disk) and displays a list of the top processes, sortable by CPU or Memory usage.

This project demonstrates strong skills in:

System Programming: Interfacing with the Operating System kernel via the psutil library.

Tooling & CLI Design: Using argparse for a professional command-line interface with custom flags.

Real-Time Visualization: Implementing terminal control (os.system) and a continuous refresh loop.

Software Testing: Implementing unit tests using the unittest framework to validate core sorting and filtering logic.

Containerization (DevOps): Providing a Dockerfile and docker-compose.yml for isolated deployment.

🚀 Getting Started

Prerequisites

Python 3.x

Docker and Docker Compose (for the containerized deployment option).

Installation (Standard Python)

Clone the Repository:

git clone [YOUR_REPOSITORY_URL_HERE]
cd system-monitor-cli

Create and Activate Virtual Environment:

python -m venv venv

# On Windows: venv\Scripts\activate.bat

# On Linux/macOS: source venv/bin/activate

Install Dependencies:

pip install psutil

Usage

Run the monitor using the monitor.py script. The tool runs continuously until manually stopped with Ctrl + C.

Command Syntax

python monitor.py [-s {cpu,memory}] [-i INTERVAL]

Flag

Argument Name

Description

Default

-s, --sort

cpu or memory

The metric used to sort the displayed process list (highest first).

cpu

-i, --interval

float (seconds)

The refresh rate for the display.

1.0

Examples

Command

Description

python monitor.py

Default mode: Sort by CPU, refresh every 1 second.

python monitor.py --sort memory -i 0.5

Sort processes by memory usage, refreshing every half-second.

✅ Running Unit Tests

To confirm the process sorting logic is robust, run the following command:

python test_monitor.py

(Expected Output: OK)

🐳 Containerized Deployment (Recommended)

To run the application inside an isolated Docker container, use Docker Compose. This allows anyone to run your project without installing Python dependencies.

Build and Run the Container:

docker-compose up --build

Stop the Container:
Press Ctrl + C in the terminal where Docker is running.
