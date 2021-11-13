# Rickroll Me
#### (Custom Metadata URL Redirect Prank)

## Inspiration
I took two of the things I love, **Rickrolls/pranks**, and **URL redirecting**, and decided to make an app that **automated the process** of bringing the two together. I have in the past used one specific repl that I had to manually edit the code in any time I wanted to make a different prank, and knew there must be a better way. That is when I decided to make this app.

## What it does
This web app **takes input from the user** of how the URL should look, and different **metadata tags** (*site name, title, description, and image*) as well as the **destination URL**, and creates a redirect link. It stores this information in an **SQL database** so that old links can be used in the future. When someone pastes the link, **the website will appear just as they set up with the metadata**, and when they click on the link, it **redirects to the desired URL**.

## How I built it
I used **flask** to host the **back end** of the application, and **HTML/CSS/JS** for the look and feel of the website. User data is posted from the web form into an **SQL database**. When someone tried to paste or open a link from the website, flask grabs the URL and **queries the database** to find the pre-entered metadata, then **uses it to generate a redir.html file with metadata and a redirect timeout**. Thus when someone clicks the link they are redirected to the pre-determined website.

## Challenges I ran into
The main challenge I ran into is how **Facebook was ignoring the metadata** I included in my redir.html file and went straight to the redirect's metadata instead. **This was solved by using JavaScript to handle the redirecting**, and **setting a timeout of 1 second** so that Facebook could not predict the redirect before hosting the link's metadata.

## Accomplishments that I'm proud of
I'm proud of **overcoming the challenge that Facebook posed** (as noted above). Moreover, I'm proud of being able to **set up a proper web server on a VPS**, something I have never done before. This will open up many new opportunities for me, and will allow me to create much more robust applications in the future.

## What I learned
This was my first time using **Gunicorn** and **Caddyserver** to host a website, and also my **first time hosting a web app on a VPS** (in the past I would just use a platform such as Heroku or GitHub Pages). Therefore I learned more about web servers in general, and about how reverse proxy works. Moreover, **I am now much more comfortable with web servers and backend programming in general**.

## What's next for Rickroll Me
I plan to develop a **login system** whereby users may save their custom links, and access/edit/delete them from a **central dashboard**.
