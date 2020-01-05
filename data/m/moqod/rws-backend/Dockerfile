FROM moqod/django-backend:1.9.6
RUN apt-get update && apt-get install -y --no-install-recommends binutils libproj0 libproj-dev gdal-bin && rm -rf /var/lib/apt/lists/*
ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get -y purge binutils libproj-dev gdal-bin
RUN apt-get -y autoremove --purge
