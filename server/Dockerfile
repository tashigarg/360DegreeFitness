FROM node:20

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 5050

ENV PORT=5050

CMD ["npm", "start"]

