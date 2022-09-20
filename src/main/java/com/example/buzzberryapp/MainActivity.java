package com.example.buzzberryapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.pubnub.api.PNConfiguration;
import com.pubnub.api.PubNub;
import com.pubnub.api.PubNubException;
import com.pubnub.api.UserId;
import com.pubnub.api.callbacks.PNCallback;
import com.pubnub.api.callbacks.SubscribeCallback;
import com.pubnub.api.enums.PNStatusCategory;
import com.pubnub.api.models.consumer.PNPublishResult;
import com.pubnub.api.models.consumer.PNStatus;
import com.pubnub.api.models.consumer.pubsub.PNMessageResult;
import com.pubnub.api.models.consumer.pubsub.PNPresenceEventResult;

import org.jetbrains.annotations.NotNull;

import java.util.Arrays;

public class MainActivity extends AppCompatActivity {


    String PUBLISHKEY = BuildConfig.PUBLISHKEY;
    String SUBSCRIBEKEY = BuildConfig.SUBSCRIBEKEY;

    PNConfiguration pnConfiguration = null;

    String channelName = "taco_channel";

    JsonObject messageJsonObject = new JsonObject();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        configuration();

        Button playSound = (Button) this.findViewById(R.id.button);

        playSound.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                System.out.println("click");
                sendMessage();
            }

        });

    }

    public void configuration(){

        try {
            pnConfiguration = new PNConfiguration(new UserId("BuzzBerryApp"));
        } catch (PubNubException e) {
            e.printStackTrace();
        }

        pnConfiguration.setSubscribeKey(SUBSCRIBEKEY);
        pnConfiguration.setPublishKey(PUBLISHKEY);

    }

    public void sendMessage() {
        PubNub pubnub = new PubNub(pnConfiguration);

        // create message payload using Gson
        messageJsonObject.addProperty("msg", "Can you see me ");

        System.out.println("Message to send: " + messageJsonObject.toString());

        pubnub.publish().channel(channelName)
                .message(messageJsonObject)
                .async((result, publishStatus) -> {
                    if (!publishStatus.isError()) {
                        System.out.println("Connected");
                    } else { // Request processing failed.
                        System.out.println("Error");
                        publishStatus.retry();
                    }
                });
            }

    public void unsubscribe(){
         PubNub pubnub = new PubNub(pnConfiguration);
         pubnub.unsubscribe();
         pubnub.disconnect();
    }
}

