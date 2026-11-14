# Copyright 2026 Intelligent Robotics Lab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Sphinx configuration of the MOCAP4ROS2 website."""

import time

project = 'MOCAP4ROS2'
author = 'Intelligent Robotics Lab and contributors'
copyright = f'2020-{time.strftime("%Y")}, {author}'
version = release = 'latest'  # scripts/build_site.py sets the real one

extensions = [
    'sphinx.ext.extlinks',
    'sphinx_copybutton',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = ['_build', '_site', 'scripts', 'README.md', 'venv']
source_suffix = '.rst'
master_doc = 'index'
language = 'en'

html_theme = 'shibuya'
html_title = 'MOCAP4ROS2'
html_favicon = 'images/favicon-48x48.png'
html_static_path = ['_static', 'images/mocap4r2_symbol_light.png',
                    'images/mocap4r2_symbol_dark.png', 'images/apple-touch-icon.png']
html_css_files = ['mocap4r2.css']
html_js_files = ['version_switcher.js', 'repo_cards.js']
html_baseurl = 'https://mocap4ros2-project.github.io/'
html_theme_options = {
    'accent_color': 'red',
    'light_logo': '_static/mocap4r2_symbol_light.png',
    'dark_logo': '_static/mocap4r2_symbol_dark.png',
    'github_url': 'https://github.com/MOCAP4ROS2-Project',
    'nav_links': [
        {'title': 'Get started', 'url': 'getting_started/index'},
        {'title': 'Systems', 'url': 'systems/index'},
        {'title': 'Guides', 'url': 'guides/index'},
        {'title': 'Tools', 'url': 'tools/index'},
        {'title': 'Developers', 'url': 'developer/index'},
    ],
    'globaltoc_expand_depth': 1,
}
html_context = {
    'source_type': 'github',
    'source_user': 'MOCAP4ROS2-Project',
    'source_repo': 'MOCAP4ROS2-Project.github.io',
    'source_version': 'main',
    'source_docs_path': '/',
}
html_show_sourcelink = False
html_last_updated_fmt = None

extlinks = {
    'repo': ('https://github.com/MOCAP4ROS2-Project/%s', '%s'),
}
copybutton_prompt_text = r'\$ '
copybutton_prompt_is_regexp = True
