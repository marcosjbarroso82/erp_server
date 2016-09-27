#!/bin/bash
NAME="Erp"                                                              # Name of the application
ENVNAME=environment                                                             # Name of virtualenvi
DJANGODIR=/webapps/erp/erp_server                                      # Django project directory
SOCKFILE=/webapps/erp/erp_server/run/gunicorn.sock                     # we will communicte using this unix socket
USER=erp                                                                # the user to run as
GROUP=webapps                                                                   # the group to run as
NUM_WORKERS=3                                                                   # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=erp_server.settings                          # which settings file should Django use
DJANGO_WSGI_MODULE=erp_server.wsgi                                             # WSGI module name
    
# Activate the virtual environment
cd $DJANGODIR
source ../$ENVNAME/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
    
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
    
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=info \
  --log-file=-
