# Часть 1

Для работы установить пакет pip install djangorestframework  

## Задание 1
Создан новый Django-проект, подключен DRF в настройках проекта.

## Задание 2
Созданы следующие модели:
### Пользователь (Модель пользователя в приложении users)
- все поля от обычного пользователя, но авторизацию заменить на email;
- телефон;
- город;
- аватарка.

### Курс:
- название,
- превью (картинка),
- описание.

### Урок:
- название,
- описание,
- превью (картинка),
- ссылка на видео.

Урок и курс - это связанные между собой сущности. Уроки складываются в курс, в одном курсе может быть много уроков.

Модель курса и урока - в отдельном приложении materials.

## Задание 3
- Опиcаны CRUD для моделей курса и урока. Для реализации CRUD для курса использованы Viewsets, а для урока - Generic-классы.
- Для работы контроллеров описаны простейшие сериализаторы.
- При реализации CRUD для уроков реализованы все необходимые операции (получение списка, получение одной сущности, создание, изменение и удаление).
- Для работы контроллеров описаны простейшие сериализаторы.

# Часть 2. Сериализаторы

Для работы установить пакет pip install django-filter 

## Задание 1
Для модели курса добавлено в сериализатор поле вывода количества уроков. Поле реализовано с помощью SerializerMethodField()

## Задание 2
Добавлена новая модель в приложение users:

Платежи
- пользователь,
- дата оплаты,
- оплаченный курс или урок,
- сумма оплаты,
- способ оплаты: наличные или перевод на счет.

Поля пользователь, оплаченный курс и отдельно оплаченный урок - ссылки на соответствующие модели.

## Задание 3
Для сериализатора для модели курса реализовано поле вывода уроков. Вывод реализован с помощью сериализатора для связанной модели.

Один сериализатор должен выдавать и количество уроков курса и информацию по всем урокам курса одновременно.

## Задание 4
Настроена фильтрация для эндпоинта вывода списка платежей с возможностями:

- менять порядок сортировки по дате оплаты,
- фильтровать по курсу или уроку,
- фильтровать по способу оплаты.

# Часть 3. Права доступа в DRF

## Задание 1
Реализован CRUD для пользователей, настроен в проекте использование JWT-авторизации и закрыт каждый эндпоинт авторизацией.
Эндпоинты для авторизации и регистрации доступны для неавторизованных пользователей.

## Задание 2
Создана группа модераторов с правами работы с любыми уроками и курсами, но без возможности их удалять и создавать новые. Заложен функционал такой проверки в контроллеры.

## Задание 3
Описаны права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу модераторов, могли видеть, редактировать и удалять только свои курсы и уроки.

# Часть 4. Валидаторы, пагинация и тесты

## Задание 1
Для сохранения уроков и курсов реализована дополнительная проверка на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com.
То есть ссылки на видео можно прикреплять в материалы, а ссылки на сторонние образовательные платформы или личные сайты — нельзя.

В отдельном файле validators.py реализован валидатор, проверяющий ссылку, которую пользователь хочет записать в поле урока с помощью класса или функции. Интегрирован валидатор в сериализатор.

## Задание 2
Добавлена модель подписки на обновления курса для пользователя.

Модель подписки содержит следующие поля: «пользователь» (FK на модель пользователя), «курс» (FK на модель курса). Реализован эндпоинт для установки подписки пользователя и на удаление подписки у пользователя.

При этом при выборке данных по курсу пользователю присылается признак подписки текущего пользователя на курс. То есть дается информация, подписан пользователь на обновления курса или нет.

## Задание 3
Реализована пагинация для вывода всех уроков и курсов.

Пагинация реализована в отдельном файле paginators.py. Указаны параметры page_size, page_size_query_param, max_page_size для класса PageNumberPagination. Количество элементов на странице выберите самостоятельно. Интегрируйте пагинатор в контроллеры, используя параметр pagination_class.

## Задание 4
Написаны тесты, которые проверяют корректность работы CRUD уроков и функционал работы подписки на обновления курса.

В тестах использован метод setUp для заполнения базы данных тестовыми данными. Обработаны возможные варианты взаимодействия с контроллерами пользователей с разными правами доступа. Для аутентификации пользователей использованы self.client.force_authenticate().
