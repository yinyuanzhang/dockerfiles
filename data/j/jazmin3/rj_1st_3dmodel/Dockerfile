FROM   python:3.7-alpine

MAINTAINER Roman Jazmin <client@socialconsulting.onmicrosoft.com>

# Copy html
WORKDIR /
COPY . .

# Run http server on port 8080
EXPOSE  8080
CMD ["python3", "-m", "http.server", "8080"]
