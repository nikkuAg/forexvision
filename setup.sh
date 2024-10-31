#!/bin/bash

read -p "Enter SECRET_KEY (leave blank for auto-generation): " SECRET_KEY
if [ -z "$SECRET_KEY" ]; then
  SECRET_KEY=$(openssl rand -base64 32)
fi

while true; do
  read -p "Set DEBUG mode to (True/False): " DEBUG
  case $DEBUG in
    True|true) DEBUG=True; break;;
    False|false) DEBUG=False; break;;
    *) echo "Invalid input. Please enter True or False.";;
  esac
done

read -p "Enter Backend URL (with trailing slash, leave blank for default): " BACKEND_URL
if [ -z "$BACKEND_URL" ]; then
  BACKEND_URL="http://localhost:8000/"
fi


# Create .env file
echo "SECRET_KEY=$SECRET_KEY" > .env
echo "DEBUG=$DEBUG" >> .env

echo "NEXT_PUBLIC_API_BASE_URL=$BACKEND_URL" >> ./forex_vision_frontend/.env

echo ".env file created successfully!"

echo "Starting backend container..."
docker compose up -d backend --build

docker exec -it forex_vision_backend python manage.py migrate

read -p "Do you want to populate the database for a time period of 1 year? (y/n): " POPULATE_DB
case $POPULATE_DB in
  y|Y) 
    docker exec -it forex_vision_backend python manage.py populate
    ;;
  n|N) 
    echo "Database not populated."
    ;;
  *) 
    echo "Invalid input. Please enter y or n."
    ;;
esac

cd forex_vision_frontend
npm install --force
npm run build
npm run start

