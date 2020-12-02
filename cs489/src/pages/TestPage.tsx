import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { Button } from "react-bootstrap";
import { Container } from "./Home.styles";

import "./TestPage.css";

export function Testpage() {
  const [review, setReview] = useState("");
  const [rate, setRate] = useState("0");

  useEffect(() => {
    console.log("mz..?", rate);
  }, [rate]);

  function checkReview(review: String) {
    console.log(review);

    fetch("http://localhost:3001/test/" + review).then((response) =>
      console.log(response.json())
    );
  }

  async function reviewCheck(review: string) {
    console.log("check this:", review);
    const response = await fetch("http://localhost:3001/test/" + review);
    const response_score = await response.json();
    console.log(response_score);
  }

  return (
    <Container>
      <label>
        <Container>
          <h2>Put your review</h2>
        </Container>
        <input
          className="textinput"
          onChange={(x) => setReview(x.target.value)}
        />
        <Container>
          <Button className="submit_button" onClick={() => reviewCheck(review)}>
            <b>check review</b>
          </Button>
        </Container>
        <h1>{rate}</h1>
      </label>
    </Container>
  );
}
