#!flask/bin/python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#---------------------------------------#
from flask import Flask                 #
from flask import jsonify,make_response #
from orumcek import Scraping            #
#---------------------------------------#

#-----------------------#
app = Flask(__name__)   #
#-----------------------#

# https://stackabuse.com/deploying-a-flask-application-to-heroku/

@app.route('/')
def index():
    return jsonify(Kurslar=Scraping(1))

@app.route('/<int:hangi_sayfa>', methods=['GET'])
def get_kullanici(hangi_sayfa):
    return jsonify(Kurslar=Scraping(hangi_sayfa))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'HTTP 404 Error': 'Aradığınız içerik mevcut değil. Lütfen isteğinizi kontrol edin.'}), 404)

#---------------------------------------------------#
if __name__ == '__main__':                          #
    app.config['JSON_AS_ASCII'] = False             #
    app.run(debug=True, host='0.0.0.0', port=5000)  #
#---------------------------------------------------#