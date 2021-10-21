#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, task
import os

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "Algorithms-Visualizer"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("coverage_break_build", False)

@task
def run(project):
    os.chdir("./src/main/python")
    os.system("python3 main.py")