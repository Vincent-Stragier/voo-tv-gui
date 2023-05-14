""" Compile the recipe for the remote."""
import locale
import os
import shutil
import subprocess
import time


def generate_version_information():
    """ Generate the version token and the date taken for this repository. """
    # Get repo information
    try:
        import git
        repo = git.Repo(search_parent_directories=True)
        url = repo.remotes.origin.url.split('.git')[0]
        sha = repo.head.object.hexsha
    except Exception:
        sha = 'none'
        url = ('https://github.com/vincent-stragier/')

    date = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.gmtime())

    return date, sha, url


def run_command(command):
    """ Run the command and directly output to the console. """
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(output.decode(locale.getdefaultlocale()[1]), end='')
    return process.poll()


if __name__ == '__main__':
    # Go to the root directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    python_version = '-3.11'
    run_command(['py', python_version, '-m', 'pip', 'install',
                '-r', 'build_requirements.txt'])
    VERSION_DATE, VERSION_HASH, VERSION_URL = generate_version_information()
    name = f'Télécommande VOO .évasion ({VERSION_DATE.replace(":", "-")})'

    print('Install GUI dependencies...')
    run_command(['py', python_version, '-m', 'pip', 'install',
                '-r', './src/requirements.txt'])

    print('Generate GUI code...')
    run_command(['py', python_version, './src/ui_to_py_converter.py',
                './src/remote_ui.ui', './src/remote_ui.py'])
    run_command(['py', python_version, './src/ui_to_py_converter.py',
                './src/settings.ui', './src/settings_ui.py'])

    print('Compile GUI code...')
    run_command(['py', python_version, '-m', 'PyInstaller', '-F', '--workpath',
                 './', '--distpath', './', '--specpath', './src/build',
                 '--clean', '--add-data', '../package_data;package_data',
                 '-n', name, '--windowed', '--icon=../package_data/icon.ico',
                 '--additional-hooks-dir=./src/hooks',
                 './src/remote.pyw'])

    print('Partially clean the build...')
    shutil.rmtree(name)
