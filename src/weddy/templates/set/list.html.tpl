{% extends "base.html.tpl" %}
{% block title %}sets{% endblock %}
{% block name %}Sets{% endblock %}
{% block content %}
    <ul class="repos">
        {% for set in sets.photosets.photoset %}
            <li>
                <div class="name">
                    <a href="#">{{ set.title._content }}</a>
                </div>
                <div class="description">
                    <span>{{ set.description._content|safe }}</span>
                </div>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
