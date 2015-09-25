docker run -d --name db postgres
docker build -t fabrica .
docker run -d --name fabrica -v ${root}/fabricadeideias:/var/www/fabrica fabrica
docker run -d --name nginx -p 80:80 -p 443:443 -v ${root}/certificate:/etc/nginx/conf -v ${root}/config:/etc/nginx/conf.d nginx
