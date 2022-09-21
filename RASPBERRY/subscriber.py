from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory, PNOperationType
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from piezo import Piezo
PIEZO = Piezo()

class SubscribeHandler(SubscribeCallback):
    
    def message(self, pubnub, message):
        print("Message channel: %s" % message.channel)
        print("Message subscription: %s" % message.subscription)
        print("Message timetoken: %s" % message.timetoken)
        print("Message payload: %s" % message.message)
        print("Message publisher: %s" % message.publisher)
        msg = message.message['msg']
        # Send message to piezo to play
        PIEZO.play(msg)
