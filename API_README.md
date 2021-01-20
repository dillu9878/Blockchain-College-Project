# Wallet

## 1. Login Page

https://ecoinwallet.herokuapp.com/login

post request(jason format):-

    {
        "public_key": "0x28E98D1593f604e8E35EDBeb123160b90055baC3",
        "private_key": "bc0771a448c062a1a86ad128b124473f5121c895dd8a56a1c0a2f429785b88ec"
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

## 2. Send Coin

https://ecoinwallet.herokuapp.com/send_coin

Post Request(jason format):

    {
        "receiver": "0x28E98D1593f604e8E35EDBeb123160b90055baC3",
        "sender": "0x60355c86285aeA67DE32E218E2e1307e0ef87699",
        "amount": 50
    }

Post Response:

    {
        "amount": 40,
        "transactions": [
            {
                "amount": 50,
                "receiver": "0x28E98D1593f604e8E35EDBeb123160b90055baC3",
                "sender": "0x60355c86285aeA67DE32E218E2e1307e0ef87699",
                "status": "pending",
                "timestamp": "2021-01-20 22:01:31.468442"
            },
            {
                "amount": 10,
                "receiver": "0x28E98D1593f604e8E35EDBeb123160b90055baC3",
                "sender": "0x60355c86285aeA67DE32E218E2e1307e0ef87699",
                "status": "pending",
                "timestamp": "2021-01-20 22:01:31.468465"
            }
        ]
    }

## 3. Refresh(Get all transaction)

https://ecoinwallet.herokuapp.com/get_all_transactions

Post Request:

    {
        "account_number": "0x60355c86285aeA67DE32E218E2e1307e0ef87699"
    }

Post Response:

    {
        "amount": 40,
        "transactions": [
            {
                "amount": 50,
                "receiver": "0x28E98D1593f604e8E35EDBeb123160b90055baC3",
                "sender": "0x60355c86285aeA67DE32E218E2e1307e0ef87699",
                "status": "pending",
                "timestamp": "2021-01-20 22:02:38.029058"
            },
            {
                "amount": 10,
                "receiver": "0x28E98D1593f604e8E35EDBeb123160b90055baC3",
                "sender": "0x60355c86285aeA67DE32E218E2e1307e0ef87699",
                "status": "pending",
                "timestamp": "2021-01-20 22:02:38.029073"
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

https://ecoinwallet.herokuapp.com/add_coin

Post Request: 

    {
        "account_number": "0x28E98D1593f604e8E35EDBeb123160b90055baC3",
        "amount":1000
    }

Post Response:

    {
        "amount": 100,
        "transactions": [
            {
                "amount": 50,
                "receiver": "0x28E98D1593f604e8E35EDBeb123160b90055baC3",
                "sender": "0x60355c86285aeA67DE32E218E2e1307e0ef87699",
                "status": "pending",
                "timestamp": "2021-01-20 22:05:01.443753"
            },
            {
                "amount": 10,
                "receiver": "0x28E98D1593f604e8E35EDBeb123160b90055baC3",
                "sender": "0x60355c86285aeA67DE32E218E2e1307e0ef87699",
                "status": "pending",
                "timestamp": "2021-01-20 22:05:01.443768"
            },
            {
                "amount": 1000,
                "receiver": "0x28E98D1593f604e8E35EDBeb123160b90055baC3",
                "sender": "",
                "status": "pending",
                "timestamp": "2021-01-20 22:05:01.443773"
            }
        ]
    }











