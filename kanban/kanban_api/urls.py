from django.urls import path
from .views import *

urlpatterns = [
    # Task
    # GET
    path('tasks', GetTasksView.as_view()),
    # GET BY ID
    path('task/id/<int:id>/', GetTasksByIDView.as_view()),
    # POST
    path('task', PostTasksView.as_view()),
    # DELETE
    path('task/<int:id>', DeleteTasksView.as_view()),
    # PUT
    path('task/<int:id>/', PutTasksView.as_view()),
    # GET TASKS FROM TODAY
    path('tasks/today/', GetTasksTodayView.as_view()),
    # GET TASKS FROM THIS WEEK
    path('tasks/this-week/', GetTasksThisWeekView.as_view()),
    # GET TASKS FROM THIS MONTH
    path('tasks/this-month/', GetTasksThisMonthView.as_view()),
    # GET TASKS FROM THIS YEAR
    path('tasks/this-year/', GetTasksThisYearView.as_view()),
    # GET TASK FROM ALL TIME
    path('tasks/all-time/', GetTasksView.as_view()),

    # Employee
    # GET
    path('employees', GetEmployeesView.as_view()),
    # GET BY ID
    path('employee/<int:id>', GetEmployeesByIdView.as_view()),
    # POST
    path('register', PostEmployeesView.as_view()),

    # Login employee
    path('login', LoginView.as_view()),
]
