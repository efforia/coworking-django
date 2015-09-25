docker run -d --name nginx -p 80:80 -v ${root}/certificate:/etc/nginx/conf -v ${root}/config:/etc/nginx/conf.d nginx
docker run -d --name db postgres
docker build -t fabrica .
docker run -d --name fabrica -v ${root}/:/usr/src/app fabrica
