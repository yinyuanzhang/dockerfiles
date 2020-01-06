# Imagen raíz
FROM node
# Carpeta raíz
WORKDIR /bwain-server
# Copia de archivos
ADD . /bwain-server
#Instalo los paquetes necesarios
RUN npm install
#Volumen de la imagen
VOLUME ["/logs"]
# Puerto que expone
EXPOSE 3000
# Comando de iniciado
CMD ["npm", "start"]
