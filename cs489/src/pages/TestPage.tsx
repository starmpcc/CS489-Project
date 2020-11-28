import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { Button } from "react-bootstrap";
import { Container } from "./Home.styles";

import "./TestPage.css";

export function Testpage() {
  const [review, setReview] = useState("");

  function checkReview() {}

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
          <Button className="submit_button" onClick={() => checkReview()}>
            <b>리뷰 체크하기</b>
          </Button>
        </Container>
      </label>
    </Container>
  );
}