#!/usr/bin/env python3
"""Our first Flask application."""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Our front page for our Flask app."""
    return "Hello world!"


if (__name__ == "__main__"):
    app.run(debug=True)
