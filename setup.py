from setuptools import setup

setup(
    name="bindtool",
    version="1.0",
    scripts=["bindtool.py"],
    entry_points={
        "console_scripts": [
            "bindtool = bindtool:BindTool.Run"
        ]
    }
)