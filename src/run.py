#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
run.py
Description:

Author: PhatLuu
Contact: tpluu2207@gmail.com
Created on: 2021/07/06
"""

#%%
# ================================IMPORT PACKAGES====================================

from livereload import Server

# Custom Packages
from webUI import create_app


app = create_app()

if __name__ == "__main__":
    # app.run(debug=app.config.get("DEBUG"))
    server = Server(app.wsgi_app)
    server.serve()
