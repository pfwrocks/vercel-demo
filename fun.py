import os

def cron_job(request):
    # Accessing the secret stored in an environment variable
    secret = os.environ.get('MY_SECRET')

    # This is where you'd use the secret, but for demo purposes, we're just printing it
    return f"The secret is: {secret}"

# Vercel expects a WSGI application, so we need to wrap our function
from flask import Flask, request
app = Flask(__name__)

@app.route('/api/cron', methods=['GET'])
def cron_route():
    return cron_job(request)
