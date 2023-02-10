# Generated by Django 4.1.2 on 2023-01-30 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XLiNK', '0004_remove_account_image_alter_account_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='genre',
            field=models.CharField(choices=[('企業', '企業'), ('運動', '運動'), ('科学', '科学'), ('投資', '投資'), ('芸術', '芸術'), ('経済', '経済'), ('音楽', '音楽')], default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('学校', '学校'), ('小学生', '小学生'), ('高校生', '高校生'), ('社会人', '社会人'), ('中学生', '中学生'), ('会社', '会社'), ('大学生', '大学生'), ('サイト', 'サイト')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('運動', '運動'), ('ゲーム', 'ゲーム'), ('プログラミング', 'プログラミング'), ('VR/AR', 'VR/AR'), ('読書', '読書'), ('PC', 'PC'), ('映画', '映画'), ('TV', 'TV')], max_length=8),
        ),
    ]
