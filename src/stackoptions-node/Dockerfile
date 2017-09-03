FROM node:8.4.0-slim

# Create app directory
RUN mkdir -p /usr/src/stackoptions-node
WORKDIR /usr/src/stackoptions-node

# Install app dependencies
COPY src/stackoptions-node/src/ /usr/src/stackoptions-node
RUN npm install

EXPOSE 80

# CMD ["npm", "start"]
