<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Warbler</h3>

  <p align="center">
    Warbler is a Flask-powered Twitter clone with functionality for users to:
        <ul>
            <li> register </li>
            <li> sign in/out </li>
            <li> follow/unfollow other users </li>
            <li> like/unlike posts </li>
            <li> update their profile</li>
            <li> view other user's profiles</li>
            <li> view a feed of posts from users they follow </li>
        <ul>
    <br>
    The backend was built with: Python, Flask, SQLAlchemy, PostgreSQL.
    <br>
    The frontend was built with Javascript, HTML, CSS.
  </p>

</div>
[![Watch a demo](homepage.png)](https://youtu.be/EQ_4qoR9ePc)

<!-- GETTING STARTED -->

### Getting Started

To run this app locally:

1. Clone the repo

```sh
git clone git@github.com:alicechang29/flask-warbler.git
```

2. Start Python Virtual Environment

```sh
python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
```

3. Create an .env file to hold configuration

```.env
DATABASE_URL=postgresql:///warbler
SECRET_KEY=<insert your value here>
```

4. Create postgreSQL database and seed the data

```shell
(venv) $ createdb warbler
(venv) $ python seed.py
```

5. Start the Flask server

```sh
flask run -p 5001
```

6. Open in browser: http://localhost:5001

### Collaborators

[Aubrey Sherman](https://github.com/aubrey-sherman)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/alicechang29/sharebnb.svg?style=for-the-badge
[contributors-url]: https://github.com/alicechang29/sharebnb/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alicechang29/sharebnb.svg?style=for-the-badge
[forks-url]: https://github.com/alicechang29/sharebnb/network/members
[stars-shield]: https://img.shields.io/github/stars/alicechang29/sharebnb.svg?style=for-the-badge
[stars-url]: https://github.com/alicechang29/sharebnb/stargazers
[issues-shield]: https://img.shields.io/github/issues/alicechang29/sharebnb.svg?style=for-the-badge
[issues-url]: https://github.com/alicechang29/sharebnb/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/achang9
[product-screenshot]: sharebnb/AllListings.png
