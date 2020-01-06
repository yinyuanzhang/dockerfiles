FROM busybox

WORKDIR /www/
ADD index.html container.png ./

EXPOSE 8000

# Create a basic webserver and run it until the container is stopped 
CMD trap "exit 0;" TERM INT; httpd -p 8000 -f -v & wait
