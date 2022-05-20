import axios from 'axios';

const BASE_URL = `http://ec2-54-180-109-17.ap-northeast-2.compute.amazonaws.com`;

// eslint-disable-next-line import/prefer-default-export
export async function getTotalSongs() {
  const songs = [
    {
      rank: 1,
      song: 'That That',
      artist: 'PSY',
      coverImg: 'coverImg',
      date: '2022-05-17',
      time: 18,
      weight: 99.97
    },
    {
      rank: 2,
      song: 'LOVE DIVE',
      artist: 'IVE',
      coverImg: 'coverImg',
      date: '2022-05-17',
      time: 18,
      weight: 98.79
    },
    {
      rank: 3,
      song: 'TOMBOY',
      artist: 'IDLE',
      coverImg: 'coverImg',
      date: '2022-05-17',
      time: 18,
      weight: 98.13
    },
    {
      rank: 4,
      song: 'Still Life',
      artist: 'BIGBANG',
      coverImg: 'coverImg',
      date: '2022-05-17',
      time: 18,
      weight: 96.88
    },
  ];

  return songs;
}

export async function getMelonSongs() {
  const songs = [
    {
      rank: 1,
      song: 'That That',
      artist: 'PSY',
      coverImg: 'coverImg',
      date: '2022-05-17',
      time: 18,
      weight: 99.97
    },
    {
      rank: 2,
      song: 'LOVE DIVE',
      artist: 'IVE',
      coverImg: 'coverImg',
      date: '2022-05-17',
      time: 18,
      weight: 98.79
    }
  ];

  return songs;
}

export async function getGenieSongs() {
  let songs;
  await axios.get(`${BASE_URL}/chart`)
    .then((res) => {
      console.log(res)

      songs = res;
    })
  return songs;
}

export async function getBugsSongs() {
  return [];
}
