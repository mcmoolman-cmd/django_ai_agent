import os
import pathlib
import sys

NOTEBOOKS_DIR = pathlib.Path(__file__).parent
REPO_DIR = NOTEBOOKS_DIR.parent
DJANGO_PROJECT_ROOT=REPO_DIR / "src"
DJANGO_SETTINGS_MODULE = "cfehom.settings"

def init(verbose=False):
    # allow for nest_asuncio patch to allow for nested events in Jupyter

    try:
        import nest_asyncio

        if verbose:
            print("Applied nest_asyncio path for Jupyter")

    except ImportError:
        if verbose:
            print("nest_asyncio is not available, skipping patch")

    os.chdir(DJANGO_PROJECT_ROOT)
    sys.path.insert(0, str(DJANGO_PROJECT_ROOT))
    if verbose:
        print(f"Changed working directory to: {DJANGO_PROJECT_ROOT}")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = "true"

    import django

    django.setup()