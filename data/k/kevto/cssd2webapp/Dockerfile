FROM node:7.10.0

RUN npm install -g serve

# Create the app folder and install the right packages.
WORKDIR /
RUN mkdir -p /var/apotfiat/
WORKDIR /var/apotfiat/
COPY . /var/apotfiat/
RUN chmod +x entrypoint.sh

# Installing frontend
WORKDIR /var/apotfiat/frontend/
RUN npm install
RUN npm run build

# Installing backend
WORKDIR /var/apotfiat/backend/
RUN npm install

WORKDIR /var/apotfiat/
EXPOSE 8080
CMD ./entrypoint.sh 
