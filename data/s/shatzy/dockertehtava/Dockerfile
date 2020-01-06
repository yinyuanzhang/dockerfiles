###########################################
# Dockerfile webpalvelimen rakentamiseksi
# Perustuu Nginx
# Mikko Kivelä 0439328
###########################################

# Haetaan Nginx levykuva
FROM nginx:alpine

# Kopioidaan repositorion tiedostot webpalvelimelle
COPY . /usr/share/nginx/html/

# Avataan portti 80
EXPOSE 80

# EOF
