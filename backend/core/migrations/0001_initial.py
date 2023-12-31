# Generated by Django 4.2.3 on 2023-08-07 17:10

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_name', models.CharField(max_length=255)),
                ('updated_date', models.DateField(auto_now=True)),
                ('file', models.FileField(upload_to='core/assignment/files')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=255)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_detail', models.CharField(max_length=255)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SectionYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=255)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_name', models.CharField(max_length=255)),
                ('updated_date', models.DateField(auto_now=True)),
                ('file', models.FileField(upload_to='core/resource/files')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='PlanTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.chapter')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.plan')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.topic')),
            ],
        ),
        migrations.CreateModel(
            name='PlanResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.chapter')),
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
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.chapter')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.plan')),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='sectionyear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sectionyear'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='section_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sectionyear'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.chapter'),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_detail', models.CharField(max_length=255)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.plan')),
            ],
        ),
    ]
