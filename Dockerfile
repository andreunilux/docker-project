# Use a lightweight Python base image
FROM python:3.9.21-alpine3.21


# Copy the requirements and install them
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py ./

# Set the default command to run the game
CMD ["python", "app.py"]


