


class InvalidCrontabError(Exception):
    """Raised when the crontab is invalid"""
    pass

class InvalidCronJobError(Exception):
    """Raised when the cron job is invalid"""
    pass

class InvalidCronJobIdError(Exception):
    """Raised when the cron job id is invalid"""
    pass

class InvalidCronJobIdAlreadyExistsError(Exception):
    """Raised when the cron job id already exists"""
    pass

class InvalidCronJobFrequencyError(Exception):
    """Raised when the cron job frequency is invalid"""
    pass