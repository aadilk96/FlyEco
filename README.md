# FlyEco - Project for JacobsHack 2019 

## A website that lists the most eco-friendly routes between two chosen destinations with a gamification aspect

### Tech used 
    1. Django 
    2. SkyScanner Emissions API
    3. SkyScanner Routes API
    4. Twilio Messaging API
    5. Crispy Forms

### Description of implementation 
   The project is made using a Django stack. It has a fully functioning backend allowing for the 
   creation of different users and their own individual data. 
   We make use of the SkyScanner Emissions API to calculate the amount of CO2 that is produced 
   for any given flight route. The API only works for direct flights, so we used the Routes API 
   to segment the route into direct flights and then get the total emissions. 
   When a user clicks of a flight, they get points based on how eco-friendly their option is. 
   They also receive a text message on their phone (if they have a number entered) that shows them details about the flight. 
   The background image of the webapp changes depending on how many points the user has.
    
