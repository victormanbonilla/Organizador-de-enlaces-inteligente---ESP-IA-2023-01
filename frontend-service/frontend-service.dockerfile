FROM node:16.17.0-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN yarn

COPY . .

RUN yarn build

EXPOSE 8080
CMD [ "http-server", "dist" ]