import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Dropdown from './Dropdown';
import { Button } from '../Common/Button';
import './Header.css';

function Header() {
  
    const [click, setClick] = useState(false);
    const [button, setButton] = useState(true);
    const [dropdown, setDropdown] = useState(false);
  
    const handleClick = () => setClick(!click);
    const closeMobileMenu = () => setClick(false);
  

    const onMouseEnter = () => {
        if (window.innerWidth < 960) {
          setDropdown(false);
        } else {
          setDropdown(true);
        }
      };
    
      const onMouseLeave = () => {
        if (window.innerWidth < 960) {
          setDropdown(false);
        } else {
          setDropdown(false);
        }
      };

    const showButton = () => {
      if (window.innerWidth <= 960) {
        setButton(false);
      } else {
        setButton(true);
      }
    };
  
    useEffect(() => {
      showButton();
    }, []);
  
    window.addEventListener('resize', showButton);
  
    return (
      <>
        <nav className='navbar'>
          <div className='navbar-container'>
          <Link to='/' className='navbar-logo' onClick={closeMobileMenu} >
  WatchaFlick <span> &nbsp;&nbsp; </span>
  <img src="images/logo.png" alt="logo" style={{ width: '50px', height: '50px', objectFit: 'contain' }} />
</Link>

            <div className='menu-icon' onClick={handleClick}>
              <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
            </div>
            <ul className={click ? 'nav-menu active' : 'nav-menu'}>
           
              <li className='nav-item'>
                <Link to='/' className='nav-links' onClick={closeMobileMenu}>
                  Home
                </Link>
              </li>
              <li
            className='nav-item'
            onMouseEnter={onMouseEnter}
            onMouseLeave={onMouseLeave}
          >
           <div style={{ position: "relative" }}>
            <Link
              className='nav-links'
              onClick={closeMobileMenu}
            >
              Users <span> &nbsp;   </span>
            <i className='fas fa-caret-down' />
            
            {dropdown && <Dropdown />}
            </Link>
            </div>
          </li>
          <li>
                <Link
                  to='/login'
                  className='nav-links-mobile'
                  onClick={closeMobileMenu}
                >
                  LOGIN
                </Link>
              </li>
            </ul>
            {button && <Button buttonStyle='btn--outline' url="/login">LOGIN</Button>}
          </div>
        </nav>
      </>
    );
    
}

export default Header