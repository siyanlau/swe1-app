# Generated by Django 4.2.6 on 2023-10-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0003_rename_pub_data_question_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(
                db_column="pub_data", verbose_name="date published"
            ),
        ),
    ]
