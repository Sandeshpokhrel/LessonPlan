# Generated by Django 4.2.3 on 2023-08-07 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_sectionyear_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='chapter',
        ),
        migrations.CreateModel(
            name='PlanTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.plan')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.topic')),
            ],
        ),
        migrations.CreateModel(
            name='PlanResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.plan')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.resource')),
            ],
        ),
        migrations.CreateModel(
            name='PlanChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.chapter')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.plan')),
            ],
        ),
        migrations.CreateModel(
            name='PlanAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.assignment')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.plan')),
            ],
        ),
    ]