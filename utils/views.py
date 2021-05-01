from django.shortcuts import render

# Create your views here.
def checkpaginator(self):
    if self.request.query_params.get("no_paginate") == "true":
        self.pagination_class = None