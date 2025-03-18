from django.http import HttpResponse
import os
import datetime
import subprocess

def htop(request):
    name = "Your Full Name"
    username = os.getlogin()
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    response = f"""
    <h1>System Info</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response)
