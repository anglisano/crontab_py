from typing import List
import subprocess
import re
import _routing as r
from utils.errors import (
    InvalidCrontabError, 
    InvalidCronJobError, 
    InvalidCronJobIdError,
    InvalidCronJobIdAlreadyExistsError
)
from uuid import uuid4

class Crontab():
    
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
        subprocess.run(["crontab", "-r"])
        self._read_crontab()
    
    def _list_crontab(self)->List:
        return [line for line in self.crontab.split("\n")]
    
    def remove_job(self,id:str) -> None:
        
        list_crontab=self._list_crontab()
        
        for line in list_crontab:
            pass
        
        self.crontab = "\n".join([line for line in self.crontab.split("\n") if id not in line])
        self._write_crontab()
        return None    
        
# if __name__ == "__main__":
#     ct=Crontab()
#     ct.crontab
#     ct.add_pyjob(path="/app/tests/resources/pr.py",frequency="* * * * *",path_to_log="/app/a.txt",id="testpy",path_requirements="/app/requirements-dev.txt")
#     # ct.add_pyjob(path="/app/tests/resources/pr.py",frequency="* * * * *",1,2)

#     ct.add_job(cmd="cd /app && ls",frequency="* * * * *",path_to_log="/app/a.txt",id="testid1",description="test")
    
#     ct.remove_job(id="testid1")
    
#     ct.remove_all()
    
## cronR job
## id:   COMPASS_PUBLI
## tags: 
## desc: genera tabla COMPASS_PUBLI
## 1 9,16 * * 1-5 /opt/R/3.5.0/lib/R/bin/Rscript '/home/Operaciones_cron_R/cron_r/executable/COMPASS_PUBLI.R'  >> '/Analitycs/OPERACIONES/LOG_CRON_R/COMPASS_PUBLI.log' 2>&1