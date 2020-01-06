FROM osrm/osrm-backend:v5.22.0
RUN apt-get update
RUN apt-get install -y wget
RUN wget http://download.geofabrik.de/europe/denmark-latest.osm.pbf
RUN osrm-extract -p /opt/foot.lua denmark-latest.osm.pbf
RUN osrm-partition denmark-latest.osrm
RUN osrm-customize denmark-latest.osrm

