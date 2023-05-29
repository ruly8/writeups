FROM node:latest
WORKDIR /usr/src/nodejs_server
COPY package.json ./
RUN npm install
COPY . .
EXPOSE 9090
CMD ["node", "server.js"]
