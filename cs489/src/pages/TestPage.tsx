import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { Button } from "react-bootstrap";

import "./TestPage.css";
import { Section, SectionTitle, TextArea } from "./TestPage.styles";
import { Container, Title } from "./Home.styles";

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
    console.log(response_score.score);
    setRate(response_score.score);
  }

  return (
    <Container>
      <Section>
        <Container>
          <Title>Put your Review</Title>
        </Container>
        <TextArea
          value={review}
          onChange={({ target }) => setReview(target.value)}
        />
      </Section>

      <Container>
        <Button className="submit_button" onClick={() => reviewCheck(review)}>
          <b>check review</b>
        </Button>
      </Container>
      <h1>This review is determined to be {rate}</h1>
    </Container>
  );
}
