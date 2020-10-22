import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import logo_img from "../assets/logo_img.png";
import { Nav, Image, NavDropdown } from "react-bootstrap";

import "../styles/css/Topbar.css";

export function Topbar() {
  return (
    <div>
      <Link to="/">
        <div>
          <Image src={logo_img}></Image>
        </div>
      </Link>

      <Nav className="navitems">
        <Nav.Item>
          <Nav.Link className="navlink" href="/purchase">
            <b>기능 소개</b>
          </Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link className="navlink" href="/purchase">
            <b>팀 소개</b>
          </Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link className="navlink" href="/purchase">
            <b>회원가입</b>
          </Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link className="navlink" href="/purchase">
            <b>로그인</b>
          </Nav.Link>
        </Nav.Item>
      </Nav>
    </div>
  );
}
