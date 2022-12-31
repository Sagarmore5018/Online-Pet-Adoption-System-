# Generated by Django 4.0.3 on 2022-10-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_adopt_contact_info_alter_adopt_good_with_dogs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopt',
            name='age',
            field=models.CharField(choices=[('p', 'Puppyhood'), ('a', 'Adolescence'), ('ad', 'Adulthood'), ('s', 'Senior')], max_length=2),
        ),
        migrations.AlterField(
            model_name='adopt',
            name='contact_info',
            field=models.IntegerField(default='987654321'),
        ),
        migrations.AlterField(
            model_name='adopt',
            name='good_with_kids',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], max_length=1),
        ),
        migrations.AlterField(
            model_name='adopt',
            name='shots_upto_date',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], max_length=1),
        ),
        migrations.AlterField(
            model_name='adopt',
            name='vacinated',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], max_length=1),
        ),
    ]
