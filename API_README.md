# Wallet

## 1. Login Page

http://machine_ip:5000/login

post request(jason format):-

    {

        "public_key": "",
        "private_key": ""
    }

Response(jason):

    {
        "account_no": "",
        "amount": 00,
        "transaction": [
            {
                "time_stamp": "",
                "reciever": "",
                "amount": 00,
                "status": ""
            }
        ]
    }

## 2. Add transaction

http://machine_ip:5000/add_transaction

Post Request(jason format):

    {
        "sender_account_no": "",
        "reciever_account_no": "",
        "amount":00
    }

Post Response:

    {
        "account_no": "",
        "amount": 00,
        "transaction": [
            {
                "time_stamp": "",
                "reciever": "",
                "amount": 00,
                "status": ""
            },
            {
                "time_stamp": "",
                "reciever": "",
                "amount": 00,
                "status": ""
            }
        ]
    }

## 3. Refresh(Get all transaction)

http://machine_ip:5000/get_trnsaction

Post Request:

    {
        "account_no": "",
        "type": "all/confirmed/unconfirmed"
    }

Post Response:

    {
        "transaction": [
            {
                "time_stamp": "",
                "reciever": "",
                "amount": 00,
                "status": ""
            },
            {
                "time_stamp": "",
                "reciever": "",
                "amount": 00,
                "status": ""
            }
        ]
    
    }

## 4. Join network

http://machine_ip:5000/new_user

Empty Get Request

Response:

    {
    "public_key": ""
    }

## 5. Generate Key

http://machine_ip:5000/genrate_key

Post Request:

    {
        "public_key": "",
        "phrase": ""
    }

Post Response:

    {
        "peivate_key": ""
    }

## 6. Add amount

http://machine_ip:5000/add_amount

Post Request: 

    {
        "account_number": "",
        "amount": ""
    }

Post Response:

    {
        "account_no": "",
        "amount": 00,
        "transaction": [
            {
                "time_stamp": "",
                "reciever": "",
                "amount": 00,
                "status": ""
            },
            {
                "time_stamp": "",
                "reciever": "",
                "amount": 00,
                "status": ""
            }
        ]
    }











