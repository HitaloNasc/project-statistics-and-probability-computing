import subprocess


def install_dependencies():
    subprocess.run(['pip', 'install', 'numpy'])
    subprocess.run(['pip', 'install', 'scipy'])
    subprocess.run(['pip', 'install', 'matplotlib'])
