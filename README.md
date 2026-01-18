<img width="890" height="359" alt="logo" src="https://github.com/user-attachments/assets/3b1facaf-ad81-47b6-985c-5e9732c00bdc" />
<img width="1579" height="948" alt="Снимок экрана 2026-01-18 в 21 16 45" src="https://github.com/user-attachments/assets/d476e55e-946b-48ea-ae52-ddfeedc61acb" />
<img width="1579" height="948" alt="Снимок экрана 2026-01-18 в 21 15 13" src="https://github.com/user-attachments/assets/eb6ae832-2f00-4a03-ad97-b9d382f4f583" />
<img width="1579" height="948" alt="Снимок экрана 2026-01-18 в 21 14 45" src="https://github.com/user-attachments/assets/3274d931-5b52-4126-a45e-4bd7de7d3e9f" />
<img width="1579" height="948" alt="Снимок экрана 2026-01-18 в 21 16 28" src="https://github.com/user-attachments/assets/e8fb7b31-8369-4ddf-9d78-107ad9caf58a" />
<img width="1579" height="948" alt="Снимок экрана 2026-01-18 в 21 15 32" src="https://github.com/user-attachments/assets/a75784ee-af51-426e-b6d3-08b141519c3d" />
<img width="1070" height="948" alt="Снимок экрана 2026-01-18 в 21 17 13" src="https://github.com/user-attachments/assets/ddb7486b-7e4f-48b1-a5a9-e35997a71786" />

### Facade-Contunent - Сайт строиткльных услуг


### Установка приложения Facade-Contunent локально
-Предварительные требования
-Перед началом убедитесь, что у вас установлены следующие компоненты на вашем устройстве:

-Docker
-Python
-1. Клонирование репозитория
-Клонируйте репозиторий вашего приложения (замените URL на ваш):

- git clone https://github.com/xash1rama/Facade-Continentgit

-Настройка окружения При необходимости создайте файл .env в корневой директории вашего проекта для хранения переменных окружения. Например:
-POSTGRES_DB=tweet_db
-POSTGRES_USER=admin
-POSTGRES_PASSWORD=admin
-Запуск приложения Теперь вы готовы запустить приложение. Выполните следующую команду в корневой директории проекта:
-docker-compose up -build
-Проверка статуса контейнеров Чтобы убедиться, что контейнеры запущены, выполните:
-docker-compose ps
-Доступ к приложению После успешного запуска вы сможете получить доступ к вашему приложению через браузер по адресу:
-http://localhost:8000
-Проверка логов Если что-то пошло не так, вы можете просмотреть логи с помощью:
-docker-compose logs
-Остановка приложения Чтобы остановить приложение и контейнеры, выполните:
-docker-compose down


### Установка приложения Facade-Contunent на удаленном сервере
-Это руководство поможет вам установить и запустить приложение на удаленном сервере с использованием Docker и Docker Compose.

-Предварительные требования
-Перед началом убедитесь, что у вас установлены следующие компоненты на вашем удаленном сервере:

-Docker
-Docker Compose
### Шаги по установке
-1. Подключение к удаленному серверу
-Подключитесь к вашему удаленному серверу с помощью SSH:

-:bash
-ssh username@your_server_ip
-Установка Docker и Docker Compose Если Docker и Docker Compose не установлены, выполните следующие команды:
### Установка Docker:

-sudo apt update
-sudo apt install -y docker.io
-sudo systemctl start docker
-sudo systemctl enable docker
### Установка Docker Compose:

-sudo apt install -y docker-compose
-Клонирование репозитория Клонируйте репозиторий вашего приложения (замените URL на ваш):
-git clone https://github.com/xash1rama/Facade-Continent.git
-cd python_advanced_diploma
-Настройка окружения При необходимости создайте файл .env в корневой директории вашего проекта для хранения переменных окружения. Например:
-POSTGRES_DB=tweet_db
-POSTGRES_USER=admin
-POSTGRES_PASSWORD=admin
-Запуск приложения Теперь вы готовы запустить приложение. Выполните следующую команду в корневой директории проекта:
-docker-compose up -d
-Проверка статуса контейнеров Чтобы убедиться, что контейнеры запущены, выполните:
-docker-compose ps
-Доступ к приложению После успешного запуска вы сможете получить доступ к вашему приложению через браузер по адресу:
-http://your_server_ip:8000
-Проверка логов Если что-то пошло не так, вы можете просмотреть логи с помощью:
-docker-compose logs
-Остановка приложения Чтобы остановить приложение и контейнеры, выполните:
-docker-compose down
-Заключение Теперь ваше приложение Facade-Contunent должно быть успешно установлено и запущено на удаленном сервере. Если у вас возникнут вопросы или проблемы, не стесняйтесь обращаться за помощью.
