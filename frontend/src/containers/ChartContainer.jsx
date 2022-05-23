/* eslint-disable react/no-danger */
/* eslint-disable jsx-a11y/no-noninteractive-element-interactions */
/* eslint-disable jsx-a11y/iframe-has-title */
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { getTotalSongs, getMelonSongs, getGenieSongs, getBugsSongs } from '../apis/chart-api';

import "../assets/ChartContainer.css";
import youtubeIcon from '../assets/youtube.png'

function SongLable({ song }) {
  SongLable.propTypes = {
    song: PropTypes.node.isRequired,
  };
  const [showYoutube, setShowYoutube] = useState(false);

  const youtubeClicked = () => {
    if (showYoutube) {
      setShowYoutube(false);
      return;
    }
    setShowYoutube(true);
  };

  return (
    <div>
      <div className="chart">
        <div className="rank">{song.rank}</div>
        <img className="albumImg" src={song.coverImg} alt={song.rank}/>
        <div className="song">{song.song}</div>
        <div className="artist">{song.artist}</div>
        <div className="weight" style={{fontWeight: '700'}}>{(song.weight).toFixed(2)}</div>
        {song.link &&
          <img className="youtubeButton" src={youtubeIcon} alt={song.song} onClick={() => youtubeClicked()} onKeyDown={() => youtubeClicked()}/>}
      </div>
      {showYoutube && 
        <div className="youtube" dangerouslySetInnerHTML={{ __html: song.link }} />}
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
    <div style={{marginTop: '15vh', marginBottom: '10vh'}}>
      <div className="chartTitle">
        <div className="rankTitle">순위</div>
        <div className="albumImgTitle" />
        <div className="song">제목</div>
        <div className="artist">아티스트</div>
        <div className="weight" style={{textAlign: 'center'}}>점수</div>
      </div>
      {songLabels.map((song) => <SongLable key={song.rank} song={song} />)}
    </div>
  );
}

export default ChartContainer;
