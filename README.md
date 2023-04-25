![Overview Diagram](./Overview_diagram.png "Overview Diagram")

1. ~~ Setup API Gateway, pointed at our lambda ~~
2. ~~cURL from the raspberry pi~~
3. Register/provision phone number with AWS (registration request made on 4/1/23)
4. Setup tinyDB to check if we texted Cole today 
5. Write our lambda, to fire a text (via AWS SNS)
6. ~~Get laser working...and allow Cole to calibrate it when it's on site~~
7. ~~Get a tilt sensor working, in tandem with the laser? Otherwise we need to use an accelerometer~~
8. Setup solar power
9. Figure out how to do database dumps, so Cole can put data on r/dataisbeautiful

`sudo nano /lib/systemd/system/myservice.service`
