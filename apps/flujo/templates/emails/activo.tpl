{% extends "mail_templated/base.tpl" %}

{% block subject %}
    bienvenido
{% endblock %}

{% block html %}
    <h6>{{nombre}}</h6>
    correo de pruebas enviado a  de edad {{edad}}
{% endblock %}