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
      <div>{song.rank}</div>
      <div>{song.song}</div>
      <div>{song.artist}</div>
      <div>{song.weight}</div>
      <hr/>
    </div>
  );
}

function Chart(menu) {
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
    const chartData = getData()
    chartData.then(data => {
      setSongLabels(data);
    }); 
    setisLoading(false);
  }, []);

  if (isLoading) return <div>loading...</div>

  return (
    <>
      {songLabels.map((song) => <SongLable key={song.rank} song={song} />)}
    </>
  );
}

export default Chart;
