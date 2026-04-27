from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='imagem_principal',
            field=models.ImageField(blank=True, null=True, upload_to='imoveis/'),
        ),
    ]
