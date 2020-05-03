## Components

### Server

### Load Balancer

Load balancer
    - Keeps a list of servers
    - New servers can be added or removed
    - Cleanup task to remove served requests from sever request pool
    - Routes a request to a server
        - Round Robin Strategy
        - Based on success factor
        - .. 
    - Output which server is serving which requests


Server:
    - id
    - success percentage
    - max request limit
    
    S1 (90%, 5, 4), S2 (85%, 5, 1), S3(5%, 5, 1)
    