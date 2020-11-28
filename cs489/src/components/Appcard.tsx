import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Nav, Image } from "react-bootstrap";

import "../styles/css/Reviewcard.css";

export function Appcard(props: { name: string }) {
  return (
    <div className="maincontainercard">
      <a>{props.name}</a>
    </div>
  );
}
