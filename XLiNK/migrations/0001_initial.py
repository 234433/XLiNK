# Generated by Django 4.1.2 on 2023-02-10 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='k宛ごり')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_name', models.CharField(blank=True, max_length=25, null=True, verbose_name='管理者名')),
                ('class_name', models.CharField(blank=True, max_length=23, null=True, verbose_name='Class名')),
                ('backimage', models.ImageField(upload_to='media/', verbose_name='BackImage')),
                ('explain', models.TextField(blank=True, max_length=180, verbose_name='explain')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='XLiNK.category', verbose_name='ジャンル')),
            ],
            options={
                'verbose_name_plural': 'ClassName',
            },
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=25, null=True, verbose_name='ユーザー名')),
                ('comment', models.TextField(blank=True, max_length=180)),
                ('image', models.ImageField(upload_to='image/', verbose_name='Image')),
                ('Destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='XLiNK.group')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infomation', models.TextField(blank=True, max_length=180, verbose_name='infomation')),
                ('hobby', models.CharField(choices=[('読書', '読書'), ('TV', 'TV'), ('プログラミング', 'プログラミング'), ('運動', '運動'), ('PC', 'PC'), ('VR/AR', 'VR/AR'), ('映画', '映画'), ('ゲーム', 'ゲーム')], max_length=8)),
                ('detail', models.CharField(choices=[('高校生', '高校生'), ('中学生', '中学生'), ('社会人', '社会人'), ('サイト', 'サイト'), ('会社', '会社'), ('大学生', '大学生'), ('小学生', '小学生'), ('学校', '学校')], max_length=8)),
                ('explain', models.TextField(blank=True, max_length=180, verbose_name='explain')),
                ('name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Account',
                'ordering': ['-name'],
            },
        ),
    ]
