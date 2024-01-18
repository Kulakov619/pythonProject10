СТАРТ БЕЗ ДОКЕРА:
1) pip install django
2) pip install Pillow
3) python manage.py makemigrations
4) python manage.py migrate
5) python manage.py createsuperuser
6) python manage.py runserver 0.0.0.0:8000
7) Перейти в браузер 127.0.0.1:8000/admin

МОДЕЛИ:

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

Мета данные в классе модели 

    class Meta:
        verbose_name = _('пользователь') # имя в единсвенном числе
        verbose_name_plural = _('пользователи') # имя во мнодественном числе
        ordering = ['last_name'] # упорядочить по полю ...

Связь с другой моделью (один ко многим)
Пример (фото в альбомах)


    class Album(models.Model):
        name = models.CharField(_("название"), max_length=500)
        created = models.DateField(_("дата создания"), auto_now_add=True)
    
        class Meta:
            verbose_name = _('альбом')
            verbose_name_plural = _('альбомы')
            ordering = ['created']


    class Photo(models.Model):
        album = models.ForeignKey('album', on_delete=models.CASCADE, db_column='album_id')
        created = models.DateField(_("дата создания"), auto_now_add=True)
        photo = models.ImageField(_("фотография"), upload_to="uploads/photo/")
    
    
        class Meta:
            verbose_name = _('фотография')
            verbose_name_plural = _('фотографии')
            ordering = ['created']


АДМИНКА:

@admin.register(models.Имя модели)

class ИМЯ МОДЕЛИ+Admin(admin.ModelAdmin):

list_display = (поля модели для отображения в списке) 

search_fields = (поля модели для поиска)

Пример:

    class MessageAdmin(admin.ModelAdmin):
        list_display = ('user_to', 'user_from')
        search_fields = ('user_to',)

Пример СТЭКА:

    class PhotoInline(admin.StackedInline):
        model = models.Photo
        exclude = ('id',)
        extra = 0


    @admin.register(models.Album)
    class UserAdmin(admin.ModelAdmin):
        inlines = [PhotoInline, ]
        list_display = ('name', 'user')
        search_fields = ('name', 'user')


Связь многие ко многим. (Пример хобби из списка хобби)

Для этого необходимо сделать 2 таблица (класса):

Класс хобби:

    class Hobby(models.Model):
    name = models.CharField(_("название"), max_length=500)

    class Meta:
        verbose_name = _('хобби')
        verbose_name_plural = _('хобби')
        ordering = ['name']

Таблица связи Юзер-Хобби:

    class UserHobby(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE, db_column='user_id')
    hobby = models.ForeignKey('hobby', on_delete=models.CASCADE, db_column='hobby_id')

    class Meta:
        index_together = ['user_id', 'hobby_id']
        verbose_name = _('хобби пользователя')
        verbose_name_plural = _('хобби пользователя')

Добавить к юзеру новое поле:

    hobby = models.ManyToManyField(Hobby, through='UserHobby', verbose_name=_('хобби'), blank=True)