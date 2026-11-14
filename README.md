# MOCAP4ROS2 website

Sources of https://mocap4ros2-project.github.io (Sphinx, Shibuya theme). Pushes to
`main` and tags build every version listed in `versions.json` and publish them to
`gh-pages` (`.github/workflows/publish.yml`).

```bash
python3 -m venv venv && venv/bin/pip install -r requirements.txt
venv/bin/python scripts/build_site.py      # all versions into _site/
venv/bin/python -m http.server -d _site    # http://localhost:8000
```

To add a released version, tag this repository (e.g. `2.0.0`) and add it to
`versions.json`.
