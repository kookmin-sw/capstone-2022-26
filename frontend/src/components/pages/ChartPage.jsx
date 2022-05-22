import React from 'react';
import DashboardContainer from '../../containers/DashboardContainer';
import ChartContainer from '../../containers/ChartContainer';

function ChartPage() {
  return (
    <div>
      <DashboardContainer />
      <ChartContainer menu='Chart' />
    </div>
  );
}

export default ChartPage;
