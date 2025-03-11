# Usar una imagen base de Node.js
FROM node:18-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de dependencias
COPY package.json package-lock.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto del código
COPY . .

# Exponer el puerto 3000
EXPOSE 3000

# Comando para ejecutar el servidor de desarrollo
CMD ["npm", "run", "dev"]