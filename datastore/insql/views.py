from django.http import HttpResponse

from insql.models import Student


def home(request):
    return HttpResponse("ok")


def data(request):
    name = "maiyl"
    age = 23
    place = "kodathi gate"
    email = "mai@gon.com"
    score = 59
    # data = {name,age,score,email,place}
    std = Student(name, age, score, email, place)
    return HttpResponse(f"name:{name},age : {age} , place : {place} , email : {email} ,score : {score}")
