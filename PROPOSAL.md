# SPLOTCHIFY
## Like Spotify, but for karaoke.


### Creators
Priyanka Kishore

### Description
*SPLOTCHIFY* is all the karaoke you'll ever need. Access millions (kinda) of songs, karaoke-style, and create playlists of your favorites. Keep track of your highest score on a song and join the conversation on every single one. Can't find your favorite? Add it for us!

### Stretch Goals
(May not be achieved by due date. But it would be cool if I did.)

- View other user profiles
- Show lyrics to a song
- Use Spotify API to link to actual version of a song
    - Probably need user to sign in to their Spotify?
- Link to SingKingKaraoke for selected number of songs
    - Let user add YouTube link for a song they add
- User can rate each song based on difficulty


## Requirement Satisfaction

### Registration and Login
- Users *must* register for an account and login in order to create playlists, comment on songs, keep track of singing scores, and add songs to the database.

### Forms
1. User registration
2. User login
3. Add song to database
4. Create new playlist
5. Comment on song
6. Edit user profile (time permitting)

### Database
- MongoDB will store user account details (hashed passwords, emails, usernames), user song information (playlists, scores), and song information (song information, comments, etc).

### Security
- The modules used to achieve a secure webapp includes:
    - Flask-Talisman (to set a CSP)
    - Flask-WTF (for CSRF tokens)

### Blueprints
1. user account
    - with view functions to login, register, update profile
2. home/song database
    - with view functions for index, specific song
    - (maybe) top 10 or 100 songs (based on rating)
3. user actions
    - adding songs to database
    - creating playlist
    - commenting on a song
4. App description/about page

(Still kind of confused on blueprints, so may reorganize or come up with better blueprints!)

### Presentation/Appearance
- Multiple templates for various pages
- Bootstrap
- CSS

### New Python Package
- Flask_Mail will be used either for user registration email authentication, or notifying user when someone comments on a user's favorite song (or under some other condition).

### Evidence of Usage
- Must generate a JSON/object and/or pre-fill database to store information on various songs to start with
- Will add sample profiles for at least 2 users, each with their own playlists, comments on songs, etc.

### GitHub for SPLOTCHIFY
https://github.com/priyanka-kishore/SPLOTCHIFY
