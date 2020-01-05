FROM python:3.6.2-alpine

# Set Environment Variables for DEV
ENV DB_USER=$DB_USER
ENV DB_PASS=$DB_PASS
ENV TZ=America/Bogota

# Copy all the requirements into the container
COPY requirements.txt ./

# Update apt-get, install unixodbc-dev
RUN pip install --upgrade pip \
&& apk add --no-cache --virtual .build-deps gcc g++ musl-dev \
&& apk add --no-cache jpeg-dev zlib-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev \
&& apk add --no-cache libffi-dev unixodbc-dev freetds-dev \
&& pip install -r ./requirements.txt \
&& apk del .build-deps && apk add --no-cache libstdc++ \
&& apk add --no-cache tzdata \
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Copy the application and create the application folder in the container
COPY ./ /app/

# Set the working directory in the container
WORKDIR /app

# Copy ODBC configuration
COPY odbc/odbc.ini /etc/
COPY odbc/odbcinst.ini /etc/

EXPOSE 5000
# Run the application
CMD python manage.py runserver -h 0.0.0.0