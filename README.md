# Broker API (Remote Teller)
The Broker API is the application responsible for serving and keeping
track of Clients and Server connection information (such as IPv4,
Protocols, unique GUIDs)

It is used to dispatch data for valid connections from end to end,
acting as a middleman


## Setting up
To setup for development or production, check [Deployment](Docs/Deployment.md) steps

## Running in production
To run the broker for production, run the uwsgi server with:
`uwsgi uwsgi.ini`

