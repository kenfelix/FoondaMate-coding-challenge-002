FROM node:lts-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential libkrb5-dev

WORKDIR /front-end
COPY ./package.json /front-end
COPY ./package-lock.json /front-end
RUN npm install
COPY . /front-end/
EXPOSE 3000

CMD ["npm", "run", "dev"]