# DevOps Foundations: Chaos Engineering Project

A demo for the [ChaosToolkit](https://chaostoolkit.org/) framework to simulate a chaos engineering experiment in a simple api server.

This project is part of the LinkedIn Learning course [DevOps Foundations: Chaos Engineering](https://www.linkedin.com/learning/devops-foundations-chaos-engineering).

## Project Structure

The application runs as a server in a Docker container, exposed on port 6000.

## Running the Application

### Prerequisites

- Docker and Docker Compose installed on your system

### Starting the Application

1. Clone this repository
2. Navigate to the project directory
3. Run the application in detached mode:

```bash
docker-compose up -d
```

### Stopping the Application

To stop the running containers:

```bash
docker-compose down
```

### Run the Chaos Experiment

To run the chaos experiment, you can run

```bash
docker-compose run --rm server sh -c "./run_experiments.sh"
```

This command will execute the chaos experiment defined in the [`experiments/dat-file-removal-tolerance-experiment.json`](./experiments/dat-file-removal-tolerance-experiment.json) file. The experiment simulates the removal of the `.dat` file and observes the server's response to determine if it can tolerate the absence of that file.
