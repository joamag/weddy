#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import abstract

class SetController(abstract.AbstractController):

    @appier.route("/sets", "GET")
    @appier.private
    def list(self):
        url = self.ensure_api()
        if url: return self.redirect(url)
        api = self.get_api()
        sets = api.list_sets()
        return self.template(
            "set/list.html.tpl",
            area = "sets",
            sets = sets
        )
