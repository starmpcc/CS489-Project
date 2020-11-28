import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { Button } from "react-bootstrap";
import { Container } from "./Home.styles";

import "./Home.css";

export function Home() {
  const [message, setMessage] = useState("loading...");
  const [review, setReview] = useState("");

  fetch("http://localhost:3001/api")
    .then((res) => res.json())
    .then((data) => setMessage(data.title));

  useEffect(() => {
    console.log("message...?", message);
  }, [message]);

  function checkReview() {}

  return (
    <Container>
      <h1>{message}</h1>
      <label>
        검사하고 싶은 리뷰를 넣어주세요
        <input onChange={(x) => setReview(x.target.value)} />
        <Button className="submit_button" onClick={() => checkReview()}>
          <b>리뷰 체크하기</b>
        </Button>
      </label>
    </Container>
  );
}
