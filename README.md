1. Установите openssl

2. Создайте самоподписанный сертификат с помощью команды creat_self_cert.sh
Проверетье что вы находитесь в дериктории проекта
Сертификаты создадутся по пути $pwd/mosquitto/config/ca_certificates

3. Для тестового сервера получите переменные окружения из файла example.env командой: export $(grep -v '^#' example.env | xargs)

4. Запустите: docker-compose up -d

5. Зайдите в консоль докера: docker exec -it mosquitto sh
Выполните там команду mosquitto_passwd -b /mosquitto/data/pwfile mosquitto vedroid 
Где mosquitto логин, а vedroid пароль
Выйдите из консоли

6. Проверьте обновился ли файл /mosquitto/data/pwfile