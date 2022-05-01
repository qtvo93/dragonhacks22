# dragonhacks22

## Inspiration
Hi, our team includes Hiep, Tuong, and Quoc. We developed an app because we want people to be notified when it's unsafe to go outside, which we believe makes our community healthier. Also, people might want to visit a city and check how the quality of air in that city is.
## What it does
The application allows users to insert a city and get the quality index of the city at that time. The application also has a feature that allows users to subscribe to our services which will send a message including the air quality index every hour if the air quality index is above a threshold that can cause health illnesses to people.
## How we built it
We first make a UI that users can interact with and insert the city they want to get the air quality index. Then, we call an API endpoint from API - Air Quality Programmatic APIs based on the city that users specify. Then, we create a database that stores the user's phone number and email. Finally, we use Twilio to send a message to the user's phone number and Mailgun to send a message to the user's email address.
## Challenges we ran into
We had some issues with importing modules in sqlalchemy. Then, we worked together to help each other out. Finally, I found a tutorial that helps us solve the problem. Also, it takes us some time to get familiar with Twilio and Mailgun services.
## Accomplishments that we're proud of
We are able to develop a project with all features we want it to have. Also, we know how to set up a sqlalchemy database and get familiar with the services of Twilio and Mailgun.
## What we learned
We learned the importance of teamwork. We also learned how to send a message to phone numbers and emails using services. We also learned how to use git.
## What's next for Air Care
The next step for our project is to make the UI more beautiful and more interactive.
