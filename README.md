# Crontab_py

## Introduction
Crontab_py is a Python module designed to simplify the management of cron jobs. It enables easy addition, removal, and listing of scheduled tasks.

## Example
```python
from crontab_py import Crontab

ct = Crontab()
ct.add_job(
    cmd="echo 'hello world'",
    frequency="* * * * *",
    path_to_log="/tmp/crontab.log",
    id="my_job",
    description="my job"
)
```

## Sphinx Documentation
Explore the [complete documentation](https://anglisano.github.io/crontab_py/) for detailed usage instructions and advanced features.

## Get Started
For installation and additional details, refer to the [official website](https://anglisano.github.io/crontab_py/) or check out the [API Guide](https://anglisano.github.io/crontab_py/api_guide.html).

Feel free to contribute, report issues, or suggest improvements by [raising an issue](https://github.com/anglisano/crontab_py/issues) 
