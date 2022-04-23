import React, { useState, useEffect } from 'react';

function RankBoard(songs) {
  const [songLabels, setSongLabels] = useState([]);

  useEffect(() => {
    console.log(songs);
    setSongLabels(['first', 'second', 'third']);
  }, [songs]);

  return <div className="rank-board">{songLabels}</div>;
}

export default RankBoard;
