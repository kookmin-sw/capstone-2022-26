import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

function SongLable({ song }) {
  SongLable.propTypes = {
    song: PropTypes.node.isRequired,
  };
  return (
    <div>
      <div>{song.total_rank}</div>
      <div>{song.song}</div>
      <div>{song.artist}</div>
      <div>{song.weight}</div>
      <hr/>
    </div>
  );
}

function TotalChart() {
  const [songLabels, setSongLabels] = useState([]);

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

  useEffect(() => {
    setSongLabels(songs);
  }, []);

  return (
    <>
      {songLabels.map(song => <SongLable song={song} />)}
    </>
  );
}

export default TotalChart;
