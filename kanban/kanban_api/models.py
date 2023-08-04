 
from django.db import models


class Board(models.Model):
    board_id = models.IntegerField(primary_key=True)
    bname = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board'


class Comment(models.Model):
    comment_id = models.IntegerField(db_column='Comment_id', primary_key=True)  # Field name made lowercase.
    message = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Employee(models.Model):
    emp_id = models.AutoField(db_column='Emp_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    acc_citeria = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    assigner = models.IntegerField(blank=True, null=True)
    assignee = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    comment_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'

