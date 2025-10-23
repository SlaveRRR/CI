# frontend/Dockerfile
FROM node:20-alpine

# Создание рабочей директории
WORKDIR /app

# Копирование package.json и yarn.lock
COPY package.json yarn.lock .

# Установка зависимостей
RUN yarn install --frozen-lockfile

# Копирование исходного кода
COPY . .

# Открытие порта
EXPOSE 5173
