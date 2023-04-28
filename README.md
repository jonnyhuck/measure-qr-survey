# measure-qr-survey
Simple Flask-based survey to collect info on deer and ticks in parks

To run local dev server:
```bash
cd application
export FLASK_APP=survey && export FLASK_DEBUG=true && flask run
```

To run prod server (from `/measure-qr-survey/applicaton`)

```bash
gunicorn3 -w 5 survey:app
```

This is `[filename]:[variable name for Flask instance]`

Check nginx

```bash
systemctl status nginx
```

---

## Configure Supervisor
Supervisor is a client/server system that allows its users to monitor and control a number of processes on UNIX-like operating systems. Supervisor is great for auto-reloading gunicorn if it crashes or if your Linode is rebooted unexpectedly.
1. Install Supervisor
```bash
sudo apt install supervisor
```
2. Create a Supervisor program
```bash
sudo nano /etc/supervisor/conf.d/flaskapp.conf
```
```
[program:flaskapp]
directory=/home/flask_app_project/measure-qr-survey/applicaton
command=gunicorn3 -w 5 survey:app
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/flaskapp/flaskapp.err.log
stdout_logfile=/var/log/flaskapp/flaskapp.out.log
```
2. create your log files
```bash
sudo mkdir /var/log/flaskapp
touch /var/log/flaskapp/flaskapp.out.log
touch /var/log/flaskapp/flaskapp.err.log
```

3. Reload Supervisor to apply changes
```bash
sudo supervisorctl reload
```

Stop Supervisor

```bash
sudo supervisorctl stop all
```

If you get an error like this:



It means supervisor is not running - do this:

```bash
service supervisor start
```

## Refs

https://www.linode.com/docs/products/tools/marketplace/guides/flask/

https://www.linode.com/docs/guides/flask-and-gunicorn-on-ubuntu/

https://github.com/abalarin/Flask-on-Linode/blob/master/FlaskDeployment.md
