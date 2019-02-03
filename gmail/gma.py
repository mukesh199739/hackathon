from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pyttsx3
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

def main():
   
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    
    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
    messages = results.get('messages', [])
    

    if not messages:
        print ("No messages found.")
    else:
        print ("Message snippets:")
        for message in messages[0:5]:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print (msg['snippet'])
            import pyttsx3
            engine=pyttsx3.init()
            engine.say(msg['snippet'])
            engine.setProperty('volume',0.9)
            engine.runAndWait()
            
            

if __name__ == '__main__':
    main()



