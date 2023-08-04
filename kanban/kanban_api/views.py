from django.http import JsonResponse
from django.views.generic import View
from rest_framework import status
from .serializers import *
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
import json
from .models import *


errors = {
    'not_found' : JsonResponse(json.loads('{"error" : "not_found"}'),safe = False , status = status.HTTP_404_NOT_FOUND),
    'not_updated' : JsonResponse(json.loads('{"error" : "not_updated"}'),safe=False, status = status.HTTP_304_NOT_MODIFIED),
    'already_exists' : JsonResponse({'error':'already_exists'},safe=False, status = status.HTTP_409_CONFLICT),
}
# Abstract class to check if the id exists in a particular table or not (Returns True if the id exists in the table)
class CheckExistsClass(View):
    def check_exists(self, object):
        if object.exists():
            return True
        else:
            return False

# Abstract class for GET operations
class BaseGetView(View):
    model = None
    serializer = None

    def get(self, request):
        objects = self.model.objects.all()
        serialized = self.serializer(objects, many=True)
        return JsonResponse(serialized.data, safe=False, status=status.HTTP_200_OK)


# Abstract class for POST operations
class BasePostView(View):
    model = None
    serializer = None

    def post(self, request):
        data = json.loads(request.body)
        serialized = self.serializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        return errors['not_updated']


# Abstract class for DELETE operations
class BaseDeleteView(View):
    model = None

    def delete(self, request, id):
        objects = self.model.objects.filter(pk=id)
        if CheckExistsClass().check_exists(objects):
            objects.delete()
            return JsonResponse({'message': 'deleted'}, status=status.HTTP_200_OK)
        else:
            return errors['not_found']


# Abstract class for PUT operations
class BasePutView(View):
    model = None
    serializer = None

    def put(self, request, id):
        obj = self.model.objects.filter(pk=id).first()
        if CheckExistsClass().check_exists(self.model.objects.filter(pk=id)):
            data = json.loads(request.body)
            serialized = self.serializer(instance=obj, data=data)
            if serialized.is_valid():
                serialized.save()
                return JsonResponse(serialized.data, safe=False, status=status.HTTP_200_OK)
            return errors['not_updated']
        else:
            return errors['not_found']


# Concrete views for 'tasks' resource
class GetTasksView(BaseGetView):
    model = Task
    serializer = TaskSerializer


class GetTasksByStatusView(BaseGetView):
    model = Task
    serializer = TaskSerializer

    def get(self, request, id):
        tasks = Task.objects.filter(status=id)
        serialized = self.serializer(tasks, many=True)
        return JsonResponse(serialized.data, safe=False, status=status.HTTP_200_OK)


class GetTasksByIDView(BaseGetView):
    model = Task
    serializer = TaskSerializer

    def get(self, request, id):
        tasks = Task.objects.filter(task_id=id)
        serialized = self.serializer(tasks, many=True)
        return JsonResponse(serialized.data, safe=False, status=status.HTTP_200_OK)


class GetTasksTodayView(BaseGetView):
    model = Task
    serializer = TaskSerializer

    def get(self, request):
        today = timezone.now().date()
        tomorrow = today + timedelta(days=1)
        tasks = Task.objects.filter(start_date__gte=today, start_date__lt=tomorrow)
        serialized = self.serializer(tasks, many=True)
        return JsonResponse(serialized.data, safe=False, status=status.HTTP_200_OK)


class GetTasksThisWeekView(BaseGetView):
    model = Task
    serializer = TaskSerializer

    def get(self, request):
        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=7)
        tasks = Task.objects.filter(start_date__gte=start_of_week, start_date__lt=end_of_week)
        serialized = self.serializer(tasks, many=True)
        return JsonResponse(serialized.data, safe=False, status=status.HTTP_200_OK)


class GetTasksThisMonthView(BaseGetView):
    model = Task
    serializer = TaskSerializer

    def get(self, request):
        today = timezone.now().date()
        start_of_month = today.replace(day=1)
        next_month = start_of_month.replace(month=start_of_month.month + 1, day=1)
        tasks = Task.objects.filter(start_date__gte=start_of_month, start_date__lt=next_month)
        serialized = self.serializer(tasks, many=True)
        return JsonResponse(serialized.data, safe=False, status=status.HTTP_200_OK)


class GetTasksThisYearView(BaseGetView):
    model = Task
    serializer = TaskSerializer

    def get(self, request):
        today = timezone.now().date()
        start_of_year = today.replace(month=1, day=1)
        next_year = start_of_year.replace(year=start_of_year.year + 1)
        tasks = Task.objects.filter(start_date__gte=start_of_year, start_date__lt=next_year)
        serialized = self.serializer(tasks, many=True)
        return JsonResponse(serialized.data, safe=False, status=status.HTTP_200_OK)


class PostTasksView(BasePostView):
    model = Task
    serializer = TaskSerializer


class DeleteTasksView(BaseDeleteView):
    model = Task


class PutTasksView(BasePutView):
    model = Task
    serializer = TaskSerializer


# Concrete views for 'employees' resource
class GetEmployeesView(BaseGetView):
    model = Employee
    serializer = EmployeeSerializer


class GetEmployeesByIdView(BaseGetView):
    model = Employee
    serializer = EmployeeSerializer

    def get(self, request, id):
        employees = Employee.objects.filter(emp_id=id)
        if CheckExistsClass().check_exists(employees):
            serialized = EmployeeSerializer(employees, many=True)
            return JsonResponse(serialized.data, safe=False, status=status.HTTP_200_OK)
        else:
            return errors['not_found']


class PostEmployeesView(BasePostView):
    model = Employee
    serializer = EmployeeSerializer


class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        emp = Employee.objects.filter(email=data['email'])
        if emp:
            if data['email'] == emp[0].email and check_password(data['password'], emp[0].password):
                return JsonResponse({'token': 'admin', 'username': emp[0].name},
                                    status=status.HTTP_202_ACCEPTED)
            if data['email'] == emp[0].email and not check_password(data['password'], emp[0].password):
                return JsonResponse({'token': 'invalid', 'username': 'WhoYou'},
                                    status=status.HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse({'token': 'invalid', 'username': 'WhoYou'},
                                status=status.HTTP_401_UNAUTHORIZED)
