cd ..
cd docker-compose
cd django_starter_kit_production

docker compose down django_0
docker compose up django_0 -d
docker compose down django_1
docker compose up django_1 -d