from twilio.rest import Client 
 
account_sid = 'ACce40dc834207e2950d2e5b4e8b408afa' 
auth_token = '<USEYOUROWNAUTHENTICATIONTOKEN>' 
client = Client(account_sid, auth_token) 

def send():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Gud Night Buddy!',      
                                to='whatsapp:+919123338627' 
                            ) 
    
    print(message.sid)
