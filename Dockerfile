# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 for the application
EXPOSE 8000

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=your_project.settings.production

# Run the Django application using gunicorn as the WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project.wsgi:application"]
