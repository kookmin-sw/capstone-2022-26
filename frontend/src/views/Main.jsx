import React, { useState } from 'react';
// import RankBoard from '../containers/RankBoard';
import SideBar from '../components/Sidebar';

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
      <h1>{menu}</h1>
      { menu === 'Home' && <div>Home</div> }
      { menu === 'Chart' && <div>Chart</div> }
      { menu === 'Melon' && <div>Melon</div> }
      { menu === 'Genie' && <div>Genie</div> }
      { menu === 'Bugs' && <div>Bugs</div> }
      { menu === 'About' && <div>About</div> }
    </div>
  );
}

export default Main;
