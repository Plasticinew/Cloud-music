from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

bp = Blueprint("bank", __name__)


@bp.route("/", methods=("GET", "POST"))
def index(page=None):
    cont = [['aa', 'aaa', '100'],
            ['bb', 'bbb', '1000'],
            ['cc', 'ccc', '10000']
            ]

    return render_template("index.html", owned=1, songlist=cont)


@bp.route("/link<int:index>", methods=('GET', 'POST'))
def link(index):
    cont = [['aa', 'aaa', '100', '111', '3423', '3223'],
            ['bb', 'bbb', '1000', 'bb', 'bbb', '1000'],
            ['cc', 'ccc', '10000', 'cc', 'ccc', '10000']
            ]
    return render_template("link.html", songlistlist=cont)


@bp.route("/detail<int:index>", methods=('GET', 'POST'))
def detail(index):
    cont = ['aa', 'aaa', '100']
    cmtlist = [['a', 'svfdvd'], ['b', 'sbrbfsvf'], ['c', 'aeveaVdv'], ['d', 'agegvgafvg']]

    return render_template("detail.html", cont=cont, cmtlist=cmtlist)
