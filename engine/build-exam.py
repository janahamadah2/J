#!/usr/bin/env python3
"""Build the Mastery Study Guide and then the drill from one config.

    python3 engine/build-exam.py exams/cvs-mid2/config-cvs-mid2.json

Both pages carry the same Read me (engine/readme-study-system.html).
When either page changes, rebuild with this script and republish both.
"""
import importlib.util
import os
import sys

ENGINE = os.path.dirname(os.path.abspath(__file__))


def mod(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), os.path.join(ENGINE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    mod("build-guide").build(sys.argv[1])
    mod("build-drill").build(sys.argv[1])
