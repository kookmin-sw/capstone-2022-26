/* eslint-disable react/prop-types */
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import * as FaIcons from 'react-icons/fa';
// import * as AiIcons from 'react-icons/ai';

import { SidebarData } from './SidebarData';
import styles from '../assets/Sidebar.module.scss';

// eslint-disable-next-line no-unused-vars
function Sidebar({ menu, getSelectedMenu }) {
  const [sidebar, setSidebar] = useState(false);
  
  const showSidebar = () => setSidebar(!sidebar);
  
  const sendSelectedMenu = (data) => {
    getSelectedMenu(data);
  }

  return (
    <>
      <div className={styles.navbar}>
        <Link to='#!' className={styles['menu-bars']}>
        <FaIcons.FaBars onClick={showSidebar} />
        </Link>
      </div>
      <nav className={sidebar ? styles['nav-menu active'] : styles['nav-menu']} style={{width: '200px'}}>
        <ul className={styles['nav-menu-items']} onClick={showSidebar} role='presentation'
          style={{height: '100vh', backgroundColor: '#7265FF', float: 'left', marginTop: '0px', padding: '0px'}}>
          <li className={styles['navbar-toggle']}>
            <Link to='#!' className={styles['menu-bars']}>
              {/* <AiIcons.AiOutlineClose /> */}
            </Link>
          </li>
          {SidebarData.map((item) => (
            <li key={item.title} className={styles[item.cName]}>
              <button className={styles['menu-button']} type='button' onClick={() => sendSelectedMenu(item.title)}>
                <span>{item.title}</span>
              </button>
            </li>
          ))}
        </ul>
      </nav>
    </>
  );
}

export default Sidebar;