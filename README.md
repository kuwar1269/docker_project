# Docker & Streamlit Experiments Repository

Welcome to my GitHub repository for Docker and Streamlit experiments. This repo contains various mini-projects, experiments, and setups designed to enhance my understanding and application of Docker, Streamlit, MySQL, Kubernetes, and related DevOps/MLOps tools.

## 📁 Repository Structure

| Folder | Description |
|--------|-------------|
| `1.docker-hello-world` | Basic Docker container example using the "Hello World" image. |
| `2.streamlit-docker` | Running a Streamlit application inside a Docker container. |
| `3.StreamlitModel_Docker/StreamlitModel_Docker` | Deploying a machine learning model using Streamlit and Docker. |
| `4.MySQL_Docker_Project` | Dockerized MySQL server setup with sample database operations. |
| `5.docker-network` | Demonstrating inter-container communication using Docker networks. |
| `6.dockerfullstackapp` | Full-stack app setup using Docker (frontend, backend, and database). |
| `7.docker-volume` | Using Docker volumes for persistent storage and data sharing. |
| `8.Streamlit_evidently` | Streamlit project integrating [Evidently](https://evidentlyai.com/) for model monitoring and analysis. |
| `9.minikube-and-kubectl-exp` | Kubernetes experiments using Minikube and `kubectl`. |
| `10.streamlit_app` | Another standalone Streamlit application project. |
| `.venv` | Virtual environment for Python dependency isolation (typically excluded from version control). |

## 🔧 Technologies Used

- **Docker**
- **Streamlit**
- **MySQL**
- **Kubernetes (Minikube, kubectl)**
- **Evidently AI**
- **Python**
- **FastAPI** (in some full stack setups)

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/kuwar1269/<repo-name>.git
   cd <repo-name>  
docker build -t example-app .
docker run -p 8501:8501 example-app
kubectl apply -f deployment.yaml
