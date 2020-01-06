# Base docker image to use
FROM node:alpine
LABEL maintainer="ken.godoy@xome.com"

# Copy the code
RUN mkdir /app
COPY diy-res-ui/ /app

# Build the app
WORKDIR /app
RUN npm install
RUN npm run build

# Run the app on instantiation
EXPOSE 3000
CMD ["npm","run","start"]