# Generated by Django 4.1.2 on 2023-01-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XLiNK', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(default=1, upload_to='media/', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('サイト', 'サイト'), ('会社', '会社'), ('学校', '学校'), ('中学生', '中学生'), ('高校生', '高校生'), ('社会人', '社会人'), ('大学生', '大学生'), ('小学生', '小学生')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('運動', '運動'), ('TV', 'TV'), ('VR/AR', 'VR/AR'), ('プログラミング', 'プログラミング'), ('読書', '読書'), ('PC', 'PC'), ('ゲーム', 'ゲーム'), ('映画', '映画')], max_length=8),
        ),
    ]
