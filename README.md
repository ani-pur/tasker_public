Author: Anirudh Purohit

# What is this? 
This is a simple locally hosted task-manager app built using the **Flask** python framework and some AI generated UI as I have not yet learned css.

` Running main.py will host the app at localhost. `

## User Authentication: 
> User profiles are handled on the backend (hasher.py provides CRUD operations)
> 
> Credentials are stored in ``` users.json ``` as ```username:hashed_password``` pairs (Werkzeug security library in python).
> 
> Once a user is added, they can log in at ``` 127.0.0.1 ``` from their browser.
> 
> App is "scaleable" and supports multiple users with individual task storage, no overlap.
> 
> Tasks are currently sorted by ``` Earliest Due - Latest Due```, will add sorting functionality soon.


## Personal Deployment and Architecture:

- Containerized with Docker
- Reverse proxied to the web through Cloudflare using [Cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) (NOT         included in this repo)
- UI auto-switches between mobile and desktop based on User-Agent headers.
- Automated to start on boot with some batch scripting (NOT included in this repo)

## Screenshots:
![image](https://github.com/user-attachments/assets/2e90706c-0b1d-4adc-93f3-25b578a86598)

![image](https://github.com/user-attachments/assets/da821e57-0aec-49aa-807b-e2842bb6fec0)

![image](https://github.com/user-attachments/assets/aaad88f1-df40-4412-867e-e8a33d8c9dc3)

