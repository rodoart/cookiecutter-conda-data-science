from cookiecutter.main import cookiecutter

from datetime import datetime

cookiecutter(
    'cookiecutter-conda-data-science',
    extra_context={'_timestamp': datetime.utcnow().isoformat()}
)