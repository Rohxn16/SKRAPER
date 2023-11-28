from app import app
from flask import render_template
from app.scraper import scrapeCodeforces

# getting all the upcoming contests first while the server loads in order to not fetch it until reload
CODEFORCES = len(scrapeCodeforces.fetchCodeforces())


@app.route('/')
def home():
    return render_template('index.html',page=' - HOME')

@app.route('/compete')
def compete():

    return render_template('compete.html',codeforces_contests=CODEFORCES, page=' - COMPETE')

@app.route('/compete/codeforces')
def codeforces():
    contestlist = scrapeCodeforces.fetchCodeforces()
    return render_template('codeforces.html', contestlist=contestlist)

@app.route('/compete/codechef')
def codechef():
    return render_template('codechef.html')

@app.route('/compete/leetcode')
def leetcode():
    return render_template('leetcode.html')

@app.route('/compete/atcoder')
def atcoder():
    return render_template('atcoder.html')

@app.route('/compete/topcoder')
def topcoder():
    return render_template('topcoder.html')

@app.route('/compete/spoj')
def spoj():
    return render_template('spoj.html')

@app.route('/compete/hackerearth')
def hackerearth():
    return render_template('hackerearth.html')

@app.route('/compete/hackerrank')
def hackerrank():
    return render_template('hackerrank.html')
