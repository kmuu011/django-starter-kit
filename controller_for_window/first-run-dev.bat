cd ..
cd docker-compose
cd django-starter-kit-dev

docker compose up -d

cd ..
cd ..

python -m venv venv

call venv/Scripts/activate.bat

pip install -r requirements.txt
