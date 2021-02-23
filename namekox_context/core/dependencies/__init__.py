#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals


from namekox_core.core.service.dependency import Dependency


class ContextHelper(Dependency):
    def __init__(self, *args, **kwargs):
        super(ContextHelper, self).__init__(*args, **kwargs)

    def get_instance(self, context):
        return context
