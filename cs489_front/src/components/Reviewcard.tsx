import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Nav, Image } from "react-bootstrap";
import BeautyStars from "beauty-stars";

import "../styles/css/Reviewcard.css";

export function Reviewcard(props: {
  reviewer: string;
  score: number;
  text: string;
  realscore: string;
}) {
  return (
    <div className="maincontainercard">
      <a>{props.reviewer}</a>
      <BeautyStars value={props.score} size="20px" />
      <a>{props.score}</a>
    </div>
  );
}
