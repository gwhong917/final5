# -*- encoding: utf-8 -*-


from calendar import month
from time import time
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import folium
from .models import Post
from django.shortcuts import render
# from image import Post


# @login_required(login_url="/login/")
# def dashboard(request):
#     chart = Post.objects.all()
#     # jan = chart.filter(time__range=["2022-01-01", "2022-01-31"]).count()
#     # feb = chart.filter(time__range=["2022-02-01", "2022-03-01"]).count()
#     # mar = chart.filter(time__range=["2022-03-02", "2022-03-31"]).count()
#     # apr = chart.filter(time__range=["2022-04-01", "2022-04-30"]).count()
#     # may = chart.filter(time__range=["2022-05-01", "2022-05-31"]).count()
#     # jun = chart.filter(time__range=["2022-06-01", "2022-06-30"]).count()
#     # jul = chart.filter(time__range=["2022-07-01", "2022-07-31"]).count()
#     # aug = chart.filter(time__range=["2022-08-01", "2022-08-31"]).count()
#     # sep = chart.filter(time__range=["2022-09-01", "2022-09-30"]).count()
#     # oct = chart.filter(time__range=["2022-10-01", "2022-10-31"]).count()
#     # nov = chart.filter(time__range=["2022-11-01", "2022-11-30"]).count()
#     # dec = chart.filter(time__range=["2022-12-01", "2022-12-31"]).count()
    
#     jan = chart.filter(time__year = '2022', time__month='01').count()
#     feb = chart.filter(time__year = '2022', time__month='02').count()
#     mar = chart.filter(time__year = '2022', time__month='03').count()
#     apr = chart.filter(time__year = '2022', time__month='04').count()
#     may = chart.filter(time__year = '2022', time__month='05').count()
#     jun = chart.filter(time__year = '2022', time__month='06').count()
#     jul = chart.filter(time__year = '2022', time__month='07').count()
#     aug = chart.filter(time__year = '2022', time__month='08').count()
#     sep = chart.filter(time__year = '2022', time__month='09').count()
#     oct = chart.filter(time__year = '2022', time__month='10').count()
#     nov = chart.filter(time__year = '2022', time__month='11').count()
#     dec = chart.filter(time__year = '2022', time__month='12').count()

#     monthly_chart = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
#     context = {'monthly_chart': monthly_chart}
#     return render(request, "home/index.html", context)


# @login_required(login_url="/login/")
# def ui_maps(request):
#     map23 = folium.Map(location=[37,126], zoom_start=7)
#     maps = map23._repr_html_()
#     # table_log = Post.objects.all()
#     # context = {'table_log': table_log}

#     return render(request, "home/ui-maps.html", {'maps':maps})


@login_required(login_url="/login/")
def ui_tables(request):
    table_log = Post.objects.all()
    context = {'table_log': table_log}

    return render(request, "home/ui-tables.html", context)


@login_required(login_url="/login/")
def index(request):
    chart = Post.objects.all()

    #월별 카운트
    jan = chart.filter(time__year = '2022', time__month='01').count()
    feb = chart.filter(time__year = '2022', time__month='02').count()
    mar = chart.filter(time__year = '2022', time__month='03').count()
    apr = chart.filter(time__year = '2022', time__month='04').count()
    may = chart.filter(time__year = '2022', time__month='05').count()
    jun = chart.filter(time__year = '2022', time__month='06').count()
    jul = chart.filter(time__year = '2022', time__month='07').count()
    aug = chart.filter(time__year = '2022', time__month='08').count()
    sep = chart.filter(time__year = '2022', time__month='09').count()
    oct = chart.filter(time__year = '2022', time__month='10').count()
    nov = chart.filter(time__year = '2022', time__month='11').count()
    dec = chart.filter(time__year = '2022', time__month='12').count()

    monthly_chart = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    
    context = {
        'segment': 'index',
        'monthly_chart': monthly_chart
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.

    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

