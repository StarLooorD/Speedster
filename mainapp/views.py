import speedtest

from django.shortcuts import render, redirect


def redirect_home(request):
    return redirect('home_page')


def home_page(request):
    return render(request, 'mainapp/home.html')


def collect_speed_data():
    st = speedtest.Speedtest()
    speed_data = {
        'download_speed': "{:.2f}".format(st.download() / 10 ** 6),
        'upload_speed': "{:.2f}".format(st.upload() / 10 ** 6),
        'ping': st.results.ping,
        'country': st.results.client['country'],
        'ip_address': st.results.client['ip'],
        'provider': st.results.client['isp'],
    }
    return speed_data


def do_test(request):
    speed_data = collect_speed_data()
    return render(request, 'mainapp/test.html', speed_data)
