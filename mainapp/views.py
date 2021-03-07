import speedtest

from django.shortcuts import render, redirect
from django.http.response import HttpResponse


def redirect_home(reqest):
    return redirect('home_page')


def home_page(request):
    return render(request, 'mainapp/home.html')


def test_speed(request):
    st = speedtest.Speedtest()
    speed_data = {
        'download_speed': "{:.2f}".format(st.download() / 10 ** 6),
        'upload_speed': "{:.2f}".format(st.upload() / 10 ** 6),
        'ping': st.results.ping,
        'country': st.results.client['country'],
        'ip_address': st.results.client['ip'],
        'provider': st.results.client['isp'],
    }
    # speed_data = {
    #     'download_speed': 100.00,
    #     'upload_speed': 100.00,
    #     'ping': 10.00,
    #     'country': st.results.client['country'],
    #     'ip_address': st.results.client['ip'],
    #     'provider': st.results.client['isp'],
    # }
    return render(request, 'mainapp/test.html', speed_data)
