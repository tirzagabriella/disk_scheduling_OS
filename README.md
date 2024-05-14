# Disk Scheduling Project

## Introduction

This project simulates disk scheduling techniques. Disk scheduling is a strategy used in operating systems to schedule I/O requests that arrive on the disk. Disk scheduling is critical for improving the overall performance of the system.

## Algorithms Implemented

- FCFS (First Come, First Serve): Requests are handled in the order they are received in the disk queue.
- SCAN (Elevator Algorithm): Moves to one end of the disk, then reverses direction to handle the remaining requests.
- C-SCAN (Circular SCAN) is similar to SCAN, except when it reaches the end of the disk, it quickly returns to the beginning.

## File Structure

- disk_scheduling.py: Contains the logic for implementing the disk scheduling algorithms.
- generate_requests.py: Script to generate a set of random disk requests and saves them to requests.txt.
- requests.txt: Stores disk requests. Each request is a number that represents a position on the disk.

## How to Run the Program

- Generate Disk Requests: Run the generate_requests.py to create random disk requests. You can adjust parameters to generate different sets of requests. (python generate_requests.py)
- Run Disk Scheduling Simulation: Execute the disk_scheduling.py with the algorithm of your choice specified as an argument. (python disk_scheduling.py)

## Requirements

- Python 3.x
- No external libraries are required for the basic functioning of this program.

## Screenshots of the following answer

<img src="https://github.com/tirzagabriella/disk_scheduling_ForumWeek9/blob/main/Screenshot/disk.jpeg" width="700" height="400" />
