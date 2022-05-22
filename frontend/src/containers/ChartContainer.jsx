import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { getTotalSongs, getMelonSongs, getGenieSongs, getBugsSongs } from '../apis/chart-api';

import "../assets/ChartContainer.css";

function SongLable({ song }) {
  SongLable.propTypes = {
    song: PropTypes.node.isRequired,
  };
  return (
    <div className="chart">
      <div className="rank">{song.rank}</div>
      <img className="albumImg" src={song.coverImg} alt={song.rank}/>
      <div className="song">{song.song}</div>
      <div className="artist">{song.artist}</div>
      <div className="weight">{(song.weight).toFixed(2)}</div>
    </div>
  );
}

function ChartContainer(menu) {
  const [songLabels, setSongLabels] = useState([]);
  const [isLoading, setisLoading] = useState(true);

  const getData = async () => {
    let result;
    // eslint-disable-next-line react/destructuring-assignment
    switch(menu.menu) {
      case 'Home':
      case 'Chart':
        result = await getTotalSongs();
        break;
      case 'Melon':
        result = await getMelonSongs();
        break;
      case 'Genie':
        result = await getGenieSongs();
        break;
      case 'Bugs':
        result = await getBugsSongs();
        break;
      default:
        result = await getTotalSongs();
    }
    return result;
  }

  useEffect(() => {
    const chartData = getData();
    chartData.then(data => {
      setSongLabels(data);
    }); 
    setisLoading(false);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  if (isLoading) return <div>loading...</div>

  return (
    <div style={{marginTop: '15vh'}}>
      {songLabels.map((song) => <SongLable key={song.rank} song={song} />)}
    </div>
  );
}

export default ChartContainer;
