import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import logo_img from "../assets/logo_img.png";
import { Nav, Image } from "react-bootstrap";

import "../styles/css/Topbar.css";

export function Topbar() {
  return (
    <div className="topbarcompound">
      <Link to="/">
        <div>
          <Image src={logo_img} width="180vw"></Image>
        </div>
      </Link>

      <Nav className="navitems">
        <Nav.Item>
          <Nav.Link className="navlink" href="/function">
            <b>기능 소개</b>
          </Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link className="navlink" href="/team">
            <b>팀 소개</b>
          </Nav.Link>
        </Nav.Item>
      </Nav>
    </div>
  );
}
