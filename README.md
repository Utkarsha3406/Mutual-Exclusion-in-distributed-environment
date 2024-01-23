# Mutual-Exclusion-in-distributed-environment
The provided Python code implements a simple simulation of a distributed mutual exclusion algorithm using threads and queues.

Mutual Exclusion in Distributed Environment:
In a distributed system, mutual exclusion refers to the coordination of processes to ensure that only one process can access a critical section at a time. This is crucial to prevent conflicts, data corruption, and ensure the integrity of shared resources.

# Code Description:
The code simulates a distributed environment with multiple processes that contend for access to a critical section. Each process runs as a separate thread and communicates with others using shared queues. The algorithm implemented here is a basic request-reply protocol.

# Process Class:

The Process class represents a single process in the distributed system.
It has methods for requesting and releasing the critical section (request_cs and release_cs), and a thread (handle_requests) to handle incoming requests from other processes.
Main Function:

The main function initializes the shared resources (lock and queues) and creates multiple instances of the Process class to represent individual processes.
Each process is started as a separate thread.
Simulation:

Each process, running in its thread, periodically requests the critical section, simulating some computation before making the request.
While waiting for replies from other processes, a process listens for incoming replies in its handle_requests thread.
Once the required number of replies (from all other processes) is received, the process enters the critical section, simulates work inside it, and then releases the critical section.
How the Code Works:
Initialization:

The main function initializes the shared lock and queues.
Creates multiple processes (instances of the Process class) with their own request and reply queues.
Process Execution:

Each process runs in its thread, continuously requesting the critical section at random intervals and handling replies from other processes.
The simulation includes a delay in the critical section to represent work being done.
Output:

The code outputs messages indicating when a process requests, receives a reply, enters the critical section, and releases the critical section.
Command-Line Arguments:

The code takes two command-line arguments: the number of processes and the duration of the simulation.





# Running the Code:
To run the code, you would execute it from the command line, providing the number of processes and the duration of the simulation as arguments. For example:

python distributed_mutual_exclusion.py 15 10

This would simulate a system with 15 processes for 10 seconds.

![DOS project ss](https://github.com/Utkarsha3406/Mutual-Exclusion-in-distributed-environment/assets/104308777/478c52e5-a5fe-4346-993e-7967f8ad8c29)

