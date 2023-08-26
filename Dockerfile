# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Streamlit
RUN pip install streamlit

# Expose the port the app runs on
EXPOSE 8501

# Run the command to start the Streamlit app
# CMD streamlit run app/streamlit_app.py & python backend/backend.py

# Copy start script into container
COPY start.sh /app/start.sh

# Make start script executable
RUN chmod +x /app/start.sh

# Run start script
CMD ["/app/start.sh"]