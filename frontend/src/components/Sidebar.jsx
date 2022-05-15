import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';

import { SidebarData } from './SidebarData';
import styles from '../assets/Sidebar.module.scss';

function Sidebar() {
  const [sidebar, setSidebar] = useState(false);
  
  const showSidebar = () => setSidebar(!sidebar);

  return (
    <>
      <div className={styles.navbar}>
        <Link to='#!' className={styles['menu-bars']}>
        <FaIcons.FaBars onClick={showSidebar} />
        </Link>
      </div>
      {sidebar ? console.log(sidebar) : console.log(sidebar)}
      <nav className={sidebar ? styles['nav-menu active'] : styles['nav-menu']} style={{width: '200px'}}>
        <ul className={styles['nav-menu-items']} onClick={showSidebar} role='presentation'>
          <li className={styles['navbar-toggle']}>
            <Link to='#!' className={styles['menu-bars']}>
              <AiIcons.AiOutlineClose />
            </Link>
          </li>
          {SidebarData.map((item) => (
            <li key={item.id} className={styles[item.cName]}>
              <Link to={item.path}>
                {item.title}
                <span>{item.title}</span>
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </>
  );
}

export default Sidebar;