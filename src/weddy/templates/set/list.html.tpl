{% extends "base.html.tpl" %}
{% block title %}Sets{% endblock %}
{% block name %}Sets{% endblock %}
{% block content %}
    <ul class="sets">
        {% for set in sets %}
            <li>
                <div class="name">
                    <a href="{{ url_for('set.photos', id = set.id) }}">{{ set.title._content }}</a>
                </div>
                <div class="description">
                    <span>{{ set.description._content|safe }}</span>
                </div>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
