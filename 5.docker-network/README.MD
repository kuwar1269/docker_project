Networking Using Docker 🐳🌐
Docker Networking is a powerful feature that allows you to create and manage networks of Docker containers. These networks enable seamless communication between containers, making it easier to build and deploy distributed applications. In this guide, we will explore the fundamentals of Docker Networking, including the types of network drivers, essential commands, and practical examples to help you get started.

By the end of this tutorial, you will have a solid understanding of how to configure and manage Docker networks, enabling your containers to communicate effectively. 🚀

Overview of Docker Networking 🖥️
Docker Networking allows you to create a network of Docker containers managed by a master node called the manager. Containers within the same Docker network can communicate with each other by sharing packets of information. This feature is essential for building microservices architectures, distributed systems, and multi-container applications.

Types of Network Drivers 🚦
Docker supports several network drivers, each designed for specific use cases. Below are the most commonly used network drivers:

Bridge: The default network driver. Containers in a bridge network are isolated from the host system but can communicate with each other.
Host: Containers share the host's network stack, removing isolation between the Docker host and containers.
None: No network interfaces are assigned to containers, making them inaccessible from the outside.
Overlay: Enables communication between multiple Docker daemons, making it ideal for Docker Swarm services.
IPvlan: Provides complete control over IPv4 and IPv6 addressing.
Macvlan: Assigns MAC addresses to containers, allowing them to appear as physical devices on the network.
Documentation 📚
For more information, refer to the official documentation:

Docker Documentation
Docker Network Documentation
Basics of Computer Networking
Installation and Setup 🛠️
Step 1: Verify Docker Installation
Run the following command in your terminal to check if Docker is installed:

docker --version
You should see an output similar to:

Docker version 20.10.17, build 100c701
Step 2: List Existing Docker Networks

To view the existing Docker networks, run:

docker network ls
This command lists all networks currently managed by Docker.

Essential Docker Networking Commands 🛠️
Create a Custom Bridge Network
To create a custom bridge network with a specific subnet and IP range, use the following command:

docker network create --driver bridge --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 net-bridge
--driver bridge: Specifies the bridge network driver.
--subnet 172.20.0.0/16: Defines the subnet for the network.
--ip-range 172.20.240.0/20: Specifies the IP range for container allocation.
net-bridge: The name of the custom network.
Connect a Container to a Network
To connect a running container to a specific network, use:

sudo docker network connect <network-name> <container-name or id>
Replace with the name of the network and with the container's name or ID.

Inspect a Docker Network
To view detailed information about a Docker network, use:

sudo docker network inspect <network-name>
This command provides JSON-formatted details about the network, including connected containers and IP addresses.

Run a Container on a Specific Network
To launch a container on a custom network, use:

docker run -itd --net=net-bridge --name=cont_database redis
-itd: Runs the container in detached mode with an interactive terminal.
--net=net-bridge: Connects the container to the net-bridge network.
--name=cont_database: Assigns a name to the container.
redis: The image used to create the container.
Retrieve a Container's IP Address
To fetch the IP address of a specific container, use:

docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' cont_database2
This command extracts the IP address of the container named cont_database2.

Inspect Network Containers in JSON Format
To inspect the containers connected to a network in a readable JSON format, use:

docker inspect --format='{{json .Containers}}' net-bridge | python -m json.tool
This command formats the output for better readability.

Inspect a Container's Network Settings
To view the network settings of a specific container, use:

docker inspect --format='{{json .NetworkSettings}}' server-B | python -m json.tool
This command provides detailed network configuration in JSON format.

Execute Commands Inside a Running Container
To open a Bash shell inside a running container, use:

docker container exec -it <CONTAINER ID> bash
Replace with the container's ID.

Install Network Utilities Inside a Container
To install the ping utility inside a container, use:

apt-get update
apt-get install iputils-ping
These commands update the package list and install the ping utility.

Test Network Connectivity
To test connectivity between containers, use the ping command:

ping <container-ip>
Practical Example: Container Communication 🖧

Launch Two Containers:
docker run -itd --net=net-bridge --name=server-A busybox
docker run -itd --net=net-bridge --name=server-B busybox
Retrieve IP Addresses:
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server-A
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server-B
Test Connectivity:
docker exec -it server-A ping <server-B-ip>
Conclusion 🎉

Congratulations! 🎉 You’ve successfully learned how to configure and manage Docker networks. By leveraging Docker Networking, you can build scalable, distributed applications with ease. Whether you're working on microservices, multi-container applications, or distributed systems, Docker Networking provides the tools you need to ensure seamless communication between containers.

Keep exploring and building more complex networks with Docker! 🚀🌐

Happy networking! 💻✨