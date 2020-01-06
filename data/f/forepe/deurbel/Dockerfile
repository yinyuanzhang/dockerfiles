FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

# Temp SoCo
RUN /bin/sed -i "s/for group_element in tree.findall('ZoneGroup'):/for group_element in tree.find('ZoneGroups').findall('ZoneGroup'):/" /usr/local/lib/python3.7/site-packages/soco/core.py
