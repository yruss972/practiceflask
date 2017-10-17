import copy
import config as cfg
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/<path:route>')
def catch_all(route=''):
    navitems=copy.deepcopy(cfg.SITE_NAVITEMS)
    for item in navitems:
        if item['route'] == route:
            item['active']=True
        else:
            item['active']=False
        item['href']='/'+item['route']    
        
        template=(route or 'index')+'.html'

        return render_template([route+'.html','404.html'], route=route, title=cfg.SITE_TITLE, navitems=navitems)