from django.shortcuts import render
from django.views.generic import View


class Gettrains(View):
    def get(self,request):
        return render(request,"index.html")
    def post(self,request):
        tr=request.POST.get("train_search")

        import requests

        url = "https://trains.p.rapidapi.com/"

        payload = "{\"search\":\""+tr+"\"}"
        headers = {
            'x-rapidapi-host': "trains.p.rapidapi.com",
            'x-rapidapi-key': "ffc135b1d6msh48ed5e2971128a5p1f3e65jsn0408bb956706",
            'content-type': "application/json",
            'accept': "application/json"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        train_info = response.json()
        return render(request, "index.html", {"data": train_info})