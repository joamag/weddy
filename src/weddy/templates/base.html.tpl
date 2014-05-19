{% extends "partials/layout.static.html.tpl" %}
{% block head %}
    {{ super() }}
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename = 'css/layout.css') }}" />
{% endblock %}
{% block links %}
    <a href="#">home</a>
    //
    <a class="active" href="#">sets</a>
    //
    <a href="#">about</a>
{% endblock %}
