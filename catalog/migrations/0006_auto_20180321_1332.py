# Generated by Django 2.0.3 on 2018-03-21 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
        migrations.AddField(
            model_name='book',
            name='book_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_id', to='catalog.BookInstance', unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_name', to='catalog.Author'),
        ),
    ]