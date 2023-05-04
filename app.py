from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/crawl')
def crawl():
    url = request.args.get('url')
    if not url:
        return 'Please provide a URL to crawl'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and not href.startswith('#'):
            links.append(href)

    return render_template('links.html', url=url, links=links)
