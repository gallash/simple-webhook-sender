# Simple Webhook Sender
This is a Python project

## Description

This project aims to be a quick and simple way to send webhooks to webhook receivers with pre-established messages. It also works well when imported via another Python project that would deal with business logic and calling the sender using `os.system`

This Webhook sender allows two modes of sending HTTP messages in JSON: 

1. To the local server (by default it is the Flask's development server, http://127.0.0.1:5000/);

2. To the specified URL. E.g., webhook.site, your own webhook receiver's URL.

If a custom message is desired, you can modify the hardcoded as needed.
Further modifications allowing connection to Database are on the plans. These modifications would make possible sending webhooks to several webhook receivers in sequence, without the need of writing them on the terminal every single time. 

## Getting started 
The simplest way to use it, for testing, is straight from the terminal. Open up the terminal inside the project's home directory and activate the virtual environment:

```bash
source venv/bin/activate
``` 

Install dependencies declared in `requirements.txt` by using:

```bash
pip3 install -r requirements.txt
```

## How to use it
Next, run the Python script:

1. To the local server
Run the Webhook receiver. If it is built on top of Flask, it will probably have the port as hardcoded in the Python script. If it was not built using Flask, inspection of the port in which it operates will be required [here, jump to number 2 (specified URL)].

With the Flask receiver, no URL is needed to be passed. Simply run, in the terminal:

```bash
python webhook\_sender.py
```

Now, check the terminal that runs the receiver, the JSON message should appear there, containing the hardcoded message.

2. To the specified URL
Simply paste the URL to be connected to after the `-u` or `--url` flag:

```bash
python webhook\_sender.py --url \<insert URL here>
```
