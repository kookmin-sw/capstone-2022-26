
// eslint-disable-next-line import/prefer-default-export
export async function getTotalSongs() {
  const songs = [
    {
      total_rank: 1,
      song: 'That That',
      artist: 'PSY',
      coverImg: 'coverImg',
      date: '2022-05-17',
      time: 18,
      weight: 99.97
    },
    {
      total_rank: 2,
      song: 'LOVE DIVE',
      artist: 'IVE',
      coverImg: 'coverImg',
      date: '2022-05-17',
      time: 18,
      weight: 98.79
    },
    {
      total_rank: 3,
      song: 'TOMBOY',
      artist: 'IDLE',
      coverImg: 'coverImg',
      date: '2022-05-17',
      time: 18,
      weight: 98.13
    },
    {
      total_rank: 4,
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
      total_rank: 1,
      song: 'That That',
      artist: 'PSY',
      coverImg: 'coverImg',
      date: '2022-05-17',
      time: 18,
      weight: 99.97
    },
    {
      total_rank: 2,
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
  return [];
}

export async function getBugsSongs() {
  return [];
}
