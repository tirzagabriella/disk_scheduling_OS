import sys

def read_requests(filename):
    # Read cylinder requests from txt.file 
    with open(filename, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines()]
    return requests

def fcfs(requests, start):
    # FCFS (First Come First Served) alogirthm without sorting
    head_movements = 0
    current_position = start
    for request in requests:
        head_movements += abs(request - current_position)
        current_position = request
    return head_movements

def fcfs_optimized(requests, start):
    # Improved FCFS (First Come First Served) algorithm with sorting
    requests.sort()
    head_movements = 0
    current_position = start
    for request in requests:
        head_movements += abs(request - current_position)
        current_position = request
    return head_movements

def scan(requests, start, direction='right', total_cylinders=5000):
    # SCAN algorithm without sorting and with default right direction
    head_movements = 0
    current_position = start
    left = []
    right = [total_cylinders - 1]

    for request in requests:
        if request < start:
            left.append(request)
        else:
            right.append(request)

    if direction == 'left': # But I decided to default from right
        # Move left first, then right
        for request in reversed(left):
            head_movements += abs(current_position - request)
            current_position = request
        for request in right:
            head_movements += abs(current_position - request)
            current_position = request
    else:
        # Move right first, then left
        for request in right:
            head_movements += abs(current_position - request)
            current_position = request
        for request in reversed(left):
            head_movements += abs(current_position - request)
            current_position = request

    return head_movements

def scan_optimized(requests, start, direction='right', total_cylinders=5000):
    # Improved SCAN algorithm with sorting and with default right direction
    head_movements = 0
    current_position = start
    left = []
    right = [total_cylinders - 1]

    for request in requests:
        if request < start:
            left.append(request)
        else:
            right.append(request)

    left.sort()
    right.sort()

    if direction == 'left': # I already set the direction from right
        # Move left first, then right
        for request in reversed(left):
            head_movements += abs(current_position - request)
            current_position = request
        for request in right:
            head_movements += abs(current_position - request)
            current_position = request
    else:
        # Move right first, then left
        for request in right:
            head_movements += abs(current_position - request)
            current_position = request
        for request in reversed(left):
            head_movements += abs(current_position - request)
            current_position = request

    return head_movements

def c_scan(requests, start, total_cylinders=5000):
    # C-SCAN algorithm without sorting 
    head_movements = 0
    current_position = start

    # Create lists for requests on the right and left 
    right = [total_cylinders - 1]  # simulate the end of the disk
    left = [0]  # simulate the start of the disk
    for req in requests:
        if req >= start:
            right.append(req)
        else:
            left.append(req)

    # First process all requests
    for request in right:
        head_movements += abs(current_position - request)
        current_position = request

    # Jump back to the start 
    head_movements += total_cylinders - current_position
    current_position = 0

    # Then process all requests
    for request in left:
        head_movements += abs(current_position - request)
        current_position = request

    return head_movements

def c_scan_optimized(requests, start, total_cylinders=5000):
    # Improved C-SCAN algorithm with sorting 
    head_movements = 0
    current_position = start

    # Create lists for requests
    right = [total_cylinders - 1]  # simulate the end of the disk
    left = [0]  # simulate the start of the disk
    for req in requests:
        if req >= start:
            right.append(req)
        else:
            left.append(req)

    # Sort the lists
    right.sort()
    left.sort()

    # Process all requests 
    for request in right:
        head_movements += abs(current_position - request)
        current_position = request

    # Jump back to the start 
    head_movements += total_cylinders - current_position
    current_position = 0

    # Process all requests 
    for request in left:
        head_movements += abs(current_position - request)
        current_position = request

    return head_movements

def main():
    # Hardcode the filename and starting position
    filename = 'requests.txt'
    requests = read_requests(filename)

    # Initial disk setup
    start = requests[0]
    requests = requests[1:]

    original_fcfs = fcfs(requests, start)
    optimized_fcfs = fcfs_optimized(requests, start) 
    original_scan = scan(requests, start)
    optimized_scan = scan_optimized(requests, start)
    original_cscan = c_scan(requests, start)
    optimized_cscan = c_scan_optimized(requests, start)

    print(f"FCFS Original: {original_fcfs}, Optimized: {optimized_fcfs}")
    print(f"SCAN Original: {original_scan}, Optimized: {optimized_scan}")
    print(f"C-SCAN Original: {original_cscan}, Optimized: {optimized_cscan}")

if __name__ == "__main__":
    main()
