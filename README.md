# Docker Flask Project

A simple Flask web application containerized with Docker for easy deployment and scalability.

## Project Overview

This project demonstrates a basic Flask web application that has been containerized using Docker. The application serves a simple greeting message and is designed to showcase Docker containerization best practices.

## Features

- **Simple Flask Web App**: A minimal Flask application with a single route
- **Docker Containerization**: Fully containerized for consistent deployment
- **Lightweight**: Uses Python 3.10 slim image for optimal performance
- **Production Ready**: Configured to run on all interfaces (0.0.0.0)

## Project Structure

```text
dockerproject/
├── app.py              # Main Flask application
├── Dockerfile          # Docker configuration file
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Prerequisites

Before running this project, make sure you have the following installed:

- [Docker](https://www.docker.com/get-started) (version 20.10 or higher)
- [Docker Compose](https://docs.docker.com/compose/install/) (optional, for advanced usage)

## Getting Started

### Option 1: Using Docker (Recommended)

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd dockerproject
   ```

2. **Build the Docker image**:

   ```bash
   docker build -t flask-docker-app .
   ```

3. **Run the container**:

   ```bash
   docker run -p 5000:5000 flask-docker-app
   ```

4. **Access the application**:
   Open your web browser and navigate to `http://localhost:5000`

### Option 2: Local Development

1. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:

   ```bash
   python app.py
   ```

3. **Access the application**:
   Open your web browser and navigate to `http://localhost:5000`

## Docker Commands

### Build the image

```bash
docker build -t flask-docker-app .
```

### Run the container

```bash
docker run -p 5000:5000 flask-docker-app
```

### Run in detached mode

```bash
docker run -d -p 5000:5000 flask-docker-app
```

### Stop the container

```bash
docker stop <container-id>
```

### View running containers

```bash
docker ps
```

### View application logs

```bash
docker logs <container-id>
```

## Configuration

- **Port**: The application runs on port 5000 by default
- **Host**: Configured to accept connections from all interfaces (0.0.0.0)
- **Python Version**: Uses Python 3.10 slim image

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Returns a welcome message |

## Dependencies

- **Flask**: Web framework for Python
- **Python 3.10**: Runtime environment

## Development

### Adding New Features

1. Modify the `app.py` file to add new routes or functionality
2. Update `requirements.txt` if you add new dependencies
3. Rebuild the Docker image:
   ```bash
   docker build -t flask-docker-app .
   ```

### Environment Variables

You can customize the application behavior using environment variables:

```bash
docker run -p 5000:5000 -e FLASK_ENV=development flask-docker-app
```

## Deployment

### Production Deployment

For production deployment, consider:

1. **Using a production WSGI server** (e.g., Gunicorn):
   ```dockerfile
   CMD ["gunicorn", "--host", "0.0.0.0", "--port", "5000", "app:app"]
   ```

2. **Environment-specific configurations**
3. **Health checks and monitoring**
4. **Load balancing**

### Docker Compose (Optional)

Create a `docker-compose.yml` file for easier container management:

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
```

Run with:
```bash
docker-compose up
```

## Troubleshooting

### Common Issues

1. **Port already in use**: 
   - Change the port mapping: `docker run -p 8080:5000 flask-docker-app`

2. **Permission denied**:
   - Make sure Docker daemon is running
   - Check user permissions for Docker

3. **Build fails**:
   - Ensure all files are in the correct directory
   - Check Dockerfile syntax

