# Use a base image
FROM ubuntu:latest

ENV SRVPORT=4499
ENV RSPFILE=response

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y netcat-openbsd fortune-mod cowsay 

COPY . .

RUN chmod +x /usr/src/app/wisecow.sh

EXPOSE $SRVPORT

CMD ["./wisecow.sh"]