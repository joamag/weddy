#!/usr/bin/python
# -*- coding: utf-8 -*-

import flickr
import appier
import appier_extras

class Instance(appier_extras.admin.Account):

    client_key = appier.field(
        index = True
    )

    client_secret = appier.field(
        private = True
    )

    oauth_token = appier.field(
        private = True
    )

    oauth_token_secret = appier.field(
        private = True
    )

    @classmethod
    def login(cls, username, password):
        account = super(Instance, cls).login(username, password)
        return account

    def get_api(self):
        instance = self.reload(rules = False)
        return flickr.Api(
            client_key = instance.client_key,
            client_secret = instance.client_secret,
            oauth_token = instance.oauth_token,
            oauth_token_secret = instance.oauth_token_secret
        )
