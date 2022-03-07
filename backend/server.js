const SpotifyWebApi = require('spotify-web-api-node');
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 8060;
require('dotenv').config();

let index = require('./routes/index');

app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use(express.static('public'));

app.use('/', index);


// let clientId = process.env.clientId,
//   clientSecret = process.env.clientSecret;
//   accessToken = '';

// let spotifyApi = new SpotifyWebApi({
//   clientId: process.env.clientId,
//   clientSecret: process.env.clientSecret
// });
// scopes = ['user-read-private', 'user-read-email','playlist-modify-public','playlist-modify-private'];

// spotifyApi.clientCredentialsGrant()
//   .then(function(data) {
//     spotifyApi.setAccessToken(data.body['access_token']);
//     console.log(spotifyApi.getAccessToken());
//   }, function(err) {
//     console.log(err);
//   });

// app.get('/', (req, res, next) => {
//   res.send('home')
// });

// app.get('/login', (req,res) => {
//   var html = spotifyApi.createAuthorizeURL(scopes)
//   console.log(html)
//   res.send(html+"&show_dialog=true")  
// })

// app.get('/playlists', async (req, res) => {
//   try {
//     let result = await spotifyApi.getUserPlaylists();
//     console.log(result.body);
//     res.status(200).send(result.body);
//   } catch (err) {
//     res.status(400).send(err);
//   }
// });

// app.get('/albums/:artistId', (req, res, next) => {
//   spotifyApi.getArtistAlbums(req.params.artistId)
//     .then(function(data) {
//       res.send(data.body.items);
//       // res.render('albums', {
//       //   albums: data.body.items
//       // });
//     }, function(err){
//       console.log(err);
//     })
// })

// app.use((req, res, next) => {
//   let err = new Error('404 Not Found');
//   err.status = 404;
//   next(err);
// });

// app.use((err, req, res, next) => {
//   res.locals.message = err.message;
//   res.locals.error = req.app.get('env') === 'development' ? err: {};

//   res.status(err.status || 500);
//   res.render('error');
// });

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
});

module.exports = app;