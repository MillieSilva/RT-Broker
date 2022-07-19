# Deployment

Below are the steps to set up the broker environment, for production and debugging


## Debian Setup

### Installing Python
`apt install python3`

### Clone the repository
`git clone git@github.com:MillieSilva/RT-Broker.git`

### Install dependencies
`cd RT-Broker`

`pipenv shell && pipenv install`

### Running for Production or Debugging
To run in production `uwsgi uwsgi.ini`

To debug with flask's weizer server `python debug.py` (preferred entry main for debugging overall)


