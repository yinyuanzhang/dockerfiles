#Imagen
FROM    node:slim
#Carpeta de la app
WORKDIR /miapp
#Copia archivos
ADD . /miapp
#Paquetes necesarios
RUN npm install
#Puerto que expongo
VOLUME /datos
EXPOSE 3000
#Comando de inicio
CMD ["npm", "start"]
