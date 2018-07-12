# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Post


class PostTests(TestCase):
    """
    defining the tests that'll run
    against the Post model
    """

    def test_str(self):
        test_title = Post(title='My latest blog post')
        self.assertEqual(str(test_title),
                         'My latest blog post')
