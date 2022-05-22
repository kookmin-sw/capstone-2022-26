import React, { useState, useEffect } from 'react';
// eslint-disable-next-line
import { Chart } from 'chart.js/auto';
import { Line } from 'react-chartjs-2';
import { getDashboardData } from '../apis/dashboard-api';

const options = {
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'right',
      maxWidth: 140,
    }
  }
}

function DashboardContainer() {
  const [chartData, setChartData] = useState({labels: [], datasets: []})
  const [isLoading, setisLoading] = useState(true);

  const getData = async () => {
    const data = await getDashboardData();
    return data;
  };

  useEffect(() => {
    const data = getData();
    data.then(e => {
      setChartData(e);
    })
    setisLoading(false);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  if (isLoading) return <div>loading...</div>

  return (
    <div style={{width: '70vw', height: '50vh', margin: '0 auto', marginTop: '10vh', backgroundColor: 'white', border: '1px solid #EFEFEF', borderRadius: '1em'}}>
      <div style={{textAlign: 'center', fontSize: '1.5em', margin: '3vh', fontWeight: '300', color: '#261C4C'}}> Top 10 Songs Chart </div>
      <Line
        data={chartData}
        options={options}
        style={{padding: '1em', backgroundColor: 'white', borderBottom: '1px solid #EFEFEF', borderRadius: '1em'}}
      />
    </div>
  );
}

export default DashboardContainer;
