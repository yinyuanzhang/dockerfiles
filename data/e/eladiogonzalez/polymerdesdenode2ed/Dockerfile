# para colocar comentarios
# Imagen base
# las palabras reservadas van en mayusculas
FROM node:latest

# Directorio raiz para la aplicacion
WORKDIR /app

# definimos la seccion para el copiado de archivos, con el . indica anadir todo
# en el directorio raiz que hemos creado
ADD build/default  /app/build/default
#ADD . /app
ADD server.js /app
ADD package.json /app
ADD index.html /app



#add img/. /app/build/default



# como los archivos server.js y packages.json no se copian lo hacemos manul
ADD server.js /app
ADD package.json /app


#Dependencias necesarias para ejecutar la aplicacion
RUN  npm install

#se define el puerto a exponer
# generalmente las app node se crean en el nodo 3000 o sera indicado
EXPOSE 3000

#no requerimos variables de entorno

#definimos el comando para ejecutar la app
# se utiiza el mismo alias
CMD ["npm", "start"]
