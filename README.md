Сборка тестировалась на Ubuntu 22.04 

Docker version 20.10.22

docker-compose version 1.29.2

docker-py version: 5.0.3

CPython version: 3.10.6

OpenSSL version: OpenSSL 3.0.2 15 Mar 2022

1. Обновите apt и затем установите docker и docker-compose.
```sudo apt update```
```sudo apt install docker.io```
```sudo apt install docker-compose```

2. Добавьте пользователю доступ к группе docker и выполните logout

```sudo usermod -aG docker $USER```

3. Установите git если он не установлен

```sudo apt install git```

Клонируйте код из репозитория в домашнюю папку пользователя

```cd ~/```

```git clone https://github.com/FedOTs/mosquitto-python-mysql.git```

4. Узнайте свой внешний ip - адрес (по которому будут подрубатся клиенты), либо для тестирования ip-адрес хоста

Введите данный адрес в файл example.env - MOSQUITTO_IP.

5. Для тестового сервера получите переменные окружения из файла example.env командой: ```export $(grep -v '^#' example.env | xargs)```

Для рабочего сервера обязательно измените пароли

6. Запустите: ```docker-compose build``` для постройки dockerfile

7. Запустите: ```docker-compose up```

Дождитесь запуска всех служб, обязательно создания бд MySql затем остановите docker-compose т.к. на данный момент не настроены ssl-сертификаты

```docker-compose down```

8. Установите openssl (если он не установлен) и создайте самоподписанный сертификат с помощью команды ```./creat_self_cert.sh```

Проверетье что вы находитесь в дериктории проекта

Сертификаты создадутся по пути $pwd/mosquitto/config/ca_certificates

9. Запустите: ```docker-compose up -d``` и зайдите в консоль докера: ```docker exec -it mosquitto sh```

Выполните там команду ```mosquitto_passwd -b /mosquitto/data/pwfile mosquitto vedroid```

Где mosquitto логин, а vedroid пароль

Выйдите из консоли

10. Проверьте обновился ли файл /mosquitto/data/pwfile

11. Перезапустите docker-compose: 

```docker-compose down``` 

```docker-compose up -d```

Либо 

```docker-compose restart```