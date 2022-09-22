from pubnub.pnconfiguration import PNConfiguration
from pubnub.enums import PNReconnectionPolicy
from pubnub.pubnub import PubNub
import time
from subscriber import SubscribeHandler
#from key_config import *
from raspberry_keys import *

def run():
    
    # sleep before starting to configure
    _time = time.time()
    delay = 10
    while(true):
        # sleeping
        if(time.time()-_time > delay):
            break

    pnconfig = PNConfiguration()
    # Subscribe key for connection 
    pnconfig.subscribe_key = SUB_KEY
    # User id for connection
    pnconfig.user_id = 'buzzberry-pi'
    # For automatic reconnect
    pnconfig.reconnect_policy = PNReconnectionPolicy.LINEAR
    # Initialize PubNub
    pubnub = PubNub(pnconfig) # returns PubNub instance for invoking PubNub APIs.
    print("Starting listener..")
    pubnub.add_listener(SubscribeHandler())
    pubnub.subscribe().channels('taco_channel').execute()


if __name__ == "__main__":
    run()
