{% extends "base.html.tpl" %}
{% block title %}repos{% endblock %}
{% block name %}Repos{% endblock %}
{% block content %}
    <div class="quote">
        We're only showing your public repositories below, you can find your private projects on GitHub.<br/>
        Enable your projects below by flicking the switch.
    </div>
    <ul class="repos">
        {% for repo in repos %}
            <li>
                <a href="{{ repo.html_url }}">{{ repo.full_name }}</a>
                {% if repo.status %}
                    <input class="button float-right" type="checkbox" name="{{ repo.full_name}}" checked="1"
                           data-link="{{ url_for('repo.disable', id = repo.id) }}" />
                {% else %}
                    <input class="button float-right" type="checkbox" name="{{ repo.full_name}}"
                           data-link="{{ url_for('repo.enable', id = repo.id) }}" />
                {% endif %}
                <div class="clear"></div>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
