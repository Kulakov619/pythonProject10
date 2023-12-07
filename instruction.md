start:
1) pip install django
2) pip install Pillow
3) python manage.py makemigrations
4) python manage.py migrate
5) python manage.py createsuperuser
6) python manage.py runserver 0.0.0.0:8000
7) Перейти в браузер 127.0.0.1:8000/admin

Fields:
CharField - короткая строка 
    Пример: o_name = models.CharField(_("отчество"), max_length=500)
TextField - текстовое поле с неограниченным количеством символов
    Пример: about = models.TextField(_("обо мне"))
ImageField - фотография или картинка
    Пример: about = my_photo = models.ImageField(_("аватар"), upload_to="uploads/photo/")
BooleanField - True или False
    Пример: gender = models.BooleanField(_("мужчина?"))
DateField - дата
    Пример: gender = models.DateField(_("дата рождения"))
            created = models.DateField(_("дата отправки"), auto_now_add=True) автоматически заполняется  текущей датой
Аргументы blank=True, null=True для возможности оставлять поле пустым
    Пример: birthday = models.DateField(_("дата рождения"), blank=True, null=True)