import os
from flask import Flask, render_template,request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)

@app.route("/",methods = ["GET"])
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route('/review', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchstring = request.form["content"].replace(" ","")
            url = "https://www.flipkart.com/search?q=" + searchstring
            uClient = uReq(url)
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage,"html.parser")
            data = flipkart_html.find_all("div", {"class": "bhgxx2 col-12-12"})
            del data[0:3]
            filename = searchstring+".csv"
            fw = open(filename,"w")
            headers = "Model Name, Customer Name,Rating,Heading,Comment \n"
            reviews = []
            for i in data:
                try:
                    new_url = "https://www.flipkart.com" + (i.find("a", {"class": "_31qSD5"})["href"])
                    req_newurl_soup = bs(requests.get(new_url).content, "html.parser")
                except Exception as q:
                    print("The error is : ",q)
                    break
                try:
                    review_url = "https://www.flipkart.com" + (
                    req_newurl_soup.find("div", {"class": "swINJg _3nrCtb"}).find_parent().get("href"))
                    req_review_url_soup = bs(requests.get(review_url).content, "html.parser")
                    new_req = req_review_url_soup.find_all("div", {"class": "col _390CkK _1gY8H-"})
                except:
                    new_req = req_newurl_soup.find_all('div', {'class': 'col _39LH-M'})
                for j in new_req:
                    try:
                        model_name = i.find("div",{"class":"_3wU53n"}).text
                    except:
                        model_name = "no model name"
                        continue
                    try:
                        rating = j.div.div.text
                    except:
                        rating = "No Rating"
                    try:
                        review_header = j.find("p",{"class":"_2xg6Ul"}).text
                    except:
                        review_header = "No Review Header"
                    try:
                        detailed_review = j.find("div",{"class":"qwjRop"}).div.div.text
                    except:
                        detailed_review = "No Review"
                    try:
                        custmer_name = j.find("p",{"class":"_3LYOAd _3sxSiS"}).text
                    except:
                        custmer_name = "No Name"
                    mydict = {"Model Name":model_name,"Customer Name":custmer_name,"Rating":rating,"Heading":review_header,"Comment":detailed_review}
                    reviews.append(mydict)
            return render_template("results.html",reviews=reviews[0:(len(reviews) - 1)])
        except Exception as e:
            print("The Exception message is: ",e)
            return "Something is wrong"
    else:
        return render_template('index.html')

port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=port)  # for cloud deployment




