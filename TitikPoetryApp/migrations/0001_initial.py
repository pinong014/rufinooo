# Generated by Django 3.1.6 on 2021-06-25 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True)),
                ('birthday', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tula', models.CharField(max_length=50)),
                ('text', models.TextField(default='')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='post_files')),
                ('RecId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TitikPoetryApp.recruit')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSigya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messagebox', models.TextField(default='')),
                ('book_donation', models.ImageField(upload_to=None)),
                ('integer', models.IntegerField(null=True)),
                ('date1', models.DateTimeField()),
                ('RecId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TitikPoetryApp.recruit')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50)),
                ('date2', models.DateTimeField(auto_now_add=True)),
                ('RecId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TitikPoetryApp.recruit')),
                ('publications', models.ManyToManyField(to='TitikPoetryApp.Tula')),
            ],
        ),
    ]
