# Generated by Django 3.0.2 on 2020-08-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_books_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.CharField(choices=[('all', 'ALL'), ('books_school', 'School Books'), ('books_college', 'College Books'), ('biographic', 'Biographic'), ('adventure', 'Adventure'), ('childern', 'Childern'), ('cook', 'Cook'), ('treding', 'Trending'), ('other', 'Other')], default='Other', max_length=50),
        ),
    ]
