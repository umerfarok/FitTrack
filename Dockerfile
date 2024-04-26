# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . .

# Collect the static files
RUN python manage.py collectstatic --no-input

# Expose the port the app runs on
EXPOSE 8000

# Start the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]