{% extends "base.html.tpl" %}
{% block title %}Sets{% endblock %}
{% block name %}Sets :: {{ photos.title }}{% endblock %}
{% block content %}
    <div class="photos">
        {% for photo in photos.photo %}
            <img src="http://farm{{ photo.farm }}.staticflickr.com/{{ photo.server }}/{{ photo.id }}_{{ photo.secret }}_m.jpg" />
        {% endfor %}
    </div>
{% endblock %}
