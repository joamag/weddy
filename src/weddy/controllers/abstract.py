#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import weddy

class AbstractController(appier.Controller):

    def ensure_api(self):
        instance = weddy.Instance.from_session(rules = False)
        if not instance.oauth_temporary and instance.oauth_token and\
            instance.oauth_token_secret: return
        instance.invalidate_s()
        api = self.get_api()
        url = api.oauth_authorize(state = self.request.location)
        instance.tokens_s(
            api.oauth_token,
            api.oauth_token_secret,
            temporary = True
        )
        return url

    def get_api(self, redirect_url = None):
        instance = weddy.Instance.from_session(rules = False)
        redirect_url = redirect_url or self.url_for("base.oauth", absolute = True)
        return instance.get_api(redirect_url = redirect_url)
