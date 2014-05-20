{% set style = "full" %}
{% extends "base.html.tpl" %}
{% block title %}Sets{% endblock %}
{% block name %}Sets :: {{ photos.title }}{% endblock %}
{% block content %}
    <div class="photos">
        {% for photo in photos.photo %}
            <img class="image photo"
                 src="http://farm{{ photo.farm }}.staticflickr.com/{{ photo.server }}/{{ photo.id }}_{{ photo.secret }}_m.jpg"
                 data-lightbox_path="http://farm{{ photo.farm }}.staticflickr.com/{{ photo.server }}/{{ photo.id }}_{{ photo.secret }}_b.jpg" />
        {% endfor %}
    </div>
    {% if photos.pages > 1 %}
        {{ paging(photos.page|int, photos.pages, caller = pager) }}
    {% endif %}
{% endblock %}
