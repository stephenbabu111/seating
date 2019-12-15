def send_message(phone,password):
    account_side='AC36fbfefc8c73f28db214b6f1d46ea232'
    auth_token='8c54d3e2d5dda4ff71aa1bcf3c73aa39'
    phone=str(phone)
    my_cell='+91'+phone
    my_twilio='+12569527054'
    from twilio.rest import Client

    client =Client(account_side,auth_token)

    my_msg= 'your password for user login is:'+password

    message=client.messages.create(to=my_cell,from_=my_twilio,body=my_msg)
    print(message)

