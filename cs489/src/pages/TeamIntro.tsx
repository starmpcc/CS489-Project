import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { Button } from "react-bootstrap";
import { Container } from "./Home.styles";

import "./TestPage.css";

export function Teamintro() {
  const [review, setReview] = useState("");

  function checkReview() {}

  return (
    <Container>
      <label>
        <Container>
          <h2>We are team 6</h2>
        </Container>
      </label>
    </Container>
  );
}
