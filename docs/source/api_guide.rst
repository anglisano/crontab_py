API Guide
=========

Model Class
-----------

.. automodule:: crontab_py.crontab
   :members: Crontab

   ct=Crontab()

   # reboot every day at 00:00
   ct.add_job(
      cmd='sudo reboot',
      frequency='0 0 * * *',
      path_to_log='/var/log/crontab.log',
      id='reboot',
      description='Reboot every day at 00:00'
   )

   cr.remove_all()
