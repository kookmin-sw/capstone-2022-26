import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { getTotalSongs, getMelonSongs, getGenieSongs, getBugsSongs } from '../apis/chart-api';

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

function Chart(menu) {
  const [songLabels, setSongLabels] = useState([]);
  const [isLoading, setisLoading] = useState(true);

  const getData = async () => {
    let result;
    switch(menu) {
      case 'Home':
      case 'Chart':
        result = await getTotalSongs();
        break;
      case 'Melon':
        console.log('melon');
        result = await getMelonSongs();
        break;
      case 'Genie':
        console.log('melon');
        result = await getGenieSongs();
        break;
      case 'Bugs':
        console.log('melon');
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
      {songLabels.map((song) => <SongLable key={song.total_rank} song={song} />)}
    </>
  );
}

export default Chart;
