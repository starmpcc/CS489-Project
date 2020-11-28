import React from "react";
import { Link } from "react-router-dom";

import app_img from "../assets/sample_app_img.png";
import { Nav, Image } from "react-bootstrap";
import BeautyStars from "beauty-stars";
import { Reviewcard } from "../components/Reviewcard";

import "../styles/css/Review.css";

export function Reviewpage() {
  const rate = 2;

  return (
    <div className="container">
      <div className="maincontainer">
        <div className="apptitle">
          <Image src={app_img} width="180px" height="180px"></Image>
          <div>
            <a>KAIST Portal</a>
            <div className="linktoappstore">
              <Link to="/hey">view at playstore</Link>
            </div>
          </div>
        </div>

        <div className="ratingcontainer">
          <a>Rating</a>
          <BeautyStars value={rate} />
          <h2>{rate}</h2>
        </div>
        <div className="graphcontainer">
          <div>
            <a>Rating Overtime</a>
          </div>
          <div>
            <h2>here should be graph</h2>
          </div>
        </div>
        <div className="reviewcontainer">
          <a>Review</a>
          <Reviewcard reviewer="mj" score={rate} text="sleepy" realscore="2" />
        </div>
      </div>
    </div>
  );
}
