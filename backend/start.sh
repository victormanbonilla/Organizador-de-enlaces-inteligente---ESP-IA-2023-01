echo "Iniciando MySQL"
docker compose -f ./mysql/docker-compose.yaml up -d
echo "Iniciando Redis"
docker compose -f ./Redis/docker-compose.yaml up -d
echo "Iniciando Backend"
docker compose build
docker compose down
docker compose up --no-deps --force-recreate --remove-orphans