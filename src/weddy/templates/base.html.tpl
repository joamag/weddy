{% extends "partials/layout.static.html.tpl" %}
{% block htitle %}{{ own.description }} / {% block title %}{% endblock %}{% endblock %}
{% block head %}
    {{ super() }}
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename = 'css/layout.css') }}" />
{% endblock %}
{% block links %}
    {{ menu_link("home", url_for("base.index")) }}
    //
    {{ menu_link("sets", url_for("set.list")) }}
    //
    {{ menu_link("about", url_for("base.about")) }}
{% endblock %}
