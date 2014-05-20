{% extends "base.html.tpl" %}
{% block title %}Home{% endblock %}
{% block name %}{{ own.description }}{% endblock %}
{% block content %}
    <div class="quote">
        {{ own.description }} is a new simplified version of the flickr visualization process for people that like control.
        This beast is written <strong>only in python</strong>.
    </div>
{% endblock %}
