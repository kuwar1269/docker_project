# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Upgrade pip to avoid compatibility issues
RUN pip install --upgrade pip

# Install dependencies with increased timeout and faster mirror
RUN pip install --default-timeout=100 -r requirements.txt --index-url https://pypi.org/simple

# Expose the port on which Streamlit runs
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "stream.py", "--server.port=8501", "--server.address=0.0.0.0"]