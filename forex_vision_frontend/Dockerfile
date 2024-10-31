FROM node:22-alpine

WORKDIR /app

COPY . .

WORKDIR /app/forex_vision_frontend

RUN npm install --force

RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "start"]
