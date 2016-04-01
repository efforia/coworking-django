FROM django:latest
MAINTAINER William Oliveira de Lagos <william.lagos@outlook.com>
RUN apt-get update && apt-get install -y libjpeg-dev
RUN pip install --upgrade pip
RUN pip install Mezzanine Cartridge Pillow
