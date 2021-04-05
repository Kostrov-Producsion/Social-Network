# Generated by Django 2.2.6 on 2021-02-12 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import project.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('date_birth', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=7)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('quote', models.CharField(blank=True, max_length=150)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('description', models.CharField(blank=True, max_length=150)),
                ('date_pub', models.DateField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('type', models.CharField(choices=[('D', 'Диалог'), ('C', 'Чат')], default='C', max_length=1)),
            ],
            options={
                'ordering': ['-last_message'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('description_video', models.TextField(blank=True)),
                ('video', project.models.ContentTypeRestrictedFileField(blank=True, null=True, upload_to=project.models.user_directory_path_video)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Re_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('re_posts', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('recipients', models.ManyToManyField(related_name='Recipients_content', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('message', models.TextField()),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Posts',
                'ordering': ['date_pub'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Принадлжеит_альбому', to='project.Album')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('txtAll', models.TextField(blank=True, verbose_name='описание_профиля')),
                ('txtAudio', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_аудио')),
                ('txtHidAudio', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_аудио_от_некоторых_друзей')),
                ('txtVideo', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_видео')),
                ('txtHidVideo', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_видео_от_некоторых_друзей')),
                ('txtPhoto', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_фото')),
                ('txtHidPhoto', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_фото_от_некоторых_друзей')),
                ('txtGroup', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_группа')),
                ('txtHidGroup', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_группа_от_некоторых_друзей')),
                ('txtPost', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_пост')),
                ('txtHidPost', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_пост_от_некоторых_друзей')),
                ('txtFriend', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_друзей')),
                ('txtHidFriend', models.TextField(blank=True, verbose_name='статус_приватности_для_модели_друзей_от_некоторых_друзей')),
                ('all', models.ManyToManyField(blank=True, related_name='Скрыть_от_всех', to=settings.AUTH_USER_MODEL)),
                ('audio', models.ManyToManyField(blank=True, related_name='Скрыть_аудио', to=settings.AUTH_USER_MODEL)),
                ('audioHidFriend', models.ManyToManyField(blank=True, related_name='Скрыть_аудио_от_некоторых_друзей', to=settings.AUTH_USER_MODEL)),
                ('friend', models.ManyToManyField(blank=True, related_name='Скрыть_друзей', to=settings.AUTH_USER_MODEL)),
                ('friendHidFriend', models.ManyToManyField(blank=True, related_name='Скрыть_друзей_от_некоторых_друзей', to=settings.AUTH_USER_MODEL)),
                ('group', models.ManyToManyField(blank=True, related_name='Скрыть_группы', to=settings.AUTH_USER_MODEL)),
                ('groupHidFriend', models.ManyToManyField(blank=True, related_name='Скрыть_группы_от_некоторых_друзей', to=settings.AUTH_USER_MODEL)),
                ('photo', models.ManyToManyField(blank=True, related_name='Скрыть_фото', to=settings.AUTH_USER_MODEL)),
                ('photoHidFriend', models.ManyToManyField(blank=True, related_name='Скрыть_фото_от_некоторых_друзей', to=settings.AUTH_USER_MODEL)),
                ('post', models.ManyToManyField(blank=True, related_name='Скрыть_посты', to=settings.AUTH_USER_MODEL)),
                ('postHidFriend', models.ManyToManyField(blank=True, related_name='Скрыть_посты_от_некоторых_друзей', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ManyToManyField(blank=True, related_name='Скрыть_видео', to=settings.AUTH_USER_MODEL)),
                ('videoHidFriend', models.ManyToManyField(blank=True, related_name='Скрыть_видео_от_некоторых_друзей', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_message', models.SlugField(max_length=150, unique=True)),
                ('message', models.TextField()),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False, verbose_name='')),
                ('is_update', models.BooleanField(default=False, verbose_name='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Chat', verbose_name='')),
            ],
            options={
                'ordering': ['date_pub'],
            },
        ),
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('vote', models.SmallIntegerField(choices=[(1, 'Нравится'), (1, 'Не нравится')], verbose_name='Голос')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('friends', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Друзья', to=settings.AUTH_USER_MODEL)),
                ('possible_friends', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Возможные_друзья', to=settings.AUTH_USER_MODEL)),
                ('waiting_confirmations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ожидание_подтвержденя', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments',
                'ordering': ['date'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='chat',
            name='last_message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_message', to='project.Message'),
        ),
        migrations.AddField(
            model_name='chat',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Участник'),
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('author_track', models.CharField(blank=True, max_length=200, null=True)),
                ('title_track', models.CharField(blank=True, max_length=200, null=True)),
                ('audio', project.models.ContentTypeRestrictedFileField(blank=True, null=True, upload_to=project.models.user_directory_path_audio)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Содержит_фото', to='project.Photo'),
        ),
    ]