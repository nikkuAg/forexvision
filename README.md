# Forex Vision

Forex Vision is a full-stack application that scrapes historic exchange data from Yahoo Finance, stores it in a database, and provides a REST API to query the data. It also includes a simple frontend to visualize the historic data.

## Project Overview

This project is divided into three main tasks:

1. Scraping historic exchange data from Yahoo Finance using Python.
2. Building a REST API using Django to query the scraped data.
3. Creating a simple frontend using ReactJS to visualize the historic data.

## Setting Up the Project

To set up the project, follow these steps:

### Option 1: Using Docker (Recommended)

1. Clone the repository: `git clone https://github.com/nikkuAg/forexvision.git`
2. Navigate to the project directory: `cd forexvision`
3. Run the setup script: `bash setup.sh`
   This script will set up the environment variables, create a .env file, start the Docker container, and run the database migrations.

### Option 2: Without Docker

#### Backend

1. Clone the repository: `git clone https://github.com/your-username/forexvision.git`
2. Navigate to the backend directory: `cd forexvision/forex_vision`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on Windows)
5. Install the required packages: `pip install -r requirements.txt`
6. Set up the environment variables manually by creating a .env file with the required variables.
   1. SECRET_KEY=YOUR_SECRET_KEY
   2. DEBUG=True
7. Run the database migrations: `python manage.py migrate`
8. Start the backend server: `python manage.py runserver`

#### Frontend

1. Navigate to the frontend directory: `cd forex_vision_frontend`
2. Install the required packages: `npm install` or `npm install --force`
3. Build the frontend: `npm run build`
4. Start the frontend server: `npm run start`

## Hosting

The project is hosted at [ForexVision](https://forexvision-frontend.onrender.com/)

## API Documentation

The API documentation can be found at `http://localhost:8000/swagger` or [ForexVision Api Docs](https://forexvision-backend.onrender.com/swagger).
