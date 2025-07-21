from flask import Flask, render_template, request, redirect, url_for
import json
import os

from src.config import load_config, save_config
from src.account import get_account_info
from src.campaign import load_campaigns, save_campaigns, search_campaigns, filter_campaigns_by_status, bulk_update_campaign_status
from src.adgroup import load_adgroups, save_adgroups, get_adgroups_by_campaign_id
from src.keyword import load_keywords, save_keywords, get_keywords_by_adgroup_id
from src.creative import load_creatives, save_creatives, get_creatives_by_adgroup_id

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/config', methods=['GET', 'POST'])
def config_page():
    if request.method == 'POST':
        api_config = {
            "api_key": request.form['api_key'],
            "api_secret": request.form['api_secret']
        }
        save_config('config/api_config.json', api_config)
        return redirect(url_for('config_page'))

    api_config = load_config('config/api_config.json')
    return render_template('config.html', api_config=api_config)

@app.route('/account')
def account_page():
    account_info = get_account_info()
    return render_template('account.html', account_info=account_info)

@app.route('/campaigns')
def campaigns_page():
    campaigns = load_campaigns('data/campaigns/campaigns.json')
    return render_template('campaigns.html', campaigns=campaigns)

@app.route('/adgroups/<int:campaign_id>')
def adgroups_page(campaign_id):
    adgroups = load_adgroups('data/adgroups/adgroups.json')
    adgroups = get_adgroups_by_campaign_id(adgroups, campaign_id)
    return render_template('adgroups.html', adgroups=adgroups, campaign_id=campaign_id)

@app.route('/keywords/<int:adgroup_id>')
def keywords_page(adgroup_id):
    keywords = load_keywords('data/keywords/keywords.json')
    keywords = get_keywords_by_adgroup_id(keywords, adgroup_id)
    return render_template('keywords.html', keywords=keywords, adgroup_id=adgroup_id)

@app.route('/creatives/<int:adgroup_id>')
def creatives_page(adgroup_id):
    creatives = load_creatives('data/creatives/creatives.json')
    creatives = get_creatives_by_adgroup_id(creatives, adgroup_id)
    return render_template('creatives.html', creatives=creatives, adgroup_id=adgroup_id)

if __name__ == '__main__':
    app.run(debug=True)
