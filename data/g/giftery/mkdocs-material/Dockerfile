FROM python:3.6-alpine

# Set build directory
WORKDIR /tmp

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

# Set working directory
WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8000

# Start development server by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
