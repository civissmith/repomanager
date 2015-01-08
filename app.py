#!/usr/bin/python -B
################################################################################
# Copyright (c) 2015 Phil Smith
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
################################################################################
################################################################################
# @Title: app.py
#
# @Author: Phil Smith
#
# @Date: Wed, 07-Jan-15 05:28PM
#
# @Project: Flask Repo Manager
#
# @Purpose: Flask-based web app to manage a remote source control server.
#           
#
#
################################################################################
import flask as fl
import flask.views as fv

app = fl.Flask(__name__)

# Set the temporary secret key
app.secret_key = "FOO"

class Landing( fv.MethodView ):
  """
  The Landing view is responsible for handling the splash page or site
  landing page.
  """
  def get(self):
    return fl.render_template('landing.html')

  def post(self):
    pass

class Auth( fv.MethodView ):
  """
  The Auth view is responsible for handling user authentication (login/logout).
  """
  def get(self):
    return "Auth"

  def post(self):
    pass


class Repo( fv.MethodView ):
  """
  The Repo view is responsible for handling the repository management functions.
  """
  def get(self):
    return "Repo"
  def post(self):
    pass


# Add URL rules so the app can navigate.
app.add_url_rule('/', view_func=Landing.as_view('landing'))
app.add_url_rule('/auth/', view_func=Auth.as_view('auth'))
app.add_url_rule('/repo/', view_func=Repo.as_view('repo'))

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
