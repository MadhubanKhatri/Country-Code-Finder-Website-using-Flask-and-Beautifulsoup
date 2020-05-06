from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        country_name = request.form.get('country_name')
        url = "https://countrycode.org/"+country_name
        r = requests.get(url)
        data = r.content
        soup = BeautifulSoup(data,'html.parser')
        h2 = soup.find_all('h2',class_="text-center")[0].get_text()
        h3 = soup.find_all('h3',class_="text-center")[0].get_text()
        h4 = soup.find_all('h4', class_="text-center")[0].get_text()
        return render_template("flask_countryCode.html", country_name=country_name,h2=h2,h3=h3,h4=h4)
    return render_template("flask_countryCode.html")


app.run(debug=True)