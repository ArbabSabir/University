# Generated by Django 4.2.5 on 2023-09-10 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ccode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=39)),
                ('rollnumber', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=39)),
                ('address', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='University_app.coursemodel')),
            ],
        ),
        migrations.CreateModel(
            name='EnromentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='University_app.coursemodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='University_app.studentmodel')),
            ],
        ),
    ]