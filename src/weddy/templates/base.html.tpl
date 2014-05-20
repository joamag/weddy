{% extends "partials/layout.static.html.tpl" %}
{% block head %}
    {{ super() }}
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename = 'css/layout.css') }}" />
{% endblock %}
{% block links %}
    {{ menu_link("home") }}
    //
    {{ menu_link("sets") }}
    //
    {{ menu_link("about") }}
{% endblock %}
