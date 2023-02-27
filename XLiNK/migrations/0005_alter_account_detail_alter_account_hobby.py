# Generated by Django 4.1.2 on 2023-02-27 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XLiNK', '0004_followerscount_alter_account_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('小学生', '小学生'), ('高校生', '高校生'), ('会社', '会社'), ('中学生', '中学生'), ('大学生', '大学生'), ('社会人', '社会人'), ('サイト', 'サイト'), ('学校', '学校')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('映画', '映画'), ('読書', '読書'), ('TV', 'TV'), ('ゲーム', 'ゲーム'), ('PC', 'PC'), ('運動', '運動'), ('プログラミング', 'プログラミング'), ('VR/AR', 'VR/AR')], max_length=8),
        ),
    ]
