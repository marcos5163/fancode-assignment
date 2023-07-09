# Base image
FROM node:16

# Set working directory
WORKDIR /app-node

# Copy package.json and package-lock.json
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy project files
COPY . .

# Base image for Django
FROM python:3.9 AS django

# Set working directory for Django app
WORKDIR /app-django

# Copy requirements.txt
COPY requirements.txt .

# Install Django dependencies
RUN pip install -r requirements.txt

# Copy Django app source code
COPY . .

# Expose a port for node 
EXPOSE 3000

# Expose a port for django 
EXPOSE 8000

# Start the application
CMD ["sh", "-c", "cd /app-node && npm run start & cd /app-django && python manage.py runserver 0.0.0.0:8000"]