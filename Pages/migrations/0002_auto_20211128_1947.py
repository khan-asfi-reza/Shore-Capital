# Generated by Django 3.2.9 on 2021-11-28 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='componenttextcontent',
            name='image_alt',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sectiontextcontent',
            name='image_alt',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='SectionImageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_alt', models.CharField(blank=True, max_length=200)),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Pages.pagesection')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]