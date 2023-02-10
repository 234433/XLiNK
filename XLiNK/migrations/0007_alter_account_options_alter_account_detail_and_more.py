# Generated by Django 4.1.2 on 2023-01-31 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('XLiNK', '0006_alter_account_detail_alter_account_hobby_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['-name'], 'verbose_name_plural': 'Account'},
        ),
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('大学生', '大学生'), ('学校', '学校'), ('高校生', '高校生'), ('社会人', '社会人'), ('小学生', '小学生'), ('サイト', 'サイト'), ('会社', '会社'), ('中学生', '中学生')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('TV', 'TV'), ('プログラミング', 'プログラミング'), ('PC', 'PC'), ('運動', '運動'), ('ゲーム', 'ゲーム'), ('VR/AR', 'VR/AR'), ('映画', '映画'), ('読書', '読書')], max_length=8),
        ),
        migrations.AlterField(
            model_name='group',
            name='genre',
            field=models.CharField(choices=[('投資', '投資'), ('運動', '運動'), ('音楽', '音楽'), ('芸術', '芸術'), ('科学', '科学'), ('経済', '経済'), ('企業', '企業')], max_length=8),
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
