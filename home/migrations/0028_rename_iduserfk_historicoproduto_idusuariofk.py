# Generated by Django 4.0.3 on 2022-03-23 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_usuario_iduserfk_alter_fotos_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicoproduto',
            old_name='idUserFK',
            new_name='idUsuarioFK',
        ),
    ]
