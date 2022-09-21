package com.example.test_app;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import com.google.gson.JsonObject;
import com.pubnub.api.PNConfiguration;
import com.pubnub.api.PubNub;
import com.pubnub.api.PubNubException;
import com.pubnub.api.UserId;


public class MainActivity extends AppCompatActivity {

    String PUBLISHKEY = "your PUB_KEY";
    String SUBSCRIBEKEY = "your SUB_KEY";
    PubNub pubnub = null;
    String channelName = "taco_channel";

    JsonObject messageJsonObject = new JsonObject();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        configuration();

        findViewById(R.id.mario_id).setOnClickListener(view ->  {
                System.out.println("click on mario");
                sendMessage("mario");
            });

        findViewById(R.id.ice_cream_id).setOnClickListener(view ->  {
            System.out.println("click on ice cream");
            sendMessage("icecream");
        });

        findViewById(R.id.star_wars_id).setOnClickListener(view ->  {
            System.out.println("click on star wars");
            sendMessage("starwars");
        });
    }

    public void configuration(){

        try {
            PNConfiguration pnConfiguration = new PNConfiguration(new UserId("test_publisher"));
            pnConfiguration.setSubscribeKey(SUBSCRIBEKEY);
            pnConfiguration.setPublishKey(PUBLISHKEY);
            pubnub = new PubNub(pnConfiguration);
        } catch (PubNubException e) {
            e.printStackTrace();
            System.out.println("Could not connect");
        }
    }

    public void sendMessage(String msg) {
        // create message payload using Gson
        messageJsonObject.addProperty("msg", msg);

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
        pubnub.unsubscribe();
        pubnub.disconnect();
    }
}