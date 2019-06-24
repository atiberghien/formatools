from django.shortcuts import render
from django.views.generic import FormView
from django_weasyprint import WeasyTemplateResponseMixin
from .forms import SololearnAccountsForm
from collections import OrderedDict
from bs4 import BeautifulSoup
import csv
import io

import requests

class SololearnAccountFormView(FormView):
    form_class = SololearnAccountsForm
    http_method_names = ['post', 'head', 'options']
    template_name = "sololearn_extract/extract.html"
    pdf_filename = 'sololearn.pdf'

    def get_context_data(self, **kwargs):
        context = FormView.get_context_data(self, **kwargs)
        
        form = context["form"]
        context["headers"] = ("username", "level", "xp", "courses", "certificates")#, "achievements")
        context["rows"] = []
        for url in form.cleaned_data["account_list"].split('\n'):
            resp = requests.get(url.strip())
            html_soup = BeautifulSoup(resp.text, 'html.parser')
            try:
                username = list(html_soup.select_one("div.userProfile .details .name").stripped_strings)[0]
                level = list(html_soup.select_one("div.userProfile .details .detail div").stripped_strings)[1]
                xp = html_soup.select_one("div.userProfile .details .detail div:nth-child(2) span").text.replace(" XP", "")
                courses = ", ".join(["%s (%s)" % (course.select_one('a')["title"].split(' ')[0], course.select_one('.courseXp').string) for course in html_soup.select("div.userCourses .courseWrapper")])
                certificates = ", ".join(["%s (%s)" % (certif["title"], " ".join(list(certif.select_one(".details .date").stripped_strings))) for certif in html_soup.select("#certificates .certificate")])
                # achievements = ", ".join(["%s (%s)" % (achiev["title"], " ".join(list(achiev.select_one(".description").stripped_strings))) for achiev in html_soup.select(".userAchievements.full .achievement:not(.disabled)")])
                context["rows"].append((username, level, xp, courses, certificates))#, achievements))
            except:
                print("ERROR", url.strip())
            # break
        return context
        
    def form_valid(self, form):
        return FormView.render_to_response(self, self.get_context_data(form=form))

    def form_invalid(self, form):
        return FormView.render_to_response(self, self.get_context_data(form=form))

