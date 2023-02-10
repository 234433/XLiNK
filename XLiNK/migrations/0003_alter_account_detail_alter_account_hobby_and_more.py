# Generated by Django 4.1.2 on 2023-01-29 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XLiNK', '0002_account_image_alter_account_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('学校', '学校'), ('高校生', '高校生'), ('サイト', 'サイト'), ('社会人', '社会人'), ('中学生', '中学生'), ('小学生', '小学生'), ('大学生', '大学生'), ('会社', '会社')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('TV', 'TV'), ('プログラミング', 'プログラミング'), ('映画', '映画'), ('運動', '運動'), ('VR/AR', 'VR/AR'), ('PC', 'PC'), ('読書', '読書'), ('ゲーム', 'ゲーム')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(upload_to='image/', verbose_name='Image'),
        ),
    ]
