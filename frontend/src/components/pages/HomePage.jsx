import { React, useEffect } from 'react';
import AOS from 'aos';
import '../../assets/HomePage.css';
import 'aos/dist/aos.css';

import mainPage from '../../assets/mainPage.png';
import dashboard from '../../assets/dashboard.png';
import chart from '../../assets/chart.png';

function HomePage() {
  useEffect(() => {
    AOS.init({
      duration: 1200
    });
  }, [])

  return(
    <div className='page'>
      <div className='subtitle' data-aos='fade-up'>Capstone 26</div>
      <div className='title' data-aos='fade-up'>멜벅지</div>
      <div style={{marginTop: '10vh', textAlign: 'center'}}>
        <img className='main-img' src={mainPage} alt='main' data-aos='fade-up' />
      </div>

      <div style={{marginTop: '30vh', textAlign: 'right'}}>
        <div style={{float: 'left'}}>
          <div data-aos='fade-right' style={{marginTop: '22vh', paddingLeft: '10vw', fontSize: '2em'}}>Real-Time Chart</div>
          <div data-aos='fade-right' style={{paddingLeft: '10vw', color: 'gray'}}>with Melon, Genie, Bugs</div>
        </div>
        <img className='dashboard-img' src={dashboard} alt='dashboard' data-aos='fade-left' />
      </div>

      <div style={{marginTop: '30vh', textAlign: 'left'}}>
        <div style={{float: 'right'}}>
          <div data-aos='fade-left' style={{marginTop: '30vh', paddingRight: '15vw', fontSize: '2em'}}>Scoring by Weight</div>
          <div data-aos='fade-left' style={{paddingRight: '15vw', color: 'gray'}}>up to 100 songs info</div>
        </div>
        <img className='chart-img' src={chart} alt='chart' data-aos='fade-right' />
      </div>

      <div className='subtitle' data-aos='fade-up' style={{marginTop: '50vh'}}>Contributors</div>

      <div>
        <div data-aos='fade-right' style={{fontSize: '2em', marginTop: '30vh', textAlign: 'left', marginLeft: '47vw'}}>Data Analysis</div>
        <div data-aos='fade-left' style={{paddingRight: '15vw', fontSize: '2em'}}>박태범</div>
        <div data-aos='fade-left' style={{paddingRight: '15vw', color: 'gray'}}>20171626</div>
        <div data-aos='fade-left' style={{paddingRight: '15vw', color: 'gray'}}>ppttbb9461@kookmin.ac.kr</div>
      </div>

      <div>
        <div data-aos='fade-left' style={{fontSize: '2em', marginTop: '30vh', textAlign: 'right', marginRight: '50vw'}}>Frontend</div>
        <div data-aos='fade-right' style={{paddingLeft: '10vw', fontSize: '2em'}}>서범석</div>
        <div data-aos='fade-right' style={{paddingLeft: '10vw', color: 'gray'}}>20171628</div>
        <div data-aos='fade-right' style={{paddingLeft: '10vw', color: 'gray'}}>sbs9805@kookmin.ac.kr</div>
      </div>

      <div>
        <div data-aos='fade-right' style={{fontSize: '2em', marginTop: '30vh', textAlign: 'left', marginLeft: '47vw'}}>Design</div>
        <div data-aos='fade-left' style={{paddingRight: '15vw', fontSize: '2em'}}>서필립</div>
        <div data-aos='fade-left' style={{paddingRight: '15vw', color: 'gray'}}>20171631</div>
        <div data-aos='fade-left' style={{paddingRight: '15vw', color: 'gray'}}>seophillip10@gmail.com</div>
      </div>

      <div>
        <div data-aos='fade-left' style={{fontSize: '2em', marginTop: '30vh', textAlign: 'right', marginRight: '50vw'}}>Backend</div>
        <div data-aos='fade-right' style={{paddingLeft: '10vw', fontSize: '2em'}}>이인호</div>
        <div data-aos='fade-right' style={{paddingLeft: '10vw', color: 'gray'}}>20171675</div>
        <div data-aos='fade-right' style={{paddingLeft: '10vw', color: 'gray'}}>inhoking@kookmin.ac.kr</div>
      </div>

      <div style={{height: '20vh'}} />
    </div>
  )
}

export default HomePage;
