import React, { useState } from 'react';
import SideBar from '../components/Sidebar';
import HomePage from '../components/pages/HomePage';
import ChartPage from '../components/pages/ChartPage';
import MelonPage from '../components/pages/MelonPage';
import GeniePage from '../components/pages/GeniePage';
import BugsPage from '../components/pages/BugsPage';
// import AboutPage from '../components/pages/AboutPage';

import styles from '../assets/Main.module.scss';

function Main() {
  const [menu, setMenu] = useState('Home');

  const getSelectedMenu = (menuData) => {
    setMenu(menuData);
  }

  return (
    <div className={styles.page}>
      <SideBar
        menu={menu}
        getSelectedMenu={getSelectedMenu}
      />
      <div className={styles.menuPages}>
        { menu === 'Home' && <HomePage /> }
        { menu === 'Chart' && <ChartPage /> }
        { menu === 'Melon' && <MelonPage /> }
        { menu === 'Genie' && <GeniePage /> }
        { menu === 'Bugs' && <BugsPage /> }
      {/* { menu === 'About' && <AboutPage /> } */}
      </div>
    </div>
  );
}

export default Main;
