import ssl
import time
from nostr.event import Event
from nostr.relay_manager import RelayManager
from nostr.key import PrivateKey
import random

# generating private, public key
private_key = PrivateKey()
pub_hex = private_key.public_key.hex()

# connecting to relays
relay_manager = RelayManager()
relay_list = ["wss://nostr-pub.wellorder.net", "wss://relay.damus.io", "wss://relay.snort.social", 
              "wss://nostr.bitcoiner.social", "wss://offchain.pub", "wss://nostr.wine/", 
              "wss://nos.lol/"]
for item in relay_list:
  relay_manager.add_relay(item)

# the URL for viewing notes
pub_bech = private_key.public_key.bech32()
url = "https://snort.social/p/"
nostr_profile = url + str(pub_bech)

def publish_quote(quote):
  relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE}) # NOTE: This disables ssl certificate verification
  time.sleep(1.25) # allow the connections to open
  event = Event(pub_hex, quote)
  private_key.sign_event(event)
  relay_manager.publish_event(event)
  time.sleep(1) # allow the messages to send
  print(f"Published\n{event.content}")
  relay_manager.close_connections()

with open("random_quotes.txt", 'r') as source:
# you could modify this to publish all notes. At once. But I've done it for my own sanity
  quotes = source.readlines()
  for line in quotes[:25]:
    publish_quote(line)
    sleep_time = random.randint(2,12)
    print(f'sleeping for {sleep_time}s')
    time.sleep(sleep_time)
print(f'You can check the details at {nostr_profile}')