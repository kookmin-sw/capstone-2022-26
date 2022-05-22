import axios from 'axios';

const BASE_URL = `http://ec2-13-125-170-254.ap-northeast-2.compute.amazonaws.com/`;

// eslint-disable-next-line import/prefer-default-export
export async function getTotalSongs() {
  let songs;
  await axios.get(`${BASE_URL}/chart`)
    .then((res) => {
      songs = res.data;
    })
  return songs;
}

export async function getMelonSongs() {
  let songs;
  await axios.get(`${BASE_URL}/chart/melon`)
    .then((res) => {
      songs = res.data;
    })
  return songs;
}

export async function getGenieSongs() {
  let songs;
  await axios.get(`${BASE_URL}/chart/genie`)
    .then((res) => {
      songs = res.data;
    })
  return songs;
}

export async function getBugsSongs() {
  let songs;
  await axios.get(`${BASE_URL}/chart/bugs`)
    .then((res) => {
      songs = res.data;
    })
  return songs;
}
