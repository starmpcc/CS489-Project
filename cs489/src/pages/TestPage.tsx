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

    fetch("http://localhost:3001/test/" + review, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    }).then((response) => console.log(response.json()));
  }

  return (
    <Container>
      <label>
        <Container>
          <h2>검사하고 싶은 리뷰를 넣어주세요</h2>
        </Container>
        <input
          className="textinput"
          onChange={(x) => setReview(x.target.value)}
        />
        <Container>
          <Button className="submit_button" onClick={() => checkReview(review)}>
            <b>리뷰 체크하기</b>
          </Button>
        </Container>
        <h1>{rate}</h1>
      </label>
    </Container>
  );
}
