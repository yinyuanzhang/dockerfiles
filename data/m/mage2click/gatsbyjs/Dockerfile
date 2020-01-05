# Create a standalone instance of GraphiQL populated with gatsbyjs.org's data
# ---
FROM node:8

RUN npm install -g gatsby-cli
WORKDIR /usr/src/app/www

EXPOSE 8080
CMD [ "npm", "start" ]
# To run this image, set the port as an env var with `-e PORT=xxxx` e.g.
# docker run -p 8080:8080 --rm -it -e PORT=8080 <registryUsername>/<imageName>