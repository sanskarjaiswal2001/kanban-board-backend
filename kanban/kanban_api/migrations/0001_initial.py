# Generated by Django 3.0.3 on 2023-07-12 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bname', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'board',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(db_column='Emp_ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('col_id', models.IntegerField(primary_key=True, serialize=False)),
                ('col_name', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='kanban_api.Board')),
            ],
            options={
                'db_table': 'list',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.IntegerField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('acc_citeria', models.CharField(blank=True, max_length=255, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('assignee', models.ForeignKey(blank=True, db_column='assignee', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_tasks', to='kanban_api.Employee')),
                ('assigner', models.ForeignKey(blank=True, db_column='assigner', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='kanban_api.Employee')),
                ('col', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='kanban_api.List')),
            ],
            options={
                'db_table': 'task',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.IntegerField(db_column='Comment_id', primary_key=True, serialize=False)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='kanban_api.Task')),
            ],
            options={
                'db_table': 'comment',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='board',
            name='emp',
            field=models.ForeignKey(blank=True, db_column='Emp_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='kanban_api.Employee'),
        ),
    ]