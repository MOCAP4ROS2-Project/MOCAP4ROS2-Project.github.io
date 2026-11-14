#!/usr/bin/env python3
# Copyright 2026 Intelligent Robotics Lab
"""Build the versioned website in _site/: one Sphinx build per entry of versions.json.

_site/<version>/   each version, built from its git ref (HEAD: the working tree)
_site/index.html   redirect to the default version
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / '_site'
# Copied into older versions so that they show the current selector too.
SELECTOR = [pathlib.Path('_static/version_switcher.js'), pathlib.Path('_static/mocap4r2.css')]

REDIRECT = '''<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>MOCAP4ROS2</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={url}">
<script>window.location.replace("{url}" + window.location.hash);</script>
</head><body><a href="{url}">{url}</a></body></html>
'''


def run(*cmd, cwd=ROOT):
    subprocess.run(cmd, cwd=cwd, check=True)


def build(src, out, version):
    tags = ['-t', 'latest'] if version == 'latest' else []
    run(sys.executable, '-m', 'sphinx', '-q', '-W', '--keep-going', *tags, '-b', 'html',
        '-D', f'version={version}', '-D', f'release={version}', str(src), str(out))


def main():
    versions = json.loads((ROOT / 'versions.json').read_text())
    shutil.rmtree(SITE, ignore_errors=True)
    SITE.mkdir()
    for v in versions['versions']:
        out = SITE / v['name']
        print(f"== {v['name']} ({v['ref']})", flush=True)
        if v['ref'] == 'HEAD':
            build(ROOT, out, v['name'])
            continue
        with tempfile.TemporaryDirectory() as tmp:
            src = pathlib.Path(tmp) / 'src'
            run('git', 'worktree', 'add', '--detach', str(src), v['ref'])
            try:
                for f in SELECTOR:
                    (src / f).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(ROOT / f, src / f)
                build(src, out, v['name'])
            finally:
                run('git', 'worktree', 'remove', '--force', str(src))
    default = versions['default']
    (SITE / 'index.html').write_text(REDIRECT.format(url=f'/{default}/'))
    shutil.copy(ROOT / 'versions.json', SITE / 'versions.json')
    (SITE / '.nojekyll').touch()
    print(f'Site in {SITE} (default: {default})')


if __name__ == '__main__':
    main()
