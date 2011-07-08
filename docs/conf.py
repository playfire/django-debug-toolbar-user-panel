project = 'django-debug-toolbar-user-panel'
version = ''
release = ''
copyright = '2010, 2011 UUMC Ltd.'

html_logo = 'playfire.png'
html_theme = 'nature'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']
html_title = "%s documentation" % project
master_doc = 'index'
exclude_trees = ['_build']
templates_path = ['_templates']
latex_documents = [
  ('index', '%s.tex' % project, html_title, u'Playfire', 'manual'),
]
intersphinx_mapping = {'http://docs.python.org/': None}
