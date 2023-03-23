# FROM node:16.17.0-alpine AS build

# WORKDIR /app

# COPY . .

# RUN yarn

# RUN yarn build

# # Stage 2 - Production Stage
# FROM nginx:1.23.3-alpine

# COPY --from=build /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]

FROM node:16.17.0-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN yarn

COPY . .

RUN yarn build

EXPOSE 80
CMD [ "http-server", "dist" ]