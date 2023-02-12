# Generated by Django 4.1.2 on 2023-02-11 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XLiNK', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='genre',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('社会人', '社会人'), ('サイト', 'サイト'), ('大学生', '大学生'), ('小学生', '小学生'), ('学校', '学校'), ('会社', '会社'), ('高校生', '高校生'), ('中学生', '中学生')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('ゲーム', 'ゲーム'), ('運動', '運動'), ('VR/AR', 'VR/AR'), ('プログラミング', 'プログラミング'), ('読書', '読書'), ('映画', '映画'), ('PC', 'PC'), ('TV', 'TV')], max_length=8),
        ),
    ]