from flask import Blueprint, render_template, request, flash, jsonify, make_response
from . import db
import json
from .typingdna import send_typing_data

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/typing-patterns')
def typing_patterns():
    return render_template("typing_patterns.html")

@views.route('/typingdna', methods=["POST"])
def typingdna():
    data = request.get_json()
    pattern = data.get("pattern")
    user_id = data.get("user_id")
    response = send_typing_data(user_id, pattern)
    print(response)
    return make_response(jsonify(response), 200)

