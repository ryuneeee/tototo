# -*- coding: utf-8 -*-
from datetime import datetime
import re

from jinja2 import evalcontextfilter, escape, Markup
from tototo import config, app

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')


@app.template_filter()
def localtime_format(value: datetime, fmt: str):
    return value.astimezone(config.TIMEZONE).strftime(fmt)


@app.template_filter()
@evalcontextfilter
def nl2br(ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') for p in _paragraph_re.split(escape(value)))
    if ctx.autoescape:
        result = Markup(result)
    return result
