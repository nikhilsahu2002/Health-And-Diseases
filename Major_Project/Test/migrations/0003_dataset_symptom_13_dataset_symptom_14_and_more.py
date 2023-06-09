# Generated by Django 4.1.8 on 2023-05-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_dataset'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='Symptom_13',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='dataset',
            name='Symptom_14',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='dataset',
            name='Symptom_15',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='dataset',
            name='Symptom_16',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='dataset',
            name='Symptom_17',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Disease',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_1',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_10',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_11',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_12',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_2',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_3',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_4',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_5',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_6',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_7',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_8',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='Symptom_9',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
