import axios from 'axios';

const BASE_URL = `http://ec2-13-125-170-254.ap-northeast-2.compute.amazonaws.com/`;

export const backgroundColor = [
  'rgba(255, 92, 299, 0.8)',
  'rgba(114, 251, 168, 0.8)',
  'rgba(148, 147, 255, 0.8)',
  'rgba(255, 244, 141, 0.8)',
  'rgba(214, 147, 255, 0.8)',
  'rgba(255, 188, 140, 0.8)',
  'rgba(255, 143, 157, 0.8)',
  'rgba(151, 230, 255, 0.8)',
  'rgba(229, 251, 143, 0.8)',
  'rgba(255, 191, 222, 0.8)',
  'rgba(218, 218, 218, 0.8)',
];

// eslint-disable-next-line import/prefer-default-export
export async function getDashboardData() {
  const dashboardData = {
    labels: [],
    datasets: [],
  };
  await axios.get(`${BASE_URL}/chart/dashboard`)
    .then((res) => {
      const labels = res.data[0].time;
      dashboardData.labels = labels;

      const datasets = res.data.map((e, i) => {
        const element = {
          label: '',
          data: [],
          backgroundColor: '',
          borderColor: '',
          pointRadius: 1,
        };
        element.label = e.song;
        element.data = e.weight;
        element.backgroundColor = backgroundColor[i];
        element.borderColor = backgroundColor[i];

        return element;
      });
      dashboardData.datasets = datasets;
    });
  return dashboardData;
}
