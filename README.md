1. Установите openssl

2. Создайте самоподписанный сертификат с помощью команды creat_self_cert.sh
Сертификаты создадутся по пути /home/rkc/mosquitto-python-mysql/mosquitto/config/ca_certificates

3. Запустите: docker-compose up -d

4. Зайдите в консоль докера: docker exec -it mosquitto sh
Выполните там команду mosquitto_passwd -b /mosquitto/data/pwfile mosquitto vedroid 
Где mosquitto логин, а vedroid пароль
Выйдите из консоли

5. Проверьте обновился ли файл /mosquitto/data/pwfile