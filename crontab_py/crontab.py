from typing import List
import subprocess
import re
import crontab_py._routing as r
from crontab_py.utils.errors import (
    InvalidCrontabError, 
    InvalidCronJobError, 
    InvalidCronJobIdError,
    InvalidCronJobIdAlreadyExistsError
)
from uuid import uuid4

class Crontab():
    """
    Crontab class to manage crontab jobs.
    
    example:\n
    from crontab_py import Crontab \n
    ct = Crontab()\n
    ct.add_job(
        cmd="echo 'hello world'",
        frequency="* * * * *",
        path_to_log="/tmp/crontab.log",
        id="my_job",
        description="my job"
    )

    """    
    def __init__(self) -> None:
        self._read_crontab()
        pass
    
    def _read_crontab(self) -> None:
        self.crontab = subprocess.getoutput("crontab -l 2>/dev/null")
    
    def _write_crontab(self) -> None:
        with open("tempfile", "w") as file:
            file.write(self.crontab)
        subprocess.run(["crontab", "tempfile"])
    
    def _check_id_in_crontab(self,id:str) -> bool:
        if id in self.crontab:
            return True
        else:
            return False
    def _check_format_id(self,id:str) -> bool:
        # Alphanumeric check with underscore and hyphen, no spaces
        regex = r"^[a-zA-Z0-9_-]+$"

        if re.match(regex, id):
            return False
        else:
            return True
    
    def _check_id(self,id:str) -> None:
        if self._check_id_in_crontab(id=id):
            raise InvalidCronJobIdAlreadyExistsError
        if self._check_format_id(id=id):
            raise InvalidCronJobIdError
    
    def _check_format_frequency(self,frequency:str) -> bool:
        # Alphanumeric check with underscore and hyphen, no spaces
        regex = r"^[0-9*\/,-]+$"

        if re.match(regex, frequency):
            return True
        else:
            return False
    
    def add_pyjob(
        self,
        path:str,
        frequency:str,
        path_to_log:str=None,
        path_requirements:str=None,
        id:str=None,
        description:str=None,
        *args, **kwargs) -> None:
        """add a python job to crontab

        Args:
            path (str): path to python script
            frequency (str): crontab frequency
            path_to_log (str, optional): path to log file if it needed. Defaults to None.
            path_requirements (str, optional): path to pip install - r, if exist generate a venv to execute the script. Defaults to None.
            id (str, optional): unic identifier for the job. Defaults to None.
            description (str, optional): description of the job. Defaults to None.
        """        
        #if path_requirements is not None then install requirements with env_generator.sh
        if path_requirements is not None:
            subprocess.run([r.PATH_GENERATE_ENV, r.PKG_NAME ,path_requirements])
            # subprocess.run([f"source {r.PKG_APP_ROOT}/.env/{r.PKG_NAME}/bin/activate"])
            python_path = f"{r.PKG_APP_ROOT}/.env/{r.PKG_NAME}/bin/python3"
        else:
            python_path = subprocess.getoutput("which python3")
        
        
        
        #build cmd string using args and kwargs
        cmd = f"{python_path} {path}"
        if args:
            cmd = f"{cmd} {' '.join(args)}"
        if kwargs:
            cmd = f"{cmd} {' '.join([f'--{k} {v}' for k,v in kwargs.items()])}"
        self.add_job(
            cmd=cmd,
            frequency=frequency,
            path_to_log=path_to_log,
            id=id,
            description=description
        )
        
    
    def add_job(
        self,
        cmd:str,
        frequency:str,
        path_to_log:str=None,
        id:str=None	,
        description:str=None) -> None:    
        """ Add a job to crontab

        Args:
            cmd (str): cmd to execute
            frequency (str): crontab frequency
            path_to_log (str, optional): path to log file if it needed. Defaults to None.
            id (str, optional): unic identifier for the job. Defaults to None.
            description (str, optional): description of the job. Defaults to None.
        """         
        if id is None:
            id = str(uuid4())
        if path_to_log is not None:
            cmd = f"{cmd} >> {path_to_log} 2>&1"
        
        self._check_id(id=id)
        self._check_format_frequency(frequency=frequency)
        
        job_str = f"""## crontab_py job
## id: {id}
## description: {description}
{frequency} {cmd}
"""
        self.crontab = "\n".join([self.crontab, job_str, ""])
        self._write_crontab()
        return None
    
    def remove_all(self) -> None:
        """
        Remove all jobs from crontab
        """        
        subprocess.run(["crontab", "-r"])
        self._read_crontab()
    
    def _list_crontab(self)->List:
        return [line for line in self.crontab.split("\n")]
    
    def remove_job(self,id:str) -> None:
        """remove a job from crontab by id
        not working yet

        Args:
            id (str): unic identifier for the job
        """        
        list_crontab=self._list_crontab()
        
        for line in list_crontab:
            pass
        
        self.crontab = "\n".join([line for line in self.crontab.split("\n") if id not in line])
        self._write_crontab()
        return None    
        