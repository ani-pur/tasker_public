Author: Anirudh Purohit

# What is this? 
This is a simple locally hosted task-manager app built using the **Flask** python framework.

## User Authentication: 
> User profiles are handled on the backend (hasher.py provides CRUD)
> 
> Credentials are stored in ``` users.json ``` as ```username:hashed_password``` pairs (Werkzeug security library in python).
> 
> Once a user is added, they can log in at ``` localhost ```
> 
> App is "scaleable" and supports multiple users with individual task storage, no overlap.
> 
> Tasks are currently sorted by ``` Earliest Due - Latest Due```, will add sorting functionality soon.

## Planned updates:
> ~~Visual Overhaul (complete)~~
> Migrate to database for task storage (soon)


## Deployment and Architecture:

- Containerized with Docker
- Reverse proxied through Cloudflare using [Cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)


