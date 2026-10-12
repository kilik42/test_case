servers = [
    {"name": "web-01", "cpu": 45, "memory": 60},
    {"name": "web-02", "cpu": 92, "memory": 75},
    {"name": "api-01", "cpu": 65, "memory": 91},
    {"name": "api-02", "cpu": 30, "memory": 40},
    {"name": "worker-01", "cpu": 95, "memory": 94}
]

def check_servers(servers):
    # Counts the total number of servers.

    total_servers = len(servers)


    exceed_threshold = []
    memGreater = []
    cpuGreater = []
    # Identifies servers with CPU usage greater than 80%.
    for serv in servers:
        if serv.get("cpu") > 80:
            # returns greater than 80
            cpuGreater.append(serv.get("name"))
            exceed_threshold.append(serv.get("name"))


    # Identifies servers with memory usage greater than 85%.
           
        if serv.get("memory") > 85:
            memGreater.append(serv.get("name"))
            exceed_threshold.append(serv.get("name"))


    # Creates a list of server names that exceed either threshold, without duplicates.
    exceed_threshold = list(set(exceed_threshold))


    # Returns the results as a dictionary.
    return {
        "total": total_servers,
        "high_cpu": cpuGreater,
        "high_memory": memGreater,

        "unhealthy_servers": exceed_threshold

    }


print(check_servers(servers))