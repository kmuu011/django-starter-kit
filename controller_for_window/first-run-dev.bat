cd ..
cd docker-compose
cd django_starter_kit_dev

docker compose up -d

cd ..
cd ..

python -m venv venv

call venv/Scripts/activate.bat

pip install -r requirements.txt
