import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { Button } from "react-bootstrap";
import { Container, MainContainer, LoadingText } from "./Home.styles";
import { Image } from "react-bootstrap";
import eye_img from "../assets/eye_img.png";
import hand_img from "../assets/hand_img.png";

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

  return (
    <MainContainer>
      <LoadingText>{message}</LoadingText>
      <Image src={hand_img} className="catch_img" />
      <Container>
        <label>
          <Link to="/test">
            <Button className="go_test">
              <b>Review Judgement</b>
            </Button>
          </Link>
          <Link to="/table">
            <Button className="go_timeline">
              <b>Alert Reviews</b>
            </Button>
          </Link>
        </label>
      </Container>
    </MainContainer>
  );
}
