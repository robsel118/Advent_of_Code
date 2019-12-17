FROM ubuntu:latest

RUN apt-get update \
    && apt-get install --no-install-recommends  --no-install-suggests -y curl \
    && apt-get -y install python3  \
    && apt-get -y install python3-pip 

WORKDIR /app  

COPY . .
CMD ["tail", "-f", "/dev/null"]