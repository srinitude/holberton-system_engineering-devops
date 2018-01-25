# Issue Summary

The outage, codename Yellow Storm, occurred from 11:00 AM UTC to 4:00 PM UTC on January 24, 2018. For these 5 consecutive hours, users were experiencing 500 errors on all endpoints that would normally return 200 and 300-class status codes. The root cause of the outage was that OAuth credentials were not being properly passed to our API endpoints.

# Timeline

* 11:00 AM - Our power users were furious about the downtime and told us that weren't able to access our site resources. We were on the phone with them for half an hour.
* 11:30 AM - We started to cURL on many different endpoints and started getting the same 500 error. We know that there was one root cause at this point.
* 12:00 PM - The SRE team were initially looking at the Flask app, trying to pinpoint if that is where the problem was stemming from. This didn’t seem to be the case.
* 12:30 PM - The SRE team then looked at the Nginx configuration file to make sure that everything was in order. Everything was in order.
* 01:00 PM - The SRE team then looked at the client request body to make sure that the format was valid. The format was valid and the keys were being passed correctly to the server.
* 01:30 PM - The SRE team then looked at the uWSGI configuration file to make sure that everything was order. Nothing seemed like it was out of the ordinary.
* 02:00 PM - The SRE team then went out to lunch to take a break because they were way too stressed that they weren’t able to debug the issue yet. Everyone went out to The Melt. The food was apparently amazing and the prices weren’t too bad. It was really close to work, so everyone was able to get back in a timely fashion.

* 02:30 PM - Everyone enjoyed their lunch, so they were now able to get back to work. However, the SRE team felt like they exhausted all of their options at this point and Googled what would be causing a 500 error.
* 03:00 PM - It turns out that the Google search didn’t bear any fruit, so they went back to blindly debugging the problem.
* 03:30 PM - After many print statements within the Flask app, the SRE team found that the value of the OAUTH_KEY and OAUTH_SECRET environment variables were None.
* 04:00 PM - It turns out that the keys were lost in translation from NGINX to uWSGI to Flask. However, the SRE team didn’t know how to fix that problem.

# Root Cause

The root cause was the fact that the SRE team did not receive the proper training in how all of the frameworks related.

# Resolution

We went out of business.

# Corrective/Preventative Measures

¯\\_(ツ)_/¯
