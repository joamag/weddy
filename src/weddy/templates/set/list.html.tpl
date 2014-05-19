{% extends "base.html.tpl" %}
{% block title %}sets{% endblock %}
{% block name %}Sets{% endblock %}
{% block content %}
    <div class="quote">
        We're only showing your public repositories below, you can find your private projects on GitHub.<br/>
        Enable your projects below by flicking the switch.
    </div>
    <ul class="repos">
        {% for set in sets %}
            <li>
                <a href="#">{{ set }}</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
