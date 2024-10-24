from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import  messages
from common import models
import traceback
from django.shortcuts import render, redirect
import os
from django.http import FileResponse, Http404
from django.conf import settings


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)



class HomeView(View):
    def get(self, request):

        return render(request, "index.html")

class NizomView(View):
    def get(self, request):

        return render(request, "nizom.html")

class SuccessView(View):
    def get(self, request):

        return render(request, "success.html")

class ErrorView(View):
    def get(self, request):

        return render(request, "error.html")




class FormView(View):
    def get(self, request):
        skill1 = models.StartAppCategory.objects.all()
        skill2 = models.Purposes.objects.all()
        
        context = {
            "skill1": skill1,
            "skill2": skill2,
        }
        return render(request, "forms.html", context)

    def post(self, request):
        print("++++++++++++++GOOOD+++++++++++++++++++++++++++")
        agree = request.POST.get("agree") == "True"

        # Extract data from the POST request
        data = {
            "name": request.POST.get("name"),
            "gender": request.POST.get("gender"),  # Fixed gender extraction
            "date": request.POST.get("date"),
            "address": request.POST.get("address"),
            "phonenumber": request.POST.get("phonenumber"),
            "startappname": request.POST.get("startappname"),
            "skills": request.POST.getlist("skills"),
            "anotherskill": request.POST.get("anotherskill"),  # Extract another skill
            "aboutstartapp": request.POST.get("aboutstartapp"),  # Extract about startapp
            "aboutteam": request.POST.get("aboutteam"),
            "skills2": request.POST.getlist("skills2"),
            "mvp": request.POST.get("mvp"),
            "startappimg": request.FILES.get("startappimg"),
            "startapppdf": request.FILES.get("startapppdf"),
        }

        # Print received data for debugging
        print("Data received from POST request:", data)

        try:
            registration = models.Registration(
                full_name=data["name"],
                gender=data["gender"],  # Ensure gender is saved correctly
                date_birth=data["date"],
                address=data["address"],
                phone=data["phonenumber"],
                startap_name=data["startappname"],
                another_category=data["anotherskill"],  # Save another skill
                about_startapp=data["aboutstartapp"],  # Save about startapp
                about_team=data["aboutteam"],
                project_prototype=data["mvp"],
                startap_image=data["startappimg"],
                presentation=data["startapppdf"],
                agree=agree
            )
            registration.save()

            registration.category.set(data["skills"])
            registration.purpose.set(data["skills2"])

            messages.success(request, 'Your message has been sent successfully!')
            return redirect("common:success")

        except Exception as e:
            print("Error occurred:", str(e))
            traceback.print_exc()
            messages.error(request, f'An error occurred: {str(e)}')  # Include the error message
            return redirect("common:error")
        
    # def post(self, request):
    #             print("++++++++++++++GOOOD+++++++++++++++++++++++++++") #BUG
    #             name = request.POST.get("name")
    #             gender = request.POST.get("gender")
    #             date = request.POST.get("date")
    #             address = request.POST.get("address")
    #             phonenumber = request.POST.get("phonenumber")
    #             startappname = request.POST.get("startappname")
    #             skills = request.POST.get("skills")
    #             anotherskill = request.POST.get("anotherskill")
    #             aboutteam = request.POST.get("aboutteam")
    #             skills2 = request.POST.get("skills2")
    #             mvp= request.POST.get("mvp")
    #             startappimg = request.POST.get("startappimg")
    #             startapppdf = request.POST.get("startapppdf")

    #             try:
    #              models.Registration.objects.create(full_name=name, gender=gender, date_birth=date, address=address, phone= phonenumber, startapp_name=startappname, category=skills,about_startapp=anotherskill, about_team = aboutteam, purpose = skills2,project_prototype=mvp, startap_image = startappimg, presentation = startapppdf )
    #              messages.add_message(request, messages.SUCCESS, 'Your message has been send bradar')
    #              return HttpResponseRedirect(reverse("common:home"))
    #             except Exception as e:
    #              messages.add_message(request, messages.WARNING, 'Error occured!')
    #              return HttpResponseRedirect(reverse("common:home"))



