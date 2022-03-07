const SpotifyWebApi = require('spotify-web-api-node');
const express = require('express');
const router = express.Router();

require('dotenv').config();
scopes = ['user-read-private', 'user-read-email','playlist-modify-public','playlist-modify-private'];

let spotifyApi = new SpotifyWebApi({
    clientId: process.env.clientId,
    clientSecret: process.env.clientSecret,
    redirectUri: process.env.callbackUrl
  });

spotifyApi.clientCredentialsGrant()
    .then(function(data) {
        spotifyApi.setAccessToken(data.body['access_token']);
        console.log(spotifyApi.getAccessToken());
    }, function(err) {
        console.log(err);   
    });

router.get('/', (req, res, next) => {
    res.render('index');
});

router.get('/login', (req,res) => {
    var html = spotifyApi.createAuthorizeURL(scopes);
    console.log(html);
    res.redirect(html+"&show_dialog=true");
});

router.get('/artists', async (req, res, next) => {
    await spotifyApi.searchArtists(req.query.artist)
        .then(function(data) {
            res.render('artists', {
                artists: data.body.artists.items,
                artist: req.query.artist
            });
        }, function(err) {
            console.log(err);
        });
});

router.get('/albums/:id', async (req, res, next) => {
    await spotifyApi.getArtistAlbums(req.params.id)
        .then(function(data) {
            let artist = req.query.artist;
            res.render('albums', {
                albums: data.body.items,
                artist: artist
            });
        }, function(err) {
            console.log(err);
        })
})

router.get('/tracks/:id', (req, res, next) => {
    spotifyApi
      .getAlbumTracks(req.params.id)
      .then(function(data) {
          console.log(data.body.items[0].id);
          spotifyApi.getTrack(data.body.items[1].id)
          .then(function(data){
              console.log(data.body);
          })
        // res.render('tracks', {tracks: data.body.items, album: req.query.album, artist: req.query.artist})
  
      }, function(err) {
        console.log('Something went wrong!', err);
      });
  });

// router.get('/callback', async (req, res) => {
//     const code = req.query.code;
//     console.log(code);
//     try {
//         let data = await spotifyApi.authorizationCodeGrant(code);
//         const {acces_token, refresh_token} = data.body;
//         spotifyApi.setAccessToken(acces_token);
//         spotifyApi.setRefreshToken(refresh_token);
//         console.log(data);
//         res.redirect('http://localhost:8060');
//     } catch(err){
//         res.redirect(err);
//         console.log(err);
//     }
// });


module.exports = router;