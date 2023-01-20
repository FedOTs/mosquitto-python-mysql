1. Установите openssl

2. Узнайте свой внешний ip - адрес (по которому будут подрубатся клиенты), либо для тестирования ip-адрес хоста
Введите данный адрес в файл example.env - MOSQUITTO_IP.

3. Создайте самоподписанный сертификат с помощью команды creat_self_cert.sh
Проверетье что вы находитесь в дериктории проекта
Сертификаты создадутся по пути $pwd/mosquitto/config/ca_certificates

4. Для тестового сервера получите переменные окружения из файла example.env командой: export $(grep -v '^#' example.env | xargs)
Для рабочего сервера обязательно измените пароли

5. Запустите: docker-compose build для постройки dockerfile

6. Запустите: docker-compose up -d

7. Зайдите в консоль докера: docker exec -it mosquitto sh
Выполните там команду mosquitto_passwd -b /mosquitto/data/pwfile mosquitto vedroid 
Где mosquitto логин, а vedroid пароль
Выйдите из консоли

8. Проверьте обновился ли файл /mosquitto/data/pwfile

9. Перезапустите docker-compose: 
docker-compose down 
docker-compose up -d
Либо 
docker-compose restart