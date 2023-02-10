# Generated by Django 4.1.2 on 2023-01-31 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XLiNK', '0008_alter_account_detail_alter_account_hobby_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('小学生', '小学生'), ('大学生', '大学生'), ('社会人', '社会人'), ('サイト', 'サイト'), ('高校生', '高校生'), ('中学生', '中学生'), ('会社', '会社'), ('学校', '学校')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('ゲーム', 'ゲーム'), ('運動', '運動'), ('TV', 'TV'), ('読書', '読書'), ('プログラミング', 'プログラミング'), ('PC', 'PC'), ('VR/AR', 'VR/AR'), ('映画', '映画')], max_length=8),
        ),
        migrations.AlterField(
            model_name='group',
            name='genre',
            field=models.CharField(choices=[('運動', '運動'), ('経済', '経済'), ('投資', '投資'), ('科学', '科学'), ('音楽', '音楽'), ('企業', '企業'), ('芸術', '芸術')], max_length=8),
        ),
    ]
