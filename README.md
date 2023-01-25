Сборка тестировалась на Ubuntu 22.04 

Docker version 20.10.22

docker-compose version 1.29.2

docker-py version: 5.0.3

CPython version: 3.10.6

OpenSSL version: OpenSSL 3.0.2 15 Mar 2022

1. Установите docker и docker-compose.

```sudo apt install docker.io```
```sudo apt install docker-compose```

2. Добавьте пользователю доступ к группе docker и выполните logout

```sudo usermod -aG docker $USER```

3. Узнайте свой внешний ip - адрес (по которому будут подрубатся клиенты), либо для тестирования ip-адрес хоста

Введите данный адрес в файл example.env - MOSQUITTO_IP.

4. Для тестового сервера получите переменные окружения из файла example.env командой: ```export $(grep -v '^#' example.env | xargs)```

Для рабочего сервера обязательно измените пароли

5. Запустите: ```docker-compose build``` для постройки dockerfile

6. Запустите: ```docker-compose up -d```

7. Зайдите в консоль докера: ```docker exec -it mosquitto sh```

Выполните там команду ```mosquitto_passwd -b /mosquitto/data/pwfile mosquitto vedroid```

Где mosquitto логин, а vedroid пароль

Выйдите из консоли

8. Проверьте обновился ли файл /mosquitto/data/pwfile

9. Установите openssl

10. Создайте самоподписанный сертификат с помощью команды ```./creat_self_cert.sh```

Проверетье что вы находитесь в дериктории проекта

Сертификаты создадутся по пути $pwd/mosquitto/config/ca_certificates

11. Перезапустите docker-compose: 

```docker-compose down``` 

```docker-compose up -d```

Либо 

```docker-compose restart```