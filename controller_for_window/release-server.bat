cd ..
cd docker-compose
cd django_starter_kit_production

docker compose stop django_0
docker compose rm -f django_0
docker compose up -d --no-deps django_0

docker compose stop django_1
docker compose rm -f django_1
docker compose up -d --no-deps django_1
